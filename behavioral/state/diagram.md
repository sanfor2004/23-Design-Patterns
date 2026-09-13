# State: example map

[English lesson](README.md) · [الشرح بالمصري](README.ar-EG.md) · [Python source](python/main.py) · [C++20 source](cpp/main.cpp)

![State example map](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

Door is the context. DoorState defines press and name. Open and Closed hold non-owning links to the next state; main keeps both alive longer than Door.

The sketch maps the example's call path. The middle card is where the pattern assigns or changes responsibility; arrows show the demonstrated flow, not inheritance or object ownership.
