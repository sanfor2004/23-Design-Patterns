# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/flyweight/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/chain-of-responsibility/README.it.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Un Design Pattern che organizza le relazioni fra object e class.

## Difficulty

Intermedio

## In One Sentence

Controlla l'accesso a un object tramite un sostituto con la stessa [`interface`](../../GLOSSARY.md#interface) (Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa).

## The Problem

Una galleria prepara molte immagini ma ne mostra poche.

## Naive Solution

```cpp
DiskImage image; // loads even if never displayed
```

## Why It Becomes a Problem

Costruire subito tutte le immagini pesanti carica dati prima che servano.

## The Idea

LazyImage implementa Image, crea DiskImage al primo display e poi la riutilizza.

## Real-World Analogy

Una richiesta di biblioteca rappresenta il libro finché il bibliotecario lo recupera.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Proxy](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## Participants

Image è il contratto, DiskImage svolge il lavoro, LazyImage possiede il Real Subject creato su richiesta.

Ruoli canonici in questo esempio:

- [`Subject interface`](../../GLOSSARY.md#subject-interface) — Il contratto condiviso da Proxy e Real Subject. Qui: `Image`.
- [`Real Subject`](../../GLOSSARY.md#real-subject) — L'object che svolge il lavoro dietro un Proxy. Qui: `DiskImage`.
- [`lazy initialization`](../../GLOSSARY.md#lazy-initialization) — Rinviare la creazione fino al primo utilizzo del valore o della risorsa. Qui: `LazyImage::display`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() const = 0;
};
struct DiskImage final : Image {
    DiskImage() { std::cout << "Load image\n"; }
    void display() const override { std::cout << "Display image\n"; }
};
class LazyImage final : public Image {
    mutable std::unique_ptr<DiskImage> image_;
public:
    void display() const override {
        if (!image_) image_ = std::make_unique<DiskImage>();
        image_->display();
    }
};
int main() {
    const LazyImage image;
    std::cout << "Proxy ready\n";
    image.display();
    image.display();
}
```

## Example Output

```text
Proxy ready
Load image
Display image
Display image
```

## When to Use

Usalo per lazy initialization, autorizzazione o accesso remoto con un'interface stabile.

### Use cases

Media caricati su richiesta, controlli di autorizzazione e stub remoti hanno questa forma ma semantiche d'errore diverse.

## When NOT to Use

Evitalo se costruire direttamente costa poco e la politica di accesso non serve.

## Advantages

Il client conserva display mentre la creazione viene rinviata.

## Trade-offs

La prima chiamata paga il caricamento. mutable esprime logical constness, non sicurezza fra thread; serve anche una politica per gli errori.

## Related Patterns

[Decorator](../decorator/README.it.md) · [Adapter](../adapter/README.it.md)

## Common Confusion

Decorator aggiunge responsibility, Proxy controlla quando o se raggiungere il Real Subject; le strutture possono coincidere.

## Terms to Remember

- `Proxy` — Controlla l'accesso a un object tramite un sostituto con la stessa interface.
- `Subject interface` — Il contratto condiviso da Proxy e Real Subject. Esempio: `Image`.
- `Real Subject` — L'object che svolge il lavoro dietro un Proxy. Esempio: `DiskImage`.
- `lazy initialization` — Rinviare la creazione fino al primo utilizzo del valore o della risorsa. Esempio: `LazyImage::display`.

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — Un object affida parte del proprio lavoro a un collaboratore.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — Ciò che il programma fa durante l'esecuzione, incluso il behavior scelto dagli input.
- [`trade-off`](../../GLOSSARY.md#trade-off) — Un vantaggio ottenuto rinunciando a un'altra proprietà desiderabile.

## Interview Question

Se il caricamento lancia un'eccezione, ritenti o memorizzi il fallimento? Definisci il contratto.

## Mini Challenge

Conta i caricamenti su tre display e prova un loader che fallisce una volta.

## Quick Summary

- **Problema:** Una galleria prepara molte immagini ma ne mostra poche.
- **Soluzione:** LazyImage implementa Image, crea DiskImage al primo display e poi la riutilizza.
- **Trade-off:** La prima chiamata paga il caricamento. mutable esprime logical constness, non sicurezza fra thread; serve anche una politica per gli errori.
- **Da ricordare:** Un sostituto controlla l'accesso.

[Precedente](../../structural/flyweight/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/chain-of-responsibility/README.it.md)
