# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

متقدم

## In One Sentence

ضيف عمليات على أنواع عناصر ثابتة عن طريق Visitor منفصلة.

## The Problem

السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل class.

## Naive Solution

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## Why It Becomes a Problem

إضافة virtual Method لكل عملية بتطلب تعديل كل عناصر السلة مع كل مهمة جديدة.

## The Idea

كل Item فعلية بتنادي Visitor::visit المناسبة لنوعها من accept ، و Tax بتنّفذ العملية لكل نوع.

## Real-World Analogy

مفتش بيزور محطات ورشة، ولكل نوع محطة قائمة فحص مناسبة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## Participants

Item بتحدد accept ، Book و Food بيختاروا الـ Overload ، Visitor بتسرد الأنواع، Tax بتجمع النتيجة، والسلة بتمتلك العناصر.

الأدوار القياسية في المثال ده:

- [`Element`](../../GLOSSARY.md#element) — عقد الـ objects اللي بتقبل Visitor. هنا: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — implementation لـ Element بتختار Visitor overload المناسبة لنوعها. هنا: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — implementation لـ Visitor فيها عملية لكل نوع Element مدعوم. هنا: `Tax`.

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

استخدمه لما أنواع العناصر ثابتة والعمليات الجديدة كتير.

### Use cases

مناسب لتحليل AST وتصدير المستندات مع عيلة عقد ثابتة؛ std::variant مع std::visit بديل لمجموعة أنواع مقفولة.

## When NOT to Use

بلاش لو الأنواع الجديدة بتزيد باستمرار أو كشف تفاصيلها هيكسر الـ [`encapsulation`](../../GLOSSARY.md#encapsulation) (بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة).

## Advantages

تضيف عملية في Visitor من غير تعديل classes العناصر الموجودة.

## Trade-offs

إضافة نوع عنصر بتطلب تعديل [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها) Visitor وكل الزوار. نسب الضريبة هنا للتوضيح مش قواعد حقيقية، والتقريب محتاج سياسة من المجال.

## Related Patterns

[Composite](../../structural/composite/README.ar-EG.md) · [Iterator](../iterator/README.ar-EG.md)

## Common Confusion

Iterator بتلف على المجموعة، Visitor بتختار العملية حسب النوع، وComposite ممكن توفر الشجرة.

## Terms to Remember

- `Visitor` — ضيف عمليات على أنواع عناصر ثابتة عن طريق Visitor منفصلة.
- `Element` — عقد الـ objects اللي بتقبل Visitor. مثال: `Item`.
- `Concrete Element` — implementation لـ Element بتختار Visitor overload المناسبة لنوعها. مثال: `Book, Food`.
- `Concrete Visitor` — implementation لـ Visitor فيها عملية لكل نوع Element مدعوم. مثال: `Tax`.

## Interview Vocabulary

- [`double dispatch`](../../GLOSSARY.md#double-dispatch) — اختيار behavior بناءً على نوعين وقت runtime؛ Visitor التقليدية بتجمع نداءين virtual مع overload resolution.
- [`overload resolution`](../../GLOSSARY.md#overload-resolution) — اختيار function من كذا واحدة بنفس الاسم حسب أنواع المعاملات وقت compile time.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — استهدف open for extension, closed for modification عند حدود مفيدة ومختارة بوضوح.

## Interview Question

ليه visitor.visit(*this) جوه Book تختار Overload الكتب، و Item reference لوحدها مش كفاية؟

## Mini Challenge

ضيف Label Visitor من غير تعديل Book أو Food ، وبعدها ضيف نوع ثالث وعدّ التغييرات.

## Quick Summary

- **المشكلة:** السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل class.
- **الحل:** كل Item فعلية بتنادي Visitor::visit المناسبة لنوعها من accept ، و Tax بتنّفذ العملية لكل نوع.
- **Trade-off:** إضافة نوع عنصر بتطلب تعديل interface Visitor وكل الزوار. نسب الضريبة هنا للتوضيح مش قواعد حقيقية، والتقريب محتاج سياسة من المجال.
- **افتكر:** أنواع ثابتة، عمليات جديدة.

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)
