# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/state/README.md) · [Category](../README.md) · [Next](../../behavioral/template-method/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Beginner

## In One Sentence

Supply an interchangeable algorithm to the object that needs it.

## The Problem

Checkout totals need different shipping policies without mixing every policy into checkout logic.

## Naive Solution

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## Why It Becomes a Problem

One conditional is readable; repeated policy branches across checkout paths make adding and testing rules harder.

## The Idea

Checkout owns a ShippingRule callable and asks it for the fee. The caller selects the rule at construction.

## Real-World Analogy

Choose a route planner for walking or driving while the destination stays the same.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Participants

Checkout is the context, ShippingRule the behavioral contract, and lambdas implement standard and express fees.

Canonical roles in this example:

- [`Context`](../../GLOSSARY.md#context) — The object that uses a Strategy or delegates behavior to its current State. Here: `Checkout`.
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — The contract for interchangeable algorithms used by a Context. Here: `ShippingRule`.
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — A particular implementation of a Strategy interface, possibly a callable rather than a class. Here: `standard / express lambdas`.

## Modern C++20 Example

```cpp
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
```

## When to Use

Use it when algorithms vary independently and callers need to select a policy.

### Use cases

Pricing rules, ranking functions and retry policies are appropriate design contexts.

## When NOT to Use

Avoid it for one stable algorithm or a single readable conditional that has no real extension pressure.

## Advantages

Each policy can be tested independently while total calculation stays shared.

## Trade-offs

[`std::function`](../../GLOSSARY.md#stdfunction) (A type-erased wrapper that stores a callable with a chosen signature) adds [`type erasure`](../../GLOSSARY.md#type-erasure) (Hiding a concrete type behind a uniform runtime interface, as std::function does for callables) and may allocate; templates or a function pointer can be better with different constraints. Validate policy results if external code can return invalid fees.

## Related Patterns

[State](../state/README.md) · [Template Method](../template-method/README.md)

## Common Confusion

State represents [`lifecycle`](../../GLOSSARY.md#lifecycle) (The modeled stages and transitions of a domain entity, distinct from a C++ object's lifetime) and transitions; Strategy chooses an algorithm. Template Method customizes inherited steps rather than an injected callable.

## Terms to Remember

- `Strategy` — Supply an interchangeable algorithm to the object that needs it.
- `Context` — The object that uses a Strategy or delegates behavior to its current State. Example: `Checkout`.
- `Strategy interface` — The contract for interchangeable algorithms used by a Context. Example: `ShippingRule`.
- `Concrete Strategy` — A particular implementation of a Strategy interface, possibly a callable rather than a class. Example: `standard / express lambdas`.

## Interview Vocabulary

- [`interchangeable behavior`](../../GLOSSARY.md#interchangeable-behavior) — Different behaviors that can be supplied through the same contract.
- [`encapsulate an algorithm`](../../GLOSSARY.md#encapsulate-an-algorithm) — Put an algorithm behind an operation that hides its internal steps.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — Prefer collaborating objects when they express variation more clearly than extending a class hierarchy.
- [`runtime selection`](../../GLOSSARY.md#runtime-selection) — Choosing an implementation while the program is executing.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Parts know only the small contracts needed to cooperate, limiting change propagation.

## Interview Question

How would replacing std::function with a template parameter affect [`runtime`](../../GLOSSARY.md#runtime) (The period when a compiled program is executing) selection and compilation?

## Mini Challenge

Add free shipping for subtotals of at least 80 and test 79, 80 and 81.

## Quick Summary

- **Problem:** Checkout totals need different shipping policies without mixing every policy into checkout logic.
- **Solution:** Checkout owns a ShippingRule callable and asks it for the fee. The caller selects the rule at construction.
- **Trade-off:** std::function adds type erasure and may allocate; templates or a function pointer can be better with different constraints. Validate policy results if external code can return invalid fees.
- **Remember:** Same task, choose the algorithm.

[Previous](../../behavioral/state/README.md) · [Category](../README.md) · [Next](../../behavioral/template-method/README.md)
