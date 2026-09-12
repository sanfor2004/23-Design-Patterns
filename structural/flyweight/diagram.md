# Flyweight: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

Glyph holds shared intrinsic shape; GlyphPool interns it; PlacedGlyph stores extrinsic position and shared ownership.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
