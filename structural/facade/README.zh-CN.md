# 外观

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/decorator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/flyweight/README.zh-CN.md)

## 类别

结构型

## 难度

入门

## 一句话说明

为子系统的常见流程提供一个小而清晰的入口。

## 问题

每个结账调用方都要按顺序检查库存、扣款和发货。

## 最初的简单方案

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## 为什么难以维护

直接调用可能漏掉库存检查，也会在不同调用点重复编排逻辑。

## 核心思路

Checkout 提供 buy，在操作内部协调多个服务。

## 生活类比

餐厅前台帮你协调预订，不必自己联系每个部门。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![外观](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## 参与者

Stock 检查库存，Payment 扣款，Shipping 发货，Checkout 提供公共流程。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount) const { std::cout << "Charged " << amount << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

## 预期输出

```text
Charged 20
Dispatched
Unavailable
```

## 何时使用

多个调用方都需要复杂子系统中同一部分能力时使用。

## 何时不该使用

只是毫无简化作用的转发层时，不必使用。

## 优点

调用方依赖更小的接口，流程顺序集中维护。

## 缺点与权衡

外观可能变成包办一切的大对象。示例没有事务保证；真实支付、发货失败需要补偿或其他一致性方案。

## 技术应用场景

适合 SDK 入口和应用服务边界；示例没有接入真实支付。

## 相关模式

[adapter](../adapter/README.zh-CN.md) · [mediator](../../behavioral/mediator/README.zh-CN.md)

## 常见混淆

适配器处理兼容性；外观缩小子系统的使用范围，不必实现已有接口。

## 面试问题

扣款成功但发货失败时，buy 实际能保证什么？

## 小练习

模拟发货失败，设计明确的退款结果，不要默默返回成功。

## 小结

- **问题:** 每个结账调用方都要按顺序检查库存、扣款和发货。
- **方案:** Checkout 提供 buy，在操作内部协调多个服务。
- **权衡:** 外观可能变成包办一切的大对象。示例没有事务保证；真实支付、发货失败需要补偿或其他一致性方案。
- **记忆提示:** 多项服务，一个入口。

[上一个](../../structural/decorator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/flyweight/README.zh-CN.md)
