# Visitor: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![Visitor example map](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

Item defines accept. Book and Food select their typed overload. Visitor lists supported types. Tax accumulates the result; the basket owns items.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
