# Promemoria

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/mediator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/observer/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Intermedio

## In una frase

Salva e ripristina lo stato senza esporre i dettagli dello snapshot.

## Il problema

Un editor vuole un checkpoint prima di una modifica sperimentale.

## Soluzione iniziale

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Perché diventa difficile

Se il gestore copia campi pubblici, ogni nuovo campo interno richiede una sua modifica.

## Idea centrale

Editor crea Snapshot con testo privato e lo legge per ripristinarsi.

## Analogia quotidiana

Un checkpoint di gioco ripristina il progresso senza mostrare il formato dei dati.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Promemoria](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Partecipanti

Editor è l'originatore, Snapshot il memento privato, main il custode che lo conserva senza ispezionarlo.

## C++20 moderno — esempio eseguibile completo

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
}
```

## Output previsto

```text
Broken edit
Draft
```

## Quando usarlo

Usalo per checkpoint di cui l'originatore sa definire uno stato consistente.

## Quando NON usarlo

Evitalo per stati enormi, risorse non ripristinabili o quando operazioni inverse costano meno.

## Vantaggi

La rappresentazione resta privata e il custode non copia campi a mano.

## Svantaggi e compromessi

Snapshot completi costano memoria e tempo; ripristinare una stringa non annulla file o chiamate di rete.

## Applicazioni tecniche

Checkpoint di editor e simulazioni, purché lo stato salvato sia completo e consistente.

## Pattern correlati

[command](../command/README.it.md) · [prototype](../../creational/prototype/README.it.md)

## Confusione comune

Command registra azioni, Memento registra stato; Prototype crea un altro oggetto anziché ripristinare questo.

## Domanda da colloquio

Aggiungendo la posizione del cursore, chi deve cambiare per mantenere corretto il ripristino?

## Piccola sfida

Salva anche il cursore e verifica che torni insieme al testo.

## Riepilogo

- **Problema:** Un editor vuole un checkpoint prima di una modifica sperimentale.
- **Soluzione:** Editor crea Snapshot con testo privato e lo legge per ripristinarsi.
- **Compromesso:** Snapshot completi costano memoria e tempo; ripristinare una stringa non annulla file o chiamate di rete.
- **Da ricordare:** Ricorda lo stato senza esporlo.

[Precedente](../../behavioral/mediator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/observer/README.it.md)
