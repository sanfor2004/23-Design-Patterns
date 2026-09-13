# State

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/observer/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/strategy/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

由 object 的当前 state 决定响应和 state transition。

## 简单理解

按门的按钮时，关闭的门会打开，打开的门会关闭。State 把响应和转换放进代表当前状况的 Object。

## The Problem

门在开启与关闭时对同一按钮反应不同，更复杂设备还会有锁定或故障 state。

## Naive Solution

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Why It Becomes a Problem

两态切换用布尔值足够，但多个 event 复制 state 判断后，转换规则容易不一致。

## The Idea

Door 把 press 委托给当前 DoorState，由 state 选择下一 state。

## Real-World Analogy

自动售货机在付款前后对同一输入做不同处理。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Participants

Door 是 Context，DoorState 定义 press 和 name；Open、Closed 保存 non-owning 的 后继链接，main 保证两者比 Door 活得更久。

本例中的标准角色：

- [`Context`](../../GLOSSARY.md#context) — 使用 Strategy 或把 behavior 委托给当前 State 的 object。 对应代码： `Door`。
- [`State interface`](../../GLOSSARY.md#state-interface) — Context 用于委托与 state 有关的 behavior 的约定。 对应代码： `DoorState`。
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — 为某个 State 定义 behavior 和转换规则的 implementation。 对应代码： `Open, Closed`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

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

## Example Output

```text
closed
open
closed
```

## When to Use

state 相关 behavior 和转换分散在多个操作时使用。

### Use cases

适合协议会话和设备流程，前提是转换规则明确。

## When NOT to Use

简单开关或清晰的小型 enum 转换表，不必换成 class hierarchy。

## Advantages

behavior 按 state 集中，转换可在局部检查。

## Trade-offs

增加 type 和 [`lifetime`](../../GLOSSARY.md#lifetime) 关系。 state object 在 Door 外部，转换不会销毁仍在执行的 state；复杂设计也需保持这一安全条件。

## Related Patterns

[Strategy](../strategy/README.zh-CN.md) · [Observer](../observer/README.zh-CN.md)

## Common Confusion

Strategy 通常由 Client 选择 algorithm；State 表示 [`lifecycle`](../../GLOSSARY.md#lifecycle)，并可能自行决定转换。

## Terms to Remember

- `State` — 由 object 的当前 state 决定响应和 state transition。
- `Context` — 使用 Strategy 或把 behavior 委托给当前 State 的 object。 示例： `Door`。
- `State interface` — Context 用于委托与 state 有关的 behavior 的约定。 示例： `DoorState`。
- `Concrete State` — 为某个 State 定义 behavior 和转换规则的 implementation。 示例： `Open, Closed`。

## Interview Vocabulary

- [`state transition`](../../GLOSSARY.md#state-transition) — 在 event 后从一个建模状态转到另一个状态。
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — 程序执行时实际发生的动作，包括由运行时输入选择的 behavior。
- [`delegation`](../../GLOSSARY.md#delegation) — 一个 object 把部分工作交给协作方完成。

## Interview Question

这里由谁选择下个 state？与选择运费 Strategy 有什么不同？

## Mini Challenge

增加 Locked，使 press 不解锁，再添加独立 unlock event 并测试转换序列。

## 检查理解

1. 按下门按钮时，谁选择下一个 State？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 门在开启与关闭时对同一按钮反应不同，更复杂设备还会有锁定或故障 state。
- **方案:** Door 把 press 委托给当前 DoorState，由 state 选择下一 state。
- **权衡:** 增加 type 和 lifetime 关系。 state object 在 Door 外部，转换不会销毁仍在执行的 state；复杂设计也需保持这一安全条件。
- **记忆提示:** event 相同， state 不同，响应不同。

[上一个](../../behavioral/observer/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/strategy/README.zh-CN.md)
