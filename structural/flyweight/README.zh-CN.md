# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/facade/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/proxy/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — 关注 object 与 class 如何组织在一起的 Design Pattern。

## Difficulty

进阶

## In One Sentence

共享不可变的 intrinsic state，把每次使用的 extrinsic state 留在共享 object 外部。

## 简单理解

同一个字母可能在文档中出现数千次。Flyweight 只保存一份共用字形，每次出现的位置单独保存。

## The Problem

文档里大量字符重复，为每个位置保存完整轮廓会浪费内存。

## Naive Solution

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Why It Becomes a Problem

逐次复制形状，使内存随出现次数增长，而不是随不同形状数量增长。

## The Idea

GlyphPool 按字符复用 Glyph，PlacedGlyph 共享 const Glyph 并独立保存 x 坐标。

## Real-World Analogy

多人共用一本参考书，但各自保留书签。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Flyweight](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## Participants

Glyph 保存内在形状，GlyphPool 负责驻留复用，PlacedGlyph 保存外在位置和 shared [`ownership`](../../GLOSSARY.md#ownership)。

本例中的标准角色：

- [`intrinsic state`](../../GLOSSARY.md#intrinsic-state) — 不依赖具体使用位置、可由 Flyweight 共享的数据。 对应代码： `Glyph::shape`。
- [`extrinsic state`](../../GLOSSARY.md#extrinsic-state) — 每次使用独有、保存在共享 Flyweight 外部的数据。 对应代码： `PlacedGlyph::x`。
- [`Flyweight Factory`](../../GLOSSARY.md#flyweight-factory) — 按键查找并返回共享 Flyweight 的服务。 对应代码： `GlyphPool`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

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

## Example Output

```text
A at 0
A at 10
Shared shape: true
```

## When to Use

测量确认大量 object 重复持有不可变数据时使用。

### Use cases

字形轮廓、地形定义、驻留标识符都可在性能分析后考虑。

## When NOT to Use

数据量很小、每个 instance 的数据都可变，或查找成本超过收益时避免。

## Advantages

重复出现的字符共享形状，位置保持独立。

## Trade-offs

池会保留条目，map 查找和 [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) 有成本。示例字符串很小，不声称已有内存收益测量；池也未同步。

## Related Patterns

[Composite](../composite/README.zh-CN.md) · [Prototype](../../creational/prototype/README.zh-CN.md)

## Common Confusion

Prototype 复制配置生成新 object； Flyweight 有意让多个使用位置共享内部 state。

## Terms to Remember

- `Flyweight` — 共享不可变的 intrinsic state，把每次使用的 extrinsic state 留在共享 object 外部。
- `intrinsic state` — 不依赖具体使用位置、可由 Flyweight 共享的数据。 示例： `Glyph::shape`。
- `extrinsic state` — 每次使用独有、保存在共享 Flyweight 外部的数据。 示例： `PlacedGlyph::x`。
- `Flyweight Factory` — 按键查找并返回共享 Flyweight 的服务。 示例： `GlyphPool`。

## Interview Vocabulary

- [`interning`](../../GLOSSARY.md#interning) — 通过查找池为等价值复用同一个表示。
- [`ownership`](../../GLOSSARY.md#ownership) — 负责维持资源存活并最终释放资源的责任。
- [`memory allocation`](../../GLOSSARY.md#memory-allocation) — 为数据取得存储空间，其成本和失败方式取决于所用机制。

## Interview Question

若字体和字号影响形状，缓存键应该包含哪些字段？

## Mini Challenge

给键增加字体标识，验证相同键共享、不同字体不共享。

## 检查理解

1. 哪些数据必须放在共享 Glyph 之外？为什么？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 文档里大量字符重复，为每个位置保存完整轮廓会浪费内存。
- **方案:** GlyphPool 按字符复用 Glyph，PlacedGlyph 共享 const Glyph 并独立保存 x 坐标。
- **权衡:** 池会保留条目，map 查找和 std::shared_ptr 有成本。示例字符串很小，不声称已有内存收益测量；池也未同步。
- **记忆提示:** 共享形状，位置随身带。

[上一个](../../structural/facade/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/proxy/README.zh-CN.md)
