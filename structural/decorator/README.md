# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/composite/README.md) · [Category](../README.md) · [Next](../../structural/facade/README.md)

## Category

Structural

## Difficulty

Beginner

## In One Sentence

Add behavior by wrapping an object in another object with the same interface.

## The Problem

A coffee order can add milk once or several times without inventing a drink class for every combination.

## A Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why This Becomes a Problem

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

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price() const override { return inner_->price() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use It

Use it for optional, composable behavior that preserves the wrapped contract.

## When NOT to Use It

Avoid it when a simple list of ingredients and a sum express the entire requirement; this example intentionally illustrates the structure.

## Advantages

Add-ons combine at runtime, and the base implementation stays small.

## Disadvantages / Trade-offs

Wrapper order can change behavior. Many tiny objects complicate debugging, and preserving the interface does not automatically preserve every semantic promise.

## Technical Use Cases

Streams with compression or encryption layers are a technical context; order and failure handling matter.

## Related Patterns

[proxy](../proxy/README.md) · [composite](../composite/README.md)

## Common Confusion

Proxy controls access to an object. Decorator adds responsibilities. A wrapper's shape alone does not tell you its intent.

## Interview Question

Would logging before encryption observe the same data as logging after encryption?

## Mini Challenge

Add a Syrup decorator costing 3, wrap it in two different orders, and explain the resulting descriptions.

## Quick Summary

- **Problem:** A coffee order can add milk once or several times without inventing a drink class for every combination.
- **Solution:** Milk owns a Drink and delegates before adding its own description and price.
- **Trade-off:** Wrapper order can change behavior. Many tiny objects complicate debugging, and preserving the interface does not automatically preserve every semantic promise.
- **Remember:** Same contract, another layer.

[Previous](../../structural/composite/README.md) · [Category](../README.md) · [Next](../../structural/facade/README.md)
