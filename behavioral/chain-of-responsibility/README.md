# Chain of Responsibility

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Pass a request through Handlers that can stop or continue.

## The problem

A request must pass authentication and spending checks, and different entry points need different policies. One expression is fine initially; duplicating and editing it for several pipelines makes policy order and reuse difficult.

## The idea

A request must pass authentication and an amount limit. Each Handler owns one check; the caller chooses the chain order. Each Handler runs its own check and delegates only on success; the final successful handler accepts.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Chain of Responsibility example map](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

Handler owns its successor. Auth checks identity, Limit checks amount. The client chooses the chain order. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Handler owns its successor. Auth checks identity, Limit checks amount. The client chooses the chain order.

Canonical roles in this example:

- [`Handler`](../../GLOSSARY.md#handler) — A role that handles a request or passes it to its successor. Here: `Handler`.
- [`Concrete Handler`](../../GLOSSARY.md#concrete-handler) — A Handler implementing one particular processing rule. Here: `Auth, Limit`.
- [`chain termination`](../../GLOSSARY.md#chain-termination) — The rule for stopping a chain and deciding what happens after the last handler. Here: `Handler::handle`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Request:
    def __init__(self, authenticated, amount_cents):
        self.authenticated = authenticated
        self.amount_cents = amount_cents


class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def accepts(self, request):
        raise NotImplementedError

    def handle(self, request):
        if not self.accepts(request):
            return False
        if self.next_handler is None:
            return True
        return self.next_handler.handle(request)


class Auth(Handler):
    def accepts(self, request):
        return request.authenticated


class Limit(Handler):
    def accepts(self, request):
        return 0 < request.amount_cents <= 10000


if __name__ == "__main__":
    chain = Auth(Limit())
    for authenticated, amount_cents in [(False, 2000), (True, 20000),
                                       (True, 2000), (True, 0), (True, 10000)]:
        request = Request(authenticated, amount_cents)
        print("Accepted" if chain.handle(request) else "Rejected")
```

### Python output

```text
Rejected
Rejected
Accepted
Rejected
Accepted
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount_cents; };
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
    bool accepts(const Request& request) const override { return request.amount_cents > 0 && request.amount_cents <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

### C++20 output

```text
Rejected
Rejected
Accepted
```

## Compare the languages

Both versions use a validation chain: each Handler may reject, or pass onward; reaching the end means success. Other chains stop at the first Handler that can fulfill a request. Python holds successor references; C++ owns them with `unique_ptr`.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when request handling order or membership must be composed independently.

### Use cases

Validation pipelines and request middleware fit. This variant requires every handler to approve, rather than stopping at the first successful handler.

**Cost:** Order affects behavior. A chain needs an explicit end policy; this example accepts after all checks, while other chains may reject unhandled requests.

## Check yourself

1. What does reaching the end of this chain mean, and when does a check stop it?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a maintenance-mode handler and verify that rejected requests never reach later checks.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
