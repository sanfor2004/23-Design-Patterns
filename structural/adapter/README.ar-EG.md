# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — بيركز على تركيب الـ`Objects` والـ`Classes` عشان تتعاون.

## Difficulty

مبتدئ

## In One Sentence

وفّق طريقة التعامل الحالية مع العقد اللي الكود المستدعي (`Client`) محتاجه. العقد ده بنسميه [`interface`](../../GLOSSARY.md#interface): بيحدد العمليات المتاحة والنتيجة المتوقعة منها.

## ببساطة

الحساس بيرجع فهرنهايت، والعرض محتاج مئوية.الـ`Adapter` بيحوّل الاستدعاء والقيمة من غير تعديل الطرفين.

## The Problem

لوحة العرض مستنية `Celsius`، بس الحساس الموجود بيرجع `Fahrenheit`.

## Naive Solution

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## Why It Becomes a Problem

تمرير الرقم زي ما هو بيعرض وحدة غلط. وتكرار معادلة التحويل في كذا مكان بيكرر قاعدة التوافق.

## The Idea

اعمل طبقة توافق من نوع `CelsiusAdapter` بتنفّذ العقد `Temperature`. الطبقة بتستعير الحساس القديم `LegacyThermometer`، وبتحوّل وحدات القياس عند الحد الفاصل.

## Real-World Analogy

زي وصلة كهربا للسفر؛ هنا الوصلة بتحوّل معنى القيمة كمان.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Adapter](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## Participants

في المثال، العقد المطلوب هو `Temperature`، والحساس القديم هو `LegacyThermometer`. طبقة التوافق `CelsiusAdapter` بتستعير الحساس وبتحوّل القيمة. دالة العرض `display` بتتعامل مع العقد المطلوب بس.

الأدوار القياسية في المثال ده:

- [`Target`](../../GLOSSARY.md#target) — الـ `interface` اللي `Client` متوقع يتعامل معاها. هنا: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — الـ `object` الموجودة اللي `interface` بتاعتها محتاجة تتوافق مع المطلوب. هنا: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Temperature`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

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

استخدمه عند التعامل مع `API` موجودة مش قادر أو مش مناسب تغيّرها.

### Use cases

مناسب لربط `APIs` قديمة وتحويل وحدات؛ الدقة والتعامل مع الأخطاء محتاجين اتفاق واضح.

## When NOT to Use

بلاش لو أنت مالك الطرفين وتوحيد الـ `interface` أبسط.

## Advantages

التحويل في مكان واحد، والعرض يقبل أي [`implementation`](../../GLOSSARY.md#implementation) لـ `Temperature`.

## Trade-offs

تغيير أسماء الـ `methods` بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ `Adapter` لأن الـ `reference` مش مالكة.

## Related Patterns

[Facade](../facade/README.ar-EG.md) · [Bridge](../bridge/README.ar-EG.md)

## Common Confusion

الـ `Facade` بتبسّط `Subsystem`. الـ `Adapter` بتخلّي `interface` بعينها متوافقة مع عقد مطلوب.

## Terms to Remember

- `Adapter` — وفّق طريقة التعامل الحالية (`interface`) مع العقد اللي الكود المستدعي (`Client`) محتاجه.
- `Target` — الـ `interface` اللي `Client` متوقع يتعامل معاها. مثال: `Temperature`.
- `Adaptee` — الـ `object` الموجودة اللي `interface` بتاعتها محتاجة تتوافق مع المطلوب. مثال: `LegacyThermometer`.
- `interface` — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. مثال: `Temperature`.

## Interview Vocabulary

- [`program to an interface, not an implementation`](../../GLOSSARY.md#program-to-an-interface-not-an-implementation) — اعتمد على العقد المعلن بدل تفاصيل `implementation` بعينها.
- [`delegation`](../../GLOSSARY.md#delegation) — الكائن بيفوّض جزء من شغله لكائن متعاون معاه (`object`)، بدل ما ينفّذ كل حاجة بنفسه.
- [`lifetime`](../../GLOSSARY.md#lifetime) — الفترة اللي الـ `object` موجودة فيها وينفع تستخدمها حسب قواعدها.

## Interview Question

هل ينفع دايماً تحافظ على الـ `behavior` لو المصدر `Async` والـ `interface` المطلوبة `Sync`؟

## Mini Challenge

خلّي `Fahrenheit` قابلة للتغيير، واختبر نقطتي التجمد والغليان.

## اختبر فهمك

1. مين بيحوّل الوحدات، ومين مسؤول عن `Lifetime` الحساس؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** لوحة العرض مستنية `Celsius`، بس الحساس الموجود بيرجع `Fahrenheit`.
- **الحل:** اعمل طبقة توافق من نوع `CelsiusAdapter` بتنفّذ العقد `Temperature`. الطبقة بتستعير الحساس القديم `LegacyThermometer`، وبتحوّل وحدات القياس عند الحد الفاصل.
- **`Trade-off`:** تغيير أسماء الـ `methods` بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ `Adapter` لأن الـ `reference` مش مالكة.
- **افتكر:** حوّل عند نقطة الاتصال.

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)
