# Interpreter: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

Expression defines evaluation, Context supplies roles, Role tests membership, Both owns its child expressions.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
