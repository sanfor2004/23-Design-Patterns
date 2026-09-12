# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/command/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/iterator/README.it.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Avanzato

## In One Sentence

Rappresenta un piccolo linguaggio con object che valutano le regole grammaticali.

## The Problem

Le regole combinano ruoli e congiunzioni e devono essere costruibili come dati.

## Naive Solution

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## Why It Becomes a Problem

Una condizione fissa è semplice, ma cambiare regole annidate richiede modifiche all'applicazione.

## The Idea

Role è un terminale; Both è un non terminale che valuta due figli con AND a cortocircuito.

## Real-World Analogy

Una frase combina parole secondo una grammatica; una regola combina ruoli con AND.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Interpreter](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## Participants

Expression definisce la valutazione, Context fornisce ruoli, Role verifica appartenenza, Both possiede i figli.

Ruoli canonici in questo esempio:

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — Il contratto per valutare i nodi della grammatica di Interpreter. Qui: `Expression`.
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — Un'espressione senza espressioni figlie. Qui: `Role`.
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — Un'espressione che combina espressioni figlie secondo una regola grammaticale. Qui: `Both`.
- `Context` — I dati usati durante la valutazione delle espressioni; qui l’insieme dei nomi dei ruoli. `Context`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>

using Context = std::unordered_set<std::string>;
struct Expression {
    virtual ~Expression() = default;
    virtual bool evaluate(const Context& context) const = 0;
};
class Role final : public Expression {
    std::string name_;
public:
    explicit Role(std::string name) : name_(std::move(name)) {}
    bool evaluate(const Context& context) const override { return context.contains(name_); }
};
class Both final : public Expression {
    std::unique_ptr<Expression> left_, right_;
public:
    Both(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {
        if (!left_ || !right_) throw std::invalid_argument("Missing expression");
    }
    bool evaluate(const Context& context) const override {
        return left_->evaluate(context) && right_->evaluate(context);
    }
};
int main() {
    const Both rule{std::make_unique<Role>("editor"), std::make_unique<Role>("verified")};
    std::cout << std::boolalpha << rule.evaluate(Context{"editor"}) << '\n';
    std::cout << rule.evaluate(Context{"editor", "verified"}) << '\n';
}
```

## Example Output

```text
false
true
```

## When to Use

Usalo per grammatiche piccole e stabili con un albero utile da costruire e ispezionare.

### Use cases

Piccoli linguaggi di filtro o idoneità; non è un sistema sicuro di autorizzazione né un parser generale.

## When NOT to Use

Evitalo per linguaggi grandi che richiedono parsing robusto, diagnostica e ottimizzazione.

## Advantages

Le regole si compongono ricorsivamente e si valutano su contesti diversi.

## Trade-offs

Ogni forma grammaticale aggiunge codice; alberi profondi rischiano lo stack. Non c'è parser: main costruisce direttamente l'albero.

## Related Patterns

[Composite](../../structural/composite/README.it.md) · [Visitor](../visitor/README.it.md)

## Common Confusion

Composite descrive l'albero, Interpreter aggiunge semantica e valutazione. Visitor può aggiungere altre operazioni.

## Terms to Remember

- `Interpreter` — Rappresenta un piccolo linguaggio con object che valutano le regole grammaticali.
- `Abstract Expression` — Il contratto per valutare i nodi della grammatica di Interpreter. Esempio: `Expression`.
- `Terminal Expression` — Un'espressione senza espressioni figlie. Esempio: `Role`.
- `Nonterminal Expression` — Un'espressione che combina espressioni figlie secondo una regola grammaticale. Esempio: `Both`.
- `Context` — I dati usati durante la valutazione delle espressioni; qui l’insieme dei nomi dei ruoli.

## Interview Vocabulary

- [`abstract syntax tree`](../../GLOSSARY.md#abstract-syntax-tree) — Un albero che rappresenta la struttura grammaticale anziché la forma testuale originale.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — Costruire ricorsivamente una struttura con parti che espongono il contratto dell'insieme.
- [`short-circuit evaluation`](../../GLOSSARY.md#short-circuit-evaluation) — Saltare gli operandi successivi quando un risultato precedente determina già la risposta.

## Interview Question

Dove gestiresti la precedenza nell'input editor AND verified OR admin?

## Mini Challenge

Aggiungi Either per OR e prova una regola annidata su tre contesti.

## Quick Summary

- **Problema:** Le regole combinano ruoli e congiunzioni e devono essere costruibili come dati.
- **Soluzione:** Role è un terminale; Both è un non terminale che valuta due figli con AND a cortocircuito.
- **Trade-off:** Ogni forma grammaticale aggiunge codice; alberi profondi rischiano lo stack. Non c'è parser: main costruisce direttamente l'albero.
- **Da ricordare:** I nodi grammaticali danno significato.

[Precedente](../../behavioral/command/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/iterator/README.it.md)
