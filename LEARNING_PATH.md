# Learning path

[Pattern catalog](README.md)

Catalog order groups ideas by purpose. This path starts with small, visible changes and introduces harder ownership and dispatch choices later.


## A small study routine

Use one pattern per session. Aim to explain a design decision, not recite a definition.

1. Read **Explain It Simply**.
2. Read **The Problem** and **Naive Solution**. Describe the difficulty before looking at the pattern's solution.
3. Read the Python implementation and predict its output.
4. Run Python. Change one input or behavior and check your prediction.
5. Read and run the C++20 implementation.
6. Compare Python and C++ using the notes in the Python README. Track Interfaces, Composition, Ownership, Lifetime, and Runtime choices.
7. Answer **Interview Question** without looking up an answer. Use **Check Yourself** to find gaps.
8. Complete **Mini Challenge**. Keep the original example small; experiment in your own copy.
9. Explain the pattern aloud in one minute: problem, why simple code starts hurting, solution, trade-off, and when not to use it.

Move through five levels: **Understand** the need, **See It** in the small example, **Implement It** by running and changing code, **Understand the Engineering** through trade-offs, then **Prepare for Interviews** with accurate terminology. You can stop and revisit any level.

Write three notes: what changes, what stays stable, and what extra complexity you paid for. Revisit them the next day. Try the mixed [recognition practice](PRACTICE.md) without using the catalog as a hint.

Follow the numbered order below. Catalog navigation groups patterns by category; it is not a difficulty ranking. The later patterns introduce harder copying, Ownership, Lifetime, memory sharing, dispatch, type relationships, and global State decisions.


1. [Strategy](behavioral/strategy/README.md) — Replace one calculation: Strategy makes the change easy to see.
2. [Observer](behavioral/observer/README.md) — Connect a change to listeners, then learn subscription lifetime.
3. [Factory Method](creational/factory-method/README.md) — Keep a workflow while varying object creation.
4. [Adapter](structural/adapter/README.md) — Translate an existing interface at a clear boundary.
5. [Decorator](structural/decorator/README.md) — Compose behavior one wrapper at a time.
6. [Command](behavioral/command/README.md) — Represent an action and give undo an explicit home.
7. [Composite](structural/composite/README.md) — Extend from one object to a tree of objects.
8. [State](behavioral/state/README.md) — Move from chosen algorithms to lifecycle transitions.

## Then build breadth

Study Facade, Builder, Template Method, Bridge, Proxy, Chain of Responsibility and Mediator next. They connect familiar delegation to construction and coordination.

9. [Facade](structural/facade/README.md)
10. [Builder](creational/builder/README.md)
11. [Template Method](behavioral/template-method/README.md)
12. [Bridge](structural/bridge/README.md)
13. [Proxy](structural/proxy/README.md)
14. [Chain of Responsibility](behavioral/chain-of-responsibility/README.md)
15. [Mediator](behavioral/mediator/README.md)

## Finish with deeper trade-offs

Finish with Abstract Factory, Prototype, Memento, Iterator, Flyweight, Interpreter, Visitor and Singleton. Pay particular attention to copying, lifetimes, memory, type dispatch and global state.

16. [Abstract Factory](creational/abstract-factory/README.md)
17. [Prototype](creational/prototype/README.md)
18. [Memento](behavioral/memento/README.md)
19. [Iterator](behavioral/iterator/README.md)
20. [Flyweight](structural/flyweight/README.md)
21. [Interpreter](behavioral/interpreter/README.md)
22. [Visitor](behavioral/visitor/README.md)
23. [Singleton](creational/singleton/README.md)
