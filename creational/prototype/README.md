# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/factory-method/README.md) · [Category](../README.md) · [Next](../../creational/singleton/README.md)

## Category

Creational

## Difficulty

Intermediate

## In One Sentence

Create an independent object by cloning an existing configured object.

## The Problem

A game needs several enemies based on a configured template whose concrete type the spawning code does not know.

## A Naive Solution

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Why This Becomes a Problem

Reconstructing a default Guard repeats setup and loses any custom equipment on the template.

## The Idea

Expose clone on Enemy. Guard copies its value members and returns a unique_ptr to an independent object.

## Real-World Analogy

Make a copy of a prepared document, then rename the copy without changing the original.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Participants

Enemy defines polymorphic cloning; Guard implements the copy; the client owns the clone and changes its name.

## Modern C++20 Example

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

## Example Output

```text
template: 2 items
gate guard: 2 items
```

## When to Use It

Use it when runtime objects carry useful configuration and clients should not reconstruct their concrete types.

## When NOT to Use It

Avoid it when ordinary value copying already expresses the requirement clearly.

## Advantages

Configured state can be reused without exposing each construction step to the client.

## Disadvantages / Trade-offs

Pointers require a deliberate deep-versus-shared-copy policy. Copying live sockets or unique external resources may be impossible or misleading.

## Technical Use Cases

Game entity templates and editable document presets fit; this example copies a string and vector with value semantics.

## Related Patterns

[abstract-factory](../abstract-factory/README.md) · [memento](../../behavioral/memento/README.md)

## Common Confusion

Memento restores a previous state of an object. Prototype creates another object; a copy constructor alone does not provide polymorphic cloning.

## Interview Question

If equipment becomes vector<shared_ptr<Item>>, will clone still be independent? Explain the aliasing.

## Mini Challenge

Add editable equipment and verify that changing the clone's equipment leaves the prototype unchanged.

## Quick Summary

- **Problem:** A game needs several enemies based on a configured template whose concrete type the spawning code does not know.
- **Solution:** Expose clone on Enemy. Guard copies its value members and returns a unique_ptr to an independent object.
- **Trade-off:** Pointers require a deliberate deep-versus-shared-copy policy. Copying live sockets or unique external resources may be impossible or misleading.
- **Remember:** Copy the setup, not the identity.

[Previous](../../creational/factory-method/README.md) · [Category](../README.md) · [Next](../../creational/singleton/README.md)
