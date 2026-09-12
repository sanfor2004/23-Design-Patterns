# Metodo modello

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/strategy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/visitor/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Intermedio

## In una frase

Fissa la sequenza dell'algoritmo lasciando alle sottoclassi alcuni passi.

## Il problema

I report condividono apertura, lettura, formato e chiusura ma variano dati o presentazione.

## Soluzione iniziale

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## Perché diventa difficile

Funzioni complete separate duplicano l'ordine e divergono quando cambia un passo comune.

## Idea centrale

Report::generate non virtuale richiama read e format, hook virtuali protetti, nell'ordine stabilito.

## Analogia quotidiana

La ricetta fissa l'ordine ma consente ripieni diversi.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Metodo modello](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## Partecipanti

Report possiede lo scheletro, TextReport implementa le variazioni, il client chiama generate.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Report {
protected:
    virtual std::string read() const = 0;
    virtual void format(std::string_view data) const = 0;
public:
    virtual ~Report() = default;
    void generate() const {
        std::cout << "Begin report\n";
        const auto data = read();
        format(data);
        std::cout << "End report\n";
    }
};
class TextReport final : public Report {
    std::string read() const override { return "sales=42"; }
    void format(std::string_view data) const override { std::cout << data << '\n'; }
};
int main() { TextReport{}.generate(); }
```

## Output previsto

```text
Begin report
sales=42
End report
```

## Quando usarlo

Usalo per una sequenza stabile con pochi punti di estensione ben definiti.

## Quando NON usarlo

Evitalo se i passi vanno riordinati a runtime o la composizione chiarisce meglio le dipendenze.

## Vantaggi

Le regole d'ordine restano nella base; le sottoclassi scrivono solo differenze.

## Svantaggi e compromessi

L'ereditarietà lega al protocollo base. End non avviene se un hook lancia: per liberare risorse usa RAII, non l'ultimo passo come garanzia.

## Applicazioni tecniche

Pipeline di importazione e report con scheletro stabile.

## Pattern correlati

[strategy](../strategy/README.it.md) · [factory-method](../../creational/factory-method/README.it.md)

## Confusione comune

Strategy inietta comportamento sostituibile; Template Method usa hook ereditati. Factory Method può essere uno di questi hook.

## Domanda da colloquio

Perché generate non è virtuale mentre read e format lo sono? Quali invarianti esprime?

## Piccola sfida

Aggiungi CsvReport, verifica l'ordine e simula un'eccezione di formattazione discutendo la pulizia.

## Riepilogo

- **Problema:** I report condividono apertura, lettura, formato e chiusura ma variano dati o presentazione.
- **Soluzione:** Report::generate non virtuale richiama read e format, hook virtuali protetti, nell'ordine stabilito.
- **Compromesso:** L'ereditarietà lega al protocollo base. End non avviene se un hook lancia: per liberare risorse usa RAII, non l'ultimo passo come garanzia.
- **Da ricordare:** Conserva la ricetta, varia i passi.

[Precedente](../../behavioral/strategy/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/visitor/README.it.md)
