# Template Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/strategy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/visitor/README.zh-CN.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

固定 algorithm 流程，让 subclass 实现部分步骤。

## The Problem

报告共享开始、读取、格式化、结束步骤，但数据来源或格式不同。

## Naive Solution

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## Why It Becomes a Problem

分别编写完整报告 function 会重复顺序，共同步骤变化后容易各自偏离。

## The Idea

nonvirtual 的 Report::generate 按固定顺序调用 protected 的 virtual hook methods read、format。

## Real-World Analogy

食谱固定制作顺序，但允许选择不同馅料。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Template Method](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## Participants

Report 定义 algorithm skeleton，TextReport 实现变化点， Client 通过 generate 使用公共流程。

本例中的标准角色：

- [`Abstract Class`](../../GLOSSARY.md#abstract-class-template-method-role) — Template Method 中拥有 algorithm skeleton 并声明可变步骤的角色。 对应代码： `Report`。
- [`Concrete Class`](../../GLOSSARY.md#concrete-class-template-method-role) — Template Method 中提供可变步骤的角色。 对应代码： `TextReport`。
- [`hook method`](../../GLOSSARY.md#hook-method) — 由固定流程调用的扩展操作，可以有默认 implementation。 对应代码： `read, format`。

## Modern C++20 Example

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

## Example Output

```text
Begin report
sales=42
End report
```

## When to Use

稳定流程中有少量明确的 subclass 扩展点时使用。

### Use cases

适合骨架稳定的导入流程和报告生成。

## When NOT to Use

步骤需要 [`runtime`](../../GLOSSARY.md#runtime)（编译后的程序正在执行的阶段） 重排，或 [`composition`](../../GLOSSARY.md#composition)（通过连接使用或包含其他 object 的 object 来组合行为） 更能清楚表达 dependency 时避免。

## Advantages

公共顺序留在 base class， subclass 只实现差异。

## Trade-offs

[`inheritance`](../../GLOSSARY.md#inheritance)（从 base class 定义 derived class，复用或扩展约定及实现） 让 subclass 与 base class 协议产生 [`coupling`](../../GLOSSARY.md#coupling)（一个部分的修改需要了解或修改另一部分的程度）。read 或 format 抛出 exception 时不会保证 End；资源清理应使用 [`RAII`](../../GLOSSARY.md#raii)（Resource Acquisition Is Initialization：把资源 ownership 绑定到 object lifetime，在析构时释放资源），不能把最后一步 当 destructor 的保障。

## Related Patterns

[Strategy](../strategy/README.zh-CN.md) · [Factory Method](../../creational/factory-method/README.zh-CN.md)

## Common Confusion

Strategy 注入可替换 behavior， Template Method 依赖 inheritance 钩子； Factory Method 可以成为其中一个创建步骤。

## Terms to Remember

- `Template Method` — 固定 algorithm 流程，让 subclass 实现部分步骤。
- `Abstract Class` — Template Method 中拥有 algorithm skeleton 并声明可变步骤的角色。 示例： `Report`。
- `Concrete Class` — Template Method 中提供可变步骤的角色。 示例： `TextReport`。
- `hook method` — 由固定流程调用的扩展操作，可以有默认 implementation。 示例： `read, format`。

## Interview Vocabulary

- [`algorithm skeleton`](../../GLOSSARY.md#algorithm-skeleton) — 某些步骤可以变化、整体顺序保持固定的 algorithm 框架。
- [`inheritance`](../../GLOSSARY.md#inheritance) — 从 base class 定义 derived class，复用或扩展约定及实现。
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — 在选定的有效边界上追求 open for extension, closed for modification。

## Interview Question

为什么 generate nonvirtual 而 read、format 为 virtual？表达了哪些 invariant？

## Mini Challenge

添加 CsvReport 验证首尾顺序，再模拟格式化 exception 并讨论清理。

## Quick Summary

- **问题:** 报告共享开始、读取、格式化、结束步骤，但数据来源或格式不同。
- **方案:** nonvirtual 的 Report::generate 按固定顺序调用 protected 的 virtual hook methods read、format。
- **权衡:** inheritance 让 subclass 与 base class 协议产生 coupling。read 或 format 抛出 exception 时不会保证 End；资源清理应使用 RAII，不能把最后一步 当 destructor 的保障。
- **记忆提示:** 流程固定，步骤可变。

[上一个](../../behavioral/strategy/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/visitor/README.zh-CN.md)
