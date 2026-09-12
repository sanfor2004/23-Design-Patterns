# Comparisons

[Pattern catalog](README.md)

Similar shapes can solve different problems. Choose by intent, by what changes, and by where the responsibility belongs.


## Strategy ↔ State

### Core problem

Both delegate behavior, but Strategy addresses algorithm choice and State addresses lifecycle-dependent responses.

### Structural difference

Strategy is normally supplied by the caller. A State can initiate a context transition after an event.

### Common use case

Select a shipping fee rule with Strategy; model a door moving between open, closed and locked with State.

### Decision rule

Ask what causes the change: a chosen policy suggests Strategy; a domain event that changes lifecycle suggests State.

### Small design example

Checkout → selected ShippingRule; Door → current DoorState → next DoorState.

[Strategy](behavioral/strategy/README.md) · [State](behavioral/state/README.md)

### Memory trick

Strategy chooses how; State explains how behavior changes with lifecycle.

## Adapter ↔ Facade

### Core problem

Adapter solves an interface mismatch; Facade reduces the work needed to use a subsystem.

### Structural difference

Adapter implements a required target contract around an existing API. Facade offers a smaller workflow API over several services.

### Common use case

Convert Fahrenheit to a Celsius interface with Adapter; expose checkout over stock, payment and shipping with Facade.

### Decision rule

Need compatibility with a specific contract? Adapter. Need a simpler entry point? Facade. A facade may internally use adapters.

### Small design example

Temperature ← CelsiusAdapter → LegacyThermometer; Client → Checkout → services.

[Adapter](structural/adapter/README.md) · [Facade](structural/facade/README.md)

### Memory trick

Adapter translates a contract; Facade simplifies a workflow.

## Decorator ↔ Proxy

### Core problem

Decorator adds responsibilities; Proxy controls access to a subject.

### Structural difference

Both may implement the same interface and delegate to a wrapped object. Intent distinguishes them more reliably than shape.

### Common use case

Add milk pricing or compression with Decorator; defer image loading or check access with Proxy.

### Decision rule

Ask whether the wrapper adds an optional capability or governs reaching the underlying object. Some wrappers serve both purposes.

### Small design example

Milk(Drink) adds price; LazyImage(Image) decides when DiskImage exists.

[Decorator](structural/decorator/README.md) · [Proxy](structural/proxy/README.md)

### Memory trick

Decorator adds a capability; Proxy governs access.

## Factory Method ↔ Abstract Factory

### Core problem

Factory Method varies a creation step; Abstract Factory supplies a coherent family of different product types.

### Structural difference

Factory Method is an overridable operation in a creator workflow. Abstract Factory is an object exposing creation operations for related products.

### Common use case

Choose a sender inside AlertJob with Factory Method; create matching Button and Panel products with Abstract Factory.

### Decision rule

If the extension point is one workflow's product creation, use Factory Method. If clients need a whole interchangeable family, consider Abstract Factory.

### Small design example

AlertJob::run → make_sender(); render → Theme.button() + Theme.panel().

[Factory Method](creational/factory-method/README.md) · [Abstract Factory](creational/abstract-factory/README.md)

### Memory trick

Factory Method varies a creation step; Abstract Factory supplies a matching family.

## Builder ↔ Factory Method

### Core problem

Builder addresses complex configuration; Factory Method addresses which concrete product a workflow creates.

### Structural difference

Builder collects state across named calls then returns a result. Factory Method selects a product through an overridden creation operation.

### Common use case

Build a request with timeout and retry options; choose a sender for a shared alert workflow.

### Decision rule

Many construction choices suggest Builder. A subclass-controlled product choice suggests Factory Method. Neither is required for a simple constructor.

### Small design example

RequestBuilder.endpoint(...).timeout(...).build(); EmailJob overrides make_sender().

[Builder](creational/builder/README.md) · [Factory Method](creational/factory-method/README.md)

### Memory trick

Builder configures step by step; Factory Method lets a subclass choose a product.

## Observer ↔ Mediator

### Core problem

Observer distributes change notifications; Mediator organizes interactions among colleagues.

### Structural difference

Observer manages subscriptions without encoding each subscriber's workflow. Mediator knows the coordination rule and often particular colleague roles.

### Common use case

Broadcast stock changes to views; coordinate form fields and submit-button availability.

### Decision rule

Independent reactions to a published event suggest Observer. A rule connecting several peers suggests Mediator. A mediator can receive observer notifications.

### Small design example

Stock → listeners; Field → LoginForm → Button.

[Observer](behavioral/observer/README.md) · [Mediator](behavioral/mediator/README.md)

### Memory trick

Observer announces a change; Mediator coordinates a rule.

## Template Method ↔ Strategy

### Core problem

Both reuse a workflow while varying behavior, but they place the variation in different relationships.

### Structural difference

Template Method calls subclass hooks from a fixed inherited skeleton. Strategy delegates to a supplied collaborator or callable.

### Common use case

Keep report begin/read/format/end order through hooks; swap a shipping rule through a callable.

### Decision rule

Choose Template Method for a stable inheritance extension protocol. Prefer Strategy when behavior should be supplied independently of the context's type.

### Small design example

Report::generate → virtual format(); Checkout::total → ShippingRule.

[Template Method](behavioral/template-method/README.md) · [Strategy](behavioral/strategy/README.md)

### Memory trick

Template Method inherits the sequence; Strategy receives the behavior.

## Composite ↔ Decorator

### Core problem

Composite models a part-whole hierarchy; Decorator adds behavior to an individual component.

### Structural difference

A composite generally owns several children and aggregates an operation. A decorator wraps one component and augments delegation.

### Common use case

Sum a folder's nested file sizes with Composite; add milk pricing around a Drink with Decorator.

### Decision rule

Need a group that acts like a leaf? Composite. Need optional layers around one object? Decorator. A decorator may also wrap a composite.

### Small design example

Folder[File, Folder[File]]; Milk(Milk(Coffee)).

[Composite](structural/composite/README.md) · [Decorator](structural/decorator/README.md)

### Memory trick

Composite groups children; Decorator layers one component.
