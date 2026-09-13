# Project brief

## Identity and positioning

| Field | Finding |
| --- | --- |
| Name | 23 Design Patterns |
| Owner | Sanfor2004, supported by README, remote, and license |
| Type | Educational repository: GoF design patterns with standalone C++20 examples |
| Audience | Learners, C++ developers, and interview candidates deciding when a pattern helps |
| Problem | Pattern names and diagrams alone leave the motivation and observable behavior unexplained |
| Method | Problem → naive solution → pattern responsibilities → diagram → complete program → expected output → trade-offs and challenge |
| Result | Readers can inspect and run 23 examples and compare demonstrated output; four documentation languages cover the same examples |
| Stack | C++20, CMake 3.20+, CTest, Markdown, SVG; Python documentation validator |
| Status | Local examples compile and all 23 output tests passed in this execution; this campaign is prepared, not published |
| Destination | Configured remote: https://github.com/sanfor2004/Design-Patterns-23; browser retrieval failed, public availability not independently verified |
| Brand | Original Sanfor logo, orange #EE5712, paper #e7c99f, text #25170e; system Arial/Consolas fallbacks |
| Limits | No adoption, reach, search-volume, performance, or time-saving measurements; example tests do not cover all inputs |

## Messaging foundation

**One sentence:** 23 Design Patterns teaches the GoF patterns through concrete problems, diagrams, and runnable C++20 examples in four documentation languages.

**Two-sentence summary:** For learners who recognize a pattern but cannot yet explain when to use it, this repository traces the problem, the naive solution, and the resulting design. Readers can run a complete example, compare its output, and inspect the trade-offs before applying the idea elsewhere.

**Problem hook:** Knowing a pattern's name is easier than knowing when to use it.

**Implementation hook:** Give Checkout an interchangeable shipping rule, then trace the totals.

**Outcome hook:** Read one pattern, run its example, and explain what the abstraction changes.

**Problem / method / result:** Abstract pattern descriptions can hide motivation; linked explanations, diagrams, source, and expected output make the design traceable; readers can connect the Strategy shipping policy to three concrete totals.

**Primary CTA:** Explore the repository, start with Strategy, and run its example.

## Claim evidence

| Claim | Source |
| --- | --- |
| 23 GoF examples and four languages | [catalog](../README.md), category directories, [validator](../scripts/validate_docs.py) |
| Problem-first teaching and trade-offs | [Strategy article](../behavioral/strategy/README.md), [learning path](../LEARNING_PATH.md) |
| Callable shipping policy and printed totals | [main.cpp](../behavioral/strategy/cpp/main.cpp), [expected.txt](../behavioral/strategy/cpp/expected.txt) |
| Build and stdout comparison | [CMake](../CMakeLists.txt), [comparator](../cmake/CheckOutput.cmake), [build guide](../CPP_EXAMPLES.md) |
| Brand ownership and reuse boundary | [brand guide](../assets/brand/README.md), [license](../LICENSE) |
| Validation performed now | [validation report](validation.md) |

No personal origin story, community affiliation, hosted application, or user endorsement is inferred. First-person post copy is written for the documented owner to use.
