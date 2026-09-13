# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** وفّق طريقة التعامل الحالية مع العقد اللي الكود المستدعي (`Client`) محتاجه. العقد ده بنسميه [`interface`](../../GLOSSARY.md#interface): بيحدد العمليات المتاحة والنتيجة المتوقعة منها.

## المشكلة

لوحة العرض مستنية `Celsius`، بس الحساس الموجود بيرجع `Fahrenheit`. تمرير الرقم زي ما هو بيعرض وحدة غلط. وتكرار معادلة التحويل في كذا مكان بيكرر قاعدة التوافق.

## الحل ببساطة

الحساس بيرجع فهرنهايت، والعرض محتاج مئوية.الـ`Adapter` بيحوّل الاستدعاء والقيمة من غير تعديل الطرفين. اعمل طبقة توافق من نوع `CelsiusAdapter` بتنفّذ العقد `Temperature`. الطبقة بتستعير الحساس القديم `LegacyThermometer`، وبتحوّل وحدات القياس عند الحد الفاصل.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Adapter](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

في المثال، العقد المطلوب هو `Temperature`، والحساس القديم هو `LegacyThermometer`. طبقة التوافق `CelsiusAdapter` بتستعير الحساس وبتحوّل القيمة. دالة العرض `display` بتتعامل مع العقد المطلوب بس.

الأدوار القياسية في المثال ده:

- [`Target`](../../GLOSSARY.md#target) — الـ `interface` اللي `Client` متوقع يتعامل معاها. هنا: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — الـ `object` الموجودة اللي `interface` بتاعتها محتاجة تتوافق مع المطلوب. هنا: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Temperature`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class LegacyThermometer:
    def fahrenheit(self):
        return 77.0


class CelsiusAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def celsius(self):
        return (self.sensor.fahrenheit() - 32) * 5 / 9


def display(temperature):
    print(temperature.celsius(), "C")


if __name__ == "__main__":
    display(CelsiusAdapter(LegacyThermometer()))
```

### Python output

```text
25.0 C
```

## C++20 example

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

### C++20 output

```text
25 C
```

## قارن اللغتين

Python accepts any Object with `celsius`; C++ declares Temperature as an Interface. The Python Adapter retains its sensor. The C++ reference borrows it, so the sensor must outlive the Adapter.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه عند التعامل مع `API` موجودة مش قادر أو مش مناسب تغيّرها.

### Use cases

مناسب لربط `APIs` قديمة وتحويل وحدات؛ الدقة والتعامل مع الأخطاء محتاجين اتفاق واضح.

**التكلفة:** تغيير أسماء الـ `methods` بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ `Adapter` لأن الـ `reference` مش مالكة.

## جرّب تجاوب

1. مين بيحوّل الوحدات، ومين مسؤول عن `Lifetime` الحساس؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** خلّي `Fahrenheit` قابلة للتغيير، واختبر نقطتي التجمد والغليان.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
