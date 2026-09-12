# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

مبتدئ

## In One Sentence

حوّل [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها) موجودة للشكل اللي الـ Client مستنيه.

## The Problem

لوحة العرض مستنية Celsius ، بس الحساس الموجود بيرجع Fahrenheit.

## Naive Solution

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Why It Becomes a Problem

تمرير الرقم زي ما هو بيعرض وحدة غلط. وتكرار معادلة التحويل في كذا مكان بيكرر قاعدة التوافق.

## The Idea

اعمل Temperature حوالين LegacyThermometer مستعارة، وحوّل الوحدات عند الحد الفاصل.

## Real-World Analogy

زي وصلة كهربا للسفر؛ هنا الوصلة بتحوّل معنى القيمة كمان.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Adapter](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## Participants

Temperature هي الـ interface المطلوبة، و LegacyThermometer هي القديمة. CelsiusAdapter بتستعيرها، و display بتعرف Temperature بس.

الأدوار القياسية في المثال ده:

- [`Target`](../../GLOSSARY.md#target) — الـ interface اللي Client متوقع يتعامل معاها. هنا: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — الـ object الموجودة اللي interface بتاعتها محتاجة تتوافق مع المطلوب. هنا: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Temperature`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <stdexcept>

class LegacyThermometer {
public:
    double fahrenheit() const { return 77.0; }
};
struct Temperature {
    virtual ~Temperature() = default;
    virtual double celsius() const = 0;
};
class CelsiusAdapter final : public Temperature {
    const LegacyThermometer& sensor_;
public:
    explicit CelsiusAdapter(const LegacyThermometer& sensor) : sensor_(sensor) {}
    double celsius() const override { return (sensor_.fahrenheit() - 32.0) * 5.0 / 9.0; }
};
void display(const Temperature& temperature) {
    std::cout << temperature.celsius() << " C\n";
}
int main() {
    const LegacyThermometer sensor;
    const CelsiusAdapter adapter{sensor};
    display(adapter);
}
```

## Example Output

```text
25 C
```

## When to Use

استخدمه عند التعامل مع API موجودة مش قادر أو مش مناسب تغيّرها.

### Use cases

مناسب لربط APIs قديمة وتحويل وحدات؛ الدقة والتعامل مع الأخطاء محتاجين اتفاق واضح.

## When NOT to Use

بلاش لو أنت مالك الطرفين وتوحيد الـ interface أبسط.

## Advantages

التحويل في مكان واحد، والعرض يقبل أي [`implementation`](../../GLOSSARY.md#implementation) (الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد interface) لـ Temperature.

## Trade-offs

تغيير أسماء الـ methods بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ Adapter لأن الـ reference مش مالكة.

## Related Patterns

[Facade](../facade/README.ar-EG.md) · [Bridge](../bridge/README.ar-EG.md)

## Common Confusion

Facade بتبسّط Subsystem. Adapter بتخلّي interface بعينها متوافقة مع عقد مطلوب.

## Terms to Remember

- `Adapter` — حوّل interface موجودة للشكل اللي الـ Client مستنيه.
- `Target` — الـ interface اللي Client متوقع يتعامل معاها. مثال: `Temperature`.
- `Adaptee` — الـ object الموجودة اللي interface بتاعتها محتاجة تتوافق مع المطلوب. مثال: `LegacyThermometer`.
- `interface` — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. مثال: `Temperature`.

## Interview Vocabulary

- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — اعتمد على العقد المعلن بدل تفاصيل implementation بعينها.
- [`delegation`](../../GLOSSARY.md#delegation) — object بتطلب من object متعاونة معاها تنفذ جزء من الشغل.
- [`lifetime`](../../GLOSSARY.md#lifetime) — الفترة اللي الـ object موجودة فيها وينفع تستخدمها حسب قواعدها.

## Interview Question

هل ينفع دايماً تحافظ على الـ behavior لو المصدر Async والـ interface المطلوبة Sync ؟

## Mini Challenge

خلّي Fahrenheit قابلة للتغيير، واختبر نقطتي التجمد والغليان.

## Quick Summary

- **المشكلة:** لوحة العرض مستنية Celsius ، بس الحساس الموجود بيرجع Fahrenheit.
- **الحل:** اعمل Temperature حوالين LegacyThermometer مستعارة، وحوّل الوحدات عند الحد الفاصل.
- **Trade-off:** تغيير أسماء الـ methods بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ Adapter لأن الـ reference مش مالكة.
- **افتكر:** حوّل عند نقطة الاتصال.

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)
