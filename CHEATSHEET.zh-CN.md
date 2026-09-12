# 速查表

[模式目录](README.zh-CN.md)

覆盖全部 23 种模式的选择参考。“何时不用”与“何时使用”同样重要。

| 模式目录 | 分类 | 适用场景 | 避免使用 | 记忆提示 |
| --- | --- | --- | --- | --- |
| [Abstract Factory](creational/abstract-factory/README.zh-CN.md) | Creational Pattern | 当多种产品必须一起切换，且 Client 不应决定 concrete type 时使用。 | 只有一种稳定产品，或者产品本来就应该自由组合时，不必使用。 | 一个工厂，一套产品。 |
| [Builder](creational/builder/README.zh-CN.md) | Creational Pattern | 适合独立选项较多，或需要明确构建校验阶段的 object。 | 只有两个直观参数时，普通 constructor 或小型聚合 type 更简单。 | 先选配置，再生成 object。 |
| [Factory Method](creational/factory-method/README.zh-CN.md) | Creational Pattern | 已有 inheritance 体系中的公共流程需要 可扩展（extensibility） 的创建步骤时使用。 | 直接把 Sender 传给 function 就能解决时，不必引入 inheritance 层次。 | 保留流程，重写创建步骤。 |
| [Prototype](creational/prototype/README.zh-CN.md) | Creational Pattern | 已有 runtime object 带有有用配置，且 Client 不应重建 concrete type 时使用。 | 普通值复制已经清晰表达需求时，不必增加克隆 interface。 | 复制配置，不复制身份。 |
| [Singleton](creational/singleton/README.zh-CN.md) | Creational Pattern | 只有唯一 instance 确实是进程级约束，且 lifetime 合适时才考虑。 | 不要为了访问方便而使用；需要隔离测试的普通 dependency 应显式传入 reference。 | instance 唯一，问题未必少。 |
| [Adapter](structural/adapter/README.zh-CN.md) | Structural Pattern | 适合不能或不宜修改的已有 API 边界。 | 双方 interface 都由你控制，统一 interface 更简单时，不必适配。 | 在边界完成转换。 |
| [Bridge](structural/bridge/README.zh-CN.md) | Structural Pattern | 两个变化轴会导致 subclass 组合爆炸时使用。 | 只有一个简单变化维度， function 参数就足够时，不必 Bridge。 | 两个维度，一条连接。 |
| [Composite](structural/composite/README.zh-CN.md) | Structural Pattern | 适合真正的部分—整体树，且叶子与分组都有共同的有效操作。 | 平面列表或带共享父节点、环的图，不宜硬套树形 ownership。 | 整体像单项一样回答。 |
| [Decorator](structural/decorator/README.zh-CN.md) | Structural Pattern | 适合可选、可组合且保持原契约的附加 behavior。 | 如果配料列表加求和已经足够，就别用类层层包装；本例着重展示结构。 | 契约不变，再加一层。 |
| [Facade](structural/facade/README.zh-CN.md) | Structural Pattern | 多个 Client 都需要复杂 subsystem 中同一部分能力时使用。 | 只是毫无简化作用的转发层时，不必使用。 | 多项服务，一个入口。 |
| [Flyweight](structural/flyweight/README.zh-CN.md) | Structural Pattern | 测量确认大量 object 重复持有不可变数据时使用。 | 数据量很小、每个 instance 的数据都可变，或查找成本超过收益时避免。 | 共享形状，位置随身带。 |
| [Proxy](structural/proxy/README.zh-CN.md) | Structural Pattern | 适合延迟初始化、访问检查或远程访问，同时希望保留稳定 interface 的场景。 | 直接创建很便宜， access policy 也没有价值时，不必 Proxy。 | 替身控制真实访问。 |
| [Chain of Responsibility](behavioral/chain-of-responsibility/README.zh-CN.md) | Behavioral Pattern | 处理步骤的顺序或成员需要独立组合时使用。 | 只有一个地方的两个固定检查时，原表达式更清晰。 | 处理，或者传递。 |
| [Command](behavioral/command/README.zh-CN.md) | Behavioral Pattern | 适合延迟操作、队列、宏 Command 或撤销历史。 | 一次性 function 调用无需保存或调度意图时，避免额外 object。 | 把动作保存下来。 |
| [Interpreter](behavioral/interpreter/README.zh-CN.md) | Behavioral Pattern | grammar 小而稳定，且 expression tree 本身有构建和检查价值时使用。 | 大型语言需要健壮解析、诊断和优化时，应考虑成熟解析工具。 | grammar 节点赋予表达式含义。 |
| [Iterator](behavioral/iterator/README.zh-CN.md) | Behavioral Pattern | 优先用标准 iterator 或 ranges 暴露遍历能力而非存储细节。 | 直接返回已有 const_iterator 或标准范围即可时，不必自定义；这里用于教学。 | 遍历数据，不暴露 container 内部。 |
| [Mediator](behavioral/mediator/README.zh-CN.md) | Behavioral Pattern | 多个同级 object 的交互规则开始纠缠时使用。 | 一个简单 callback 就够，或组件间没有实质协调时避免。 | 同级 object 通过协调者协作。 |
| [Memento](behavioral/memento/README.zh-CN.md) | Behavioral Pattern | object 能定义一致 snapshot，且需要检查点时使用。 | state 巨大、资源不可恢复，或逆操作记录更便宜时避免。 | 保存 state，不 public 细节。 |
| [Observer](behavioral/observer/README.zh-CN.md) | Behavioral Pattern | 一个变化对应多个独立注册的消费者时使用。 | 只有一个固定依赖，或需要严格事务一致性时，不宜用简单广播替代。 | 发布变化，让订阅者响应。 |
| [State](behavioral/state/README.zh-CN.md) | Behavioral Pattern | state 相关 behavior 和转换分散在多个操作时使用。 | 简单开关或清晰的小型 enum 转换表，不必换成 class hierarchy。 | event 相同， state 不同，响应不同。 |
| [Strategy](behavioral/strategy/README.zh-CN.md) | Behavioral Pattern | algorithm 独立变化， Client 需要选择 Strategy 时使用。 | 只有一种稳定 algorithm，或单个清晰条件没有扩展压力时，不必 abstraction。 | 任务相同， algorithm 可选。 |
| [Template Method](behavioral/template-method/README.zh-CN.md) | Behavioral Pattern | 稳定流程中有少量明确的 subclass 扩展点时使用。 | 步骤需要 runtime 重排，或 composition 更能清楚表达 dependency 时避免。 | 流程固定，步骤可变。 |
| [Visitor](behavioral/visitor/README.zh-CN.md) | Behavioral Pattern | Element type 稳定，而新操作频繁增加时使用。 | Element type 经常增加，或暴露内部细节会破坏 encapsulation 时避免。 | type 稳定，操作扩展。 |
