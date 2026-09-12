# 关系图

[模式目录](README.zh-CN.md)

这些是可用的关系，不是强制依赖。箭头表示一种设计可能，并不要求同时使用两个模式。

- [抽象工厂](creational/abstract-factory/README.zh-CN.md) → 可用来实现创建操作 → [工厂方法](creational/factory-method/README.zh-CN.md)
- [状态](behavioral/state/README.zh-CN.md) → 委托结构相似 → [策略](behavioral/strategy/README.zh-CN.md)
- [装饰器](structural/decorator/README.zh-CN.md) → 共享递归组件结构 → [组合](structural/composite/README.zh-CN.md)
- [代理](structural/proxy/README.zh-CN.md) → 包装结构可能相似 → [装饰器](structural/decorator/README.zh-CN.md)
- [模板方法](behavioral/template-method/README.zh-CN.md) → 提供基于继承的替代思路 → [策略](behavioral/strategy/README.zh-CN.md)
- [命令](behavioral/command/README.zh-CN.md) → 可借助快照实现撤销 → [备忘录](behavioral/memento/README.zh-CN.md)

- [Observer](behavioral/observer/README.zh-CN.md) ↔ 比较通知与协调 ↔ [Mediator](behavioral/mediator/README.zh-CN.md)

```mermaid
flowchart LR
  AF["Abstract Factory"] -->|"may use creation methods"| FM["Factory Method"]
  ST["Strategy"] ---|"compare intent"| SA["State"]
  DE["Decorator"] ---|"compare wrapper intent"| PR["Proxy"]
  CO["Composite"] ---|"recursive components"| DE
  OB["Observer"] ---|"notification vs coordination"| ME["Mediator"]
  TM["Template Method"] ---|"inheritance vs composition"| ST
  CM["Command"] -->|"may use snapshots for undo"| MM["Memento"]
```
