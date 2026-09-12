# 中介者

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/iterator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/memento/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

把同级对象之间的协调规则集中到专门对象。

## 问题

用户名和密码字段共同决定登录按钮是否可用。

## 最初的简单方案

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## 为什么难以维护

每个字段都了解另一个字段和按钮，会让规则分散并产生相互依赖。

## 核心思路

字段向 LoginForm 报告 changed，由表单检查两个值并更新按钮。

## 生活类比

空中交通协调员集中协调，不必让每位飞行员与所有其他人协商。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![中介者](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## 参与者

Mediator 定义通知，Field 报告变化，Button 保存可用状态，LoginForm 拥有并协调这些对象。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
Ready: false
Ready: true
```

## 何时使用

多个同级对象的交互规则开始纠缠时使用。

## 何时不该使用

一个简单回调就够，或组件间没有实质协调时避免。

## 优点

字段无需了解兄弟组件或按钮，协调规则集中维护。

## 缺点与权衡

中介者可能过大。LoginForm 禁止复制，因为字段持有回指表单的引用，默认复制会保留错误链接。

## 技术应用场景

适合对话框协调和流程控制；启用按钮不是身份认证或密码校验。

## 相关模式

[observer](../observer/README.zh-CN.md) · [facade](../../structural/facade/README.zh-CN.md)

## 常见混淆

观察者向订阅者广播变化；中介者定义特定同级对象如何协作，也可用观察者传递通知。

## 面试问题

为什么 LoginForm 自动生成的复制构造函数危险？

## 小练习

增加同意条款复选框，要求三个条件都满足，且不让 Field 了解按钮。

## 小结

- **问题:** 用户名和密码字段共同决定登录按钮是否可用。
- **方案:** 字段向 LoginForm 报告 changed，由表单检查两个值并更新按钮。
- **权衡:** 中介者可能过大。LoginForm 禁止复制，因为字段持有回指表单的引用，默认复制会保留错误链接。
- **记忆提示:** 同级对象通过协调者协作。

[上一个](../../behavioral/iterator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/memento/README.zh-CN.md)
