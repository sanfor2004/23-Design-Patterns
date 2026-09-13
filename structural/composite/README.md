# Composite

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Use the same operation for one item or a tree of items.

## The problem

A file browser must compute bytes for a file or a folder containing nested folders. Special loops for each depth break as nesting grows and repeat file-versus-folder checks.

## The idea

A folder contains files and other folders. Composite gives both a `bytes` operation, so a caller can ask for a size without handling every nesting level itself. Give File and Folder the Entry [`interface`](../../GLOSSARY.md#interface). A folder recursively asks its children for bytes.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Composite example map](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

Entry defines bytes. File returns its size; Folder owns children with unique_ptr and aggregates their results. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Entry defines bytes. File returns its size; Folder owns children with [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) and aggregates their results.

Canonical roles in this example:

- [`Component`](../../GLOSSARY.md#component) — The common contract exposed by leaves, groups, or wrappers. Here: `Entry`.
- [`Leaf`](../../GLOSSARY.md#leaf) — A Component with no child Components. Here: `File`.
- [`ownership`](../../GLOSSARY.md#ownership) — Responsibility for keeping a resource alive and eventually releasing it. Here: `Folder::children_`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class File:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Negative size")
        self.size = size

    def bytes(self):
        return self.size


class Folder:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def bytes(self):
        return sum(child.bytes() for child in self.children)


def main():
    root = Folder()
    print("Empty:", root.bytes(), "bytes")
    images = Folder()
    images.add(File(20))
    root.add(File(10))
    root.add(images)
    print("Total:", root.bytes(), "bytes")
    try:
        File(-1)
    except ValueError:
        print("Negative size rejected")


if __name__ == "__main__":
    main()
```

### Python output

```text
Empty: 0 bytes
Total: 30 bytes
Negative size rejected
```

## C++20 example

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
    std::cout << "Empty: " << Folder{}.bytes() << " bytes\n";
    try { const File invalid{-1}; }
    catch (const std::invalid_argument&) { std::cout << "Negative size rejected\n"; }
}
```

### C++20 output

```text
Total: 30 bytes
Empty: 0 bytes
Negative size rejected
```

## Compare the languages

Python uses a list of Objects that offer `bytes`; C++ uses a common Entry Interface and exclusive Ownership with `unique_ptr`. Python references allow accidental shared children or cycles. Keep this example a tree; garbage collection does not make recursive traversal of a cycle safe.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for genuine part-whole trees where a useful operation applies to both leaves and groups.

### Use cases

File trees, scene graphs without sharing, and menu hierarchies are suitable contexts.

**Cost:** Very deep trees can overflow the call stack, integer sums can overflow, and group-only operations should not be forced onto leaves.

## Check yourself

1. Why can an empty Folder return zero through the same Interface as File?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add an empty folder and a second nesting level; verify both totals and consider a wider size type.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
