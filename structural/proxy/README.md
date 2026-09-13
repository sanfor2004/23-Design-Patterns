# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Control access through a stand-in Object.

## The problem

A gallery may prepare many images but display only a few. Constructing every heavy image immediately performs unnecessary loading before anyone asks to display it.

## The idea

A gallery should not load every image before anyone views it. This Proxy offers `display`, creates the real image on first use, then reuses it. LazyImage implements Image and creates DiskImage on the first display call, then reuses it.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Proxy example map](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

Image is the shared interface; DiskImage performs the real work; LazyImage owns the lazily created subject. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Image is the shared interface; DiskImage performs the real work; LazyImage owns the lazily created subject.

Canonical roles in this example:

- [`Subject interface`](../../GLOSSARY.md#subject-interface) — The shared contract offered by a Proxy and its Real Subject. Here: `Image`.
- [`Real Subject`](../../GLOSSARY.md#real-subject) — The object that does the work behind a Proxy. Here: `DiskImage`.
- [`lazy initialization`](../../GLOSSARY.md#lazy-initialization) — Deferring creation until the value or resource is first needed. Here: `LazyImage::display`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class DiskImage:
    def __init__(self):
        print("Load image")

    def display(self):
        print("Display image")


class LazyImage:
    def __init__(self):
        self.image = None

    def display(self):
        if self.image is None:
            self.image = DiskImage()
        self.image.display()


if __name__ == "__main__":
    image = LazyImage()
    print("Proxy ready")
    image.display()
    image.display()
```

### Python output

```text
Proxy ready
Load image
Display image
Display image
```

## C++20 example

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() const = 0;
};
struct DiskImage final : Image {
    DiskImage() { std::cout << "Load image\n"; }
    void display() const override { std::cout << "Display image\n"; }
};
class LazyImage final : public Image {
    mutable std::unique_ptr<DiskImage> image_;
public:
    void display() const override {
        if (!image_) image_ = std::make_unique<DiskImage>();
        image_->display();
    }
};
int main() {
    const LazyImage image;
    std::cout << "Proxy ready\n";
    image.display();
    image.display();
}
```

### C++20 output

```text
Proxy ready
Load image
Display image
Display image
```

## Compare the languages

Python starts with `None`; C++ starts with an empty `unique_ptr`. Both create the real image on the first call. C++ uses `mutable` to cache inside a const operation. Neither version synchronizes concurrent calls or demonstrates access control; this is a virtual Proxy for lazy loading.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for lazy initialization, access checks or remote access when a stable subject interface is useful.

### Use cases

Lazy media access, authorization gates and remote object stubs are possible uses, with different failure semantics.

**Cost:** The first call now bears loading cost. mutable enables logical constness here but does not make concurrent display safe; loading failures also need a policy.

## Check yourself

1. How many real images exist after two display calls, and when were they created?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Count loads across three display calls and add a failure-once loader to test your retry policy.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
