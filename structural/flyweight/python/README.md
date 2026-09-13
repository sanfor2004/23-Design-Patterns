# Flyweight in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

A small frozen dataclass makes the shared Python Glyph immutable through normal attribute assignment. C++ uses `shared_ptr<const Glyph>`. Both pools keep entries alive. This demonstrates sharing, not measured memory savings; the pool itself has a cost.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
