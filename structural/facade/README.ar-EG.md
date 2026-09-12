# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/decorator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/flyweight/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

مبتدئ

## In One Sentence

وفّر مدخل صغير لخطوات شائعة جوه Subsystem.

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

Checkout بتوفر buy وبتنسق الخدمات الداخلية ورا العملية دي.

## Real-World Analogy

استقبال المطعم بينسق الحجز بدل ما تكلم كل قسم.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

## Participants

Stock بتراجع التوفر، Payment بتحاسب، Shipping بتشحن، و Checkout بتعرض الخطوات المشتركة.

الأدوار القياسية في المثال ده:

- [`subsystem`](../../GLOSSARY.md#subsystem) — مجموعة خدمات أو objects بتتعاون جوه نظام أكبر. هنا: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — الكود اللي بيستخدم interface أو بيتعامل مع objects بتاعة الـ Pattern. هنا: `main`.

## Modern C++20 Example

```cpp
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount) const { std::cout << "Charged " << amount << '\n'; }
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

مناسب لمداخل SDK وحدود خدمات التطبيق؛ مفيش تكامل دفع حقيقي هنا.

## When NOT to Use

بلاش لو مجرد تمرير لـ function من غير تبسيط حقيقي.

## Advantages

الـ Callers بيعتمدوا على interface أصغر وترتيب موحد.

## Trade-offs

الـ Facade ممكن تكبر وتعمل كل حاجة. المثال مش Transaction: فشل الدفع أو الشحن الحقيقي محتاج تعويض أو طريقة اتساق مناسبة.

## Related Patterns

[Adapter](../adapter/README.ar-EG.md) · [Mediator](../../behavioral/mediator/README.ar-EG.md)

## Common Confusion

Adapter بتعالج التوافق. Facade بتصغّر interface النظام ومش لازم تنفذ interface موجودة.

## Terms to Remember

- `Facade` — وفّر مدخل صغير لخطوات شائعة جوه Subsystem.
- `subsystem` — مجموعة خدمات أو objects بتتعاون جوه نظام أكبر. مثال: `Stock, Payment, Shipping`.
- `interface` — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. مثال: `Checkout::buy`.
- `Client` — الكود اللي بيستخدم interface أو بيتعامل مع objects بتاعة الـ Pattern. مثال: `main`.

## Interview Vocabulary

- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`trade-off`](../../GLOSSARY.md#trade-off) — ميزة بتكسبها قصاد تكلفة أو تنازل في ناحية تانية.

## Interview Question

لو الدفع نجح والشحن فشل، buy تقدر توعد بإيه فعلاً؟

## Mini Challenge

ضيف فشل شحن تجريبي وصمّم نتيجة Refund واضحة بدل نجاح وهمي.

## Quick Summary

- **المشكلة:** كل مستدعي للشراء محتاج يراجع المخزون ويدفع ويطلب الشحن بالترتيب الصح.
- **الحل:** Checkout بتوفر buy وبتنسق الخدمات الداخلية ورا العملية دي.
- **Trade-off:** الـ Facade ممكن تكبر وتعمل كل حاجة. المثال مش Transaction: فشل الدفع أو الشحن الحقيقي محتاج تعويض أو طريقة اتساق مناسبة.
- **افتكر:** باب واحد لكذا خدمة.

[السابق](../../structural/decorator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/flyweight/README.ar-EG.md)
