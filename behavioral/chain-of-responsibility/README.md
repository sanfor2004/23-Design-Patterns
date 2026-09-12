# Chain of Responsibility

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../structural/proxy/README.md) · [Category](../README.md) · [Next](../../behavioral/command/README.md)

## Category

Behavioral

## Difficulty

Intermediate

## In One Sentence

Pass a request along handlers that can stop or continue processing.

## The Problem

A request must pass authentication and spending checks, and different entry points need different policies.

## A Naive Solution

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## Why This Becomes a Problem

One expression is fine initially; duplicating and editing it for several pipelines makes policy order and reuse difficult.

## The Idea

Each Handler runs its own check and delegates only on success; the final successful handler accepts.

## Real-World Analogy

A support desk resolves a request or passes it to the next specialist.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Chain of Responsibility](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## Participants

Handler owns its successor. Auth checks identity, Limit checks amount. The client chooses the chain order.

## Modern C++20 Example

```cpp
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount; };
class Handler {
    std::unique_ptr<Handler> next_;
protected:
    virtual bool accepts(const Request& request) const = 0;
public:
    explicit Handler(std::unique_ptr<Handler> next = {}) : next_(std::move(next)) {}
    virtual ~Handler() = default;
    bool handle(const Request& request) const {
        if (!accepts(request)) return false;
        return next_ ? next_->handle(request) : true;
    }
};
class Auth final : public Handler {
    bool accepts(const Request& request) const override { return request.authenticated; }
public:
    using Handler::Handler;
};
class Limit final : public Handler {
    bool accepts(const Request& request) const override { return request.amount > 0 && request.amount <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

## Example Output

```text
Rejected
Rejected
Accepted
```

## When to Use It

Use it when request handling order or membership must be composed independently.

## When NOT to Use It

Avoid it for two fixed checks in one place; the initial expression is then clearer.

## Advantages

Checks can be reused and reordered without a giant conditional.

## Disadvantages / Trade-offs

Order affects behavior. A chain needs an explicit end policy; this example accepts after all checks, while other chains may reject unhandled requests.

## Technical Use Cases

Validation pipelines and request middleware fit. This variant requires every handler to approve, rather than stopping at the first successful handler.

## Related Patterns

[decorator](../../structural/decorator/README.md) · [command](../command/README.md)

## Common Confusion

Decorator layers behavior around a component; this chain may terminate without reaching later handlers. Command represents the request as an object.

## Interview Question

What happens to an unauthenticated request if Limit is expensive and placed first?

## Mini Challenge

Add a maintenance-mode handler and verify that rejected requests never reach later checks.

## Quick Summary

- **Problem:** A request must pass authentication and spending checks, and different entry points need different policies.
- **Solution:** Each Handler runs its own check and delegates only on success; the final successful handler accepts.
- **Trade-off:** Order affects behavior. A chain needs an explicit end policy; this example accepts after all checks, while other chains may reject unhandled requests.
- **Remember:** Handle it, or pass it on.

[Previous](../../structural/proxy/README.md) · [Category](../README.md) · [Next](../../behavioral/command/README.md)
