# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Categoria](../README.it.md) · [Successivo](../../creational/builder/README.it.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Un Design Pattern che riguarda la creazione e configurazione degli object.

## Difficulty

Intermedio

## In One Sentence

Crea object compatibili attraverso un unico contratto di famiglia.

## The Problem

Una schermata richiede pulsanti e pannelli dello stesso tema.

## Naive Solution

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Why It Becomes a Problem

Creare ogni widget direttamente permette di mescolare un pulsante scuro e un pannello chiaro. Ogni client deve ricordare le combinazioni valide.

## The Idea

Passa un Theme a render: la fabbrica produce entrambi gli object e il client usa soltanto le [`interface`](../../GLOSSARY.md#interface) (Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa).

## Real-World Analogy

Un set di mobili coordinati evita di abbinare ogni pezzo a mano.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Abstract Factory](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## Participants

Theme definisce la famiglia; DarkTheme e LightTheme la realizzano. Button e Panel sono i prodotti astratti, render li utilizza.

Ruoli canonici in questo esempio:

- [`Product`](../../GLOSSARY.md#product) — Il contratto dell'object restituito dal codice di creazione. Qui: `Button, Panel`.
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — Una particolare implementation del contratto Product. Qui: `DarkButton, LightButton, DarkPanel, LightPanel`.
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — Un'implementation che crea una famiglia coerente di Product. Qui: `DarkTheme, LightTheme`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Button {
    virtual ~Button() = default;
    virtual std::string_view paint() const = 0;
};
struct Panel {
    virtual ~Panel() = default;
    virtual std::string_view paint() const = 0;
};
struct DarkButton final : Button {
    std::string_view paint() const override { return "dark button"; }
};
struct DarkPanel final : Panel {
    std::string_view paint() const override { return "dark panel"; }
};
struct LightButton final : Button {
    std::string_view paint() const override { return "light button"; }
};
struct LightPanel final : Panel {
    std::string_view paint() const override { return "light panel"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Panel> panel() const = 0;
};
struct DarkTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<DarkPanel>(); }
};
struct LightTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<LightPanel>(); }
};
void render(const Theme& theme) {
    const auto button = theme.button();
    const auto panel = theme.panel();
    std::cout << button->paint() << " + " << panel->paint() << '\n';
}
int main() {
    render(DarkTheme{});
    render(LightTheme{});
}
```

## Example Output

```text
dark button + dark panel
light button + light panel
```

## When to Use

Usalo quando più tipi di prodotto devono cambiare insieme senza esporre le concrete class al client.

### Use cases

Kit di temi e famiglie di driver per database sono contesti adatti; qui stampiamo soltanto nomi.

## When NOT to Use

Evitalo per un solo prodotto stabile o quando le combinazioni indipendenti sono desiderabili.

## Advantages

Puoi sostituire una famiglia completa senza modificare il flusso di rendering.

## Trade-offs

Aggiungere un prodotto come Slider richiede modifiche a tutte le fabbriche. Il contratto non garantisce da solo la coerenza visiva delle [`implementation`](../../GLOSSARY.md#implementation) (Il codice concreto che esegue un'operazione o soddisfa un'interface).

## Related Patterns

[Factory Method](../factory-method/README.it.md) · [Builder](../builder/README.it.md)

## Common Confusion

Factory Method varia un punto di creazione. Abstract Factory coordina più tipi correlati e può usare factory methods al proprio interno.

## Terms to Remember

- `Abstract Factory` — Crea object compatibili attraverso un unico contratto di famiglia.
- `Product` — Il contratto dell'object restituito dal codice di creazione. Esempio: `Button, Panel`.
- `Concrete Product` — Una particolare implementation del contratto Product. Esempio: `DarkButton, LightButton, DarkPanel, LightPanel`.
- `Concrete Factory` — Un'implementation che crea una famiglia coerente di Product. Esempio: `DarkTheme, LightTheme`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — Scegliere il tipo concreto e stabilire valori iniziali e lifetime di un object.
- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — Dipendere dal contratto promesso anziché da una particolare implementation concreta.
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — Racchiudere una decisione variabile dietro un confine stabile.

## Interview Question

Quali interface cambiano aggiungendo un tema? E aggiungendo un tipo di widget?

## Mini Challenge

Aggiungi una famiglia ad alto contrasto, poi un prodotto Slider. Confronta l'estensione delle modifiche.

## Quick Summary

- **Problema:** Una schermata richiede pulsanti e pannelli dello stesso tema.
- **Soluzione:** Passa un Theme a render: la fabbrica produce entrambi gli object e il client usa soltanto le interface.
- **Trade-off:** Aggiungere un prodotto come Slider richiede modifiche a tutte le fabbriche. Il contratto non garantisce da solo la coerenza visiva delle implementation.
- **Da ricordare:** Una fabbrica, un insieme coordinato.

[Categoria](../README.it.md) · [Successivo](../../creational/builder/README.it.md)
