# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/state/README.md) · [Category](../README.md) · [Next](../../behavioral/template-method/README.md)

## Category

Behavioral

## Difficulty

Beginner

## In One Sentence

Supply an interchangeable algorithm to the object that needs it.

## The Problem

Checkout totals need different shipping policies without mixing every policy into checkout logic.

## A Naive Solution

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## Why This Becomes a Problem

One conditional is readable; repeated policy branches across checkout paths make adding and testing rules harder.

## The Idea

Checkout owns a ShippingRule callable and asks it for the fee. The caller selects the rule at construction.

## Real-World Analogy

Choose a route planner for walking or driving while the destination stays the same.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Participants

Checkout is the context, ShippingRule the behavioral contract, and lambdas implement standard and express fees.

## Modern C++20 Example

```cpp
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
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
```

## When to Use It

Use it when algorithms vary independently and callers need to select a policy.

## When NOT to Use It

Avoid it for one stable algorithm or a single readable conditional that has no real extension pressure.

## Advantages

Each policy can be tested independently while total calculation stays shared.

## Disadvantages / Trade-offs

std::function adds type erasure and may allocate; templates or a function pointer can be better with different constraints. Validate policy results if external code can return invalid fees.

## Technical Use Cases

Pricing rules, ranking functions and retry policies are appropriate design contexts.

## Related Patterns

[state](../state/README.md) · [template-method](../template-method/README.md)

## Common Confusion

State represents lifecycle and transitions; Strategy chooses an algorithm. Template Method customizes inherited steps rather than an injected callable.

## Interview Question

How would replacing std::function with a template parameter affect runtime selection and compilation?

## Mini Challenge

Add free shipping for subtotals of at least 80 and test 79, 80 and 81.

## Quick Summary

- **Problem:** Checkout totals need different shipping policies without mixing every policy into checkout logic.
- **Solution:** Checkout owns a ShippingRule callable and asks it for the fee. The caller selects the rule at construction.
- **Trade-off:** std::function adds type erasure and may allocate; templates or a function pointer can be better with different constraints. Validate policy results if external code can return invalid fees.
- **Remember:** Same task, choose the algorithm.

[Previous](../../behavioral/state/README.md) · [Category](../README.md) · [Next](../../behavioral/template-method/README.md)
