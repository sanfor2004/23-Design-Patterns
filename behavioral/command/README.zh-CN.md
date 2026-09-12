# 命令

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/chain-of-responsibility/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/interpreter/README.zh-CN.md)

## 类别

行为型

## 难度

中级

## 一句话说明

把操作封装成可保存、可延后调用的对象。

## 问题

编辑器要执行和撤销操作，工具栏不应了解每种文档修改。

## 最初的简单方案

```cpp
document.text += " world"; // no object records how to undo
```

## 为什么难以维护

直接修改文本完成了工作，却没有留下动作及之前状态的记录。

## 核心思路

Append 保存接收者和参数；execute 记录旧文本，undo 恢复。History 拥有已执行命令。

## 生活类比

餐厅点菜单独立记录动作，不依赖提交它的服务员。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![命令](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## 参与者

Command 定义执行和撤销，Append 修改借用的 Document，History 按栈顺序调用和保存。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Document { std::string text; };
struct Command {
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};
class Append final : public Command {
    Document& document_;
    std::string suffix_;
    std::string before_;
public:
    Append(Document& document, std::string suffix) : document_(document), suffix_(std::move(suffix)) {}
    void execute() override { before_ = document_.text; document_.text += suffix_; }
    void undo() override { document_.text = before_; }
};
class History {
    std::vector<std::unique_ptr<Command>> commands_;
public:
    void run(std::unique_ptr<Command> command) {
        if (!command) throw std::invalid_argument("Missing command");
        commands_.push_back(std::move(command));
        try { commands_.back()->execute(); }
        catch (...) { commands_.pop_back(); throw; }
    }
    void undo() {
        if (commands_.empty()) return;
        commands_.back()->undo();
        commands_.pop_back();
    }
};
int main() {
    Document document{"Hello"};
    History history;
    history.run(std::make_unique<Append>(document, " world"));
    std::cout << document.text << '\n';
    history.undo();
    std::cout << document.text << '\n';
}
```

## 预期输出

```text
Hello world
Hello
```

## 何时使用

适合延迟操作、队列、宏命令或撤销历史。

## 何时不该使用

一次性函数调用无需保存或调度意图时，避免额外对象。

## 优点

调用者不依赖具体操作，可以保留执行历史。

## 缺点与权衡

保存全文耗费内存。单线程示例假定修改都经过 History，且 Document 比历史活得更久；外部修改会破坏撤销预期。

## 技术应用场景

适合编辑器操作和任务队列；持久队列还需要序列化、幂等性等机制。

## 相关模式

[memento](../memento/README.zh-CN.md) · [chain-of-responsibility](../chain-of-responsibility/README.zh-CN.md)

## 常见混淆

备忘录保存状态，命令保存动作并可用快照撤销；不是所有命令都可逆。

## 面试问题

发送邮件能像恢复字符串一样撤销吗？区分补偿和逆操作。

## 小练习

连续追加两次再撤销两次，验证空历史上的撤销无副作用。

## 小结

- **问题:** 编辑器要执行和撤销操作，工具栏不应了解每种文档修改。
- **方案:** Append 保存接收者和参数；execute 记录旧文本，undo 恢复。History 拥有已执行命令。
- **权衡:** 保存全文耗费内存。单线程示例假定修改都经过 History，且 Document 比历史活得更久；外部修改会破坏撤销预期。
- **记忆提示:** 把动作保存下来。

[上一个](../../behavioral/chain-of-responsibility/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/interpreter/README.zh-CN.md)
