# Proxy in Python

[Explanation](../README.md) · [C++20](../cpp/README.md) · [All Python examples](../../../PYTHON_EXAMPLES.md)

From this directory, run with Python 3.10 or newer:

```sh
python main.py
```

Read [main.py](main.py), predict its output, then compare with [expected.txt](expected.txt).
From the repository root, verify all 23 examples with `python scripts/test_python.py`.

## Python vs C++

Python starts with `None`; C++ starts with an empty `unique_ptr`. Both create the real image on the first call. C++ uses `mutable` to cache inside a const operation. Neither version synchronizes concurrent calls or demonstrates access control; this is a virtual Proxy for lazy loading.

## Try it

Change one input and predict the result before running again. Use the pattern page's Mini Challenge and Check Yourself questions to explain what changed and why.
