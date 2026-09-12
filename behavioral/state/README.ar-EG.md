# State

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

متوسط

## In One Sentence

خلّي state بتاعة الـ object الحالية تحدد ردها وانتقالاتها.

## The Problem

الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.

## Naive Solution

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Why It Becomes a Problem

Boolean كفاية لحالتين، بس نسخ شروط الـ state على events كتير بيخلّي الانتقالات تتعارض.

## The Idea

Door بتفوّض press للـ DoorState الحالية، والـ state تختار اللي بعدها.

## Real-World Analogy

ماكينة البيع بتتعامل مع المدخل حسب الدفع حصل ولا لأ.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Participants

Door هي الـ Context ، DoorState بتحدد press و name ، و Open و Closed شايلين روابط مش مالكة للـ state التالية. main بتخليهم عايشين أطول من الباب.

الأدوار القياسية في المثال ده:

- [`Context`](../../GLOSSARY.md#context) — الـ object اللي بتستخدم Strategy أو بتفوّض behavior للـ State الحالية. هنا: `Door`.
- [`State interface`](../../GLOSSARY.md#state-interface) — العقد اللي Context بتفوّض من خلاله behavior المعتمدة على state. هنا: `DoorState`.
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — implementation بتحدد behavior والانتقالات لوضع State واحد. هنا: `Open, Closed`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string_view>

class Door;
struct DoorState {
    virtual ~DoorState() = default;
    virtual void press(Door& door) const = 0;
    virtual std::string_view name() const = 0;
};
class Door {
    const DoorState* state_;
public:
    explicit Door(const DoorState& state) : state_(&state) {}
    void change(const DoorState& state) { state_ = &state; }
    void press() { state_->press(*this); }
    std::string_view name() const { return state_->name(); }
};
struct Open final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "open"; }
};
struct Closed final : DoorState {
    const DoorState* next = nullptr;
    void press(Door& door) const override { if (next) door.change(*next); }
    std::string_view name() const override { return "closed"; }
};
int main() {
    Open open;
    Closed closed;
    open.next = &closed;
    closed.next = &open;
    Door door{closed};
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
    door.press();
    std::cout << door.name() << '\n';
}
```

## Example Output

```text
closed
open
closed
```

## When to Use

استخدمه لما الـ behavior حسب الـ state والانتقالات يتوزعوا على كذا عملية.

### Use cases

مناسب لجلسات البروتوكولات ودورات عمل الأجهزة لما قواعد الانتقال واضحة.

## When NOT to Use

بلاش لـ Toggle بسيطة أو جدول enum واضح وصغير.

## Advantages

الـ behavior متجمع حسب الـ state ، والانتقالات واضحة في مكانها.

## Trade-offs

فيه classes وعلاقات [`lifetime`](../../GLOSSARY.md#lifetime) (الفترة اللي الـ object موجودة فيها وينفع تستخدمها حسب قواعدها) زيادة. الـ states هنا بره Door عشان الانتقال ما يدمرش الـ state وهي لسه بتنفذ؛ التصميم الأكبر لازم يحافظ على الأمان ده.

## Related Patterns

[Strategy](../strategy/README.ar-EG.md) · [Observer](../observer/README.ar-EG.md)

## Common Confusion

Strategy غالباً الـ Client بيختارها لـ algorithm. State بتمثل [`lifecycle`](../../GLOSSARY.md#lifecycle) (المراحل والانتقالات اللي بنمثلها لكيان في المشكلة؛ مش نفس lifetime بتاعة object في C++) وممكن تختار انتقالها بنفسها.

## Terms to Remember

- `State` — خلّي state بتاعة الـ object الحالية تحدد ردها وانتقالاتها.
- `Context` — الـ object اللي بتستخدم Strategy أو بتفوّض behavior للـ State الحالية. مثال: `Door`.
- `State interface` — العقد اللي Context بتفوّض من خلاله behavior المعتمدة على state. مثال: `DoorState`.
- `Concrete State` — implementation بتحدد behavior والانتقالات لوضع State واحد. مثال: `Open, Closed`.

## Interview Vocabulary

- [`state transition`](../../GLOSSARY.md#state-transition) — انتقال من وضع ممثّل في التصميم لوضع تاني بعد event.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — اللي البرنامج بيعمله وهو شغال، بما فيه behavior بتتحدد من المدخلات.
- [`delegation`](../../GLOSSARY.md#delegation) — object بتطلب من object متعاونة معاها تنفذ جزء من الشغل.

## Interview Question

مين بيختار الـ state التالية هنا؟ وإيه الفرق عن اختيار Strategy للشحن؟

## Mini Challenge

ضيف Locked تخلي press ما تفتحش، وحدث unlock منفصل واختبر التسلسل.

## Quick Summary

- **المشكلة:** الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.
- **الحل:** Door بتفوّض press للـ DoorState الحالية، والـ state تختار اللي بعدها.
- **Trade-off:** فيه classes وعلاقات lifetime زيادة. الـ states هنا بره Door عشان الانتقال ما يدمرش الـ state وهي لسه بتنفذ؛ التصميم الأكبر لازم يحافظ على الأمان ده.
- **افتكر:** نفس الـ event ، حالة مختلفة، رد مختلف.

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)
