# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/flyweight/README.md) · [Category](../README.md) · [Next](../../behavioral/chain-of-responsibility/README.md)

## Category

Structural

## Difficulty

Intermediate

## In One Sentence

Control access to an object through a stand-in with the same interface.

## The Problem

A gallery may prepare many images but display only a few.

## A Naive Solution

```cpp
DiskImage image; // loads even if never displayed
```

## Why This Becomes a Problem

Constructing every heavy image immediately performs unnecessary loading before anyone asks to display it.

## The Idea

LazyImage implements Image and creates DiskImage on the first display call, then reuses it.

## Real-World Analogy

A library request slip represents a stored book until the librarian retrieves it.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Proxy](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## Participants

Image is the shared interface; DiskImage performs the real work; LazyImage owns the lazily created subject.

## Modern C++20 Example

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

## Example Output

```text
Proxy ready
Load image
Display image
Display image
```

## When to Use It

Use it for lazy initialization, access checks or remote access when a stable subject interface is useful.

## When NOT to Use It

Avoid it if direct construction is cheap and the access policy adds no value.

## Advantages

Callers use the same display interface while creation is deferred.

## Disadvantages / Trade-offs

The first call now bears loading cost. mutable enables logical constness here but does not make concurrent display safe; loading failures also need a policy.

## Technical Use Cases

Lazy media access, authorization gates and remote object stubs are possible uses, with different failure semantics.

## Related Patterns

[decorator](../decorator/README.md) · [adapter](../adapter/README.md)

## Common Confusion

Decorator adds behavior; Proxy controls when or whether a subject is reached. Their class diagrams can look similar.

## Interview Question

If loading throws, should the proxy retry on the next call or remember failure? Explain your contract.

## Mini Challenge

Count loads across three display calls and add a failure-once loader to test your retry policy.

## Quick Summary

- **Problem:** A gallery may prepare many images but display only a few.
- **Solution:** LazyImage implements Image and creates DiskImage on the first display call, then reuses it.
- **Trade-off:** The first call now bears loading cost. mutable enables logical constness here but does not make concurrent display safe; loading failures also need a policy.
- **Remember:** A stand-in guards the real object.

[Previous](../../structural/flyweight/README.md) · [Category](../README.md) · [Next](../../behavioral/chain-of-responsibility/README.md)
