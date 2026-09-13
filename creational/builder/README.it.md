# Builder

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/abstract-factory/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/factory-method/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Un Design Pattern che riguarda la creazione e configurazione degli object.

## Difficulty

Principiante

## In One Sentence

Configura un object con passi espliciti e produci il risultato alla fine.

## In parole semplici

Con molte opzioni, una chiamata al `constructor` nasconde il significato dei valori. `Builder` raccoglie scelte con nomi chiari, le verifica e crea il risultato.

## The Problem

Una richiesta contiene endpoint, timeout e retry; aumentando le opzioni, gli argomenti posizionali diventano poco leggibili.

## Naive Solution

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## Why It Becomes a Problem

Il constructor funziona, ma numeri e booleani consecutivi nascondono il significato e rendono facili gli scambi accidentali.

## The Idea

RequestBuilder conserva le scelte. I method espliciti le raccolgono; build controlla i valori obbligatori e restituisce Request per valore.

## Real-World Analogy

Prima scegli gli ingredienti del panino, poi la cucina prepara il risultato.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Builder](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## Participants

RequestBuilder gestisce configurazione temporanea e controlli; Request possiede i dati finali. Il client ordina i passi facoltativi.

Ruoli canonici in questo esempio:

- [`Product`](../../GLOSSARY.md#product) — L'object finale prodotto dal Builder. Qui: `Request`.
- [`fluent interface`](../../GLOSSARY.md#fluent-interface) — Un'interface pensata come catena leggibile di chiamate; da sola non implica Builder. Qui: `RequestBuilder.endpoint().timeout().retry()`.
- [`constructor`](../../GLOSSARY.md#constructor) — L'operazione speciale che inizializza una nuova instance di una class. Qui: `Request::Request`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Request {
    std::string endpoint_;
    int timeout_;
    bool retry_;
public:
    Request(std::string endpoint, int timeout, bool retry)
        : endpoint_(std::move(endpoint)), timeout_(timeout), retry_(retry) {}
    void describe() const {
        std::cout << endpoint_ << " timeout=" << timeout_ << " retry=" << retry_ << '\n';
    }
};
class RequestBuilder {
    std::string endpoint_;
    int timeout_ = 30;
    bool retry_ = false;
public:
    RequestBuilder& endpoint(std::string value) { endpoint_ = std::move(value); return *this; }
    RequestBuilder& timeout(int seconds) { timeout_ = seconds; return *this; }
    RequestBuilder& retry(bool enabled) { retry_ = enabled; return *this; }
    Request build() const {
        if (endpoint_.empty() || timeout_ <= 0) throw std::invalid_argument("Invalid request");
        return Request{endpoint_, timeout_, retry_};
    }
};
int main() {
    const auto request = RequestBuilder{}.endpoint("/orders").timeout(5).retry(true).build();
    request.describe();
    try { static_cast<void>(RequestBuilder{}.build()); }
    catch (const std::invalid_argument&) { std::cout << "Invalid request rejected\n"; }
}
```

## Example Output

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## When to Use

Usalo con molte opzioni indipendenti o un punto significativo di validazione.

### Use cases

Configurazione di richieste HTTP e fixture di test; l'esempio non esegue richieste di rete.

## When NOT to Use

Evitalo per due parametri evidenti: un piccolo aggregato può bastare.

## Advantages

Le chiamate rendono visibili le scelte e build può rifiutare una configurazione incompleta.

## Trade-offs

Introduci un tipo aggiuntivo. Il constructor di Request resta public: in produzione occorre validare anche lì oppure limitarne l'accesso.

## Related Patterns

[Factory Method](../factory-method/README.it.md) · [Abstract Factory](../abstract-factory/README.it.md)

## Common Confusion

Factory Method sceglie il concrete type dentro un flusso ereditato; Builder compone la configurazione con più chiamate.

## Terms to Remember

- `Builder` — Configura un object con passi espliciti e produci il risultato alla fine.
- `Product` — L'object finale prodotto dal Builder. Esempio: `Request`.
- `fluent interface` — Un'interface pensata come catena leggibile di chiamate; da sola non implica Builder. Esempio: `RequestBuilder.endpoint().timeout().retry()`.
- `constructor` — L'operazione speciale che inizializza una nuova instance di una class. Esempio: `Request::Request`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Scegliere il tipo concreto e stabilire valori iniziali e lifetime di un object.
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — Tenere separate responsabilità di natura diversa perché possano cambiare indipendentemente.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — Concentrare un modulo su un motivo coerente di cambiamento.

## Interview Question

Una fluent interface è sempre un Builder? Individua il momento in cui termina la costruzione.

## Mini Challenge

Rifiuta timeout superiori a 120 e prova il limite e il primo valore non valido.

## Verifica cosa hai capito

1. Cosa succede chiamando Request direttamente invece di build?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Una richiesta contiene endpoint, timeout e retry; aumentando le opzioni, gli argomenti posizionali diventano poco leggibili.
- **Soluzione:** RequestBuilder conserva le scelte. I method espliciti le raccolgono; build controlla i valori obbligatori e restituisce Request per valore.
- **Trade-off:** Introduci un tipo aggiuntivo. Il constructor di Request resta public: in produzione occorre validare anche lì oppure limitarne l'accesso.
- **Da ricordare:** Scegli i passi, poi costruisci.

[Precedente](../../creational/abstract-factory/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/factory-method/README.it.md)
