# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Precedente](../../behavioral/iterator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/memento/README.it.md)

[Percorso di studio](../../LEARNING_PATH.it.md) · [Scheda rapida](../../CHEATSHEET.it.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Un Design Pattern che organizza behavior e collaborazione fra object.

## Difficulty

Intermedio

## In One Sentence

Sposta la coordinazione fra object pari in un object dedicato.

## In parole semplici

Il pulsante di accesso richiede due campi compilati.Mediator gestisce la regola, così ogni campo non deve conoscere l’altro o il pulsante.

## The Problem

Username e password determinano insieme se il pulsante di accesso è attivo.

## Naive Solution

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## Why It Becomes a Problem

Se ogni campo conosce l'altro e il pulsante, le regole si disperdono e le dependency si intrecciano.

## The Idea

I campi notificano changed a LoginForm, che verifica i valori e aggiorna il pulsante.

## Real-World Analogy

Il controllo aereo coordina le interazioni senza negoziazioni fra ogni coppia di piloti.

## Structure

[Diagramma](diagram.md) · [Esegui l’esempio](cpp/README.md)

![Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## Participants

Mediator definisce le notifiche, Field le invia, Button conserva lo state, LoginForm possiede e coordina i colleghi.

Ruoli canonici in questo esempio:

- [`Colleague`](../../GLOSSARY.md#colleague) — Un object le cui interazioni vengono coordinate da un Mediator. Qui: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — Un'implementation che contiene le regole di coordinazione dei Colleague. Qui: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — Una function o operazione fornita perché un'altra parte possa richiamarla quando serve. Qui: `Mediator::changed`.

## Python Example

Leggi prima il [piccolo esempio Python](python/README.md) e il [codice](python/main.py). Prevedi l’[output](python/expected.txt), poi esegui e modifica. Le note in inglese confrontano il progetto con C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <utility>

struct Mediator {
    virtual ~Mediator() = default;
    virtual void changed() = 0;
};
class Field {
    Mediator& mediator_;
    std::string value_;
public:
    explicit Field(Mediator& mediator) : mediator_(mediator) {}
    void set(std::string value) { value_ = std::move(value); mediator_.changed(); }
    bool empty() const { return value_.empty(); }
};
class Button {
    bool enabled_ = false;
public:
    void enable(bool enabled) { enabled_ = enabled; }
    bool enabled() const { return enabled_; }
};
class LoginForm final : public Mediator {
    Field username_;
    Field password_;
    Button submit_;
public:
    LoginForm() : username_(*this), password_(*this) {}
    LoginForm(const LoginForm&) = delete;
    LoginForm& operator=(const LoginForm&) = delete;
    void changed() override { submit_.enable(!username_.empty() && !password_.empty()); }
    void username(std::string value) { username_.set(std::move(value)); }
    void password(std::string value) { password_.set(std::move(value)); }
    bool ready() const { return submit_.enabled(); }
};
int main() {
    LoginForm form;
    form.username("learner");
    std::cout << "Ready: " << std::boolalpha << form.ready() << '\n';
    form.password("example");
    std::cout << "Ready: " << form.ready() << '\n';
    form.password("");
    std::cout << "Ready after clearing: " << form.ready() << '\n';
}
```

## Example Output

```text
Ready: false
Ready: true
Ready after clearing: false
```

## When to Use

Usalo quando le interazioni fra più pari diventano intricate.

### Use cases

Dialoghi e controllori di flusso; abilitare un pulsante non autentica né valida password.

## When NOT to Use

Evitalo per un semplice callback o in assenza di regole di coordinazione.

## Advantages

I campi non conoscono fratelli o pulsante e la regola vive in un punto.

## Trade-offs

Il Mediator può ingrandirsi troppo. LoginForm non è copiabile: i campi conservano reference al form e una copia avrebbe collegamenti sbagliati.

## Related Patterns

[Observer](../observer/README.it.md) · [Facade](../../structural/facade/README.it.md)

## Common Confusion

Observer diffonde cambiamenti; Mediator stabilisce come specifici colleghi collaborano e può usare Observer per le notifiche.

## Terms to Remember

- `Mediator` — Sposta la coordinazione fra object pari in un object dedicato.
- `Colleague` — Un object le cui interazioni vengono coordinate da un Mediator. Esempio: `Field, Button`.
- `Concrete Mediator` — Un'implementation che contiene le regole di coordinazione dei Colleague. Esempio: `LoginForm`.
- `callback` — Una function o operazione fornita perché un'altra parte possa richiamarla quando serve. Esempio: `Mediator::changed`.

## Interview Vocabulary

- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — Le parti conoscono solo i contratti necessari a collaborare, limitando la propagazione delle modifiche.
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — Tenere separate responsabilità di natura diversa perché possano cambiare indipendentemente.
- [`god object`](../../GLOSSARY.md#god-object) — Un object che accumula troppe responsabilità non correlate.

## Interview Question

Perché un copy constructor automatico sarebbe pericoloso per LoginForm?

## Mini Challenge

Aggiungi l'accettazione dei termini senza far conoscere il pulsante a Field.

## Verifica cosa hai capito

1. Chi decide se abilitare il pulsante quando un campo si svuota?
2. Quando sarebbe più facile mantenere la soluzione semplice della pagina? Fai un esempio concreto.
3. Cambia un input dell’esempio Python. Prevedi l’output e spiega quale parte gestisce il cambiamento.

## Quick Summary

- **Problema:** Username e password determinano insieme se il pulsante di accesso è attivo.
- **Soluzione:** I campi notificano changed a LoginForm, che verifica i valori e aggiorna il pulsante.
- **Trade-off:** Il Mediator può ingrandirsi troppo. LoginForm non è copiabile: i campi conservano reference al form e una copia avrebbe collegamenti sbagliati.
- **Da ricordare:** I colleghi passano dal coordinatore.

[Precedente](../../behavioral/iterator/README.it.md) · [Categoria](../README.it.md) · [Successivo](../../behavioral/memento/README.it.md)
