# Python examples

Python reduces syntax overhead so you can follow each Design Pattern's intent. Each of the 23 patterns has a standalone `python/main.py`, a short README, and an `expected.txt`. No packages need installing. Use Python 3.10 or newer.

## Run and test

From the repository root:

```sh
python behavioral/strategy/python/main.py
python scripts/test_python.py
python scripts/validate_docs.py
```

The runner checks the exact set of 23 patterns, runs each in a separate process, and compares its output with the checked-in expectation. Only platform line endings are normalized. A missing example, timeout, error, or output mismatch fails the check.

## Study both implementations

Read the [Learning Path](LEARNING_PATH.md), predict the Python output, then change one input. Next read the [C++20 example](CPP_EXAMPLES.md) and the pattern's Python vs C++ notes. Design Patterns describe design intent, not syntax.

Compare responsibilities rather than exact output across languages. Some Python examples use different amounts or demonstrate extra cases. Each version has its own expected output. In both languages, monetary amounts are integer cents.

Python references keep Objects reachable, but resource cleanup still needs care. Use context managers for files and similar resources; garbage collection is not a substitute for a resource Lifetime policy. C++ makes Ownership more explicit with value semantics, references, smart pointers, and RAII.

These are small synchronous teaching examples. Their expected outputs cover selected useful cases, not every possible input. Keep a simple function, constructor, or `if` when it solves the problem clearly.

[Pattern catalog](README.md) · [Contributing](CONTRIBUTING.md)
