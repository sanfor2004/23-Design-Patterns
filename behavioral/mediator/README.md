# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Put coordination rules in one Object.

## The problem

Username and password fields jointly determine whether a login button is enabled. If each field knows the other field and the button, UI rules spread across components and create mutual dependencies.

## The idea

A login button depends on two fields being filled. Mediator handles that rule so each field does not need to know the other field or the button. Fields report changed to LoginForm; the form checks both values and updates the button.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Mediator example map](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

Mediator defines notifications. Field reports changes. Button stores enabled state. LoginForm owns colleagues and coordinates them. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Mediator defines notifications. Field reports changes. Button stores enabled state. LoginForm owns colleagues and coordinates them.

Canonical roles in this example:

- [`Colleague`](../../GLOSSARY.md#colleague) — An object whose interactions are coordinated by a Mediator. Here: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — An implementation that contains the coordination rules for its Colleagues. Here: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — A function or operation supplied to be called when another operation needs it. Here: `Mediator::changed`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Field:
    def __init__(self, changed):
        self.changed = changed
        self.value = ""

    def set(self, value):
        self.value = value
        self.changed()


class Button:
    def __init__(self):
        self.enabled = False


class LoginForm:
    def __init__(self):
        self.username = Field(self.changed)
        self.password = Field(self.changed)
        self.submit = Button()

    def changed(self):
        self.submit.enabled = bool(self.username.value and self.password.value)


if __name__ == "__main__":
    form = LoginForm()
    form.username.set("learner")
    print("Ready:", form.submit.enabled)
    form.password.set("example")
    print("Ready:", form.submit.enabled)
    form.password.set("")
    print("Ready:", form.submit.enabled)
```

### Python output

```text
Ready: False
Ready: True
Ready: False
```

## C++20 example

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <utility>

struct Mediator {
    virtual ~Mediator() = default;
    virtual void changed() = 0;
};
class Field {
    Mediator& mediator_;
    std::string value_;
public:
    explicit Field(Mediator& mediator) : mediator_(mediator) {}
    void set(std::string value) { value_ = std::move(value); mediator_.changed(); }
    bool empty() const { return value_.empty(); }
};
class Button {
    bool enabled_ = false;
public:
    void enable(bool enabled) { enabled_ = enabled; }
    bool enabled() const { return enabled_; }
};
class LoginForm final : public Mediator {
    Field username_;
    Field password_;
    Button submit_;
public:
    LoginForm() : username_(*this), password_(*this) {}
    LoginForm(const LoginForm&) = delete;
    LoginForm& operator=(const LoginForm&) = delete;
    void changed() override { submit_.enable(!username_.empty() && !password_.empty()); }
    void username(std::string value) { username_.set(std::move(value)); }
    void password(std::string value) { password_.set(std::move(value)); }
    bool ready() const { return submit_.enabled(); }
};
int main() {
    LoginForm form;
    form.username("learner");
    std::cout << "Ready: " << std::boolalpha << form.ready() << '\n';
    form.password("example");
    std::cout << "Ready: " << form.ready() << '\n';
    form.password("");
    std::cout << "Ready after clearing: " << form.ready() << '\n';
}
```

### C++20 output

```text
Ready: false
Ready: true
Ready after clearing: false
```

## Compare the languages

Python Fields call a bound method on their Mediator. C++ Fields borrow a Mediator reference, and LoginForm disables copying to protect those links. Python can collect reference cycles, but copying this form still needs care: a shallow copy would share Fields and callbacks.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when interaction rules between several peers are becoming tangled.

### Use cases

Dialog coordination and workflow controllers fit; enabling a button is not authentication or password validation.

**Cost:** The mediator can become too large. LoginForm is noncopyable because its fields hold references back to it; copying would leave incorrect links.

## Check yourself

1. Who decides whether the button is enabled when a field becomes empty?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a terms checkbox and require all three conditions without teaching Field about the button.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
