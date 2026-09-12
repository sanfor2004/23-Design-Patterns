# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/prototype/README.md) · [Category](../README.md) · [Next](../../structural/adapter/README.md)

## Category

Creational

## Difficulty

Intermediate

## In One Sentence

Restrict a type to one accessible instance, accepting the cost of shared global state.

## The Problem

Two independently created metrics counters split a process-wide total.

## A Naive Solution

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Why This Becomes a Problem

Making the constructor public gives each caller its own counter; the intended shared total is no longer shared.

## The Idea

Hide construction, delete copying, and return a function-local static instance.

## Real-World Analogy

A small office has one visitor ledger, so every desk writes to the same book.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Singleton](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## Participants

Metrics controls its lifetime and stores the count. instance returns a non-owning reference; callers must never delete it.

## Modern C++20 Example

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

## Example Output

```text
Same instance: true
Requests: 2
```

## When to Use It

Consider it only when one instance really is a process-level invariant and its lifetime is appropriate.

## When NOT to Use It

Avoid it for convenient access to ordinary dependencies. Pass a Metrics reference explicitly when tests need isolation.

## Advantages

There is one well-defined initialization point and callers reach the same object.

## Disadvantages / Trade-offs

Global access hides dependencies and contaminates tests. Local-static initialization is thread-safe, but record is not; concurrent calls need synchronization. Shutdown order can also matter.

## Technical Use Cases

A tiny single-threaded diagnostic counter demonstrates the mechanism, not a recommendation for production metrics architecture.

## Related Patterns

[abstract-factory](../abstract-factory/README.md) · [facade](../../structural/facade/README.md)

## Common Confusion

One object managed by dependency injection is not necessarily a Singleton: uniqueness need not be enforced by the type.

## Interview Question

Does thread-safe initialization make requests_ thread-safe? Identify the separate operations involved.

## Mini Challenge

Refactor the example to inject a Metrics-like counter into two jobs, then test two isolated counters.

## Quick Summary

- **Problem:** Two independently created metrics counters split a process-wide total.
- **Solution:** Hide construction, delete copying, and return a function-local static instance.
- **Trade-off:** Global access hides dependencies and contaminates tests. Local-static initialization is thread-safe, but record is not; concurrent calls need synchronization. Shutdown order can also matter.
- **Remember:** One instance can still mean many problems.

[Previous](../../creational/prototype/README.md) · [Category](../README.md) · [Next](../../structural/adapter/README.md)
