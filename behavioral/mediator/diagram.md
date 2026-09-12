# Mediator: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

Mediator defines notifications. Field reports changes. Button stores enabled state. LoginForm owns colleagues and coordinates them.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
