# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/decorator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/flyweight/README.it.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Un Design Pattern che organizza le relazioni fra object e class.

## Difficulty

Principiante

## In One Sentence

Offre un ingresso semplice al flusso comune di un subsystem.

## The Problem

Ogni client deve controllare disponibilità, addebitare e spedire nell'ordine giusto.

## Naive Solution

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Why It Becomes a Problem

Le chiamate dirette possono saltare i controlli o duplicare l'orchestrazione in modo incoerente.

## The Idea

Checkout espone buy e coordina i servizi interni.

## Real-World Analogy

La reception coordina una prenotazione senza farti chiamare ogni reparto.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Participants

Stock verifica la disponibilità, Payment addebita, Shipping spedisce e Checkout presenta il flusso.

Ruoli canonici in questo esempio:

- [`subsystem`](../../GLOSSARY.md#subsystem) — Un gruppo di servizi o object collaboranti dentro un sistema più ampio. Qui: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa. Qui: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — Il codice che usa un'interface o collabora con gli object del pattern. Qui: `main`.

## Modern C++20 Example

```cpp
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount) const { std::cout << "Charged " << amount << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

## Example Output

```text
Charged 20
Dispatched
Unavailable
```

## When to Use

Usala quando molti client richiedono lo stesso sottoinsieme utile di un sistema complesso.

### Use cases

Punti d'ingresso di SDK e servizi applicativi; non c'è un'integrazione di pagamento reale.

## When NOT to Use

Evitala per un semplice inoltro che non semplifica nulla.

## Advantages

I client dipendono da un contratto ridotto e da una regola d'ordine condivisa.

## Trade-offs

Può diventare un object onnipotente. L'esempio non è transazionale: errori reali richiedono compensazioni o altre strategie di consistenza.

## Related Patterns

[Adapter](../adapter/README.it.md) · [Mediator](../../behavioral/mediator/README.it.md)

## Common Confusion

Adapter risolve compatibilità, Facade riduce la superficie del subsystem senza dover rispettare un'interface preesistente.

## Terms to Remember

- `Facade` — Offre un ingresso semplice al flusso comune di un subsystem.
- `subsystem` — Un gruppo di servizi o object collaboranti dentro un sistema più ampio. Esempio: `Stock, Payment, Shipping`.
- `interface` — Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa. Esempio: `Checkout::buy`.
- `Client` — Il codice che usa un'interface o collabora con gli object del pattern. Esempio: `main`.

## Interview Vocabulary

- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — Tenere separate responsabilità di natura diversa perché possano cambiare indipendentemente.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Le parti conoscono solo i contratti necessari a collaborare, limitando la propagazione delle modifiche.
- [`trade-off`](../../GLOSSARY.md#trade-off) — Un vantaggio ottenuto rinunciando a un'altra proprietà desiderabile.

## Interview Question

Se l'addebito riesce e la spedizione fallisce, cosa può garantire buy?

## Mini Challenge

Simula un errore di spedizione e progetta un esito esplicito del rimborso.

## Quick Summary

- **Problema:** Ogni client deve controllare disponibilità, addebitare e spedire nell'ordine giusto.
- **Soluzione:** Checkout espone buy e coordina i servizi interni.
- **Trade-off:** Può diventare un object onnipotente. L'esempio non è transazionale: errori reali richiedono compensazioni o altre strategie di consistenza.
- **Da ricordare:** Un ingresso per più servizi.

[Precedente](../../structural/decorator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/flyweight/README.it.md)
