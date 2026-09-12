# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/interpreter/README.md) · [Category](../README.md) · [Next](../../behavioral/mediator/README.md)

## Category

Behavioral

## Difficulty

Beginner

## In One Sentence

Traverse a collection through a stable access protocol.

## The Problem

Clients need to read playlist entries without reaching into its private storage.

## A Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why This Becomes a Problem

Index-based code tied to a public vector exposes representation and spreads boundary handling.

## The Idea

Provide begin and end plus an iterator supporting dereference, increment and equality.

## Real-World Analogy

Follow a museum route one exhibit at a time without needing its internal room database.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Participants

Playlist owns tracks; Iterator borrows the vector and stores a position. Range-for is the client. A static_assert checks the C++20 forward_iterator concept.

## Modern C++20 Example

```cpp
#include <cstddef>
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

class Playlist {
    std::vector<int> tracks_;
public:
    explicit Playlist(std::vector<int> tracks) : tracks_(std::move(tracks)) {}
    class Iterator {
        const std::vector<int>* tracks_ = nullptr;
        std::size_t index_ = 0;
    public:
        using value_type = int;
        using difference_type = std::ptrdiff_t;
        using iterator_concept = std::forward_iterator_tag;
        Iterator() = default;
        Iterator(const std::vector<int>& tracks, std::size_t index) : tracks_(&tracks), index_(index) {}
        const int& operator*() const { return (*tracks_)[index_]; }
        Iterator& operator++() { ++index_; return *this; }
        Iterator operator++(int) { auto old = *this; ++*this; return old; }
        bool operator==(const Iterator&) const = default;
    };
    Iterator begin() const { return Iterator{tracks_, 0}; }
    Iterator end() const { return Iterator{tracks_, tracks_.size()}; }
};
static_assert(std::forward_iterator<Playlist::Iterator>);
int main() {
    const Playlist playlist{{7, 12, 18}};
    for (int track : playlist) std::cout << "Track " << track << '\n';
}
```

## Example Output

```text
Track 7
Track 12
Track 18
```

## When to Use It

Use standard iterators or ranges to expose traversal without exposing storage details.

## When NOT to Use It

Avoid a custom iterator when returning existing const iterators or a standard range is sufficient; this custom implementation is educational.

## Advantages

Algorithms can use a common protocol, and multiple iterators maintain independent positions.

## Disadvantages / Trade-offs

Iterators do not extend the collection lifetime. Moving or destroying this Playlist invalidates assumptions; dereferencing end is invalid, just as with standard iterators.

## Technical Use Cases

Container traversal and tree walks fit; choose iterator category according to actual operations and complexity.

## Related Patterns

[composite](../../structural/composite/README.md) · [visitor](../visitor/README.md)

## Common Confusion

Visitor chooses operations by element type. Iterator controls traversal and need not know what the client does with an element.

## Interview Question

Why does the equality check include the vector pointer as well as the index?

## Mini Challenge

Test an empty playlist and two independent iterators; verify advancing one does not advance the other.

## Quick Summary

- **Problem:** Clients need to read playlist entries without reaching into its private storage.
- **Solution:** Provide begin and end plus an iterator supporting dereference, increment and equality.
- **Trade-off:** Iterators do not extend the collection lifetime. Moving or destroying this Playlist invalidates assumptions; dereferencing end is invalid, just as with standard iterators.
- **Remember:** Move through data without opening the container.

[Previous](../../behavioral/interpreter/README.md) · [Category](../README.md) · [Next](../../behavioral/mediator/README.md)
