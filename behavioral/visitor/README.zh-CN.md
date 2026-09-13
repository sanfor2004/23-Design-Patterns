# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/template-method/README.zh-CN.md) · [类别](../README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

进阶

## In One Sentence

通过独立 Visitor，为稳定的 Element type 集合增加操作。

## 简单理解

图书和食品需要不同的税额计算。Visitor 把这些计算放在一起，每个元素调用对应自身类型的方法。

## The Problem

购物篮包含书和食品，新增税费、导出等操作不应不断塞进每个 Element class。

## Naive Solution

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## Why It Becomes a Problem

每增加一个任务就给 Item 增加 virtual method，会要求修改所有具体元素。

## The Idea

具体 Item 在 accept 中调用匹配 type 的 Visitor::visit 重载，Tax 为每种 type 实现操作。

## Real-World Analogy

检查员走访不同工位，按工位类型使用不同检查清单。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## Participants

Item 定义 accept，Book 和 Food 选择 type 重载，Visitor 列出支持 type，Tax 汇总结果，购物篮拥有元素。

本例中的标准角色：

- [`Element`](../../GLOSSARY.md#element) — 接受 Visitor 的 object 所提供的约定。 对应代码： `Item`。
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — 选择与自身类型匹配的 Visitor overload 的 Element implementation。 对应代码： `Book, Food`。
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — 为每种受支持的 Element 类型提供操作的 Visitor implementation。 对应代码： `Tax`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <vector>

struct Book;
struct Food;
struct Visitor {
    virtual ~Visitor() = default;
    virtual void visit(const Book& book) = 0;
    virtual void visit(const Food& food) = 0;
};
struct Item {
    virtual ~Item() = default;
    virtual void accept(Visitor& visitor) const = 0;
};
struct Book final : Item {
    int price_cents = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Food final : Item {
    int price_cents = 10;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Tax final : Visitor {
    int total_cents = 0;
    void visit(const Book& book) override { total_cents += book.price_cents / 10; }
    void visit(const Food& food) override { total_cents += food.price_cents / 5; }
};
int main() {
    std::vector<std::unique_ptr<Item>> basket;
    basket.push_back(std::make_unique<Book>());
    basket.push_back(std::make_unique<Food>());
    Tax tax;
    for (const auto& item : basket) item->accept(tax);
    std::cout << "Tax: " << tax.total_cents << '\n';
}
```

## Example Output

```text
Tax: 4
```

## When to Use

Element type 稳定，而新操作频繁增加时使用。

### Use cases

适合稳定节点族上的 AST 分析和文档导出；封闭 type 集合也可考虑 std::variant 与 std::visit。

## When NOT to Use

Element type 经常增加，或暴露内部细节会破坏 [`encapsulation`](../../GLOSSARY.md#encapsulation) 时避免。

## Advantages

增加 Visitor 即可增加操作，不必修改现有 Element class。

## Trade-offs

新增 Element type 要修改 Visitor [`interface`](../../GLOSSARY.md#interface) 和所有 Visitor。整数税率仅供演示，不代表真实税法，舍入需要领域规则。

## Related Patterns

[Composite](../../structural/composite/README.zh-CN.md) · [Iterator](../iterator/README.zh-CN.md)

## Common Confusion

iterator 负责遍历， Visitor 按 Element type 分派操作，Composite 可提供被访问的树。

## Terms to Remember

- `Visitor` — 通过独立 Visitor，为稳定的 Element type 集合增加操作。
- `Element` — 接受 Visitor 的 object 所提供的约定。 示例： `Item`。
- `Concrete Element` — 选择与自身类型匹配的 Visitor overload 的 Element implementation。 示例： `Book, Food`。
- `Concrete Visitor` — 为每种受支持的 Element 类型提供操作的 Visitor implementation。 示例： `Tax`。

## Interview Vocabulary

- [`double dispatch`](../../GLOSSARY.md#double-dispatch) — 依据两个 runtime 类型选择 behavior；经典 Visitor 结合两次 virtual 调用与 overload resolution。
- [`overload resolution`](../../GLOSSARY.md#overload-resolution) — 在 compile time 根据参数类型，从同名 function 中选择匹配项。
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — 在选定的有效边界上追求 open for extension, closed for modification。

## Interview Question

为什么 Book 内的 visitor.visit(*this) 会选择 Book 重载，而单独的 Item reference 不行？

## Mini Challenge

不修改 Book 和 Food，添加 Label Visitor；再添加第三种元素，统计修改范围。

## 检查理解

1. 增加元素类型与增加操作时，需要修改的地方有何不同？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 购物篮包含书和食品，新增税费、导出等操作不应不断塞进每个 Element class。
- **方案:** 具体 Item 在 accept 中调用匹配 type 的 Visitor::visit 重载，Tax 为每种 type 实现操作。
- **权衡:** 新增 Element type 要修改 Visitor interface 和所有 Visitor。整数税率仅供演示，不代表真实税法，舍入需要领域规则。
- **记忆提示:** type 稳定，操作扩展。

[上一个](../../behavioral/template-method/README.zh-CN.md) · [类别](../README.zh-CN.md)
