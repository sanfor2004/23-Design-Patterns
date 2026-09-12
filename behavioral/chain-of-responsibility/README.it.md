# Catena di responsabilità

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/proxy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/command/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Intermedio

## In una frase

Passa una richiesta fra gestori che possono fermarla o proseguire.

## Il problema

Una richiesta deve superare autenticazione e limiti di spesa, con politiche diverse per ingresso.

## Soluzione iniziale

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## Perché diventa difficile

Una singola espressione inizialmente basta; copiarla in più flussi rende difficili ordine e riuso.

## Idea centrale

Ogni Handler controlla la propria regola e delega solo se passa; l'ultimo successo accetta.

## Analogia quotidiana

L'assistenza risolve una richiesta o la passa allo specialista successivo.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Catena di responsabilità](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## Partecipanti

Handler possiede il successore, Auth controlla l'identità, Limit l'importo; il client decide l'ordine.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Rejected
Rejected
Accepted
```

## Quando usarlo

Usala quando ordine e composizione dei controlli devono variare indipendentemente.

## Quando NON usarlo

Evitala per due controlli fissi in un solo punto: l'espressione iniziale è più chiara.

## Vantaggi

I controlli diventano riutilizzabili e riordinabili.

## Svantaggi e compromessi

L'ordine conta e la fine della catena richiede una politica. Qui tutti devono approvare; altre catene rifiutano richieste non gestite.

## Applicazioni tecniche

Pipeline di validazione e middleware; questa variante richiede l'approvazione di tutti, non il primo gestore capace.

## Pattern correlati

[decorator](../../structural/decorator/README.it.md) · [command](../command/README.it.md)

## Confusione comune

Decorator aggiunge strati; la catena può fermarsi prima. Command rappresenta invece la richiesta come oggetto.

## Domanda da colloquio

Cosa costa mettere un Limit oneroso prima di Auth per richieste anonime?

## Piccola sfida

Aggiungi un controllo di manutenzione e verifica che un rifiuto blocchi i successivi.

## Riepilogo

- **Problema:** Una richiesta deve superare autenticazione e limiti di spesa, con politiche diverse per ingresso.
- **Soluzione:** Ogni Handler controlla la propria regola e delega solo se passa; l'ultimo successo accetta.
- **Compromesso:** L'ordine conta e la fine della catena richiede una politica. Qui tutti devono approvare; altre catene rifiutano richieste non gestite.
- **Da ricordare:** Gestisci oppure passa avanti.

[Precedente](../../structural/proxy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/command/README.it.md)
