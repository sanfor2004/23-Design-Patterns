# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/command/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/iterator/README.zh-CN.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

进阶

## In One Sentence

用 object 表示小型语言，并按 grammar 规则 求值（evaluation）。

## The Problem

权限规则组合角色名和逻辑与，希望把规则建成数据结构。

## Naive Solution

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## Why It Becomes a Problem

固定布尔表达式很简单，但更换嵌套规则结构需要修改应用代码。

## The Idea

Role 是 Terminal Expression，Both 是 Nonterminal Expression，对两个子表达式执行 short-circuit AND。

## Real-World Analogy

句子按语法组合词语，规则按 AND 组合角色名。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Interpreter](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## Participants

Expression 定义 求值（evaluation），Context 提供角色集合，Role 检查成员，Both 拥有两个子表达式。

本例中的标准角色：

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — 对 Interpreter 语法节点求值的约定。 对应代码： `Expression`。
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — 不含子表达式的表达式。 对应代码： `Role`。
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — 按照语法规则组合子表达式的表达式。 对应代码： `Both`。
- `Context` — 表达式求值时使用的数据，本例中是权限角色名称的集合。 `Context`。

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

grammar 小而稳定，且 expression tree 本身有构建和检查价值时使用。

### Use cases

适合小型筛选或资格规则语言；不是安全授权系统或通用 parser。

## When NOT to Use

大型语言需要健壮解析、诊断和优化时，应考虑成熟解析工具。

## Advantages

规则 recursive 组合，可在不同 Context 中重复 求值（evaluation）。

## Trade-offs

每种 grammar 形式都增加代码；深树可能耗尽栈。示例没有 parser，main 直接构造 syntax tree。

## Related Patterns

[Composite](../../structural/composite/README.zh-CN.md) · [Visitor](../visitor/README.zh-CN.md)

## Common Confusion

Composite 描述树结构， Interpreter 赋予 grammar 含义和 求值（evaluation）； Visitor 可以给树增加操作。

## Terms to Remember

- `Interpreter` — 用 object 表示小型语言，并按 grammar 规则 求值（evaluation）。
- `Abstract Expression` — 对 Interpreter 语法节点求值的约定。 示例： `Expression`。
- `Terminal Expression` — 不含子表达式的表达式。 示例： `Role`。
- `Nonterminal Expression` — 按照语法规则组合子表达式的表达式。 示例： `Both`。
- `Context` — 表达式求值时使用的数据，本例中是权限角色名称的集合。

## Interview Vocabulary

- [`abstract syntax tree`](../../GLOSSARY.md#abstract-syntax-tree) — 表示语法结构、而不是原始文本表面格式的树。
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — 由提供与整体相同约定的部分递归构建结构。
- [`short-circuit evaluation`](../../GLOSSARY.md#short-circuit-evaluation) — 当前面的结果已决定答案时，跳过后续操作数的求值。

## Interview Question

用户输入 editor AND verified OR admin 时，优先级应该在哪里处理？

## Mini Challenge

增加表示 OR 的 Either，用三个不同 Context 测试嵌套规则。

## Quick Summary

- **问题:** 权限规则组合角色名和逻辑与，希望把规则建成数据结构。
- **方案:** Role 是 Terminal Expression，Both 是 Nonterminal Expression，对两个子表达式执行 short-circuit AND。
- **权衡:** 每种 grammar 形式都增加代码；深树可能耗尽栈。示例没有 parser，main 直接构造 syntax tree。
- **记忆提示:** grammar 节点赋予表达式含义。

[上一个](../../behavioral/command/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/iterator/README.zh-CN.md)
