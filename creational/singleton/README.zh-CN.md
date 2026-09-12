# 单例

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/prototype/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/adapter/README.zh-CN.md)

## 类别

创建型

## 难度

中级

## 一句话说明

限制类型只提供一个实例，同时承担全局共享状态的代价。

## 问题

分别创建的两个指标计数器把本应属于整个进程的总数拆开了。

## 最初的简单方案

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## 为什么难以维护

公开构造函数让每个调用方创建自己的计数器，原本需要共享的总数不再共享。

## 核心思路

隐藏构造，禁止复制，通过函数内的局部静态对象返回唯一实例。

## 生活类比

小办公室只放一本访客登记簿，各前台都写同一本。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![单例](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## 参与者

Metrics 管理自身生命周期并保存计数；instance 返回非拥有引用，调用方不能删除它。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>

class Metrics {
    int requests_ = 0;
    Metrics() = default;
public:
    Metrics(const Metrics&) = delete;
    Metrics& operator=(const Metrics&) = delete;
    static Metrics& instance() {
        static Metrics metrics;
        return metrics;
    }
    void record() { ++requests_; }
    int requests() const { return requests_; }
};
int main() {
    auto& first = Metrics::instance();
    auto& second = Metrics::instance();
    first.record();
    second.record();
    std::cout << "Same instance: " << std::boolalpha << (&first == &second) << '\n';
    std::cout << "Requests: " << first.requests() << '\n';
}
```

## 预期输出

```text
Same instance: true
Requests: 2
```

## 何时使用

只有唯一实例确实是进程级约束，且生命周期合适时才考虑。

## 何时不该使用

不要为了访问方便而使用；需要隔离测试的普通依赖应显式传入引用。

## 优点

初始化入口明确，所有调用方访问同一个对象。

## 缺点与权衡

全局访问隐藏依赖并干扰测试。局部静态初始化是线程安全的，但 record 不是；并发修改需要同步，退出时的析构顺序也可能有影响。

## 技术应用场景

这个单线程诊断计数器只演示机制，不是生产指标系统的架构建议。

## 相关模式

[abstract-factory](../abstract-factory/README.zh-CN.md) · [facade](../../structural/facade/README.zh-CN.md)

## 常见混淆

依赖注入管理一个实例不等于单例模式：唯一性不一定由类型强制。

## 面试问题

初始化线程安全是否代表 requests_ 的修改也安全？区分这两个过程。

## 小练习

改成给两个任务注入计数器，再测试两个互不影响的计数器。

## 小结

- **问题:** 分别创建的两个指标计数器把本应属于整个进程的总数拆开了。
- **方案:** 隐藏构造，禁止复制，通过函数内的局部静态对象返回唯一实例。
- **权衡:** 全局访问隐藏依赖并干扰测试。局部静态初始化是线程安全的，但 record 不是；并发修改需要同步，退出时的析构顺序也可能有影响。
- **记忆提示:** 实例唯一，问题未必少。

[上一个](../../creational/prototype/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/adapter/README.zh-CN.md)
