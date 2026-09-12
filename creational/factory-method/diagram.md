# Factory Method: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

AlertJob owns the workflow. EmailJob and ConsoleJob override creation. Sender supplies the operation and the returned unique_ptr owns the product.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
