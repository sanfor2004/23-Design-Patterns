# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[类别](../README.zh-CN.md) · [下一个](../../creational/builder/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — 关注如何创建和配置 object 的 Design Pattern。

## Difficulty

中级

## In One Sentence

通过统一的工厂 [`interface`](../../GLOSSARY.md#interface) 创建相互配套的 object。

## 简单理解

界面的按钮和面板需要使用同一主题。选择一个 Factory 来创建两者，调用方就不用分别选择具体 Class。

## The Problem

设置页面需要风格一致的按钮和面板。

## Naive Solution

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Why It Becomes a Problem

各处直接创建控件，容易把深色按钮和浅色面板混在一起。每个 Client 都得记住搭配规则。

## The Idea

给 render 传入一个 Theme，由它创建两类产品， Client 只依赖 Product interface。

## Real-World Analogy

买成套家具，比逐件确认风格是否一致更省心。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Abstract Factory](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## Participants

Theme 定义 Product family；DarkTheme 和 LightTheme 创建 Concrete Product。Button、Panel 是 Product interface，render 负责使用。

本例中的标准角色：

- [`Product`](../../GLOSSARY.md#product) — 创建代码返回的 object 所提供的约定。 对应代码： `Button, Panel`。
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — Product 约定的一种具体 implementation。 对应代码： `DarkButton, LightButton, DarkPanel, LightPanel`。
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — 创建一组配套 Product 的 implementation。 对应代码： `DarkTheme, LightTheme`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Button {
    virtual ~Button() = default;
    virtual std::string_view paint() const = 0;
};
struct Panel {
    virtual ~Panel() = default;
    virtual std::string_view paint() const = 0;
};
struct DarkButton final : Button {
    std::string_view paint() const override { return "dark button"; }
};
struct DarkPanel final : Panel {
    std::string_view paint() const override { return "dark panel"; }
};
struct LightButton final : Button {
    std::string_view paint() const override { return "light button"; }
};
struct LightPanel final : Panel {
    std::string_view paint() const override { return "light panel"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Panel> panel() const = 0;
};
struct DarkTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<DarkPanel>(); }
};
struct LightTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<LightPanel>(); }
};
void render(const Theme& theme) {
    const auto button = theme.button();
    const auto panel = theme.panel();
    std::cout << button->paint() << " + " << panel->paint() << '\n';
}
int main() {
    render(DarkTheme{});
    render(LightTheme{});
}
```

## Example Output

```text
dark button + dark panel
light button + light panel
```

## When to Use

当多种产品必须一起切换，且 Client 不应决定 concrete type 时使用。

### Use cases

主题组件库、配套数据库驱动是合适的设计场景；示例仅输出名称。

## When NOT to Use

只有一种稳定产品，或者产品本来就应该自由组合时，不必使用。

## Advantages

切换整个 Product family，不需要修改渲染流程。

## Trade-offs

新增 Slider 这样的产品 type 时，每个工厂都要修改。 interface 本身也无法保证实现真的保持视觉一致。

## Related Patterns

[Factory Method](../factory-method/README.zh-CN.md) · [Builder](../builder/README.zh-CN.md)

## Common Confusion

Factory Method 改变一个创建步骤； Abstract Factory 组织多种相关产品，内部可以使用 Factory Method。

## Terms to Remember

- `Abstract Factory` — 通过统一的工厂 interface 创建相互配套的 object。
- `Product` — 创建代码返回的 object 所提供的约定。 示例： `Button, Panel`。
- `Concrete Product` — Product 约定的一种具体 implementation。 示例： `DarkButton, LightButton, DarkPanel, LightPanel`。
- `Concrete Factory` — 创建一组配套 Product 的 implementation。 示例： `DarkTheme, LightTheme`。

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — 选择具体类型，建立 object 的初始值并开始其 lifetime。
- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — 依赖公开约定，而不是某个具体 implementation。
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — 把会变化的设计决策放在稳定边界之后。

## Interview Question

新增主题和新增控件 type，分别会影响哪些 interface？

## Mini Challenge

增加高对比度主题，再增加 Slider 产品，对比两次修改的范围。

## 检查理解

1. 为什么同一个 Theme 要创建两种产品？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 设置页面需要风格一致的按钮和面板。
- **方案:** 给 render 传入一个 Theme，由它创建两类产品， Client 只依赖 Product interface。
- **权衡:** 新增 Slider 这样的产品 type 时，每个工厂都要修改。 interface 本身也无法保证实现真的保持视觉一致。
- **记忆提示:** 一个工厂，一套产品。

[类别](../README.zh-CN.md) · [下一个](../../creational/builder/README.zh-CN.md)
