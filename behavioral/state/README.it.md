# State

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/observer/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/strategy/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Intermedio

## In One Sentence

Lascia che lo state corrente determini risposta e transizioni.

## In parole semplici

La porta reagisce allo stesso pulsante in modi diversi: si apre se è chiusa e si chiude se è aperta. `State` mette la risposta e la transizione nell’Object che rappresenta lo `state` corrente.

## The Problem

Una porta reagisce allo stesso pulsante diversamente da aperta o chiusa; dispositivi più ricchi aggiungono blocchi e guasti.

## Naive Solution

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Why It Becomes a Problem

Un booleano basta per due state, ma condizioni ripetute su molti event rendono incoerenti le transizioni.

## The Idea

Door delega press al DoorState corrente, che sceglie il successivo.

## Real-World Analogy

Un distributore interpreta l'input diversamente prima e dopo il pagamento.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Participants

Door è il Context; DoorState definisce press e name. Open e Closed hanno collegamenti non proprietari; main li mantiene vivi più di Door.

Ruoli canonici in questo esempio:

- [`Context`](../../GLOSSARY.md#context) — L'object che usa una Strategy o delega il behavior allo State corrente. Qui: `Door`.
- [`State interface`](../../GLOSSARY.md#state-interface) — Il contratto con cui un Context delega il behavior dipendente dallo state. Qui: `DoorState`.
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — Un'implementation che definisce behavior e transizioni di uno State. Qui: `Open, Closed`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

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

## Example Output

```text
closed
open
closed
```

## When to Use

Usalo quando behavior e transizioni dipendenti dallo state si disperdono fra operazioni.

### Use cases

Sessioni di protocollo e flussi di dispositivi con transizioni esplicite.

## When NOT to Use

Evitalo per un toggle banale o una piccola tabella enum leggibile.

## Advantages

Il behavior è raccolto per state e le transizioni sono ispezionabili localmente.

## Trade-offs

Aggiunge class e vincoli di [`lifetime`](../../GLOSSARY.md#lifetime). Gli state esterni a Door non vengono distrutti durante la transizione: preserva questa sicurezza in progetti più grandi.

## Related Patterns

[Strategy](../strategy/README.it.md) · [Observer](../observer/README.it.md)

## Common Confusion

Strategy è solitamente scelta dal client per un algorithm; State rappresenta il [`lifecycle`](../../GLOSSARY.md#lifecycle) e può decidere le transizioni.

## Terms to Remember

- `State` — Lascia che lo state corrente determini risposta e transizioni.
- `Context` — L'object che usa una Strategy o delega il behavior allo State corrente. Esempio: `Door`.
- `State interface` — Il contratto con cui un Context delega il behavior dipendente dallo state. Esempio: `DoorState`.
- `Concrete State` — Un'implementation che definisce behavior e transizioni di uno State. Esempio: `Open, Closed`.

## Interview Vocabulary

- [`state transition`](../../GLOSSARY.md#state-transition) — Il passaggio fra due condizioni modellate in seguito a un event.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — Ciò che il programma fa durante l'esecuzione, incluso il behavior scelto dagli input.
- [`delegation`](../../GLOSSARY.md#delegation) — Un object affida parte del proprio lavoro a un collaboratore.

## Interview Question

Chi sceglie lo state successivo e perché è diverso da scegliere una Strategy di spedizione?

## Mini Challenge

Aggiungi Locked che ignora press e un event unlock separato; verifica la sequenza.

## Verifica cosa hai capito

1. Chi sceglie lo State successivo quando si preme il pulsante?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Una porta reagisce allo stesso pulsante diversamente da aperta o chiusa; dispositivi più ricchi aggiungono blocchi e guasti.
- **Soluzione:** Door delega press al DoorState corrente, che sceglie il successivo.
- **Trade-off:** Aggiunge class e vincoli di lifetime. Gli state esterni a Door non vengono distrutti durante la transizione: preserva questa sicurezza in progetti più grandi.
- **Da ricordare:** Stesso event, state diverso, risposta diversa.

[Precedente](../../behavioral/observer/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/strategy/README.it.md)
