# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/decorator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/flyweight/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — 关注 object 与 class 如何组织在一起的 Design Pattern。

## Difficulty

入门

## In One Sentence

为 subsystem 的常见流程提供一个小而清晰的入口。

## 简单理解

购买流程需要依次检查库存、付款和发货。Facade 把常用流程放进一次调用，但不会自动保证 Transaction。

## The Problem

每个结账 Client 都要按顺序检查库存、扣款和发货。

## Naive Solution

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Why It Becomes a Problem

直接调用可能漏掉库存检查，也会在不同调用点重复编排逻辑。

## The Idea

Checkout 提供 buy，在操作内部协调多个服务。

## Real-World Analogy

餐厅前台帮你协调预订，不必自己联系每个部门。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Participants

Stock 检查库存，Payment 扣款，Shipping 发货，Checkout 提供公共流程。

本例中的标准角色：

- [`subsystem`](../../GLOSSARY.md#subsystem) — 较大系统中相互协作的一组服务或 object。 对应代码： `Stock, Payment, Shipping`。
- [`interface`](../../GLOSSARY.md#interface) — 约定可调用的操作及其对外可观察行为。 对应代码： `Checkout::buy`。
- [`Client`](../../GLOSSARY.md#client-pattern-role) — 使用 interface 或与模式中的 object 协作的代码。 对应代码： `main`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount_cents) const { std::cout << "Charged " << amount_cents << '\n'; }
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

## Example Output

```text
Charged 20
Dispatched
Unavailable
```

## When to Use

多个 Client 都需要复杂 subsystem 中同一部分能力时使用。

### Use cases

适合 SDK 入口和应用服务边界；示例没有接入真实支付。

## When NOT to Use

只是毫无简化作用的转发层时，不必使用。

## Advantages

Client 依赖更小的 interface，流程顺序集中维护。

## Trade-offs

Facade 可能变成包办一切的大 object。示例没有事务保证；真实支付、发货失败需要补偿或其他一致性方案。

## Related Patterns

[Adapter](../adapter/README.zh-CN.md) · [Mediator](../../behavioral/mediator/README.zh-CN.md)

## Common Confusion

Adapter 处理兼容性； Facade 缩小 subsystem 的使用范围，不必实现已有 interface。

## Terms to Remember

- `Facade` — 为 subsystem 的常见流程提供一个小而清晰的入口。
- `subsystem` — 较大系统中相互协作的一组服务或 object。 示例： `Stock, Payment, Shipping`。
- `interface` — 约定可调用的操作及其对外可观察行为。 示例： `Checkout::buy`。
- `Client` — 使用 interface 或与模式中的 object 协作的代码。 示例： `main`。

## Interview Vocabulary

- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — 把不同关注点分开，使它们能够独立变化。
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — 各部分只了解协作所需的小范围约定，限制修改传播。
- [`trade-off`](../../GLOSSARY.md#trade-off) — 获得一种好处时付出的另一种代价。

## Interview Question

扣款成功但发货失败时，buy 实际能保证什么？

## Mini Challenge

模拟发货失败，设计明确的退款结果，不要默默返回成功。

## 检查理解

1. 付款后发货失败时，buy 无法保证什么？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 每个结账 Client 都要按顺序检查库存、扣款和发货。
- **方案:** Checkout 提供 buy，在操作内部协调多个服务。
- **权衡:** Facade 可能变成包办一切的大 object。示例没有事务保证；真实支付、发货失败需要补偿或其他一致性方案。
- **记忆提示:** 多项服务，一个入口。

[上一个](../../structural/decorator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/flyweight/README.zh-CN.md)
