# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Provide one shared instance with global access.

## The problem

Two independently created metrics counters split a process-wide total. Making the constructor public gives each caller its own counter; the intended shared total is no longer shared.

## The idea

Several callers need the same metrics counter. Singleton controls creation, but that shared state also makes tests and dependencies harder to isolate. Hide construction, delete copying, and return a function-local static instance.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Singleton example map](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

Metrics controls its lifetime and stores the count. instance returns a non-owning reference; callers must never delete it. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Metrics controls its [`lifetime`](../../GLOSSARY.md#lifetime) and stores the count. instance returns a non-owning reference; callers must never delete it.

Canonical roles in this example:

- [`instance`](../../GLOSSARY.md#instance) — A particular object of a type. Here: `Metrics::instance()`.
- [`global state`](../../GLOSSARY.md#global-state) — Data reachable broadly across a program whose changes can affect distant code. Here: `Metrics::requests_`.
- [`thread-safe initialization`](../../GLOSSARY.md#thread-safe-initialization) — Initialization protected against concurrent construction; it does not make later operations thread-safe. Here: `static Metrics metrics`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Metrics:
    def __init__(self):
        self.requests = 0

    def record(self):
        self.requests += 1


# One shared instance under normal imports of this module.
# This expresses shared access, not a ban on creating other Metrics objects.
metrics = Metrics()


def main():
    first = metrics
    second = metrics
    first.record()
    second.record()
    print("Same instance:", first is second)
    print("Requests:", metrics.requests)


if __name__ == "__main__":
    main()
```

### Python output

```text
Same instance: True
Requests: 2
```

## C++20 example

```cpp
#include <iostream>

class Metrics {
    int requests_ = 0;
    Metrics() = default;
public:
    Metrics(const Metrics&) = delete;
    Metrics& operator=(const Metrics&) = delete;
    static Metrics& instance() {
        static Metrics metrics;
        return metrics;
    }
    void record() { ++requests_; }
    int requests() const { return requests_; }
};
int main() {
    auto& first = Metrics::instance();
    auto& second = Metrics::instance();
    first.record();
    second.record();
    std::cout << "Same instance: " << std::boolalpha << (&first == &second) << '\n';
    std::cout << "Requests: " << first.requests() << '\n';
}
```

### C++20 output

```text
Same instance: true
Requests: 2
```

## Compare the languages

Python uses one module-level instance, a common alternative to a strict Singleton Class. It does not prevent callers from constructing Metrics. C++ makes its constructor private and deletes copying. Shared mutable State complicates isolation in both; prefer passing a Dependency explicitly. Neither counter is thread-safe.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Consider it only when one instance really is a process-level invariant and its lifetime is appropriate.

### Use cases

A tiny single-threaded diagnostic counter demonstrates the mechanism, not a recommendation for production metrics architecture.

**Cost:** Global access hides dependencies and contaminates tests. Local-static initialization is thread-safe, but record is not; concurrent calls need synchronization. Shutdown order can also matter.

## Check yourself

1. How could one test leave counter State that affects the next test?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Refactor the example to inject a Metrics-like counter into two jobs, then test two isolated counters.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
