"""Check documentation links, coverage, and embedded examples without dependencies."""

from pathlib import Path
import re
import sys
import struct
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'ar-EG')
LANGUAGES = ('README.md', 'README.ar-EG.md')
CATEGORIES = {
    'creational': 'abstract-factory builder factory-method prototype singleton'.split(),
    'structural': 'adapter bridge composite decorator facade flyweight proxy'.split(),
    'behavioral': ('chain-of-responsibility command interpreter iterator mediator memento '
                   'observer state strategy template-method visitor').split(),
}
LESSON_HEADINGS = {
    'README.md': ('The problem', 'The idea', 'Trace the sketch', 'Read the code',
                  'Python example', 'C++20 example', 'Compare the languages', 'When it helps', 'Check yourself'),
    'README.ar-EG.md': ('المشكلة', 'الحل ببساطة', 'اقرأ الرسمة', 'امشِ مع الكود',
                        'Python example', 'C++20 example', 'قارن اللغتين', 'إمتى تستخدمه؟', 'جرّب تجاوب'),
}


def main():
    errors = []
    removed_locales = [*ROOT.rglob('*.zh-CN.md'), *ROOT.rglob('*.it.md')]
    if removed_locales:
        errors.append(f'Unsupported translated documents remain: {removed_locales}')
    def heading_anchors(text):
        counts = {}
        anchors = set()
        for heading in re.findall(r'^#+ (.+)$', text, re.M):
            heading = re.sub(r'[`*]', '', heading)
            slug = re.sub(r'[^\w -]', '', heading.lower()).replace(' ', '-')
            index = counts.get(slug, 0)
            counts[slug] = index + 1
            anchors.add(slug if index == 0 else f'{slug}-{index}')
        return anchors
    documents = list(ROOT.glob('*.md')) + list((ROOT / 'assets').rglob('*.md'))
    documents.extend((ROOT / 'Marketing').rglob('*.md'))
    for category in CATEGORIES:
        documents.extend((ROOT / category).rglob('*.md'))
    for document in documents:
        text = document.read_text(encoding='utf-8')
        if 'Mark' + 'ting/' in text or 'Mark' + 'ting\\' in text:
            errors.append(f'{document.relative_to(ROOT)}: obsolete Marketing path')
        prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
        if len(re.findall(r'^# ', prose, re.M)) != 1:
            errors.append(f'{document.relative_to(ROOT)}: expected one top-level heading')
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)\)', prose):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            resolved = (document.parent / unquote(url.path)).resolve() if url.path else document
            if url.path.startswith('/') or not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(f'{document.relative_to(ROOT)}: broken local link {target}')
            elif url.fragment and resolved.suffix == '.md':
                if unquote(url.fragment) not in heading_anchors(resolved.read_text(encoding='utf-8')):
                    errors.append(f'{document.relative_to(ROOT)}: missing anchor {target}')

    sources = sorted(source for category in CATEGORIES for source in (ROOT / category).glob('*/cpp/main.cpp'))
    if len(sources) != 23:
        errors.append(f'Expected 23 examples, found {len(sources)}')
    ordered = [(category, slug) for category, slugs in CATEGORIES.items() for slug in slugs]
    for category, slugs in CATEGORIES.items():
        if {p.name for p in (ROOT / category).iterdir() if p.is_dir()} != set(slugs):
            errors.append(f'{category}: unexpected pattern directory set')
    for filename in LANGUAGES:
        root_readme = ROOT / filename
        if not root_readme.is_file():
            errors.append(f'Missing root {filename}')
            continue
        catalog = root_readme.read_text(encoding='utf-8')
        for index, (category, slug) in enumerate(ordered):
            article = ROOT / category / slug / filename
            if f']({category}/{slug}/{filename})' not in catalog:
                errors.append(f'{filename}: missing localized link for {slug}')
            if not article.is_file():
                errors.append(f'Missing {article.relative_to(ROOT)}')
                continue
            text = article.read_text(encoding='utf-8')
            expected_name = ' '.join(word.capitalize() if word not in ('of',) else word for word in slug.split('-'))
            if not text.startswith(f'# {expected_name}\n'):
                errors.append(f'{article.relative_to(ROOT)}: pattern title must be {expected_name}')
            headings = tuple(re.findall(r'^## (.+)$', text, re.M))
            if headings != LESSON_HEADINGS[filename]:
                errors.append(f'{article.relative_to(ROOT)}: missing or out-of-order lesson sections')
            check = 'Check yourself' if filename == 'README.md' else 'جرّب تجاوب'
            questions = re.search(r'^## ' + re.escape(check) + r'\n(.*?)(?=^## |\Z)', text, re.M | re.S)
            if not questions or len(re.findall(r'^\d+\. ', questions[1], re.M)) != 3:
                errors.append(f'{article.relative_to(ROOT)}: expected three self-check questions')
            for target in ('python/main.py', 'cpp/main.cpp', 'diagram.md',
                           '../../LEARNING_PATH' + filename.removeprefix('README')):
                if f']({target})' not in text:
                    errors.append(f'{article.relative_to(ROOT)}: missing study navigation {target}')
            if any(not section.strip() for section in re.split(r'^## .+\n', text, flags=re.M)[1:]):
                errors.append(f'{article.relative_to(ROOT)}: empty section')
            for language in LANGUAGES:
                if f']({language})' not in text:
                    errors.append(f'{article.relative_to(ROOT)}: missing language navigation')
        for guide in ('CHEATSHEET', 'LEARNING_PATH', 'PATTERN_MAP', 'COMPARISONS'):
            path = ROOT / (guide + filename.removeprefix('README'))
            if not path.is_file():
                errors.append(f'Missing {path.name}')
                continue
            text = path.read_text(encoding='utf-8')
            if guide in ('CHEATSHEET', 'LEARNING_PATH'):
                for category, slug in ordered:
                    if f']({category}/{slug}/{filename})' not in text:
                        errors.append(f'{path.name}: missing {slug}')
            if guide == 'COMPARISONS' and len(re.findall(r'^## ', text, re.M)) < 7:
                errors.append(f'{path.name}: missing comparisons')
    for source in sources:
        slug = source.parent.parent.name
        for required in ('python/main.py', 'python/expected.txt', 'python/README.md', 'cpp/README.md'):
            if not (source.parent.parent / required).is_file():
                errors.append(f'{slug}: missing {required}')
        if not (ROOT / 'assets/diagrams' / f'{slug}.svg').is_file():
            errors.append(f'{slug}: missing SVG diagram')
        expected_file = source.with_name('expected.txt')
        if not expected_file.is_file():
            errors.append(f'{slug}: missing expected.txt')
            continue
        code = source.read_text(encoding='utf-8').strip()
        output = expected_file.read_text(encoding='utf-8').strip()
        diagram = source.parent.parent / 'diagram.md'
        if not diagram.is_file():
            errors.append(f'{slug}: missing diagram.md')
            diagram_blocks = []
        else:
            diagram_blocks = re.findall(r'^```text\n(.*?)^```', diagram.read_text(encoding='utf-8'), re.M | re.S)
            if any(re.search(r'[\u0600-\u06ff]', block) for block in diagram_blocks):
                errors.append(f'{slug}: diagram labels must remain English')
        for locale, filename in zip(LOCALES, LANGUAGES):
            article = source.parent.parent / filename
            if not article.is_file():
                continue
            text = article.read_text(encoding='utf-8')
            cpp_blocks = re.findall(r'^```cpp\n(.*?)^```', text, re.M | re.S)
            python_blocks = re.findall(r'^```python\n(.*?)^```', text, re.M | re.S)
            output_blocks = re.findall(r'^```text\n(.*?)^```', text, re.M | re.S)
            python_code = (source.parent.parent / 'python/main.py').read_text(encoding='utf-8').strip()
            python_output = (source.parent.parent / 'python/expected.txt').read_text(encoding='utf-8').strip()
            if python_code not in [block.strip() for block in python_blocks]:
                errors.append(f'{locale}/{slug}: complete Python example differs from main.py')
            if python_output not in [block.strip() for block in output_blocks]:
                errors.append(f'{locale}/{slug}: Python output differs from expected.txt')
            if code not in [block.strip() for block in cpp_blocks]:
                errors.append(f'{locale}/{slug}: complete C++ example differs from main.cpp')
            if output not in [block.strip() for block in output_blocks]:
                errors.append(f'{locale}/{slug}: expected output differs from expected.txt')
            if not diagram_blocks or diagram_blocks[0].strip() not in [block.strip() for block in output_blocks]:
                errors.append(f'{locale}/{slug}: diagram differs from diagram.md')
            if text.index('```python') > text.index('```cpp'):
                errors.append(f'{locale}/{slug}: Python must appear before C++')
    python_sources = [p for category in CATEGORIES for p in (ROOT / category).glob('*/python/main.py')]
    if len(python_sources) != 23:
        errors.append(f'Expected 23 Python examples, found {len(python_sources)}')
    if (ROOT / 'Mark' 'ting').exists():
        errors.append('Marketing directory still has its old misspelled name')
    for required in ('LICENSE', 'REFERENCES.md', 'CONTRIBUTING.md', 'CPP_EXAMPLES.md', 'PYTHON_EXAMPLES.md', 'GLOSSARY.md', 'Marketing/README.md'):
        if not (ROOT / required).is_file():
            errors.append(f'Missing {required}')
    glossary_path = ROOT / 'GLOSSARY.md'
    if glossary_path.is_file():
        glossary = glossary_path.read_text(encoding='utf-8')
        for entry in re.split(r'^## ', glossary, flags=re.M)[1:]:
            for label in ('Meaning', 'مصري'):
                if not re.search(r'\*\*'+label+r':\*\* \S', entry):
                    errors.append(f'Glossary entry {entry.splitlines()[0]}: missing {label} explanation')
    for svg in (ROOT / 'assets').rglob('*.svg'):
        try:
            ET.parse(svg)
        except ET.ParseError as error:
            errors.append(f'{svg.relative_to(ROOT)}: invalid SVG: {error}')
    preview = ROOT / 'assets/social-preview.png'
    if not preview.is_file():
        errors.append('Missing social preview')
    else:
        data = preview.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (1280, 640):
            errors.append('Social preview must be a 1280 x 640 PNG')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Validated {len(documents)} Markdown files: local links, navigation, diagrams, and two-language article coverage.')
    print('Implementation coverage: C++ 23/23; Python 23/23. Embedded sources and expected outputs match.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
