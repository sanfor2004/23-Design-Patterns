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

## Terminology policy

**Translate the explanation, not the terminology.** This applies to every language, including root READMEs, guides, tables, image alternatives, and individual pattern pages.

- Always use official English pattern names, including in headings and link labels. Use `Creational Pattern`, `Structural Pattern`, and `Behavioral Pattern` for the categories.
- Keep software-engineering terms in English: for example, `interface`, `implementation`, `coupling`, `composition`, `inheritance`, `ownership`, and `lifetime`.
- Keep canonical roles such as `Context`, `Concrete Strategy`, `Subject`, `Creator`, and `Receiver` in English. Map them to the actual example's identifiers without renaming its classes.
- Preserve code identifiers, C++ keywords, and standard-library names exactly. Use code formatting for identifiers and expressions where it helps reading. Never change fenced code as part of a terminology edit.
- Keep interview expressions such as `composition over inheritance`, `encapsulate what varies`, and `program to an interface, not an implementation` visible in English, with a short explanation in the current language.
- Explain an unfamiliar term at first use. Keep explanations brief and avoid redefining the same term throughout the page. Use [GLOSSARY.md](GLOSSARY.md) links for concepts a beginner may want to revisit.
- Keep ordinary prose natural. Verbs and everyday examples can remain localized. Do not replace a word in an analogy merely because it also has a technical meaning.
- Distinguish `State` (the pattern) from `state` (an object's current condition), and `lifecycle` (modeled stages) from `lifetime` (the interval in which an object exists).
- Include pattern-specific `Terms to Remember` and `Interview Vocabulary` entries in all four versions. Explain the same English terms in each language, including any constraints of the actual implementation.

The glossary is the shared reference for definitions. When adding an entry, supply English, Egyptian Arabic, Simplified Chinese, and Italian explanations. Check meaning and grammar manually; automated checks cannot establish translation quality.

### Egyptian Arabic and reading direction

Write the explanation naturally in Egyptian Arabic, and keep English terminology visually separate with inline code. Prefer an Arabic sentence opening, then introduce the English term beside its meaning. For example: «خلّي الـ `subclass` هي اللي تحدد الـ `concrete object` اللي هيتعمل.»

- Rewrite crowded sentences instead of inserting more English words into Arabic grammar. For example: «إزاي بننشئ الكائنات؟ المصطلح هنا هو `object creation`.»
- Keep official pattern names, architectural roles, and code identifiers in English. Keep a whole expression or code snippet inside one code span, including its parentheses or operators.
- English technical headings can remain English. In Arabic headings, isolate the English term in code or put it after the Arabic explanation in parentheses.
- Use short sentences for responsibilities and comparisons. Describe relationships in Arabic prose; put directional arrows in the English diagram instead of between mixed Arabic/English fragments.
- Check every `README.ar-EG.md`, the Arabic guides, and Egyptian Arabic glossary explanations for reading order. Review narrow-screen previews when available; source checks alone cannot guarantee GitHub mobile rendering.
- Preserve fenced C++ examples, output, and English diagrams exactly during prose formatting edits. Do not insert invisible direction-control characters into code or identifiers.

## Pattern document template

Use these English headings in all four pattern files. The body is written in the file's language. Existing technical use cases belong under `When to Use`, optionally in a `### Use cases` subsection.

```markdown
# Official English Pattern Name

## Category
## Difficulty
## In One Sentence
## The Problem
## Naive Solution
## Why It Becomes a Problem
## The Idea
## Real-World Analogy
## Structure
## Participants
## Modern C++20 Example
## Example Output
## When to Use
## When NOT to Use
## Advantages
## Trade-offs
## Related Patterns
## Common Confusion
## Terms to Remember
## Interview Vocabulary
## Interview Question
## Mini Challenge
## Quick Summary
```

In `Terms to Remember`, explain the pattern and map its canonical roles to the sample code. In `Interview Vocabulary`, explain relevant expressions and why they matter to this pattern; avoid a generic list pasted into every page.

## Report a mistake

Open an [issue](https://github.com/Sanfor2004/Design-Patterns-23/issues) or a pull request. Identify the pattern and language, quote the small section at issue, and explain the correction. For code failures, include the compiler version, command, and actual output. Translation corrections and clearer diagrams are welcome alongside code fixes.

## Examples and validation

The canonical runnable code lives in `<category>/<pattern>/cpp/main.cpp`. When changing it, update its `expected.txt` and the complete C++ and expected-output blocks in every translation.

An optional check uses Python 3.9 or newer and only the standard library:

```sh
python scripts/validate_docs.py
```

It checks local Markdown links and glossary anchors, all 23 English pattern names in all four languages, the required headings and vocabulary sections, four-language glossary entries, shared diagrams, and agreement between article examples and executable sources/expected outputs. Review localized prose separately for natural phrasing and technical accuracy.

For code changes, also [build the examples and run CTest](CPP_EXAMPLES.md). Preview edited Markdown in your editor or on GitHub, especially tables, diagrams, and Arabic text.

## Brand assets

Preserve the existing Sanfor2004 logo's geometry, orange color, and aspect ratio. See [asset provenance](assets/brand/README.md). Keep this repository self-contained; do not add dependencies on another local project.
