# Percorso di studio

[Catalogo dei pattern](README.it.md)

Il catalogo raggruppa per scopo. Questo percorso parte da cambiamenti piccoli e visibili, poi introduce ownership e dispatch più impegnativi.


## Un metodo di studio leggero

Studia un Design Pattern per sessione. Cerca di spiegare una scelta di progetto, senza recitare una definizione.

1. Leggi **In parole semplici**.
2. Leggi **The Problem** e **Naive Solution**. Descrivi la difficoltà prima di guardare la soluzione.
3. Leggi il codice Python e prevedi l’output.
4. Eseguilo, modifica un input o un behavior e verifica la previsione.
5. Leggi ed esegui l’esempio C++20.
6. Confronta le versioni con le note del README Python. Segui Interface, Composition, Ownership, Lifetime e scelte a Runtime.
7. Rispondi a **Interview Question** senza cercare la risposta, poi prova **Verifica cosa hai capito**.
8. Completa **Mini Challenge** in una copia per gli esperimenti.
9. Spiega in un minuto problema, limite del codice semplice, soluzione, trade-off e quando evitarla.

Passa dalla comprensione all’esempio, poi all’implementazione, alle scelte ingegneristiche e alla preparazione per il colloquio. Annota cosa cambia, cosa resta stabile e il costo della struttura aggiunta. Rivedi gli appunti il giorno dopo e prova gli [esercizi di riconoscimento](PRACTICE.md) in inglese.

Segui l’ordine numerato. Il catalogo raggruppa per categoria, non per difficoltà. Le ultime tappe introducono copia, Ownership, Lifetime, memoria condivisa, dispatch, relazioni tra tipi e global state.


1. [Strategy](behavioral/strategy/README.it.md) — Sostituisci un calcolo: Strategy rende visibile il cambiamento.
2. [Observer](behavioral/observer/README.it.md) — Collega un cambiamento ai listener e studia la loro durata.
3. [Factory Method](creational/factory-method/README.it.md) — Mantieni un flusso variando la creazione.
4. [Adapter](structural/adapter/README.it.md) — Traduci un'interface a un confine chiaro.
5. [Decorator](structural/decorator/README.it.md) — Componi behavior uno strato alla volta.
6. [Command](behavioral/command/README.it.md) — Rappresenta l'azione e assegna un posto all'annullamento.
7. [Composite](structural/composite/README.it.md) — Passa da un object a un albero.
8. [State](behavioral/state/README.it.md) — Dagli algorithm scelti passa alle transizioni del lifetime.

## Poi amplia il quadro

Continua con Facade, Builder, Template Method, Bridge, Proxy, Chain of Responsibility e Mediator: collegano delega, costruzione e coordinazione.

9. [Facade](structural/facade/README.it.md)
10. [Builder](creational/builder/README.it.md)
11. [Template Method](behavioral/template-method/README.it.md)
12. [Bridge](structural/bridge/README.it.md)
13. [Proxy](structural/proxy/README.it.md)
14. [Chain of Responsibility](behavioral/chain-of-responsibility/README.it.md)
15. [Mediator](behavioral/mediator/README.it.md)

## Concludi con trade-offs più profondi

Termina con Abstract Factory, Prototype, Memento, Iterator, Flyweight, Interpreter, Visitor e Singleton. Concentrati su copie, durata, memoria, dispatch e state globale.

16. [Abstract Factory](creational/abstract-factory/README.it.md)
17. [Prototype](creational/prototype/README.it.md)
18. [Memento](behavioral/memento/README.it.md)
19. [Iterator](behavioral/iterator/README.it.md)
20. [Flyweight](structural/flyweight/README.it.md)
21. [Interpreter](behavioral/interpreter/README.it.md)
22. [Visitor](behavioral/visitor/README.it.md)
23. [Singleton](creational/singleton/README.it.md)
