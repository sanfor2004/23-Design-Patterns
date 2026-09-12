# Strategia

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)

## Categoria

Comportamentali

## Difficoltà

Principiante

## In una frase

Fornisci un algoritmo sostituibile all'oggetto che ne ha bisogno.

## Il problema

Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.

## Soluzione iniziale

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## Perché diventa difficile

Una condizione è leggibile; ripeterla in più percorsi rende difficili aggiunte e test.

## Idea centrale

Checkout possiede un callable ShippingRule e gli chiede il costo; il client sceglie alla costruzione.

## Analogia quotidiana

Scegli il percorso a piedi o in auto mantenendo la stessa destinazione.

## Diagramma originale

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Strategia](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Partecipanti

Checkout è il contesto, ShippingRule il contratto, le lambda implementano tariffe standard ed express.

## C++20 moderno — esempio eseguibile completo

```cpp
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## Output previsto

```text
Standard: 45
Express: 55
Express large: 120
```

## Quando usarlo

Usala quando gli algoritmi variano indipendentemente e il client deve scegliere una politica.

## Quando NON usarlo

Evitala per un algoritmo stabile o una condizione leggibile senza vera pressione di estensione.

## Vantaggi

Ogni politica si prova isolatamente e il calcolo totale resta condiviso.

## Svantaggi e compromessi

std::function introduce cancellazione del tipo e possibili allocazioni; template o puntatori a funzione rispondono a vincoli diversi. Valida i risultati di politiche esterne.

## Applicazioni tecniche

Prezzi, funzioni di ranking e politiche di retry sono contesti adatti.

## Pattern correlati

[state](../state/README.it.md) · [template-method](../template-method/README.it.md)

## Confusione comune

State riguarda ciclo di vita e transizioni; Strategy sceglie algoritmi. Template Method personalizza passi ereditati anziché callable iniettati.

## Domanda da colloquio

Sostituendo std::function con un parametro template, cosa cambia per scelta a runtime e compilazione?

## Piccola sfida

Aggiungi spedizione gratuita da 80 e prova 79, 80 e 81.

## Riepilogo

- **Problema:** Il checkout richiede politiche di spedizione diverse senza inglobarle tutte.
- **Soluzione:** Checkout possiede un callable ShippingRule e gli chiede il costo; il client sceglie alla costruzione.
- **Compromesso:** std::function introduce cancellazione del tipo e possibili allocazioni; template o puntatori a funzione rispondono a vincoli diversi. Valida i risultati di politiche esterne.
- **Da ricordare:** Stesso compito, algoritmo a scelta.

[Precedente](../../behavioral/state/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/template-method/README.it.md)
