# Composite

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/bridge/README.md) · [Category](../README.md) · [Next](../../structural/decorator/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — A Design Pattern concerned with how objects and classes fit together.

## Difficulty

Beginner

## In One Sentence

Treat a leaf and a tree of objects through the same operation.

## The Problem

A file browser must compute bytes for a file or a folder containing nested folders.

## Naive Solution

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## Why It Becomes a Problem

Special loops for each depth break as nesting grows and repeat file-versus-folder checks.

## The Idea

Give File and Folder the Entry [`interface`](../../GLOSSARY.md#interface) (The contract of operations and observable behavior offered to a caller). A folder recursively asks its children for bytes.

## Real-World Analogy

A delivery box can hold parcels or smaller boxes; the total weight follows the same rule at each level.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Composite](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## Participants

Entry defines bytes. File returns its size; Folder owns children with [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) (A smart pointer with exclusive ownership that releases its object when the owner is destroyed) and aggregates their results.

Canonical roles in this example:

- [`Component`](../../GLOSSARY.md#component) — The common contract exposed by leaves, groups, or wrappers. Here: `Entry`.
- [`Leaf`](../../GLOSSARY.md#leaf) — A Component with no child Components. Here: `File`.
- [`ownership`](../../GLOSSARY.md#ownership) — Responsibility for keeping a resource alive and eventually releasing it. Here: `Folder::children_`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>
#include <vector>

struct Entry {
    virtual ~Entry() = default;
    virtual int bytes() const = 0;
};
class File final : public Entry {
    int size_;
public:
    explicit File(int size) : size_(size) {
        if (size < 0) throw std::invalid_argument("Negative size");
    }
    int bytes() const override { return size_; }
};
class Folder final : public Entry {
    std::vector<std::unique_ptr<Entry>> children_;
public:
    void add(std::unique_ptr<Entry> child) {
        if (!child) throw std::invalid_argument("Null child");
        children_.push_back(std::move(child));
    }
    int bytes() const override {
        int total = 0;
        for (const auto& child : children_) total += child->bytes();
        return total;
    }
};
int main() {
    auto images = std::make_unique<Folder>();
    images->add(std::make_unique<File>(20));
    Folder root;
    root.add(std::make_unique<File>(10));
    root.add(std::move(images));
    std::cout << "Total: " << root.bytes() << " bytes\n";
}
```

## Example Output

```text
Total: 30 bytes
```

## When to Use

Use it for genuine part-whole trees where a useful operation applies to both leaves and groups.

### Use cases

File trees, scene graphs without sharing, and menu hierarchies are suitable contexts.

## When NOT to Use

Avoid it for a flat list or a graph with shared parents and cycles; tree ownership would misrepresent the domain.

## Advantages

Clients calculate a subtree total without knowing its depth or concrete shape.

## Trade-offs

Very deep trees can overflow the call stack, integer sums can overflow, and group-only operations should not be forced onto leaves.

## Related Patterns

[Decorator](../decorator/README.md) · [Iterator](../../behavioral/iterator/README.md)

## Common Confusion

Decorator wraps one object to add behavior. Composite normally owns multiple children to represent a whole; both can recurse through an interface.

## Terms to Remember

- `Composite` — Treat a leaf and a tree of objects through the same operation.
- `Component` — The common contract exposed by leaves, groups, or wrappers. Example: `Entry`.
- `Leaf` — A Component with no child Components. Example: `File`.
- `ownership` — Responsibility for keeping a resource alive and eventually releasing it. Example: `Folder::children_`.

## Interview Vocabulary

- [`part-whole hierarchy`](../../GLOSSARY.md#part-whole-hierarchy) — A recursive structure in which groups contain leaves or smaller groups.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — Building a structure from parts that expose the same contract as the whole.
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — Using one interface with different implementations; C++ supports runtime and compile-time forms.

## Interview Question

Why is add available on Folder rather than Entry? What would a File.add mean?

## Mini Challenge

Add an empty folder and a second nesting level; verify both totals and consider a wider size type.

## Quick Summary

- **Problem:** A file browser must compute bytes for a file or a folder containing nested folders.
- **Solution:** Give File and Folder the Entry interface. A folder recursively asks its children for bytes.
- **Trade-off:** Very deep trees can overflow the call stack, integer sums can overflow, and group-only operations should not be forced onto leaves.
- **Remember:** A group answers like one item.

[Previous](../../structural/bridge/README.md) · [Category](../README.md) · [Next](../../structural/decorator/README.md)
