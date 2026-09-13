# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/interpreter/README.md) · [Category](../README.md) · [Next](../../behavioral/mediator/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Beginner

## In One Sentence

Visit a collection without exposing its storage.

## Explain It Simply

A caller wants each track, not the details of a playlist container. Iterator keeps traversal position separate and lets a loop request the next item.

## The Problem

Clients need to read playlist entries without reaching into its private storage.

## Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why It Becomes a Problem

Index-based code tied to a public std::vector exposes representation and spreads boundary handling.

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

Playlist owns tracks; Iterator borrows the std::vector and stores a position. Range-for is the client. A static_assert checks the C++20 forward_iterator concept.

Canonical roles in this example:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — The collection that provides access to iterators. Here: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — An implementation that stores a traversal position for a particular Aggregate. Here: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — An iterator supporting forward traversal and the multipass guarantee, allowing independent copies to traverse the same range. Here: `std::forward_iterator`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

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
    const Playlist empty{{}};
    std::cout << "Empty: " << std::boolalpha << (empty.begin() == empty.end()) << '\n';
    auto first = playlist.begin();
    const auto copy = first;
    ++first;
    std::cout << "Independent positions: " << *first << ' ' << *copy << '\n';
}
```

## Example Output

```text
Track 7
Track 12
Track 18
Empty: true
Independent positions: 12 7
```

## When to Use

Use standard iterators or ranges to expose traversal without exposing storage details.

### Use cases

Container traversal and tree walks fit; choose iterator category according to actual operations and complexity.

## When NOT to Use

Avoid a custom iterator when returning existing const iterators or a standard range is sufficient; this custom [`implementation`](../../GLOSSARY.md#implementation) is educational.

## Advantages

Algorithms can use a common protocol, and multiple iterators maintain independent positions.

## Trade-offs

Iterators do not extend the collection [`lifetime`](../../GLOSSARY.md#lifetime). Moving or destroying this Playlist invalidates assumptions; dereferencing end is invalid, just as with standard iterators.

## Related Patterns

[Composite](../../structural/composite/README.md) · [Visitor](../visitor/README.md)

## Common Confusion

Visitor chooses operations by element type. Iterator controls traversal and need not know what the client does with an element.

## Terms to Remember

- `Iterator` — Traverse a collection through a stable access protocol.
- `Aggregate` — The collection that provides access to iterators. Example: `Playlist`.
- `Concrete Iterator` — An implementation that stores a traversal position for a particular Aggregate. Example: `Playlist::Iterator`.
- `forward iterator` — An iterator supporting forward traversal and the multipass guarantee, allowing independent copies to traverse the same range. Example: `std::forward_iterator`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — Keeping representation and invariants behind controlled operations.
- [`iterator invalidation`](../../GLOSSARY.md#iterator-invalidation) — An operation makes an iterator no longer valid for its intended use.
- [`generic programming`](../../GLOSSARY.md#generic-programming) — Writing algorithms against requirements on types rather than one concrete type.

## Interview Question

Why does the equality check include the std::vector pointer as well as the index?

## Mini Challenge

Test an empty playlist and two independent iterators; verify advancing one does not advance the other.

## Check Yourself

1. Can two traversals keep separate positions in the same Playlist?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** Clients need to read playlist entries without reaching into its private storage.
- **Solution:** Provide begin and end plus an iterator supporting dereference, increment and equality.
- **Trade-off:** Iterators do not extend the collection lifetime. Moving or destroying this Playlist invalidates assumptions; dereferencing end is invalid, just as with standard iterators.
- **Remember:** Move through data without opening the container.

[Previous](../../behavioral/interpreter/README.md) · [Category](../README.md) · [Next](../../behavioral/mediator/README.md)
