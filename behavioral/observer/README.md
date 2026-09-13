# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Notify subscribers when something changes.

## The problem

Stock changes should update interested displays without making Stock know every concrete display type. Calling each concrete consumer directly couples the publisher to the current list and requires edits whenever consumers change.

## The idea

Several displays may need the latest stock quantity. Observer lets them subscribe, so Stock can send updates without hardcoding every display. Stock stores weak references to Listener objects and broadcasts updates to the live subscribers.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Observer example map](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

Stock is the subject, Listener the callback interface, Display a subscriber. The client owns subscribers; weak_ptr avoids extending their lifetime. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Stock is the subject, Listener the callback [`interface`](../../GLOSSARY.md#interface), Display a subscriber. The client owns subscribers; [`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr) avoids extending their [`lifetime`](../../GLOSSARY.md#lifetime).

Canonical roles in this example:

- [`Subject`](../../GLOSSARY.md#subject) — The publisher whose changes are announced to registered Observers. Here: `Stock`.
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — The callback contract implemented by subscribers. Here: `Listener`.
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — An Observer implementation that reacts to notifications. Here: `Display`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Stock:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def set(self, quantity):
        for listener in self.listeners.copy():
            listener(quantity)


def screen(quantity):
    print("Screen:", quantity)


def log(quantity):
    print("Log:", quantity)


def main():
    stock = Stock()
    stock.subscribe(screen)
    stock.subscribe(log)
    stock.set(4)
    stock.unsubscribe(screen)
    stock.set(0)
    stock.unsubscribe(log)
    stock.set(8)
    print("No subscribers")


if __name__ == "__main__":
    main()
```

### Python output

```text
Screen: 4
Log: 4
Log: 0
No subscribers
```

## C++20 example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
    auto screen = std::make_shared<Display>();
    auto log = std::make_shared<Display>();
    stock.subscribe(screen);
    stock.subscribe(log);
    stock.set(2);
}
```

### C++20 output

```text
Stock: 4
Expired listener skipped
Stock: 2
Stock: 2
```

## Compare the languages

Python stores callbacks with strong references and removes them explicitly. C++ uses `weak_ptr` and skips expired listeners. Neither version sends notifications asynchronously. A snapshot makes changes to subscriptions affect the next notification.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when one change has several independently registered consumers.

### Use cases

UI updates and local event subscriptions fit; delivery guarantees of distributed event systems are separate concerns.

**Cost:** Callback order and exceptions need a policy. This synchronous example propagates exceptions and is not thread-safe. Snapshotting tolerates subscription changes but does not prevent recursive notifications.

## Check yourself

1. How do unsubscribe in Python and an expired weak_ptr in C++ differ?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add two listeners, destroy one, and verify only the survivor receives later updates. Define an explicit unsubscribe operation.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
