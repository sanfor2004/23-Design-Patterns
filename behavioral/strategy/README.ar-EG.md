# Strategy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/state/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/template-method/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

مبتدئ

## In One Sentence

مرّر algorithm قابلة للتبديل للـ object اللي محتاجاها.

## The Problem

إجمالي الشراء محتاج سياسات شحن مختلفة من غير حشر كل سياسة جوه Checkout.

## Naive Solution

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## Why It Becomes a Problem

شرط واحد مقروء؛ تكرار فروع السياسات في كذا مسار بيصعّب إضافة القواعد واختبارها.

## The Idea

Checkout بتمتلك callable اسمها ShippingRule وبتسألها عن الرسوم؛ المستدعي بيختار القاعدة وقت الإنشاء.

## Real-World Analogy

اختار تخطيط طريق للمشي أو السواقة، والوجهة واحدة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Strategy](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## Participants

Checkout هي الـ Context ، ShippingRule عقد الـ behavior ، والـ Lambdas بتنّفذ الشحن العادي والسريع.

الأدوار القياسية في المثال ده:

- [`Context`](../../GLOSSARY.md#context) — الـ object اللي بتستخدم Strategy أو بتفوّض behavior للـ State الحالية. هنا: `Checkout`.
- [`Strategy interface`](../../GLOSSARY.md#strategy-interface) — عقد الـ algorithms القابلة للتبديل اللي Context بتستخدمها. هنا: `ShippingRule`.
- [`Concrete Strategy`](../../GLOSSARY.md#concrete-strategy) — implementation محددة لـ Strategy interface؛ ممكن تكون callable بدل class. هنا: `standard / express lambdas`.

## Modern C++20 Example

```cpp
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
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## Example Output

```text
Standard: 45
Express: 55
Express large: 120
```

## When to Use

استخدمه لما الـ algorithms بتتغير باستقلال والـ Client محتاج يختار سياسة.

### Use cases

مناسب للتسعير والترتيب وسياسات إعادة المحاولة.

## When NOT to Use

بلاش لـ algorithm ثابتة واحدة أو شرط واضح مش محتاج توسعة فعلية.

## Advantages

كل سياسة تتختبر لوحدها، وحساب الإجمالي يفضل مشترك.

## Trade-offs

[`std::function`](../../GLOSSARY.md#stdfunction) (Wrapper بتخزن callable بتوقيع محدد وبتخفي نوعها الفعلي) فيها [`type erasure`](../../GLOSSARY.md#type-erasure) (بتخفي النوع الفعلي ورا interface موحدة وقت runtime، زي std::function مع callables) وممكن تخصص ذاكرة؛ template أو function pointer ممكن يناسبوا قيود تانية. راجع الرسوم لو كود خارجي ممكن يرجع قيم غير صالحة.

## Related Patterns

[State](../state/README.ar-EG.md) · [Template Method](../template-method/README.ar-EG.md)

## Common Confusion

State بتمثل [`lifecycle`](../../GLOSSARY.md#lifecycle) (المراحل والانتقالات اللي بنمثلها لكيان في المشكلة؛ مش نفس lifetime بتاعة object في C++) وانتقالات، Strategy بتختار algorithm. Template Method بتغيّر خطوات موروثة بدل callable محقونة.

## Terms to Remember

- `Strategy` — مرّر algorithm قابلة للتبديل للـ object اللي محتاجاها.
- `Context` — الـ object اللي بتستخدم Strategy أو بتفوّض behavior للـ State الحالية. مثال: `Checkout`.
- `Strategy interface` — عقد الـ algorithms القابلة للتبديل اللي Context بتستخدمها. مثال: `ShippingRule`.
- `Concrete Strategy` — implementation محددة لـ Strategy interface؛ ممكن تكون callable بدل class. مثال: `standard / express lambdas`.

## Interview Vocabulary

- [`interchangeable behavior`](../../GLOSSARY.md#interchangeable-behavior) — behaviors مختلفة تقدر تمرّر أي واحدة منها من نفس العقد.
- [`encapsulate an algorithm`](../../GLOSSARY.md#encapsulate-an-algorithm) — حط algorithm ورا عملية بتخفي خطواتها الداخلية.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — فضّل objects متعاونة لما تعبر عن التغيير أوضح من تكبير شجرة inheritance.
- [`runtime selection`](../../GLOSSARY.md#runtime-selection) — اختيار implementation والبرنامج شغال.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.

## Interview Question

استبدال std::function بـ template Parameter هيأثر إزاي على الاختيار وقت [`runtime`](../../GLOSSARY.md#runtime) (الوقت اللي البرنامج فيه شغال بعد البناء) والترجمة؟

## Mini Challenge

ضيف شحن مجاني من 80 واختبر 79 و80 و81.

## Quick Summary

- **المشكلة:** إجمالي الشراء محتاج سياسات شحن مختلفة من غير حشر كل سياسة جوه Checkout.
- **الحل:** Checkout بتمتلك callable اسمها ShippingRule وبتسألها عن الرسوم؛ المستدعي بيختار القاعدة وقت الإنشاء.
- **Trade-off:** std::function فيها type erasure وممكن تخصص ذاكرة؛ template أو function pointer ممكن يناسبوا قيود تانية. راجع الرسوم لو كود خارجي ممكن يرجع قيم غير صالحة.
- **افتكر:** نفس المهمة، اختار الـ algorithm.

[السابق](../../behavioral/state/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/template-method/README.ar-EG.md)
