# Procuratore

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/flyweight/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/chain-of-responsibility/README.it.md)

## Categoria

Strutturali

## Difficoltà

Intermedio

## In una frase

Controlla l'accesso a un oggetto tramite un sostituto con la stessa interfaccia.

## Il problema

Una galleria prepara molte immagini ma ne mostra poche.

## Soluzione iniziale

```cpp
DiskImage image; // loads even if never displayed
```

## Perché diventa difficile

Costruire subito tutte le immagini pesanti carica dati prima che servano.

## Idea centrale

LazyImage implementa Image, crea DiskImage al primo display e poi la riutilizza.

## Analogia quotidiana

Una richiesta di biblioteca rappresenta il libro finché il bibliotecario lo recupera.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Procuratore](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## Partecipanti

Image è il contratto, DiskImage svolge il lavoro, LazyImage possiede il soggetto creato su richiesta.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
Proxy ready
Load image
Display image
Display image
```

## Quando usarlo

Usalo per inizializzazione differita, autorizzazione o accesso remoto con un'interfaccia stabile.

## Quando NON usarlo

Evitalo se costruire direttamente costa poco e la politica di accesso non serve.

## Vantaggi

Il client conserva display mentre la creazione viene rinviata.

## Svantaggi e compromessi

La prima chiamata paga il caricamento. mutable esprime costanza logica, non sicurezza fra thread; serve anche una politica per gli errori.

## Applicazioni tecniche

Media caricati su richiesta, controlli di autorizzazione e stub remoti hanno questa forma ma semantiche d'errore diverse.

## Pattern correlati

[decorator](../decorator/README.it.md) · [adapter](../adapter/README.it.md)

## Confusione comune

Decorator aggiunge responsabilità, Proxy controlla quando o se raggiungere il soggetto; le strutture possono coincidere.

## Domanda da colloquio

Se il caricamento lancia un'eccezione, ritenti o memorizzi il fallimento? Definisci il contratto.

## Piccola sfida

Conta i caricamenti su tre display e prova un loader che fallisce una volta.

## Riepilogo

- **Problema:** Una galleria prepara molte immagini ma ne mostra poche.
- **Soluzione:** LazyImage implementa Image, crea DiskImage al primo display e poi la riutilizza.
- **Compromesso:** La prima chiamata paga il caricamento. mutable esprime costanza logica, non sicurezza fra thread; serve anche una politica per gli errori.
- **Da ricordare:** Un sostituto controlla l'accesso.

[Precedente](../../structural/flyweight/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/chain-of-responsibility/README.it.md)
