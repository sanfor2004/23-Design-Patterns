# Builder: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client  -->  RequestBuilder  -->  Request
```

RequestBuilder stores temporary choices and validates them. Request owns the finished values. The client chooses the order of optional steps.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
