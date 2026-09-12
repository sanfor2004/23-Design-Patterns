![Sanfor2004](assets/brand/logo.svg)

# Design-Patterns-23

23 Patterns · 4 Languages · Real Examples · Simple Explanations

[Sanfor2004](https://github.com/Sanfor2004) · C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

从真实问题出发，看看简单方案何时遇到困难。理解模式，运行 C++，再判断额外结构是否值得。

- [学习路线](LEARNING_PATH.zh-CN.md)
- [速查表](CHEATSHEET.zh-CN.md)
- [关系图](PATTERN_MAP.zh-CN.md)
- [模式对比](COMPARISONS.zh-CN.md)
- [C++20](CPP_EXAMPLES.md)

## 为什么建立这个仓库

通过一个小程序追踪具体问题，比只记住模式名称更容易理解设计。这里把动机、代码、输出和权衡放在一起，帮助你判断额外的抽象是否值得。

## 如何阅读

从下面的分类或学习路径开始。每个模式目录包含四种语言的说明、结构图和 `cpp/` 目录。语言链接会打开同一模式的对应译文。

## 创建型

对象如何创建

- [抽象工厂](creational/abstract-factory/README.zh-CN.md) — 通过统一的工厂接口创建相互配套的对象。 (中级)
- [建造者](creational/builder/README.zh-CN.md) — 用具名步骤配置对象，最后一次性生成结果。 (入门)
- [工厂方法](creational/factory-method/README.zh-CN.md) — 让子类决定公共流程所使用的具体对象。 (入门)
- [原型](creational/prototype/README.zh-CN.md) — 复制一个配置好的对象，得到独立的新对象。 (中级)
- [单例](creational/singleton/README.zh-CN.md) — 限制类型只提供一个实例，同时承担全局共享状态的代价。 (中级)

## 结构型

对象如何组合

- [适配器](structural/adapter/README.zh-CN.md) — 把已有接口转换成调用方期待的接口。 (入门)
- [桥接](structural/bridge/README.zh-CN.md) — 把两个变化维度分开，再用组合连接。 (中级)
- [组合](structural/composite/README.zh-CN.md) — 让单个叶子和对象树提供同一种操作。 (入门)
- [装饰器](structural/decorator/README.zh-CN.md) — 用实现相同接口的包装对象叠加行为。 (入门)
- [外观](structural/facade/README.zh-CN.md) — 为子系统的常见流程提供一个小而清晰的入口。 (入门)
- [享元](structural/flyweight/README.zh-CN.md) — 共享不可变的内部数据，把每次使用的上下文留在外部。 (进阶)
- [代理](structural/proxy/README.zh-CN.md) — 通过相同接口的替身控制对真实对象的访问。 (中级)

## 行为型

对象如何协作与响应

- [责任链](behavioral/chain-of-responsibility/README.zh-CN.md) — 让请求沿处理器传递，每个处理器可以停止或继续。 (中级)
- [命令](behavioral/command/README.zh-CN.md) — 把操作封装成可保存、可延后调用的对象。 (中级)
- [解释器](behavioral/interpreter/README.zh-CN.md) — 用对象表示小型语言，并按语法规则求值。 (进阶)
- [迭代器](behavioral/iterator/README.zh-CN.md) — 通过稳定的访问协议遍历集合。 (入门)
- [中介者](behavioral/mediator/README.zh-CN.md) — 把同级对象之间的协调规则集中到专门对象。 (中级)
- [备忘录](behavioral/memento/README.zh-CN.md) — 在不公开快照内部数据的情况下保存和恢复对象状态。 (中级)
- [观察者](behavioral/observer/README.zh-CN.md) — 被关注的状态变化时，通知已订阅的对象。 (入门)
- [状态](behavioral/state/README.zh-CN.md) — 由对象的当前状态决定响应和状态转换。 (中级)
- [策略](behavioral/strategy/README.zh-CN.md) — 给需要算法的对象传入可替换的行为。 (入门)
- [模板方法](behavioral/template-method/README.zh-CN.md) — 固定算法流程，让子类实现部分步骤。 (中级)
- [访问者](behavioral/visitor/README.zh-CN.md) — 通过独立访问者，为稳定的元素类型集合增加操作。 (进阶)

## 先理解问题， 再引入抽象。

模式是应对重复问题的可复用设计思路，不是到处照搬的类图。先写简单代码，等真实变化需要时再引入结构。

1. **认识问题** — 具体示例说明设计为何存在。
2. **检查简单方案** — 找出真正造成阻力的耦合或重复。
3. **跟踪设计** — 理解职责、所有权和权衡。
4. **运行并修改 C++** — 对照输出，完成练习，测试边界。

## 仓库资源

- [参考资料](REFERENCES.md)
- [参与贡献](CONTRIBUTING.md)
- [许可证](LICENSE)
- [C++20](CPP_EXAMPLES.md)
