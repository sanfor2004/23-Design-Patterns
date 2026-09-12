# المصنع المجرّد

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[الفئة](../README.ar-EG.md) · [التالي](../../creational/builder/README.ar-EG.md)

## الفئة

الإنشاء

## المستوى

متوسط

## في جملة واحدة

اعمل مجموعة Objects متوافقة من خلال Factory واحدة.

## المشكلة

شاشة الإعدادات محتاجة Buttons وPanels من نفس الـ Theme.

## حل بسيط في الأول

```cpp
auto button = DarkButton{};
auto panel = LightPanel{}; // mixed theme
```

## ليه الحل بيصعّب الدنيا

لما كل مكان يعمل الـ Widget بنفسه، ممكن Button غامق يطلع جنب Panel فاتح. كل Client بيضطر يفتكر قواعد التوافق.

## الفكرة الأساسية

مرّر Theme واحدة لـ render. هي اللي بتعمل النوعين، فالـ Client مش محتاج يسمي الكلاسات الفعلية.

## مثال من الحياة

زي ما تطلب طقم أثاث كامل بدل ما تختار كل قطعة لوحدها.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المصنع المجرّد](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

## الأدوار

Theme بتحدد المجموعة؛ DarkTheme وLightTheme بيعملوها. Button وPanel واجهات المنتجات، وrender بيستخدمهم.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
dark button + dark panel
light button + light panel
```

## إمتى تستخدمه

استخدمه لما كذا نوع من المنتجات لازم يتغيروا مع بعض، والـ Client ماينفعش يختار الكلاسات بنفسه.

## إمتى ما تستخدموش

بلاش لو عندك نوع واحد ثابت، أو لو الاختيارات المستقلة مطلوبة أصلاً.

## المميزات

تقدر تبدّل المجموعة كلها من غير ما تغيّر خطوات العرض.

## العيوب والمقايضات

إضافة منتج زي Slider بتحتاج تعديل كل Factory. الواجهة لوحدها مش بتضمن إن الألوان متوافقة فعلاً.

## استخدامات تقنية

ينفع مع Themes أو مجموعات Database Drivers المتوافقة؛ المثال هنا بيطبع أسماء بس.

## أنماط مرتبطة

[factory-method](../factory-method/README.ar-EG.md) · [builder](../builder/README.ar-EG.md)

## لخبطة شائعة

Factory Method بتغيّر خطوة إنشاء واحدة. Abstract Factory بتنسّق أنواع منتجات مرتبطة، وممكن تستخدم Factory Methods جواها.

## سؤال انترفيو

إيه اللي بيتغير لما تضيف Theme، وإيه اللي بيتغير لما تضيف Widget جديدة؟

## تحدي صغير

ضيف مجموعة High Contrast، وبعدها ضيف Slider وقارن حجم التعديلات.

## الخلاصة

- **المشكلة:** شاشة الإعدادات محتاجة Buttons وPanels من نفس الـ Theme.
- **الحل:** مرّر Theme واحدة لـ render. هي اللي بتعمل النوعين، فالـ Client مش محتاج يسمي الكلاسات الفعلية.
- **المقايضة:** إضافة منتج زي Slider بتحتاج تعديل كل Factory. الواجهة لوحدها مش بتضمن إن الألوان متوافقة فعلاً.
- **افتكر:** Factory واحدة، طقم متوافق.

[الفئة](../README.ar-EG.md) · [التالي](../../creational/builder/README.ar-EG.md)
