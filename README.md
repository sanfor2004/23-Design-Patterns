![Sanfor2004](assets/brand/logo.svg)

# Design-Patterns-23

23 Patterns · 4 Languages · Real Examples · Simple Explanations

[Sanfor2004](https://github.com/Sanfor2004) · C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

Start with a real problem. See where the simple solution bends. Learn the pattern, run the C++, and decide whether the extra structure earns its place.

- [Learning path](LEARNING_PATH.md)
- [Cheat sheet](CHEATSHEET.md)
- [Relationship map](PATTERN_MAP.md)
- [Comparisons](COMPARISONS.md)
- [C++20](CPP_EXAMPLES.md)

## Why this repository exists

Patterns are easier to understand when you can trace a concrete problem through a small program. This repository puts the motivation, code, output, and trade-offs together so you can judge when an abstraction earns its cost.

## How to navigate

Choose a category below or follow the learning path. Every pattern directory contains four translations, a diagram, and a `cpp/` directory. Language links keep you on the same pattern.

## Creational Pattern

How objects get created

- [Abstract Factory](creational/abstract-factory/README.md) — Create related objects through one family interface. (Intermediate)
- [Builder](creational/builder/README.md) — Assemble a configured object through named steps before producing the result. (Beginner)
- [Factory Method](creational/factory-method/README.md) — Let a subclass choose the object used by a shared workflow. (Beginner)
- [Prototype](creational/prototype/README.md) — Create an independent object by cloning an existing configured object. (Intermediate)
- [Singleton](creational/singleton/README.md) — Restrict a type to one accessible instance, accepting the cost of shared global state. (Intermediate)

## Structural Pattern

How objects fit together

- [Adapter](structural/adapter/README.md) — Translate an existing interface into the one a client expects. (Beginner)
- [Bridge](structural/bridge/README.md) — Separate two changing dimensions and connect them through composition. (Intermediate)
- [Composite](structural/composite/README.md) — Treat a leaf and a tree of objects through the same operation. (Beginner)
- [Decorator](structural/decorator/README.md) — Add behavior by wrapping an object in another object with the same interface. (Beginner)
- [Facade](structural/facade/README.md) — Offer a small entry point to a subsystem's common workflow. (Beginner)
- [Flyweight](structural/flyweight/README.md) — Share immutable intrinsic data while keeping each occurrence's context separate. (Advanced)
- [Proxy](structural/proxy/README.md) — Control access to an object through a stand-in with the same interface. (Intermediate)

## Behavioral Pattern

How objects communicate and behave

- [Chain of Responsibility](behavioral/chain-of-responsibility/README.md) — Pass a request along handlers that can stop or continue processing. (Intermediate)
- [Command](behavioral/command/README.md) — Turn an action into an object that can be stored and invoked later. (Intermediate)
- [Interpreter](behavioral/interpreter/README.md) — Represent a small language as objects that evaluate its grammar rules. (Advanced)
- [Iterator](behavioral/iterator/README.md) — Traverse a collection through a stable access protocol. (Beginner)
- [Mediator](behavioral/mediator/README.md) — Move coordination between peer objects into a dedicated object. (Intermediate)
- [Memento](behavioral/memento/README.md) — Save and restore an object's state without exposing snapshot internals. (Intermediate)
- [Observer](behavioral/observer/README.md) — Notify subscribed objects when something they follow changes. (Beginner)
- [State](behavioral/state/README.md) — Let an object's current state determine its response and transitions. (Intermediate)
- [Strategy](behavioral/strategy/README.md) — Supply an interchangeable algorithm to the object that needs it. (Beginner)
- [Template Method](behavioral/template-method/README.md) — Fix an algorithm's sequence while subclasses implement selected steps. (Intermediate)
- [Visitor](behavioral/visitor/README.md) — Add operations across a stable set of element types using a separate visitor. (Advanced)

## Understand the problem. Then earn the abstraction.

A pattern is a reusable design idea for a recurring problem—not a class diagram to copy everywhere. Start with simple code; introduce structure when a real change makes it useful.

1. **Meet the problem** — A concrete example gives the design a reason to exist.
2. **Challenge the simple solution** — Find the exact coupling or repetition that creates friction.
3. **Trace the design** — Follow responsibilities, ownership, and trade-offs.
4. **Run and change the C++** — Compare the output, try the challenge, and test the boundary.

## Repository resources

- [References](REFERENCES.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

Translate the explanation, not the terminology. Pattern names, software terms, code identifiers, and interview expressions stay in English; each language explains their meaning.

[Glossary](GLOSSARY.md)
