# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/mediator/README.md) · [Category](../README.md) · [Next](../../behavioral/observer/README.md)

## Category

Behavioral

## Difficulty

Intermediate

## In One Sentence

Save and restore an object's state without exposing snapshot internals.

## The Problem

An editor needs a checkpoint before an experimental edit.

## A Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why This Becomes a Problem

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
}
```

## Example Output

```text
Broken edit
Draft
```

## When to Use It

Use it for checkpoints where the originator can define a consistent state snapshot.

## When NOT to Use It

Avoid it when state is huge, resources cannot be restored, or recording inverse operations is cheaper.

## Advantages

Snapshot representation stays private to the originator, so the caretaker does not copy fields manually.

## Disadvantages / Trade-offs

Full snapshots cost memory and copying time. External effects such as files or network calls are not undone by restoring this string.

## Technical Use Cases

Editor checkpoints and simulation snapshots fit when the saved state is complete and consistent.

## Related Patterns

[command](../command/README.md) · [prototype](../../creational/prototype/README.md)

## Common Confusion

Command records an action; Memento records state. Prototype makes a separate object rather than restoring this one.

## Interview Question

If Editor later stores cursor position, who must change so restoration stays correct?

## Mini Challenge

Include a cursor position in Snapshot and test that both text and cursor return together.

## Quick Summary

- **Problem:** An editor needs a checkpoint before an experimental edit.
- **Solution:** Editor creates a Snapshot with private text and later reads it to restore itself.
- **Trade-off:** Full snapshots cost memory and copying time. External effects such as files or network calls are not undone by restoring this string.
- **Remember:** Remember state without exposing it.

[Previous](../../behavioral/mediator/README.md) · [Category](../README.md) · [Next](../../behavioral/observer/README.md)
