# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/command/README.md) · [Category](../README.md) · [Next](../../behavioral/iterator/README.md)

[Learning Path](../../LEARNING_PATH.md) · [Cheat Sheet](../../CHEATSHEET.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Advanced

## In One Sentence

Represent small language rules as an expression tree.

## Explain It Simply

An access rule can require both editor and verified roles. Each node evaluates one grammar rule, and larger expressions combine smaller ones.

## The Problem

Permission rules combine named roles and conjunctions, and rules should be built as data structures.

## Naive Solution

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## Why It Becomes a Problem

One hardcoded boolean expression is simple but changing nested rule structures requires changing application code.

## The Idea

Role is a terminal expression. Both is a nonterminal that evaluates two child expressions with short-circuit AND.

## Real-World Analogy

A sentence combines words using grammar; a rule combines role names using AND.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Interpreter](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## Participants

Expression defines evaluation, Context supplies roles, Role tests membership, Both owns its child expressions.

Canonical roles in this example:

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — The contract for evaluating nodes in an Interpreter grammar. Here: `Expression`.
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — An expression with no child expressions. Here: `Role`.
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — An expression that combines child expressions according to a grammar rule. Here: `Both`.
- `Context` — The evaluation data used by expressions; here it is the set of role names. `Context`.

## Python Example

Read the [small Python example](python/README.md) and [source](python/main.py) first. Predict the [output](python/expected.txt), then run and modify it. The notes compare its design with C++20.

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

Use it for a small stable grammar whose expression tree is useful to construct and inspect.

### Use cases

Small filtering or eligibility languages fit; this is not a secure authorization system or a general parser.

## When NOT to Use

Avoid it for a large language needing robust parsing, diagnostics and optimization; established parser tools are more appropriate.

## Advantages

Rules compose recursively and can be evaluated against different contexts.

## Trade-offs

Each grammar form adds code. Deep trees risk stack exhaustion, and a parser is deliberately absent: main constructs the syntax tree directly.

## Related Patterns

[Composite](../../structural/composite/README.md) · [Visitor](../visitor/README.md)

## Common Confusion

Composite describes the tree structure; Interpreter adds grammar-specific meaning and evaluation. Visitor can add operations over that tree.

## Terms to Remember

- `Interpreter` — Represent a small language as objects that evaluate its grammar rules.
- `Abstract Expression` — The contract for evaluating nodes in an Interpreter grammar. Example: `Expression`.
- `Terminal Expression` — An expression with no child expressions. Example: `Role`.
- `Nonterminal Expression` — An expression that combines child expressions according to a grammar rule. Example: `Both`.
- `Context` — The evaluation data used by expressions; here it is the set of role names.

## Interview Vocabulary

- [`abstract syntax tree`](../../GLOSSARY.md#abstract-syntax-tree) — A tree representing grammatical structure rather than the original text's surface formatting.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — Building a structure from parts that expose the same contract as the whole.
- [`short-circuit evaluation`](../../GLOSSARY.md#short-circuit-evaluation) — Skipping later operands when an earlier result already determines the answer.

## Interview Question

Where would precedence be handled if users typed editor AND verified OR admin?

## Mini Challenge

Add Either for OR and test a nested rule with three distinct contexts.

## Check Yourself

1. Does this example parse text, or evaluate an already built tree?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

## Quick Summary

- **Problem:** Permission rules combine named roles and conjunctions, and rules should be built as data structures.
- **Solution:** Role is a terminal expression. Both is a nonterminal that evaluates two child expressions with short-circuit AND.
- **Trade-off:** Each grammar form adds code. Deep trees risk stack exhaustion, and a parser is deliberately absent: main constructs the syntax tree directly.
- **Remember:** Grammar nodes give expressions meaning.

[Previous](../../behavioral/command/README.md) · [Category](../README.md) · [Next](../../behavioral/iterator/README.md)
