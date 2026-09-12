# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Category](../README.md) · [Next](../../creational/builder/README.md)

## Category

Creational

## Difficulty

Intermediate

## In One Sentence

Create related objects through one family interface.

## The Problem

A settings screen needs buttons and panels that belong to the same theme.

## A Naive Solution

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Why This Becomes a Problem

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

## When to Use It

Use it when several product types must vary together and clients should not choose concrete classes.

## When NOT to Use It

Avoid it for one stable product type or when independent choices are actually desirable.

## Advantages

The client can switch whole families without changing its rendering workflow.

## Disadvantages / Trade-offs

Adding a new product type, such as Slider, requires changing every factory. The interface cannot alone prove that an implementation returns a visually consistent family.

## Technical Use Cases

Theme kits and interchangeable database driver families are useful design contexts; this example only renders names.

## Related Patterns

[factory-method](../factory-method/README.md) · [builder](../builder/README.md)

## Common Confusion

Factory Method varies a creation step. Abstract Factory coordinates multiple related product types; a concrete factory can implement its operations with factory methods.

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
