# Interpreter: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![Interpreter example map](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

Expression defines evaluation, Context supplies roles, Role tests membership, Both owns its child expressions.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
