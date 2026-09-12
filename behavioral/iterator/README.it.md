# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/interpreter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/mediator/README.it.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Principiante

## In One Sentence

Attraversa una collezione tramite un protocollo stabile.

## The Problem

Il client deve leggere una playlist senza accedere alla memoria privata.

## Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why It Becomes a Problem

Gli indici su un std::vector public espongono la rappresentazione e distribuiscono i controlli dei limiti.

## The Idea

Fornisci begin, end e un iterator con dereferenziazione, incremento e uguaglianza.

## Real-World Analogy

Segui un percorso museale senza conoscere il database interno delle sale.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Participants

Playlist possiede le tracce; Iterator prende in prestito il container std::vector e conserva una posizione. Range-for è il client; static_assert verifica forward_iterator di C++20.

Ruoli canonici in questo esempio:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — La raccolta che fornisce accesso tramite iterator. Qui: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — Un'implementation che conserva una posizione di attraversamento per un particolare Aggregate. Qui: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — Un iterator con avanzamento e garanzia multipass: copie indipendenti possono percorrere lo stesso intervallo. Qui: `std::forward_iterator`.

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

## When to Use

Preferisci iterator standard o ranges per esporre il percorso senza esporre lo storage.

### Use cases

Attraversamento di container e alberi; la categoria deve rispettare operazioni e complessità reali.

## When NOT to Use

Evita un iterator personalizzato quando bastano const_iterator esistenti o un range; qui è didattico.

## Advantages

Gli algorithm condividono un protocollo e più iterator mantengono posizioni indipendenti.

## Trade-offs

L'iterator non prolunga la [`lifetime`](../../GLOSSARY.md#lifetime) (L'intervallo in cui un object esiste e può essere usato secondo le sue regole) della raccolta. Spostare o distruggere Playlist invalida le premesse; dereferenziare end non è valido.

## Related Patterns

[Composite](../../structural/composite/README.it.md) · [Visitor](../visitor/README.it.md)

## Common Confusion

Visitor seleziona operazioni in base al tipo, Iterator gestisce il percorso senza conoscere l'elaborazione.

## Terms to Remember

- `Iterator` — Attraversa una collezione tramite un protocollo stabile.
- `Aggregate` — La raccolta che fornisce accesso tramite iterator. Esempio: `Playlist`.
- `Concrete Iterator` — Un'implementation che conserva una posizione di attraversamento per un particolare Aggregate. Esempio: `Playlist::Iterator`.
- `forward iterator` — Un iterator con avanzamento e garanzia multipass: copie indipendenti possono percorrere lo stesso intervallo. Esempio: `std::forward_iterator`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — Proteggere rappresentazione interna e invarianti mediante operazioni controllate.
- [`iterator invalidation`](../../GLOSSARY.md#iterator-invalidation) — Un'operazione rende un iterator non più valido per l'uso previsto.
- [`generic programming`](../../GLOSSARY.md#generic-programming) — Scrivere algorithm basati sui requisiti dei tipi invece che su un solo tipo concreto.

## Interview Question

Perché l'uguaglianza confronta anche il pointer al std::vector oltre all'indice?

## Mini Challenge

Prova una playlist vuota e due iterator indipendenti: avanzarne uno non deve muovere l'altro.

## Quick Summary

- **Problema:** Il client deve leggere una playlist senza accedere alla memoria privata.
- **Soluzione:** Fornisci begin, end e un iterator con dereferenziazione, incremento e uguaglianza.
- **Trade-off:** L'iterator non prolunga la lifetime della raccolta. Spostare o distruggere Playlist invalida le premesse; dereferenziare end non è valido.
- **Da ricordare:** Percorri i dati senza aprire il container.

[Precedente](../../behavioral/interpreter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/mediator/README.it.md)
