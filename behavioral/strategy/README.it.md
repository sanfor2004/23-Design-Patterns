# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Principiante

## In One Sentence

Fornisci un algorithm sostituibile all'object che ne ha bisogno.

## The Problem

Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.

## Naive Solution

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
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

## Modern C++20 Example

```cpp
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
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
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

[`std::function`](../../GLOSSARY.md#stdfunction) (Un wrapper con type erasure che conserva un callable con una firma scelta) introduce [`type erasure`](../../GLOSSARY.md#type-erasure) (Nascondere un tipo concreto dietro un'interface uniforme a runtime, come std::function per i callable) e possibili [`memory allocation`](../../GLOSSARY.md#memory-allocation) (Ottenere spazio per i dati; costi e possibilità di errore dipendono dal meccanismo); template o function pointer rispondono a vincoli diversi. Valida i risultati di politiche esterne.

## Related Patterns

[State](../state/README.it.md) · [Template Method](../template-method/README.it.md)

## Common Confusion

State riguarda il [`lifecycle`](../../GLOSSARY.md#lifecycle) (Le fasi e transizioni modellate di un'entità del dominio, distinte dalla lifetime di un object C++) e transizioni; Strategy sceglie algorithm. Template Method personalizza passi ereditati anziché callable iniettati.

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

Sostituendo std::function con un parametro template, cosa cambia per scelta a [`runtime`](../../GLOSSARY.md#runtime) (Il periodo in cui il programma compilato è in esecuzione) e compilazione?

## Mini Challenge

Aggiungi spedizione gratuita da 80 e prova 79, 80 e 81.

## Quick Summary

- **Problema:** Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.
- **Soluzione:** Checkout possiede un callable ShippingRule e gli chiede il costo; il client sceglie alla costruzione.
- **Trade-off:** std::function introduce type erasure e possibili memory allocation; template o function pointer rispondono a vincoli diversi. Valida i risultati di politiche esterne.
- **Da ricordare:** Stesso compito, algorithm a scelta.

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)
