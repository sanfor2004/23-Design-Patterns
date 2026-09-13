# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/state/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/template-method/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

入门

## In One Sentence

给需要 algorithm 的 object 传入可替换的 behavior。

## 简单理解

结账时可以计算普通或加急运费。Strategy 把运费规则交给 Checkout 调用，总价计算就不用包含所有规则。

## The Problem

结账需要不同运费规则，不应把每条规则混进结账流程。

## Naive Solution

```cpp
int fee = express ? (subtotal_cents >= 100 ? 0 : 15) : 5;
```

## Why It Becomes a Problem

一个条件表达式很清楚，但在多条结账路径重复 policy 分支，会增加扩展与测试成本。

## The Idea

Checkout 拥有 ShippingRule callable，用它计算运费，由 Client 在构造时选择。

## Real-World Analogy

同一目的地，可以选择步行或驾车路线规划。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Participants

Checkout 是 Context，ShippingRule 是 behavior 契约，lambda 分别实现普通和加急规则。

本例中的标准角色：

- [`Context`](../../GLOSSARY.md#context) — 使用 Strategy 或把 behavior 委托给当前 State 的 object。 对应代码： `Checkout`。
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — Context 所使用的可替换 algorithm 的约定。 对应代码： `ShippingRule`。
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — Strategy interface 的一种具体 implementation，可以是 callable 而不必是 class。 对应代码： `standard / express lambdas`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal_cents) const {
        if (subtotal_cents < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal_cents + shipping_(subtotal_cents);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal_cents) { return subtotal_cents >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
    std::cout << "Express boundary: " << express.total(100) << '\n';
    try { static_cast<void>(standard.total(-1)); }
    catch (const std::invalid_argument&) { std::cout << "Negative subtotal rejected\n"; }
    try { const Checkout missing{ShippingRule{}}; }
    catch (const std::invalid_argument&) { std::cout << "Missing rule rejected\n"; }
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
Express boundary: 100
Negative subtotal rejected
Missing rule rejected
```

## When to Use

algorithm 独立变化， Client 需要选择 Strategy 时使用。

### Use cases

适合定价规则、排序评分和 retry policy。

## When NOT to Use

只有一种稳定 algorithm，或单个清晰条件没有扩展压力时，不必增加 [`abstraction`](../../GLOSSARY.md#abstraction)。

## Advantages

Strategy 能独立测试，总价计算保持共用。

## Trade-offs

[`std::function`](../../GLOSSARY.md#stdfunction) 带来 [`type erasure`](../../GLOSSARY.md#type-erasure) ，也可能进行 [`memory allocation`](../../GLOSSARY.md#memory-allocation)；template 或 function pointer 适合不同约束。外部 policy 可能返回非法费用时应校验结果。

## Related Patterns

[State](../state/README.zh-CN.md) · [Template Method](../template-method/README.zh-CN.md)

## Common Confusion

State 表示 [`lifecycle`](../../GLOSSARY.md#lifecycle) 与转换， Strategy 选择 algorithm； Template Method 通过 [`inheritance`](../../GLOSSARY.md#inheritance) 定制步骤，而非注入 callable。

## Terms to Remember

- `Strategy` — 让 object 在几种完成同一任务的 algorithm 中选择。
- `Context` — 使用 Strategy 或把 behavior 委托给当前 State 的 object。 示例： `Checkout`。
- `Strategy interface` — Context 所使用的可替换 algorithm 的约定。 示例： `ShippingRule`。
- `Concrete Strategy` — Strategy interface 的一种具体 implementation，可以是 callable 而不必是 class。 示例： `standard / express lambdas`。

## Interview Vocabulary

- [`interchangeable behavior`](../../GLOSSARY.md#interchangeable-behavior) — 可以通过同一约定提供的不同 behavior。
- [`encapsulate an algorithm`](../../GLOSSARY.md#encapsulate-an-algorithm) — 把 algorithm 放在隐藏其内部步骤的操作之后。
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — 当协作 object 能更清楚地表达变化时，优先使用它们而不是扩展 inheritance 层次。
- [`runtime selection`](../../GLOSSARY.md#runtime-selection) — 在程序执行期间选择 implementation。
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — 各部分只了解协作所需的小范围约定，限制修改传播。

## Interview Question

改用 template 参数会怎样影响 [`runtime`](../../GLOSSARY.md#runtime) 选择和编译？

## Mini Challenge

添加满 80 免运费规则，测试 79、80、81。

## 检查理解

1. 本例 Checkout 的公共 API 能在创建后更换规则吗？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 结账需要不同运费规则，不应把每条规则混进结账流程。
- **方案:** Checkout 拥有 ShippingRule callable，用它计算运费，由 Client 在构造时选择。
- **权衡:** std::function 带来 type erasure ，也可能进行 memory allocation；template 或 function pointer 适合不同约束。外部 policy 可能返回非法费用时应校验结果。
- **记忆提示:** 任务相同， algorithm 可选。

[上一个](../../behavioral/state/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/template-method/README.zh-CN.md)
