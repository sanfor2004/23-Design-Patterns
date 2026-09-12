# 享元

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/facade/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/proxy/README.zh-CN.md)

## 类别

结构型

## 难度

进阶

## 一句话说明

共享不可变的内部数据，把每次使用的上下文留在外部。

## 问题

文档里大量字符重复，为每个位置保存完整轮廓会浪费内存。

## 最初的简单方案

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## 为什么难以维护

逐次复制形状，使内存随出现次数增长，而不是随不同形状数量增长。

## 核心思路

GlyphPool 按字符复用 Glyph，PlacedGlyph 共享 const Glyph 并独立保存 x 坐标。

## 生活类比

多人共用一本参考书，但各自保留书签。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![享元](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## 参与者

Glyph 保存内在形状，GlyphPool 负责驻留复用，PlacedGlyph 保存外在位置和共享所有权。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Glyph {
    const std::string shape;
    explicit Glyph(std::string value) : shape(std::move(value)) {}
};
class GlyphPool {
    std::map<char, std::shared_ptr<const Glyph>> glyphs_;
public:
    std::shared_ptr<const Glyph> get(char symbol) {
        auto& glyph = glyphs_[symbol];
        if (!glyph) glyph = std::make_shared<const Glyph>(std::string(1, symbol));
        return glyph;
    }
};
struct PlacedGlyph {
    std::shared_ptr<const Glyph> glyph;
    int x;
    void draw() const { std::cout << glyph->shape << " at " << x << '\n'; }
};
int main() {
    GlyphPool pool;
    const PlacedGlyph first{pool.get('A'), 0};
    const PlacedGlyph second{pool.get('A'), 10};
    first.draw();
    second.draw();
    std::cout << "Shared shape: " << std::boolalpha << (first.glyph == second.glyph) << '\n';
}
```

## 预期输出

```text
A at 0
A at 10
Shared shape: true
```

## 何时使用

测量确认大量对象重复持有不可变数据时使用。

## 何时不该使用

数据量很小、每个实例的数据都可变，或查找成本超过收益时避免。

## 优点

重复出现的字符共享形状，位置保持独立。

## 缺点与权衡

池会保留条目，map 查找和 shared_ptr 有成本。示例字符串很小，不声称已有内存收益测量；池也未同步。

## 技术应用场景

字形轮廓、地形定义、驻留标识符都可在性能分析后考虑。

## 相关模式

[composite](../composite/README.zh-CN.md) · [prototype](../../creational/prototype/README.zh-CN.md)

## 常见混淆

原型复制配置生成新对象；享元有意让多个使用位置共享内部状态。

## 面试问题

若字体和字号影响形状，缓存键应该包含哪些字段？

## 小练习

给键增加字体标识，验证相同键共享、不同字体不共享。

## 小结

- **问题:** 文档里大量字符重复，为每个位置保存完整轮廓会浪费内存。
- **方案:** GlyphPool 按字符复用 Glyph，PlacedGlyph 共享 const Glyph 并独立保存 x 坐标。
- **权衡:** 池会保留条目，map 查找和 shared_ptr 有成本。示例字符串很小，不声称已有内存收益测量；池也未同步。
- **记忆提示:** 共享形状，位置随身带。

[上一个](../../structural/facade/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/proxy/README.zh-CN.md)
