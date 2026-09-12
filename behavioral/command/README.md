# Command

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/chain-of-responsibility/README.md) · [Category](../README.md) · [Next](../../behavioral/interpreter/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Intermediate

## In One Sentence

Turn an action into an object that can be stored and invoked later.

## The Problem

An editor must apply changes and undo the last action without teaching the toolbar every document operation.

## Naive Solution

```cpp
document.text += " world"; // no object records how to undo
```

## Why It Becomes a Problem

Direct mutation performs the edit but leaves no record of the action or its prior state.

## The Idea

Append captures a receiver and argument; execute stores the old text, and undo restores it. History owns executed commands.

## Real-World Analogy

A restaurant order ticket records an action independently of the waiter who submits it.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Command](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## Participants

Command defines execute and undo. Append changes a borrowed Document. History invokes and retains commands in stack order.

Canonical roles in this example:

- [`Receiver`](../../GLOSSARY.md#receiver) — The object that performs the work requested by a Command. Here: `Document`.
- [`Invoker`](../../GLOSSARY.md#invoker) — The role that starts or stores Commands without knowing each operation's details. Here: `History`.
- [`Concrete Command`](../../GLOSSARY.md#concrete-command) — A Command implementation that binds a Receiver and an action. Here: `Append`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Document { std::string text; };
struct Command {
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};
class Append final : public Command {
    Document& document_;
    std::string suffix_;
    std::string before_;
public:
    Append(Document& document, std::string suffix) : document_(document), suffix_(std::move(suffix)) {}
    void execute() override { before_ = document_.text; document_.text += suffix_; }
    void undo() override { document_.text = before_; }
};
class History {
    std::vector<std::unique_ptr<Command>> commands_;
public:
    void run(std::unique_ptr<Command> command) {
        if (!command) throw std::invalid_argument("Missing command");
        commands_.push_back(std::move(command));
        try { commands_.back()->execute(); }
        catch (...) { commands_.pop_back(); throw; }
    }
    void undo() {
        if (commands_.empty()) return;
        commands_.back()->undo();
        commands_.pop_back();
    }
};
int main() {
    Document document{"Hello"};
    History history;
    history.run(std::make_unique<Append>(document, " world"));
    std::cout << document.text << '\n';
    history.undo();
    std::cout << document.text << '\n';
}
```

## Example Output

```text
Hello world
Hello
```

## When to Use

Use it for deferred actions, queues, macros or undo histories.

### Use cases

Editor actions and job queues fit, but durable queues need serialization and idempotency beyond this example.

## When NOT to Use

Avoid it for a one-off function call with no need to store or schedule intent.

## Advantages

The invoker does not depend on concrete operations and can retain their execution history.

## Trade-offs

Saving whole text costs memory. This single-threaded demo assumes edits go through History and Document outlives it; external edits would invalidate undo expectations.

## Related Patterns

[Memento](../memento/README.md) · [Chain of Responsibility](../chain-of-responsibility/README.md)

## Common Confusion

Memento stores state; Command stores an action and may use a snapshot to undo it. Not every command is reversible.

## Terms to Remember

- `Command` — Turn an action into an object that can be stored and invoked later.
- `Receiver` — The object that performs the work requested by a Command. Example: `Document`.
- `Invoker` — The role that starts or stores Commands without knowing each operation's details. Example: `History`.
- `Concrete Command` — A Command implementation that binds a Receiver and an action. Example: `Append`.

## Interview Vocabulary

- [`undo`](../../GLOSSARY.md#undo) — Restoring an earlier logical result, using saved state or an inverse operation when possible.
- [`encapsulation`](../../GLOSSARY.md#encapsulation) — Keeping representation and invariants behind controlled operations.
- [`exception safety`](../../GLOSSARY.md#exception-safety) — The guarantees an operation preserves if it fails by throwing an exception.

## Interview Question

Can sending an email be undone in the same sense as restoring a string? Define compensation versus reversal.

## Mini Challenge

Add a second append, undo twice, and verify the empty-history call is harmless.

## Quick Summary

- **Problem:** An editor must apply changes and undo the last action without teaching the toolbar every document operation.
- **Solution:** Append captures a receiver and argument; execute stores the old text, and undo restores it. History owns executed commands.
- **Trade-off:** Saving whole text costs memory. This single-threaded demo assumes edits go through History and Document outlives it; external edits would invalidate undo expectations.
- **Remember:** An action you can keep.

[Previous](../../behavioral/chain-of-responsibility/README.md) · [Category](../README.md) · [Next](../../behavioral/interpreter/README.md)
