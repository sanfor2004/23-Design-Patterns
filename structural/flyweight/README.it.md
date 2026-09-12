# Oggetto condiviso leggero

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/facade/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/proxy/README.it.md)

## Categoria

Strutturali

## Difficoltà

Avanzato

## In una frase

Condividi dati intrinseci immutabili e separa il contesto di ogni occorrenza.

## Il problema

Un documento ripete molti glifi; conservare il contorno per ogni posizione spreca memoria.

## Soluzione iniziale

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Perché diventa difficile

Duplicare la forma fa crescere la memoria con le occorrenze invece che con le forme distinte.

## Idea centrale

GlyphPool riutilizza Glyph per carattere; PlacedGlyph condivide un const Glyph e conserva la propria x.

## Analogia quotidiana

Più lettori usano lo stesso libro di riferimento ma tengono segnalibri diversi.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Oggetto condiviso leggero](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## Partecipanti

Glyph contiene la forma intrinseca, GlyphPool la internizza, PlacedGlyph conserva posizione estrinseca e ownership condivisa.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
A at 0
A at 10
Shared shape: true
```

## Quando usarlo

Usalo dopo aver misurato una duplicazione significativa di dati immutabili.

## Quando NON usarlo

Evitalo per pochi dati, stato individuale mutabile o ricerche più costose del risparmio.

## Vantaggi

Le occorrenze riutilizzano la forma mantenendo posizioni indipendenti.

## Svantaggi e compromessi

Il pool trattiene gli elementi; map e shared_ptr hanno costi. La stringa dimostrativa è piccola: non si rivendica un risparmio misurato. Il pool non è sincronizzato.

## Applicazioni tecniche

Contorni dei glifi, definizioni del terreno e identificatori internizzati sono candidati da valutare con misure.

## Pattern correlati

[composite](../composite/README.it.md) · [prototype](../../creational/prototype/README.it.md)

## Confusione comune

Prototype copia lo stato in un nuovo oggetto; Flyweight condivide intenzionalmente lo stato intrinseco.

## Domanda da colloquio

Quali campi servono nella chiave se font e dimensione cambiano la forma?

## Piccola sfida

Aggiungi il font alla chiave e verifica condivisione per chiavi uguali, separazione per font diversi.

## Riepilogo

- **Problema:** Un documento ripete molti glifi; conservare il contorno per ogni posizione spreca memoria.
- **Soluzione:** GlyphPool riutilizza Glyph per carattere; PlacedGlyph condivide un const Glyph e conserva la propria x.
- **Compromesso:** Il pool trattiene gli elementi; map e shared_ptr hanno costi. La stringa dimostrativa è piccola: non si rivendica un risparmio misurato. Il pool non è sincronizzato.
- **Da ricordare:** Condividi la forma, separa la posizione.

[Precedente](../../structural/facade/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/proxy/README.it.md)
