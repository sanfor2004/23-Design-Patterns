# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — بيركز على تركيب الـ`Objects` والـ`Classes` عشان تتعاون.

## Difficulty

متوسط

## In One Sentence

افصل ناحيتين بيتغيروا بشكل مستقل، واربطهم عن طريق [`composition`](../../GLOSSARY.md#composition): تركيب الحل من كائنات بتتعاون مع بعض.

## ببساطة

التنبيه ممكن يبقى عادي أو عاجل، والإرسال ممكن يبقى إيميل أو SMS.الـ`Bridge` بيربط التنبيه بقناة إرسال بدل `Class` لكل تركيبة.

## The Problem

التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها.

## Naive Solution

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## Why It Becomes a Problem

الـ `class` لكل تركيبة أولوية وقناة بتزوّد التركيبات وبتكرر منطق الإرسال.

## The Idea

خلّي `Notice` تفوّض الإرسال لقناة من نوع `Channel`. النوع `UrgentNotice` يقدر يغيّر الرسالة من غير ما يختار وسيلة النقل.

## Real-World Analogy

الريموت ووصلة الاتصال بتاعته ممكن يتطوروا لوحدهم طالما بينهم بروتوكول صغير.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Bridge](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## Participants

في المثال، `Notice` هي ناحية [`abstraction`](../../GLOSSARY.md#abstraction): بتعرض العمليات اللي المستدعي محتاجها وتخفي تفاصيل الإرسال. النوع `UrgentNotice` بيخصص الرسالة. عقد الإرسال هو `Channel`، وبيتوفّر له تنفيذان: `Email` و `Sms`.

الأدوار القياسية في المثال ده:

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — الناحية اللي بتوفر العمليات الأساسية في `Bridge` وبتفوّض شغل التنفيذ. هنا: `Notice`.
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — تخصيص لـ `Abstraction` مستقل عن ناحية التنفيذ. هنا: `UrgentNotice`.
- [`Implementor`](../../GLOSSARY.md#implementor) — العقد اللي `Abstraction` بتستخدمه للشغل في الناحية التانية من `Bridge`. هنا: `Channel`.
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — تنفيذ محدد (`implementation`) لعقد `Implementor`. هنا: `Email, Sms`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string_view>

struct Channel {
    virtual ~Channel() = default;
    virtual void deliver(std::string_view text) const = 0;
};
struct Email final : Channel {
    void deliver(std::string_view text) const override { std::cout << "Email: " << text << '\n'; }
};
struct Sms final : Channel {
    void deliver(std::string_view text) const override { std::cout << "SMS: " << text << '\n'; }
};
class Notice {
protected:
    const Channel& channel_;
public:
    explicit Notice(const Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void send() const { channel_.deliver("status normal"); }
};
class UrgentNotice final : public Notice {
public:
    using Notice::Notice;
    void send() const override { channel_.deliver("URGENT: disk full"); }
};
int main() {
    const Email email;
    const Sms sms;
    Notice{email}.send();
    UrgentNotice{email}.send();
    UrgentNotice{sms}.send();
}
```

## Example Output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## When to Use

استخدمه لما ناحيتين من التغيير هيعملوا عدد كبير من الـ `subclasses` لكل التركيبات.

### Use cases

مناسب لأشكال رسم مع `Backends` مختلفة، أو أنواع تنبيه بقنوات متنوعة.

## When NOT to Use

بلاش لو فيه ناحية بسيطة واحدة ومتغير لـ `function` كفاية.

## Advantages

القناة الجديدة تشتغل مع أنواع التنبيه الموجودة من غير `classes` لكل تركيبة.

## Trade-offs

فيه طبقة `delegation` زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.

## Related Patterns

[Adapter](../adapter/README.ar-EG.md) · [Strategy](../../behavioral/strategy/README.ar-EG.md)

## Common Confusion

الـ `Adapter` بتصلح عدم توافق موجود. الـ `Bridge` فصل مقصود لاتجاهين بيتطوروا لوحدهم، و `Strategy` مركزة على `behavior` قابل للتبديل.

## Terms to Remember

- `Bridge` — افصل ناحيتين بيتغيروا بشكل مستقل، واربطهم عن طريق التركيب (`composition`).
- `Abstraction` — الناحية اللي بتوفر العمليات الأساسية في `Bridge` وبتفوّض شغل التنفيذ. مثال: `Notice`.
- `Refined Abstraction` — تخصيص لـ `Abstraction` مستقل عن ناحية التنفيذ. مثال: `UrgentNotice`.
- `Implementor` — العقد اللي `Abstraction` بتستخدمه للشغل في الناحية التانية من `Bridge`. مثال: `Channel`.
- `Concrete Implementor` — تنفيذ محدد (`implementation`) لعقد `Implementor`. مثال: `Email, Sms`.

## Interview Vocabulary

- [`object composition`](../../GLOSSARY.md#object-composition) — بتوصل الكائنات (`objects`) ببعض عشان تبني سلوك متكامل (`behavior`) أو تركيب أكبر.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — فضّل تركيب الحل من كائنات متعاونة (`objects`)، لما ده يكون أوضح من توسيع شجرة الوراثة (`inheritance`).
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — حط القرار اللي بيتغير ورا حدود ثابتة وواضحة.

## Interview Question

لو ضفت `Push` و `ScheduledNotice`، هتحتاج كام `class` باستخدام `Bridge` ومن غيره؟

## Mini Challenge

ضيف `Push` واستخدم نوعي التنبيه من غير تعديلهم.

## اختبر فهمك

1. إيه الـ`Classes` اللي هتتغير لو ضفت قناة إرسال بس؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها.
- **الحل:** خلّي `Notice` تفوّض الإرسال لقناة من نوع `Channel`. النوع `UrgentNotice` يقدر يغيّر الرسالة من غير ما يختار وسيلة النقل.
- **`Trade-off`:** فيه طبقة `delegation` زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.
- **افتكر:** ناحيتين، ووصلة واحدة.

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)
