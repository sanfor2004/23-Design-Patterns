# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/memento/README.md) · [Category](../README.md) · [Next](../../behavioral/state/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Beginner

## In One Sentence

Notify subscribed objects when something they follow changes.

## The Problem

Stock changes should update interested displays without making Stock know every concrete display type.

## Naive Solution

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## Why It Becomes a Problem

Calling each concrete consumer directly couples the publisher to the current list and requires edits whenever consumers change.

## The Idea

Stock stores weak references to Listener objects and broadcasts updates to the live subscribers.

## Real-World Analogy

Subscribers receive a shop's stock alert only while their subscription remains active.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Observer](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## Participants

Stock is the subject, Listener the callback [`interface`](../../GLOSSARY.md#interface) (The contract of operations and observable behavior offered to a caller), Display a subscriber. The client owns subscribers; [`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr) (A non-owning observer of shared ownership; lock attempts to obtain a temporary shared_ptr) avoids extending their [`lifetime`](../../GLOSSARY.md#lifetime) (The interval during which an object exists and may be used according to its rules).

Canonical roles in this example:

- [`Subject`](../../GLOSSARY.md#subject) — The publisher whose changes are announced to registered Observers. Here: `Stock`.
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — The callback contract implemented by subscribers. Here: `Listener`.
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — An Observer implementation that reacts to notifications. Here: `Display`.

## Modern C++20 Example

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
}
```

## Example Output

```text
Stock: 4
Expired listener skipped
```

## When to Use

Use it when one change has several independently registered consumers.

### Use cases

UI updates and local event subscriptions fit; delivery guarantees of distributed event systems are separate concerns.

## When NOT to Use

Avoid it for one fixed dependency where a direct call is clearer, or when strict transactional consistency is required.

## Advantages

Subscribers can come and go without changing publisher code.

## Trade-offs

Callback order and exceptions need a policy. This synchronous example propagates exceptions and is not thread-safe. Snapshotting tolerates subscription changes but does not prevent recursive notifications.

## Related Patterns

[Mediator](../mediator/README.md) · [State](../state/README.md)

## Common Confusion

Mediator defines coordination rules among known peers. Observer broadcasts notifications and does not prescribe the subscribers' relationship.

## Terms to Remember

- `Observer` — Notify subscribed objects when something they follow changes.
- `Subject` — The publisher whose changes are announced to registered Observers. Example: `Stock`.
- `Observer interface` — The callback contract implemented by subscribers. Example: `Listener`.
- `Concrete Observer` — An Observer implementation that reacts to notifications. Example: `Display`.

## Interview Vocabulary

- [`one-to-many dependency`](../../GLOSSARY.md#one-to-many-dependency) — One source has multiple dependents that react to its changes.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Parts know only the small contracts needed to cooperate, limiting change propagation.
- [`subscription lifetime`](../../GLOSSARY.md#subscription-lifetime) — The interval in which a listener is registered and eligible for notification.

## Interview Question

Why use std::weak_ptr for stored listeners but lock it into [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) (A smart pointer sharing ownership; the managed object is released when the last owning reference disappears) during the callback?

## Mini Challenge

Add two listeners, destroy one, and verify only the survivor receives later updates. Define an explicit unsubscribe operation.

## Quick Summary

- **Problem:** Stock changes should update interested displays without making Stock know every concrete display type.
- **Solution:** Stock stores weak references to Listener objects and broadcasts updates to the live subscribers.
- **Trade-off:** Callback order and exceptions need a policy. This synchronous example propagates exceptions and is not thread-safe. Snapshotting tolerates subscription changes but does not prevent recursive notifications.
- **Remember:** Publish a change, let subscribers react.

[Previous](../../behavioral/memento/README.md) · [Category](../README.md) · [Next](../../behavioral/state/README.md)
