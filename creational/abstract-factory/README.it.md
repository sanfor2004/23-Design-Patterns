# Fabbrica astratta

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Categoria](../README.it.md) · [Successivo](../../creational/builder/README.it.md)

## Categoria

Creazionali

## Difficoltà

Intermedio

## In una frase

Crea oggetti compatibili attraverso un unico contratto di famiglia.

## Il problema

Una schermata richiede pulsanti e pannelli dello stesso tema.

## Soluzione iniziale

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Perché diventa difficile

Creare ogni widget direttamente permette di mescolare un pulsante scuro e un pannello chiaro. Ogni client deve ricordare le combinazioni valide.

## Idea centrale

Passa un Theme a render: la fabbrica produce entrambi gli oggetti e il client usa soltanto le interfacce.

## Analogia quotidiana

Un set di mobili coordinati evita di abbinare ogni pezzo a mano.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Fabbrica astratta](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## Partecipanti

Theme definisce la famiglia; DarkTheme e LightTheme la realizzano. Button e Panel sono i prodotti astratti, render li utilizza.

## C++20 moderno — esempio eseguibile completo

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

## Output previsto

```text
dark button + dark panel
light button + light panel
```

## Quando usarlo

Usalo quando più tipi di prodotto devono cambiare insieme senza esporre le classi concrete al client.

## Quando NON usarlo

Evitalo per un solo prodotto stabile o quando le combinazioni indipendenti sono desiderabili.

## Vantaggi

Puoi sostituire una famiglia completa senza modificare il flusso di rendering.

## Svantaggi e compromessi

Aggiungere un prodotto come Slider richiede modifiche a tutte le fabbriche. Il contratto non garantisce da solo la coerenza visiva delle implementazioni.

## Applicazioni tecniche

Kit di temi e famiglie di driver per database sono contesti adatti; qui stampiamo soltanto nomi.

## Pattern correlati

[factory-method](../factory-method/README.it.md) · [builder](../builder/README.it.md)

## Confusione comune

Factory Method varia un punto di creazione. Abstract Factory coordina più tipi correlati e può usare metodi fabbrica al proprio interno.

## Domanda da colloquio

Quali interfacce cambiano aggiungendo un tema? E aggiungendo un tipo di widget?

## Piccola sfida

Aggiungi una famiglia ad alto contrasto, poi un prodotto Slider. Confronta l'estensione delle modifiche.

## Riepilogo

- **Problema:** Una schermata richiede pulsanti e pannelli dello stesso tema.
- **Soluzione:** Passa un Theme a render: la fabbrica produce entrambi gli oggetti e il client usa soltanto le interfacce.
- **Compromesso:** Aggiungere un prodotto come Slider richiede modifiche a tutte le fabbriche. Il contratto non garantisce da solo la coerenza visiva delle implementazioni.
- **Da ricordare:** Una fabbrica, un insieme coordinato.

[Categoria](../README.it.md) · [Successivo](../../creational/builder/README.it.md)
