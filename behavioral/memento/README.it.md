# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/mediator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/observer/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Intermedio

## In One Sentence

Salva e ripristina lo state senza esporre i dettagli dello snapshot.

## In parole semplici

Un editor richiede un punto di ripristino prima di una modifica rischiosa. `Memento` conserva una copia dello `state`; l’editor decide come salvarla e ripristinarla.

## The Problem

Un editor vuole un checkpoint prima di una modifica sperimentale.

## Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why It Becomes a Problem

Se il gestore copia campi public, ogni nuovo campo interno richiede una sua modifica.

## The Idea

`Editor` crea uno `Snapshot` con il testo in un campo `private`. Quando serve, legge quel campo e ripristina il testo.

## Real-World Analogy

Un checkpoint di gioco ripristina il progresso senza mostrare il formato dei dati.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Participants

Editor è l'Originator, Snapshot il Memento private, main il Caretaker che lo conserva senza ispezionarlo.

Ruoli canonici in questo esempio:

- [`Originator`](../../GLOSSARY.md#originator) — L'object che sa acquisire e ripristinare il proprio state. Qui: `Editor`.
- [`Caretaker`](../../GLOSSARY.md#caretaker) — Il ruolo che conserva un Memento senza ispezionarne la rappresentazione privata. Qui: `main`.
- [`snapshot`](../../GLOSSARY.md#snapshot) — Una rappresentazione di uno state selezionato in un dato momento. Qui: `Editor::Snapshot`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <utility>

class Editor {
    std::string text_;
public:
    class Snapshot {
        friend class Editor;
        std::string text_;
        explicit Snapshot(std::string text) : text_(std::move(text)) {}
    };
    void write(std::string text) { text_ = std::move(text); }
    Snapshot save() const { return Snapshot{text_}; }
    void restore(const Snapshot& snapshot) { text_ = snapshot.text_; }
    const std::string& text() const { return text_; }
};
int main() {
    Editor editor;
    editor.write("Draft");
    const auto checkpoint = editor.save();
    editor.write("Broken edit");
    std::cout << editor.text() << '\n';
    editor.restore(checkpoint);
    std::cout << editor.text() << '\n';
    editor.write("Another edit");
    editor.restore(checkpoint);
    std::cout << "Restore again: " << editor.text() << '\n';
}
```

## Example Output

```text
Broken edit
Draft
Restore again: Draft
```

## When to Use

Usalo per checkpoint di cui l'Originator sa definire uno state consistente.

### Use cases

Checkpoint di editor e simulazioni, purché lo state salvato sia completo e consistente.

## When NOT to Use

Evitalo per state enormi, risorse non ripristinabili o quando operazioni inverse costano meno.

## Advantages

La rappresentazione resta privata e il Caretaker non copia campi a mano.

## Trade-offs

Snapshot completi costano memoria e tempo; ripristinare una stringa non annulla file o chiamate di rete.

## Related Patterns

[Command](../command/README.it.md) · [Prototype](../../creational/prototype/README.it.md)

## Common Confusion

Command registra azioni, Memento registra state; Prototype crea un altro object anziché ripristinare questo.

## Terms to Remember

- `Memento` — Salva e ripristina lo state senza esporre i dettagli dello snapshot.
- `Originator` — L'object che sa acquisire e ripristinare il proprio state. Esempio: `Editor`.
- `Caretaker` — Il ruolo che conserva un Memento senza ispezionarne la rappresentazione privata. Esempio: `main`.
- `snapshot` — Una rappresentazione di uno state selezionato in un dato momento. Esempio: `Editor::Snapshot`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — Proteggere rappresentazione interna e invarianti mediante operazioni controllate.
- [`undo`](../../GLOSSARY.md#undo) — Ripristinare un risultato precedente con state salvato o un'operazione inversa, quando possibile.
- [`ownership`](../../GLOSSARY.md#ownership) — La responsabilità di mantenere una risorsa valida e infine rilasciarla.

## Interview Question

Aggiungendo la posizione del cursore, chi deve cambiare per mantenere corretto il ripristino?

## Mini Challenge

Salva anche il cursore e verifica che torni insieme al testo.

## Verifica cosa hai capito

1. Perché le modifiche successive non devono cambiare uno Snapshot salvato?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Un editor vuole un checkpoint prima di una modifica sperimentale.
- **Soluzione:** `Editor` crea uno `Snapshot` con il testo in un campo `private`. Quando serve, legge quel campo e ripristina il testo.
- **Trade-off:** Snapshot completi costano memoria e tempo; ripristinare una stringa non annulla file o chiamate di rete.
- **Da ricordare:** Ricorda lo state senza esporlo.

[Precedente](../../behavioral/mediator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/observer/README.it.md)
