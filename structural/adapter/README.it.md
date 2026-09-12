# Adattatore

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/singleton/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/bridge/README.it.md)

## Categoria

Strutturali

## Difficoltà

Principiante

## In una frase

Traduce un'interfaccia esistente nel contratto atteso dal client.

## Il problema

Il pannello usa Celsius, ma un sensore esistente espone Fahrenheit.

## Soluzione iniziale

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Perché diventa difficile

Passare il numero direttamente mostra l'unità sbagliata; ripetere la formula disperde la regola di compatibilità.

## Idea centrale

Implementa Temperature intorno a un LegacyThermometer preso in prestito e converti al confine.

## Analogia quotidiana

Come un adattatore da viaggio, ma qui cambia anche il significato del valore.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Adattatore](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## Partecipanti

Temperature è il contratto atteso, LegacyThermometer l'API esistente. CelsiusAdapter la usa senza possederla; display conosce solo Temperature.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
25 C
```

## Quando usarlo

Usalo al confine con un'API che non puoi o non conviene modificare.

## Quando NON usarlo

Evitalo se controlli entrambe le parti e puoi uniformare facilmente il contratto.

## Vantaggi

La conversione resta centralizzata e display accetta altre implementazioni.

## Svantaggi e compromessi

Rinominare metodi può nascondere differenze semantiche. Il sensore deve vivere più dell'adattatore, che conserva un riferimento non proprietario.

## Applicazioni tecniche

Integrazione di API legacy e conversioni di unità; precisione ed errori richiedono comunque un contratto.

## Pattern correlati

[facade](../facade/README.it.md) · [bridge](../bridge/README.it.md)

## Confusione comune

Facade semplifica un sottosistema; Adapter rende compatibile una specifica interfaccia.

## Domanda da colloquio

Puoi sempre preservare il comportamento adattando un'API asincrona a una sincrona?

## Piccola sfida

Rendi configurabile la temperatura Fahrenheit e prova congelamento ed ebollizione.

## Riepilogo

- **Problema:** Il pannello usa Celsius, ma un sensore esistente espone Fahrenheit.
- **Soluzione:** Implementa Temperature intorno a un LegacyThermometer preso in prestito e converti al confine.
- **Compromesso:** Rinominare metodi può nascondere differenze semantiche. Il sensore deve vivere più dell'adattatore, che conserva un riferimento non proprietario.
- **Da ricordare:** Traduci al confine.

[Precedente](../../creational/singleton/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/bridge/README.it.md)
