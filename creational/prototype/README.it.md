# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/factory-method/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/singleton/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Un Design Pattern che riguarda la creazione e configurazione degli object.

## Difficulty

Intermedio

## In One Sentence

Crea un object indipendente copiando un modello già configurato.

## In parole semplici

Un gioco ha già una guardia con l’equipaggiamento necessario.Prototype copia questa configurazione per modificare la nuova guardia senza cambiare l’originale.

## The Problem

Un gioco genera nemici da un modello configurato senza conoscere il concrete type.

## Naive Solution

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Why It Becomes a Problem

Ricostruire un Guard predefinito ripete la preparazione e perde l'equipaggiamento personalizzato del modello.

## The Idea

Enemy espone clone; Guard copia i membri per valore e restituisce un [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) a un nuovo object.

## Real-World Analogy

Duplica un documento pronto e rinomina la copia senza modificare l'originale.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Participants

Enemy definisce la polymorphic cloning, Guard la realizza, il client possiede e rinomina la copia.

Ruoli canonici in questo esempio:

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — Un object la cui operazione clone crea un altro object dai valori configurati. Qui: `Guard`.
- [`deep copy`](../../GLOSSARY.md#deep-copy) — Copiare i dati interni posseduti perché il nuovo object non condivida quei dati modificabili con l'originale. Qui: `Guard::clone`.
- [`value semantics`](../../GLOSSARY.md#value-semantics) — Le copie si comportano come valori indipendenti secondo il contratto del tipo. Qui: `name_, equipment_`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

struct Enemy {
    virtual ~Enemy() = default;
    virtual std::unique_ptr<Enemy> clone() const = 0;
    virtual void rename(std::string name) = 0;
    virtual void describe() const = 0;
};
class Guard final : public Enemy {
    std::string name_ = "template";
    std::vector<std::string> equipment_{"shield", "spear"};
public:
    std::unique_ptr<Enemy> clone() const override { return std::make_unique<Guard>(*this); }
    void rename(std::string name) override { name_ = std::move(name); }
    void describe() const override {
        std::cout << name_ << ": " << equipment_.size() << " items\n";
    }
};
int main() {
    const Guard prototype;
    auto copy = prototype.clone();
    copy->rename("gate guard");
    prototype.describe();
    copy->describe();
}
```

## Example Output

```text
template: 2 items
gate guard: 2 items
```

## When to Use

Usalo quando object esistenti contengono configurazioni utili e il client non deve ricostruire i concrete type.

### Use cases

Modelli di entità di gioco e documenti preconfigurati; qui string e std::vector hanno value semantics.

## When NOT to Use

Evitalo quando una normale copia per valore esprime già bene il bisogno.

## Advantages

Riutilizzi la configurazione senza esporre tutti i passi di costruzione.

## Trade-offs

I pointer richiedono una scelta fra deep copy e condivisione. Socket attivi e risorse esclusive possono non essere duplicabili.

## Related Patterns

[Abstract Factory](../abstract-factory/README.it.md) · [Memento](../../behavioral/memento/README.it.md)

## Common Confusion

Memento ripristina uno state precedente dello stesso object. Prototype ne crea un altro; il solo copy constructor non fornisce polymorphic cloning.

## Terms to Remember

- `Prototype` — Crea un object indipendente copiando un modello già configurato.
- `Concrete Prototype` — Un object la cui operazione clone crea un altro object dai valori configurati. Esempio: `Guard`.
- `deep copy` — Copiare i dati interni posseduti perché il nuovo object non condivida quei dati modificabili con l'originale. Esempio: `Guard::clone`.
- `value semantics` — Le copie si comportano come valori indipendenti secondo il contratto del tipo. Esempio: `name_, equipment_`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Scegliere il tipo concreto e stabilire valori iniziali e lifetime di un object.
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — Usare un'interface con implementation diverse; C++ offre forme a runtime e a compile time.
- [`ownership`](../../GLOSSARY.md#ownership) — La responsabilità di mantenere una risorsa valida e infine rilasciarla.

## Interview Question

Con `std::vector<std::shared_ptr<Item>>`, la copia sarebbe ancora indipendente? Spiega gli alias.

## Mini Challenge

Rendi modificabile l'equipaggiamento e verifica che cambiare la copia non tocchi il Prototype.

## Verifica cosa hai capito

1. Assegnare l’originale a un’altra variabile crea una copia indipendente?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Un gioco genera nemici da un modello configurato senza conoscere il concrete type.
- **Soluzione:** Enemy espone clone; Guard copia i membri per valore e restituisce un std::unique_ptr a un nuovo object.
- **Trade-off:** I pointer richiedono una scelta fra deep copy e condivisione. Socket attivi e risorse esclusive possono non essere duplicabili.
- **Da ricordare:** Copia la configurazione, non l'identità.

[Precedente](../../creational/factory-method/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/singleton/README.it.md)
