# C++20 examples

Each pattern has a standalone `main.cpp` and an `expected.txt` containing its exact output. The same source and output appear in all four translations of the article.

Start with the [Python examples](PYTHON_EXAMPLES.md) to see the design intent, then use C++20 to study Ownership, Lifetime, and implementation trade-offs. Money examples use integer cents; their small demonstration values are not a production money or rounding policy.

Browse the [pattern catalog](README.md) for explanations and links to individual examples.

## Build and test all examples

Install CMake 3.20 or newer and a C++20 compiler (GCC, Clang, or MSVC). Run these commands from the repository root:

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
```

On Windows, use a Visual Studio Developer PowerShell or Developer Command Prompt with the C++ build tools installed. `--config Debug` and `-C Debug` select the configuration for generators such as Visual Studio; `CMAKE_BUILD_TYPE` selects it for single-configuration generators such as Ninja or Makefiles.

CTest runs each executable and compares stdout with `expected.txt`, normalizing Windows line endings. These tests check the demonstrated behavior; they do not cover every possible input or mini challenge.

CMake requires exactly 23 C++ examples and 23 Python examples, with companion README and expected-output files. Python is not needed to compile C++; run `python scripts/test_python.py` separately to test Python output. CI runs both sets plus documentation checks on Ubuntu with GCC and Clang, and on Windows with MSVC.

## Build one pattern

Target names start with `pattern_` and replace hyphens in the directory name with underscores. After configuring:

```sh
cmake --build build --config Debug --target pattern_strategy
ctest --test-dir build -C Debug -R "^pattern_strategy$" --output-on-failure
```

For Factory Method, use `pattern_factory_method`. You can also compile an individual `main.cpp` directly with your compiler's C++20 option.

## Change an example

Keep `main.cpp`, `expected.txt`, and the complete example and expected-output blocks in all four articles synchronized. See [contribution instructions](CONTRIBUTING.md).
