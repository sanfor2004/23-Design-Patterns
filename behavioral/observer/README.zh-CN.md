# 观察者

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/memento/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/state/README.zh-CN.md)

## 类别

行为型

## 难度

入门

## 一句话说明

被关注的状态变化时，通知已订阅的对象。

## 问题

库存变化要更新相关显示，但 Stock 不应了解每种具体显示类型。

## 最初的简单方案

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## 为什么难以维护

直接点名调用各消费者，会把发布者绑定到当前名单，新增消费者就要修改它。

## 核心思路

Stock 保存 Listener 的弱引用，更新时通知仍存活的订阅者。

## 生活类比

订阅商品到货提醒后，在订阅有效期间接收通知。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![观察者](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## 参与者

Stock 是主题，Listener 是回调接口，Display 是订阅者。调用方拥有订阅者，weak_ptr 不延长其寿命。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
Stock: 4
Expired listener skipped
```

## 何时使用

一个变化对应多个独立注册的消费者时使用。

## 何时不该使用

只有一个固定依赖，或需要严格事务一致性时，不宜用简单广播替代。

## 优点

订阅者可增减，发布者代码不变。

## 缺点与权衡

回调顺序和异常需要策略。此同步示例传播异常且非线程安全；列表快照允许订阅变更，但不阻止递归通知。

## 技术应用场景

适合 UI 更新和本地事件订阅；分布式事件投递保证是额外问题。

## 相关模式

[mediator](../mediator/README.zh-CN.md) · [state](../state/README.zh-CN.md)

## 常见混淆

中介者规定已知同级对象的协调规则；观察者广播通知，不规定订阅者之间的关系。

## 面试问题

为什么保存 weak_ptr，却在回调时 lock 成 shared_ptr？

## 小练习

注册两个监听者，销毁其中一个，验证后续只通知存活者，再定义显式取消订阅。

## 小结

- **问题:** 库存变化要更新相关显示，但 Stock 不应了解每种具体显示类型。
- **方案:** Stock 保存 Listener 的弱引用，更新时通知仍存活的订阅者。
- **权衡:** 回调顺序和异常需要策略。此同步示例传播异常且非线程安全；列表快照允许订阅变更，但不阻止递归通知。
- **记忆提示:** 发布变化，让订阅者响应。

[上一个](../../behavioral/memento/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/state/README.zh-CN.md)
