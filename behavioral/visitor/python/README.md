# Visitor in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Python uses separate `visit_book` and `visit_food` methods because it does not overload methods by parameter type. C++ uses overloads plus virtual dispatch. Both keep Tax outside the element types. Integer division truncates fractional cents; these sample rates and amounts avoid fractions and are not a tax policy.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
