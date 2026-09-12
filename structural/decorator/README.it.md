# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/composite/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/facade/README.it.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Un Design Pattern che organizza le relazioni fra object e class.

## Difficulty

Principiante

## In One Sentence

Aggiungi behavior avvolgendo un object con la stessa [`interface`](../../GLOSSARY.md#interface) (Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa).

## The Problem

Un caffè può avere una o più dosi di latte senza creare una class per ogni combinazione.

## Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why It Becomes a Problem

Le class dedicate duplicano il prezzo base e crescono con gli extra.

## The Idea

Milk possiede un Drink, delega e aggiunge descrizione e prezzo.

## Real-World Analogy

Ogni strato di carta avvolge il pacco precedente, che rimane un pacco.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Participants

Drink è il contratto, Coffee il behavior base, Milk avvolge un solo Drink; il client possiede lo strato esterno.

Ruoli canonici in questo esempio:

- [`Component`](../../GLOSSARY.md#component) — Il contratto comune esposto da foglie, gruppi o wrapper. Qui: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — L'implementation di base prima dell'aggiunta di wrapper facoltativi. Qui: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — Un wrapper che mantiene il contratto Component e aggiunge una responsibility specifica. Qui: `Milk`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price() const override { return inner_->price() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use

Usalo per behavior facoltativi e componibili che rispettano il contratto originale.

### Use cases

Stream con compressione o cifratura: ordine e gestione degli errori sono essenziali.

## When NOT to Use

Evitalo se bastano una lista di ingredienti e una somma; qui lo scopo è mostrare la struttura.

## Advantages

Componi gli extra a [`runtime`](../../GLOSSARY.md#runtime) (Il periodo in cui il programma compilato è in esecuzione) mantenendo piccola l'[`implementation`](../../GLOSSARY.md#implementation) (Il codice concreto che esegue un'operazione o soddisfa un'interface) base.

## Trade-offs

L'ordine può cambiare il behavior. Molti piccoli object complicano il debug; la stessa interface non garantisce tutte le promesse semantiche.

## Related Patterns

[Proxy](../proxy/README.it.md) · [Composite](../composite/README.it.md)

## Common Confusion

Proxy controlla l'accesso, Decorator aggiunge responsibility. La forma del wrapper non basta a riconoscerne l'intento.

## Terms to Remember

- `Decorator` — Aggiungi behavior avvolgendo un object con la stessa interface.
- `Component` — Il contratto comune esposto da foglie, gruppi o wrapper. Esempio: `Drink`.
- `Concrete Component` — L'implementation di base prima dell'aggiunta di wrapper facoltativi. Esempio: `Coffee`.
- `Concrete Decorator` — Un wrapper che mantiene il contratto Component e aggiunge una responsibility specifica. Esempio: `Milk`.

## Interview Vocabulary

- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — Preferire object collaboranti quando esprimono la variazione meglio di una gerarchia di inheritance.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — Costruire ricorsivamente una struttura con parti che espongono il contratto dell'insieme.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — Concentrare un modulo su un motivo coerente di cambiamento.

## Interview Question

Registrare dati prima e dopo la cifratura mostra le stesse informazioni?

## Mini Challenge

Aggiungi Syrup con costo 3, prova due ordini e spiega le descrizioni ottenute.

## Quick Summary

- **Problema:** Un caffè può avere una o più dosi di latte senza creare una class per ogni combinazione.
- **Soluzione:** Milk possiede un Drink, delega e aggiunge descrizione e prezzo.
- **Trade-off:** L'ordine può cambiare il behavior. Molti piccoli object complicano il debug; la stessa interface non garantisce tutte le promesse semantiche.
- **Da ricordare:** Stesso contratto, uno strato in più.

[Precedente](../../structural/composite/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/facade/README.it.md)
