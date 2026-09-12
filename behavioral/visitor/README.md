# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[Previous](../../behavioral/template-method/README.md) · [Category](../README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — A Design Pattern concerned with behavior and collaboration among objects.

## Difficulty

Advanced

## In One Sentence

Add operations across a stable set of element types using a separate visitor.

## The Problem

A basket contains books and food, and new operations such as tax or export should not fill every item class.

## Naive Solution

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## Why It Becomes a Problem

Adding every operation as another virtual Item method requires editing all item classes for each new task.

## The Idea

Each concrete Item calls the matching Visitor::visit overload from accept; Tax implements the operation for each type.

## Real-World Analogy

An inspector visits different workshop stations and applies a station-specific checklist.

## Structure

[Diagram](diagram.md) · [Run the example](cpp/README.md)

![Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## Participants

Item defines accept. Book and Food select their typed overload. Visitor lists supported types. Tax accumulates the result; the basket owns items.

Canonical roles in this example:

- [`Element`](../../GLOSSARY.md#element) — The contract for objects that accept a Visitor. Here: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — An Element implementation that selects its matching Visitor overload. Here: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — A Visitor implementation containing one operation for every supported Element type. Here: `Tax`.

## Modern C++20 Example

```cpp
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
    int price = 20;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Food final : Item {
    int price = 10;
    void accept(Visitor& visitor) const override { visitor.visit(*this); }
};
struct Tax final : Visitor {
    int total = 0;
    void visit(const Book& book) override { total += book.price / 10; }
    void visit(const Food& food) override { total += food.price / 5; }
};
int main() {
    std::vector<std::unique_ptr<Item>> basket;
    basket.push_back(std::make_unique<Book>());
    basket.push_back(std::make_unique<Food>());
    Tax tax;
    for (const auto& item : basket) item->accept(tax);
    std::cout << "Tax: " << tax.total << '\n';
}
```

## Example Output

```text
Tax: 4
```

## When to Use

Use it when element types are stable but new operations are frequent.

### Use cases

AST analyses and document exports fit a stable node family; std::variant with std::visit is another option for closed type sets.

## When NOT to Use

Avoid it when new element types are frequent or exposing their details would break [`encapsulation`](../../GLOSSARY.md#encapsulation) (Keeping representation and invariants behind controlled operations).

## Advantages

A new operation can be added in a visitor without changing existing element classes.

## Trade-offs

Adding an element type requires updating the Visitor [`interface`](../../GLOSSARY.md#interface) (The contract of operations and observable behavior offered to a caller) and all visitors. Integer tax rates here are illustrative, not real tax rules; rounding needs a domain policy.

## Related Patterns

[Composite](../../structural/composite/README.md) · [Iterator](../iterator/README.md)

## Common Confusion

Iterator traverses a collection; Visitor dispatches an operation by element type. Composite can supply the tree on which visitors work.

## Terms to Remember

- `Visitor` — Add operations across a stable set of element types using a separate visitor.
- `Element` — The contract for objects that accept a Visitor. Example: `Item`.
- `Concrete Element` — An Element implementation that selects its matching Visitor overload. Example: `Book, Food`.
- `Concrete Visitor` — A Visitor implementation containing one operation for every supported Element type. Example: `Tax`.

## Interview Vocabulary

- [`double dispatch`](../../GLOSSARY.md#double-dispatch) — Selecting behavior using two runtime types; classic Visitor combines two virtual calls with overload resolution.
- [`overload resolution`](../../GLOSSARY.md#overload-resolution) — Compile-time selection among functions with the same name using the argument types.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — Aim for open for extension, closed for modification at a useful, chosen boundary.

## Interview Question

Why does visitor.visit(*this) inside Book select the Book overload, while an Item reference alone would not?

## Mini Challenge

Add a Label visitor without modifying Book or Food, then add a third item type and count the changes.

## Quick Summary

- **Problem:** A basket contains books and food, and new operations such as tax or export should not fill every item class.
- **Solution:** Each concrete Item calls the matching Visitor::visit overload from accept; Tax implements the operation for each type.
- **Trade-off:** Adding an element type requires updating the Visitor interface and all visitors. Integer tax rates here are illustrative, not real tax rules; rounding needs a domain policy.
- **Remember:** Stable types, new operations.

[Previous](../../behavioral/template-method/README.md) · [Category](../README.md)
