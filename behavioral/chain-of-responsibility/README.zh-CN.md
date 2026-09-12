# 责任链

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/proxy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/command/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

让请求沿处理器传递，每个处理器可以停止或继续。

## 问题

请求要通过身份和金额检查，不同入口需要不同策略组合。

## 最初的简单方案

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## 为什么难以维护

一个表达式起初足够，但复制到多条流程后，顺序与复用变得难维护。

## 核心思路

每个 Handler 检查自己的规则，成功后再委托；最后一个检查通过即接受。

## 生活类比

客服能处理就处理，否则交给下一位专员。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![责任链](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## 参与者

Handler 拥有后继，Auth 检查身份，Limit 检查金额，调用方组装顺序。

## 现代 C++20 完整可运行示例

```cpp
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount; };
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
    bool accepts(const Request& request) const override { return request.amount > 0 && request.amount <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

## 预期输出

```text
Rejected
Rejected
Accepted
```

## 何时使用

处理步骤的顺序或成员需要独立组合时使用。

## 何时不该使用

只有一个地方的两个固定检查时，原表达式更清晰。

## 优点

检查可复用、可重排，无需庞大条件分支。

## 缺点与权衡

顺序会影响行为，链尾策略必须明确。本例全部通过才接受，其他链可能拒绝无人处理的请求。

## 技术应用场景

适合校验管线和请求中间件；本变体要求全部批准，而非第一个成功处理器即结束。

## 相关模式

[decorator](../../structural/decorator/README.zh-CN.md) · [command](../command/README.zh-CN.md)

## 常见混淆

装饰器叠加行为；此责任链可能提前结束。命令则把请求本身表示为对象。

## 面试问题

如果昂贵的 Limit 放在前面，未认证请求会产生什么额外工作？

## 小练习

添加维护模式处理器，验证被拒绝的请求不会进入后续检查。

## 小结

- **问题:** 请求要通过身份和金额检查，不同入口需要不同策略组合。
- **方案:** 每个 Handler 检查自己的规则，成功后再委托；最后一个检查通过即接受。
- **权衡:** 顺序会影响行为，链尾策略必须明确。本例全部通过才接受，其他链可能拒绝无人处理的请求。
- **记忆提示:** 处理，或者传递。

[上一个](../../structural/proxy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/command/README.zh-CN.md)
