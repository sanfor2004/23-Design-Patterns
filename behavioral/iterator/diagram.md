# Iterator: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

Playlist owns tracks; Iterator borrows the vector and stores a position. Range-for is the client. A static_assert checks the C++20 forward_iterator concept.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
