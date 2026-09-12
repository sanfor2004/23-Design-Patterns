# Decorator: C++20 example

[Explanation](../README.md) · [Source](main.cpp) · [Expected output](expected.txt)

From the repository root:

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug --target pattern_decorator
ctest --test-dir build -C Debug -R "^pattern_decorator$" --output-on-failure
```

See [compiler requirements and all-example instructions](../../../CPP_EXAMPLES.md). The output check runs the program and compares its stdout with `expected.txt`.
