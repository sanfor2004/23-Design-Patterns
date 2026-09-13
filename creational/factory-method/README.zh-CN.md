# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/builder/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/prototype/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — 关注如何创建和配置 object 的 Design Pattern。

## Difficulty

入门

## In One Sentence

让 subclass 决定公共流程所使用的 concrete object。

## 简单理解

通知任务发送相同消息，但发送方式不同。流程调用 Factory Method，由各个 subclass 创建合适的 Sender。

## The Problem

通知任务总是发送完成消息，但不同环境需要不同发送方式。

## Naive Solution

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Why It Becomes a Problem

在 run 中直接创建 EmailSender 会把流程绑定到邮件；复制一份流程用于控制台又产生重复。

这就是 `tight coupling`：流程直接绑定某个具体 Sender，发送方式改变时，流程也可能需要修改。

## The Idea

把流程放在 AlertJob 中，并通过可重写的 make_sender 创建产品。

## Real-World Analogy

配送站遵循同一派送流程，各分站选择自己的运输工具。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Participants

AlertJob 管理流程；EmailJob、ConsoleJob 重写创建步骤；Sender 提供操作，返回的 [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) 拥有产品。

本例中的标准角色：

- [`Creator`](../../GLOSSARY.md#creator) — 拥有公共流程并声明创建操作的基础角色。 对应代码： `AlertJob`。
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — 提供某种 Product 的 Creator subclass。 对应代码： `EmailJob, ConsoleJob`。
- [`Product`](../../GLOSSARY.md#product) — 创建代码返回的 object 所提供的约定。 对应代码： `Sender`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(std::string_view message) const = 0;
};
struct EmailSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Email: " << message << '\n'; }
};
struct ConsoleSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Console: " << message << '\n'; }
};
class AlertJob {
protected:
    virtual std::unique_ptr<Sender> make_sender() const = 0;
public:
    virtual ~AlertJob() = default;
    void run() const {
        const auto sender = make_sender();
        sender->send("build complete");
    }
};
class EmailJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<EmailSender>(); }
};
class ConsoleJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<ConsoleSender>(); }
};
int main() {
    EmailJob{}.run();
    ConsoleJob{}.run();
}
```

## Example Output

```text
Email: build complete
Console: build complete
```

## When to Use

已有 [`inheritance`](../../GLOSSARY.md#inheritance) 体系中的公共流程需要 可扩展（extensibility） 的创建步骤时使用。

### Use cases

适合 可扩展（extensibility） 导出器或按环境选择实现的任务执行器；示例发送器只打印。

## When NOT to Use

直接把 Sender 传给 function 就能解决时，不必引入 inheritance 层次。

## Advantages

流程只保留一份，产品选择可以独立变化。

## Trade-offs

新增选择可能需要新增 subclass。 base class constructor 中调用 virtual function 不会按预期分派到 derived class 重写。

## Related Patterns

[Abstract Factory](../abstract-factory/README.zh-CN.md) · [Template Method](../../behavioral/template-method/README.zh-CN.md)

## Common Confusion

含 switch 的普通创建 function 是简单工厂；这里强调 subclass 扩展点。 Abstract Factory 则协调一组相关产品。

## Terms to Remember

- `Factory Method` — 让 subclass 决定公共流程所使用的 concrete object。
- `Creator` — 拥有公共流程并声明创建操作的基础角色。 示例： `AlertJob`。
- `Concrete Creator` — 提供某种 Product 的 Creator subclass。 示例： `EmailJob, ConsoleJob`。
- `Product` — 创建代码返回的 object 所提供的约定。 示例： `Sender`。

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — 选择具体类型，建立 object 的初始值并开始其 lifetime。
- [`tight coupling`](../../GLOSSARY.md#tight-coupling) — 各部分过度依赖彼此的具体细节，修改容易扩散。
- [`inheritance`](../../GLOSSARY.md#inheritance) — 从 base class 定义 derived class，复用或扩展约定及实现。
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — 在选定的有效边界上追求 open for extension, closed for modification。

## Interview Question

为什么在构造完成后的 run 中调用 make_sender，而不是在 base class constructor 中调用？

## Mini Challenge

添加 FileJob，把消息写入临时文件，并验证文件内容。

## 检查理解

1. 在哪里选择 Sender？哪些流程保持共用？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 通知任务总是发送完成消息，但不同环境需要不同发送方式。
- **方案:** 把流程放在 AlertJob 中，并通过可重写的 make_sender 创建产品。
- **权衡:** 新增选择可能需要新增 subclass。 base class constructor 中调用 virtual function 不会按预期分派到 derived class 重写。
- **记忆提示:** 保留流程，重写创建步骤。

[上一个](../../creational/builder/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/prototype/README.zh-CN.md)
