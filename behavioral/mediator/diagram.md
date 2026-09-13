# Mediator: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![Mediator example map](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

Mediator defines notifications. Field reports changes. Button stores enabled state. LoginForm owns colleagues and coordinates them.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
