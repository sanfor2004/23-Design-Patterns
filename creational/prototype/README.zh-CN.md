# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/factory-method/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/singleton/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — 关注如何创建和配置 object 的 Design Pattern。

## Difficulty

中级

## In One Sentence

复制一个配置好的 object，得到独立的新 object。

## 简单理解

游戏中已有一个装备齐全的守卫。Prototype 复制这份配置，让新守卫可以独立修改，不影响原来的守卫。

## The Problem

游戏需要从已配置 template 生成敌人，而生成逻辑不知道 template 的 concrete type。

## Naive Solution

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Why It Becomes a Problem

每次重建默认 Guard 会重复初始化，也会丢失 template 上的自定义装备。

## The Idea

Enemy 提供 clone；Guard 复制值成员并返回指向独立 object 的 [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr)。

## Real-World Analogy

复制一份准备好的文档，只修改副本的名称，原件保持不变。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Participants

Enemy 定义 polymorphic cloning [`interface`](../../GLOSSARY.md#interface)，Guard 实现复制， Client 拥有副本并修改名称。

本例中的标准角色：

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — 通过 clone 操作按已配置值创建另一 object 的 object。 对应代码： `Guard`。
- [`deep copy`](../../GLOSSARY.md#deep-copy) — 复制所拥有的嵌套数据，使新 object 不与原 object 共享这些可变数据。 对应代码： `Guard::clone`。
- [`value semantics`](../../GLOSSARY.md#value-semantics) — 按照类型约定，副本表现为独立的值。 对应代码： `name_, equipment_`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

struct Enemy {
    virtual ~Enemy() = default;
    virtual std::unique_ptr<Enemy> clone() const = 0;
    virtual void rename(std::string name) = 0;
    virtual void describe() const = 0;
};
class Guard final : public Enemy {
    std::string name_ = "template";
    std::vector<std::string> equipment_{"shield", "spear"};
public:
    std::unique_ptr<Enemy> clone() const override { return std::make_unique<Guard>(*this); }
    void rename(std::string name) override { name_ = std::move(name); }
    void describe() const override {
        std::cout << name_ << ": " << equipment_.size() << " items\n";
    }
};
int main() {
    const Guard prototype;
    auto copy = prototype.clone();
    copy->rename("gate guard");
    prototype.describe();
    copy->describe();
}
```

## Example Output

```text
template: 2 items
gate guard: 2 items
```

## When to Use

已有 [`runtime`](../../GLOSSARY.md#runtime) object 带有有用配置，且 Client 不应重建 concrete type 时使用。

### Use cases

适合游戏实体 template 和可编辑文档预设；这里的字符串与向量都按值复制。

## When NOT to Use

普通值复制已经清晰表达需求时，不必增加克隆 interface。

## Advantages

复用配置， Client 无需了解每个初始化步骤。

## Trade-offs

pointer 成员需要明确 deep copy 还是共享。活动套接字等独占资源可能无法合理复制。

## Related Patterns

[Abstract Factory](../abstract-factory/README.zh-CN.md) · [Memento](../../behavioral/memento/README.zh-CN.md)

## Common Confusion

Memento 恢复同一 object 的旧 state， Prototype 创建另一个 object；普通 copy constructor 本身不提供 polymorphic cloning。

## Terms to Remember

- `Prototype` — 复制一个配置好的 object，得到独立的新 object。
- `Concrete Prototype` — 通过 clone 操作按已配置值创建另一 object 的 object。 示例： `Guard`。
- `deep copy` — 复制所拥有的嵌套数据，使新 object 不与原 object 共享这些可变数据。 示例： `Guard::clone`。
- `value semantics` — 按照类型约定，副本表现为独立的值。 示例： `name_, equipment_`。

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — 选择具体类型，建立 object 的初始值并开始其 lifetime。
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — 同一 interface 对应不同 implementation；C++ 同时支持 runtime 与 compile time 的形式。
- [`ownership`](../../GLOSSARY.md#ownership) — 负责维持资源存活并最终释放资源的责任。

## Interview Question

若装备变成 `std::vector<std::shared_ptr<Item>>`，副本还独立吗？解释别名问题。

## Mini Challenge

增加可编辑装备，并验证修改副本不会影响 Prototype。

## 检查理解

1. 把原 Object 赋给另一个变量会得到独立副本吗？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 游戏需要从已配置 template 生成敌人，而生成逻辑不知道 template 的 concrete type。
- **方案:** Enemy 提供 clone；Guard 复制值成员并返回指向独立 object 的 std::unique_ptr。
- **权衡:** pointer 成员需要明确 deep copy 还是共享。活动套接字等独占资源可能无法合理复制。
- **记忆提示:** 复制配置，不复制身份。

[上一个](../../creational/factory-method/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/singleton/README.zh-CN.md)
