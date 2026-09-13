# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** انسخ نموذج متجهّز عشان تنشئ كائن مستقل (`object`) وتعدّله من غير ما تغيّر الأصل.

## المشكلة

اللعبة محتاجة تنسخ أعداء من نموذج جاهز، لكن كود إنشاء الأعداء (`spawn`) مش عارف النوع الفعلي. النموذج هنا مش `template` بالمعنى الخاص بلغة `C++`. إنشاء `Guard` افتراضية كل مرة بيكرر التجهيز وبيضيّع أي معدات مخصصة في النموذج.

## الحل ببساطة

اللعبة فيها حارس متجهّز بالمعدات المطلوبة.الـ`Prototype` بينسخ التجهيز ده عشان تغيّر النسخة الجديدة من غير ما تغيّر الأصل. وفّر العملية `clone` في العقد `Enemy`. عند نسخ `Guard`، انسخ البيانات المخزّنة بالقيمة (`value members`). ارجع الكائن المستقل داخل [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr)، وهو مؤشر بملكية حصرية بيحرر الكائن تلقائيًا مع المالك.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

في المثال، `Enemy` بتحدد عقد النسخ حسب النوع الفعلي (`polymorphic cloning`)، و `Guard` بتنفّذه. المستدعي (`Client`) بيمتلك النسخة الجديدة ويغيّر اسمها.

الأدوار القياسية في المثال ده:

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — كائن بيوفّر العملية `clone` لإنشاء كائن تاني (`object`) من القيم المتجهّزة. هنا: `Guard`.
- [`deep copy`](../../GLOSSARY.md#deep-copy) — بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل. هنا: `Guard::clone`.
- [`value semantics`](../../GLOSSARY.md#value-semantics) — النسخ تتعامل كقيم مستقلة حسب عقد النوع. هنا: `name_, equipment_`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Guard:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment

    def clone(self):
        return Guard(self.name, self.equipment.copy())

    def describe(self):
        print(self.name + ": " + ", ".join(self.equipment))


def main():
    prototype = Guard("template", ["shield", "spear"])
    guard = prototype.clone()
    guard.name = "gate guard"
    guard.equipment.append("helmet")
    prototype.describe()
    guard.describe()


if __name__ == "__main__":
    main()
```

### Python output

```text
template: shield, spear
gate guard: shield, spear, helmet
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

struct Enemy {
    virtual ~Enemy() = default;
    virtual std::unique_ptr<Enemy> clone() const = 0;
    virtual void rename(std::string name) = 0;
    virtual void describe() const = 0;
};
class Guard final : public Enemy {
    std::string name_ = "template";
    std::vector<std::string> equipment_{"shield", "spear"};
public:
    std::unique_ptr<Enemy> clone() const override { return std::make_unique<Guard>(*this); }
    void rename(std::string name) override { name_ = std::move(name); }
    void describe() const override {
        std::cout << name_ << ": " << equipment_.size() << " items\n";
    }
};
int main() {
    const Guard prototype;
    auto copy = prototype.clone();
    copy->rename("gate guard");
    prototype.describe();
    copy->describe();
}
```

### C++20 output

```text
template: 2 items
gate guard: 2 items
```

## قارن اللغتين

Assignment in Python shares an Object. This clone copies the equipment list explicitly; its strings are immutable. C++ copies the vector by value inside a polymorphic `clone`. Nested mutable data would require a deliberate deeper copy in Python; `copy.deepcopy` is an option, not a universal resource-copy policy.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما الـ `objects` الموجودة شايلة إعداد مهم، والـ `Client` مش المفروض يعيد بناء نوعها الفعلي.

### Use cases

مناسب لقوالب كيانات الألعاب والمستندات؛ المثال بينسخ `string` و `std::vector` بالقيمة.

**التكلفة:** لو فيه `pointers` لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. الـ `Socket` مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.

## جرّب تجاوب

1. هل إسناد الأصل لمتغير تاني بيعمل نسخة مستقلة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** خلّي المعدات قابلة للتعديل، واتأكد إن تعديل النسخة مايمسش الأصل.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
