# Iteratore

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/interpreter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/mediator/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Principiante

## In una frase

Attraversa una collezione tramite un protocollo stabile.

## Il problema

Il client deve leggere una playlist senza accedere alla memoria privata.

## Soluzione iniziale

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Perché diventa difficile

Gli indici su un vector pubblico espongono la rappresentazione e distribuiscono i controlli dei limiti.

## Idea centrale

Fornisci begin, end e un iteratore con dereferenziazione, incremento e uguaglianza.

## Analogia quotidiana

Segui un percorso museale senza conoscere il database interno delle sale.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Iteratore](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Partecipanti

Playlist possiede le tracce; Iterator prende in prestito il vector e conserva una posizione. Range-for è il client; static_assert verifica forward_iterator di C++20.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Track 7
Track 12
Track 18
```

## Quando usarlo

Preferisci iteratori standard o ranges per esporre il percorso senza esporre lo storage.

## Quando NON usarlo

Evita un iteratore personalizzato quando bastano const_iterator esistenti o un range; qui è didattico.

## Vantaggi

Gli algoritmi condividono un protocollo e più iteratori mantengono posizioni indipendenti.

## Svantaggi e compromessi

L'iteratore non prolunga la vita della collezione. Spostare o distruggere Playlist invalida le premesse; dereferenziare end non è valido.

## Applicazioni tecniche

Attraversamento di contenitori e alberi; la categoria deve rispettare operazioni e complessità reali.

## Pattern correlati

[composite](../../structural/composite/README.it.md) · [visitor](../visitor/README.it.md)

## Confusione comune

Visitor seleziona operazioni in base al tipo, Iterator gestisce il percorso senza conoscere l'elaborazione.

## Domanda da colloquio

Perché l'uguaglianza confronta anche il puntatore al vector oltre all'indice?

## Piccola sfida

Prova una playlist vuota e due iteratori indipendenti: avanzarne uno non deve muovere l'altro.

## Riepilogo

- **Problema:** Il client deve leggere una playlist senza accedere alla memoria privata.
- **Soluzione:** Fornisci begin, end e un iteratore con dereferenziazione, incremento e uguaglianza.
- **Compromesso:** L'iteratore non prolunga la vita della collezione. Spostare o distruggere Playlist invalida le premesse; dereferenziare end non è valido.
- **Da ricordare:** Percorri i dati senza aprire il contenitore.

[Precedente](../../behavioral/interpreter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/mediator/README.it.md)
