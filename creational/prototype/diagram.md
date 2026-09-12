# Prototype: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

Enemy defines polymorphic cloning; Guard implements the copy; the client owns the clone and changes its name.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
