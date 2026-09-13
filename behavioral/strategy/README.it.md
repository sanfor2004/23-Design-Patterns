# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Principiante

## In One Sentence

Fornisci un algorithm sostituibile all'object che ne ha bisogno.

## In parole semplici

Il checkout può calcolare una spedizione normale o express. `Strategy` fornisce a `Checkout` l’`algorithm` scelto, così il calcolo totale non deve contenere tutte le regole.

## The Problem

Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.

## Naive Solution

```cpp
int fee = express ? (subtotal_cents >= 100 ? 0 : 15) : 5;
```

## Why It Becomes a Problem

Una condizione è leggibile; ripeterla in più percorsi rende difficili aggiunte e test.

## The Idea

Checkout possiede un callable ShippingRule e gli chiede il costo; il client sceglie alla costruzione.

## Real-World Analogy

Scegli il percorso a piedi o in auto mantenendo la stessa destinazione.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Participants

Checkout è il Context, ShippingRule il contratto, le lambda implementano tariffe standard ed express.

Ruoli canonici in questo esempio:

- [`Context`](../../GLOSSARY.md#context) — L'object che usa una Strategy o delega il behavior allo State corrente. Qui: `Checkout`.
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — Il contratto degli algorithm intercambiabili usati da un Context. Qui: `ShippingRule`.
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — Una particolare implementation della Strategy interface, anche un callable invece di una class. Qui: `standard / express lambdas`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal_cents) const {
        if (subtotal_cents < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal_cents + shipping_(subtotal_cents);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal_cents) { return subtotal_cents >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
    std::cout << "Express boundary: " << express.total(100) << '\n';
    try { static_cast<void>(standard.total(-1)); }
    catch (const std::invalid_argument&) { std::cout << "Negative subtotal rejected\n"; }
    try { const Checkout missing{ShippingRule{}}; }
    catch (const std::invalid_argument&) { std::cout << "Missing rule rejected\n"; }
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
Express boundary: 100
Negative subtotal rejected
Missing rule rejected
```

## When to Use

Usala quando gli algorithm variano indipendentemente e il client deve scegliere una politica.

### Use cases

Prezzi, function di ranking e politiche di retry sono contesti adatti.

## When NOT to Use

Evitala per un algorithm stabile o una condizione leggibile senza vera pressione di estensione.

## Advantages

Ogni politica si prova isolatamente e il calcolo totale resta condiviso.

## Trade-offs

[`std::function`](../../GLOSSARY.md#stdfunction) introduce [`type erasure`](../../GLOSSARY.md#type-erasure) e possibili [`memory allocation`](../../GLOSSARY.md#memory-allocation); template o function pointer rispondono a vincoli diversi. Valida i risultati di politiche esterne.

## Related Patterns

[State](../state/README.it.md) · [Template Method](../template-method/README.it.md)

## Common Confusion

State riguarda il [`lifecycle`](../../GLOSSARY.md#lifecycle) e transizioni; Strategy sceglie algorithm. Template Method personalizza passi ereditati anziché callable iniettati.

## Terms to Remember

- `Strategy` — Fornisci un algorithm sostituibile all'object che ne ha bisogno.
- `Context` — L'object che usa una Strategy o delega il behavior allo State corrente. Esempio: `Checkout`.
- `Strategy interface` — Il contratto degli algorithm intercambiabili usati da un Context. Esempio: `ShippingRule`.
- `Concrete Strategy` — Una particolare implementation della Strategy interface, anche un callable invece di una class. Esempio: `standard / express lambdas`.

## Interview Vocabulary

- [`interchangeable behavior`](../../GLOSSARY.md#interchangeable-behavior) — Behavior diversi fornibili attraverso lo stesso contratto.
- [`encapsulate an algorithm`](../../GLOSSARY.md#encapsulate-an-algorithm) — Racchiudere un algorithm dietro un'operazione che ne nasconde i passi interni.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — Preferire object collaboranti quando esprimono la variazione meglio di una gerarchia di inheritance.
- [`runtime selection`](../../GLOSSARY.md#runtime-selection) — Scegliere un'implementation durante l'esecuzione del programma.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Le parti conoscono solo i contratti necessari a collaborare, limitando la propagazione delle modifiche.

## Interview Question

Sostituendo std::function con un parametro template, cosa cambia per scelta a [`runtime`](../../GLOSSARY.md#runtime) e compilazione?

## Mini Challenge

Aggiungi spedizione gratuita da 80 e prova 79, 80 e 81.

## Verifica cosa hai capito

1. L’API pubblica di questo Checkout permette di cambiare regola dopo la creazione?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.
- **Soluzione:** Checkout possiede un callable ShippingRule e gli chiede il costo; il client sceglie alla costruzione.
- **Trade-off:** std::function introduce type erasure e possibili memory allocation; template o function pointer rispondono a vincoli diversi. Valida i risultati di politiche esterne.
- **Da ricordare:** Stesso compito, algorithm a scelta.

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)
