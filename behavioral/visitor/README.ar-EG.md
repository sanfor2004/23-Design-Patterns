# Visitor

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** ضيف عمليات جديدة على مجموعة أنواع ثابتة، وحط العمليات دي في `Visitor` منفصلة.

## المشكلة

السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل `class`. إضافة `virtual method` لكل عملية بتطلب تعديل كل عناصر السلة مع كل مهمة جديدة.

## الحل ببساطة

الكتب والأكل ليهم حساب ضريبة مختلف.الـ`Visitor` بيجمع الحسابات، وكل عنصر بينادي العملية المناسبة لنوعه. خلّي كل نوع فعلي من `Item` ينفّذ العملية `accept` بحيث ينادي النسخة المناسبة لنوعه من `Visitor::visit`. الزائر `Tax` بيوفّر حساب الضريبة لكل نوع.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Visitor](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

في المثال، العقد `Item` بيحدد العملية `accept`. كل من `Book` و `Food` بيختار الاستدعاء المناسب لنوعه (`overload`). عقد الزيارة `Visitor` بيسرد الأنواع المدعومة، و `Tax` بتجمع النتيجة. السلة بتمتلك العناصر.

الأدوار القياسية في المثال ده:

- [`Element`](../../GLOSSARY.md#element) — عقد الـ `objects` اللي بتقبل `Visitor`. هنا: `Item`.
- [`Concrete Element`](../../GLOSSARY.md#concrete-element) — تنفيذ للعنصر (`Element implementation`) بيختار الاستدعاء المناسب لنوعه من عمليات الزيارة (`Visitor overload`). هنا: `Book, Food`.
- [`Concrete Visitor`](../../GLOSSARY.md#concrete-visitor) — تنفيذ للزائر (`Visitor implementation`) فيه عملية لكل نوع عنصر مدعوم (`Element`). هنا: `Tax`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

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

## قارن اللغتين

Python uses separate `visit_book` and `visit_food` methods because it does not overload methods by parameter type. C++ uses overloads plus virtual dispatch. Both keep Tax outside the element types. Integer division truncates fractional cents; these sample rates and amounts avoid fractions and are not a tax policy.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما أنواع العناصر ثابتة والعمليات الجديدة كتير.

### Use cases

مناسب لتحليل `AST` وتصدير المستندات مع عيلة عقد ثابتة؛ الـ `std::variant` مع `std::visit` بديل لمجموعة أنواع مقفولة.

**التكلفة:** إضافة نوع عنصر جديد بتحتاج تعديل عقد الزيارة في `Visitor`، وكل تنفيذ للزائر. العقد ده هو الـ [`interface`](../../GLOSSARY.md#interface): العمليات اللي كل تنفيذ لازم يوفّرها. نسب الضريبة هنا للتوضيح، والتقريب محتاج قاعدة مناسبة للمجال.

## جرّب تجاوب

1. إيه اللي بيتغير لما تضيف نوع عنصر جديد بدل عملية جديدة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Label Visitor` من غير تعديل `Book` أو `Food`، وبعدها ضيف نوع ثالث وعدّ التغييرات.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
