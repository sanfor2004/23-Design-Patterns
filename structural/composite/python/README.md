# Composite in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Python uses a list of Objects that offer `bytes`; C++ uses a common Entry Interface and exclusive Ownership with `unique_ptr`. Python references allow accidental shared children or cycles. Keep this example a tree; garbage collection does not make recursive traversal of a cycle safe.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
