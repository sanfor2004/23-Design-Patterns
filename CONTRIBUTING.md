# Contributing

This repository is edited as Markdown, SVG, Python, and C++20. Keep the English and Egyptian Arabic lessons aligned when changing a pattern's behavior or explanation. Use plain language, define a technical term when it first matters, and keep claims tied to the runnable example.

Each pattern has `README.md`, `README.ar-EG.md`, `diagram.md`, and matching files in `python/` and `cpp/`. Both lessons show the complete Python example and its expected output first, then the complete C++20 example and its output. Explain the problem, follow the sketch through the actual code, compare the languages, state a meaningful cost, and ask questions readers can answer from the example. Keep the two source files and both `expected.txt` files synchronized with the displayed blocks.

The SVG map in `assets/diagrams/` should name the roles used by that example. Its arrows describe the demonstrated call flow, not ownership or inheritance. Update `diagram.md` and both lessons when changing it. Preserve the source license and image provenance.

Run the checks from the repository root:

```sh
python scripts/validate_docs.py
python scripts/test_python.py
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
```

`validate_docs.py` checks local Markdown links, two-language navigation, diagrams, full embedded code, and expected output against the runnable sources. The Python runner executes all 23 examples. CTest runs the C++20 suite. On Windows, use a Visual Studio developer shell for MSVC.

The website's English Markdown posts are maintained separately. Preserve their original `pubDate`, set an accurate `updatedDate` for substantive revisions, and run its pattern verifier and Astro build before publication. Keep the website's Python and C++ blocks synchronized with this repository.
