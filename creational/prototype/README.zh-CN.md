# 原型

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/factory-method/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/singleton/README.zh-CN.md)

## 类别

创建型

## 难度

中级

## 一句话说明

复制一个配置好的对象，得到独立的新对象。

## 问题

游戏需要从已配置模板生成敌人，而生成逻辑不知道模板的具体类型。

## 最初的简单方案

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## 为什么难以维护

每次重建默认 Guard 会重复初始化，也会丢失模板上的自定义装备。

## 核心思路

Enemy 提供 clone；Guard 复制值成员并返回指向独立对象的 unique_ptr。

## 生活类比

复制一份准备好的文档，只修改副本的名称，原件保持不变。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![原型](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## 参与者

Enemy 定义多态克隆接口，Guard 实现复制，调用方拥有副本并修改名称。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
template: 2 items
gate guard: 2 items
```

## 何时使用

已有运行时对象带有有用配置，且调用方不应重建具体类型时使用。

## 何时不该使用

普通值复制已经清晰表达需求时，不必增加克隆接口。

## 优点

复用配置，调用方无需了解每个初始化步骤。

## 缺点与权衡

指针成员需要明确深拷贝还是共享。活动套接字等独占资源可能无法合理复制。

## 技术应用场景

适合游戏实体模板和可编辑文档预设；这里的字符串与向量都按值复制。

## 相关模式

[abstract-factory](../abstract-factory/README.zh-CN.md) · [memento](../../behavioral/memento/README.zh-CN.md)

## 常见混淆

备忘录恢复同一对象的旧状态，原型创建另一个对象；普通复制构造函数本身不提供多态克隆。

## 面试问题

若装备变成 vector<shared_ptr<Item>>，副本还独立吗？解释别名问题。

## 小练习

增加可编辑装备，并验证修改副本不会影响原型。

## 小结

- **问题:** 游戏需要从已配置模板生成敌人，而生成逻辑不知道模板的具体类型。
- **方案:** Enemy 提供 clone；Guard 复制值成员并返回指向独立对象的 unique_ptr。
- **权衡:** 指针成员需要明确深拷贝还是共享。活动套接字等独占资源可能无法合理复制。
- **记忆提示:** 复制配置，不复制身份。

[上一个](../../creational/factory-method/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../creational/singleton/README.zh-CN.md)
