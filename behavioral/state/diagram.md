# State: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

Door is the context. DoorState defines press and name. Open and Closed hold non-owning links to the next state; main keeps both alive longer than Door.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
