# Prototipo

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../creational/factory-method/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/singleton/README.it.md)

## Categoria

Creazionali

## Difficoltà

Intermedio

## In una frase

Crea un oggetto indipendente copiando un modello già configurato.

## Il problema

Un gioco genera nemici da un modello configurato senza conoscere il tipo concreto.

## Soluzione iniziale

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Perché diventa difficile

Ricostruire un Guard predefinito ripete la preparazione e perde l'equipaggiamento personalizzato del modello.

## Idea centrale

Enemy espone clone; Guard copia i membri per valore e restituisce un unique_ptr a un nuovo oggetto.

## Analogia quotidiana

Duplica un documento pronto e rinomina la copia senza modificare l'originale.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Prototipo](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Partecipanti

Enemy definisce la clonazione polimorfica, Guard la realizza, il client possiede e rinomina la copia.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
template: 2 items
gate guard: 2 items
```

## Quando usarlo

Usalo quando oggetti esistenti contengono configurazioni utili e il client non deve ricostruire i tipi concreti.

## Quando NON usarlo

Evitalo quando una normale copia per valore esprime già bene il bisogno.

## Vantaggi

Riutilizzi la configurazione senza esporre tutti i passi di costruzione.

## Svantaggi e compromessi

I puntatori richiedono una scelta fra copia profonda e condivisione. Socket attivi e risorse esclusive possono non essere duplicabili.

## Applicazioni tecniche

Modelli di entità di gioco e documenti preconfigurati; qui string e vector hanno semantica di valore.

## Pattern correlati

[abstract-factory](../abstract-factory/README.it.md) · [memento](../../behavioral/memento/README.it.md)

## Confusione comune

Memento ripristina uno stato precedente dello stesso oggetto. Prototype ne crea un altro; il solo costruttore di copia non fornisce clonazione polimorfica.

## Domanda da colloquio

Con vector<shared_ptr<Item>>, la copia sarebbe ancora indipendente? Spiega gli alias.

## Piccola sfida

Rendi modificabile l'equipaggiamento e verifica che cambiare la copia non tocchi il prototipo.

## Riepilogo

- **Problema:** Un gioco genera nemici da un modello configurato senza conoscere il tipo concreto.
- **Soluzione:** Enemy espone clone; Guard copia i membri per valore e restituisce un unique_ptr a un nuovo oggetto.
- **Compromesso:** I puntatori richiedono una scelta fra copia profonda e condivisione. Socket attivi e risorse esclusive possono non essere duplicabili.
- **Da ricordare:** Copia la configurazione, non l'identità.

[Precedente](../../creational/factory-method/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../creational/singleton/README.it.md)
