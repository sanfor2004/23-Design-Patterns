# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Create a matching family of Objects.

## The problem

A settings screen needs buttons and panels that belong to the same theme. Constructing each widget directly lets a dark button accidentally sit inside a light panel. Every client must remember the matching rules.

## The idea

A screen needs buttons and panels with the same theme. One Factory supplies both, so the caller does not choose each concrete Class separately. Pass one Theme to render. The chosen factory supplies both products, so the client never names concrete widget classes.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Abstract Factory example map](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

Theme defines the family; DarkTheme and LightTheme create it. Button and Panel define product interfaces. render consumes those interfaces. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Theme defines the family; DarkTheme and LightTheme create it. Button and Panel define product interfaces. render consumes those interfaces.

Canonical roles in this example:

- [`Product`](../../GLOSSARY.md#product) — The contract of an object returned by creation code. Here: `Button, Panel`.
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — A particular implementation of a Product contract. Here: `DarkButton, LightButton, DarkPanel, LightPanel`.
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — An implementation that creates one matching Product family. Here: `DarkTheme, LightTheme`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Button:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " button"


class Panel:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " panel"


class DarkTheme:
    def button(self):
        return Button("dark")

    def panel(self):
        return Panel("dark")


class LightTheme:
    def button(self):
        return Button("light")

    def panel(self):
        return Panel("light")


def render(theme):
    print(theme.button().paint() + " + " + theme.panel().paint())


if __name__ == "__main__":
    render(DarkTheme())
    render(LightTheme())
```

### Python output

```text
dark button + dark panel
light button + light panel
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Button {
    virtual ~Button() = default;
    virtual std::string_view paint() const = 0;
};
struct Panel {
    virtual ~Panel() = default;
    virtual std::string_view paint() const = 0;
};
struct DarkButton final : Button {
    std::string_view paint() const override { return "dark button"; }
};
struct DarkPanel final : Panel {
    std::string_view paint() const override { return "dark panel"; }
};
struct LightButton final : Button {
    std::string_view paint() const override { return "light button"; }
};
struct LightPanel final : Panel {
    std::string_view paint() const override { return "light panel"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Panel> panel() const = 0;
};
struct DarkTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<DarkPanel>(); }
};
struct LightTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<LightPanel>(); }
};
void render(const Theme& theme) {
    const auto button = theme.button();
    const auto panel = theme.panel();
    std::cout << button->paint() << " + " << panel->paint() << '\n';
}
int main() {
    render(DarkTheme{});
    render(LightTheme{});
}
```

### C++20 output

```text
dark button + dark panel
light button + light panel
```

## Compare the languages

Python uses matching method names instead of abstract base classes. C++ declares separate Button, Panel, and Theme Interfaces. Both create a family of products. Neither language automatically proves that the products match visually.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when several product types must vary together and clients should not choose concrete classes.

### Use cases

Theme kits and interchangeable database driver families are useful design contexts; this example only renders names.

**Cost:** Adding a new product type, such as Slider, requires changing every factory. The interface cannot alone prove that an [`implementation`](../../GLOSSARY.md#implementation) returns a visually consistent family.

## Check yourself

1. Why does one Theme create both products?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a high-contrast family. Then add a Slider product and compare the number of files or classes affected.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
