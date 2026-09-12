# 桥接

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/adapter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/composite/README.zh-CN.md)

## 类别

结构型

## 难度

中级

## 一句话说明

把两个变化维度分开，再用组合连接。

## 问题

通知同时按紧急程度和发送渠道变化，两边都需要独立扩展。

## 最初的简单方案

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## 为什么难以维护

为每个组合建类会造成子类数量膨胀，并重复发送逻辑。

## 核心思路

Notice 把发送交给 Channel；UrgentNotice 改变消息行为，不决定传输方式。

## 生活类比

遥控器和通信链路可以分别升级，只要共享一个小协议。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![桥接](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## 参与者

Notice 是抽象，UrgentNotice 扩展抽象，Channel 是实现接口，Email 与 Sms 负责发送。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## 何时使用

两个变化轴会导致子类组合爆炸时使用。

## 何时不该使用

只有一个简单变化维度，函数参数就足够时，不必桥接。

## 优点

新渠道可直接服务已有通知类型，不必补齐所有组合类。

## 缺点与权衡

增加间接调用，需要清晰的分界；借用的渠道必须比通知活得更久。

## 技术应用场景

适合形状与渲染后端、通知类型与发送渠道这样的独立维度。

## 相关模式

[adapter](../adapter/README.zh-CN.md) · [strategy](../../behavioral/strategy/README.zh-CN.md)

## 常见混淆

适配器解决已有接口不匹配；桥接通常主动分离独立演进的维度。策略更关注可替换行为。

## 面试问题

增加 Push 和 ScheduledNotice 时，有无桥接分别需要多少类？

## 小练习

添加 Push 渠道，不修改现有两种通知类。

## 小结

- **问题:** 通知同时按紧急程度和发送渠道变化，两边都需要独立扩展。
- **方案:** Notice 把发送交给 Channel；UrgentNotice 改变消息行为，不决定传输方式。
- **权衡:** 增加间接调用，需要清晰的分界；借用的渠道必须比通知活得更久。
- **记忆提示:** 两个维度，一条连接。

[上一个](../../structural/adapter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/composite/README.zh-CN.md)
