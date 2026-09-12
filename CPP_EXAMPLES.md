# C++20 examples

Each pattern has a standalone `main.cpp` and an `expected.txt` containing its exact output. The same source and output appear in all four translations of the article.

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

## Build one pattern

Target names start with `pattern_` and replace hyphens in the directory name with underscores. After configuring:

```sh
cmake --build build --config Debug --target pattern_strategy
ctest --test-dir build -C Debug -R "^pattern_strategy$" --output-on-failure
```

For Factory Method, use `pattern_factory_method`. You can also compile an individual `main.cpp` directly with your compiler's C++20 option.

## Change an example

Keep `main.cpp`, `expected.txt`, and the complete example and expected-output blocks in all four articles synchronized. See [contribution instructions](CONTRIBUTING.md).
