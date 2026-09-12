# Ponte

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../structural/adapter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/composite/README.it.md)

## Categoria

Strutturali

## Difficoltà

Intermedio

## In una frase

Separa due dimensioni variabili e collegale tramite composizione.

## Il problema

Gli avvisi variano per urgenza e canale, con estensioni indipendenti.

## Soluzione iniziale

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## Perché diventa difficile

Una classe per ogni coppia moltiplica le combinazioni e duplica la consegna.

## Idea centrale

Notice delega a Channel; UrgentNotice cambia il messaggio senza scegliere il trasporto.

## Analogia quotidiana

Un telecomando e il collegamento radio possono evolvere separatamente attraverso un piccolo protocollo.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Ponte](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## Partecipanti

Notice è l'astrazione, UrgentNotice la raffina, Channel è il contratto d'implementazione, Email e Sms consegnano.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <iostream>
#include <string_view>

struct Channel {
    virtual ~Channel() = default;
    virtual void deliver(std::string_view text) const = 0;
};
struct Email final : Channel {
    void deliver(std::string_view text) const override { std::cout << "Email: " << text << '\n'; }
};
struct Sms final : Channel {
    void deliver(std::string_view text) const override { std::cout << "SMS: " << text << '\n'; }
};
class Notice {
protected:
    const Channel& channel_;
public:
    explicit Notice(const Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void send() const { channel_.deliver("status normal"); }
};
class UrgentNotice final : public Notice {
public:
    using Notice::Notice;
    void send() const override { channel_.deliver("URGENT: disk full"); }
};
int main() {
    const Email email;
    const Sms sms;
    Notice{email}.send();
    UrgentNotice{email}.send();
    UrgentNotice{sms}.send();
}
```

## Output previsto

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## Quando usarlo

Usalo se due assi di variazione produrrebbero un prodotto cartesiano di sottoclassi.

## Quando NON usarlo

Evitalo con una sola variazione semplice già gestibile da un parametro.

## Vantaggi

Un nuovo canale funziona con gli avvisi esistenti senza creare tutte le coppie.

## Svantaggi e compromessi

L'indirezione richiede un confine chiaro; i canali non posseduti devono vivere più degli avvisi.

## Applicazioni tecniche

Forme e backend grafici, oppure tipi di notifica e canali, sono contesti adatti.

## Pattern correlati

[adapter](../adapter/README.it.md) · [strategy](../../behavioral/strategy/README.it.md)

## Confusione comune

Adapter corregge un'incompatibilità esistente. Bridge separa intenzionalmente dimensioni indipendenti; Strategy riguarda comportamenti sostituibili.

## Domanda da colloquio

Aggiungendo Push e ScheduledNotice, quante classi servono con e senza Bridge?

## Piccola sfida

Aggiungi Push e riutilizza entrambi gli avvisi senza modificarli.

## Riepilogo

- **Problema:** Gli avvisi variano per urgenza e canale, con estensioni indipendenti.
- **Soluzione:** Notice delega a Channel; UrgentNotice cambia il messaggio senza scegliere il trasporto.
- **Compromesso:** L'indirezione richiede un confine chiaro; i canali non posseduti devono vivere più degli avvisi.
- **Da ricordare:** Due assi, un collegamento.

[Precedente](../../structural/adapter/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../structural/composite/README.it.md)
