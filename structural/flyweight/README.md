# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/facade/README.md) · [Category](../README.md) · [Next](../../structural/proxy/README.md)

## Category

Structural

## Difficulty

Advanced

## In One Sentence

Share immutable intrinsic data while keeping each occurrence's context separate.

## The Problem

A document has many repeated glyphs; storing a full outline for each position wastes memory.

## A Naive Solution

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Why This Becomes a Problem

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

Glyph holds shared intrinsic shape; GlyphPool interns it; PlacedGlyph stores extrinsic position and shared ownership.

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

## When to Use It

Use it after measuring significant duplication of immutable data across many objects.

## When NOT to Use It

Avoid it for tiny datasets, mutable per-instance data, or when lookup overhead outweighs savings.

## Advantages

Repeated placements reuse the same shape object while positions remain independent.

## Disadvantages / Trade-offs

The pool retains entries, map lookup costs time, and shared_ptr adds bookkeeping. This toy string is small; no memory-saving benchmark is claimed. Pool access is not synchronized.

## Technical Use Cases

Glyph outlines, terrain tile definitions and interned identifiers are suitable candidates when profiling supports sharing.

## Related Patterns

[composite](../composite/README.md) · [prototype](../../creational/prototype/README.md)

## Common Confusion

Prototype copies configured state to a new object. Flyweight deliberately shares intrinsic state across occurrences.

## Interview Question

Which fields belong in the pool key if font family and size affect the shape?

## Mini Challenge

Extend the key with a font identifier. Verify same keys share and different fonts do not.

## Quick Summary

- **Problem:** A document has many repeated glyphs; storing a full outline for each position wastes memory.
- **Solution:** Pool Glyph objects by character. PlacedGlyph shares a const Glyph and keeps its own x position.
- **Trade-off:** The pool retains entries, map lookup costs time, and shared_ptr adds bookkeeping. This toy string is small; no memory-saving benchmark is claimed. Pool access is not synchronized.
- **Remember:** Share the shape; carry the position.

[Previous](../../structural/facade/README.md) · [Category](../README.md) · [Next](../../structural/proxy/README.md)
