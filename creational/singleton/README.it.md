# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/prototype/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/adapter/README.it.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Un Design Pattern che riguarda la creazione e configurazione degli object.

## Difficulty

Intermedio

## In One Sentence

Limita un tipo a un'unica instance accessibile, accettando il costo dello state globale.

## The Problem

Due contatori creati separatamente dividono un totale che dovrebbe appartenere all'intero processo.

## Naive Solution

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Why It Becomes a Problem

Un constructor public consente a ogni client di creare il proprio contatore e perdere la condivisione desiderata.

## The Idea

Nascondi la costruzione, vieta la copia e restituisci un object statico locale da instance.

## Real-World Analogy

Un piccolo ufficio usa un solo registro visitatori, condiviso da tutti gli sportelli.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Singleton](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## Participants

Metrics controlla il proprio [`lifetime`](../../GLOSSARY.md#lifetime) (L'intervallo in cui un object esiste e può essere usato secondo le sue regole) e conserva il conteggio. instance restituisce un non-owning reference, da non eliminare.

Ruoli canonici in questo esempio:

- [`instance`](../../GLOSSARY.md#instance) — Un particolare object appartenente a un tipo. Qui: `Metrics::instance()`.
- [`global state`](../../GLOSSARY.md#global-state) — Dati accessibili da molte parti del programma, le cui modifiche possono influire su codice distante. Qui: `Metrics::requests_`.
- [`thread-safe initialization`](../../GLOSSARY.md#thread-safe-initialization) — Inizializzazione protetta dalla costruzione concorrente; non rende thread-safe le operazioni successive. Qui: `static Metrics metrics`.

## Modern C++20 Example

```cpp
#include <iostream>

class Metrics {
    int requests_ = 0;
    Metrics() = default;
public:
    Metrics(const Metrics&) = delete;
    Metrics& operator=(const Metrics&) = delete;
    static Metrics& instance() {
        static Metrics metrics;
        return metrics;
    }
    void record() { ++requests_; }
    int requests() const { return requests_; }
};
int main() {
    auto& first = Metrics::instance();
    auto& second = Metrics::instance();
    first.record();
    second.record();
    std::cout << "Same instance: " << std::boolalpha << (&first == &second) << '\n';
    std::cout << "Requests: " << first.requests() << '\n';
}
```

## Example Output

```text
Same instance: true
Requests: 2
```

## When to Use

Consideralo solo se l'unicità è davvero un vincolo del processo e il lifetime è appropriato.

### Use cases

Il contatore diagnostico a thread singolo mostra il meccanismo, non una raccomandazione per metriche di produzione.

## When NOT to Use

Evitalo per rendere comodo l'accesso alle dependency: passa un reference esplicito per isolare i test.

## Advantages

L'inizializzazione ha un punto definito e tutti raggiungono lo stesso object.

## Trade-offs

L'accesso globale nasconde dependency e mescola i test. L'inizializzazione statica locale è sicura fra thread, record no: serve sincronizzazione. Anche l'ordine di distruzione può contare.

## Related Patterns

[Abstract Factory](../abstract-factory/README.it.md) · [Facade](../../structural/facade/README.it.md)

## Common Confusion

Un solo object gestito tramite [`dependency injection`](../../GLOSSARY.md#dependency-injection) (Fornire una dependency dall'esterno invece di sceglierla o costruirla nel codice che la usa) non implica Singleton: il tipo può non imporre l'unicità.

## Terms to Remember

- `Singleton` — Limita un tipo a un'unica instance accessibile, accettando il costo dello state globale.
- `instance` — Un particolare object appartenente a un tipo. Esempio: `Metrics::instance()`.
- `global state` — Dati accessibili da molte parti del programma, le cui modifiche possono influire su codice distante. Esempio: `Metrics::requests_`.
- `thread-safe initialization` — Inizializzazione protetta dalla costruzione concorrente; non rende thread-safe le operazioni successive. Esempio: `static Metrics metrics`.

## Interview Vocabulary

- [`dependency injection`](../../GLOSSARY.md#dependency-injection) — Fornire una dependency dall'esterno invece di sceglierla o costruirla nel codice che la usa.
- [`testability`](../../GLOSSARY.md#testability) — Quanto è facile isolare, esercitare e verificare un behavior.
- [`lifetime`](../../GLOSSARY.md#lifetime) — L'intervallo in cui un object esiste e può essere usato secondo le sue regole.

## Interview Question

L'inizializzazione sicura fra thread rende sicuro requests_? Distingui le operazioni.

## Mini Challenge

Passa esplicitamente un contatore a due job, poi prova due contatori isolati.

## Quick Summary

- **Problema:** Due contatori creati separatamente dividono un totale che dovrebbe appartenere all'intero processo.
- **Soluzione:** Nascondi la costruzione, vieta la copia e restituisci un object statico locale da instance.
- **Trade-off:** L'accesso globale nasconde dependency e mescola i test. L'inizializzazione statica locale è sicura fra thread, record no: serve sincronizzazione. Anche l'ordine di distruzione può contare.
- **Da ricordare:** Una sola instance può creare molti problemi.

[Precedente](../../creational/prototype/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/adapter/README.it.md)
