# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/command/README.md) · [Category](../README.md) · [Next](../../behavioral/iterator/README.md)

## Category

Behavioral

## Difficulty

Advanced

## In One Sentence

Represent a small language as objects that evaluate its grammar rules.

## The Problem

Permission rules combine named roles and conjunctions, and rules should be built as data structures.

## A Naive Solution

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## Why This Becomes a Problem

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

## When to Use It

Use it for a small stable grammar whose expression tree is useful to construct and inspect.

## When NOT to Use It

Avoid it for a large language needing robust parsing, diagnostics and optimization; established parser tools are more appropriate.

## Advantages

Rules compose recursively and can be evaluated against different contexts.

## Disadvantages / Trade-offs

Each grammar form adds code. Deep trees risk stack exhaustion, and a parser is deliberately absent: main constructs the syntax tree directly.

## Technical Use Cases

Small filtering or eligibility languages fit; this is not a secure authorization system or a general parser.

## Related Patterns

[composite](../../structural/composite/README.md) · [visitor](../visitor/README.md)

## Common Confusion

Composite describes the tree structure; Interpreter adds grammar-specific meaning and evaluation. Visitor can add operations over that tree.

## Interview Question

Where would precedence be handled if users typed editor AND verified OR admin?

## Mini Challenge

Add Either for OR and test a nested rule with three distinct contexts.

## Quick Summary

- **Problem:** Permission rules combine named roles and conjunctions, and rules should be built as data structures.
- **Solution:** Role is a terminal expression. Both is a nonterminal that evaluates two child expressions with short-circuit AND.
- **Trade-off:** Each grammar form adds code. Deep trees risk stack exhaustion, and a parser is deliberately absent: main constructs the syntax tree directly.
- **Remember:** Grammar nodes give expressions meaning.

[Previous](../../behavioral/command/README.md) · [Category](../README.md) · [Next](../../behavioral/iterator/README.md)
