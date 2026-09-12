# Bridge: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

Notice is the abstraction, UrgentNotice refines it, Channel is the implementation contract, Email and Sms implement delivery.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
