# Launch validation

Executed 2026-09-12 against base revision `0fd233e` plus the current working tree.

## Build

A fresh MSVC 19.51 / Ninja Debug build in `build-launch` compiled all 23 C++20 examples. CTest reported **23/23 passed**, with expected-output comparisons. The initial attempt through the existing `build` configuration could not locate a compiler in the ordinary shell; using the Visual Studio developer environment and a fresh build directory resolved it. No C++ source was changed.

These tests cover the demonstrated output only. No performance, production readiness, or comprehensive input-coverage claim is made.

## Content and images

- All 12 requested post IDs have finished copy, attachments or text-only designations, publishing notes, evidence, and exact tag selections.
- DEV-01 is a complete article; HN-01 includes three titles and an author comment; IG-01 has six rendered slides and a caption; UP-01 has two lengths.
- Problem, method, and supported result were reviewed across every standalone post or sequence.
- All 10 campaign PNGs were opened and visually inspected, along with the updated repository preview. Logos and diagram geometry remain unchanged.
- The renderer checks viewport overflow, records actual PNG dimensions and sizes, and rejects a GitHub preview at or above 1 MB.
- No account publishing, scheduling, repository rename, or social-preview setting update occurred.

## Publication limits

GitHub image specifications, GitHub Traffic scope, Google people-first guidance, and HN Show HN guidance were checked through their official sources linked in this pack. No specific Reddit community has been selected; its rules and flair remain unverified. DEV native tags and other platform-specific upload requirements need a publishing-time check. X counts below are raw Unicode counts including literal URLs, spaces, numbering, and hashtags; platform-weighted limits were not independently verified.

The repository destination is taken from `git remote -v`. Browser retrieval returned a cache-miss error, so current public access was not independently verified. No trend, keyword-volume, or campaign metrics were available. Missing measurements remain empty in the CSV.

## Final checks

The repository validator passed: 176 Markdown files, local links, and 23 examples in four languages. All campaign Markdown links resolve. All 12 post IDs have required metadata; the DEV article contains 847 whitespace-separated words. The metrics CSV has 21 consistent columns. `git diff --check` passed (only line-ending conversion notices).

| Copy block | Raw characters |
| --- | --- |
| X-01 / 1 | 161 |
| X-01 / 2 | 181 |
| X-01 / 3 | 207 |
| X-01 / 4 | 218 |
| X-02 / 1 | 239 |
| X-03 / 1 | 223 |
| UP-01 / 1 | 235 |
| UP-01 / 2 | 690 |
