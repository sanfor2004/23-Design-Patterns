# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../creational/builder/README.md) · [Category](../README.md) · [Next](../../creational/prototype/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — A Design Pattern concerned with how objects are created and configured.

## Difficulty

Beginner

## In One Sentence

Let a subclass choose what a shared workflow creates.

## Explain It Simply

An alert job always sends the same message, but the delivery method varies. The workflow calls a Factory Method; each subclass creates its own Sender.

## The Problem

An alert job always sends a completion message, but different environments need different senders.

## Naive Solution

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Why It Becomes a Problem

Hardcoding EmailSender inside run couples the workflow to email; copying run for console delivery duplicates the workflow.

This is `tight coupling`: the workflow knows a concrete sender type, so changing delivery can require changing that workflow.

## The Idea

Put the workflow in AlertJob and call the overridable make_sender creation step.

## Real-World Analogy

A delivery office follows the same dispatch process while each branch chooses its vehicle.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Participants

AlertJob owns the workflow. EmailJob and ConsoleJob override creation. Sender supplies the operation and the returned [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) owns the product.

Canonical roles in this example:

- [`Creator`](../../GLOSSARY.md#creator) — The base role that owns a workflow and declares its creation operation. Here: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — A Creator subclass that supplies a particular Product. Here: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — The contract of an object returned by creation code. Here: `Sender`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(std::string_view message) const = 0;
};
struct EmailSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Email: " << message << '\n'; }
};
struct ConsoleSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Console: " << message << '\n'; }
};
class AlertJob {
protected:
    virtual std::unique_ptr<Sender> make_sender() const = 0;
public:
    virtual ~AlertJob() = default;
    void run() const {
        const auto sender = make_sender();
        sender->send("build complete");
    }
};
class EmailJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<EmailSender>(); }
};
class ConsoleJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<ConsoleSender>(); }
};
int main() {
    EmailJob{}.run();
    ConsoleJob{}.run();
}
```

## Example Output

```text
Email: build complete
Console: build complete
```

## When to Use

Use it when an existing [`inheritance`](../../GLOSSARY.md#inheritance)-based workflow needs an extensible creation step.

### Use cases

Pluggable exporters and environment-specific job runners are plausible applications; the senders here only print text.

## When NOT to Use

Avoid it when passing a ready-made Sender into a function is sufficient; inheritance would add needless structure.

## Advantages

The workflow stays in one place while product selection varies.

## Trade-offs

Each new selection may need a subclass. Calling virtual creation from a base constructor would not dispatch to a derived override as intended.

## Related Patterns

[Abstract Factory](../abstract-factory/README.md) · [Template Method](../../behavioral/template-method/README.md)

## Common Confusion

A free function containing a switch is a simple factory, not this GoF subclass extension point. Abstract Factory instead coordinates a family.

## Terms to Remember

- `Factory Method` — Let a subclass choose the object used by a shared workflow.
- `Creator` — The base role that owns a workflow and declares its creation operation. Example: `AlertJob`.
- `Concrete Creator` — A Creator subclass that supplies a particular Product. Example: `EmailJob, ConsoleJob`.
- `Product` — The contract of an object returned by creation code. Example: `Sender`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Choosing a concrete type and establishing an object's initial values and lifetime.
- [`tight coupling`](../../GLOSSARY.md#tight-coupling) — Parts depend heavily on each other's concrete details, so changes tend to spread.
- [`inheritance`](../../GLOSSARY.md#inheritance) — Defining a derived class from a base class to reuse or specialize its contract and implementation.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — Aim for open for extension, closed for modification at a useful, chosen boundary.

## Interview Question

Why does run call make_sender after construction rather than from AlertJob's constructor?

## Mini Challenge

Add a FileJob with a sender that writes to a temporary file, and verify its contents.

## Check Yourself

1. Where does Sender selection happen, and what workflow stays shared?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** An alert job always sends a completion message, but different environments need different senders.
- **Solution:** Put the workflow in AlertJob and call the overridable make_sender creation step.
- **Trade-off:** Each new selection may need a subclass. Calling virtual creation from a base constructor would not dispatch to a derived override as intended.
- **Remember:** Keep the workflow; override creation.

[Previous](../../creational/builder/README.md) · [Category](../README.md) · [Next](../../creational/prototype/README.md)
