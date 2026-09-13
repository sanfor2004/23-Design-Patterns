# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/mediator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/observer/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

保存并恢复 Object 的 `state`，同时不暴露 Snapshot 的内部数据。

## 简单理解

编辑器需要在可能出错的修改前保留检查点。Memento 保存当前 `state`，由编辑器决定如何恢复。

## The Problem

编辑器在尝试修改前需要一个检查点。

## Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why It Becomes a Problem

撤销管理器自己复制 public 字段时，每增加一个内部字段都得跟着修改。

## The Idea

Editor 创建保存 private 文本的 Snapshot，需要时读取 snapshot 并恢复自身。

## Real-World Analogy

游戏存档能返回早先进度，玩家不必了解其数据格式。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Participants

Editor 是 Originator，Snapshot 是保存 private state 的 Memento，main 是只持有 snapshot 的 Caretaker。

本例中的标准角色：

- [`Originator`](../../GLOSSARY.md#originator) — 知道如何保存和恢复自身 state 的 object。 对应代码： `Editor`。
- [`Caretaker`](../../GLOSSARY.md#caretaker) — 保存 Memento、但不检查其私有表示的角色。 对应代码： `main`。
- [`snapshot`](../../GLOSSARY.md#snapshot) — 某一时刻所选 state 的保存表示。 对应代码： `Editor::Snapshot`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <utility>

class Editor {
    std::string text_;
public:
    class Snapshot {
        friend class Editor;
        std::string text_;
        explicit Snapshot(std::string text) : text_(std::move(text)) {}
    };
    void write(std::string text) { text_ = std::move(text); }
    Snapshot save() const { return Snapshot{text_}; }
    void restore(const Snapshot& snapshot) { text_ = snapshot.text_; }
    const std::string& text() const { return text_; }
};
int main() {
    Editor editor;
    editor.write("Draft");
    const auto checkpoint = editor.save();
    editor.write("Broken edit");
    std::cout << editor.text() << '\n';
    editor.restore(checkpoint);
    std::cout << editor.text() << '\n';
    editor.write("Another edit");
    editor.restore(checkpoint);
    std::cout << "Restore again: " << editor.text() << '\n';
}
```

## Example Output

```text
Broken edit
Draft
Restore again: Draft
```

## When to Use

object 能定义一致 snapshot，且需要检查点时使用。

### Use cases

适合编辑器检查点和模拟 snapshot，前提是保存 state 完整且一致。

## When NOT to Use

state 巨大、资源不可恢复，或逆操作记录更便宜时避免。

## Advantages

State 的表示保留在 Originator 内部，Caretaker 无需手动复制字段。

## Trade-offs

完整 snapshot 占用内存和复制时间；恢复字符串无法撤销文件、网络等外部 side effect。

## Related Patterns

[Command](../command/README.zh-CN.md) · [Prototype](../../creational/prototype/README.zh-CN.md)

## Common Confusion

Command 保存动作， Memento 保存 state； Prototype 创建另一个 object，而不是恢复当前 object。

## Terms to Remember

- `Memento` — 保存并恢复 Object 的 `state`，同时不暴露 Snapshot 的内部数据。
- `Originator` — 知道如何保存和恢复自身 state 的 object。 示例： `Editor`。
- `Caretaker` — 保存 Memento、但不检查其私有表示的角色。 示例： `main`。
- `snapshot` — 某一时刻所选 state 的保存表示。 示例： `Editor::Snapshot`。

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — 把内部表示和必须保持的规则放在受控操作之后。
- [`undo`](../../GLOSSARY.md#undo) — 在可行时用保存的 state 或逆操作恢复之前的逻辑结果。
- [`ownership`](../../GLOSSARY.md#ownership) — 负责维持资源存活并最终释放资源的责任。

## Interview Question

Editor 增加光标位置后，哪些地方必须修改才能正确恢复？

## Mini Challenge

在 Snapshot 中保存光标，验证文本和光标一起恢复。

## 检查理解

1. 为什么之后的修改不能改变已保存的 Snapshot？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 编辑器在尝试修改前需要一个检查点。
- **方案:** Editor 创建保存 private 文本的 Snapshot，需要时读取 snapshot 并恢复自身。
- **权衡:** 完整 snapshot 占用内存和复制时间；恢复字符串无法撤销文件、网络等外部 side effect。
- **记忆提示:** 保存 state，不 public 细节。

[上一个](../../behavioral/mediator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/observer/README.zh-CN.md)
