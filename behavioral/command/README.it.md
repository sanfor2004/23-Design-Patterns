# Comando

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/chain-of-responsibility/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/interpreter/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Intermedio

## In una frase

Trasforma un'azione in un oggetto conservabile e invocabile in seguito.

## Il problema

Un editor deve applicare e annullare modifiche senza insegnare ogni operazione alla barra degli strumenti.

## Soluzione iniziale

```cpp
document.text += " world"; // no object records how to undo
```

## Perché diventa difficile

La modifica diretta non registra né l'azione né lo stato precedente.

## Idea centrale

Append cattura destinatario e argomento; execute salva il testo precedente, undo lo ripristina. History possiede i comandi.

## Analogia quotidiana

La comanda del ristorante conserva l'azione separatamente dal cameriere.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Comando](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## Partecipanti

Command definisce execute e undo, Append modifica un Document non posseduto, History conserva i comandi come stack.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Document { std::string text; };
struct Command {
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};
class Append final : public Command {
    Document& document_;
    std::string suffix_;
    std::string before_;
public:
    Append(Document& document, std::string suffix) : document_(document), suffix_(std::move(suffix)) {}
    void execute() override { before_ = document_.text; document_.text += suffix_; }
    void undo() override { document_.text = before_; }
};
class History {
    std::vector<std::unique_ptr<Command>> commands_;
public:
    void run(std::unique_ptr<Command> command) {
        if (!command) throw std::invalid_argument("Missing command");
        commands_.push_back(std::move(command));
        try { commands_.back()->execute(); }
        catch (...) { commands_.pop_back(); throw; }
    }
    void undo() {
        if (commands_.empty()) return;
        commands_.back()->undo();
        commands_.pop_back();
    }
};
int main() {
    Document document{"Hello"};
    History history;
    history.run(std::make_unique<Append>(document, " world"));
    std::cout << document.text << '\n';
    history.undo();
    std::cout << document.text << '\n';
}
```

## Output previsto

```text
Hello world
Hello
```

## Quando usarlo

Usalo per azioni differite, code, macro e annullamento.

## Quando NON usarlo

Evitalo per una chiamata isolata senza necessità di memorizzare o pianificare l'intento.

## Vantaggi

L'invocatore resta indipendente dalle operazioni concrete e ne conserva la storia.

## Svantaggi e compromessi

Salvare tutto il testo costa memoria. Il demo a thread singolo presume modifiche tramite History e un Document più longevo; modifiche esterne rompono l'annullamento atteso.

## Applicazioni tecniche

Azioni di editor e code di job; una coda durevole richiede anche serializzazione e idempotenza.

## Pattern correlati

[memento](../memento/README.it.md) · [chain-of-responsibility](../chain-of-responsibility/README.it.md)

## Confusione comune

Memento conserva stato, Command conserva un'azione e può usare uno snapshot. Non ogni comando è reversibile.

## Domanda da colloquio

Inviare un'email è annullabile come ripristinare una stringa? Distingui compensazione e inversione.

## Piccola sfida

Esegui due append, annulla due volte e verifica che annullare una storia vuota sia innocuo.

## Riepilogo

- **Problema:** Un editor deve applicare e annullare modifiche senza insegnare ogni operazione alla barra degli strumenti.
- **Soluzione:** Append cattura destinatario e argomento; execute salva il testo precedente, undo lo ripristina. History possiede i comandi.
- **Compromesso:** Salvare tutto il testo costa memoria. Il demo a thread singolo presume modifiche tramite History e un Document più longevo; modifiche esterne rompono l'annullamento atteso.
- **Da ricordare:** Un'azione da conservare.

[Precedente](../../behavioral/chain-of-responsibility/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/interpreter/README.it.md)
