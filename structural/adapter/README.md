# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/singleton/README.md) · [Category](../README.md) · [Next](../../structural/bridge/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Beginner

## In One Sentence

Make an existing Interface fit another.

## Explain It Simply

A sensor returns Fahrenheit, while the display expects Celsius. Adapter translates the call and value so neither side needs to change.

## The Problem

A dashboard expects Celsius but an existing sensor exposes Fahrenheit.

## Naive Solution

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Why It Becomes a Problem

Passing the raw number displays the wrong unit. Scattered conversion formulas duplicate a compatibility rule.

## The Idea

Implement Temperature around a borrowed LegacyThermometer and convert Fahrenheit to Celsius at the boundary.

## Real-World Analogy

A travel plug connects incompatible sockets; this adapter also translates the value's meaning.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Adapter](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## Participants

Temperature is the target interface. LegacyThermometer is the existing API. CelsiusAdapter borrows it; display uses only Temperature.

Canonical roles in this example:

- [`Target`](../../GLOSSARY.md#target) — The interface expected by the Client. Here: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — The existing object whose interface needs adaptation. Here: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — The contract of operations and observable behavior offered to a caller. Here: `Temperature`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <stdexcept>

class LegacyThermometer {
public:
    double fahrenheit() const { return 77.0; }
};
struct Temperature {
    virtual ~Temperature() = default;
    virtual double celsius() const = 0;
};
class CelsiusAdapter final : public Temperature {
    const LegacyThermometer& sensor_;
public:
    explicit CelsiusAdapter(const LegacyThermometer& sensor) : sensor_(sensor) {}
    double celsius() const override { return (sensor_.fahrenheit() - 32.0) * 5.0 / 9.0; }
};
void display(const Temperature& temperature) {
    std::cout << temperature.celsius() << " C\n";
}
int main() {
    const LegacyThermometer sensor;
    const CelsiusAdapter adapter{sensor};
    display(adapter);
}
```

## Example Output

```text
25 C
```

## When to Use

Use it at a boundary to an existing API you cannot or should not change.

### Use cases

Legacy API integration and unit conversion are common contexts; conversion accuracy and error handling still need explicit contracts.

## When NOT to Use

Avoid it when you own both sides and a single consistent interface would be simpler.

## Advantages

Unit conversion lives in one place, and the display can accept other Temperature implementations.

## Trade-offs

An adapter can hide semantic mismatches if it only renames methods. The sensor must outlive the adapter because the reference does not own it.

## Related Patterns

[Facade](../facade/README.md) · [Bridge](../bridge/README.md)

## Common Confusion

Facade simplifies a subsystem. Adapter makes a specific existing interface compatible with a target contract.

## Terms to Remember

- `Adapter` — Translate an existing interface into the one a client expects.
- `Target` — The interface expected by the Client. Example: `Temperature`.
- `Adaptee` — The existing object whose interface needs adaptation. Example: `LegacyThermometer`.
- `interface` — The contract of operations and observable behavior offered to a caller. Example: `Temperature`.

## Interview Vocabulary

- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — Depend on the promised contract instead of a particular concrete implementation.
- [`delegation`](../../GLOSSARY.md#delegation) — An object asks a collaborator to perform part of its work.
- [`lifetime`](../../GLOSSARY.md#lifetime) — The interval during which an object exists and may be used according to its rules.

## Interview Question

Can an adapter always preserve behavior if the source API is asynchronous and the target is synchronous?

## Mini Challenge

Test freezing and boiling points by allowing the legacy sensor to return configurable Fahrenheit values.

## Check Yourself

1. Who converts the units, and who keeps the sensor alive?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** A dashboard expects Celsius but an existing sensor exposes Fahrenheit.
- **Solution:** Implement Temperature around a borrowed LegacyThermometer and convert Fahrenheit to Celsius at the boundary.
- **Trade-off:** An adapter can hide semantic mismatches if it only renames methods. The sensor must outlive the adapter because the reference does not own it.
- **Remember:** Translate at the boundary.

[Previous](../../creational/singleton/README.md) · [Category](../README.md) · [Next](../../structural/bridge/README.md)
