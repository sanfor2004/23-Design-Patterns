![Sanfor2004](assets/brand/logo.svg)

# 23 Design Patterns

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

通过一个小程序追踪具体问题，比只记住模式名称更容易理解设计。这里把动机、代码、输出和权衡放在一起，帮助你判断额外的 abstraction 是否值得。

## 如何阅读

从下面的分类或学习路径开始。每个模式目录包含四种语言的说明、结构图和 `cpp/` 目录。语言链接会打开同一模式的对应译文。

## Creational Pattern

 object 如何创建

- [Abstract Factory](creational/abstract-factory/README.zh-CN.md) — 通过统一的工厂 interface 创建相互配套的 object。 (中级)
- [Builder](creational/builder/README.zh-CN.md) — 用具名步骤配置 object，最后一次性生成结果。 (入门)
- [Factory Method](creational/factory-method/README.zh-CN.md) — 让 subclass 决定公共流程所使用的 concrete object。 (入门)
- [Prototype](creational/prototype/README.zh-CN.md) — 复制一个配置好的 object，得到独立的新 object。 (中级)
- [Singleton](creational/singleton/README.zh-CN.md) — 限制 type 只提供一个 instance，同时承担全局共享 state 的代价。 (中级)

## Structural Pattern

 object 如何组合

- [Adapter](structural/adapter/README.zh-CN.md) — 把已有 interface 转换成 Client 期待的 interface。 (入门)
- [Bridge](structural/bridge/README.zh-CN.md) — 把两个变化维度分开，再用 composition 连接。 (中级)
- [Composite](structural/composite/README.zh-CN.md) — 让单个叶子和 object 树提供同一种操作。 (入门)
- [Decorator](structural/decorator/README.zh-CN.md) — 用实现相同 interface 的包装 object 叠加 behavior。 (入门)
- [Facade](structural/facade/README.zh-CN.md) — 为 subsystem 的常见流程提供一个小而清晰的入口。 (入门)
- [Flyweight](structural/flyweight/README.zh-CN.md) — 共享不可变的内部数据，把每次使用的 Context 留在外部。 (进阶)
- [Proxy](structural/proxy/README.zh-CN.md) — 通过相同 interface 的替身控制对真实 object 的访问。 (中级)

## Behavioral Pattern

 object 如何协作与响应

- [Chain of Responsibility](behavioral/chain-of-responsibility/README.zh-CN.md) — 让请求沿 Handler 传递，每个 Handler 可以停止或继续。 (中级)
- [Command](behavioral/command/README.zh-CN.md) — 把操作 encapsulation 成可保存、可延后调用的 object。 (中级)
- [Interpreter](behavioral/interpreter/README.zh-CN.md) — 用 object 表示小型语言，并按 grammar 规则 求值（evaluation）。 (进阶)
- [Iterator](behavioral/iterator/README.zh-CN.md) — 通过稳定的访问协议遍历集合。 (入门)
- [Mediator](behavioral/mediator/README.zh-CN.md) — 把同级 object 之间的协调规则集中到专门 object。 (中级)
- [Memento](behavioral/memento/README.zh-CN.md) — 在不 暴露 snapshot 内部数据 的情况下保存和恢复 object state。 (中级)
- [Observer](behavioral/observer/README.zh-CN.md) — 被关注的 state 变化时，通知已订阅的 object。 (入门)
- [State](behavioral/state/README.zh-CN.md) — 由 object 的当前 state 决定响应和 state transition。 (中级)
- [Strategy](behavioral/strategy/README.zh-CN.md) — 给需要 algorithm 的 object 传入可替换的 behavior。 (入门)
- [Template Method](behavioral/template-method/README.zh-CN.md) — 固定 algorithm 流程，让 subclass 实现部分步骤。 (中级)
- [Visitor](behavioral/visitor/README.zh-CN.md) — 通过独立 Visitor，为稳定的 Element type 集合增加操作。 (进阶)

## 先理解问题， 再引入 abstraction。

模式是应对重复问题的可复用设计思路，不是到处照搬的 class diagram。先写简单代码，等真实变化需要时再引入结构。

1. **认识问题** — 具体示例说明设计为何存在。
2. **检查简单方案** — 找出真正造成阻力的 coupling 或重复。
3. **跟踪设计** — 理解 responsibility、 ownership 和权衡。
4. **运行并修改 C++** — 对照输出，完成练习，测试边界。

## 仓库资源

- [参考资料](REFERENCES.md)
- [参与贡献](CONTRIBUTING.md)
- [许可证](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

翻译解释，而不替换术语。Pattern 名称、技术术语、代码标识符和面试表达保留英文，并用中文解释含义。

[Glossary — 术语说明](GLOSSARY.md)
