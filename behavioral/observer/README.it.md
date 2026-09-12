# Osservatore

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/memento/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/state/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Principiante

## In una frase

Notifica gli oggetti iscritti quando cambia ciò che seguono.

## Il problema

Il magazzino deve aggiornare le viste interessate senza conoscere ogni tipo concreto.

## Soluzione iniziale

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## Perché diventa difficile

Chiamare direttamente ogni consumatore lega il publisher all'elenco e impone modifiche a ogni aggiunta.

## Idea centrale

Stock conserva riferimenti deboli a Listener e notifica quelli ancora vivi.

## Analogia quotidiana

Gli iscritti ricevono avvisi di disponibilità finché la sottoscrizione resta attiva.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Osservatore](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## Partecipanti

Stock è il soggetto, Listener il contratto, Display l'iscritto. Il client possiede gli osservatori; weak_ptr non ne prolunga la vita.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
}
```

## Output previsto

```text
Stock: 4
Expired listener skipped
```

## Quando usarlo

Usalo quando un cambiamento interessa più consumatori registrati indipendentemente.

## Quando NON usarlo

Evitalo per una sola dipendenza fissa o quando serve consistenza transazionale rigorosa.

## Vantaggi

Gli iscritti cambiano senza modificare il publisher.

## Svantaggi e compromessi

Ordine ed eccezioni richiedono una politica. Il demo sincrono propaga eccezioni e non è thread-safe; la copia dell'elenco tollera nuove iscrizioni ma non impedisce notifiche ricorsive.

## Applicazioni tecniche

Aggiornamenti UI ed eventi locali; le garanzie distribuite sono un problema distinto.

## Pattern correlati

[mediator](../mediator/README.it.md) · [state](../state/README.it.md)

## Confusione comune

Mediator definisce coordinazione fra pari noti; Observer diffonde eventi senza prescrivere i rapporti fra iscritti.

## Domanda da colloquio

Perché conservare weak_ptr e usare lock per ottenere shared_ptr durante il callback?

## Piccola sfida

Registra due listener, distruggine uno e verifica le notifiche al superstite; definisci unsubscribe esplicito.

## Riepilogo

- **Problema:** Il magazzino deve aggiornare le viste interessate senza conoscere ogni tipo concreto.
- **Soluzione:** Stock conserva riferimenti deboli a Listener e notifica quelli ancora vivi.
- **Compromesso:** Ordine ed eccezioni richiedono una politica. Il demo sincrono propaga eccezioni e non è thread-safe; la copia dell'elenco tollera nuove iscrizioni ma non impedisce notifiche ricorsive.
- **Da ricordare:** Pubblica il cambiamento, lascia reagire.

[Precedente](../../behavioral/memento/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/state/README.it.md)
