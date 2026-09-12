# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/composite/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/facade/README.zh-CN.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — 关注 object 与 class 如何组织在一起的 Design Pattern。

## Difficulty

入门

## In One Sentence

用实现相同 [`interface`](../../GLOSSARY.md#interface)（约定可调用的操作及其对外可观察行为） 的包装 object 叠加 behavior。

## The Problem

咖啡可以加一次或多次牛奶，不应为每种组合都创建专用 type。

## Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why It Becomes a Problem

组合的 class 重复基础定价，新增配料后数量继续增长。

## The Idea

Milk 拥有一个 Drink，先委托，再增加自己的描述和价格。

## Real-World Analogy

一层包装纸包住上一层，包装后的礼物仍能继续被包装。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Participants

Drink 是共同契约，Coffee 提供基础 behavior，Milk 包装一个 Drink， Client 拥有最外层。

本例中的标准角色：

- [`Component`](../../GLOSSARY.md#component) — 叶子、分组或包装层共同提供的约定。 对应代码： `Drink`。
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — 添加可选包装层之前的基础 implementation。 对应代码： `Coffee`。
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — 保留 Component 约定并增加某项 responsibility 的包装层。 对应代码： `Milk`。

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price() const override { return inner_->price() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use

适合可选、可组合且保持原契约的附加 behavior。

### Use cases

流的压缩和加密层是典型设计场景，需要明确顺序与失败处理。

## When NOT to Use

如果配料列表加求和已经足够，就别用类层层包装；本例着重展示结构。

## Advantages

[`runtime`](../../GLOSSARY.md#runtime)（编译后的程序正在执行的阶段） 组合附加 behavior， base [`implementation`](../../GLOSSARY.md#implementation)（实际完成操作或履行 interface 约定的代码） 保持简洁。

## Trade-offs

包装顺序可能改变 behavior；大量小 object 增加调试难度，相同 interface 也不自动保证所有语义约束。

## Related Patterns

[Proxy](../proxy/README.zh-CN.md) · [Composite](../composite/README.zh-CN.md)

## Common Confusion

Proxy 控制访问， Decorator 增加 responsibility。仅看包装结构不能判断意图。

## Terms to Remember

- `Decorator` — 用实现相同 interface 的包装 object 叠加 behavior。
- `Component` — 叶子、分组或包装层共同提供的约定。 示例： `Drink`。
- `Concrete Component` — 添加可选包装层之前的基础 implementation。 示例： `Coffee`。
- `Concrete Decorator` — 保留 Component 约定并增加某项 responsibility 的包装层。 示例： `Milk`。

## Interview Vocabulary

- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — 当协作 object 能更清楚地表达变化时，优先使用它们而不是扩展 inheritance 层次。
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — 由提供与整体相同约定的部分递归构建结构。
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — 让一个模块围绕一个连贯的变化原因组织职责。

## Interview Question

在加密前记录日志与加密后记录日志，看到的数据一样吗？

## Mini Challenge

增加价格为 3 的 Syrup，尝试两种包装顺序并解释描述差异。

## Quick Summary

- **问题:** 咖啡可以加一次或多次牛奶，不应为每种组合都创建专用 type。
- **方案:** Milk 拥有一个 Drink，先委托，再增加自己的描述和价格。
- **权衡:** 包装顺序可能改变 behavior；大量小 object 增加调试难度，相同 interface 也不自动保证所有语义约束。
- **记忆提示:** 契约不变，再加一层。

[上一个](../../structural/composite/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/facade/README.zh-CN.md)
