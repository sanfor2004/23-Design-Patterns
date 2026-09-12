# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/adapter/README.md) · [Category](../README.md) · [Next](../../structural/composite/README.md)

## Category

Structural

## Difficulty

Intermediate

## In One Sentence

Separate two changing dimensions and connect them through composition.

## The Problem

Notices vary by urgency and by delivery channel; both dimensions need independent extensions.

## A Naive Solution

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## Why This Becomes a Problem

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

Notice is the abstraction, UrgentNotice refines it, Channel is the implementation contract, Email and Sms implement delivery.

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

## When to Use It

Use it when two axes of variation would otherwise produce a cross-product of subclasses.

## When NOT to Use It

Avoid it when only one small dimension changes and a function parameter already handles it.

## Advantages

A new channel serves existing notice types without adding every possible pair.

## Disadvantages / Trade-offs

The extra indirection requires a clear boundary; borrowed channels must outlive their notices.

## Technical Use Cases

Rendering APIs with independent shapes and backends, or notification types with channels, fit this structure.

## Related Patterns

[adapter](../adapter/README.md) · [strategy](../../behavioral/strategy/README.md)

## Common Confusion

Adapter reconciles an existing mismatch. Bridge is usually an intentional separation of independently evolving dimensions; Strategy focuses on interchangeable behavior.

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
