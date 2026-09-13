# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/iterator/README.md) · [Category](../README.md) · [Next](../../behavioral/memento/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Intermediate

## In One Sentence

Put coordination rules in one Object.

## Explain It Simply

A login button depends on two fields being filled. Mediator handles that rule so each field does not need to know the other field or the button.

## The Problem

Username and password fields jointly determine whether a login button is enabled.

## Naive Solution

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## Why It Becomes a Problem

If each field knows the other field and the button, UI rules spread across components and create mutual dependencies.

## The Idea

Fields report changed to LoginForm; the form checks both values and updates the button.

## Real-World Analogy

An air-traffic coordinator manages interactions so every pilot need not negotiate with every other pilot.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## Participants

Mediator defines notifications. Field reports changes. Button stores enabled state. LoginForm owns colleagues and coordinates them.

Canonical roles in this example:

- [`Colleague`](../../GLOSSARY.md#colleague) — An object whose interactions are coordinated by a Mediator. Here: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — An implementation that contains the coordination rules for its Colleagues. Here: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — A function or operation supplied to be called when another operation needs it. Here: `Mediator::changed`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <utility>

struct Mediator {
    virtual ~Mediator() = default;
    virtual void changed() = 0;
};
class Field {
    Mediator& mediator_;
    std::string value_;
public:
    explicit Field(Mediator& mediator) : mediator_(mediator) {}
    void set(std::string value) { value_ = std::move(value); mediator_.changed(); }
    bool empty() const { return value_.empty(); }
};
class Button {
    bool enabled_ = false;
public:
    void enable(bool enabled) { enabled_ = enabled; }
    bool enabled() const { return enabled_; }
};
class LoginForm final : public Mediator {
    Field username_;
    Field password_;
    Button submit_;
public:
    LoginForm() : username_(*this), password_(*this) {}
    LoginForm(const LoginForm&) = delete;
    LoginForm& operator=(const LoginForm&) = delete;
    void changed() override { submit_.enable(!username_.empty() && !password_.empty()); }
    void username(std::string value) { username_.set(std::move(value)); }
    void password(std::string value) { password_.set(std::move(value)); }
    bool ready() const { return submit_.enabled(); }
};
int main() {
    LoginForm form;
    form.username("learner");
    std::cout << "Ready: " << std::boolalpha << form.ready() << '\n';
    form.password("example");
    std::cout << "Ready: " << form.ready() << '\n';
    form.password("");
    std::cout << "Ready after clearing: " << form.ready() << '\n';
}
```

## Example Output

```text
Ready: false
Ready: true
Ready after clearing: false
```

## When to Use

Use it when interaction rules between several peers are becoming tangled.

### Use cases

Dialog coordination and workflow controllers fit; enabling a button is not authentication or password validation.

## When NOT to Use

Avoid it for one simple callback or when components have no meaningful coordination rules.

## Advantages

Fields no longer know siblings or the button, and the coordination rule has one home.

## Trade-offs

The mediator can become too large. LoginForm is noncopyable because its fields hold references back to it; copying would leave incorrect links.

## Related Patterns

[Observer](../observer/README.md) · [Facade](../../structural/facade/README.md)

## Common Confusion

Observer broadcasts a change to subscribers. Mediator encodes how particular peers should respond to one another; it can use Observer for notifications.

## Terms to Remember

- `Mediator` — Move coordination between peer objects into a dedicated object.
- `Colleague` — An object whose interactions are coordinated by a Mediator. Example: `Field, Button`.
- `Concrete Mediator` — An implementation that contains the coordination rules for its Colleagues. Example: `LoginForm`.
- `callback` — A function or operation supplied to be called when another operation needs it. Example: `Mediator::changed`.

## Interview Vocabulary

- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Parts know only the small contracts needed to cooperate, limiting change propagation.
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — Keeping distinct kinds of responsibility apart so they can change independently.
- [`god object`](../../GLOSSARY.md#god-object) — An object accumulating too many unrelated responsibilities.

## Interview Question

Why would an automatically generated copy constructor be dangerous for LoginForm?

## Mini Challenge

Add a terms checkbox and require all three conditions without teaching Field about the button.

## Check Yourself

1. Who decides whether the button is enabled when a field becomes empty?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** Username and password fields jointly determine whether a login button is enabled.
- **Solution:** Fields report changed to LoginForm; the form checks both values and updates the button.
- **Trade-off:** The mediator can become too large. LoginForm is noncopyable because its fields hold references back to it; copying would leave incorrect links.
- **Remember:** Peers talk through a coordinator.

[Previous](../../behavioral/iterator/README.md) · [Category](../README.md) · [Next](../../behavioral/memento/README.md)
