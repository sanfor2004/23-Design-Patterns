# Command

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Keep an action as an Object.

## The problem

An editor must apply changes and undo the last action without teaching the toolbar every document operation. Direct mutation performs the edit but leaves no record of the action or its prior state.

## The idea

An editor needs to remember edits so users can undo them. Command stores the action and the information needed to reverse it, while History decides when to run or undo it. Append captures a receiver and argument; execute stores the old text, and undo restores it. History owns executed commands.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Command example map](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

Command defines execute and undo. Append changes a borrowed Document. History invokes and retains commands in stack order. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Command defines execute and undo. Append changes a borrowed Document. History invokes and retains commands in stack order.

Canonical roles in this example:

- [`Receiver`](../../GLOSSARY.md#receiver) — The object that performs the work requested by a Command. Here: `Document`.
- [`Invoker`](../../GLOSSARY.md#invoker) — The role that starts or stores Commands without knowing each operation's details. Here: `History`.
- [`Concrete Command`](../../GLOSSARY.md#concrete-command) — A Command implementation that binds a Receiver and an action. Here: `Append`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Document:
    def __init__(self, text):
        self.text = text


class Append:
    def __init__(self, document, suffix):
        self.document = document
        self.suffix = suffix
        self.before = None

    def execute(self):
        self.before = self.document.text
        self.document.text += self.suffix

    def undo(self):
        self.document.text = self.before


class History:
    def __init__(self):
        self.commands = []

    def run(self, command):
        command.execute()
        self.commands.append(command)

    def undo(self):
        if self.commands:
            self.commands.pop().undo()


if __name__ == "__main__":
    document = Document("Hello")
    history = History()
    history.run(Append(document, " world"))
    history.run(Append(document, "!"))
    print(document.text)
    for _ in range(3):
        history.undo()
        print(document.text)
```

### Python output

```text
Hello world!
Hello world
Hello
Hello
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Document { std::string text; };
struct Command {
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};
class Append final : public Command {
    Document& document_;
    std::string suffix_;
    std::string before_;
public:
    Append(Document& document, std::string suffix) : document_(document), suffix_(std::move(suffix)) {}
    void execute() override { before_ = document_.text; document_.text += suffix_; }
    void undo() override { document_.text = before_; }
};
class History {
    std::vector<std::unique_ptr<Command>> commands_;
public:
    void run(std::unique_ptr<Command> command) {
        if (!command) throw std::invalid_argument("Missing command");
        commands_.push_back(std::move(command));
        try { commands_.back()->execute(); }
        catch (...) { commands_.pop_back(); throw; }
    }
    void undo() {
        if (commands_.empty()) return;
        commands_.back()->undo();
        commands_.pop_back();
    }
};
int main() {
    Document document{"Hello"};
    History history;
    history.run(std::make_unique<Append>(document, " world"));
    std::cout << document.text << '\n';
    history.undo();
    std::cout << document.text << '\n';
    history.undo();
    std::cout << "Empty undo: " << document.text << '\n';
}
```

### C++20 output

```text
Hello world
Hello
Empty undo: Hello
```

## Compare the languages

A callable is enough for an action with no history. Here a Command Object keeps the previous text for undo. Python retains the Document; C++ borrows it and owns Commands in History. Undo assumes commands run once and are undone in reverse order, with no unrelated edits in between.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for deferred actions, queues, macros or undo histories.

### Use cases

Editor actions and job queues fit, but durable queues need serialization and idempotency beyond this example.

**Cost:** Saving whole text costs memory. This single-threaded demo assumes edits go through History and Document outlives it; external edits would invalidate undo expectations.

## Check yourself

1. Why must these edits be undone in reverse order?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a second append, undo twice, and verify the empty-history call is harmless.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
