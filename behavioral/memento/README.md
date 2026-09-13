# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/mediator/README.md) · [Category](../README.md) · [Next](../../behavioral/observer/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Intermediate

## In One Sentence

Save State now and restore it later.

## Explain It Simply

An editor needs a checkpoint before a risky edit. Memento holds that checkpoint while the editor controls how its state is saved and restored.

## The Problem

An editor needs a checkpoint before an experimental edit.

## Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why It Becomes a Problem

If the undo manager copies public fields itself, every new internal field requires changes in the manager.

## The Idea

Editor creates a Snapshot with private text and later reads it to restore itself.

## Real-World Analogy

A game checkpoint stores enough state to return to an earlier point without showing the player its data format.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Participants

Editor is the originator. Snapshot is the memento with private state. main is the caretaker holding it without inspecting its contents.

Canonical roles in this example:

- [`Originator`](../../GLOSSARY.md#originator) — The object that knows how to capture and restore its own state. Here: `Editor`.
- [`Caretaker`](../../GLOSSARY.md#caretaker) — The role that keeps a Memento without inspecting its private representation. Here: `main`.
- [`snapshot`](../../GLOSSARY.md#snapshot) — A captured representation of selected state at a point in time. Here: `Editor::Snapshot`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <utility>

class Editor {
    std::string text_;
public:
    class Snapshot {
        friend class Editor;
        std::string text_;
        explicit Snapshot(std::string text) : text_(std::move(text)) {}
    };
    void write(std::string text) { text_ = std::move(text); }
    Snapshot save() const { return Snapshot{text_}; }
    void restore(const Snapshot& snapshot) { text_ = snapshot.text_; }
    const std::string& text() const { return text_; }
};
int main() {
    Editor editor;
    editor.write("Draft");
    const auto checkpoint = editor.save();
    editor.write("Broken edit");
    std::cout << editor.text() << '\n';
    editor.restore(checkpoint);
    std::cout << editor.text() << '\n';
    editor.write("Another edit");
    editor.restore(checkpoint);
    std::cout << "Restore again: " << editor.text() << '\n';
}
```

## Example Output

```text
Broken edit
Draft
Restore again: Draft
```

## When to Use

Use it for checkpoints where the originator can define a consistent state snapshot.

### Use cases

Editor checkpoints and simulation snapshots fit when the saved state is complete and consistent.

## When NOT to Use

Avoid it when state is huge, resources cannot be restored, or recording inverse operations is cheaper.

## Advantages

Snapshot representation stays private to the originator, so the caretaker does not copy fields manually.

## Trade-offs

Full snapshots cost memory and copying time. External effects such as files or network calls are not undone by restoring this string.

## Related Patterns

[Command](../command/README.md) · [Prototype](../../creational/prototype/README.md)

## Common Confusion

Command records an action; Memento records state. Prototype makes a separate object rather than restoring this one.

## Terms to Remember

- `Memento` — Save and restore an object's state without exposing snapshot internals.
- `Originator` — The object that knows how to capture and restore its own state. Example: `Editor`.
- `Caretaker` — The role that keeps a Memento without inspecting its private representation. Example: `main`.
- `snapshot` — A captured representation of selected state at a point in time. Example: `Editor::Snapshot`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — Keeping representation and invariants behind controlled operations.
- [`undo`](../../GLOSSARY.md#undo) — Restoring an earlier logical result, using saved state or an inverse operation when possible.
- [`ownership`](../../GLOSSARY.md#ownership) — Responsibility for keeping a resource alive and eventually releasing it.

## Interview Question

If Editor later stores cursor position, who must change so restoration stays correct?

## Mini Challenge

Include a cursor position in Snapshot and test that both text and cursor return together.

## Check Yourself

1. Why must later edits leave a saved Snapshot unchanged?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** An editor needs a checkpoint before an experimental edit.
- **Solution:** Editor creates a Snapshot with private text and later reads it to restore itself.
- **Trade-off:** Full snapshots cost memory and copying time. External effects such as files or network calls are not undone by restoring this string.
- **Remember:** Remember state without exposing it.

[Previous](../../behavioral/mediator/README.md) · [Category](../README.md) · [Next](../../behavioral/observer/README.md)
