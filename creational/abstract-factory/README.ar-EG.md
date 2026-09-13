# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[الفئة](../README.ar-EG.md) · [التالي](../../creational/builder/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — بيركز على إنشاء الـ`Objects` وإعدادها.

## Difficulty

متوسط

## In One Sentence

أنشئ مجموعة كائنات مرتبطة ومتوافقة مع بعض (`family of related objects`) باستخدام `Factory` واحدة.

## ببساطة

الشاشة محتاجة أزرار ولوحات بنفس الشكل.بنختار `Factory` واحدة توفر الاتنين، بدل ما كل مستدعي يختار كل `Class` لوحدها.

## The Problem

شاشة الإعدادات محتاجة أزرار ولوحات (`Buttons` و `Panels`) من نفس المظهر (`Theme`).

## Naive Solution

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## Why It Becomes a Problem

لما كل مكان يعمل الـ `Widget` بنفسه، ممكن `Button` غامق يطلع جنب `Panel` فاتح. كل `Client` بيضطر يفتكر قواعد التوافق.

## The Idea

مرّر مصنع واحد من نوع `Theme` للدالة `render`. المصنع هو اللي بينشئ نوعي المنتجات، فالكود المستدعي (`Client`) مش محتاج يحدد الأنواع الفعلية (`concrete classes`).

## Real-World Analogy

زي ما تطلب طقم أثاث كامل بدل ما تختار كل قطعة لوحدها.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Abstract Factory](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## Participants

في المثال، `Theme` بتحدد إزاي ننشئ المجموعة، و `DarkTheme` و `LightTheme` بينفّذوا الإنشاء. عقود المنتجات هي `Button` و `Panel`، والدالة `render` بتستخدمهم من غير ما تختار الأنواع الفعلية.

الأدوار القياسية في المثال ده:

- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. هنا: `Button, Panel`.
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — تنفيذ فعلي (`implementation`) لعقد المنتج (`Product`). هنا: `DarkButton, LightButton, DarkPanel, LightPanel`.
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — تنفيذ فعلي (`implementation`) بينشئ عيلة منتجات متوافقة (`Product family`). هنا: `DarkTheme, LightTheme`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Button {
    virtual ~Button() = default;
    virtual std::string_view paint() const = 0;
};
struct Panel {
    virtual ~Panel() = default;
    virtual std::string_view paint() const = 0;
};
struct DarkButton final : Button {
    std::string_view paint() const override { return "dark button"; }
};
struct DarkPanel final : Panel {
    std::string_view paint() const override { return "dark panel"; }
};
struct LightButton final : Button {
    std::string_view paint() const override { return "light button"; }
};
struct LightPanel final : Panel {
    std::string_view paint() const override { return "light panel"; }
};
struct Theme {
    virtual ~Theme() = default;
    virtual std::unique_ptr<Button> button() const = 0;
    virtual std::unique_ptr<Panel> panel() const = 0;
};
struct DarkTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<DarkButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<DarkPanel>(); }
};
struct LightTheme final : Theme {
    std::unique_ptr<Button> button() const override { return std::make_unique<LightButton>(); }
    std::unique_ptr<Panel> panel() const override { return std::make_unique<LightPanel>(); }
};
void render(const Theme& theme) {
    const auto button = theme.button();
    const auto panel = theme.panel();
    std::cout << button->paint() << " + " << panel->paint() << '\n';
}
int main() {
    render(DarkTheme{});
    render(LightTheme{});
}
```

## Example Output

```text
dark button + dark panel
light button + light panel
```

## When to Use

استخدمه لما كذا نوع من المنتجات لازم يتغيروا مع بعض، والـ `Client` ماينفعش يختار الـ `classes` بنفسه.

### Use cases

ينفع مع `Themes` أو مجموعات `Database Drivers` المتوافقة؛ المثال هنا بيطبع أسماء بس.

## When NOT to Use

بلاش لو عندك نوع واحد ثابت، أو لو الاختيارات المستقلة مطلوبة أصلاً.

## Advantages

تقدر تبدّل المجموعة كلها من غير ما تغيّر خطوات العرض.

## Trade-offs

إضافة منتج زي `Slider` بتحتاج تعديل كل `Factory`. الـ [`interface`](../../GLOSSARY.md#interface) لوحدها مش بتضمن إن الألوان متوافقة فعلاً.

## Related Patterns

[Factory Method](../factory-method/README.ar-EG.md) · [Builder](../builder/README.ar-EG.md)

## Common Confusion

الـ `Factory Method` بتغيّر خطوة إنشاء واحدة. الـ `Abstract Factory` بتنسّق أنواع منتجات مرتبطة، وممكن تستخدم `Factory Methods` جواها.

## Terms to Remember

- `Abstract Factory` — أنشئ مجموعة كائنات مرتبطة ومتوافقة مع بعض (`family of related objects`) باستخدام `Factory` واحدة.
- `Product` — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. مثال: `Button, Panel`.
- `Concrete Product` — تنفيذ فعلي (`implementation`) لعقد المنتج (`Product`). مثال: `DarkButton, LightButton, DarkPanel, LightPanel`.
- `Concrete Factory` — تنفيذ فعلي (`implementation`) بينشئ عيلة منتجات متوافقة (`Product family`). مثال: `DarkTheme, LightTheme`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).
- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — اعتمد على العقد المعلن بدل تفاصيل `implementation` بعينها.
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — حط القرار اللي بيتغير ورا حدود ثابتة وواضحة.

## Interview Question

إيه اللي بيتغير لما تضيف `Theme`، وإيه اللي بيتغير لما تضيف `Widget` جديدة؟

## Mini Challenge

ضيف مجموعة `High Contrast`، وبعدها ضيف `Slider` وقارن حجم التعديلات.

## اختبر فهمك

1. ليه `Theme` واحدة بتعمل المنتجين؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** شاشة الإعدادات محتاجة أزرار ولوحات (`Buttons` و `Panels`) من نفس المظهر (`Theme`).
- **الحل:** مرّر مصنع واحد من نوع `Theme` للدالة `render`. المصنع هو اللي بينشئ نوعي المنتجات، فالكود المستدعي (`Client`) مش محتاج يحدد الأنواع الفعلية (`concrete classes`).
- **`Trade-off`:** إضافة منتج زي `Slider` بتحتاج تعديل كل `Factory`. الـ `interface` لوحدها مش بتضمن إن الألوان متوافقة فعلاً.
- **افتكر:** طقم متوافق من `Factory` واحدة.

[الفئة](../README.ar-EG.md) · [التالي](../../creational/builder/README.ar-EG.md)
