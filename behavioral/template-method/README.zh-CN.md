# 模板方法

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/strategy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/visitor/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

固定算法流程，让子类实现部分步骤。

## 问题

报告共享开始、读取、格式化、结束步骤，但数据来源或格式不同。

## 最初的简单方案

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## 为什么难以维护

分别编写完整报告函数会重复顺序，共同步骤变化后容易各自偏离。

## 核心思路

非虚的 Report::generate 按固定顺序调用受保护的虚钩子 read、format。

## 生活类比

食谱固定制作顺序，但允许选择不同馅料。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![模板方法](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## 参与者

Report 定义算法骨架，TextReport 实现变化点，调用方通过 generate 使用公共流程。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Report {
protected:
    virtual std::string read() const = 0;
    virtual void format(std::string_view data) const = 0;
public:
    virtual ~Report() = default;
    void generate() const {
        std::cout << "Begin report\n";
        const auto data = read();
        format(data);
        std::cout << "End report\n";
    }
};
class TextReport final : public Report {
    std::string read() const override { return "sales=42"; }
    void format(std::string_view data) const override { std::cout << data << '\n'; }
};
int main() { TextReport{}.generate(); }
```

## 预期输出

```text
Begin report
sales=42
End report
```

## 何时使用

稳定流程中有少量明确的子类扩展点时使用。

## 何时不该使用

步骤需要运行时重排，或组合更能清楚表达依赖时避免。

## 优点

公共顺序留在基类，子类只实现差异。

## 缺点与权衡

继承让子类耦合到基类协议。read 或 format 抛出异常时不会保证 End；资源清理应使用 RAII，不能把最后一步当析构保障。

## 技术应用场景

适合骨架稳定的导入流程和报告生成。

## 相关模式

[strategy](../strategy/README.zh-CN.md) · [factory-method](../../creational/factory-method/README.zh-CN.md)

## 常见混淆

策略注入可替换行为，模板方法依赖继承钩子；工厂方法可以成为其中一个创建步骤。

## 面试问题

为什么 generate 非虚而 read、format 为虚？表达了哪些不变量？

## 小练习

添加 CsvReport 验证首尾顺序，再模拟格式化异常并讨论清理。

## 小结

- **问题:** 报告共享开始、读取、格式化、结束步骤，但数据来源或格式不同。
- **方案:** 非虚的 Report::generate 按固定顺序调用受保护的虚钩子 read、format。
- **权衡:** 继承让子类耦合到基类协议。read 或 format 抛出异常时不会保证 End；资源清理应使用 RAII，不能把最后一步当析构保障。
- **记忆提示:** 流程固定，步骤可变。

[上一个](../../behavioral/strategy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/visitor/README.zh-CN.md)
