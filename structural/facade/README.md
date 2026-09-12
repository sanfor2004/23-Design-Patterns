# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/decorator/README.md) · [Category](../README.md) · [Next](../../structural/flyweight/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Beginner

## In One Sentence

Offer a small entry point to a subsystem's common workflow.

## The Problem

Every checkout caller must check stock, charge payment and request shipping in the right order.

## Naive Solution

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Why It Becomes a Problem

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

Canonical roles in this example:

- [`subsystem`](../../GLOSSARY.md#subsystem) — A group of cooperating services or objects within a larger system. Here: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — The contract of operations and observable behavior offered to a caller. Here: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — Code that uses an interface or collaborates with a pattern's objects. Here: `main`.

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

## When to Use

Use it when many callers need the same useful subset of a complicated subsystem.

### Use cases

SDK entry points and application service boundaries fit; the example has no real payment integration.

## When NOT to Use

Avoid it for a trivial pass-through that adds no meaningful simplification.

## Advantages

Callers depend on a smaller interface and a shared ordering rule.

## Trade-offs

The facade can grow into a god object. This example is not transactional: real payment and shipping failures require compensation or another consistency strategy.

## Related Patterns

[Adapter](../adapter/README.md) · [Mediator](../../behavioral/mediator/README.md)

## Common Confusion

Adapter changes compatibility. Facade reduces the surface area of a subsystem and need not implement an existing interface.

## Terms to Remember

- `Facade` — Offer a small entry point to a subsystem's common workflow.
- `subsystem` — A group of cooperating services or objects within a larger system. Example: `Stock, Payment, Shipping`.
- `interface` — The contract of operations and observable behavior offered to a caller. Example: `Checkout::buy`.
- `Client` — Code that uses an interface or collaborates with a pattern's objects. Example: `main`.

## Interview Vocabulary

- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — Keeping distinct kinds of responsibility apart so they can change independently.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Parts know only the small contracts needed to cooperate, limiting change propagation.
- [`trade-off`](../../GLOSSARY.md#trade-off) — A benefit gained at the cost of another desirable property.

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
