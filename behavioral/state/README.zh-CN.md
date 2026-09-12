# 状态

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/observer/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/strategy/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

由对象的当前状态决定响应和状态转换。

## 问题

门在开启与关闭时对同一按钮反应不同，更复杂设备还会有锁定或故障状态。

## 最初的简单方案

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## 为什么难以维护

两态切换用布尔值足够，但多个事件复制状态判断后，转换规则容易不一致。

## 核心思路

Door 把 press 委托给当前 DoorState，由状态选择下一状态。

## 生活类比

自动售货机在付款前后对同一输入做不同处理。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![状态](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## 参与者

Door 是上下文，DoorState 定义 press 和 name；Open、Closed 保存非拥有的后继链接，main 保证两者比 Door 活得更久。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <string_view>

class Door;
struct DoorState {
    virtual ~DoorState() = default;
    virtual void press(Door& door) const = 0;
    virtual std::string_view name() const = 0;
};
class Door {
    const DoorState* state_;
public:
    explicit Door(const DoorState& state) : state_(&state) {}
    void change(const DoorState& state) { state_ = &state; }
    void press() { state_->press(*this); }
    std::string_view name() const { return state_->name(); }
};
struct Open final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "open"; }
};
struct Closed final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "closed"; }
};
int main() {
    Open open;
    Closed closed;
    open.next = &closed;
    closed.next = &open;
    Door door{closed};
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
}
```

## 预期输出

```text
closed
open
closed
```

## 何时使用

状态相关行为和转换分散在多个操作时使用。

## 何时不该使用

简单开关或清晰的小型枚举转换表，不必换成类层次。

## 优点

行为按状态集中，转换可在局部检查。

## 缺点与权衡

增加类型和生命周期关系。状态对象在 Door 外部，转换不会销毁仍在执行的状态；复杂设计也需保持这一安全条件。

## 技术应用场景

适合协议会话和设备流程，前提是转换规则明确。

## 相关模式

[strategy](../strategy/README.zh-CN.md) · [observer](../observer/README.zh-CN.md)

## 常见混淆

策略通常由调用方选择算法；状态表示生命周期，并可能自行决定转换。

## 面试问题

这里由谁选择下个状态？与选择运费策略有什么不同？

## 小练习

增加 Locked，使 press 不解锁，再添加独立 unlock 事件并测试转换序列。

## 小结

- **问题:** 门在开启与关闭时对同一按钮反应不同，更复杂设备还会有锁定或故障状态。
- **方案:** Door 把 press 委托给当前 DoorState，由状态选择下一状态。
- **权衡:** 增加类型和生命周期关系。状态对象在 Door 外部，转换不会销毁仍在执行的状态；复杂设计也需保持这一安全条件。
- **记忆提示:** 事件相同，状态不同，响应不同。

[上一个](../../behavioral/observer/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/strategy/README.zh-CN.md)
