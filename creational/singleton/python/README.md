# Singleton in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Python uses one module-level instance, a common alternative to a strict Singleton Class. It does not prevent callers from constructing Metrics. C++ makes its constructor private and deletes copying. Shared mutable State complicates isolation in both; prefer passing a Dependency explicitly. Neither counter is thread-safe.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
