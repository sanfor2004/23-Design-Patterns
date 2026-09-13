# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/flyweight/README.md) · [Category](../README.md) · [Next](../../behavioral/chain-of-responsibility/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Intermediate

## In One Sentence

Control access through a stand-in Object.

## Explain It Simply

A gallery should not load every image before anyone views it. This Proxy offers `display`, creates the real image on first use, then reuses it.

## The Problem

A gallery may prepare many images but display only a few.

## Naive Solution

```cpp
DiskImage image; // loads even if never displayed
```

## Why It Becomes a Problem

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

Canonical roles in this example:

- [`Subject interface`](../../GLOSSARY.md#subject-interface) — The shared contract offered by a Proxy and its Real Subject. Here: `Image`.
- [`Real Subject`](../../GLOSSARY.md#real-subject) — The object that does the work behind a Proxy. Here: `DiskImage`.
- [`lazy initialization`](../../GLOSSARY.md#lazy-initialization) — Deferring creation until the value or resource is first needed. Here: `LazyImage::display`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

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

## When to Use

Use it for lazy initialization, access checks or remote access when a stable subject interface is useful.

### Use cases

Lazy media access, authorization gates and remote object stubs are possible uses, with different failure semantics.

## When NOT to Use

Avoid it if direct construction is cheap and the access policy adds no value.

## Advantages

Callers use the same display interface while creation is deferred.

## Trade-offs

The first call now bears loading cost. mutable enables logical constness here but does not make concurrent display safe; loading failures also need a policy.

## Related Patterns

[Decorator](../decorator/README.md) · [Adapter](../adapter/README.md)

## Common Confusion

Decorator adds behavior; Proxy controls when or whether a subject is reached. Their class diagrams can look similar.

## Terms to Remember

- `Proxy` — Control access to an object through a stand-in with the same interface.
- `Subject interface` — The shared contract offered by a Proxy and its Real Subject. Example: `Image`.
- `Real Subject` — The object that does the work behind a Proxy. Example: `DiskImage`.
- `lazy initialization` — Deferring creation until the value or resource is first needed. Example: `LazyImage::display`.

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — An object asks a collaborator to perform part of its work.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — What the program does while executing, including behavior selected from runtime input.
- [`trade-off`](../../GLOSSARY.md#trade-off) — A benefit gained at the cost of another desirable property.

## Interview Question

If loading throws, should the proxy retry on the next call or remember failure? Explain your contract.

## Mini Challenge

Count loads across three display calls and add a failure-once loader to test your retry policy.

## Check Yourself

1. How many real images exist after two display calls, and when were they created?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** A gallery may prepare many images but display only a few.
- **Solution:** LazyImage implements Image and creates DiskImage on the first display call, then reuses it.
- **Trade-off:** The first call now bears loading cost. mutable enables logical constness here but does not make concurrent display safe; loading failures also need a policy.
- **Remember:** A stand-in guards the real object.

[Previous](../../structural/flyweight/README.md) · [Category](../README.md) · [Next](../../behavioral/chain-of-responsibility/README.md)
