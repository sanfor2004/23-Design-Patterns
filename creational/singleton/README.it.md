# Istanza unica

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/prototype/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/adapter/README.it.md)

## Categoria

Creazionali

## Difficoltà

Intermedio

## In una frase

Limita un tipo a un'unica istanza accessibile, accettando il costo dello stato globale.

## Il problema

Due contatori creati separatamente dividono un totale che dovrebbe appartenere all'intero processo.

## Soluzione iniziale

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Perché diventa difficile

Un costruttore pubblico consente a ogni client di creare il proprio contatore e perdere la condivisione desiderata.

## Idea centrale

Nascondi la costruzione, vieta la copia e restituisci un oggetto statico locale da instance.

## Analogia quotidiana

Un piccolo ufficio usa un solo registro visitatori, condiviso da tutti gli sportelli.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Istanza unica](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## Partecipanti

Metrics controlla il proprio ciclo di vita e conserva il conteggio. instance restituisce un riferimento non proprietario, da non eliminare.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Same instance: true
Requests: 2
```

## Quando usarlo

Consideralo solo se l'unicità è davvero un vincolo del processo e il ciclo di vita è appropriato.

## Quando NON usarlo

Evitalo per rendere comodo l'accesso alle dipendenze: passa un riferimento esplicito per isolare i test.

## Vantaggi

L'inizializzazione ha un punto definito e tutti raggiungono lo stesso oggetto.

## Svantaggi e compromessi

L'accesso globale nasconde dipendenze e mescola i test. L'inizializzazione statica locale è sicura fra thread, record no: serve sincronizzazione. Anche l'ordine di distruzione può contare.

## Applicazioni tecniche

Il contatore diagnostico a thread singolo mostra il meccanismo, non una raccomandazione per metriche di produzione.

## Pattern correlati

[abstract-factory](../abstract-factory/README.it.md) · [facade](../../structural/facade/README.it.md)

## Confusione comune

Un solo oggetto gestito tramite dependency injection non implica Singleton: il tipo può non imporre l'unicità.

## Domanda da colloquio

L'inizializzazione sicura fra thread rende sicuro requests_? Distingui le operazioni.

## Piccola sfida

Passa esplicitamente un contatore a due job, poi prova due contatori isolati.

## Riepilogo

- **Problema:** Due contatori creati separatamente dividono un totale che dovrebbe appartenere all'intero processo.
- **Soluzione:** Nascondi la costruzione, vieta la copia e restituisci un oggetto statico locale da instance.
- **Compromesso:** L'accesso globale nasconde dipendenze e mescola i test. L'inizializzazione statica locale è sicura fra thread, record no: serve sincronizzazione. Anche l'ordine di distruzione può contare.
- **Da ricordare:** Una sola istanza può creare molti problemi.

[Precedente](../../creational/prototype/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/adapter/README.it.md)
