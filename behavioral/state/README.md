# State

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/observer/README.md) · [Category](../README.md) · [Next](../../behavioral/strategy/README.md)

## Category

Behavioral

## Difficulty

Intermediate

## In One Sentence

Let an object's current state determine its response and transitions.

## The Problem

A door reacts to the same button differently when open and closed; richer devices add locked or jammed states.

## A Naive Solution

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Why This Becomes a Problem

A boolean toggle is enough for two states, but copying state conditionals across many events makes transitions inconsistent.

## The Idea

Door delegates press to its current DoorState, and that state selects the next state.

## Real-World Analogy

A vending machine treats an input differently before payment and after payment.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Participants

Door is the context. DoorState defines press and name. Open and Closed hold non-owning links to the next state; main keeps both alive longer than Door.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string_view>

class Door;
struct DoorState {
    virtual ~DoorState() = default;
    virtual void press(Door& door) const = 0;
    virtual std::string_view name() const = 0;
};
class Door {
    const DoorState* state_;
public:
    explicit Door(const DoorState& state) : state_(&state) {}
    void change(const DoorState& state) { state_ = &state; }
    void press() { state_->press(*this); }
    std::string_view name() const { return state_->name(); }
};
struct Open final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "open"; }
};
struct Closed final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "closed"; }
};
int main() {
    Open open;
    Closed closed;
    open.next = &closed;
    closed.next = &open;
    Door door{closed};
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
}
```

## Example Output

```text
closed
open
closed
```

## When to Use It

Use it when state-dependent behavior and transitions spread across several operations.

## When NOT to Use It

Avoid it for a trivial toggle or a small explicit enum transition table that stays readable.

## Advantages

Behavior is grouped by state and transitions can be inspected locally.

## Disadvantages / Trade-offs

Classes and lifetime relationships add complexity. The demo keeps state objects outside Door, so transitions never destroy the currently executing state; larger designs must preserve that safety.

## Technical Use Cases

Protocol sessions and device workflows are suitable contexts when transition rules are explicit.

## Related Patterns

[strategy](../strategy/README.md) · [observer](../observer/README.md)

## Common Confusion

Strategy is usually selected by a client to choose an algorithm. State represents lifecycle and may choose its own transitions.

## Interview Question

Who decides the next state here, and how is that different from choosing a shipping Strategy?

## Mini Challenge

Add Locked so press keeps it locked; provide a separate unlock event and test the transition sequence.

## Quick Summary

- **Problem:** A door reacts to the same button differently when open and closed; richer devices add locked or jammed states.
- **Solution:** Door delegates press to its current DoorState, and that state selects the next state.
- **Trade-off:** Classes and lifetime relationships add complexity. The demo keeps state objects outside Door, so transitions never destroy the currently executing state; larger designs must preserve that safety.
- **Remember:** Same event, different state, different response.

[Previous](../../behavioral/observer/README.md) · [Category](../README.md) · [Next](../../behavioral/strategy/README.md)
