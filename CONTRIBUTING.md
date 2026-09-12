# Contributing

This repository is edited as plain Markdown, SVG, and C++20. Reading or editing the documentation requires no dependency installation or generated site.

## Documentation

- Edit articles under `<category>/<pattern>/`: `README.md`, `README.ar-EG.md`, `README.zh-CN.md`, and `README.it.md`.
- Keep all four translations aligned when changing technical explanations or examples.
- Use relative links ending in `.md` for documents. Keep the pattern's `diagram.md`, shared SVG under `assets/diagrams/`, and source under its `cpp/` directory aligned.
- Preserve each article's problem, naive solution, analogy, participants, trade-offs, related patterns, interview question, mini challenge, and summary.
- Update language catalogs, learning paths, cheat sheets, comparisons, and relationship guides when the corresponding content changes.
- Save text as UTF-8 and keep a single top-level heading per document.
- Write original explanations, code, exercises, and diagrams. Do not copy book passages or diagrams; cite conceptual references in [REFERENCES.md](REFERENCES.md).
- Keep English simple, Arabic naturally Egyptian, Chinese in natural Simplified Chinese, and Italian idiomatic. Preserve technical meaning, ownership details, and caveats in every translation.

## Report a mistake

Open an [issue](https://github.com/Sanfor2004/Design-Patterns-23/issues) or a pull request. Identify the pattern and language, quote the small section at issue, and explain the correction. For code failures, include the compiler version, command, and actual output. Translation corrections and clearer diagrams are welcome alongside code fixes.

## Examples and validation

The canonical runnable code lives in `<category>/<pattern>/cpp/main.cpp`. When changing it, update its `expected.txt` and the complete C++ and expected-output blocks in every translation.

An optional check uses Python 3.9 or newer and only the standard library:

```sh
python scripts/validate_docs.py
```

It checks local Markdown links and images, all 23 patterns in all four languages, shared diagrams, and agreement between article examples and executable sources/expected outputs.

For code changes, also [build the examples and run CTest](CPP_EXAMPLES.md). Preview edited Markdown in your editor or on GitHub, especially tables, diagrams, and Arabic text.

## Brand assets

Preserve the existing Sanfor2004 logo's geometry, orange color, and aspect ratio. See [asset provenance](assets/brand/README.md). Keep this repository self-contained; do not add dependencies on another local project.
