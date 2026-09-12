# 模式对比

[模式目录](README.zh-CN.md)

相似结构可能解决不同问题。根据意图、变化方向和职责归属选择。


## 策略 ↔ 状态

### 核心问题

两者都委托行为；策略处理算法选择，状态处理生命周期中的响应。

### 结构差异

策略通常由调用方提供，状态可以在事件后发起上下文转换。

### 常见场景

运费规则用策略，门的开启、关闭、锁定用状态。

### 选择规则

变化来自策略选择，考虑策略；来自改变生命周期的领域事件，考虑状态。

### 简短设计示例

Checkout → 所选 ShippingRule；Door → 当前 DoorState → 下一状态。

[策略](behavioral/strategy/README.zh-CN.md) · [状态](behavioral/state/README.zh-CN.md)

### 记忆提示

策略选择做法，状态决定当前阶段的行为。

## 适配器 ↔ 外观

### 核心问题

适配器解决接口不匹配，外观降低使用子系统的复杂度。

### 结构差异

适配器包装已有 API 并实现目标契约；外观在多个服务之上提供较小的流程接口。

### 常见场景

华氏接口转摄氏接口用适配器；库存、支付、发货统一结账用外观。

### 选择规则

需要满足特定契约选适配器，需要简化入口选外观。外观内部也可使用适配器。

### 简短设计示例

Temperature ← CelsiusAdapter → LegacyThermometer；Client → Checkout → 多个服务。

[适配器](structural/adapter/README.zh-CN.md) · [外观](structural/facade/README.zh-CN.md)

### 记忆提示

适配器转换接口，外观简化流程。

## 装饰器 ↔ 代理

### 核心问题

装饰器增加职责，代理控制对目标的访问。

### 结构差异

两者都可能实现相同接口并委托包装对象，意图比结构更能区分它们。

### 常见场景

牛奶加价或压缩层用装饰器，延迟加载图片或检查访问用代理。

### 选择规则

包装层是在增加可选能力，还是管理是否到达目标？有些包装兼有两种目的。

### 简短设计示例

Milk(Drink) 增加价格；LazyImage 决定 DiskImage 何时存在。

[装饰器](structural/decorator/README.zh-CN.md) · [代理](structural/proxy/README.zh-CN.md)

### 记忆提示

装饰器增加能力，代理控制访问。

## 工厂方法 ↔ 抽象工厂

### 核心问题

工厂方法改变一个创建步骤；抽象工厂提供多种配套产品。

### 结构差异

工厂方法是创建者流程中的可重写操作；抽象工厂是提供相关产品创建操作的对象。

### 常见场景

AlertJob 内选择发送器用工厂方法；创建配套 Button、Panel 用抽象工厂。

### 选择规则

扩展点是流程中的产品创建，选工厂方法；调用方需要整套可替换产品，考虑抽象工厂。

### 简短设计示例

AlertJob::run → make_sender()；render → Theme.button() + Theme.panel()。

[工厂方法](creational/factory-method/README.zh-CN.md) · [抽象工厂](creational/abstract-factory/README.zh-CN.md)

### 记忆提示

工厂方法替换创建步骤，抽象工厂提供配套产品。

## 建造者 ↔ 工厂方法

### 核心问题

建造者处理复杂配置，工厂方法处理流程创建哪种具体产品。

### 结构差异

建造者通过具名调用收集状态后生成结果；工厂方法通过重写创建操作选择产品。

### 常见场景

配置请求的超时和重试用建造者；为共同通知流程选择发送器用工厂方法。

### 选择规则

构建选项多，考虑建造者；子类决定产品，考虑工厂方法。简单构造函数不需要它们。

### 简短设计示例

RequestBuilder.endpoint(...).timeout(...).build()；EmailJob 重写 make_sender()。

[建造者](creational/builder/README.zh-CN.md) · [工厂方法](creational/factory-method/README.zh-CN.md)

### 记忆提示

建造者分步配置，工厂方法由子类选择产品。

## 观察者 ↔ 中介者

### 核心问题

观察者分发变化通知，中介者组织同级对象的交互。

### 结构差异

观察者管理订阅，不编码每个订阅者的流程；中介者了解协调规则和特定对象角色。

### 常见场景

库存变化广播给视图用观察者；表单字段共同控制提交按钮用中介者。

### 选择规则

对事件各自独立响应，考虑观察者；一条规则连接多个同级对象，考虑中介者。中介者也可接收观察者通知。

### 简短设计示例

Stock → 监听者；Field → LoginForm → Button。

[观察者](behavioral/observer/README.zh-CN.md) · [中介者](behavioral/mediator/README.zh-CN.md)

### 记忆提示

观察者发布变化，中介者协调交互规则。

## 模板方法 ↔ 策略

### 核心问题

两者都复用流程并改变行为，但变化位于不同关系中。

### 结构差异

模板方法在固定继承骨架内调用子类钩子；策略委托给传入的协作者或可调用对象。

### 常见场景

报告首尾顺序和格式化用钩子；运费规则用可替换函数。

### 选择规则

稳定的继承扩展协议可选模板方法；行为要独立于上下文类型提供，优先策略。

### 简短设计示例

Report::generate → virtual format()；Checkout::total → ShippingRule。

[模板方法](behavioral/template-method/README.zh-CN.md) · [策略](behavioral/strategy/README.zh-CN.md)

### 记忆提示

模板方法继承流程骨架，策略接收可替换行为。

## 组合 ↔ 装饰器

### 核心问题

组合表示部分与整体，装饰器给单个组件增加行为。

### 结构差异

组合通常拥有多个子节点并汇总操作；装饰器包装一个组件并增强委托。

### 常见场景

嵌套目录大小求和用组合，给饮品添加牛奶价格用装饰器。

### 选择规则

分组要像叶子一样使用，选组合；一个对象需要可选层，选装饰器。装饰器也可以包装组合对象。

### 简短设计示例

Folder[File, Folder[File]]；Milk(Milk(Coffee))。

[组合](structural/composite/README.zh-CN.md) · [装饰器](structural/decorator/README.zh-CN.md)

### 记忆提示

组合汇集子节点，装饰器为单个组件叠加行为。
