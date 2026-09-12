# Chain of Responsibility

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/proxy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/command/README.it.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Intermedio

## In One Sentence

Passa una richiesta fra gestori che possono fermarla o proseguire.

## The Problem

Una richiesta deve superare autenticazione e limiti di spesa, con politiche diverse per ingresso.

## Naive Solution

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## Why It Becomes a Problem

Una singola espressione inizialmente basta; copiarla in più flussi rende difficili ordine e riuso.

## The Idea

Ogni Handler controlla la propria regola e delega solo se passa; l'ultimo successo accetta.

## Real-World Analogy

L'assistenza risolve una richiesta o la passa allo specialista successivo.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Chain of Responsibility](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## Participants

Handler possiede il successore, Auth controlla l'identità, Limit l'importo; il client decide l'ordine.

Ruoli canonici in questo esempio:

- [`Handler`](../../GLOSSARY.md#handler) — Un ruolo che elabora una richiesta o la passa al successore. Qui: `Handler`.
- [`Concrete Handler`](../../GLOSSARY.md#concrete-handler) — Un Handler che implementa una specifica regola di elaborazione. Qui: `Auth, Limit`.
- [`chain termination`](../../GLOSSARY.md#chain-termination) — La regola che ferma una catena e stabilisce cosa succede dopo l'ultimo Handler. Qui: `Handler::handle`.

## Modern C++20 Example

```cpp
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount; };
class Handler {
    std::unique_ptr<Handler> next_;
protected:
    virtual bool accepts(const Request& request) const = 0;
public:
    explicit Handler(std::unique_ptr<Handler> next = {}) : next_(std::move(next)) {}
    virtual ~Handler() = default;
    bool handle(const Request& request) const {
        if (!accepts(request)) return false;
        return next_ ? next_->handle(request) : true;
    }
};
class Auth final : public Handler {
    bool accepts(const Request& request) const override { return request.authenticated; }
public:
    using Handler::Handler;
};
class Limit final : public Handler {
    bool accepts(const Request& request) const override { return request.amount > 0 && request.amount <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

## Example Output

```text
Rejected
Rejected
Accepted
```

## When to Use

Usala quando ordine e [`composition`](../../GLOSSARY.md#composition) (Costruire behavior collegando object che usano o contengono altri object) dei controlli devono variare indipendentemente.

### Use cases

Pipeline di validazione e middleware; questa variante richiede l'approvazione di tutti, non il primo gestore capace.

## When NOT to Use

Evitala per due controlli fissi in un solo punto: l'espressione iniziale è più chiara.

## Advantages

I controlli diventano riutilizzabili e riordinabili.

## Trade-offs

L'ordine conta e la fine della catena richiede una politica. Qui tutti devono approvare; altre catene rifiutano richieste non gestite.

## Related Patterns

[Decorator](../../structural/decorator/README.it.md) · [Command](../command/README.it.md)

## Common Confusion

Decorator aggiunge strati; la catena può fermarsi prima. Command rappresenta invece la richiesta come object.

## Terms to Remember

- `Chain of Responsibility` — Passa una richiesta fra gestori che possono fermarla o proseguire.
- `Handler` — Un ruolo che elabora una richiesta o la passa al successore. Esempio: `Handler`.
- `Concrete Handler` — Un Handler che implementa una specifica regola di elaborazione. Esempio: `Auth, Limit`.
- `chain termination` — La regola che ferma una catena e stabilisce cosa succede dopo l'ultimo Handler. Esempio: `Handler::handle`.

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — Un object affida parte del proprio lavoro a un collaboratore.
- [`object composition`](../../GLOSSARY.md#object-composition) — Collegare object per costruire una struttura o un comportamento più ampio.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Le parti conoscono solo i contratti necessari a collaborare, limitando la propagazione delle modifiche.

## Interview Question

Cosa costa mettere un Limit oneroso prima di Auth per richieste anonime?

## Mini Challenge

Aggiungi un controllo di manutenzione e verifica che un rifiuto blocchi i successivi.

## Quick Summary

- **Problema:** Una richiesta deve superare autenticazione e limiti di spesa, con politiche diverse per ingresso.
- **Soluzione:** Ogni Handler controlla la propria regola e delega solo se passa; l'ultimo successo accetta.
- **Trade-off:** L'ordine conta e la fine della catena richiede una politica. Qui tutti devono approvare; altre catene rifiutano richieste non gestite.
- **Da ricordare:** Gestisci oppure passa avanti.

[Precedente](../../structural/proxy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/command/README.it.md)
