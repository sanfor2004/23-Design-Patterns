# Observer: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

Stock is the subject, Listener the callback interface, Display a subscriber. The client owns subscribers; weak_ptr avoids extending their lifetime.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
