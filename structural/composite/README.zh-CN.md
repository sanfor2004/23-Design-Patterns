# 组合

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/bridge/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/decorator/README.zh-CN.md)

## 类别

结构型

## 难度

入门

## 一句话说明

让单个叶子和对象树提供同一种操作。

## 问题

文件浏览器要计算文件或嵌套文件夹的大小。

## 最初的简单方案

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## 为什么难以维护

按深度分别写循环无法应对继续嵌套，还会重复判断文件和目录。

## 核心思路

File 和 Folder 都实现 Entry，文件夹递归请求各子节点的大小。

## 生活类比

运输箱既能装包裹，也能装小箱子；每一层都按同样规则计算重量。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![组合](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## 参与者

Entry 定义 bytes；File 返回自身大小；Folder 用 unique_ptr 拥有子节点并汇总结果。

## 现代 C++20 完整可运行示例

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
}
```

## 预期输出

```text
Total: 30 bytes
```

## 何时使用

适合真正的部分—整体树，且叶子与分组都有共同的有效操作。

## 何时不该使用

平面列表或带共享父节点、环的图，不宜硬套树形所有权。

## 优点

调用方无需知道深度和具体结构，就能计算子树总量。

## 缺点与权衡

极深的树可能耗尽栈，整数求和可能溢出；不要强迫叶子支持仅分组才有的操作。

## 技术应用场景

适合文件树、无节点共享的场景树和菜单层次。

## 相关模式

[decorator](../decorator/README.zh-CN.md) · [iterator](../../behavioral/iterator/README.zh-CN.md)

## 常见混淆

装饰器包装一个对象以增加行为；组合通常包含多个子节点来表示整体，两者都可能递归依赖共同接口。

## 面试问题

为什么 add 放在 Folder 而不是 Entry？给文件加子节点意味着什么？

## 小练习

增加空目录和更深一层目录，验证总量，并考虑更宽的大小类型。

## 小结

- **问题:** 文件浏览器要计算文件或嵌套文件夹的大小。
- **方案:** File 和 Folder 都实现 Entry，文件夹递归请求各子节点的大小。
- **权衡:** 极深的树可能耗尽栈，整数求和可能溢出；不要强迫叶子支持仅分组才有的操作。
- **记忆提示:** 整体像单项一样回答。

[上一个](../../structural/bridge/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/decorator/README.zh-CN.md)
