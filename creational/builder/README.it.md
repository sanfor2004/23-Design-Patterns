# Costruttore graduale

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/abstract-factory/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/factory-method/README.it.md)

## Categoria

Creazionali

## Difficoltà

Principiante

## In una frase

Configura un oggetto con passi espliciti e produci il risultato alla fine.

## Il problema

Una richiesta contiene endpoint, timeout e retry; aumentando le opzioni, gli argomenti posizionali diventano poco leggibili.

## Soluzione iniziale

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## Perché diventa difficile

Il costruttore funziona, ma numeri e booleani consecutivi nascondono il significato e rendono facili gli scambi accidentali.

## Idea centrale

RequestBuilder conserva le scelte. I metodi espliciti le raccolgono; build controlla i valori obbligatori e restituisce Request per valore.

## Analogia quotidiana

Prima scegli gli ingredienti del panino, poi la cucina prepara il risultato.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Costruttore graduale](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## Partecipanti

RequestBuilder gestisce configurazione temporanea e controlli; Request possiede i dati finali. Il client ordina i passi facoltativi.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## Quando usarlo

Usalo con molte opzioni indipendenti o un punto significativo di validazione.

## Quando NON usarlo

Evitalo per due parametri evidenti: un piccolo aggregato può bastare.

## Vantaggi

Le chiamate rendono visibili le scelte e build può rifiutare una configurazione incompleta.

## Svantaggi e compromessi

Introduci un tipo aggiuntivo. Il costruttore di Request resta pubblico: in produzione occorre validare anche lì oppure limitarne l'accesso.

## Applicazioni tecniche

Configurazione di richieste HTTP e fixture di test; l'esempio non esegue richieste di rete.

## Pattern correlati

[factory-method](../factory-method/README.it.md) · [abstract-factory](../abstract-factory/README.it.md)

## Confusione comune

Factory Method sceglie il tipo concreto dentro un flusso ereditato; Builder compone la configurazione con più chiamate.

## Domanda da colloquio

Un'interfaccia fluente è sempre un Builder? Individua il momento in cui termina la costruzione.

## Piccola sfida

Rifiuta timeout superiori a 120 e prova il limite e il primo valore non valido.

## Riepilogo

- **Problema:** Una richiesta contiene endpoint, timeout e retry; aumentando le opzioni, gli argomenti posizionali diventano poco leggibili.
- **Soluzione:** RequestBuilder conserva le scelte. I metodi espliciti le raccolgono; build controlla i valori obbligatori e restituisce Request per valore.
- **Compromesso:** Introduci un tipo aggiuntivo. Il costruttore di Request resta pubblico: in produzione occorre validare anche lì oppure limitarne l'accesso.
- **Da ricordare:** Scegli i passi, poi costruisci.

[Precedente](../../creational/abstract-factory/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/factory-method/README.it.md)
