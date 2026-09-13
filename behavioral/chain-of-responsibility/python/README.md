# Chain of Responsibility in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Both versions use a validation chain: each Handler may reject, or pass onward; reaching the end means success. Other chains stop at the first Handler that can fulfill a request. Python holds successor references; C++ owns them with `unique_ptr`.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
