# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

متوسط

## In One Sentence

افصل ناحيتين بيتغيروا، واربطهم بالـ [`composition`](../../GLOSSARY.md#composition) (بتركّب behavior من objects بتستخدم أو بتحتوي objects تانية).

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

class لكل تركيبة أولوية وقناة بتزوّد التركيبات وبتكرر منطق الإرسال.

## The Idea

Notice بتفوّض الإرسال لـ Channel. UrgentNotice بتغيّر الرسالة من غير ما تختار وسيلة النقل.

## Real-World Analogy

الريموت ووصلة الاتصال بتاعته ممكن يتطوروا لوحدهم طالما بينهم بروتوكول صغير.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Bridge](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## Participants

Notice هي الـ [`abstraction`](../../GLOSSARY.md#abstraction) (بتظهر العمليات اللي المستدعي محتاجها وبتخفي التفاصيل اللي مش محتاج يعرفها) ، و UrgentNotice تطوير ليه. Channel عقد الإرسال، و Email و Sms بينفذوه.

الأدوار القياسية في المثال ده:

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — الناحية اللي بتوفر العمليات الأساسية في Bridge وبتفوّض شغل التنفيذ. هنا: `Notice`.
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — تخصيص لـ Abstraction مستقل عن ناحية التنفيذ. هنا: `UrgentNotice`.
- [`Implementor`](../../GLOSSARY.md#implementor) — العقد اللي Abstraction بتستخدمه للشغل في الناحية التانية من Bridge. هنا: `Channel`.
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — implementation محددة لعقد Implementor. هنا: `Email, Sms`.

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

استخدمه لما ناحيتين من التغيير هيعملوا عدد كبير من الـ subclasses لكل التركيبات.

### Use cases

مناسب لأشكال رسم مع Backends مختلفة، أو أنواع تنبيه بقنوات متنوعة.

## When NOT to Use

بلاش لو فيه ناحية بسيطة واحدة ومتغير لـ function كفاية.

## Advantages

القناة الجديدة تشتغل مع أنواع التنبيه الموجودة من غير classes لكل تركيبة.

## Trade-offs

فيه طبقة delegation زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.

## Related Patterns

[Adapter](../adapter/README.ar-EG.md) · [Strategy](../../behavioral/strategy/README.ar-EG.md)

## Common Confusion

Adapter بتصلح عدم توافق موجود. Bridge فصل مقصود لاتجاهين بيتطوروا لوحدهم، وStrategy مركزة على behavior قابل للتبديل.

## Terms to Remember

- `Bridge` — افصل ناحيتين بيتغيروا، واربطهم بالـ composition.
- `Abstraction` — الناحية اللي بتوفر العمليات الأساسية في Bridge وبتفوّض شغل التنفيذ. مثال: `Notice`.
- `Refined Abstraction` — تخصيص لـ Abstraction مستقل عن ناحية التنفيذ. مثال: `UrgentNotice`.
- `Implementor` — العقد اللي Abstraction بتستخدمه للشغل في الناحية التانية من Bridge. مثال: `Channel`.
- `Concrete Implementor` — implementation محددة لعقد Implementor. مثال: `Email, Sms`.

## Interview Vocabulary

- [`object composition`](../../GLOSSARY.md#object-composition) — بتوصل objects ببعض عشان تطلع behavior أو تركيب أكبر.
- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — فضّل objects متعاونة لما تعبر عن التغيير أوضح من تكبير شجرة inheritance.
- [`encapsulate what varies`](../../GLOSSARY.md#encapsulate-what-varies) — حط القرار اللي بيتغير ورا حدود ثابتة وواضحة.

## Interview Question

لو ضفت Push و ScheduledNotice ، هتحتاج كام class باستخدام Bridge ومن غيره؟

## Mini Challenge

ضيف Push واستخدم نوعي التنبيه من غير تعديلهم.

## Quick Summary

- **المشكلة:** التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها.
- **الحل:** Notice بتفوّض الإرسال لـ Channel. UrgentNotice بتغيّر الرسالة من غير ما تختار وسيلة النقل.
- **Trade-off:** فيه طبقة delegation زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.
- **افتكر:** ناحيتين، ووصلة واحدة.

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)
