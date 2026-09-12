# 访问者

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/template-method/README.zh-CN.md) · [类别](../README.zh-CN.md)

## 类别

行为型

## 难度

进阶

## 一句话说明

通过独立访问者，为稳定的元素类型集合增加操作。

## 问题

购物篮包含书和食品，新增税费、导出等操作不应不断塞进每个元素类。

## 最初的简单方案

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## 为什么难以维护

每增加一个任务就给 Item 增加虚方法，会要求修改所有具体元素。

## 核心思路

具体 Item 在 accept 中调用匹配类型的 Visitor::visit 重载，Tax 为每种类型实现操作。

## 生活类比

检查员走访不同工位，按工位类型使用不同检查清单。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![访问者](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## 参与者

Item 定义 accept，Book 和 Food 选择类型重载，Visitor 列出支持类型，Tax 汇总结果，购物篮拥有元素。

## 现代 C++20 完整可运行示例

```cpp
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
    int price = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Food final : Item {
    int price = 10;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Tax final : Visitor {
    int total = 0;
    void visit(const Book& book) override { total += book.price / 10; }
    void visit(const Food& food) override { total += food.price / 5; }
};
int main() {
    std::vector<std::unique_ptr<Item>> basket;
    basket.push_back(std::make_unique<Book>());
    basket.push_back(std::make_unique<Food>());
    Tax tax;
    for (const auto& item : basket) item->accept(tax);
    std::cout << "Tax: " << tax.total << '\n';
}
```

## 预期输出

```text
Tax: 4
```

## 何时使用

元素类型稳定，而新操作频繁增加时使用。

## 何时不该使用

元素类型经常增加，或暴露内部细节会破坏封装时避免。

## 优点

增加访问者即可增加操作，不必修改现有元素类。

## 缺点与权衡

新增元素类型要修改 Visitor 接口和所有访问者。整数税率仅供演示，不代表真实税法，舍入需要领域规则。

## 技术应用场景

适合稳定节点族上的 AST 分析和文档导出；封闭类型集合也可考虑 std::variant 与 std::visit。

## 相关模式

[composite](../../structural/composite/README.zh-CN.md) · [iterator](../iterator/README.zh-CN.md)

## 常见混淆

迭代器负责遍历，访问者按元素类型分派操作，组合可提供被访问的树。

## 面试问题

为什么 Book 内的 visitor.visit(*this) 会选择 Book 重载，而单独的 Item 引用不行？

## 小练习

不修改 Book 和 Food，添加 Label 访问者；再添加第三种元素，统计修改范围。

## 小结

- **问题:** 购物篮包含书和食品，新增税费、导出等操作不应不断塞进每个元素类。
- **方案:** 具体 Item 在 accept 中调用匹配类型的 Visitor::visit 重载，Tax 为每种类型实现操作。
- **权衡:** 新增元素类型要修改 Visitor 接口和所有访问者。整数税率仅供演示，不代表真实税法，舍入需要领域规则。
- **记忆提示:** 类型稳定，操作扩展。

[上一个](../../behavioral/template-method/README.zh-CN.md) · [类别](../README.zh-CN.md)
