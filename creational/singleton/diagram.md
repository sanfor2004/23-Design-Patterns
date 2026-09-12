# Singleton: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

Metrics controls its lifetime and stores the count. instance returns a non-owning reference; callers must never delete it.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
