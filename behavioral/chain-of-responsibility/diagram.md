# Chain of Responsibility: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Request  -->  Auth  -->  Limit
```

Handler owns its successor. Auth checks identity, Limit checks amount. The client chooses the chain order.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
