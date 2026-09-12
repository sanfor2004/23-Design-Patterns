# Facciata

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/decorator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/flyweight/README.it.md)

## Categoria

Strutturali

## Difficoltà

Principiante

## In una frase

Offre un ingresso semplice al flusso comune di un sottosistema.

## Il problema

Ogni client deve controllare disponibilità, addebitare e spedire nell'ordine giusto.

## Soluzione iniziale

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Perché diventa difficile

Le chiamate dirette possono saltare i controlli o duplicare l'orchestrazione in modo incoerente.

## Idea centrale

Checkout espone buy e coordina i servizi interni.

## Analogia quotidiana

La reception coordina una prenotazione senza farti chiamare ogni reparto.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Facciata](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Partecipanti

Stock verifica la disponibilità, Payment addebita, Shipping spedisce e Checkout presenta il flusso.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Charged 20
Dispatched
Unavailable
```

## Quando usarlo

Usala quando molti client richiedono lo stesso sottoinsieme utile di un sistema complesso.

## Quando NON usarlo

Evitala per un semplice inoltro che non semplifica nulla.

## Vantaggi

I client dipendono da un contratto ridotto e da una regola d'ordine condivisa.

## Svantaggi e compromessi

Può diventare un oggetto onnipotente. L'esempio non è transazionale: errori reali richiedono compensazioni o altre strategie di consistenza.

## Applicazioni tecniche

Punti d'ingresso di SDK e servizi applicativi; non c'è un'integrazione di pagamento reale.

## Pattern correlati

[adapter](../adapter/README.it.md) · [mediator](../../behavioral/mediator/README.it.md)

## Confusione comune

Adapter risolve compatibilità, Facade riduce la superficie del sottosistema senza dover rispettare un'interfaccia preesistente.

## Domanda da colloquio

Se l'addebito riesce e la spedizione fallisce, cosa può garantire buy?

## Piccola sfida

Simula un errore di spedizione e progetta un esito esplicito del rimborso.

## Riepilogo

- **Problema:** Ogni client deve controllare disponibilità, addebitare e spedire nell'ordine giusto.
- **Soluzione:** Checkout espone buy e coordina i servizi interni.
- **Compromesso:** Può diventare un oggetto onnipotente. L'esempio non è transazionale: errori reali richiedono compensazioni o altre strategie di consistenza.
- **Da ricordare:** Un ingresso per più servizi.

[Precedente](../../structural/decorator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/flyweight/README.it.md)
