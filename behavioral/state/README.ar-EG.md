# الحالة

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

خلّي حالة الـ Object الحالية تحدد ردها وانتقالاتها.

## المشكلة

الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.

## حل بسيط في الأول

```cpp
if (open) open = false;
else open = true; // becomes scattered as states and events grow
```

## ليه الحل بيصعّب الدنيا

Boolean كفاية لحالتين، بس نسخ شروط الحالة على أحداث كتير بيخلّي الانتقالات تتعارض.

## الفكرة الأساسية

Door بتفوّض press للـ DoorState الحالية، والحالة تختار اللي بعدها.

## مثال من الحياة

ماكينة البيع بتتعامل مع المدخل حسب الدفع حصل ولا لأ.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الحالة](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

## الأدوار

Door هي السياق، DoorState بتحدد press وname، وOpen وClosed شايلين روابط مش مالكة للحالة التالية. main بتخليهم عايشين أطول من الباب.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
closed
open
closed
```

## إمتى تستخدمه

استخدمه لما السلوك حسب الحالة والانتقالات يتوزعوا على كذا عملية.

## إمتى ما تستخدموش

بلاش لـ Toggle بسيطة أو جدول enum واضح وصغير.

## المميزات

السلوك متجمع حسب الحالة، والانتقالات واضحة في مكانها.

## العيوب والمقايضات

فيه Classes وعلاقات عمر زيادة. الحالات هنا بره Door عشان الانتقال ما يدمرش الحالة وهي لسه بتنفذ؛ التصميم الأكبر لازم يحافظ على الأمان ده.

## استخدامات تقنية

مناسب لجلسات البروتوكولات ودورات عمل الأجهزة لما قواعد الانتقال واضحة.

## أنماط مرتبطة

[strategy](../strategy/README.ar-EG.md) · [observer](../observer/README.ar-EG.md)

## لخبطة شائعة

Strategy غالباً الـ Client بيختارها لخوارزمية. State بتمثل دورة حياة وممكن تختار انتقالها بنفسها.

## سؤال انترفيو

مين بيختار الحالة التالية هنا؟ وإيه الفرق عن اختيار Strategy للشحن؟

## تحدي صغير

ضيف Locked تخلي press ما تفتحش، وحدث unlock منفصل واختبر التسلسل.

## الخلاصة

- **المشكلة:** الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل.
- **الحل:** Door بتفوّض press للـ DoorState الحالية، والحالة تختار اللي بعدها.
- **المقايضة:** فيه Classes وعلاقات عمر زيادة. الحالات هنا بره Door عشان الانتقال ما يدمرش الحالة وهي لسه بتنفذ؛ التصميم الأكبر لازم يحافظ على الأمان ده.
- **افتكر:** نفس الحدث، حالة مختلفة، رد مختلف.

[السابق](../../behavioral/observer/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/strategy/README.ar-EG.md)
