# Builder in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Named Python arguments often make a Builder unnecessary. This example keeps separate construction steps to show the intent. `build` creates a fresh Request; as in C++, calling the public Request constructor directly bypasses Builder validation. A GoF Director is optional here, and the example builds one representation.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
