# Command: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![Command example map](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

Command defines execute and undo. Append changes a borrowed Document. History invokes and retains commands in stack order.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
