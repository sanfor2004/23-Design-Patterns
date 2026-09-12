# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/singleton/README.md) · [Category](../README.md) · [Next](../../structural/bridge/README.md)

## Category

Structural

## Difficulty

Beginner

## In One Sentence

Translate an existing interface into the one a client expects.

## The Problem

A dashboard expects Celsius but an existing sensor exposes Fahrenheit.

## A Naive Solution

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Why This Becomes a Problem

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

## When to Use It

Use it at a boundary to an existing API you cannot or should not change.

## When NOT to Use It

Avoid it when you own both sides and a single consistent interface would be simpler.

## Advantages

Unit conversion lives in one place, and the display can accept other Temperature implementations.

## Disadvantages / Trade-offs

An adapter can hide semantic mismatches if it only renames methods. The sensor must outlive the adapter because the reference does not own it.

## Technical Use Cases

Legacy API integration and unit conversion are common contexts; conversion accuracy and error handling still need explicit contracts.

## Related Patterns

[facade](../facade/README.md) · [bridge](../bridge/README.md)

## Common Confusion

Facade simplifies a subsystem. Adapter makes a specific existing interface compatible with a target contract.

## Interview Question

Can an adapter always preserve behavior if the source API is asynchronous and the target is synchronous?

## Mini Challenge

Test freezing and boiling points by allowing the legacy sensor to return configurable Fahrenheit values.

## Quick Summary

- **Problem:** A dashboard expects Celsius but an existing sensor exposes Fahrenheit.
- **Solution:** Implement Temperature around a borrowed LegacyThermometer and convert Fahrenheit to Celsius at the boundary.
- **Trade-off:** An adapter can hide semantic mismatches if it only renames methods. The sensor must outlive the adapter because the reference does not own it.
- **Remember:** Translate at the boundary.

[Previous](../../creational/singleton/README.md) · [Category](../README.md) · [Next](../../structural/bridge/README.md)
