# Strategy: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

Checkout is the context, ShippingRule the behavioral contract, and lambdas implement standard and express fees.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
