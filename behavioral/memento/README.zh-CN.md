# 备忘录

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/mediator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/observer/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

在不公开快照内部数据的情况下保存和恢复对象状态。

## 问题

编辑器在尝试修改前需要一个检查点。

## 最初的简单方案

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## 为什么难以维护

撤销管理器自己复制公开字段时，每增加一个内部字段都得跟着修改。

## 核心思路

Editor 创建保存私有文本的 Snapshot，需要时读取快照并恢复自身。

## 生活类比

游戏存档能返回早先进度，玩家不必了解其数据格式。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![备忘录](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## 参与者

Editor 是发起者，Snapshot 是保存私有状态的备忘录，main 是只持有快照的管理者。

## 现代 C++20 完整可运行示例

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
}
```

## 预期输出

```text
Broken edit
Draft
```

## 何时使用

对象能定义一致快照，且需要检查点时使用。

## 何时不该使用

状态巨大、资源不可恢复，或逆操作记录更便宜时避免。

## 优点

状态表示保留在发起者内部，管理者无需手动复制字段。

## 缺点与权衡

完整快照占用内存和复制时间；恢复字符串无法撤销文件、网络等外部副作用。

## 技术应用场景

适合编辑器检查点和模拟快照，前提是保存状态完整且一致。

## 相关模式

[command](../command/README.zh-CN.md) · [prototype](../../creational/prototype/README.zh-CN.md)

## 常见混淆

命令保存动作，备忘录保存状态；原型创建另一个对象，而不是恢复当前对象。

## 面试问题

Editor 增加光标位置后，哪些地方必须修改才能正确恢复？

## 小练习

在 Snapshot 中保存光标，验证文本和光标一起恢复。

## 小结

- **问题:** 编辑器在尝试修改前需要一个检查点。
- **方案:** Editor 创建保存私有文本的 Snapshot，需要时读取快照并恢复自身。
- **权衡:** 完整快照占用内存和复制时间；恢复字符串无法撤销文件、网络等外部副作用。
- **记忆提示:** 保存状态，不公开细节。

[上一个](../../behavioral/mediator/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/observer/README.zh-CN.md)
