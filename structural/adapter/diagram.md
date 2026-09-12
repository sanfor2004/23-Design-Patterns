# Adapter: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

Temperature is the target interface. LegacyThermometer is the existing API. CelsiusAdapter borrows it; display uses only Temperature.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
