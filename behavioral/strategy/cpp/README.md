# Strategy: C++20 example

[Explanation](../README.md) · [Source](main.cpp) · [Expected output](expected.txt)

From the repository root:

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug --target pattern_strategy
ctest --test-dir build -C Debug -R "^pattern_strategy$" --output-on-failure
```

See [compiler requirements and all-example instructions](../../../CPP_EXAMPLES.md). The output check runs the program and compares its stdout with `expected.txt`.

Start with the [Python example](../python/README.md) to see the same intent with less syntax.
