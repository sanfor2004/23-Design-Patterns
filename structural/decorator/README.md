# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/composite/README.md) · [Category](../README.md) · [Next](../../structural/facade/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Beginner

## In One Sentence

Add behavior by wrapping an Object.

## Explain It Simply

A drink can have several optional extras. Each Decorator keeps the same Interface and adds its part before or after calling the wrapped Object.

## The Problem

A coffee order can add milk once or several times without inventing a drink class for every combination.

## Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why It Becomes a Problem

Separate combination classes duplicate base pricing and expand with every add-on.

## The Idea

Milk owns a Drink and delegates before adding its own description and price.

## Real-World Analogy

Each layer of gift wrapping surrounds the previous package while it remains a package.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Participants

Drink is the shared contract. Coffee supplies the base behavior. Milk wraps exactly one Drink. The client owns the outermost wrapper.

Canonical roles in this example:

- [`Component`](../../GLOSSARY.md#component) — The common contract exposed by leaves, groups, or wrappers. Here: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — The basic implementation before optional wrappers are added. Here: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — A wrapper that keeps the Component contract and adds a specific responsibility. Here: `Milk`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price_cents() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price_cents() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price_cents() const override { return inner_->price_cents() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price_cents() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use

Use it for optional, composable behavior that preserves the wrapped contract.

### Use cases

Streams with compression or encryption layers are a technical context; order and failure handling matter.

## When NOT to Use

Avoid it when a simple list of ingredients and a sum express the entire requirement; this example intentionally illustrates the structure.

## Advantages

Add-ons combine at [`runtime`](../../GLOSSARY.md#runtime), and the base [`implementation`](../../GLOSSARY.md#implementation) stays small.

## Trade-offs

Wrapper order can change behavior. Many tiny objects complicate debugging, and preserving the interface does not automatically preserve every semantic promise.

## Related Patterns

[Proxy](../proxy/README.md) · [Composite](../composite/README.md)

## Common Confusion

Proxy controls access to an object. Decorator adds responsibilities. A wrapper's shape alone does not tell you its intent.

## Terms to Remember

- `Decorator` — Add behavior by wrapping an object in another object with the same interface.
- `Component` — The common contract exposed by leaves, groups, or wrappers. Example: `Drink`.
- `Concrete Component` — The basic implementation before optional wrappers are added. Example: `Coffee`.
- `Concrete Decorator` — A wrapper that keeps the Component contract and adds a specific responsibility. Example: `Milk`.

## Interview Vocabulary

- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — Prefer collaborating objects when they express variation more clearly than extending a class hierarchy.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — Building a structure from parts that expose the same contract as the whole.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — Keep a module focused on one coherent reason to change.

## Interview Question

Would logging before encryption observe the same data as logging after encryption?

## Mini Challenge

Add a Syrup decorator costing 3, wrap it in two different orders, and explain the resulting descriptions.

## Check Yourself

1. Why can Milk wrap another Milk without knowing its concrete type?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** A coffee order can add milk once or several times without inventing a drink class for every combination.
- **Solution:** Milk owns a Drink and delegates before adding its own description and price.
- **Trade-off:** Wrapper order can change behavior. Many tiny objects complicate debugging, and preserving the interface does not automatically preserve every semantic promise.
- **Remember:** Same contract, another layer.

[Previous](../../structural/composite/README.md) · [Category](../README.md) · [Next](../../structural/facade/README.md)
