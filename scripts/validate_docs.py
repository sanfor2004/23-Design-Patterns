"""Check documentation links, coverage, and embedded examples without dependencies."""

from pathlib import Path
import re
import sys
import struct
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'ar-EG', 'zh-CN', 'it')
LANGUAGES = ('README.md', 'README.ar-EG.md', 'README.zh-CN.md', 'README.it.md')
CATEGORIES = {
    'creational': 'abstract-factory builder factory-method prototype singleton'.split(),
    'structural': 'adapter bridge composite decorator facade flyweight proxy'.split(),
    'behavioral': ('chain-of-responsibility command interpreter iterator mediator memento '
                   'observer state strategy template-method visitor').split(),
}
ENGLISH_SECTIONS = (
    'Category', 'Difficulty', 'In One Sentence', 'The Problem', 'A Naive Solution',
    'Why This Becomes a Problem', 'The Idea', 'Real-World Analogy', 'Structure',
    'Participants', 'Modern C++20 Example', 'Example Output', 'When to Use It',
    'When NOT to Use It', 'Advantages', 'Disadvantages / Trade-offs',
    'Technical Use Cases', 'Related Patterns', 'Common Confusion',
    'Interview Question', 'Mini Challenge', 'Quick Summary',
)


def main():
    errors = []
    documents = list(ROOT.glob('*.md')) + list((ROOT / 'assets').rglob('*.md'))
    for category in CATEGORIES:
        documents.extend((ROOT / category).rglob('*.md'))
    for document in documents:
        text = document.read_text(encoding='utf-8')
        prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
        if len(re.findall(r'^# ', prose, re.M)) != 1:
            errors.append(f'{document.relative_to(ROOT)}: expected one top-level heading')
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)\)', prose):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (document.parent / unquote(url.path)).resolve()
            if url.path.startswith('/') or not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(f'{document.relative_to(ROOT)}: broken local link {target}')

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
            headings = re.findall(r'^## (.+)$', text, re.M)
            if len(headings) != len(ENGLISH_SECTIONS):
                errors.append(f'{article.relative_to(ROOT)}: incomplete sections')
            if filename == 'README.md' and tuple(headings) != ENGLISH_SECTIONS:
                errors.append(f'{slug}: English template mismatch')
            if any(not section.strip() for section in re.split(r'^## .+\n', text, flags=re.M)[1:]):
                errors.append(f'{article.relative_to(ROOT)}: empty section')
            for language in LANGUAGES:
                if f']({language})' not in text:
                    errors.append(f'{article.relative_to(ROOT)}: missing language navigation')
            if f'](../{filename})' not in text:
                errors.append(f'{article.relative_to(ROOT)}: missing category navigation')
            for adjacent in (index - 1, index + 1):
                if 0 <= adjacent < len(ordered):
                    ac, ap = ordered[adjacent]
                    if f'](../../{ac}/{ap}/{filename})' not in text:
                        errors.append(f'{article.relative_to(ROOT)}: missing adjacent navigation')
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
            if guide == 'COMPARISONS' and len(re.findall(r'^## ', text, re.M)) != 8:
                errors.append(f'{path.name}: expected eight comparisons')
    for source in sources:
        slug = source.parent.parent.name
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
        for locale, filename in zip(LOCALES, LANGUAGES):
            article = source.parent.parent / filename
            if not article.is_file():
                continue
            text = article.read_text(encoding='utf-8')
            cpp_blocks = re.findall(r'^```cpp\n(.*?)^```', text, re.M | re.S)
            output_blocks = re.findall(r'^```text\n(.*?)^```', text, re.M | re.S)
            if code not in [block.strip() for block in cpp_blocks]:
                errors.append(f'{locale}/{slug}: complete C++ example differs from main.cpp')
            if output not in [block.strip() for block in output_blocks]:
                errors.append(f'{locale}/{slug}: expected output differs from expected.txt')
            if not diagram_blocks or diagram_blocks[0].strip() not in [block.strip() for block in output_blocks]:
                errors.append(f'{locale}/{slug}: diagram differs from diagram.md')
    for required in ('LICENSE', 'REFERENCES.md', 'CONTRIBUTING.md', 'CPP_EXAMPLES.md'):
        if not (ROOT / required).is_file():
            errors.append(f'Missing {required}')
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
    print(f'Validated {len(documents)} Markdown files, local links, and 23 examples in four languages.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
