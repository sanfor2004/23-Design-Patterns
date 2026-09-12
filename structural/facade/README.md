# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/decorator/README.md) · [Category](../README.md) · [Next](../../structural/flyweight/README.md)

## Category

Structural

## Difficulty

Beginner

## In One Sentence

Offer a small entry point to a subsystem's common workflow.

## The Problem

Every checkout caller must check stock, charge payment and request shipping in the right order.

## A Naive Solution

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Why This Becomes a Problem

Direct calls let callers forget stock checks or duplicate orchestration inconsistently.

## The Idea

Checkout exposes buy and coordinates its internal services behind that operation.

## Real-World Analogy

A restaurant's front desk coordinates your booking without making you call every department.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Participants

Stock checks availability, Payment charges, Shipping dispatches, and Checkout presents the common workflow.

## Modern C++20 Example

```cpp
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount) const { std::cout << "Charged " << amount << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

## Example Output

```text
Charged 20
Dispatched
Unavailable
```

## When to Use It

Use it when many callers need the same useful subset of a complicated subsystem.

## When NOT to Use It

Avoid it for a trivial pass-through that adds no meaningful simplification.

## Advantages

Callers depend on a smaller interface and a shared ordering rule.

## Disadvantages / Trade-offs

The facade can grow into a god object. This example is not transactional: real payment and shipping failures require compensation or another consistency strategy.

## Technical Use Cases

SDK entry points and application service boundaries fit; the example has no real payment integration.

## Related Patterns

[adapter](../adapter/README.md) · [mediator](../../behavioral/mediator/README.md)

## Common Confusion

Adapter changes compatibility. Facade reduces the surface area of a subsystem and need not implement an existing interface.

## Interview Question

If charging succeeds but shipping fails, what guarantee can buy honestly provide?

## Mini Challenge

Add a simulated shipping failure and design an explicit refund result rather than silently returning success.

## Quick Summary

- **Problem:** Every checkout caller must check stock, charge payment and request shipping in the right order.
- **Solution:** Checkout exposes buy and coordinates its internal services behind that operation.
- **Trade-off:** The facade can grow into a god object. This example is not transactional: real payment and shipping failures require compensation or another consistency strategy.
- **Remember:** One front door to several services.

[Previous](../../structural/decorator/README.md) · [Category](../README.md) · [Next](../../structural/flyweight/README.md)
