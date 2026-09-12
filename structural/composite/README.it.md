# Composito

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/bridge/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/decorator/README.it.md)

## Categoria

Strutturali

## Difficoltà

Principiante

## In una frase

Tratta una foglia e un albero di oggetti attraverso la stessa operazione.

## Il problema

Un browser deve calcolare i byte di file e cartelle annidate.

## Soluzione iniziale

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## Perché diventa difficile

Cicli specifici per ogni profondità non reggono nuovi livelli e ripetono i controlli sul tipo.

## Idea centrale

File e Folder implementano Entry; la cartella chiede ricorsivamente i byte ai figli.

## Analogia quotidiana

Una scatola contiene pacchi o altre scatole: il peso si calcola con la stessa regola.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Composito](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## Partecipanti

Entry definisce bytes, File restituisce la dimensione, Folder possiede i figli con unique_ptr e somma i risultati.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>
#include <vector>

struct Entry {
    virtual ~Entry() = default;
    virtual int bytes() const = 0;
};
class File final : public Entry {
    int size_;
public:
    explicit File(int size) : size_(size) {
        if (size < 0) throw std::invalid_argument("Negative size");
    }
    int bytes() const override { return size_; }
};
class Folder final : public Entry {
    std::vector<std::unique_ptr<Entry>> children_;
public:
    void add(std::unique_ptr<Entry> child) {
        if (!child) throw std::invalid_argument("Null child");
        children_.push_back(std::move(child));
    }
    int bytes() const override {
        int total = 0;
        for (const auto& child : children_) total += child->bytes();
        return total;
    }
};
int main() {
    auto images = std::make_unique<Folder>();
    images->add(std::make_unique<File>(20));
    Folder root;
    root.add(std::make_unique<File>(10));
    root.add(std::move(images));
    std::cout << "Total: " << root.bytes() << " bytes\n";
}
```

## Output previsto

```text
Total: 30 bytes
```

## Quando usarlo

Usalo per veri alberi parte-tutto con un'operazione utile sia alle foglie sia ai gruppi.

## Quando NON usarlo

Evitalo per liste piatte o grafi con condivisioni e cicli: l'ownership ad albero sarebbe scorretta.

## Vantaggi

Il client calcola un sottoalbero senza conoscerne profondità e forma.

## Svantaggi e compromessi

Alberi profondi possono esaurire lo stack, le somme possono traboccare e le operazioni dei gruppi non vanno imposte alle foglie.

## Applicazioni tecniche

Alberi di file, scene senza nodi condivisi e gerarchie di menu.

## Pattern correlati

[decorator](../decorator/README.it.md) · [iterator](../../behavioral/iterator/README.it.md)

## Confusione comune

Decorator avvolge un oggetto per aggiungere comportamento; Composite riunisce figli per rappresentare un insieme.

## Domanda da colloquio

Perché add appartiene a Folder e non a Entry? Che significato avrebbe File.add?

## Piccola sfida

Aggiungi una cartella vuota e un livello annidato, verifica i totali e valuta un tipo numerico più ampio.

## Riepilogo

- **Problema:** Un browser deve calcolare i byte di file e cartelle annidate.
- **Soluzione:** File e Folder implementano Entry; la cartella chiede ricorsivamente i byte ai figli.
- **Compromesso:** Alberi profondi possono esaurire lo stack, le somme possono traboccare e le operazioni dei gruppi non vanno imposte alle foglie.
- **Da ricordare:** Il gruppo risponde come un elemento.

[Precedente](../../structural/bridge/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/decorator/README.it.md)
