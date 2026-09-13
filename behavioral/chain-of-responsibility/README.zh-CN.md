# Chain of Responsibility

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/proxy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/command/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

让请求沿 Handler 传递，每个 Handler 可以停止或继续。

## 简单理解

请求需要通过身份检查和金额限制。每个 Handler 负责一项检查，调用方选择排列顺序。

## The Problem

请求要通过身份和金额检查，不同入口需要不同 policy 组合。

## Naive Solution

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount_cents > 0 && r.amount_cents <= 100;
}
```

## Why It Becomes a Problem

一个表达式起初足够，但复制到多条流程后，顺序与复用变得难维护。

## The Idea

每个 Handler 检查自己的规则，成功后再委托；最后一个检查通过即接受。

## Real-World Analogy

客服能处理就处理，否则交给下一位专员。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Chain of Responsibility](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## Participants

Handler 拥有后继，Auth 检查身份，Limit 检查金额， Client 组装顺序。

本例中的标准角色：

- [`Handler`](../../GLOSSARY.md#handler) — 处理请求或把请求传给后继的角色。 对应代码： `Handler`。
- [`Concrete Handler`](../../GLOSSARY.md#concrete-handler) — 实现某项处理规则的 Handler。 对应代码： `Auth, Limit`。
- [`chain termination`](../../GLOSSARY.md#chain-termination) — 决定处理链何时停止以及最后一个 Handler 之后如何处理的规则。 对应代码： `Handler::handle`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount_cents; };
class Handler {
    std::unique_ptr<Handler> next_;
protected:
    virtual bool accepts(const Request& request) const = 0;
public:
    explicit Handler(std::unique_ptr<Handler> next = {}) : next_(std::move(next)) {}
    virtual ~Handler() = default;
    bool handle(const Request& request) const {
        if (!accepts(request)) return false;
        return next_ ? next_->handle(request) : true;
    }
};
class Auth final : public Handler {
    bool accepts(const Request& request) const override { return request.authenticated; }
public:
    using Handler::Handler;
};
class Limit final : public Handler {
    bool accepts(const Request& request) const override { return request.amount_cents > 0 && request.amount_cents <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

## Example Output

```text
Rejected
Rejected
Accepted
```

## When to Use

处理步骤的顺序或成员需要独立组合时使用。

### Use cases

适合校验管线和请求中间件；本变体要求全部批准，而非第一个成功 Handler 即结束。

## When NOT to Use

只有一个地方的两个固定检查时，原表达式更清晰。

## Advantages

检查可复用、可重排，无需庞大条件分支。

## Trade-offs

顺序会影响 behavior， chain termination policy 必须明确。本例全部通过才接受，其他链可能拒绝无人处理的请求。

## Related Patterns

[Decorator](../../structural/decorator/README.zh-CN.md) · [Command](../command/README.zh-CN.md)

## Common Confusion

Decorator 叠加 behavior；此 Chain of Responsibility 可能提前结束。 Command 则把请求本身表示为 object。

## Terms to Remember

- `Chain of Responsibility` — 让请求沿 Handler 传递，每个 Handler 可以停止或继续。
- `Handler` — 处理请求或把请求传给后继的角色。 示例： `Handler`。
- `Concrete Handler` — 实现某项处理规则的 Handler。 示例： `Auth, Limit`。
- `chain termination` — 决定处理链何时停止以及最后一个 Handler 之后如何处理的规则。 示例： `Handler::handle`。

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — 一个 object 把部分工作交给协作方完成。
- [`object composition`](../../GLOSSARY.md#object-composition) — 连接多个 object，形成更大的行为或结构。
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — 各部分只了解协作所需的小范围约定，限制修改传播。

## Interview Question

如果昂贵的 Limit 放在前面，未认证请求会产生什么额外工作？

## Mini Challenge

添加维护模式 Handler，验证被拒绝的请求不会进入后续检查。

## 检查理解

1. 到达本例链尾意味着什么？检查何时停止处理？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 请求要通过身份和金额检查，不同入口需要不同 policy 组合。
- **方案:** 每个 Handler 检查自己的规则，成功后再委托；最后一个检查通过即接受。
- **权衡:** 顺序会影响 behavior， chain termination policy 必须明确。本例全部通过才接受，其他链可能拒绝无人处理的请求。
- **记忆提示:** 处理，或者传递。

[上一个](../../structural/proxy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/command/README.zh-CN.md)
