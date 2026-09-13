# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Let two kinds of variation change separately.

## The problem

Notices vary by urgency and by delivery channel; both dimensions need independent extensions. A class for every urgency-channel pair multiplies combinations and repeats delivery logic.

## The idea

Notices can be normal or urgent, and delivery can use email or SMS. Bridge connects a notice to a channel instead of needing a Class for every combination. Notice delegates delivery to a Channel. UrgentNotice changes message behavior without choosing a transport.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Bridge example map](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

Notice is the abstraction, UrgentNotice refines it, Channel is the implementation contract, Email and Sms implement delivery. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Notice is the [`abstraction`](../../GLOSSARY.md#abstraction), UrgentNotice refines it, Channel is the [`implementation`](../../GLOSSARY.md#implementation) contract, Email and Sms implement delivery.

Canonical roles in this example:

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — The high-level side of Bridge that delegates implementation work. Here: `Notice`.
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — A specialization of Abstraction independent of the implementation side. Here: `UrgentNotice`.
- [`Implementor`](../../GLOSSARY.md#implementor) — The contract used by a Bridge Abstraction for lower-level work. Here: `Channel`.
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — A particular implementation of the Implementor contract. Here: `Email, Sms`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Email:
    def deliver(self, text):
        print("Email:", text)


class Sms:
    def deliver(self, text):
        print("SMS:", text)


class Notice:
    def __init__(self, channel):
        self.channel = channel

    def send(self):
        self.channel.deliver("status normal")


class UrgentNotice(Notice):
    def send(self):
        self.channel.deliver("URGENT: disk full")


if __name__ == "__main__":
    Notice(Email()).send()
    UrgentNotice(Email()).send()
    UrgentNotice(Sms()).send()
```

### Python output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## C++20 example

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

### C++20 output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## Compare the languages

Both examples use Composition to separate notice type from delivery channel. Python retains a channel reference and relies on `deliver`; C++ borrows an Object implementing Channel, so its Lifetime must cover the notice.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when two axes of variation would otherwise produce a cross-product of subclasses.

### Use cases

Rendering APIs with independent shapes and backends, or notification types with channels, fit this structure.

**Cost:** The extra indirection requires a clear boundary; borrowed channels must outlive their notices.

## Check yourself

1. Which Classes change if you add a new channel but no new notice type?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a Push channel and reuse both notice classes without changing them.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
