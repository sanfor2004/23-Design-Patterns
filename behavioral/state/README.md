# State

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Let current State decide how an Object responds.

## The problem

A door reacts to the same button differently when open and closed; richer devices add locked or jammed states. A boolean toggle is enough for two states, but copying state conditionals across many events makes transitions inconsistent.

## The idea

Pressing a door button opens a closed door but closes an open one. State moves each response and transition into the Object representing that condition. Door delegates press to its current DoorState, and that state selects the next state.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![State example map](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

Door is the context. DoorState defines press and name. Open and Closed hold non-owning links to the next state; main keeps both alive longer than Door. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Door is the context. DoorState defines press and name. Open and Closed hold non-owning links to the next state; main keeps both alive longer than Door.

Canonical roles in this example:

- [`Context`](../../GLOSSARY.md#context) — The object that uses a Strategy or delegates behavior to its current State. Here: `Door`.
- [`State interface`](../../GLOSSARY.md#state-interface) — The contract through which a Context delegates state-dependent behavior. Here: `DoorState`.
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — An implementation defining behavior and transitions for one State. Here: `Open, Closed`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Closed:
    name = "closed"

    def press(self, door):
        door.state = Open()


class Open:
    name = "open"

    def press(self, door):
        door.state = Closed()


class Door:
    def __init__(self):
        self.state = Closed()

    def press(self):
        self.state.press(self)


if __name__ == "__main__":
    door = Door()
    print(door.state.name)
    door.press()
    print(door.state.name)
    door.press()
    print(door.state.name)
```

### Python output

```text
closed
open
closed
```

## C++20 example

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

### C++20 output

```text
closed
open
closed
```

## Compare the languages

Python creates a new stateless State Object for each transition. C++ reuses Open and Closed Objects through borrowed pointers; they must outlive Door. Both move transition behavior into State Objects. A boolean toggle is simpler for this tiny domain.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when state-dependent behavior and transitions spread across several operations.

### Use cases

Protocol sessions and device workflows are suitable contexts when transition rules are explicit.

**Cost:** Classes and [`lifetime`](../../GLOSSARY.md#lifetime) relationships add complexity. The demo keeps state objects outside Door, so transitions never destroy the currently executing state; larger designs must preserve that safety.

## Check yourself

1. Who chooses the next State when the door button is pressed?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add Locked so press keeps it locked; provide a separate unlock event and test the transition sequence.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
