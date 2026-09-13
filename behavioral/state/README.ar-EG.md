# State

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

متوسط

## In One Sentence

خلّي الحالة الحالية للكائن (`state`) هي اللي تحدد استجابته والانتقالات المتاحة ليه.

## ببساطة

ضغطة زر الباب بتفتحه لو مقفول وبتقفله لو مفتوح.الـ`State` بينقل الاستجابة والانتقال للـ`Object` اللي بتمثل الوضع الحالي.

## The Problem

الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.

## Naive Solution

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## Why It Becomes a Problem

الـ `Boolean` كفاية لحالتين، بس نسخ شروط الـ `state` على `events` كتير بيخلّي الانتقالات تتعارض.

## The Idea

خلّي الباب `Door` يفوّض العملية `press` للحالة الحالية من نوع `DoorState`. تنفيذ الحالة هو اللي بيحدد الحالة التالية.

## Real-World Analogy

ماكينة البيع بتتعامل مع المدخل حسب الدفع حصل ولا لأ.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## Participants

في المثال، الباب `Door` بيلعب دور `Context`. العقد `DoorState` بيحدد العمليتين `press` و `name`. الحالتان `Open` و `Closed` بيحتفظوا بروابط مش مالكة للحالة التالية. الدالة `main` بتخلي الحالتين موجودتين لمدة أطول من الباب.

الأدوار القياسية في المثال ده:

- [`Context`](../../GLOSSARY.md#context) — الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). هنا: `Door`.
- [`State interface`](../../GLOSSARY.md#state-interface) — العقد اللي `Context` بتفوّض من خلاله `behavior` المعتمدة على `state`. هنا: `DoorState`.
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — تنفيذ لحالة معينة (`Concrete State`) بيحدد سلوكها (`behavior`) والانتقالات المتاحة منها. هنا: `Open, Closed`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

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

استخدمه لما الـ `behavior` حسب الـ `state` والانتقالات يتوزعوا على كذا عملية.

### Use cases

مناسب لجلسات البروتوكولات ودورات عمل الأجهزة لما قواعد الانتقال واضحة.

## When NOT to Use

بلاش لو المطلوب تبديل بسيط (`toggle`)، أو لو جدول صغير باستخدام `enum` بيعبّر عن الحالات بوضوح.

## Advantages

الـ `behavior` متجمع حسب الـ `state`، والانتقالات واضحة في مكانها.

## Trade-offs

التصميم بيضيف أنواع جديدة (`classes`)، ولازم تتابع عمر الكائنات وعلاقتها ببعض. المقصود بـ [`lifetime`](../../GLOSSARY.md#lifetime) هو الفترة اللي الكائن موجود فيها وينفع تستخدمه. الحالات في المثال موجودة بره الباب `Door`؛ عشان كده، الانتقال مش بيدمر الحالة وهي لسه بتنفّذ. حافظ على الضمان ده في التصميم الأكبر.

## Related Patterns

[Strategy](../strategy/README.ar-EG.md) · [Observer](../observer/README.ar-EG.md)

## Common Confusion

في `Strategy`، المستدعي (`Client`) غالبًا بيختار طريقة الحل (`algorithm`). أما `State`، فبتمثل مرحلة من دورة عمل الكيان وممكن تحدد الانتقال التالي بنفسها. دورة العمل اسمها [`lifecycle`](../../GLOSSARY.md#lifecycle)، ودي مختلفة عن عمر الكائن في الذاكرة (`lifetime`).

## Terms to Remember

- `State` — خلّي الحالة الحالية للكائن (`state`) هي اللي تحدد استجابته والانتقالات المتاحة ليه.
- `Context` — الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). مثال: `Door`.
- `State interface` — العقد اللي `Context` بتفوّض من خلاله `behavior` المعتمدة على `state`. مثال: `DoorState`.
- `Concrete State` — تنفيذ لحالة معينة (`Concrete State`) بيحدد سلوكها (`behavior`) والانتقالات المتاحة منها. مثال: `Open, Closed`.

## Interview Vocabulary

- [`state transition`](../../GLOSSARY.md#state-transition) — انتقال من وضع ممثّل في التصميم لوضع تاني بعد `event`.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — اللي البرنامج بيعمله وهو شغال، بما فيه `behavior` بتتحدد من المدخلات.
- [`delegation`](../../GLOSSARY.md#delegation) — الكائن بيفوّض جزء من شغله لكائن متعاون معاه (`object`)، بدل ما ينفّذ كل حاجة بنفسه.

## Interview Question

مين بيختار الـ `state` التالية هنا؟ وإيه الفرق عن اختيار `Strategy` للشحن؟

## Mini Challenge

ضيف `Locked` تخلي `press` ما تفتحش، وحدث `unlock` منفصل واختبر التسلسل.

## اختبر فهمك

1. مين بيختار الـ`State` اللي بعدها لما نضغط زر الباب؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.
- **الحل:** خلّي الباب `Door` يفوّض العملية `press` للحالة الحالية من نوع `DoorState`. تنفيذ الحالة هو اللي بيحدد الحالة التالية.
- **`Trade-off`:** التصميم بيضيف أنواع جديدة (`classes`)، ولازم تتابع عمر الكائنات وعلاقتها ببعض. المقصود بـ `lifetime` هو الفترة اللي الكائن موجود فيها وينفع تستخدمه. الحالات في المثال موجودة بره الباب `Door`؛ عشان كده، الانتقال مش بيدمر الحالة وهي لسه بتنفّذ. حافظ على الضمان ده في التصميم الأكبر.
- **افتكر:** نفس الـ `event`، حالة مختلفة، رد مختلف.

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)
