# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Give a complex subsystem one simple entry point.

## The problem

Every checkout caller must check stock, charge payment and request shipping in the right order. Direct calls let callers forget stock checks or duplicate orchestration inconsistently.

## The idea

Checkout needs stock, payment, and shipping in order. Facade puts that common sequence behind one call; it does not automatically make the steps a transaction. Checkout exposes buy and coordinates its internal services behind that operation.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Facade example map](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

Stock checks availability, Payment charges, Shipping dispatches, and Checkout presents the common workflow. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Stock checks availability, Payment charges, Shipping dispatches, and Checkout presents the common workflow.

Canonical roles in this example:

- [`subsystem`](../../GLOSSARY.md#subsystem) — A group of cooperating services or objects within a larger system. Here: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — The contract of operations and observable behavior offered to a caller. Here: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — Code that uses an interface or collaborates with a pattern's objects. Here: `main`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Stock:
    def available(self, quantity):
        return 0 < quantity <= 3


class Payment:
    def charge(self, amount_cents):
        print("Charged", amount_cents, "cents")


class Shipping:
    def dispatch(self):
        print("Dispatched")


class Checkout:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.shipping = Shipping()

    def buy(self, quantity):
        if not self.stock.available(quantity):
            return False
        self.payment.charge(quantity * 1000)
        self.shipping.dispatch()
        return True


if __name__ == "__main__":
    checkout = Checkout()
    checkout.buy(2)
    if not checkout.buy(4):
        print("Unavailable")
    if not checkout.buy(0):
        print("Invalid quantity")
```

### Python output

```text
Charged 2000 cents
Dispatched
Unavailable
Invalid quantity
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount_cents) const { std::cout << "Charged " << amount_cents << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

### C++20 output

```text
Charged 20
Dispatched
Unavailable
```

## Compare the languages

Both versions put the same small workflow behind `buy`. C++ stores service Objects by value; Python holds references. Neither example implements a transaction: a real shipping failure after payment needs an explicit recovery policy.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when many callers need the same useful subset of a complicated subsystem.

### Use cases

SDK entry points and application service boundaries fit; the example has no real payment integration.

**Cost:** The facade can grow into a god object. This example is not transactional: real payment and shipping failures require compensation or another consistency strategy.

## Check yourself

1. What does buy fail to guarantee if shipping fails after payment?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a simulated shipping failure and design an explicit refund result rather than silently returning success.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
