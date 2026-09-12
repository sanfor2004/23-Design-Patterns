![Sanfor2004](assets/brand/logo.svg)

# Design-Patterns-23

23 Patterns · 4 Languages · Real Examples · Simple Explanations

[Sanfor2004](https://github.com/Sanfor2004) · C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

Parti da un problema concreto. Scopri quando la soluzione semplice fatica. Comprendi il pattern, esegui il C++ e valuta se la struttura aggiuntiva serve davvero.

- [Percorso di studio](LEARNING_PATH.it.md)
- [Scheda rapida](CHEATSHEET.it.md)
- [Mappa delle relazioni](PATTERN_MAP.it.md)
- [Confronti](COMPARISONS.it.md)
- [C++20](CPP_EXAMPLES.md)

## Perché esiste questo repository

Seguire un problema concreto in un piccolo programma aiuta a capire i pattern. Motivazione, codice, output e trade-offs sono raccolti insieme per valutare se un’abstraction giustifica la complessità che introduce.

## Come orientarsi

Scegli una categoria o segui il percorso di apprendimento. Ogni directory contiene quattro traduzioni, un diagramma e una cartella `cpp/`. I collegamenti alle lingue aprono lo stesso pattern nella traduzione scelta.

## Creational Pattern

Come si creano gli object

- [Abstract Factory](creational/abstract-factory/README.it.md) — Crea object compatibili attraverso un unico contratto di famiglia. (Intermedio)
- [Builder](creational/builder/README.it.md) — Configura un object con passi espliciti e produci il risultato alla fine. (Principiante)
- [Factory Method](creational/factory-method/README.it.md) — Lascia a una subclass la scelta dell'object usato da un flusso comune. (Principiante)
- [Prototype](creational/prototype/README.it.md) — Crea un object indipendente copiando un modello già configurato. (Intermedio)
- [Singleton](creational/singleton/README.it.md) — Limita un tipo a un'unica instance accessibile, accettando il costo dello state globale. (Intermedio)

## Structural Pattern

Come si compongono gli object

- [Adapter](structural/adapter/README.it.md) — Traduce un'interface esistente nel contratto atteso dal client. (Principiante)
- [Bridge](structural/bridge/README.it.md) — Separa due dimensioni variabili e collegale tramite composition. (Intermedio)
- [Composite](structural/composite/README.it.md) — Tratta una foglia e un albero di object attraverso la stessa operazione. (Principiante)
- [Decorator](structural/decorator/README.it.md) — Aggiungi behavior avvolgendo un object con la stessa interface. (Principiante)
- [Facade](structural/facade/README.it.md) — Offre un ingresso semplice al flusso comune di un subsystem. (Principiante)
- [Flyweight](structural/flyweight/README.it.md) — Condividi dati intrinseci immutabili e separa il contesto di ogni occorrenza. (Avanzato)
- [Proxy](structural/proxy/README.it.md) — Controlla l'accesso a un object tramite un sostituto con la stessa interface. (Intermedio)

## Behavioral Pattern

Come comunicano e si comportano

- [Chain of Responsibility](behavioral/chain-of-responsibility/README.it.md) — Passa una richiesta fra gestori che possono fermarla o proseguire. (Intermedio)
- [Command](behavioral/command/README.it.md) — Trasforma un'azione in un object conservabile e invocabile in seguito. (Intermedio)
- [Interpreter](behavioral/interpreter/README.it.md) — Rappresenta un piccolo linguaggio con object che valutano le regole grammaticali. (Avanzato)
- [Iterator](behavioral/iterator/README.it.md) — Attraversa una collezione tramite un protocollo stabile. (Principiante)
- [Mediator](behavioral/mediator/README.it.md) — Sposta la coordinazione fra object pari in un object dedicato. (Intermedio)
- [Memento](behavioral/memento/README.it.md) — Salva e ripristina lo state senza esporre i dettagli dello snapshot. (Intermedio)
- [Observer](behavioral/observer/README.it.md) — Notifica gli object iscritti quando cambia ciò che seguono. (Principiante)
- [State](behavioral/state/README.it.md) — Lascia che lo state corrente determini risposta e transizioni. (Intermedio)
- [Strategy](behavioral/strategy/README.it.md) — Fornisci un algorithm sostituibile all'object che ne ha bisogno. (Principiante)
- [Template Method](behavioral/template-method/README.it.md) — Fissa la sequenza dell'algorithm lasciando alle subclass alcuni passi. (Intermedio)
- [Visitor](behavioral/visitor/README.it.md) — Aggiungi operazioni a tipi di elemento stabili tramite un Visitor separato. (Avanzato)

## Comprendi il problema. Poi introduci l'abstraction.

Un pattern è un'idea di design riutilizzabile per un problema ricorrente, non un diagramma da copiare ovunque. Parti semplice e aggiungi struttura quando un cambiamento concreto la giustifica.

1. **Incontra il problema** — Un caso concreto dà un motivo al design.
2. **Metti alla prova la semplicità** — Individua l'coupling o la duplicazione che crea attrito.
3. **Segui il design** — Segui responsibility, ownership e trade-offs.
4. **Esegui e modifica il C++** — Confronta l'output, affronta la sfida e prova i limiti.

## Risorse del repository

- [Riferimenti](REFERENCES.md)
- [Contribuire](CONTRIBUTING.md)
- [Licenza](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

Traduciamo le spiegazioni, non la terminologia. Nomi dei pattern, termini tecnici, identificatori ed espressioni da colloquio restano in inglese, spiegati in italiano.

[Glossary — termini](GLOSSARY.md)
