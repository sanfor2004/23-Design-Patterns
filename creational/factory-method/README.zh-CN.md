# 工厂方法

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/builder/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/prototype/README.zh-CN.md)

## 类别

创建型

## 难度

入门

## 一句话说明

让子类决定公共流程所使用的具体对象。

## 问题

通知任务总是发送完成消息，但不同环境需要不同发送方式。

## 最初的简单方案

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## 为什么难以维护

在 run 中直接创建 EmailSender 会把流程绑定到邮件；复制一份流程用于控制台又产生重复。

## 核心思路

把流程放在 AlertJob 中，并通过可重写的 make_sender 创建产品。

## 生活类比

配送站遵循同一派送流程，各分站选择自己的运输工具。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![工厂方法](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## 参与者

AlertJob 管理流程；EmailJob、ConsoleJob 重写创建步骤；Sender 提供操作，返回的 unique_ptr 拥有产品。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
Email: build complete
Console: build complete
```

## 何时使用

已有继承体系中的公共流程需要可扩展的创建步骤时使用。

## 何时不该使用

直接把 Sender 传给函数就能解决时，不必引入继承层次。

## 优点

流程只保留一份，产品选择可以独立变化。

## 缺点与权衡

新增选择可能需要新增子类。基类构造函数中调用虚函数不会按预期分派到派生类重写。

## 技术应用场景

适合可扩展导出器或按环境选择实现的任务执行器；示例发送器只打印。

## 相关模式

[abstract-factory](../abstract-factory/README.zh-CN.md) · [template-method](../../behavioral/template-method/README.zh-CN.md)

## 常见混淆

含 switch 的普通创建函数是简单工厂；这里强调子类扩展点。抽象工厂则协调一组相关产品。

## 面试问题

为什么在构造完成后的 run 中调用 make_sender，而不是在基类构造函数中调用？

## 小练习

添加 FileJob，把消息写入临时文件，并验证文件内容。

## 小结

- **问题:** 通知任务总是发送完成消息，但不同环境需要不同发送方式。
- **方案:** 把流程放在 AlertJob 中，并通过可重写的 make_sender 创建产品。
- **权衡:** 新增选择可能需要新增子类。基类构造函数中调用虚函数不会按预期分派到派生类重写。
- **记忆提示:** 保留流程，重写创建步骤。

[上一个](../../creational/builder/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/prototype/README.zh-CN.md)
