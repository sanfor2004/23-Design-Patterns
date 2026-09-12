# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Category](../README.md) · [Next](../../creational/builder/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — A Design Pattern concerned with how objects are created and configured.

## Difficulty

Intermediate

## In One Sentence

Create related objects through one family [`interface`](../../GLOSSARY.md#interface) (The contract of operations and observable behavior offered to a caller).

## The Problem

A settings screen needs buttons and panels that belong to the same theme.

## Naive Solution

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Why It Becomes a Problem

Constructing each widget directly lets a dark button accidentally sit inside a light panel. Every client must remember the matching rules.

## The Idea

Pass one Theme to render. The chosen factory supplies both products, so the client never names concrete widget classes.

## Real-World Analogy

Ordering a matching furniture set is easier than choosing each piece independently.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Abstract Factory](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## Participants

Theme defines the family; DarkTheme and LightTheme create it. Button and Panel define product interfaces. render consumes those interfaces.

Canonical roles in this example:

- [`Product`](../../GLOSSARY.md#product) — The contract of an object returned by creation code. Here: `Button, Panel`.
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — A particular implementation of a Product contract. Here: `DarkButton, LightButton, DarkPanel, LightPanel`.
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — An implementation that creates one matching Product family. Here: `DarkTheme, LightTheme`.

## Modern C++20 Example

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

## Example Output

```text
dark button + dark panel
light button + light panel
```

## When to Use

Use it when several product types must vary together and clients should not choose concrete classes.

### Use cases

Theme kits and interchangeable database driver families are useful design contexts; this example only renders names.

## When NOT to Use

Avoid it for one stable product type or when independent choices are actually desirable.

## Advantages

The client can switch whole families without changing its rendering workflow.

## Trade-offs

Adding a new product type, such as Slider, requires changing every factory. The interface cannot alone prove that an [`implementation`](../../GLOSSARY.md#implementation) (The concrete code that fulfills an interface or performs an operation) returns a visually consistent family.

## Related Patterns

[Factory Method](../factory-method/README.md) · [Builder](../builder/README.md)

## Common Confusion

Factory Method varies a creation step. Abstract Factory coordinates multiple related product types; a concrete factory can implement its operations with factory methods.

## Terms to Remember

- `Abstract Factory` — Create related objects through one family interface.
- `Product` — The contract of an object returned by creation code. Example: `Button, Panel`.
- `Concrete Product` — A particular implementation of a Product contract. Example: `DarkButton, LightButton, DarkPanel, LightPanel`.
- `Concrete Factory` — An implementation that creates one matching Product family. Example: `DarkTheme, LightTheme`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Choosing a concrete type and establishing an object's initial values and lifetime.
- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — Depend on the promised contract instead of a particular concrete implementation.
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — Put a changing design decision behind a stable boundary.

## Interview Question

What changes when you add a new theme versus a new widget type? Trace every interface affected.

## Mini Challenge

Add a high-contrast family. Then add a Slider product and compare the number of files or classes affected.

## Quick Summary

- **Problem:** A settings screen needs buttons and panels that belong to the same theme.
- **Solution:** Pass one Theme to render. The chosen factory supplies both products, so the client never names concrete widget classes.
- **Trade-off:** Adding a new product type, such as Slider, requires changing every factory. The interface cannot alone prove that an implementation returns a visually consistent family.
- **Remember:** One factory, one matching set.

[Category](../README.md) · [Next](../../creational/builder/README.md)
