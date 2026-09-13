# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Share repeated immutable data.

## The problem

A document has many repeated glyphs; storing a full outline for each position wastes memory. Duplicating the same shape for each occurrence scales memory with the number of placements rather than distinct shapes.

## The idea

A document may display the same letter thousands of times. Flyweight stores the shared shape once while each placement keeps its own position. Pool Glyph objects by character. PlacedGlyph shares a const Glyph and keeps its own x position.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Flyweight example map](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

Glyph holds shared intrinsic shape; GlyphPool interns it; PlacedGlyph stores extrinsic position and shared ownership. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Glyph holds shared intrinsic shape; GlyphPool interns it; PlacedGlyph stores extrinsic position and shared [`ownership`](../../GLOSSARY.md#ownership).

Canonical roles in this example:

- [`intrinsic state`](../../GLOSSARY.md#intrinsic-state) — Data independent of an occurrence's context that a Flyweight can share. Here: `Glyph::shape`.
- [`extrinsic state`](../../GLOSSARY.md#extrinsic-state) — Per-occurrence data kept outside a shared Flyweight. Here: `PlacedGlyph::x`.
- [`Flyweight Factory`](../../GLOSSARY.md#flyweight-factory) — A lookup service that returns a shared Flyweight for a key. Here: `GlyphPool`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Glyph:
    shape: str


class GlyphPool:
    def __init__(self):
        self.glyphs = {}

    def get(self, symbol):
        if symbol not in self.glyphs:
            self.glyphs[symbol] = Glyph(symbol)
        return self.glyphs[symbol]


class PlacedGlyph:
    def __init__(self, glyph, x):
        self.glyph = glyph
        self.x = x

    def draw(self):
        print(self.glyph.shape, "at", self.x)


if __name__ == "__main__":
    pool = GlyphPool()
    first = PlacedGlyph(pool.get("A"), 0)
    second = PlacedGlyph(pool.get("A"), 10)
    first.draw()
    second.draw()
    print("Shared shape:", first.glyph is second.glyph)
    print("Different shape:", first.glyph is pool.get("B"))
```

### Python output

```text
A at 0
A at 10
Shared shape: True
Different shape: False
```

## C++20 example

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

### C++20 output

```text
A at 0
A at 10
Shared shape: true
```

## Compare the languages

A small frozen dataclass makes the shared Python Glyph immutable through normal attribute assignment. C++ uses `shared_ptr<const Glyph>`. Both pools keep entries alive. This demonstrates sharing, not measured memory savings; the pool itself has a cost.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it after measuring significant duplication of immutable data across many objects.

### Use cases

Glyph outlines, terrain tile definitions and interned identifiers are suitable candidates when profiling supports sharing.

**Cost:** The pool retains entries, map lookup costs time, and [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) adds bookkeeping. This toy string is small; no memory-saving benchmark is claimed. Pool access is not synchronized.

## Check yourself

1. Which data must stay outside the shared Glyph, and why?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Extend the key with a font identifier. Verify same keys share and different fonts do not.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
