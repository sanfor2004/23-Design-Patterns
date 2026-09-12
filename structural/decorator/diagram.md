# Decorator: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

Drink is the shared contract. Coffee supplies the base behavior. Milk wraps exactly one Drink. The client owns the outermost wrapper.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
