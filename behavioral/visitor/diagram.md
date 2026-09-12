# Visitor: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

Item defines accept. Book and Food select their typed overload. Visitor lists supported types. Tax accumulates the result; the basket owns items.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
