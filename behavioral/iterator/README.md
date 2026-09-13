# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Visit a collection without exposing its storage.

## The problem

Clients need to read playlist entries without reaching into its private storage. Index-based code tied to a public std::vector exposes representation and spreads boundary handling.

## The idea

A caller wants each track, not the details of a playlist container. Iterator keeps traversal position separate and lets a loop request the next item. Provide begin and end plus an iterator supporting dereference, increment and equality.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Iterator example map](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

Playlist owns tracks; Iterator borrows the vector and stores a position. Range-for is the client. A static_assert checks the C++20 forward_iterator concept. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Playlist owns tracks; Iterator borrows the std::vector and stores a position. Range-for is the client. A static_assert checks the C++20 forward_iterator concept.

Canonical roles in this example:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — The collection that provides access to iterators. Here: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — An implementation that stores a traversal position for a particular Aggregate. Here: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — An iterator supporting forward traversal and the multipass guarantee, allowing independent copies to traverse the same range. Here: `std::forward_iterator`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Playlist:
    def __init__(self, tracks):
        self._tracks = list(tracks)

    def __iter__(self):
        return iter(self._tracks)


if __name__ == "__main__":
    playlist = Playlist([7, 12, 18])
    for track in playlist:
        print("Track", track)
    first = iter(playlist)
    second = iter(playlist)
    print("Independent:", next(first), next(second))
    print("Empty:", list(Playlist([])))
```

### Python output

```text
Track 7
Track 12
Track 18
Independent: 7 7
Empty: []
```

## C++20 example

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

### C++20 output

```text
Track 7
Track 12
Track 18
Empty: true
Independent positions: 12 7
```

## Compare the languages

Python delegates to the built-in list Iterator through `__iter__`; exhaustion raises StopIteration, which `for` handles. C++ demonstrates a custom forward Iterator, but returning standard iterators or ranges is usually simpler. Do not modify the collection while traversing either example.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use standard iterators or ranges to expose traversal without exposing storage details.

### Use cases

Container traversal and tree walks fit; choose iterator category according to actual operations and complexity.

**Cost:** Iterators do not extend the collection [`lifetime`](../../GLOSSARY.md#lifetime). Moving or destroying this Playlist invalidates assumptions; dereferencing end is invalid, just as with standard iterators.

## Check yourself

1. Can two traversals keep separate positions in the same Playlist?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Test an empty playlist and two independent iterators; verify advancing one does not advance the other.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
