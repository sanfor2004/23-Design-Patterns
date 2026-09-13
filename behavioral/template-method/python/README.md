# Template Method in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Both versions use Inheritance to keep the sequence in `generate` and vary individual steps. C++ marks the steps virtual and keeps the workflow non-virtual. Python can override any method, so keeping the sequence fixed is a design convention. Injected callables are an alternative when Composition fits better.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
