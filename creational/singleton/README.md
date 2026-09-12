# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/prototype/README.md) · [Category](../README.md) · [Next](../../structural/adapter/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — A Design Pattern concerned with how objects are created and configured.

## Difficulty

Intermediate

## In One Sentence

Restrict a type to one accessible instance, accepting the cost of shared global state.

## The Problem

Two independently created metrics counters split a process-wide total.

## Naive Solution

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Why It Becomes a Problem

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

Metrics controls its [`lifetime`](../../GLOSSARY.md#lifetime) (The interval during which an object exists and may be used according to its rules) and stores the count. instance returns a non-owning reference; callers must never delete it.

Canonical roles in this example:

- [`instance`](../../GLOSSARY.md#instance) — A particular object of a type. Here: `Metrics::instance()`.
- [`global state`](../../GLOSSARY.md#global-state) — Data reachable broadly across a program whose changes can affect distant code. Here: `Metrics::requests_`.
- [`thread-safe initialization`](../../GLOSSARY.md#thread-safe-initialization) — Initialization protected against concurrent construction; it does not make later operations thread-safe. Here: `static Metrics metrics`.

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

## When to Use

Consider it only when one instance really is a process-level invariant and its lifetime is appropriate.

### Use cases

A tiny single-threaded diagnostic counter demonstrates the mechanism, not a recommendation for production metrics architecture.

## When NOT to Use

Avoid it for convenient access to ordinary dependencies. Pass a Metrics reference explicitly when tests need isolation.

## Advantages

There is one well-defined initialization point and callers reach the same object.

## Trade-offs

Global access hides dependencies and contaminates tests. Local-static initialization is thread-safe, but record is not; concurrent calls need synchronization. Shutdown order can also matter.

## Related Patterns

[Abstract Factory](../abstract-factory/README.md) · [Facade](../../structural/facade/README.md)

## Common Confusion

One object managed by [`dependency injection`](../../GLOSSARY.md#dependency-injection) (Supplying a dependency from outside instead of choosing or constructing it inside the consumer) is not necessarily a Singleton: uniqueness need not be enforced by the type.

## Terms to Remember

- `Singleton` — Restrict a type to one accessible instance, accepting the cost of shared global state.
- `instance` — A particular object of a type. Example: `Metrics::instance()`.
- `global state` — Data reachable broadly across a program whose changes can affect distant code. Example: `Metrics::requests_`.
- `thread-safe initialization` — Initialization protected against concurrent construction; it does not make later operations thread-safe. Example: `static Metrics metrics`.

## Interview Vocabulary

- [`dependency injection`](../../GLOSSARY.md#dependency-injection) — Supplying a dependency from outside instead of choosing or constructing it inside the consumer.
- [`testability`](../../GLOSSARY.md#testability) — How readily behavior can be isolated, exercised, and checked.
- [`lifetime`](../../GLOSSARY.md#lifetime) — The interval during which an object exists and may be used according to its rules.

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
