# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/interpreter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/mediator/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

入门

## In One Sentence

通过稳定的访问协议遍历集合。

## 简单理解

调用方只需要逐个读取曲目，不需要了解播放列表内部的容器。Iterator 单独记录遍历位置，让循环取得下一个元素。

## The Problem

Client 需要读取播放列表，不应接触 private 存储。

## Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why It Becomes a Problem

对 public std::vector 使用索引，会暴露实现并分散边界处理。

## The Idea

提供 begin、end 以及支持 dereference、递增和相等比较的 iterator。

## Real-World Analogy

按博物馆路线逐个参观展品，不必知道内部房间数据库。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Participants

Playlist 拥有曲目；Iterator 借用向量并保存位置；范围 for 是 Client。static_assert 检查 C++20 forward_iterator 概念。

本例中的标准角色：

- [`Aggregate`](../../GLOSSARY.md#aggregate) — 提供 iterator 访问能力的集合。 对应代码： `Playlist`。
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — 为某种 Aggregate 保存遍历位置的 implementation。 对应代码： `Playlist::Iterator`。
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — 支持向前遍历与 multipass 保证的 iterator，独立副本可以遍历同一范围。 对应代码： `std::forward_iterator`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <cstddef>
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

class Playlist {
    std::vector<int> tracks_;
public:
    explicit Playlist(std::vector<int> tracks) : tracks_(std::move(tracks)) {}
    class Iterator {
        const std::vector<int>* tracks_ = nullptr;
        std::size_t index_ = 0;
    public:
        using value_type = int;
        using difference_type = std::ptrdiff_t;
        using iterator_concept = std::forward_iterator_tag;
        Iterator() = default;
        Iterator(const std::vector<int>& tracks, std::size_t index) : tracks_(&tracks), index_(index) {}
        const int& operator*() const { return (*tracks_)[index_]; }
        Iterator& operator++() { ++index_; return *this; }
        Iterator operator++(int) { auto old = *this; ++*this; return old; }
        bool operator==(const Iterator&) const = default;
    };
    Iterator begin() const { return Iterator{tracks_, 0}; }
    Iterator end() const { return Iterator{tracks_, tracks_.size()}; }
};
static_assert(std::forward_iterator<Playlist::Iterator>);
int main() {
    const Playlist playlist{{7, 12, 18}};
    for (int track : playlist) std::cout << "Track " << track << '\n';
    const Playlist empty{{}};
    std::cout << "Empty: " << std::boolalpha << (empty.begin() == empty.end()) << '\n';
    auto first = playlist.begin();
    const auto copy = first;
    ++first;
    std::cout << "Independent positions: " << *first << ' ' << *copy << '\n';
}
```

## Example Output

```text
Track 7
Track 12
Track 18
Empty: true
Independent positions: 12 7
```

## When to Use

优先用标准 iterator 或 ranges 暴露遍历能力而非存储细节。

### Use cases

适合 container 遍历和树遍历； iterator 类别必须符合实际操作与复杂度。

## When NOT to Use

直接返回已有 const_iterator 或标准范围即可时，不必自定义；这里用于教学。

## Advantages

algorithm 使用统一协议，多份 iterator 拥有独立位置。

## Trade-offs

iterator 不延长集合 [`lifetime`](../../GLOSSARY.md#lifetime)。移动或销毁 Playlist 会破坏使用前提；和标准 iterator 一样，不能 dereference end。

## Related Patterns

[Composite](../../structural/composite/README.zh-CN.md) · [Visitor](../visitor/README.zh-CN.md)

## Common Confusion

Visitor 按 Element type 选择操作， iterator 负责遍历，不必知道 Client 如何处理元素。

## Terms to Remember

- `Iterator` — 通过稳定的访问协议遍历集合。
- `Aggregate` — 提供 iterator 访问能力的集合。 示例： `Playlist`。
- `Concrete Iterator` — 为某种 Aggregate 保存遍历位置的 implementation。 示例： `Playlist::Iterator`。
- `forward iterator` — 支持向前遍历与 multipass 保证的 iterator，独立副本可以遍历同一范围。 示例： `std::forward_iterator`。

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — 把内部表示和必须保持的规则放在受控操作之后。
- [`iterator invalidation`](../../GLOSSARY.md#iterator-invalidation) — 某个操作导致 iterator 不再适合原本的使用方式。
- [`generic programming`](../../GLOSSARY.md#generic-programming) — 根据类型需要满足的要求编写 algorithm，而不是绑定一个具体类型。

## Interview Question

相等比较为什么还要检查向量 pointer，而不只比较索引？

## Mini Challenge

测试空列表和两个独立 iterator，验证移动一个不会改变另一个。

## 检查理解

1. 同一 Playlist 上的两次遍历能保留各自的位置吗？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** Client 需要读取播放列表，不应接触 private 存储。
- **方案:** 提供 begin、end 以及支持 dereference、递增和相等比较的 iterator。
- **权衡:** iterator 不延长集合 lifetime。移动或销毁 Playlist 会破坏使用前提；和标准 iterator 一样，不能 dereference end。
- **记忆提示:** 遍历数据，不暴露 container 内部。

[上一个](../../behavioral/interpreter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/mediator/README.zh-CN.md)
