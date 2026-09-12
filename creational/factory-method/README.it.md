# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/builder/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/prototype/README.it.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Un Design Pattern che riguarda la creazione e configurazione degli object.

## Difficulty

Principiante

## In One Sentence

Lascia a una subclass la scelta dell'object usato da un flusso comune.

## The Problem

Un job invia sempre il messaggio di completamento, ma l'ambiente determina il canale.

## Naive Solution

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Why It Becomes a Problem

Creare EmailSender dentro run lega il flusso all'email; copiare run per la console duplica la logica.

Questo è `tight coupling`: il flusso conosce un Sender concreto, quindi cambiare la consegna può richiedere modifiche allo stesso flusso.

## The Idea

Metti il flusso in AlertJob e richiama il punto di creazione virtual make_sender.

## Real-World Analogy

Le filiali seguono la stessa procedura di consegna, scegliendo mezzi diversi.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Participants

AlertJob definisce il flusso; EmailJob e ConsoleJob personalizzano la creazione. Sender espone l'operazione e [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) (Uno smart pointer con ownership esclusiva che rilascia l'object alla distruzione del proprietario) possiede il prodotto.

Ruoli canonici in questo esempio:

- [`Creator`](../../GLOSSARY.md#creator) — Il ruolo base che contiene il flusso e dichiara l'operazione di creazione. Qui: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — Una subclass di Creator che fornisce un particolare Product. Qui: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — Il contratto dell'object restituito dal codice di creazione. Qui: `Sender`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(std::string_view message) const = 0;
};
struct EmailSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Email: " << message << '\n'; }
};
struct ConsoleSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Console: " << message << '\n'; }
};
class AlertJob {
protected:
    virtual std::unique_ptr<Sender> make_sender() const = 0;
public:
    virtual ~AlertJob() = default;
    void run() const {
        const auto sender = make_sender();
        sender->send("build complete");
    }
};
class EmailJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<EmailSender>(); }
};
class ConsoleJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<ConsoleSender>(); }
};
int main() {
    EmailJob{}.run();
    ConsoleJob{}.run();
}
```

## Example Output

```text
Email: build complete
Console: build complete
```

## When to Use

Usalo quando un flusso già basato sull'[`inheritance`](../../GLOSSARY.md#inheritance) (Definire una derived class da una base class per riusarne o specializzarne contratto e implementation) richiede un punto di creazione estensibile.

### Use cases

Esportatori estensibili e job specifici per ambiente sono contesti adatti; qui i sender stampano soltanto.

## When NOT to Use

Evitalo se basta passare un Sender pronto a una function.

## Advantages

Il flusso rimane unico mentre varia il prodotto.

## Trade-offs

Ogni scelta può richiedere una subclass. Dal base constructor una chiamata virtual non raggiunge l'override derivato come ci si potrebbe aspettare.

## Related Patterns

[Abstract Factory](../abstract-factory/README.it.md) · [Template Method](../../behavioral/template-method/README.it.md)

## Common Confusion

Una function con switch è una simple factory, non questo punto di estensione GoF. Abstract Factory coordina una famiglia.

## Terms to Remember

- `Factory Method` — Lascia a una subclass la scelta dell'object usato da un flusso comune.
- `Creator` — Il ruolo base che contiene il flusso e dichiara l'operazione di creazione. Esempio: `AlertJob`.
- `Concrete Creator` — Una subclass di Creator che fornisce un particolare Product. Esempio: `EmailJob, ConsoleJob`.
- `Product` — Il contratto dell'object restituito dal codice di creazione. Esempio: `Sender`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Scegliere il tipo concreto e stabilire valori iniziali e lifetime di un object.
- [`tight coupling`](../../GLOSSARY.md#tight-coupling) — Le parti dipendono molto dai dettagli concreti reciproci e le modifiche tendono a propagarsi.
- [`inheritance`](../../GLOSSARY.md#inheritance) — Definire una derived class da una base class per riusarne o specializzarne contratto e implementation.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — Mirare a open for extension, closed for modification lungo un confine scelto e utile.

## Interview Question

Perché chiamare make_sender da run dopo la costruzione e non dal constructor di AlertJob?

## Mini Challenge

Aggiungi FileJob con un sender che scrive in un file temporaneo e verificane il contenuto.

## Quick Summary

- **Problema:** Un job invia sempre il messaggio di completamento, ma l'ambiente determina il canale.
- **Soluzione:** Metti il flusso in AlertJob e richiama il punto di creazione virtual make_sender.
- **Trade-off:** Ogni scelta può richiedere una subclass. Dal base constructor una chiamata virtual non raggiunge l'override derivato come ci si potrebbe aspettare.
- **Da ricordare:** Conserva il flusso, personalizza la creazione.

[Precedente](../../creational/builder/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/prototype/README.it.md)
