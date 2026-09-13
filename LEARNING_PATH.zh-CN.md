# 学习路线

[模式目录](README.zh-CN.md)

目录按目的分类；这条路线先展示小而直观的变化，再引入更复杂的 ownership 和分派选择。


## 简单的学习方法

每次学习一个 Design Pattern。目标是解释设计选择，而不是背定义。

1. 阅读 **简单理解**。
2. 阅读 **The Problem** 和 **Naive Solution**，先自己描述问题，再看方案。
3. 阅读 Python 代码，预测输出。
4. 运行并修改一个输入或 behavior，验证预测。
5. 阅读并运行 C++20 示例。
6. 根据 Python README 中的说明比较两种实现，关注 Interface、Composition、Ownership、Lifetime 和 Runtime 选择。
7. 不查答案，尝试回答 **Interview Question** 和 **检查理解**。
8. 在自己的副本中完成 **Mini Challenge**。
9. 用一分钟解释问题、简单代码何时变难维护、方案、trade-off，以及何时不使用。

学习顺序是理解需求、观察示例、动手实现、分析工程取舍，最后准备面试。记下哪些部分会变、哪些不变，以及新增结构的成本。第二天再回顾，并尝试英文[识别练习](PRACTICE.md)。

按下面的编号学习。目录按类别分组，不代表难度顺序。后面的内容逐步涉及复制、Ownership、Lifetime、内存共享、dispatch、类型关系和 global state。


1. [Strategy](behavioral/strategy/README.zh-CN.md) — 替换一个计算，直观看到 Strategy 的价值。
2. [Observer](behavioral/observer/README.zh-CN.md) — 把变化连接到监听者，再理解订阅 lifetime。
3. [Factory Method](creational/factory-method/README.zh-CN.md) — 保持流程，改变 object 创建。
4. [Adapter](structural/adapter/README.zh-CN.md) — 在清晰边界转换已有 interface。
5. [Decorator](structural/decorator/README.zh-CN.md) — 逐层组合附加 behavior。
6. [Command](behavioral/command/README.zh-CN.md) — 把动作表示出来，为撤销明确 responsibility。
7. [Composite](structural/composite/README.zh-CN.md) — 从一个 object 扩展到 object 树。
8. [State](behavioral/state/README.zh-CN.md) — 从 algorithm 选择进入 lifetime 转换。

## 接着扩展视野

继续学习 Facade、 Builder、 Template Method、 Bridge、 Proxy、 Chain of Responsibility 和 Mediator，把熟悉的委托连接到创建和协调。

9. [Facade](structural/facade/README.zh-CN.md)
10. [Builder](creational/builder/README.zh-CN.md)
11. [Template Method](behavioral/template-method/README.zh-CN.md)
12. [Bridge](structural/bridge/README.zh-CN.md)
13. [Proxy](structural/proxy/README.zh-CN.md)
14. [Chain of Responsibility](behavioral/chain-of-responsibility/README.zh-CN.md)
15. [Mediator](behavioral/mediator/README.zh-CN.md)

## 最后深入权衡

最后学习 Abstract Factory、 Prototype、 Memento、 iterator、 Flyweight、 Interpreter、 Visitor 和 Singleton。重点关注复制、 lifetime、内存、 type 分派和全局 state。

16. [Abstract Factory](creational/abstract-factory/README.zh-CN.md)
17. [Prototype](creational/prototype/README.zh-CN.md)
18. [Memento](behavioral/memento/README.zh-CN.md)
19. [Iterator](behavioral/iterator/README.zh-CN.md)
20. [Flyweight](structural/flyweight/README.zh-CN.md)
21. [Interpreter](behavioral/interpreter/README.zh-CN.md)
22. [Visitor](behavioral/visitor/README.zh-CN.md)
23. [Singleton](creational/singleton/README.zh-CN.md)
