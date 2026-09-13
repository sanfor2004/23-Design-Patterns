# Template Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/strategy/README.md) · [Category](../README.md) · [Next](../../behavioral/visitor/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Intermediate

## In One Sentence

Keep the sequence and let subclasses fill in steps.

## Explain It Simply

Reports all begin, read data, format it, and finish. Template Method keeps that order in one method while a subclass supplies the changing steps.

## The Problem

Reports share begin, read, format and end steps but vary their data access or formatting.

## Naive Solution

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## Why It Becomes a Problem

Separate complete report functions duplicate ordering and can drift when a shared step changes.

## The Idea

Report::generate is nonvirtual and calls protected virtual read and format hooks in a fixed order.

## Real-World Analogy

A recipe fixes preparation order while allowing a choice of filling.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Template Method](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## Participants

Report owns the algorithm skeleton; TextReport implements variation points. The client calls generate through the public workflow.

Canonical roles in this example:

- [`Abstract Class`](../../GLOSSARY.md#abstract-class-template-method-role) — The Template Method role that owns the algorithm skeleton and declares variable steps. Here: `Report`.
- [`Concrete Class`](../../GLOSSARY.md#concrete-class-template-method-role) — The Template Method role that supplies the variable steps. Here: `TextReport`.
- [`hook method`](../../GLOSSARY.md#hook-method) — An extension operation called by a fixed workflow; it may have a default implementation. Here: `read, format`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

## Modern C++20 Example

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

## Example Output

```text
Begin report
sales=42
End report
```

## When to Use

Use it for a stable sequence with a few well-defined subclass extension points.

### Use cases

Import pipelines and report generation fit when the skeleton is stable.

## When NOT to Use

Avoid it if steps must be rearranged at [`runtime`](../../GLOSSARY.md#runtime) or [`composition`](../../GLOSSARY.md#composition) would make dependencies clearer.

## Advantages

Shared ordering rules stay in the base and subclasses implement only their differences.

## Trade-offs

Inheritance couples subclasses to the base protocol. End is not guaranteed if read or format throws; use [`RAII`](../../GLOSSARY.md#raii) for real resource cleanup rather than treating the final step as a destructor.

## Related Patterns

[Strategy](../strategy/README.md) · [Factory Method](../../creational/factory-method/README.md)

## Common Confusion

Strategy injects replaceable behavior. Template Method relies on inherited hooks. Factory Method can be one creation hook inside such a skeleton.

## Terms to Remember

- `Template Method` — Fix an algorithm's sequence while subclasses implement selected steps.
- `Abstract Class` — The Template Method role that owns the algorithm skeleton and declares variable steps. Example: `Report`.
- `Concrete Class` — The Template Method role that supplies the variable steps. Example: `TextReport`.
- `hook method` — An extension operation called by a fixed workflow; it may have a default implementation. Example: `read, format`.

## Interview Vocabulary

- [`algorithm skeleton`](../../GLOSSARY.md#algorithm-skeleton) — The fixed sequence of an algorithm whose selected steps can vary.
- [`inheritance`](../../GLOSSARY.md#inheritance) — Defining a derived class from a base class to reuse or specialize its contract and implementation.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — Aim for open for extension, closed for modification at a useful, chosen boundary.

## Interview Question

Why is generate nonvirtual while read and format are virtual? What invariants does that express?

## Mini Challenge

Add CsvReport and verify the begin/end order; then simulate a formatting exception and discuss cleanup.

## Check Yourself

1. Which method owns the step order, and which methods can vary?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** Reports share begin, read, format and end steps but vary their data access or formatting.
- **Solution:** Report::generate is nonvirtual and calls protected virtual read and format hooks in a fixed order.
- **Trade-off:** Inheritance couples subclasses to the base protocol. End is not guaranteed if read or format throws; use RAII for real resource cleanup rather than treating the final step as a destructor.
- **Remember:** Keep the recipe, vary the steps.

[Previous](../../behavioral/strategy/README.md) · [Category](../README.md) · [Next](../../behavioral/visitor/README.md)
