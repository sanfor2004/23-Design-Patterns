# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Create a new Object by copying a configured one.

## The problem

A game needs several enemies based on a configured template whose concrete type the spawning code does not know. Reconstructing a default Guard repeats setup and loses any custom equipment on the template.

## The idea

A game already has a guard with useful equipment. Prototype copies that setup so you can change the new guard without changing the original. Expose clone on Enemy. Guard copies its value members and returns a [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) to an independent object.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Prototype example map](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

Enemy defines polymorphic cloning; Guard implements the copy; the client owns the clone and changes its name. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Enemy defines polymorphic cloning; Guard implements the copy; the client owns the clone and changes its name.

Canonical roles in this example:

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — An object whose clone operation produces another object from its configured values. Here: `Guard`.
- [`deep copy`](../../GLOSSARY.md#deep-copy) — Copying owned nested data so the new object does not share that mutable data with the original. Here: `Guard::clone`.
- [`value semantics`](../../GLOSSARY.md#value-semantics) — Copies behave as independent values according to the type's contract. Here: `name_, equipment_`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Guard:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment

    def clone(self):
        return Guard(self.name, self.equipment.copy())

    def describe(self):
        print(self.name + ": " + ", ".join(self.equipment))


def main():
    prototype = Guard("template", ["shield", "spear"])
    guard = prototype.clone()
    guard.name = "gate guard"
    guard.equipment.append("helmet")
    prototype.describe()
    guard.describe()


if __name__ == "__main__":
    main()
```

### Python output

```text
template: shield, spear
gate guard: shield, spear, helmet
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

struct Enemy {
    virtual ~Enemy() = default;
    virtual std::unique_ptr<Enemy> clone() const = 0;
    virtual void rename(std::string name) = 0;
    virtual void describe() const = 0;
};
class Guard final : public Enemy {
    std::string name_ = "template";
    std::vector<std::string> equipment_{"shield", "spear"};
public:
    std::unique_ptr<Enemy> clone() const override { return std::make_unique<Guard>(*this); }
    void rename(std::string name) override { name_ = std::move(name); }
    void describe() const override {
        std::cout << name_ << ": " << equipment_.size() << " items\n";
    }
};
int main() {
    const Guard prototype;
    auto copy = prototype.clone();
    copy->rename("gate guard");
    prototype.describe();
    copy->describe();
}
```

### C++20 output

```text
template: 2 items
gate guard: 2 items
```

## Compare the languages

Assignment in Python shares an Object. This clone copies the equipment list explicitly; its strings are immutable. C++ copies the vector by value inside a polymorphic `clone`. Nested mutable data would require a deliberate deeper copy in Python; `copy.deepcopy` is an option, not a universal resource-copy policy.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when [`runtime`](../../GLOSSARY.md#runtime) objects carry useful configuration and clients should not reconstruct their concrete types.

### Use cases

Game entity templates and editable document presets fit; this example copies a string and std::vector with value semantics.

**Cost:** Pointers require a deliberate deep-versus-shared-copy policy. Copying live sockets or unique external resources may be impossible or misleading.

## Check yourself

1. Would assigning the original to a second variable create an independent copy?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add editable equipment and verify that changing the clone's equipment leaves the prototype unchanged.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
