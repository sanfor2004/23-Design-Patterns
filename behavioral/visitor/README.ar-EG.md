# الزائر

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)

## الفئة

السلوك

## المستوى

متقدم

## في جملة واحدة

ضيف عمليات على أنواع عناصر ثابتة عن طريق Visitor منفصلة.

## المشكلة

السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل Class.

## حل بسيط في الأول

```cpp
// For each new operation, add another virtual method to every Item.
// tax(), export_json(), print_label(), ...
```

## ليه الحل بيصعّب الدنيا

إضافة Virtual Method لكل عملية بتطلب تعديل كل عناصر السلة مع كل مهمة جديدة.

## الفكرة الأساسية

كل Item فعلية بتنادي Visitor::visit المناسبة لنوعها من accept، وTax بتنّفذ العملية لكل نوع.

## مثال من الحياة

مفتش بيزور محطات ورشة، ولكل نوع محطة قائمة فحص مناسبة.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الزائر](../../assets/diagrams/visitor.svg)

```text
Item::accept(visitor)  -->  Visitor::visit(type)  -->  Tax(Book) / Tax(Food)
```

## الأدوار

Item بتحدد accept، Book وFood بيختاروا الـ Overload، Visitor بتسرد الأنواع، Tax بتجمع النتيجة، والسلة بتمتلك العناصر.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
Tax: 4
```

## إمتى تستخدمه

استخدمه لما أنواع العناصر ثابتة والعمليات الجديدة كتير.

## إمتى ما تستخدموش

بلاش لو الأنواع الجديدة بتزيد باستمرار أو كشف تفاصيلها هيكسر التغليف.

## المميزات

تضيف عملية في Visitor من غير تعديل Classes العناصر الموجودة.

## العيوب والمقايضات

إضافة نوع عنصر بتطلب تعديل واجهة Visitor وكل الزوار. نسب الضريبة هنا للتوضيح مش قواعد حقيقية، والتقريب محتاج سياسة من المجال.

## استخدامات تقنية

مناسب لتحليل AST وتصدير المستندات مع عيلة عقد ثابتة؛ std::variant مع std::visit بديل لمجموعة أنواع مقفولة.

## أنماط مرتبطة

[composite](../../structural/composite/README.ar-EG.md) · [iterator](../iterator/README.ar-EG.md)

## لخبطة شائعة

Iterator بتلف على المجموعة، Visitor بتختار العملية حسب النوع، وComposite ممكن توفر الشجرة.

## سؤال انترفيو

ليه visitor.visit(*this) جوه Book تختار Overload الكتب، وItem Reference لوحدها مش كفاية؟

## تحدي صغير

ضيف Label Visitor من غير تعديل Book أوFood، وبعدها ضيف نوع ثالث وعدّ التغييرات.

## الخلاصة

- **المشكلة:** السلة فيها كتب وأكل، وعمليات جديدة زي الضريبة أو التصدير مش المفروض تملا كل Class.
- **الحل:** كل Item فعلية بتنادي Visitor::visit المناسبة لنوعها من accept، وTax بتنّفذ العملية لكل نوع.
- **المقايضة:** إضافة نوع عنصر بتطلب تعديل واجهة Visitor وكل الزوار. نسب الضريبة هنا للتوضيح مش قواعد حقيقية، والتقريب محتاج سياسة من المجال.
- **افتكر:** أنواع ثابتة، عمليات جديدة.

[السابق](../../behavioral/template-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md)
