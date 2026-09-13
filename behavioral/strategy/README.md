# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Use different Algorithms for the same job.

## The problem

Checkout totals need different shipping policies without mixing every policy into checkout logic. One conditional is readable; repeated policy branches across checkout paths make adding and testing rules harder.

## The idea

Checkout can calculate standard or express shipping. Strategy gives Checkout a shipping rule to call, so the total calculation does not contain every rule. Checkout owns a ShippingRule callable and asks it for the fee. The caller selects the rule at construction.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Strategy example map](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

Checkout is the context, ShippingRule the behavioral contract, and lambdas implement standard and express fees. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Checkout is the context, ShippingRule the behavioral contract, and lambdas implement standard and express fees.

Canonical roles in this example:

- [`Context`](../../GLOSSARY.md#context) — The object that uses a Strategy or delegates behavior to its current State. Here: `Checkout`.
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — The contract for interchangeable algorithms used by a Context. Here: `ShippingRule`.
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — A particular implementation of a Strategy interface, possibly a callable rather than a class. Here: `standard / express lambdas`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Checkout:
    def __init__(self, shipping_rule):
        self.shipping_rule = shipping_rule

    def total(self, subtotal_cents):
        if subtotal_cents < 0:
            raise ValueError("Negative subtotal")
        return subtotal_cents + self.shipping_rule(subtotal_cents)


def standard(subtotal_cents):
    return 500


def express(subtotal_cents):
    return 0 if subtotal_cents >= 10000 else 1500


def main():
    print("Standard:", Checkout(standard).total(4000))
    print("Express:", Checkout(express).total(4000))
    print("Express boundary:", Checkout(express).total(10000))
    try:
        Checkout(standard).total(-1)
    except ValueError:
        print("Negative subtotal rejected")


if __name__ == "__main__":
    main()
```

### Python output

```text
Standard: 4500
Express: 5500
Express boundary: 10000
Negative subtotal rejected
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal_cents) const {
        if (subtotal_cents < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal_cents + shipping_(subtotal_cents);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal_cents) { return subtotal_cents >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
    std::cout << "Express boundary: " << express.total(100) << '\n';
    try { static_cast<void>(standard.total(-1)); }
    catch (const std::invalid_argument&) { std::cout << "Negative subtotal rejected\n"; }
    try { const Checkout missing{ShippingRule{}}; }
    catch (const std::invalid_argument&) { std::cout << "Missing rule rejected\n"; }
}
```

### C++20 output

```text
Standard: 45
Express: 55
Express large: 120
Express boundary: 100
Negative subtotal rejected
Missing rule rejected
```

## Compare the languages

A Python function is the Concrete Strategy. C++ stores the same kind of callable in `std::function`; a template policy can instead select it at Compile time. Both examples choose the rule when constructing Checkout. Amounts are integer cents.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when algorithms vary independently and callers need to select a policy.

### Use cases

Pricing rules, ranking functions and retry policies are appropriate design contexts.

**Cost:** [`std::function`](../../GLOSSARY.md#stdfunction) adds [`type erasure`](../../GLOSSARY.md#type-erasure) and may allocate; templates or a function pointer can be better with different constraints. Validate policy results if external code can return invalid fees.

## Check yourself

1. Can this Checkout change its rule after construction through its public API?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add free shipping for subtotals of at least 80 and test 79, 80 and 81.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
