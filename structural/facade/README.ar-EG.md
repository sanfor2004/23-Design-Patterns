# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/decorator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/flyweight/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — بيركز على تركيب الـ`Objects` والـ`Classes` عشان تتعاون.

## Difficulty

مبتدئ

## In One Sentence

وفّر مدخل بسيط للخطوات الشائعة جوه نظام فرعي (`subsystem`).

## ببساطة

الشراء محتاج مراجعة مخزون ودفع وشحن بالترتيب.الـ`Facade` بيجمع الخطوات المشتركة في استدعاء واحد، بس مش بيحوّلها تلقائيًا لـ`Transaction`.

## The Problem

كل مستدعي للشراء محتاج يراجع المخزون ويدفع ويطلب الشحن بالترتيب الصح.

## Naive Solution

```cpp
payment.charge(20);
shipping.dispatch(); // caller forgot to check stock
```

## Why It Becomes a Problem

الاستدعاءات المباشرة ممكن تنسى المخزون أو تكرر ترتيب الخطوات بشكل مختلف.

## The Idea

وفّر عملية شراء واحدة اسمها `buy` في `Checkout`. جوه العملية، نسّق الخدمات الداخلية بالترتيب المطلوب.

## Real-World Analogy

استقبال المطعم بينسق الحجز بدل ما تكلم كل قسم.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Participants

في المثال، مراجعة المخزون مسؤولية `Stock`، والدفع مسؤولية `Payment`، والشحن مسؤولية `Shipping`. المدخل المشترك `Checkout` بيرتب الخطوات دي للمستدعي.

الأدوار القياسية في المثال ده:

- [`subsystem`](../../GLOSSARY.md#subsystem) — مجموعة خدمات أو `objects` بتتعاون جوه نظام أكبر. هنا: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`. هنا: `main`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount_cents) const { std::cout << "Charged " << amount_cents << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

## Example Output

```text
Charged 20
Dispatched
Unavailable
```

## When to Use

استخدمه لما مستدعين كتير محتاجين نفس الجزء المفيد من نظام معقد.

### Use cases

مناسب لمداخل `SDK` وحدود خدمات التطبيق؛ مفيش تكامل دفع حقيقي هنا.

## When NOT to Use

بلاش لو مجرد تمرير لـ `function` من غير تبسيط حقيقي.

## Advantages

الـ `Callers` بيعتمدوا على `interface` أصغر وترتيب موحد.

## Trade-offs

الـ `Facade` ممكن تكبر وتعمل كل حاجة. المثال مش `Transaction`: فشل الدفع أو الشحن الحقيقي محتاج تعويض أو طريقة اتساق مناسبة.

## Related Patterns

[Adapter](../adapter/README.ar-EG.md) · [Mediator](../../behavioral/mediator/README.ar-EG.md)

## Common Confusion

الـ `Adapter` بتعالج التوافق. الـ `Facade` بتصغّر `interface` النظام ومش لازم تنفذ `interface` موجودة.

## Terms to Remember

- `Facade` — وفّر مدخل بسيط للخطوات الشائعة جوه نظام فرعي (`subsystem`).
- `subsystem` — مجموعة خدمات أو `objects` بتتعاون جوه نظام أكبر. مثال: `Stock, Payment, Shipping`.
- `interface` — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. مثال: `Checkout::buy`.
- `Client` — الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`. مثال: `main`.

## Interview Vocabulary

- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`trade-off`](../../GLOSSARY.md#trade-off) — ميزة بتكسبها قصاد تكلفة أو تنازل في ناحية تانية.

## Interview Question

لو الدفع نجح والشحن فشل، `buy` تقدر توعد بإيه فعلاً؟

## Mini Challenge

ضيف فشل شحن تجريبي وصمّم نتيجة `Refund` واضحة بدل نجاح وهمي.

## اختبر فهمك

1. إيه اللي `buy` مش بيضمنه لو الشحن فشل بعد الدفع؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** كل مستدعي للشراء محتاج يراجع المخزون ويدفع ويطلب الشحن بالترتيب الصح.
- **الحل:** وفّر عملية شراء واحدة اسمها `buy` في `Checkout`. جوه العملية، نسّق الخدمات الداخلية بالترتيب المطلوب.
- **`Trade-off`:** الـ `Facade` ممكن تكبر وتعمل كل حاجة. المثال مش `Transaction`: فشل الدفع أو الشحن الحقيقي محتاج تعويض أو طريقة اتساق مناسبة.
- **افتكر:** باب واحد لكذا خدمة.

[السابق](../../structural/decorator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/flyweight/README.ar-EG.md)
