# Command: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
History  -->  Command  -->  Append → Document
```

Command defines execute and undo. Append changes a borrowed Document. History invokes and retains commands in stack order.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
