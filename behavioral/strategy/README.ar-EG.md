# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** افصل طريقة الحساب (`algorithm`) عن الكائن اللي بيستخدمها، عشان تقدر تختار طريقة بديلة لنفس المهمة.

## المشكلة

إجمالي الشراء محتاج سياسات شحن مختلفة من غير حشر كل سياسة جوه `Checkout`. شرط واحد مقروء؛ تكرار فروع السياسات في كذا مسار بيصعّب إضافة القواعد واختبارها.

## الحل ببساطة

الشراء ممكن يحسب شحن عادي أو سريع.الـ`Strategy` بيدي `Checkout` قاعدة شحن يستخدمها، بدل ما حساب الإجمالي يحتوي كل القواعد. خلّي حساب الشراء `Checkout` يحتفظ بطريقة لحساب رسوم الشحن. بيمثلها عقد قابل للاستدعاء (`callable`) اسمه `ShippingRule`. المستدعي بيختار الطريقة وقت الإنشاء، وحساب الإجمالي بيستخدمها من غير ما يعرف تفاصيلها.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

في المثال، حساب الشراء `Checkout` بيلعب دور `Context`. عقد طريقة الحساب هو `ShippingRule`. بننفّذ طريقتي الشحن العادي والسريع باستخدام دوال قصيرة (`lambdas`).

الأدوار القياسية في المثال ده:

- [`Context`](../../GLOSSARY.md#context) — الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). هنا: `Checkout`.
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — بتحدد العقد المشترك للـ`algorithms` المختلفة. الـ`Context` بيعتمد على العقد ده بدل `implementation` محدد. هنا: `ShippingRule`.
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — تنفيذ محدد لعقد `Strategy interface`. ممكن تمثّله بحاجة قابلة للاستدعاء (`callable`)، ومش لازم يكون `class` مستقلة. هنا: `standard / express lambdas`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Checkout:
    def __init__(self, shipping_rule):
        self.shipping_rule = shipping_rule

    def total(self, subtotal_cents):
        if subtotal_cents < 0:
            raise ValueError("Negative subtotal")
        return subtotal_cents + self.shipping_rule(subtotal_cents)


def standard(subtotal_cents):
    return 500


def express(subtotal_cents):
    return 0 if subtotal_cents >= 10000 else 1500


def main():
    print("Standard:", Checkout(standard).total(4000))
    print("Express:", Checkout(express).total(4000))
    print("Express boundary:", Checkout(express).total(10000))
    try:
        Checkout(standard).total(-1)
    except ValueError:
        print("Negative subtotal rejected")


if __name__ == "__main__":
    main()
```

### Python output

```text
Standard: 4500
Express: 5500
Express boundary: 10000
Negative subtotal rejected
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal_cents) const {
        if (subtotal_cents < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal_cents + shipping_(subtotal_cents);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal_cents) { return subtotal_cents >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
    std::cout << "Express boundary: " << express.total(100) << '\n';
    try { static_cast<void>(standard.total(-1)); }
    catch (const std::invalid_argument&) { std::cout << "Negative subtotal rejected\n"; }
    try { const Checkout missing{ShippingRule{}}; }
    catch (const std::invalid_argument&) { std::cout << "Missing rule rejected\n"; }
}
```

### C++20 output

```text
Standard: 45
Express: 55
Express large: 120
Express boundary: 100
Negative subtotal rejected
Missing rule rejected
```

## قارن اللغتين

A Python function is the Concrete Strategy. C++ stores the same kind of callable in `std::function`; a template policy can instead select it at Compile time. Both examples choose the rule when constructing Checkout. Amounts are integer cents.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدم `Strategy` لما قواعد الحساب بتتغير بشكل مستقل عن `Checkout`، والمستدعي محتاج يختار القاعدة المناسبة.

### Use cases

مناسب للتسعير والترتيب وسياسات إعادة المحاولة.

**التكلفة:** بنستخدم [`std::function`](../../GLOSSARY.md#stdfunction) لتخزين دالة قابلة للاستدعاء بتوقيع محدد، مع إخفاء نوعها الفعلي. ده اسمه [`type erasure`](../../GLOSSARY.md#type-erasure)، وليه تكلفة وممكن يحتاج حجز ذاكرة. حسب القيود، ممكن تختار `template` أو مؤشر دالة (`function pointer`) بدلها. راجع الرسوم لو كود خارجي ممكن يرجع قيم غير صالحة.

## جرّب تجاوب

1. هل الـ`API` العامة في `Checkout` دي بتسمح بتغيير القاعدة بعد الإنشاء؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف شحن مجاني من 80 واختبر 79 و80 و81.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
