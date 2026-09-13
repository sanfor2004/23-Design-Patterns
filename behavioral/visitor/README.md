# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Add operations outside a stable set of element types.

## The problem

A basket contains books and food, and new operations such as tax or export should not fill every item class. Adding every operation as another virtual Item method requires editing all item classes for each new task.

## The idea

Books and food need different tax calculations. Visitor keeps those calculations together, while each item calls the method for its own type. Each concrete Item calls the matching Visitor::visit overload from accept; Tax implements the operation for each type.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Visitor example map](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

Item defines accept. Book and Food select their typed overload. Visitor lists supported types. Tax accumulates the result; the basket owns items. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Item defines accept. Book and Food select their typed overload. Visitor lists supported types. Tax accumulates the result; the basket owns items.

Canonical roles in this example:

- [`Element`](../../GLOSSARY.md#element) — The contract for objects that accept a Visitor. Here: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — An Element implementation that selects its matching Visitor overload. Here: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — A Visitor implementation containing one operation for every supported Element type. Here: `Tax`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Book:
    def __init__(self, price_cents):
        self.price_cents = price_cents

    def accept(self, visitor):
        visitor.visit_book(self)


class Food:
    def __init__(self, price_cents):
        self.price_cents = price_cents

    def accept(self, visitor):
        visitor.visit_food(self)


class Tax:
    def __init__(self):
        self.total_cents = 0

    def visit_book(self, book):
        self.total_cents += book.price_cents // 10

    def visit_food(self, food):
        self.total_cents += food.price_cents // 5


def tax_cents(basket):
    tax = Tax()
    for item in basket:
        item.accept(tax)
    return tax.total_cents


if __name__ == "__main__":
    print("Tax:", tax_cents([Book(2000), Food(1000)]), "cents")
    print("Empty basket tax:", tax_cents([]), "cents")
```

### Python output

```text
Tax: 400 cents
Empty basket tax: 0 cents
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <vector>

struct Book;
struct Food;
struct Visitor {
    virtual ~Visitor() = default;
    virtual void visit(const Book& book) = 0;
    virtual void visit(const Food& food) = 0;
};
struct Item {
    virtual ~Item() = default;
    virtual void accept(Visitor& visitor) const = 0;
};
struct Book final : Item {
    int price_cents = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Food final : Item {
    int price_cents = 10;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Tax final : Visitor {
    int total_cents = 0;
    void visit(const Book& book) override { total_cents += book.price_cents / 10; }
    void visit(const Food& food) override { total_cents += food.price_cents / 5; }
};
int main() {
    std::vector<std::unique_ptr<Item>> basket;
    basket.push_back(std::make_unique<Book>());
    basket.push_back(std::make_unique<Food>());
    Tax tax;
    for (const auto& item : basket) item->accept(tax);
    std::cout << "Tax: " << tax.total_cents << '\n';
}
```

### C++20 output

```text
Tax: 4
```

## Compare the languages

Python uses separate `visit_book` and `visit_food` methods because it does not overload methods by parameter type. C++ uses overloads plus virtual dispatch. Both keep Tax outside the element types. Integer division truncates fractional cents; these sample rates and amounts avoid fractions and are not a tax policy.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it when element types are stable but new operations are frequent.

### Use cases

AST analyses and document exports fit a stable node family; std::variant with std::visit is another option for closed type sets.

**Cost:** Adding an element type requires updating the Visitor [`interface`](../../GLOSSARY.md#interface) and all visitors. Integer tax rates here are illustrative, not real tax rules; rounding needs a domain policy.

## Check yourself

1. What must change when you add a new item type rather than a new operation?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add a Label visitor without modifying Book or Food, then add a third item type and count the changes.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
