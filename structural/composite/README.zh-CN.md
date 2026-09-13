# Composite

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/bridge/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/decorator/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — 关注 object 与 class 如何组织在一起的 Design Pattern。

## Difficulty

入门

## In One Sentence

让单个叶子和 object 树提供同一种操作。

## 简单理解

文件夹中可以有文件和其他文件夹。Composite 让两者都提供 `bytes`，调用方无需自己处理每一层嵌套。

## The Problem

文件浏览器要计算文件或嵌套文件夹的大小。

## Naive Solution

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## Why It Becomes a Problem

按深度分别写循环无法应对继续嵌套，还会重复判断文件和目录。

## The Idea

File 和 Folder 都实现 Entry，文件夹递归地请求各子节点的大小。

## Real-World Analogy

运输箱既能装包裹，也能装小箱子；每一层都按同样规则计算重量。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Composite](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## Participants

Entry 定义 bytes；File 返回自身大小；Folder 用 [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) 拥有子节点并汇总结果。

本例中的标准角色：

- [`Component`](../../GLOSSARY.md#component) — 叶子、分组或包装层共同提供的约定。 对应代码： `Entry`。
- [`Leaf`](../../GLOSSARY.md#leaf) — 不含子 Component 的 Component。 对应代码： `File`。
- [`ownership`](../../GLOSSARY.md#ownership) — 负责维持资源存活并最终释放资源的责任。 对应代码： `Folder::children_`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>
#include <vector>

struct Entry {
    virtual ~Entry() = default;
    virtual int bytes() const = 0;
};
class File final : public Entry {
    int size_;
public:
    explicit File(int size) : size_(size) {
        if (size < 0) throw std::invalid_argument("Negative size");
    }
    int bytes() const override { return size_; }
};
class Folder final : public Entry {
    std::vector<std::unique_ptr<Entry>> children_;
public:
    void add(std::unique_ptr<Entry> child) {
        if (!child) throw std::invalid_argument("Null child");
        children_.push_back(std::move(child));
    }
    int bytes() const override {
        int total = 0;
        for (const auto& child : children_) total += child->bytes();
        return total;
    }
};
int main() {
    auto images = std::make_unique<Folder>();
    images->add(std::make_unique<File>(20));
    Folder root;
    root.add(std::make_unique<File>(10));
    root.add(std::move(images));
    std::cout << "Total: " << root.bytes() << " bytes\n";
    std::cout << "Empty: " << Folder{}.bytes() << " bytes\n";
    try { const File invalid{-1}; }
    catch (const std::invalid_argument&) { std::cout << "Negative size rejected\n"; }
}
```

## Example Output

```text
Total: 30 bytes
Empty: 0 bytes
Negative size rejected
```

## When to Use

适合真正的部分—整体树，且叶子与分组都有共同的有效操作。

### Use cases

适合文件树、无节点共享的场景树和菜单层次。

## When NOT to Use

平面列表或带共享父节点、环的图，不宜硬套树形 ownership。

## Advantages

Client 无需知道深度和具体结构，就能计算子树总量。

## Trade-offs

极深的树可能耗尽栈，整数求和可能溢出；不要强迫叶子支持仅分组才有的操作。

## Related Patterns

[Decorator](../decorator/README.zh-CN.md) · [Iterator](../../behavioral/iterator/README.zh-CN.md)

## Common Confusion

Decorator 包装一个 object 以增加 behavior；Composite 通常包含多个子节点来表示整体，两者都可能 递归地依赖共同 [`interface`](../../GLOSSARY.md#interface)。

## Terms to Remember

- `Composite` — 让单个叶子和 object 树提供同一种操作。
- `Component` — 叶子、分组或包装层共同提供的约定。 示例： `Entry`。
- `Leaf` — 不含子 Component 的 Component。 示例： `File`。
- `ownership` — 负责维持资源存活并最终释放资源的责任。 示例： `Folder::children_`。

## Interview Vocabulary

- [`part-whole hierarchy`](../../GLOSSARY.md#part-whole-hierarchy) — 分组包含叶子或更小分组的递归结构。
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — 由提供与整体相同约定的部分递归构建结构。
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — 同一 interface 对应不同 implementation；C++ 同时支持 runtime 与 compile time 的形式。

## Interview Question

为什么 add 放在 Folder 而不是 Entry？给文件加子节点意味着什么？

## Mini Challenge

增加空目录和更深一层目录，验证总量，并考虑更宽的大小 type。

## 检查理解

1. 为什么空 Folder 能通过与 File 相同的 Interface 返回零？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 文件浏览器要计算文件或嵌套文件夹的大小。
- **方案:** File 和 Folder 都实现 Entry，文件夹递归地请求各子节点的大小。
- **权衡:** 极深的树可能耗尽栈，整数求和可能溢出；不要强迫叶子支持仅分组才有的操作。
- **记忆提示:** 整体像单项一样回答。

[上一个](../../structural/bridge/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/decorator/README.zh-CN.md)
