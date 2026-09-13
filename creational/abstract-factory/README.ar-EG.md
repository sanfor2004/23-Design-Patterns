# Abstract Factory

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** أنشئ مجموعة كائنات مرتبطة ومتوافقة مع بعض (`family of related objects`) باستخدام `Factory` واحدة.

## المشكلة

شاشة الإعدادات محتاجة أزرار ولوحات (`Buttons` و `Panels`) من نفس المظهر (`Theme`). لما كل مكان يعمل الـ `Widget` بنفسه، ممكن `Button` غامق يطلع جنب `Panel` فاتح. كل `Client` بيضطر يفتكر قواعد التوافق.

## الحل ببساطة

الشاشة محتاجة أزرار ولوحات بنفس الشكل.بنختار `Factory` واحدة توفر الاتنين، بدل ما كل مستدعي يختار كل `Class` لوحدها. مرّر مصنع واحد من نوع `Theme` للدالة `render`. المصنع هو اللي بينشئ نوعي المنتجات، فالكود المستدعي (`Client`) مش محتاج يحدد الأنواع الفعلية (`concrete classes`).

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Abstract Factory](../../assets/diagrams/abstract-factory.svg)

```text
render()  -->  Theme  -->  Button + Panel
```

في المثال، `Theme` بتحدد إزاي ننشئ المجموعة، و `DarkTheme` و `LightTheme` بينفّذوا الإنشاء. عقود المنتجات هي `Button` و `Panel`، والدالة `render` بتستخدمهم من غير ما تختار الأنواع الفعلية.

الأدوار القياسية في المثال ده:

- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. هنا: `Button, Panel`.
- [`Concrete Product`](../../GLOSSARY.md#concrete-product) — تنفيذ فعلي (`implementation`) لعقد المنتج (`Product`). هنا: `DarkButton, LightButton, DarkPanel, LightPanel`.
- [`Concrete Factory`](../../GLOSSARY.md#concrete-factory) — تنفيذ فعلي (`implementation`) بينشئ عيلة منتجات متوافقة (`Product family`). هنا: `DarkTheme, LightTheme`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Button:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " button"


class Panel:
    def __init__(self, theme):
        self.theme = theme

    def paint(self):
        return self.theme + " panel"


class DarkTheme:
    def button(self):
        return Button("dark")

    def panel(self):
        return Panel("dark")


class LightTheme:
    def button(self):
        return Button("light")

    def panel(self):
        return Panel("light")


def render(theme):
    print(theme.button().paint() + " + " + theme.panel().paint())


if __name__ == "__main__":
    render(DarkTheme())
    render(LightTheme())
```

### Python output

```text
dark button + dark panel
light button + light panel
```

## C++20 example

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

### C++20 output

```text
dark button + dark panel
light button + light panel
```

## قارن اللغتين

Python uses matching method names instead of abstract base classes. C++ declares separate Button, Panel, and Theme Interfaces. Both create a family of products. Neither language automatically proves that the products match visually.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما كذا نوع من المنتجات لازم يتغيروا مع بعض، والـ `Client` ماينفعش يختار الـ `classes` بنفسه.

### Use cases

ينفع مع `Themes` أو مجموعات `Database Drivers` المتوافقة؛ المثال هنا بيطبع أسماء بس.

**التكلفة:** إضافة منتج زي `Slider` بتحتاج تعديل كل `Factory`. الـ [`interface`](../../GLOSSARY.md#interface) لوحدها مش بتضمن إن الألوان متوافقة فعلاً.

## جرّب تجاوب

1. ليه `Theme` واحدة بتعمل المنتجين؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف مجموعة `High Contrast`، وبعدها ضيف `Slider` وقارن حجم التعديلات.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
