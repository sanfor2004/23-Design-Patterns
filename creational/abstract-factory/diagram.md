# Abstract Factory: structure

[Explanation](README.md) · [C++20 source](cpp/main.cpp)

```text
render()  -->  Theme  -->  Button + Panel
```

Theme defines the family; DarkTheme and LightTheme create it. Button and Panel define product interfaces. render consumes those interfaces.


The arrows show collaboration or delegation, not a complete UML model. This diagram describes this repository’s example.
