![Sanfor2004](assets/brand/logo.svg)

# 23 Design Patterns

Learn all 23 Gang of Four (GoF) design patterns with runnable Python and C++20 examples, diagrams, and explanations in English, Egyptian Arabic, Simplified Chinese, and Italian.

[Sanfor2004](https://github.com/Sanfor2004) · Python + C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

Start with a real problem. See where the simple solution bends. Learn the pattern, run Python and C++20, and decide whether the extra structure earns its place.

- [Learning path](LEARNING_PATH.md)
- [Cheat sheet](CHEATSHEET.md)
- [Relationship map](PATTERN_MAP.md)
- [Comparisons](COMPARISONS.md)
- [C++20](CPP_EXAMPLES.md)

## Two ways to study each pattern

**Python** reduces syntax overhead so the pattern's intent is easy to follow. Start with the small [Python examples](PYTHON_EXAMPLES.md), then run and change them.

**C++20** helps you study implementation details: Ownership, Lifetime, static typing, Runtime dispatch, RAII, and other engineering trade-offs. Keep both versions side by side; the same intent can use different language features.

Follow the [recommended study order](LEARNING_PATH.md), starting with Strategy, Observer, Factory Method, Adapter, and Decorator. Continue through all 23; leave the harder global State questions in Singleton until last. Each pattern directory has both `python/` and `cpp/` with a README, runnable source, and expected output.


## Why this repository exists

Patterns are easier to understand when you can trace a concrete problem through a small program. This repository puts the motivation, code, output, and trade-offs together so you can judge when an abstraction earns its cost.

## Learn Design Patterns with Python and C++20

- **New to object-oriented design?** Follow the [design patterns learning path](LEARNING_PATH.md).
- **Comparing similar patterns?** Read [Strategy vs State, Adapter vs Facade, and other comparisons](COMPARISONS.md).
- **Preparing for an interview?** Use the [design patterns cheat sheet](CHEATSHEET.md), then explain the trade-offs in each example.
- **Want to run the code?** Follow the [C++20 build and test instructions](CPP_EXAMPLES.md). Each example includes expected output.

## Run the examples

For Python, run `python scripts/test_python.py` from the repository root. No packages are needed.

For C++20, with CMake 3.20+ and a C++20 compiler installed, run from the repository root:

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
```

On Windows, use a Visual Studio developer shell. See the [compiler and build notes](CPP_EXAMPLES.md) for details.

## How to navigate

Choose a category below or follow the learning path. Every pattern directory contains four translations, a diagram, and `python/` and `cpp/` directories. Language links keep you on the same pattern.

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
4. **Run and change Python and C++20** — Compare the output, try the challenge, and test the boundary.

## Repository resources

- [References](REFERENCES.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

Translate the explanation, not the terminology. Pattern names, software terms, code identifiers, and interview expressions stay in English; each language explains their meaning.

[Glossary](GLOSSARY.md)

## Share and track the launch

Use the [launch pack](Marketing/README.md) for finished posts and images, including the [GitHub social preview](Marketing/images/github-social-preview.png). The [keyword and SEO tracker](Marketing/keyword-tracking.md) maps relevant search phrases to useful guides and records campaign results without assuming virality. Reproduce or adapt the campaign with the [social media launch framework](social_media_launch_framework.md).
