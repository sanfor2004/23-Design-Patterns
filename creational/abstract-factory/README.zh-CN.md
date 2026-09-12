# 抽象工厂

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[类别](../README.zh-CN.md) · [下一个](../../creational/builder/README.zh-CN.md)

## 类别

创建型

## 难度

中级

## 一句话说明

通过统一的工厂接口创建相互配套的对象。

## 问题

设置页面需要风格一致的按钮和面板。

## 最初的简单方案

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## 为什么难以维护

各处直接创建控件，容易把深色按钮和浅色面板混在一起。每个调用方都得记住搭配规则。

## 核心思路

给 render 传入一个 Theme，由它创建两类产品，调用方只依赖产品接口。

## 生活类比

买成套家具，比逐件确认风格是否一致更省心。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![抽象工厂](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## 参与者

Theme 定义产品族；DarkTheme 和 LightTheme 创建具体产品。Button、Panel 是产品接口，render 负责使用。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
dark button + dark panel
light button + light panel
```

## 何时使用

当多种产品必须一起切换，且调用方不应决定具体类型时使用。

## 何时不该使用

只有一种稳定产品，或者产品本来就应该自由组合时，不必使用。

## 优点

切换整个产品族，不需要修改渲染流程。

## 缺点与权衡

新增 Slider 这样的产品类型时，每个工厂都要修改。接口本身也无法保证实现真的保持视觉一致。

## 技术应用场景

主题组件库、配套数据库驱动是合适的设计场景；示例仅输出名称。

## 相关模式

[factory-method](../factory-method/README.zh-CN.md) · [builder](../builder/README.zh-CN.md)

## 常见混淆

工厂方法改变一个创建步骤；抽象工厂组织多种相关产品，内部可以使用工厂方法。

## 面试问题

新增主题和新增控件类型，分别会影响哪些接口？

## 小练习

增加高对比度主题，再增加 Slider 产品，对比两次修改的范围。

## 小结

- **问题:** 设置页面需要风格一致的按钮和面板。
- **方案:** 给 render 传入一个 Theme，由它创建两类产品，调用方只依赖产品接口。
- **权衡:** 新增 Slider 这样的产品类型时，每个工厂都要修改。接口本身也无法保证实现真的保持视觉一致。
- **记忆提示:** 一个工厂，一套产品。

[类别](../README.zh-CN.md) · [下一个](../../creational/builder/README.zh-CN.md)
