# Command

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../behavioral/chain-of-responsibility/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/interpreter/README.zh-CN.md)

[学习路线](../../LEARNING_PATH.zh-CN.md) · [速查表](../../CHEATSHEET.zh-CN.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — 关注 object 的 behavior 与协作方式的 Design Pattern。

## Difficulty

中级

## In One Sentence

通过 [`encapsulation`](../../GLOSSARY.md#encapsulation) 把操作及其数据组成可保存、可延后调用的 object。

## 简单理解

编辑器需要记住修改，以便用户撤销。Command 保存操作和撤销所需信息，History 决定何时执行或撤销。

## The Problem

编辑器要执行和撤销操作，工具栏不应了解每种文档修改。

## Naive Solution

```cpp
document.text += " world"; // no object records how to undo
```

## Why It Becomes a Problem

直接修改文本完成了工作，却没有留下动作及之前 state 的记录。

## The Idea

Append 保存 Receiver 和参数；execute 记录旧文本，undo 恢复。History 拥有已执行 Command。

## Real-World Analogy

餐厅点菜单独立记录动作，不依赖提交它的服务员。

## Structure

[结构图](diagram.md) · [运行示例](cpp/README.md)

![Command](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## Participants

Command 定义执行和撤销，Append 修改借用的 Document，History 按栈顺序调用和保存。

本例中的标准角色：

- [`Receiver`](../../GLOSSARY.md#receiver) — 执行 Command 所请求工作的 object。 对应代码： `Document`。
- [`Invoker`](../../GLOSSARY.md#invoker) — 启动或保存 Command、无需了解每项操作细节的角色。 对应代码： `History`。
- [`Concrete Command`](../../GLOSSARY.md#concrete-command) — 把 Receiver 与动作绑定起来的 Command implementation。 对应代码： `Append`。

## Python Example

先读[简短的 Python 示例](python/README.md)和[源码](python/main.py)。预测[输出](python/expected.txt)，然后运行并修改。示例中的英文说明比较了它与 C++20 的设计。

## Modern C++20 Example

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
    history.undo();
    std::cout << "Empty undo: " << document.text << '\n';
}
```

## Example Output

```text
Hello world
Hello
Empty undo: Hello
```

## When to Use

适合延迟操作、队列、宏 Command 或撤销历史。

### Use cases

适合编辑器操作和任务队列；持久队列还需要 serialization、 idempotency 等机制。

## When NOT to Use

一次性 function 调用无需保存或调度意图时，避免额外 object。

## Advantages

Client 不依赖具体操作，可以保留执行历史。

## Trade-offs

保存全文耗费内存。单线程示例假定修改都经过 History，且 Document 比历史活得更久；外部修改会破坏撤销预期。

## Related Patterns

[Memento](../memento/README.zh-CN.md) · [Chain of Responsibility](../chain-of-responsibility/README.zh-CN.md)

## Common Confusion

Memento 保存 state， Command 保存动作并可用 snapshot 撤销；不是所有 Command 都可逆。

## Terms to Remember

- `Command` — 通过 encapsulation 把操作及其数据组成可保存、可延后调用的 object。
- `Receiver` — 执行 Command 所请求工作的 object。 示例： `Document`。
- `Invoker` — 启动或保存 Command、无需了解每项操作细节的角色。 示例： `History`。
- `Concrete Command` — 把 Receiver 与动作绑定起来的 Command implementation。 示例： `Append`。

## Interview Vocabulary

- [`undo`](../../GLOSSARY.md#undo) — 在可行时用保存的 state 或逆操作恢复之前的逻辑结果。
- [`encapsulation`](../../GLOSSARY.md#encapsulation) — 把内部表示和必须保持的规则放在受控操作之后。
- [`exception safety`](../../GLOSSARY.md#exception-safety) — 操作抛出 exception 时仍能保持的保证。

## Interview Question

发送邮件能像恢复字符串一样撤销吗？区分补偿和逆操作。

## Mini Challenge

连续追加两次再撤销两次，验证空历史上的撤销无 side effect。

## 检查理解

1. 为什么这些修改必须按相反顺序撤销？
2. 本页的简单方案在什么情况下更容易维护？请举一个具体例子。
3. 修改 Python 示例中的一个输入，预测输出，并说明由哪个部分负责处理。

## Quick Summary

- **问题:** 编辑器要执行和撤销操作，工具栏不应了解每种文档修改。
- **方案:** Append 保存 Receiver 和参数；execute 记录旧文本，undo 恢复。History 拥有已执行 Command。
- **权衡:** 保存全文耗费内存。单线程示例假定修改都经过 History，且 Document 比历史活得更久；外部修改会破坏撤销预期。
- **记忆提示:** 把动作保存下来。

[上一个](../../behavioral/chain-of-responsibility/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/interpreter/README.zh-CN.md)
