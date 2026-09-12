# Proxy: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

Image is the shared interface; DiskImage performs the real work; LazyImage owns the lazily created subject.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
