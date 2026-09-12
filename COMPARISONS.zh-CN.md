# 模式对比

[模式目录](README.zh-CN.md)

相似结构可能解决不同问题。根据意图、变化方向和 responsibility 归属选择。


## Strategy ↔ State

### 核心问题

两者都委托 behavior； Strategy 处理 algorithm 选择， state 处理 lifetime 中的响应。

### 结构差异

 Strategy 通常由 Client 提供， state 可以在 event 后发起 Context 转换。

### 常见场景

运费规则用 Strategy，门的开启、关闭、锁定用 state。

### 选择规则

变化来自 Strategy 选择，考虑 Strategy；来自改变 lifetime 的领域 event，考虑 state。

### 简短设计示例

Checkout → 所选 ShippingRule；Door → 当前 DoorState → 下一 state。

[Strategy](behavioral/strategy/README.zh-CN.md) · [State](behavioral/state/README.zh-CN.md)

### 记忆提示

 Strategy 选择做法， state 决定当前阶段的 behavior。

## Adapter ↔ Facade

### 核心问题

 Adapter 解决 interface 不匹配， Facade 降低使用 subsystem 的复杂度。

### 结构差异

 Adapter 包装已有 API 并实现目标契约； Facade 在多个服务之上提供较小的流程 interface。

### 常见场景

华氏 interface 转摄氏 interface 用 Adapter；库存、支付、发货统一结账用 Facade。

### 选择规则

需要满足特定契约选 Adapter，需要简化入口选 Facade。 Facade 内部也可使用 Adapter。

### 简短设计示例

Temperature ← CelsiusAdapter → LegacyThermometer；Client → Checkout → 多个服务。

[Adapter](structural/adapter/README.zh-CN.md) · [Facade](structural/facade/README.zh-CN.md)

### 记忆提示

 Adapter 转换 interface， Facade 简化流程。

## Decorator ↔ Proxy

### 核心问题

 Decorator 增加 responsibility， Proxy 控制对目标的访问。

### 结构差异

两者都可能实现相同 interface 并委托包装 object，意图比结构更能区分它们。

### 常见场景

牛奶加价或压缩层用 Decorator，延迟加载图片或检查访问用 Proxy。

### 选择规则

包装层是在增加可选能力，还是管理是否到达目标？有些包装兼有两种目的。

### 简短设计示例

Milk(Drink) 增加价格；LazyImage 决定 DiskImage 何时存在。

[Decorator](structural/decorator/README.zh-CN.md) · [Proxy](structural/proxy/README.zh-CN.md)

### 记忆提示

 Decorator 增加能力， Proxy 控制访问。

## Factory Method ↔ Abstract Factory

### 核心问题

 Factory Method 改变一个创建步骤； Abstract Factory 提供多种配套产品。

### 结构差异

 Factory Method 是创建者流程中的可重写操作； Abstract Factory 是提供相关产品创建操作的 object。

### 常见场景

AlertJob 内选择发送器用 Factory Method；创建配套 Button、Panel 用 Abstract Factory。

### 选择规则

扩展点是流程中的产品创建，选 Factory Method； Client 需要整套可替换产品，考虑 Abstract Factory。

### 简短设计示例

AlertJob::run → make_sender()；render → Theme.button() + Theme.panel()。

[Factory Method](creational/factory-method/README.zh-CN.md) · [Abstract Factory](creational/abstract-factory/README.zh-CN.md)

### 记忆提示

 Factory Method 替换创建步骤， Abstract Factory 提供配套产品。

## Builder ↔ Factory Method

### 核心问题

 Builder 处理复杂配置， Factory Method 处理流程创建哪种 Concrete Product。

### 结构差异

 Builder 通过具名调用收集 state 后生成结果； Factory Method 通过重写创建操作选择产品。

### 常见场景

配置请求的超时和重试用 Builder；为共同通知流程选择发送器用 Factory Method。

### 选择规则

构建选项多，考虑 Builder； subclass 决定产品，考虑 Factory Method。简单 constructor 不需要它们。

### 简短设计示例

RequestBuilder.endpoint(...).timeout(...).build()；EmailJob 重写 make_sender()。

[Builder](creational/builder/README.zh-CN.md) · [Factory Method](creational/factory-method/README.zh-CN.md)

### 记忆提示

 Builder 分步配置， Factory Method 由 subclass 选择产品。

## Observer ↔ Mediator

### 核心问题

 Observer 分发变化通知， Mediator 组织同级 object 的交互。

### 结构差异

 Observer 管理订阅，不编码每个订阅者的流程； Mediator 了解协调规则和特定 object 角色。

### 常见场景

库存变化广播给视图用 Observer；表单字段共同控制提交按钮用 Mediator。

### 选择规则

对 event 各自独立响应，考虑 Observer；一条规则连接多个同级 object，考虑 Mediator。 Mediator 也可接收 Observer 通知。

### 简短设计示例

Stock → 监听者；Field → LoginForm → Button。

[Observer](behavioral/observer/README.zh-CN.md) · [Mediator](behavioral/mediator/README.zh-CN.md)

### 记忆提示

 Observer 发布变化， Mediator 协调交互规则。

## Template Method ↔ Strategy

### 核心问题

两者都复用流程并改变 behavior，但变化位于不同关系中。

### 结构差异

 Template Method 在固定 inheritance 骨架内调用 subclass 钩子； Strategy 委托给传入的协作者或 callable。

### 常见场景

报告首尾顺序和格式化用钩子；运费规则用可替换 function。

### 选择规则

稳定的 inheritance 扩展协议可选 Template Method； behavior 要独立于 Context type 提供，优先 Strategy。

### 简短设计示例

Report::generate → virtual format()；Checkout::total → ShippingRule。

[Template Method](behavioral/template-method/README.zh-CN.md) · [Strategy](behavioral/strategy/README.zh-CN.md)

### 记忆提示

 Template Method inheritance 流程骨架， Strategy 接收可替换 behavior。

## Composite ↔ Decorator

### 核心问题

组合表示部分与整体， Decorator 给单个组件增加 behavior。

### 结构差异

组合通常拥有多个子节点并汇总操作； Decorator 包装一个组件并增强委托。

### 常见场景

嵌套目录大小求和用组合，给饮品添加牛奶价格用 Decorator。

### 选择规则

分组要像叶子一样使用，选组合；一个 object 需要可选层，选 Decorator。 Decorator 也可以包装组合 object。

### 简短设计示例

Folder[File, Folder[File]]；Milk(Milk(Coffee))。

[Composite](structural/composite/README.zh-CN.md) · [Decorator](structural/decorator/README.zh-CN.md)

### 记忆提示

组合汇集子节点， Decorator 为单个组件叠加 behavior。
