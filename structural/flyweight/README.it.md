# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/facade/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/proxy/README.it.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Un Design Pattern che organizza le relazioni fra object e class.

## Difficulty

Avanzato

## In One Sentence

Condividi dati intrinseci immutabili e separa il contesto di ogni occorrenza.

## The Problem

Un documento ripete molti glifi; conservare il contorno per ogni posizione spreca memoria.

## Naive Solution

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Why It Becomes a Problem

Duplicare la forma fa crescere la memoria con le occorrenze invece che con le forme distinte.

## The Idea

GlyphPool riutilizza Glyph per carattere; PlacedGlyph condivide un const Glyph e conserva la propria x.

## Real-World Analogy

Più lettori usano lo stesso libro di riferimento ma tengono segnalibri diversi.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Flyweight](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## Participants

Glyph contiene la forma intrinseca, GlyphPool la internizza, PlacedGlyph conserva posizione estrinseca e [`ownership`](../../GLOSSARY.md#ownership) (La responsabilità di mantenere una risorsa valida e infine rilasciarla) condivisa.

Ruoli canonici in questo esempio:

- [`intrinsic state`](../../GLOSSARY.md#intrinsic-state) — Dati indipendenti dal contesto della singola occorrenza, condivisibili da un Flyweight. Qui: `Glyph::shape`.
- [`extrinsic state`](../../GLOSSARY.md#extrinsic-state) — Dati specifici di un'occorrenza conservati fuori dal Flyweight condiviso. Qui: `PlacedGlyph::x`.
- [`Flyweight Factory`](../../GLOSSARY.md#flyweight-factory) — Un servizio di ricerca che restituisce un Flyweight condiviso per una chiave. Qui: `GlyphPool`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Glyph {
    const std::string shape;
    explicit Glyph(std::string value) : shape(std::move(value)) {}
};
class GlyphPool {
    std::map<char, std::shared_ptr<const Glyph>> glyphs_;
public:
    std::shared_ptr<const Glyph> get(char symbol) {
        auto& glyph = glyphs_[symbol];
        if (!glyph) glyph = std::make_shared<const Glyph>(std::string(1, symbol));
        return glyph;
    }
};
struct PlacedGlyph {
    std::shared_ptr<const Glyph> glyph;
    int x;
    void draw() const { std::cout << glyph->shape << " at " << x << '\n'; }
};
int main() {
    GlyphPool pool;
    const PlacedGlyph first{pool.get('A'), 0};
    const PlacedGlyph second{pool.get('A'), 10};
    first.draw();
    second.draw();
    std::cout << "Shared shape: " << std::boolalpha << (first.glyph == second.glyph) << '\n';
}
```

## Example Output

```text
A at 0
A at 10
Shared shape: true
```

## When to Use

Usalo dopo aver misurato una duplicazione significativa di dati immutabili.

### Use cases

Contorni dei glifi, definizioni del terreno e identificatori internizzati sono candidati da valutare con misure.

## When NOT to Use

Evitalo per pochi dati, state individuale mutabile o ricerche più costose del risparmio.

## Advantages

Le occorrenze riutilizzano la forma mantenendo posizioni indipendenti.

## Trade-offs

Il pool trattiene gli elementi; map e [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) (Uno smart pointer con ownership condivisa; l'object viene rilasciato quando scompare l'ultimo riferimento proprietario) hanno costi. La stringa dimostrativa è piccola: non si rivendica un risparmio misurato. Il pool non è sincronizzato.

## Related Patterns

[Composite](../composite/README.it.md) · [Prototype](../../creational/prototype/README.it.md)

## Common Confusion

Prototype copia lo state in un nuovo object; Flyweight condivide intenzionalmente lo state intrinseco.

## Terms to Remember

- `Flyweight` — Condividi dati intrinseci immutabili e separa il contesto di ogni occorrenza.
- `intrinsic state` — Dati indipendenti dal contesto della singola occorrenza, condivisibili da un Flyweight. Esempio: `Glyph::shape`.
- `extrinsic state` — Dati specifici di un'occorrenza conservati fuori dal Flyweight condiviso. Esempio: `PlacedGlyph::x`.
- `Flyweight Factory` — Un servizio di ricerca che restituisce un Flyweight condiviso per una chiave. Esempio: `GlyphPool`.

## Interview Vocabulary

- [`interning`](../../GLOSSARY.md#interning) — Riutilizzare una rappresentazione per valori equivalenti attraverso un pool di ricerca.
- [`ownership`](../../GLOSSARY.md#ownership) — La responsabilità di mantenere una risorsa valida e infine rilasciarla.
- [`memory allocation`](../../GLOSSARY.md#memory-allocation) — Ottenere spazio per i dati; costi e possibilità di errore dipendono dal meccanismo.

## Interview Question

Quali campi servono nella chiave se font e dimensione cambiano la forma?

## Mini Challenge

Aggiungi il font alla chiave e verifica condivisione per chiavi uguali, separazione per font diversi.

## Quick Summary

- **Problema:** Un documento ripete molti glifi; conservare il contorno per ogni posizione spreca memoria.
- **Soluzione:** GlyphPool riutilizza Glyph per carattere; PlacedGlyph condivide un const Glyph e conserva la propria x.
- **Trade-off:** Il pool trattiene gli elementi; map e std::shared_ptr hanno costi. La stringa dimostrativa è piccola: non si rivendica un risparmio misurato. Il pool non è sincronizzato.
- **Da ricordare:** Condividi la forma, separa la posizione.

[Precedente](../../structural/facade/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/proxy/README.it.md)
