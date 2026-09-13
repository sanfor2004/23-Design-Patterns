# Builder: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![Builder example map](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

RequestBuilder stores temporary choices and validates them. Request owns the finished values. The client chooses the order of optional steps.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
