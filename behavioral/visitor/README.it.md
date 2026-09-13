# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/template-method/README.it.md) · [Categoria](../README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Avanzato

## In One Sentence

Aggiungi operazioni a tipi di elemento stabili tramite un Visitor separato.

## In parole semplici

Libri e alimenti richiedono calcoli fiscali diversi.Visitor raccoglie i calcoli e ogni elemento chiama il metodo per il proprio tipo.

## The Problem

Un carrello contiene libri e cibo; nuove operazioni come imposte ed export non devono riempire ogni class.

## Naive Solution

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## Why It Becomes a Problem

Aggiungere method virtual per ogni attività obbliga a modificare tutti gli elementi.

## The Idea

Ogni Item concreto chiama da accept l'overload Visitor::visit corrispondente; Tax realizza l'operazione.

## Real-World Analogy

Un ispettore visita stazioni diverse e applica una lista specifica al tipo.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## Participants

Item definisce accept; Book e Food selezionano l'overload; Visitor elenca i tipi; Tax accumula il risultato e il carrello possiede gli elementi.

Ruoli canonici in questo esempio:

- [`Element`](../../GLOSSARY.md#element) — Il contratto degli object che accettano un Visitor. Qui: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — Un'implementation di Element che seleziona l'overload di Visitor adatto al proprio tipo. Qui: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — Un'implementation di Visitor con un'operazione per ogni tipo Element supportato. Qui: `Tax`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <vector>

struct Book;
struct Food;
struct Visitor {
    virtual ~Visitor() = default;
    virtual void visit(const Book& book) = 0;
    virtual void visit(const Food& food) = 0;
};
struct Item {
    virtual ~Item() = default;
    virtual void accept(Visitor& visitor) const = 0;
};
struct Book final : Item {
    int price_cents = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Food final : Item {
    int price_cents = 10;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Tax final : Visitor {
    int total_cents = 0;
    void visit(const Book& book) override { total_cents += book.price_cents / 10; }
    void visit(const Food& food) override { total_cents += food.price_cents / 5; }
};
int main() {
    std::vector<std::unique_ptr<Item>> basket;
    basket.push_back(std::make_unique<Book>());
    basket.push_back(std::make_unique<Food>());
    Tax tax;
    for (const auto& item : basket) item->accept(tax);
    std::cout << "Tax: " << tax.total_cents << '\n';
}
```

## Example Output

```text
Tax: 4
```

## When to Use

Usalo con tipi stabili e operazioni nuove frequenti.

### Use cases

Analisi di AST ed export di documenti con tipi stabili; std::variant e std::visit sono un'alternativa per insiemi chiusi.

## When NOT to Use

Evitalo se aumentano spesso i tipi o esporre dettagli rompe l'[`encapsulation`](../../GLOSSARY.md#encapsulation).

## Advantages

Una nuova operazione richiede un Visitor, senza cambiare gli elementi esistenti.

## Trade-offs

Un nuovo tipo richiede modifiche al contratto Visitor e a tutti i Visitor. Le aliquote intere sono illustrative, non fiscali reali; l'arrotondamento richiede una politica.

## Related Patterns

[Composite](../../structural/composite/README.it.md) · [Iterator](../iterator/README.it.md)

## Common Confusion

Iterator attraversa, Visitor seleziona operazioni per tipo, Composite può fornire l'albero.

## Terms to Remember

- `Visitor` — Aggiungi operazioni a tipi di elemento stabili tramite un Visitor separato.
- `Element` — Il contratto degli object che accettano un Visitor. Esempio: `Item`.
- `Concrete Element` — Un'implementation di Element che seleziona l'overload di Visitor adatto al proprio tipo. Esempio: `Book, Food`.
- `Concrete Visitor` — Un'implementation di Visitor con un'operazione per ogni tipo Element supportato. Esempio: `Tax`.

## Interview Vocabulary

- [`double dispatch`](../../GLOSSARY.md#double-dispatch) — Selezionare behavior usando due tipi a runtime; il Visitor classico combina due chiamate virtual con overload resolution.
- [`overload resolution`](../../GLOSSARY.md#overload-resolution) — La scelta a compile time fra function omonime in base ai tipi degli argomenti.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — Mirare a open for extension, closed for modification lungo un confine scelto e utile.

## Interview Question

Perché visit(*this) dentro Book sceglie l'overload Book mentre un reference Item non basta?

## Mini Challenge

Aggiungi Label senza modificare Book e Food, poi un terzo tipo e conta le modifiche.

## Verifica cosa hai capito

1. Cosa cambia aggiungendo un tipo di elemento invece di un’operazione?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Un carrello contiene libri e cibo; nuove operazioni come imposte ed export non devono riempire ogni class.
- **Soluzione:** Ogni Item concreto chiama da accept l'overload Visitor::visit corrispondente; Tax realizza l'operazione.
- **Trade-off:** Un nuovo tipo richiede modifiche al contratto Visitor e a tutti i Visitor. Le aliquote intere sono illustrative, non fiscali reali; l'arrotondamento richiede una politica.
- **Da ricordare:** Tipi stabili, operazioni nuove.

[Precedente](../../behavioral/template-method/README.it.md) · [Categoria](../README.it.md)
