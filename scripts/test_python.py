"""Run every Python example and compare stdout with its checked-in expected output."""

import difflib
from pathlib import Path
import subprocess
import sys

from validate_docs import CATEGORIES

ROOT = Path(__file__).resolve().parents[1]


def main():
    expected = {ROOT / category / slug / 'python' / 'main.py'
                for category, slugs in CATEGORIES.items() for slug in slugs}
    found = {source for category in CATEGORIES
             for source in (ROOT / category).glob('*/python/main.py')}
    if len(found) != 23 or found != expected:
        print(f'Expected exactly 23 named Python examples; found {len(found)}.', file=sys.stderr)
        for path in sorted(expected - found):
            print(f'Missing: {path.relative_to(ROOT)}', file=sys.stderr)
        for path in sorted(found - expected):
            print(f'Unexpected: {path.relative_to(ROOT)}', file=sys.stderr)
        return 1
    passed = 0
    for source in sorted(found):
        name = source.parent.parent.name
        try:
            wanted = source.with_name('expected.txt').read_text(encoding='utf-8')
            result = subprocess.run(
                [sys.executable, '-I', '-X', 'utf8', str(source)], cwd=source.parent,
                capture_output=True, text=True, encoding='utf-8', timeout=10)
        except (OSError, subprocess.TimeoutExpired) as error:
            print(f'FAIL {name}: {error}', file=sys.stderr)
            continue
        if result.returncode or result.stderr or result.stdout != wanted:
            print(f'FAIL {name}: exit={result.returncode}', file=sys.stderr)
            print(result.stderr, end='', file=sys.stderr)
            print(''.join(difflib.unified_diff(
                wanted.splitlines(True), result.stdout.splitlines(True),
                fromfile='expected', tofile='actual')), end='', file=sys.stderr)
        else:
            passed += 1
            print(f'PASS {name}')
    print(f'Python examples: {passed}/23 passed')
    return 0 if passed == 23 else 1


if __name__ == '__main__':
    sys.exit(main())
