# Memento: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

Editor is the originator. Snapshot is the memento with private state. main is the caretaker holding it without inspecting its contents.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
