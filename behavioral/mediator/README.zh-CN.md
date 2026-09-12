# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/iterator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/memento/README.zh-CN.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

把同级 object 之间的协调规则集中到专门 object。

## The Problem

用户名和密码字段共同决定登录按钮是否可用。

## Naive Solution

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## Why It Becomes a Problem

每个字段都了解另一个字段和按钮，会让规则分散并产生相互 dependency。

## The Idea

字段向 LoginForm 报告 changed，由表单检查两个值并更新按钮。

## Real-World Analogy

空中交通协调员集中协调，不必让每位飞行员与所有其他人协商。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## Participants

Mediator 定义通知，Field 报告变化，Button 保存可用 state，LoginForm 拥有并协调这些 object。

本例中的标准角色：

- [`Colleague`](../../GLOSSARY.md#colleague) — 其交互由 Mediator 协调的 object。 对应代码： `Field, Button`。
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — 保存 Colleague 之间协调规则的 implementation。 对应代码： `LoginForm`。
- [`callback`](../../GLOSSARY.md#callback) — 传给另一部分、在需要时由它调用的 function 或操作。 对应代码： `Mediator::changed`。

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
}
```

## Example Output

```text
Ready: false
Ready: true
```

## When to Use

多个同级 object 的交互规则开始纠缠时使用。

### Use cases

适合对话框协调和流程控制；启用按钮不是身份认证或密码校验。

## When NOT to Use

一个简单 callback 就够，或组件间没有实质协调时避免。

## Advantages

字段无需了解兄弟组件或按钮，协调规则集中维护。

## Trade-offs

Mediator 可能过大。LoginForm 禁止复制，因为字段持有回指表单的 reference，默认复制会保留错误链接。

## Related Patterns

[Observer](../observer/README.zh-CN.md) · [Facade](../../structural/facade/README.zh-CN.md)

## Common Confusion

Observer 向订阅者广播变化； Mediator 定义特定同级 object 如何协作，也可用 Observer 传递通知。

## Terms to Remember

- `Mediator` — 把同级 object 之间的协调规则集中到专门 object。
- `Colleague` — 其交互由 Mediator 协调的 object。 示例： `Field, Button`。
- `Concrete Mediator` — 保存 Colleague 之间协调规则的 implementation。 示例： `LoginForm`。
- `callback` — 传给另一部分、在需要时由它调用的 function 或操作。 示例： `Mediator::changed`。

## Interview Vocabulary

- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — 各部分只了解协作所需的小范围约定，限制修改传播。
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — 把不同关注点分开，使它们能够独立变化。
- [`god object`](../../GLOSSARY.md#god-object) — 积累过多无关职责的 object。

## Interview Question

为什么 LoginForm 自动生成的 copy constructor 危险？

## Mini Challenge

增加同意条款复选框，要求三个条件都满足，且不让 Field 了解按钮。

## Quick Summary

- **问题:** 用户名和密码字段共同决定登录按钮是否可用。
- **方案:** 字段向 LoginForm 报告 changed，由表单检查两个值并更新按钮。
- **权衡:** Mediator 可能过大。LoginForm 禁止复制，因为字段持有回指表单的 reference，默认复制会保留错误链接。
- **记忆提示:** 同级 object 通过协调者协作。

[上一个](../../behavioral/iterator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/memento/README.zh-CN.md)
