# Facade: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

Stock checks availability, Payment charges, Shipping dispatches, and Checkout presents the common workflow.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
