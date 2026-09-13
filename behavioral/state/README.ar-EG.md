# State

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** خلّي الحالة الحالية للكائن (`state`) هي اللي تحدد استجابته والانتقالات المتاحة ليه.

## المشكلة

الباب بيرد على نفس الزر بشكل مختلف وهو مفتوح أو مقفول؛ أجهزة أكبر فيها قفل أو عطل. الـ `Boolean` كفاية لحالتين، بس نسخ شروط الـ `state` على `events` كتير بيخلّي الانتقالات تتعارض.

## الحل ببساطة

ضغطة زر الباب بتفتحه لو مقفول وبتقفله لو مفتوح.الـ`State` بينقل الاستجابة والانتقال للـ`Object` اللي بتمثل الوضع الحالي. خلّي الباب `Door` يفوّض العملية `press` للحالة الحالية من نوع `DoorState`. تنفيذ الحالة هو اللي بيحدد الحالة التالية.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال State](../../assets/diagrams/state.svg)

```text
Door::press()  -->  DoorState  -->  Open ↔ Closed
```

في المثال، الباب `Door` بيلعب دور `Context`. العقد `DoorState` بيحدد العمليتين `press` و `name`. الحالتان `Open` و `Closed` بيحتفظوا بروابط مش مالكة للحالة التالية. الدالة `main` بتخلي الحالتين موجودتين لمدة أطول من الباب.

الأدوار القياسية في المثال ده:

- [`Context`](../../GLOSSARY.md#context) — الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). هنا: `Door`.
- [`State interface`](../../GLOSSARY.md#state-interface) — العقد اللي `Context` بتفوّض من خلاله `behavior` المعتمدة على `state`. هنا: `DoorState`.
- [`Concrete State`](../../GLOSSARY.md#concrete-state) — تنفيذ لحالة معينة (`Concrete State`) بيحدد سلوكها (`behavior`) والانتقالات المتاحة منها. هنا: `Open, Closed`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Closed:
    name = "closed"

    def press(self, door):
        door.state = Open()


class Open:
    name = "open"

    def press(self, door):
        door.state = Closed()


class Door:
    def __init__(self):
        self.state = Closed()

    def press(self):
        self.state.press(self)


if __name__ == "__main__":
    door = Door()
    print(door.state.name)
    door.press()
    print(door.state.name)
    door.press()
    print(door.state.name)
```

### Python output

```text
closed
open
closed
```

## C++20 example

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

### C++20 output

```text
closed
open
closed
```

## قارن اللغتين

Python creates a new stateless State Object for each transition. C++ reuses Open and Closed Objects through borrowed pointers; they must outlive Door. Both move transition behavior into State Objects. A boolean toggle is simpler for this tiny domain.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما الـ `behavior` حسب الـ `state` والانتقالات يتوزعوا على كذا عملية.

### Use cases

مناسب لجلسات البروتوكولات ودورات عمل الأجهزة لما قواعد الانتقال واضحة.

**التكلفة:** التصميم بيضيف أنواع جديدة (`classes`)، ولازم تتابع عمر الكائنات وعلاقتها ببعض. المقصود بـ [`lifetime`](../../GLOSSARY.md#lifetime) هو الفترة اللي الكائن موجود فيها وينفع تستخدمه. الحالات في المثال موجودة بره الباب `Door`؛ عشان كده، الانتقال مش بيدمر الحالة وهي لسه بتنفّذ. حافظ على الضمان ده في التصميم الأكبر.

## جرّب تجاوب

1. مين بيختار الـ`State` اللي بعدها لما نضغط زر الباب؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Locked` تخلي `press` ما تفتحش، وحدث `unlock` منفصل واختبر التسلسل.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
