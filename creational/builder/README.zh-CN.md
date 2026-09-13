# Builder

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/abstract-factory/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/factory-method/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — 关注如何创建和配置 object 的 Design Pattern。

## Difficulty

入门

## In One Sentence

用具名步骤配置 object，最后一次性生成结果。

## 简单理解

请求选项较多时，很难看出 constructor 中每个参数的含义。Builder 用命名步骤收集选项，检查后再生成结果。

## The Problem

请求包含地址、超时和重试选项；选项越多，位置参数越难理解。

## Naive Solution

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## Why It Becomes a Problem

constructor 能用，但连续的数字和布尔值隐藏了意图，传错位置不容易发现。

## The Idea

RequestBuilder 保存配置过程。具名 method 收集选项，build 检查必要值并按值返回 Request。

## Real-World Analogy

点三明治时先说清配料，厨房再制作成品。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Builder](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## Participants

RequestBuilder 保存和校验临时配置，Request 拥有最终数据， Client 决定可选步骤的顺序。

本例中的标准角色：

- [`Product`](../../GLOSSARY.md#product) — Builder 最终生成的 object。对应代码：`Request`。
- [`fluent interface`](../../GLOSSARY.md#fluent-interface) — 设计成链式调用的 interface；它本身并不等于 Builder。 对应代码： `RequestBuilder.endpoint().timeout().retry()`。
- [`constructor`](../../GLOSSARY.md#constructor) — 创建 class instance 时负责初始化的特殊操作。 对应代码： `Request::Request`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

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

## Example Output

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## When to Use

适合独立选项较多，或需要明确构建校验阶段的 object。

### Use cases

适合 HTTP 请求配置和测试数据构建；示例不发送网络请求。

## When NOT to Use

只有两个直观参数时，普通 constructor 或小型聚合 type 更简单。

## Advantages

调用点更易读，构建阶段可以拒绝不完整的配置。

## Trade-offs

需要维护额外 type。示例中 Request constructor 仍是 public 的；生产代码应在 constructor 中也校验，或限制直接访问。

## Related Patterns

[Factory Method](../factory-method/README.zh-CN.md) · [Abstract Factory](../abstract-factory/README.zh-CN.md)

## Common Confusion

Factory Method 在 [`inheritance`](../../GLOSSARY.md#inheritance) 流程中选择 Concrete Product， Builder 分步骤配置一个结果。

## Terms to Remember

- `Builder` — 用具名步骤配置 object，最后一次性生成结果。
- `Product` — Builder 最终生成的 object。示例：`Request`。
- `fluent interface` — 设计成链式调用的 interface；它本身并不等于 Builder。 示例： `RequestBuilder.endpoint().timeout().retry()`。
- `constructor` — 创建 class instance 时负责初始化的特殊操作。 示例： `Request::Request`。

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — 选择具体类型，建立 object 的初始值并开始其 lifetime。
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — 把不同关注点分开，使它们能够独立变化。
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — 让一个模块围绕一个连贯的变化原因组织职责。

## Interview Question

链式调用一定是 Builder 吗？请说明构建何时结束。

## Mini Challenge

拒绝大于 120 的超时值，测试边界值及紧邻的非法值。

## 检查理解

1. 绕过 build 直接创建 Request 会怎样？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 请求包含地址、超时和重试选项；选项越多，位置参数越难理解。
- **方案:** RequestBuilder 保存配置过程。具名 method 收集选项，build 检查必要值并按值返回 Request。
- **权衡:** 需要维护额外 type。示例中 Request constructor 仍是 public 的；生产代码应在 constructor 中也校验，或限制直接访问。
- **记忆提示:** 先选配置，再生成 object。

[上一个](../../creational/abstract-factory/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/factory-method/README.zh-CN.md)
