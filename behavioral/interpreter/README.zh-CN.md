# 解释器

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/command/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/iterator/README.zh-CN.md)

## 类别

行为型

## 难度

进阶

## 一句话说明

用对象表示小型语言，并按语法规则求值。

## 问题

权限规则组合角色名和逻辑与，希望把规则建成数据结构。

## 最初的简单方案

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## 为什么难以维护

固定布尔表达式很简单，但更换嵌套规则结构需要修改应用代码。

## 核心思路

Role 是终结表达式，Both 是非终结表达式，对两个子表达式执行短路与。

## 生活类比

句子按语法组合词语，规则按 AND 组合角色名。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![解释器](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## 参与者

Expression 定义求值，Context 提供角色集合，Role 检查成员，Both 拥有两个子表达式。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
false
true
```

## 何时使用

语法小而稳定，且表达式树本身有构建和检查价值时使用。

## 何时不该使用

大型语言需要健壮解析、诊断和优化时，应考虑成熟解析工具。

## 优点

规则递归组合，可在不同上下文中重复求值。

## 缺点与权衡

每种语法形式都增加代码；深树可能耗尽栈。示例没有解析器，main 直接构造语法树。

## 技术应用场景

适合小型筛选或资格规则语言；不是安全授权系统或通用解析器。

## 相关模式

[composite](../../structural/composite/README.zh-CN.md) · [visitor](../visitor/README.zh-CN.md)

## 常见混淆

组合描述树结构，解释器赋予语法含义和求值；访问者可以给树增加操作。

## 面试问题

用户输入 editor AND verified OR admin 时，优先级应该在哪里处理？

## 小练习

增加表示 OR 的 Either，用三个不同上下文测试嵌套规则。

## 小结

- **问题:** 权限规则组合角色名和逻辑与，希望把规则建成数据结构。
- **方案:** Role 是终结表达式，Both 是非终结表达式，对两个子表达式执行短路与。
- **权衡:** 每种语法形式都增加代码；深树可能耗尽栈。示例没有解析器，main 直接构造语法树。
- **记忆提示:** 语法节点赋予表达式含义。

[上一个](../../behavioral/command/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/iterator/README.zh-CN.md)
