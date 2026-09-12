# Metodo fabbrica

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/builder/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/prototype/README.it.md)

## Categoria

Creazionali

## Difficoltà

Principiante

## In una frase

Lascia a una sottoclasse la scelta dell'oggetto usato da un flusso comune.

## Il problema

Un job invia sempre il messaggio di completamento, ma l'ambiente determina il canale.

## Soluzione iniziale

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Perché diventa difficile

Creare EmailSender dentro run lega il flusso all'email; copiare run per la console duplica la logica.

## Idea centrale

Metti il flusso in AlertJob e richiama il punto di creazione virtuale make_sender.

## Analogia quotidiana

Le filiali seguono la stessa procedura di consegna, scegliendo mezzi diversi.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Metodo fabbrica](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Partecipanti

AlertJob definisce il flusso; EmailJob e ConsoleJob personalizzano la creazione. Sender espone l'operazione e unique_ptr possiede il prodotto.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Email: build complete
Console: build complete
```

## Quando usarlo

Usalo quando un flusso già basato sull'ereditarietà richiede un punto di creazione estensibile.

## Quando NON usarlo

Evitalo se basta passare un Sender pronto a una funzione.

## Vantaggi

Il flusso rimane unico mentre varia il prodotto.

## Svantaggi e compromessi

Ogni scelta può richiedere una sottoclasse. Dal costruttore base una chiamata virtuale non raggiunge l'override derivato come ci si potrebbe aspettare.

## Applicazioni tecniche

Esportatori estensibili e job specifici per ambiente sono contesti adatti; qui i sender stampano soltanto.

## Pattern correlati

[abstract-factory](../abstract-factory/README.it.md) · [template-method](../../behavioral/template-method/README.it.md)

## Confusione comune

Una funzione con switch è una fabbrica semplice, non questo punto di estensione GoF. Abstract Factory coordina una famiglia.

## Domanda da colloquio

Perché chiamare make_sender da run dopo la costruzione e non dal costruttore di AlertJob?

## Piccola sfida

Aggiungi FileJob con un sender che scrive in un file temporaneo e verificane il contenuto.

## Riepilogo

- **Problema:** Un job invia sempre il messaggio di completamento, ma l'ambiente determina il canale.
- **Soluzione:** Metti il flusso in AlertJob e richiama il punto di creazione virtuale make_sender.
- **Compromesso:** Ogni scelta può richiedere una sottoclasse. Dal costruttore base una chiamata virtuale non raggiunge l'override derivato come ci si potrebbe aspettare.
- **Da ricordare:** Conserva il flusso, personalizza la creazione.

[Precedente](../../creational/builder/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/prototype/README.it.md)
