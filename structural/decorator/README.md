# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Add behavior by wrapping an Object.

## The problem

A coffee order can add milk once or several times without inventing a drink class for every combination. Separate combination classes duplicate base pricing and expand with every add-on.

## The idea

A drink can have several optional extras. Each Decorator keeps the same Interface and adds its part before or after calling the wrapped Object. Milk owns a Drink and delegates before adding its own description and price.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Decorator example map](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

Drink is the shared contract. Coffee supplies the base behavior. Milk wraps exactly one Drink. The client owns the outermost wrapper. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Drink is the shared contract. Coffee supplies the base behavior. Milk wraps exactly one Drink. The client owns the outermost wrapper.

Canonical roles in this example:

- [`Component`](../../GLOSSARY.md#component) — The common contract exposed by leaves, groups, or wrappers. Here: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — The basic implementation before optional wrappers are added. Here: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — A wrapper that keeps the Component contract and adds a specific responsibility. Here: `Milk`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Coffee:
    def description(self):
        return "coffee"

    def price_cents(self):
        return 1000


class Milk:
    def __init__(self, inner):
        self.inner = inner

    def description(self):
        return self.inner.description() + " + milk"

    def price_cents(self):
        return self.inner.price_cents() + 200


if __name__ == "__main__":
    drink = Milk(Milk(Coffee()))
    print(f"{drink.description()}: {drink.price_cents()} cents")
```

### Python output

```text
coffee + milk + milk: 1400 cents
```

## C++20 example

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

### C++20 output

```text
coffee + milk + milk: 14
```

## Compare the languages

This is the GoF Object-wrapping Decorator, not Python function-decorator syntax. Python retains the wrapped drink; C++ transfers exclusive Ownership into each wrapper. Prices use integer cents. A list of ingredients is simpler if price addition is the whole problem.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for optional, composable behavior that preserves the wrapped contract.

### Use cases

Streams with compression or encryption layers are a technical context; order and failure handling matter.

**Cost:** Wrapper order can change behavior. Many tiny objects complicate debugging, and preserving the interface does not automatically preserve every semantic promise.

## Check yourself

1. Why can Milk wrap another Milk without knowing its concrete type?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a Syrup decorator costing 3, wrap it in two different orders, and explain the resulting descriptions.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
