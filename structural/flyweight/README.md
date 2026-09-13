# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/facade/README.md) · [Category](../README.md) · [Next](../../structural/proxy/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Advanced

## In One Sentence

Share repeated immutable data.

## Explain It Simply

A document may display the same letter thousands of times. Flyweight stores the shared shape once while each placement keeps its own position.

## The Problem

A document has many repeated glyphs; storing a full outline for each position wastes memory.

## Naive Solution

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Why It Becomes a Problem

Duplicating the same shape for each occurrence scales memory with the number of placements rather than distinct shapes.

## The Idea

Pool Glyph objects by character. PlacedGlyph shares a const Glyph and keeps its own x position.

## Real-World Analogy

Several readers use the same reference book but keep their own bookmarks.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Flyweight](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## Participants

Glyph holds shared intrinsic shape; GlyphPool interns it; PlacedGlyph stores extrinsic position and shared [`ownership`](../../GLOSSARY.md#ownership).

Canonical roles in this example:

- [`intrinsic state`](../../GLOSSARY.md#intrinsic-state) — Data independent of an occurrence's context that a Flyweight can share. Here: `Glyph::shape`.
- [`extrinsic state`](../../GLOSSARY.md#extrinsic-state) — Per-occurrence data kept outside a shared Flyweight. Here: `PlacedGlyph::x`.
- [`Flyweight Factory`](../../GLOSSARY.md#flyweight-factory) — A lookup service that returns a shared Flyweight for a key. Here: `GlyphPool`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Glyph {
    const std::string shape;
    explicit Glyph(std::string value) : shape(std::move(value)) {}
};
class GlyphPool {
    std::map<char, std::shared_ptr<const Glyph>> glyphs_;
public:
    std::shared_ptr<const Glyph> get(char symbol) {
        auto& glyph = glyphs_[symbol];
        if (!glyph) glyph = std::make_shared<const Glyph>(std::string(1, symbol));
        return glyph;
    }
};
struct PlacedGlyph {
    std::shared_ptr<const Glyph> glyph;
    int x;
    void draw() const { std::cout << glyph->shape << " at " << x << '\n'; }
};
int main() {
    GlyphPool pool;
    const PlacedGlyph first{pool.get('A'), 0};
    const PlacedGlyph second{pool.get('A'), 10};
    first.draw();
    second.draw();
    std::cout << "Shared shape: " << std::boolalpha << (first.glyph == second.glyph) << '\n';
}
```

## Example Output

```text
A at 0
A at 10
Shared shape: true
```

## When to Use

Use it after measuring significant duplication of immutable data across many objects.

### Use cases

Glyph outlines, terrain tile definitions and interned identifiers are suitable candidates when profiling supports sharing.

## When NOT to Use

Avoid it for tiny datasets, mutable per-instance data, or when lookup overhead outweighs savings.

## Advantages

Repeated placements reuse the same shape object while positions remain independent.

## Trade-offs

The pool retains entries, map lookup costs time, and [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) adds bookkeeping. This toy string is small; no memory-saving benchmark is claimed. Pool access is not synchronized.

## Related Patterns

[Composite](../composite/README.md) · [Prototype](../../creational/prototype/README.md)

## Common Confusion

Prototype copies configured state to a new object. Flyweight deliberately shares intrinsic state across occurrences.

## Terms to Remember

- `Flyweight` — Share immutable intrinsic data while keeping each occurrence's context separate.
- `intrinsic state` — Data independent of an occurrence's context that a Flyweight can share. Example: `Glyph::shape`.
- `extrinsic state` — Per-occurrence data kept outside a shared Flyweight. Example: `PlacedGlyph::x`.
- `Flyweight Factory` — A lookup service that returns a shared Flyweight for a key. Example: `GlyphPool`.

## Interview Vocabulary

- [`interning`](../../GLOSSARY.md#interning) — Reusing one representation for equivalent values through a lookup pool.
- [`ownership`](../../GLOSSARY.md#ownership) — Responsibility for keeping a resource alive and eventually releasing it.
- [`memory allocation`](../../GLOSSARY.md#memory-allocation) — Obtaining storage for data; its cost and failure behavior depend on the mechanism.

## Interview Question

Which fields belong in the pool key if font family and size affect the shape?

## Mini Challenge

Extend the key with a font identifier. Verify same keys share and different fonts do not.

## Check Yourself

1. Which data must stay outside the shared Glyph, and why?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** A document has many repeated glyphs; storing a full outline for each position wastes memory.
- **Solution:** Pool Glyph objects by character. PlacedGlyph shares a const Glyph and keeps its own x position.
- **Trade-off:** The pool retains entries, map lookup costs time, and std::shared_ptr adds bookkeeping. This toy string is small; no memory-saving benchmark is claimed. Pool access is not synchronized.
- **Remember:** Share the shape; carry the position.

[Previous](../../structural/facade/README.md) · [Category](../README.md) · [Next](../../structural/proxy/README.md)
