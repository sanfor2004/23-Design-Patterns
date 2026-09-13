# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Let a subclass choose what a shared workflow creates.

## The problem

An alert job always sends a completion message, but different environments need different senders. Hardcoding EmailSender inside run couples the workflow to email; copying run for console delivery duplicates the workflow.

This is `tight coupling`: the workflow knows a concrete sender type, so changing delivery can require changing that workflow.

## The idea

An alert job always sends the same message, but the delivery method varies. The workflow calls a Factory Method; each subclass creates its own Sender. Put the workflow in AlertJob and call the overridable make_sender creation step.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Factory Method example map](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

AlertJob owns the workflow. EmailJob and ConsoleJob override creation. Sender supplies the operation and the returned unique_ptr owns the product. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

AlertJob owns the workflow. EmailJob and ConsoleJob override creation. Sender supplies the operation and the returned [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) owns the product.

Canonical roles in this example:

- [`Creator`](../../GLOSSARY.md#creator) — The base role that owns a workflow and declares its creation operation. Here: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — A Creator subclass that supplies a particular Product. Here: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — The contract of an object returned by creation code. Here: `Sender`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class EmailSender:
    def send(self, message):
        print("Email:", message)


class ConsoleSender:
    def send(self, message):
        print("Console:", message)


class AlertJob:
    def make_sender(self):
        raise NotImplementedError

    def run(self):
        sender = self.make_sender()
        sender.send("build complete")


class EmailJob(AlertJob):
    def make_sender(self):
        return EmailSender()


class ConsoleJob(AlertJob):
    def make_sender(self):
        return ConsoleSender()


if __name__ == "__main__":
    EmailJob().run()
    ConsoleJob().run()
```

### Python output

```text
Email: build complete
Console: build complete
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(std::string_view message) const = 0;
};
struct EmailSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Email: " << message << '\n'; }
};
struct ConsoleSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Console: " << message << '\n'; }
};
class AlertJob {
protected:
    virtual std::unique_ptr<Sender> make_sender() const = 0;
public:
    virtual ~AlertJob() = default;
    void run() const {
        const auto sender = make_sender();
        sender->send("build complete");
    }
};
class EmailJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<EmailSender>(); }
};
class ConsoleJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<ConsoleSender>(); }
};
int main() {
    EmailJob{}.run();
    ConsoleJob{}.run();
}
```

### C++20 output

```text
Email: build complete
Console: build complete
```

## Compare the languages

Both versions keep a workflow in a base Class and override its creation method. Python checks the returned Object when `send` is called; C++ declares a Sender Interface and transfers Ownership with `unique_ptr`. A standalone factory function is often enough outside an inherited workflow.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when an existing [`inheritance`](../../GLOSSARY.md#inheritance)-based workflow needs an extensible creation step.

### Use cases

Pluggable exporters and environment-specific job runners are plausible applications; the senders here only print text.

**Cost:** Each new selection may need a subclass. Calling virtual creation from a base constructor would not dispatch to a derived override as intended.

## Check yourself

1. Where does Sender selection happen, and what workflow stays shared?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a FileJob with a sender that writes to a temporary file, and verify its contents.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
