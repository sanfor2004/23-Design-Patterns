# 迭代器

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/interpreter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/mediator/README.zh-CN.md)

## 类别

行为型

## 难度

入门

## 一句话说明

通过稳定的访问协议遍历集合。

## 问题

调用方需要读取播放列表，不应接触私有存储。

## 最初的简单方案

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## 为什么难以维护

对公开 vector 使用索引，会暴露实现并分散边界处理。

## 核心思路

提供 begin、end 以及支持解引用、递增和相等比较的迭代器。

## 生活类比

按博物馆路线逐个参观展品，不必知道内部房间数据库。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![迭代器](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## 参与者

Playlist 拥有曲目；Iterator 借用向量并保存位置；范围 for 是调用方。static_assert 检查 C++20 forward_iterator 概念。

## 现代 C++20 完整可运行示例

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
}
```

## 预期输出

```text
Track 7
Track 12
Track 18
```

## 何时使用

优先用标准迭代器或 ranges 暴露遍历能力而非存储细节。

## 何时不该使用

直接返回已有 const_iterator 或标准范围即可时，不必自定义；这里用于教学。

## 优点

算法使用统一协议，多份迭代器拥有独立位置。

## 缺点与权衡

迭代器不延长集合寿命。移动或销毁 Playlist 会破坏使用前提；和标准迭代器一样，不能解引用 end。

## 技术应用场景

适合容器遍历和树遍历；迭代器类别必须符合实际操作与复杂度。

## 相关模式

[composite](../../structural/composite/README.zh-CN.md) · [visitor](../visitor/README.zh-CN.md)

## 常见混淆

访问者按元素类型选择操作，迭代器负责遍历，不必知道调用方如何处理元素。

## 面试问题

相等比较为什么还要检查向量指针，而不只比较索引？

## 小练习

测试空列表和两个独立迭代器，验证移动一个不会改变另一个。

## 小结

- **问题:** 调用方需要读取播放列表，不应接触私有存储。
- **方案:** 提供 begin、end 以及支持解引用、递增和相等比较的迭代器。
- **权衡:** 迭代器不延长集合寿命。移动或销毁 Playlist 会破坏使用前提；和标准迭代器一样，不能解引用 end。
- **记忆提示:** 遍历数据，不暴露容器内部。

[上一个](../../behavioral/interpreter/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/mediator/README.zh-CN.md)
