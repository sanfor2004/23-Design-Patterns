# Bridge in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Both examples use Composition to separate notice type from delivery channel. Python retains a channel reference and relies on `deliver`; C++ borrows an Object implementing Channel, so its Lifetime must cover the notice.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
