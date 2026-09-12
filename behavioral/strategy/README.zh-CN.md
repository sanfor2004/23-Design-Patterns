# 策略

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/state/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/template-method/README.zh-CN.md)

## 类别

行为型

## 难度

入门

## 一句话说明

给需要算法的对象传入可替换的行为。

## 问题

结账需要不同运费规则，不应把每条规则混进结账流程。

## 最初的简单方案

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## 为什么难以维护

一个条件表达式很清楚，但在多条结账路径重复策略分支，会增加扩展与测试成本。

## 核心思路

Checkout 拥有 ShippingRule 可调用对象，用它计算运费，由调用方在构造时选择。

## 生活类比

同一目的地，可以选择步行或驾车路线规划。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![策略](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## 参与者

Checkout 是上下文，ShippingRule 是行为契约，lambda 分别实现普通和加急规则。

## 现代 C++20 完整可运行示例

```cpp
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
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## 预期输出

```text
Standard: 45
Express: 55
Express large: 120
```

## 何时使用

算法独立变化，调用方需要选择策略时使用。

## 何时不该使用

只有一种稳定算法，或单个清晰条件没有扩展压力时，不必抽象。

## 优点

策略能独立测试，总价计算保持共用。

## 缺点与权衡

std::function 带来类型擦除且可能分配内存；模板或函数指针适合不同约束。外部策略可能返回非法费用时应校验结果。

## 技术应用场景

适合定价规则、排序评分和重试策略。

## 相关模式

[state](../state/README.zh-CN.md) · [template-method](../template-method/README.zh-CN.md)

## 常见混淆

状态表示生命周期与转换，策略选择算法；模板方法通过继承定制步骤，而非注入可调用对象。

## 面试问题

改用模板参数会怎样影响运行时选择和编译？

## 小练习

添加满 80 免运费规则，测试 79、80、81。

## 小结

- **问题:** 结账需要不同运费规则，不应把每条规则混进结账流程。
- **方案:** Checkout 拥有 ShippingRule 可调用对象，用它计算运费，由调用方在构造时选择。
- **权衡:** std::function 带来类型擦除且可能分配内存；模板或函数指针适合不同约束。外部策略可能返回非法费用时应校验结果。
- **记忆提示:** 任务相同，算法可选。

[上一个](../../behavioral/state/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/template-method/README.zh-CN.md)
