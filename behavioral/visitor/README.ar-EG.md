# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على السلوك (`behavior`) والتعاون بين الكائنات (`objects`)، وده واحد من أغراض الـ `Design Patterns`.

## Difficulty

متقدم

## In One Sentence

ضيف عمليات جديدة على مجموعة أنواع ثابتة، وحط العمليات دي في `Visitor` منفصلة.

## The Problem

السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل `class`.

## Naive Solution

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## Why It Becomes a Problem

إضافة `virtual method` لكل عملية بتطلب تعديل كل عناصر السلة مع كل مهمة جديدة.

## The Idea

خلّي كل نوع فعلي من `Item` ينفّذ العملية `accept` بحيث ينادي النسخة المناسبة لنوعه من `Visitor::visit`. الزائر `Tax` بيوفّر حساب الضريبة لكل نوع.

## Real-World Analogy

مفتش بيزور محطات ورشة، ولكل نوع محطة قائمة فحص مناسبة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## Participants

في المثال، العقد `Item` بيحدد العملية `accept`. كل من `Book` و `Food` بيختار الاستدعاء المناسب لنوعه (`overload`). عقد الزيارة `Visitor` بيسرد الأنواع المدعومة، و `Tax` بتجمع النتيجة. السلة بتمتلك العناصر.

الأدوار القياسية في المثال ده:

- [`Element`](../../GLOSSARY.md#element) — عقد الـ `objects` اللي بتقبل `Visitor`. هنا: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — تنفيذ للعنصر (`Element implementation`) بيختار الاستدعاء المناسب لنوعه من عمليات الزيارة (`Visitor overload`). هنا: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — تنفيذ للزائر (`Visitor implementation`) فيه عملية لكل نوع عنصر مدعوم (`Element`). هنا: `Tax`.

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

مناسب لتحليل `AST` وتصدير المستندات مع عيلة عقد ثابتة؛ الـ `std::variant` مع `std::visit` بديل لمجموعة أنواع مقفولة.

## When NOT to Use

بلاش لو الأنواع الجديدة بتزيد باستمرار أو كشف تفاصيلها هيكسر الـ [`encapsulation`](../../GLOSSARY.md#encapsulation) (بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة).

## Advantages

تضيف عملية في `Visitor` من غير تعديل `classes` العناصر الموجودة.

## Trade-offs

إضافة نوع عنصر جديد بتحتاج تعديل عقد الزيارة في `Visitor`، وكل تنفيذ للزائر. العقد ده هو الـ [`interface`](../../GLOSSARY.md#interface): العمليات اللي كل تنفيذ لازم يوفّرها. نسب الضريبة هنا للتوضيح، والتقريب محتاج قاعدة مناسبة للمجال.

## Related Patterns

[Composite](../../structural/composite/README.ar-EG.md) · [Iterator](../iterator/README.ar-EG.md)

## Common Confusion

الـ `Iterator` بتلف على المجموعة، `Visitor` بتختار العملية حسب النوع، و `Composite` ممكن توفر الشجرة.

## Terms to Remember

- `Visitor` — ضيف عمليات جديدة على مجموعة أنواع ثابتة، وحط العمليات دي في `Visitor` منفصلة.
- `Element` — عقد الـ `objects` اللي بتقبل `Visitor`. مثال: `Item`.
- `Concrete Element` — تنفيذ للعنصر (`Element implementation`) بيختار الاستدعاء المناسب لنوعه من عمليات الزيارة (`Visitor overload`). مثال: `Book, Food`.
- `Concrete Visitor` — تنفيذ للزائر (`Visitor implementation`) فيه عملية لكل نوع عنصر مدعوم (`Element`). مثال: `Tax`.

## Interview Vocabulary

- [`double dispatch`](../../GLOSSARY.md#double-dispatch) — اختيار `behavior` بناءً على نوعين وقت `runtime`؛ الـ `Visitor` التقليدية بتجمع نداءين `virtual` مع `overload resolution`.
- [`overload resolution`](../../GLOSSARY.md#overload-resolution) — اختيار `function` من كذا واحدة بنفس الاسم حسب أنواع المعاملات وقت `compile time`.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — خلّي التوسيع ممكن من غير تعديل الكود المستقر، عند حدود مختارة بوضوح. التعبير هو `open for extension, closed for modification`.

## Interview Question

ليه `visitor.visit(*this)` جوه `Book` تختار `Overload` الكتب، و `Item reference` لوحدها مش كفاية؟

## Mini Challenge

ضيف `Label Visitor` من غير تعديل `Book` أو `Food`، وبعدها ضيف نوع ثالث وعدّ التغييرات.

## Quick Summary

- **المشكلة:** السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل `class`.
- **الحل:** خلّي كل نوع فعلي من `Item` ينفّذ العملية `accept` بحيث ينادي النسخة المناسبة لنوعه من `Visitor::visit`. الزائر `Tax` بيوفّر حساب الضريبة لكل نوع.
- **`Trade-off`:** إضافة نوع عنصر جديد بتحتاج تعديل عقد الزيارة في `Visitor`، وكل تنفيذ للزائر. العقد ده هو الـ `interface`: العمليات اللي كل تنفيذ لازم يوفّرها. نسب الضريبة هنا للتوضيح، والتقريب محتاج قاعدة مناسبة للمجال.
- **افتكر:** أنواع ثابتة، عمليات جديدة.

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)
