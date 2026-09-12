# 装饰器

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/composite/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/facade/README.zh-CN.md)

## 类别

结构型

## 难度

入门

## 一句话说明

用实现相同接口的包装对象叠加行为。

## 问题

咖啡可以加一次或多次牛奶，不应为每种组合都创建专用类型。

## 最初的简单方案

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## 为什么难以维护

组合类重复基础定价，新增配料后数量继续增长。

## 核心思路

Milk 拥有一个 Drink，先委托，再增加自己的描述和价格。

## 生活类比

一层包装纸包住上一层，包装后的礼物仍能继续被包装。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![装饰器](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## 参与者

Drink 是共同契约，Coffee 提供基础行为，Milk 包装一个 Drink，调用方拥有最外层。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
coffee + milk + milk: 14
```

## 何时使用

适合可选、可组合且保持原契约的附加行为。

## 何时不该使用

如果配料列表加求和已经足够，就别用类层层包装；本例着重展示结构。

## 优点

运行时组合附加行为，基础实现保持简洁。

## 缺点与权衡

包装顺序可能改变行为；大量小对象增加调试难度，相同接口也不自动保证所有语义约束。

## 技术应用场景

流的压缩和加密层是典型设计场景，需要明确顺序与失败处理。

## 相关模式

[proxy](../proxy/README.zh-CN.md) · [composite](../composite/README.zh-CN.md)

## 常见混淆

代理控制访问，装饰器增加职责。仅看包装结构不能判断意图。

## 面试问题

在加密前记录日志与加密后记录日志，看到的数据一样吗？

## 小练习

增加价格为 3 的 Syrup，尝试两种包装顺序并解释描述差异。

## 小结

- **问题:** 咖啡可以加一次或多次牛奶，不应为每种组合都创建专用类型。
- **方案:** Milk 拥有一个 Drink，先委托，再增加自己的描述和价格。
- **权衡:** 包装顺序可能改变行为；大量小对象增加调试难度，相同接口也不自动保证所有语义约束。
- **记忆提示:** 契约不变，再加一层。

[上一个](../../structural/composite/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/facade/README.zh-CN.md)
