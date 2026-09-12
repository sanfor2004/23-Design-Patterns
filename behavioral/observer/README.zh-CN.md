# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/memento/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/state/README.zh-CN.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

入门

## In One Sentence

被关注的 state 变化时，通知已订阅的 object。

## The Problem

库存变化要更新相关显示，但 Stock 不应了解每种具体显示 type。

## Naive Solution

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## Why It Becomes a Problem

直接点名调用各消费者，会把发布者绑定到当前名单，新增消费者就要修改它。

## The Idea

Stock 保存 Listener 的 weak reference，更新时通知仍存活的订阅者。

## Real-World Analogy

订阅商品到货提醒后，在订阅有效期间接收通知。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Observer](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## Participants

Stock 是 Subject，Listener 是 callback [`interface`](../../GLOSSARY.md#interface)（约定可调用的操作及其对外可观察行为），Display 是订阅者。 Client 拥有订阅者，[`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr)（观察共享 ownership 但不拥有 object；lock 尝试取得临时 shared_ptr） 不延长其 [`lifetime`](../../GLOSSARY.md#lifetime)（object 存在且可按规则使用的时间区间）。

本例中的标准角色：

- [`Subject`](../../GLOSSARY.md#subject) — 把自身变化通知给已注册 Observer 的发布方。 对应代码： `Stock`。
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — 订阅方实现的 callback 约定。 对应代码： `Listener`。
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — 响应通知的 Observer implementation。 对应代码： `Display`。

## Modern C++20 Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
}
```

## Example Output

```text
Stock: 4
Expired listener skipped
```

## When to Use

一个变化对应多个独立注册的消费者时使用。

### Use cases

适合 UI 更新和本地 event 订阅；分布式 event 投递保证是额外问题。

## When NOT to Use

只有一个固定依赖，或需要严格事务一致性时，不宜用简单广播替代。

## Advantages

订阅者可增减，发布者代码不变。

## Trade-offs

callback 顺序和 exception 需要明确的 policy。此同步示例传播 exception 且非 thread-safe；列表 snapshot 允许订阅变更，但不阻止 recursive 通知。

## Related Patterns

[Mediator](../mediator/README.zh-CN.md) · [State](../state/README.zh-CN.md)

## Common Confusion

Mediator 规定已知同级 object 的协调规则； Observer 广播通知，不规定订阅者之间的关系。

## Terms to Remember

- `Observer` — 被关注的 state 变化时，通知已订阅的 object。
- `Subject` — 把自身变化通知给已注册 Observer 的发布方。 示例： `Stock`。
- `Observer interface` — 订阅方实现的 callback 约定。 示例： `Listener`。
- `Concrete Observer` — 响应通知的 Observer implementation。 示例： `Display`。

## Interview Vocabulary

- [`one-to-many dependency`](../../GLOSSARY.md#one-to-many-dependency) — 一个来源发生变化时，有多个依赖方需要响应。
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — 各部分只了解协作所需的小范围约定，限制修改传播。
- [`subscription lifetime`](../../GLOSSARY.md#subscription-lifetime) — 监听方已注册且可以接收通知的时间区间。

## Interview Question

为什么保存 std::weak_ptr，却在 callback 时 lock 成 [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr)（共享 ownership 的 smart pointer，最后一个拥有引用消失时释放 object）？

## Mini Challenge

注册两个监听者，销毁其中一个，验证后续只通知存活者，再定义显式取消订阅。

## Quick Summary

- **问题:** 库存变化要更新相关显示，但 Stock 不应了解每种具体显示 type。
- **方案:** Stock 保存 Listener 的 weak reference，更新时通知仍存活的订阅者。
- **权衡:** callback 顺序和 exception 需要明确的 policy。此同步示例传播 exception 且非 thread-safe；列表 snapshot 允许订阅变更，但不阻止 recursive 通知。
- **记忆提示:** 发布变化，让订阅者响应。

[上一个](../../behavioral/memento/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/state/README.zh-CN.md)
