# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Represent small language rules as an expression tree.

## The problem

Permission rules combine named roles and conjunctions, and rules should be built as data structures. One hardcoded boolean expression is simple but changing nested rule structures requires changing application code.

## The idea

An access rule can require both editor and verified roles. Each node evaluates one grammar rule, and larger expressions combine smaller ones. Role is a terminal expression. Both is a nonterminal that evaluates two child expressions with short-circuit AND.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Interpreter example map](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

Expression defines evaluation, Context supplies roles, Role tests membership, Both owns its child expressions. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Expression defines evaluation, Context supplies roles, Role tests membership, Both owns its child expressions.

Canonical roles in this example:

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — The contract for evaluating nodes in an Interpreter grammar. Here: `Expression`.
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — An expression with no child expressions. Here: `Role`.
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — An expression that combines child expressions according to a grammar rule. Here: `Both`.
- `Context` — The evaluation data used by expressions; here it is the set of role names. `Context`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Role:
    def __init__(self, name):
        self.name = name

    def evaluate(self, context):
        return self.name in context


class Both:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, context):
        return self.left.evaluate(context) and self.right.evaluate(context)


if __name__ == "__main__":
    rule = Both(Role("editor"), Role("verified"))
    for context in [set(), {"editor"}, {"editor", "verified"}]:
        print(rule.evaluate(context))
```

### Python output

```text
False
False
True
```

## C++20 example

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

### C++20 output

```text
false
true
```

## Compare the languages

Both examples build an expression tree directly; neither parses text. Python uses a set as Context and matching `evaluate` methods. C++ declares an Expression Interface. Use a direct boolean expression when rules do not need to be represented as data.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for a small stable grammar whose expression tree is useful to construct and inspect.

### Use cases

Small filtering or eligibility languages fit; this is not a secure authorization system or a general parser.

**Cost:** Each grammar form adds code. Deep trees risk stack exhaustion, and a parser is deliberately absent: main constructs the syntax tree directly.

## Check yourself

1. Does this example parse text, or evaluate an already built tree?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add Either for OR and test a nested rule with three distinct contexts.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
