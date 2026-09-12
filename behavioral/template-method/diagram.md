# Template Method: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

Report owns the algorithm skeleton; TextReport implements variation points. The client calls generate through the public workflow.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
