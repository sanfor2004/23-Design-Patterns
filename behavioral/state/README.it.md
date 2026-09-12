# Stato

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/observer/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/strategy/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Intermedio

## In una frase

Lascia che lo stato corrente determini risposta e transizioni.

## Il problema

Una porta reagisce allo stesso pulsante diversamente da aperta o chiusa; dispositivi più ricchi aggiungono blocchi e guasti.

## Soluzione iniziale

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Perché diventa difficile

Un booleano basta per due stati, ma condizioni ripetute su molti eventi rendono incoerenti le transizioni.

## Idea centrale

Door delega press al DoorState corrente, che sceglie il successivo.

## Analogia quotidiana

Un distributore interpreta l'input diversamente prima e dopo il pagamento.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Stato](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Partecipanti

Door è il contesto; DoorState definisce press e name. Open e Closed hanno collegamenti non proprietari; main li mantiene vivi più di Door.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <iostream>
#include <string_view>

class Door;
struct DoorState {
    virtual ~DoorState() = default;
    virtual void press(Door& door) const = 0;
    virtual std::string_view name() const = 0;
};
class Door {
    const DoorState* state_;
public:
    explicit Door(const DoorState& state) : state_(&state) {}
    void change(const DoorState& state) { state_ = &state; }
    void press() { state_->press(*this); }
    std::string_view name() const { return state_->name(); }
};
struct Open final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "open"; }
};
struct Closed final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "closed"; }
};
int main() {
    Open open;
    Closed closed;
    open.next = &closed;
    closed.next = &open;
    Door door{closed};
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
}
```

## Output previsto

```text
closed
open
closed
```

## Quando usarlo

Usalo quando comportamenti e transizioni dipendenti dallo stato si disperdono fra operazioni.

## Quando NON usarlo

Evitalo per un toggle banale o una piccola tabella enum leggibile.

## Vantaggi

Il comportamento è raccolto per stato e le transizioni sono ispezionabili localmente.

## Svantaggi e compromessi

Aggiunge classi e vincoli di vita. Gli stati esterni a Door non vengono distrutti durante la transizione: preserva questa sicurezza in progetti più grandi.

## Applicazioni tecniche

Sessioni di protocollo e flussi di dispositivi con transizioni esplicite.

## Pattern correlati

[strategy](../strategy/README.it.md) · [observer](../observer/README.it.md)

## Confusione comune

Strategy è solitamente scelta dal client per un algoritmo; State rappresenta il ciclo di vita e può decidere le transizioni.

## Domanda da colloquio

Chi sceglie lo stato successivo e perché è diverso da scegliere una Strategy di spedizione?

## Piccola sfida

Aggiungi Locked che ignora press e un evento unlock separato; verifica la sequenza.

## Riepilogo

- **Problema:** Una porta reagisce allo stesso pulsante diversamente da aperta o chiusa; dispositivi più ricchi aggiungono blocchi e guasti.
- **Soluzione:** Door delega press al DoorState corrente, che sceglie il successivo.
- **Compromesso:** Aggiunge classi e vincoli di vita. Gli stati esterni a Door non vengono distrutti durante la transizione: preserva questa sicurezza in progetti più grandi.
- **Da ricordare:** Stesso evento, stato diverso, risposta diversa.

[Precedente](../../behavioral/observer/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/strategy/README.it.md)
