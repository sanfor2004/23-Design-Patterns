# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/adapter/README.md) · [Category](../README.md) · [Next](../../structural/composite/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Intermediate

## In One Sentence

Separate two changing dimensions and connect them through [`composition`](../../GLOSSARY.md#composition) (Building behavior by connecting objects that use or contain other objects).

## The Problem

Notices vary by urgency and by delivery channel; both dimensions need independent extensions.

## Naive Solution

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## Why It Becomes a Problem

A class for every urgency-channel pair multiplies combinations and repeats delivery logic.

## The Idea

Notice delegates delivery to a Channel. UrgentNotice changes message behavior without choosing a transport.

## Real-World Analogy

A remote control and its radio link can evolve separately while sharing a small protocol.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Bridge](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## Participants

Notice is the [`abstraction`](../../GLOSSARY.md#abstraction) (A view that exposes the operations a caller needs while hiding irrelevant details), UrgentNotice refines it, Channel is the [`implementation`](../../GLOSSARY.md#implementation) (The concrete code that fulfills an interface or performs an operation) contract, Email and Sms implement delivery.

Canonical roles in this example:

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — The high-level side of Bridge that delegates implementation work. Here: `Notice`.
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — A specialization of Abstraction independent of the implementation side. Here: `UrgentNotice`.
- [`Implementor`](../../GLOSSARY.md#implementor) — The contract used by a Bridge Abstraction for lower-level work. Here: `Channel`.
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — A particular implementation of the Implementor contract. Here: `Email, Sms`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string_view>

struct Channel {
    virtual ~Channel() = default;
    virtual void deliver(std::string_view text) const = 0;
};
struct Email final : Channel {
    void deliver(std::string_view text) const override { std::cout << "Email: " << text << '\n'; }
};
struct Sms final : Channel {
    void deliver(std::string_view text) const override { std::cout << "SMS: " << text << '\n'; }
};
class Notice {
protected:
    const Channel& channel_;
public:
    explicit Notice(const Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void send() const { channel_.deliver("status normal"); }
};
class UrgentNotice final : public Notice {
public:
    using Notice::Notice;
    void send() const override { channel_.deliver("URGENT: disk full"); }
};
int main() {
    const Email email;
    const Sms sms;
    Notice{email}.send();
    UrgentNotice{email}.send();
    UrgentNotice{sms}.send();
}
```

## Example Output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## When to Use

Use it when two axes of variation would otherwise produce a cross-product of subclasses.

### Use cases

Rendering APIs with independent shapes and backends, or notification types with channels, fit this structure.

## When NOT to Use

Avoid it when only one small dimension changes and a function parameter already handles it.

## Advantages

A new channel serves existing notice types without adding every possible pair.

## Trade-offs

The extra indirection requires a clear boundary; borrowed channels must outlive their notices.

## Related Patterns

[Adapter](../adapter/README.md) · [Strategy](../../behavioral/strategy/README.md)

## Common Confusion

Adapter reconciles an existing mismatch. Bridge is usually an intentional separation of independently evolving dimensions; Strategy focuses on interchangeable behavior.

## Terms to Remember

- `Bridge` — Separate two changing dimensions and connect them through composition.
- `Abstraction` — The high-level side of Bridge that delegates implementation work. Example: `Notice`.
- `Refined Abstraction` — A specialization of Abstraction independent of the implementation side. Example: `UrgentNotice`.
- `Implementor` — The contract used by a Bridge Abstraction for lower-level work. Example: `Channel`.
- `Concrete Implementor` — A particular implementation of the Implementor contract. Example: `Email, Sms`.

## Interview Vocabulary

- [`object composition`](../../GLOSSARY.md#object-composition) — Connecting objects to form a larger behavior or structure.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — Prefer collaborating objects when they express variation more clearly than extending a class hierarchy.
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — Put a changing design decision behind a stable boundary.

## Interview Question

If you add Push and ScheduledNotice, how many classes are needed with and without the bridge?

## Mini Challenge

Add a Push channel and reuse both notice classes without changing them.

## Quick Summary

- **Problem:** Notices vary by urgency and by delivery channel; both dimensions need independent extensions.
- **Solution:** Notice delegates delivery to a Channel. UrgentNotice changes message behavior without choosing a transport.
- **Trade-off:** The extra indirection requires a clear boundary; borrowed channels must outlive their notices.
- **Remember:** Two axes, one connection.

[Previous](../../structural/adapter/README.md) · [Category](../README.md) · [Next](../../structural/composite/README.md)
