# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/singleton/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/bridge/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Un Design Pattern che organizza le relazioni fra object e class.

## Difficulty

Principiante

## In One Sentence

Traduce un'[`interface`](../../GLOSSARY.md#interface) esistente nel contratto atteso dal client.

## In parole semplici

Il sensore restituisce Fahrenheit, mentre il display richiede Celsius.Adapter converte chiamata e valore senza modificare le due parti.

## The Problem

Il pannello usa Celsius, ma un sensore esistente espone Fahrenheit.

## Naive Solution

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Why It Becomes a Problem

Passare il numero direttamente mostra l'unità sbagliata; ripetere la formula disperde la regola di compatibilità.

## The Idea

Implementa Temperature intorno a un LegacyThermometer preso in prestito e converti al confine.

## Real-World Analogy

Come un adattatore da viaggio, ma qui cambia anche il significato del valore.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Adapter](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## Participants

Temperature è il contratto atteso, LegacyThermometer l'API esistente. CelsiusAdapter la usa senza possederla; display conosce solo Temperature.

Ruoli canonici in questo esempio:

- [`Target`](../../GLOSSARY.md#target) — L'interface attesa dal Client. Qui: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — L'object esistente la cui interface deve essere adattata. Qui: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa. Qui: `Temperature`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <stdexcept>

class LegacyThermometer {
public:
    double fahrenheit() const { return 77.0; }
};
struct Temperature {
    virtual ~Temperature() = default;
    virtual double celsius() const = 0;
};
class CelsiusAdapter final : public Temperature {
    const LegacyThermometer& sensor_;
public:
    explicit CelsiusAdapter(const LegacyThermometer& sensor) : sensor_(sensor) {}
    double celsius() const override { return (sensor_.fahrenheit() - 32.0) * 5.0 / 9.0; }
};
void display(const Temperature& temperature) {
    std::cout << temperature.celsius() << " C\n";
}
int main() {
    const LegacyThermometer sensor;
    const CelsiusAdapter adapter{sensor};
    display(adapter);
}
```

## Example Output

```text
25 C
```

## When to Use

Usalo al confine con un'API che non puoi o non conviene modificare.

### Use cases

Integrazione di API legacy e conversioni di unità; precisione ed errori richiedono comunque un contratto.

## When NOT to Use

Evitalo se controlli entrambe le parti e puoi uniformare facilmente il contratto.

## Advantages

La conversione resta centralizzata e display accetta altre [`implementation`](../../GLOSSARY.md#implementation).

## Trade-offs

Rinominare method può nascondere differenze semantiche. Il sensore deve vivere più di CelsiusAdapter, che conserva un non-owning reference.

## Related Patterns

[Facade](../facade/README.it.md) · [Bridge](../bridge/README.it.md)

## Common Confusion

Facade semplifica un subsystem; Adapter rende compatibile una specifica interface.

## Terms to Remember

- `Adapter` — Traduce un'interface esistente nel contratto atteso dal client.
- `Target` — L'interface attesa dal Client. Esempio: `Temperature`.
- `Adaptee` — L'object esistente la cui interface deve essere adattata. Esempio: `LegacyThermometer`.
- `interface` — Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa. Esempio: `Temperature`.

## Interview Vocabulary

- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — Dipendere dal contratto promesso anziché da una particolare implementation concreta.
- [`delegation`](../../GLOSSARY.md#delegation) — Un object affida parte del proprio lavoro a un collaboratore.
- [`lifetime`](../../GLOSSARY.md#lifetime) — L'intervallo in cui un object esiste e può essere usato secondo le sue regole.

## Interview Question

Puoi sempre preservare il behavior adattando un'API asincrona a una sincrona?

## Mini Challenge

Rendi configurabile la temperatura Fahrenheit e prova congelamento ed ebollizione.

## Verifica cosa hai capito

1. Chi converte le unità e chi mantiene in vita il sensore?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Il pannello usa Celsius, ma un sensore esistente espone Fahrenheit.
- **Soluzione:** Implementa Temperature intorno a un LegacyThermometer preso in prestito e converti al confine.
- **Trade-off:** Rinominare method può nascondere differenze semantiche. Il sensore deve vivere più di CelsiusAdapter, che conserva un non-owning reference.
- **Da ricordare:** Traduci al confine.

[Precedente](../../creational/singleton/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/bridge/README.it.md)
