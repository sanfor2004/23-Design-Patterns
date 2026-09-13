# Bridge

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** افصل ناحيتين بيتغيروا بشكل مستقل، واربطهم عن طريق [`composition`](../../GLOSSARY.md#composition): تركيب الحل من كائنات بتتعاون مع بعض.

## المشكلة

التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها. الـ `class` لكل تركيبة أولوية وقناة بتزوّد التركيبات وبتكرر منطق الإرسال.

## الحل ببساطة

التنبيه ممكن يبقى عادي أو عاجل، والإرسال ممكن يبقى إيميل أو SMS.الـ`Bridge` بيربط التنبيه بقناة إرسال بدل `Class` لكل تركيبة. خلّي `Notice` تفوّض الإرسال لقناة من نوع `Channel`. النوع `UrgentNotice` يقدر يغيّر الرسالة من غير ما يختار وسيلة النقل.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Bridge](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

في المثال، `Notice` هي ناحية [`abstraction`](../../GLOSSARY.md#abstraction): بتعرض العمليات اللي المستدعي محتاجها وتخفي تفاصيل الإرسال. النوع `UrgentNotice` بيخصص الرسالة. عقد الإرسال هو `Channel`، وبيتوفّر له تنفيذان: `Email` و `Sms`.

الأدوار القياسية في المثال ده:

- [`Abstraction`](../../GLOSSARY.md#abstraction-bridge-role) — الناحية اللي بتوفر العمليات الأساسية في `Bridge` وبتفوّض شغل التنفيذ. هنا: `Notice`.
- [`Refined Abstraction`](../../GLOSSARY.md#refined-abstraction) — تخصيص لـ `Abstraction` مستقل عن ناحية التنفيذ. هنا: `UrgentNotice`.
- [`Implementor`](../../GLOSSARY.md#implementor) — العقد اللي `Abstraction` بتستخدمه للشغل في الناحية التانية من `Bridge`. هنا: `Channel`.
- [`Concrete Implementor`](../../GLOSSARY.md#concrete-implementor) — تنفيذ محدد (`implementation`) لعقد `Implementor`. هنا: `Email, Sms`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Email:
    def deliver(self, text):
        print("Email:", text)


class Sms:
    def deliver(self, text):
        print("SMS:", text)


class Notice:
    def __init__(self, channel):
        self.channel = channel

    def send(self):
        self.channel.deliver("status normal")


class UrgentNotice(Notice):
    def send(self):
        self.channel.deliver("URGENT: disk full")


if __name__ == "__main__":
    Notice(Email()).send()
    UrgentNotice(Email()).send()
    UrgentNotice(Sms()).send()
```

### Python output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## C++20 example

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

### C++20 output

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## قارن اللغتين

Both examples use Composition to separate notice type from delivery channel. Python retains a channel reference and relies on `deliver`; C++ borrows an Object implementing Channel, so its Lifetime must cover the notice.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما ناحيتين من التغيير هيعملوا عدد كبير من الـ `subclasses` لكل التركيبات.

### Use cases

مناسب لأشكال رسم مع `Backends` مختلفة، أو أنواع تنبيه بقنوات متنوعة.

**التكلفة:** فيه طبقة `delegation` زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.

## جرّب تجاوب

1. إيه الـ`Classes` اللي هتتغير لو ضفت قناة إرسال بس؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Push` واستخدم نوعي التنبيه من غير تعديلهم.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
