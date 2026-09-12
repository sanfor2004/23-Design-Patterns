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

Seguire un problema concreto in un piccolo programma aiuta a capire i pattern. Motivazione, codice, output e compromessi sono raccolti insieme per valutare se un’astrazione giustifica la complessità che introduce.

## Come orientarsi

Scegli una categoria o segui il percorso di apprendimento. Ogni directory contiene quattro traduzioni, un diagramma e una cartella `cpp/`. I collegamenti alle lingue aprono lo stesso pattern nella traduzione scelta.

## Creazionali

Come si creano gli oggetti

- [Fabbrica astratta](creational/abstract-factory/README.it.md) — Crea oggetti compatibili attraverso un unico contratto di famiglia. (Intermedio)
- [Costruttore graduale](creational/builder/README.it.md) — Configura un oggetto con passi espliciti e produci il risultato alla fine. (Principiante)
- [Metodo fabbrica](creational/factory-method/README.it.md) — Lascia a una sottoclasse la scelta dell'oggetto usato da un flusso comune. (Principiante)
- [Prototipo](creational/prototype/README.it.md) — Crea un oggetto indipendente copiando un modello già configurato. (Intermedio)
- [Istanza unica](creational/singleton/README.it.md) — Limita un tipo a un'unica istanza accessibile, accettando il costo dello stato globale. (Intermedio)

## Strutturali

Come si compongono gli oggetti

- [Adattatore](structural/adapter/README.it.md) — Traduce un'interfaccia esistente nel contratto atteso dal client. (Principiante)
- [Ponte](structural/bridge/README.it.md) — Separa due dimensioni variabili e collegale tramite composizione. (Intermedio)
- [Composito](structural/composite/README.it.md) — Tratta una foglia e un albero di oggetti attraverso la stessa operazione. (Principiante)
- [Decoratore](structural/decorator/README.it.md) — Aggiungi comportamento avvolgendo un oggetto con la stessa interfaccia. (Principiante)
- [Facciata](structural/facade/README.it.md) — Offre un ingresso semplice al flusso comune di un sottosistema. (Principiante)
- [Oggetto condiviso leggero](structural/flyweight/README.it.md) — Condividi dati intrinseci immutabili e separa il contesto di ogni occorrenza. (Avanzato)
- [Procuratore](structural/proxy/README.it.md) — Controlla l'accesso a un oggetto tramite un sostituto con la stessa interfaccia. (Intermedio)

## Comportamentali

Come comunicano e si comportano

- [Catena di responsabilità](behavioral/chain-of-responsibility/README.it.md) — Passa una richiesta fra gestori che possono fermarla o proseguire. (Intermedio)
- [Comando](behavioral/command/README.it.md) — Trasforma un'azione in un oggetto conservabile e invocabile in seguito. (Intermedio)
- [Interprete](behavioral/interpreter/README.it.md) — Rappresenta un piccolo linguaggio con oggetti che valutano le regole grammaticali. (Avanzato)
- [Iteratore](behavioral/iterator/README.it.md) — Attraversa una collezione tramite un protocollo stabile. (Principiante)
- [Mediatore](behavioral/mediator/README.it.md) — Sposta la coordinazione fra oggetti pari in un oggetto dedicato. (Intermedio)
- [Promemoria](behavioral/memento/README.it.md) — Salva e ripristina lo stato senza esporre i dettagli dello snapshot. (Intermedio)
- [Osservatore](behavioral/observer/README.it.md) — Notifica gli oggetti iscritti quando cambia ciò che seguono. (Principiante)
- [Stato](behavioral/state/README.it.md) — Lascia che lo stato corrente determini risposta e transizioni. (Intermedio)
- [Strategia](behavioral/strategy/README.it.md) — Fornisci un algoritmo sostituibile all'oggetto che ne ha bisogno. (Principiante)
- [Metodo modello](behavioral/template-method/README.it.md) — Fissa la sequenza dell'algoritmo lasciando alle sottoclassi alcuni passi. (Intermedio)
- [Visitatore](behavioral/visitor/README.it.md) — Aggiungi operazioni a tipi di elemento stabili tramite un visitatore separato. (Avanzato)

## Comprendi il problema. Poi introduci l'astrazione.

Un pattern è un'idea di design riutilizzabile per un problema ricorrente, non un diagramma da copiare ovunque. Parti semplice e aggiungi struttura quando un cambiamento concreto la giustifica.

1. **Incontra il problema** — Un caso concreto dà un motivo al design.
2. **Metti alla prova la semplicità** — Individua l'accoppiamento o la duplicazione che crea attrito.
3. **Segui il design** — Segui responsabilità, ownership e compromessi.
4. **Esegui e modifica il C++** — Confronta l'output, affronta la sfida e prova i limiti.

## Risorse del repository

- [Riferimenti](REFERENCES.md)
- [Contribuire](CONTRIBUTING.md)
- [Licenza](LICENSE)
- [C++20](CPP_EXAMPLES.md)
