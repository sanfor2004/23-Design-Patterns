# Decoratore

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/composite/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/facade/README.it.md)

## Categoria

Strutturali

## Difficoltà

Principiante

## In una frase

Aggiungi comportamento avvolgendo un oggetto con la stessa interfaccia.

## Il problema

Un caffè può avere una o più dosi di latte senza creare una classe per ogni combinazione.

## Soluzione iniziale

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Perché diventa difficile

Le classi dedicate duplicano il prezzo base e crescono con gli extra.

## Idea centrale

Milk possiede un Drink, delega e aggiunge descrizione e prezzo.

## Analogia quotidiana

Ogni strato di carta avvolge il pacco precedente, che rimane un pacco.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Decoratore](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Partecipanti

Drink è il contratto, Coffee il comportamento base, Milk avvolge un solo Drink; il client possiede lo strato esterno.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
coffee + milk + milk: 14
```

## Quando usarlo

Usalo per comportamenti facoltativi e componibili che rispettano il contratto originale.

## Quando NON usarlo

Evitalo se bastano una lista di ingredienti e una somma; qui lo scopo è mostrare la struttura.

## Vantaggi

Componi gli extra a runtime mantenendo piccola l'implementazione base.

## Svantaggi e compromessi

L'ordine può cambiare il comportamento. Molti piccoli oggetti complicano il debug; la stessa interfaccia non garantisce tutte le promesse semantiche.

## Applicazioni tecniche

Stream con compressione o cifratura: ordine e gestione degli errori sono essenziali.

## Pattern correlati

[proxy](../proxy/README.it.md) · [composite](../composite/README.it.md)

## Confusione comune

Proxy controlla l'accesso, Decorator aggiunge responsabilità. La forma del wrapper non basta a riconoscerne l'intento.

## Domanda da colloquio

Registrare dati prima e dopo la cifratura mostra le stesse informazioni?

## Piccola sfida

Aggiungi Syrup con costo 3, prova due ordini e spiega le descrizioni ottenute.

## Riepilogo

- **Problema:** Un caffè può avere una o più dosi di latte senza creare una classe per ogni combinazione.
- **Soluzione:** Milk possiede un Drink, delega e aggiunge descrizione e prezzo.
- **Compromesso:** L'ordine può cambiare il comportamento. Molti piccoli oggetti complicano il debug; la stessa interfaccia non garantisce tutte le promesse semantiche.
- **Da ricordare:** Stesso contratto, uno strato in più.

[Precedente](../../structural/composite/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/facade/README.it.md)
