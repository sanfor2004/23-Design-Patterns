# 建造者

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/abstract-factory/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/factory-method/README.zh-CN.md)

## 类别

创建型

## 难度

入门

## 一句话说明

用具名步骤配置对象，最后一次性生成结果。

## 问题

请求包含地址、超时和重试选项；选项越多，位置参数越难理解。

## 最初的简单方案

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## 为什么难以维护

构造函数能用，但连续的数字和布尔值隐藏了意图，传错位置不容易发现。

## 核心思路

RequestBuilder 保存配置过程。具名方法收集选项，build 检查必要值并按值返回 Request。

## 生活类比

点三明治时先说清配料，厨房再制作成品。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![建造者](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## 参与者

RequestBuilder 保存和校验临时配置，Request 拥有最终数据，调用方决定可选步骤的顺序。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Request {
    std::string endpoint_;
    int timeout_;
    bool retry_;
public:
    Request(std::string endpoint, int timeout, bool retry)
        : endpoint_(std::move(endpoint)), timeout_(timeout), retry_(retry) {}
    void describe() const {
        std::cout << endpoint_ << " timeout=" << timeout_ << " retry=" << retry_ << '\n';
    }
};
class RequestBuilder {
    std::string endpoint_;
    int timeout_ = 30;
    bool retry_ = false;
public:
    RequestBuilder& endpoint(std::string value) { endpoint_ = std::move(value); return *this; }
    RequestBuilder& timeout(int seconds) { timeout_ = seconds; return *this; }
    RequestBuilder& retry(bool enabled) { retry_ = enabled; return *this; }
    Request build() const {
        if (endpoint_.empty() || timeout_ <= 0) throw std::invalid_argument("Invalid request");
        return Request{endpoint_, timeout_, retry_};
    }
};
int main() {
    const auto request = RequestBuilder{}.endpoint("/orders").timeout(5).retry(true).build();
    request.describe();
    try { static_cast<void>(RequestBuilder{}.build()); }
    catch (const std::invalid_argument&) { std::cout << "Invalid request rejected\n"; }
}
```

## 预期输出

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## 何时使用

适合独立选项较多，或需要明确构建校验阶段的对象。

## 何时不该使用

只有两个直观参数时，普通构造函数或小型聚合类型更简单。

## 优点

调用点更易读，构建阶段可以拒绝不完整的配置。

## 缺点与权衡

需要维护额外类型。示例中 Request 构造函数仍是公开的；生产代码应在构造函数中也校验，或限制直接访问。

## 技术应用场景

适合 HTTP 请求配置和测试数据构建；示例不发送网络请求。

## 相关模式

[factory-method](../factory-method/README.zh-CN.md) · [abstract-factory](../abstract-factory/README.zh-CN.md)

## 常见混淆

工厂方法在继承流程中选择具体产品，建造者分步骤配置一个结果。

## 面试问题

链式调用一定是建造者吗？请说明构建何时结束。

## 小练习

拒绝大于 120 的超时值，测试边界值及紧邻的非法值。

## 小结

- **问题:** 请求包含地址、超时和重试选项；选项越多，位置参数越难理解。
- **方案:** RequestBuilder 保存配置过程。具名方法收集选项，build 检查必要值并按值返回 Request。
- **权衡:** 需要维护额外类型。示例中 Request 构造函数仍是公开的；生产代码应在构造函数中也校验，或限制直接访问。
- **记忆提示:** 先选配置，再生成对象。

[上一个](../../creational/abstract-factory/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/factory-method/README.zh-CN.md)
