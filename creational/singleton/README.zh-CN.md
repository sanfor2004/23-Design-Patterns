# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/prototype/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/adapter/README.zh-CN.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — 关注如何创建和配置 object 的 Design Pattern。

## Difficulty

中级

## In One Sentence

限制 type 只提供一个 instance，同时承担全局共享 state 的代价。

## The Problem

分别创建的两个指标计数器把本应属于整个进程的总数拆开了。

## Naive Solution

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Why It Becomes a Problem

public constructor 让每个 Client 创建自己的计数器，原本需要共享的总数不再共享。

## The Idea

隐藏构造，禁止复制，通过 function 内的 local static object 返回唯一 instance。

## Real-World Analogy

小办公室只放一本访客登记簿，各前台都写同一本。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Singleton](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## Participants

Metrics 管理自身 [`lifetime`](../../GLOSSARY.md#lifetime)（object 存在且可按规则使用的时间区间） 并保存计数；instance 返回 non-owning reference， Client 不能删除它。

本例中的标准角色：

- [`instance`](../../GLOSSARY.md#instance) — 某个类型的一个具体 object。 对应代码： `Metrics::instance()`。
- [`global state`](../../GLOSSARY.md#global-state) — 程序中广泛可访问、修改后可能影响远处代码的数据。 对应代码： `Metrics::requests_`。
- [`thread-safe initialization`](../../GLOSSARY.md#thread-safe-initialization) — 避免并发重复构造的初始化保障，不代表后续操作也 thread-safe。 对应代码： `static Metrics metrics`。

## Modern C++20 Example

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

## Example Output

```text
Same instance: true
Requests: 2
```

## When to Use

只有唯一 instance 确实是进程级约束，且 lifetime 合适时才考虑。

### Use cases

这个单线程诊断计数器只演示机制，不是生产指标系统的架构建议。

## When NOT to Use

不要为了访问方便而使用；需要隔离测试的普通 dependency 应显式传入 reference。

## Advantages

初始化入口明确，所有 Client 访问同一个 object。

## Trade-offs

全局访问隐藏 dependency 并干扰测试。 local static 初始化是 thread-safe 的，但 record 不是；并发修改需要同步，退出时的析构顺序也可能有影响。

## Related Patterns

[Abstract Factory](../abstract-factory/README.zh-CN.md) · [Facade](../../structural/facade/README.zh-CN.md)

## Common Confusion

[`dependency injection`](../../GLOSSARY.md#dependency-injection)（从外部传入 dependency，而不是由使用方自行选择或创建） 管理一个 instance 不等于 Singleton：唯一性不一定由 type 强制。

## Terms to Remember

- `Singleton` — 限制 type 只提供一个 instance，同时承担全局共享 state 的代价。
- `instance` — 某个类型的一个具体 object。 示例： `Metrics::instance()`。
- `global state` — 程序中广泛可访问、修改后可能影响远处代码的数据。 示例： `Metrics::requests_`。
- `thread-safe initialization` — 避免并发重复构造的初始化保障，不代表后续操作也 thread-safe。 示例： `static Metrics metrics`。

## Interview Vocabulary

- [`dependency injection`](../../GLOSSARY.md#dependency-injection) — 从外部传入 dependency，而不是由使用方自行选择或创建。
- [`testability`](../../GLOSSARY.md#testability) — 隔离、执行并检查 behavior 的容易程度。
- [`lifetime`](../../GLOSSARY.md#lifetime) — object 存在且可按规则使用的时间区间。

## Interview Question

初始化 thread-safe 是否代表 requests_ 的修改也安全？区分这两个过程。

## Mini Challenge

改成给两个任务注入计数器，再测试两个互不影响的计数器。

## Quick Summary

- **问题:** 分别创建的两个指标计数器把本应属于整个进程的总数拆开了。
- **方案:** 隐藏构造，禁止复制，通过 function 内的 local static object 返回唯一 instance。
- **权衡:** 全局访问隐藏 dependency 并干扰测试。 local static 初始化是 thread-safe 的，但 record 不是；并发修改需要同步，退出时的析构顺序也可能有影响。
- **记忆提示:** instance 唯一，问题未必少。

[上一个](../../creational/prototype/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/adapter/README.zh-CN.md)
