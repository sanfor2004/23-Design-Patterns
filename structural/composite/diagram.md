# Composite: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

Entry defines bytes. File returns its size; Folder owns children with unique_ptr and aggregates their results.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
