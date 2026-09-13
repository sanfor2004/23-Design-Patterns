# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/adapter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/composite/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — 关注 object 与 class 如何组织在一起的 Design Pattern。

## Difficulty

中级

## In One Sentence

把两个变化维度分开，再用 [`composition`](../../GLOSSARY.md#composition) 连接。

## 简单理解

通知可以是普通或紧急，发送渠道可以是邮件或短信。Bridge 把通知与渠道连接起来，避免为每种组合建立一个 Class。

## The Problem

通知同时按紧急程度和发送渠道变化，两边都需要独立扩展。

## Naive Solution

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## Why It Becomes a Problem

为每个组合 创建 class 会造成 subclass 数量膨胀，并重复发送逻辑。

## The Idea

Notice 把发送交给 Channel；UrgentNotice 改变消息 behavior，不决定传输方式。

## Real-World Analogy

遥控器和通信链路可以分别升级，只要共享一个小协议。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Bridge](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## Participants

Notice 是 [`abstraction`](../../GLOSSARY.md#abstraction)，UrgentNotice 扩展 abstraction，Channel 是实现 [`interface`](../../GLOSSARY.md#interface)，Email 与 Sms 负责发送。

本例中的标准角色：

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — Bridge 中提供高层操作并委托实现工作的角色。 对应代码： `Notice`。
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — 独立于实现侧的 Abstraction 特化。 对应代码： `UrgentNotice`。
- [`Implementor`](../../GLOSSARY.md#implementor) — Bridge 的 Abstraction 用于底层工作的约定。 对应代码： `Channel`。
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — Implementor 约定的一种具体 implementation。 对应代码： `Email, Sms`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <string_view>

struct Channel {
    virtual ~Channel() = default;
    virtual void deliver(std::string_view text) const = 0;
};
struct Email final : Channel {
    void deliver(std::string_view text) const override { std::cout << "Email: " << text << '\n'; }
};
struct Sms final : Channel {
    void deliver(std::string_view text) const override { std::cout << "SMS: " << text << '\n'; }
};
class Notice {
protected:
    const Channel& channel_;
public:
    explicit Notice(const Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void send() const { channel_.deliver("status normal"); }
};
class UrgentNotice final : public Notice {
public:
    using Notice::Notice;
    void send() const override { channel_.deliver("URGENT: disk full"); }
};
int main() {
    const Email email;
    const Sms sms;
    Notice{email}.send();
    UrgentNotice{email}.send();
    UrgentNotice{sms}.send();
}
```

## Example Output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## When to Use

两个变化轴会导致 subclass 组合爆炸时使用。

### Use cases

适合形状与渲染后端、 通知 class 型与发送渠道这样的独立维度。

## When NOT to Use

只有一个简单变化维度， function 参数就足够时，不必 Bridge。

## Advantages

新渠道可直接服务已有 通知 class 型，不必补齐所有 组合的 class。

## Trade-offs

增加间接调用，需要清晰的分界；借用的渠道必须比通知活得更久。

## Related Patterns

[Adapter](../adapter/README.zh-CN.md) · [Strategy](../../behavioral/strategy/README.zh-CN.md)

## Common Confusion

Adapter 解决已有 interface 不匹配； Bridge 通常主动分离独立演进的维度。 Strategy 更关注可替换 behavior。

## Terms to Remember

- `Bridge` — 把两个变化维度分开，再用 composition 连接。
- `Abstraction` — Bridge 中提供高层操作并委托实现工作的角色。 示例： `Notice`。
- `Refined Abstraction` — 独立于实现侧的 Abstraction 特化。 示例： `UrgentNotice`。
- `Implementor` — Bridge 的 Abstraction 用于底层工作的约定。 示例： `Channel`。
- `Concrete Implementor` — Implementor 约定的一种具体 implementation。 示例： `Email, Sms`。

## Interview Vocabulary

- [`object composition`](../../GLOSSARY.md#object-composition) — 连接多个 object，形成更大的行为或结构。
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — 当协作 object 能更清楚地表达变化时，优先使用它们而不是扩展 inheritance 层次。
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — 把会变化的设计决策放在稳定边界之后。

## Interview Question

增加 Push 和 ScheduledNotice 时，有无 Bridge 分别需要 多少 class？

## Mini Challenge

添加 Push 渠道，不修改现有两种 通知 class。

## 检查理解

1. 只增加发送渠道时，哪些 Class 需要改变？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 通知同时按紧急程度和发送渠道变化，两边都需要独立扩展。
- **方案:** Notice 把发送交给 Channel；UrgentNotice 改变消息 behavior，不决定传输方式。
- **权衡:** 增加间接调用，需要清晰的分界；借用的渠道必须比通知活得更久。
- **记忆提示:** 两个维度，一条连接。

[上一个](../../structural/adapter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/composite/README.zh-CN.md)
