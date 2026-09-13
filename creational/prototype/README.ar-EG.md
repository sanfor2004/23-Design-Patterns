# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — بيركز على إنشاء الـ`Objects` وإعدادها.

## Difficulty

متوسط

## In One Sentence

انسخ نموذج متجهّز عشان تنشئ كائن مستقل (`object`) وتعدّله من غير ما تغيّر الأصل.

## ببساطة

اللعبة فيها حارس متجهّز بالمعدات المطلوبة.الـ`Prototype` بينسخ التجهيز ده عشان تغيّر النسخة الجديدة من غير ما تغيّر الأصل.

## The Problem

اللعبة محتاجة تنسخ أعداء من نموذج جاهز، لكن كود إنشاء الأعداء (`spawn`) مش عارف النوع الفعلي. النموذج هنا مش `template` بالمعنى الخاص بلغة `C++`.

## Naive Solution

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Why It Becomes a Problem

إنشاء `Guard` افتراضية كل مرة بيكرر التجهيز وبيضيّع أي معدات مخصصة في النموذج.

## The Idea

وفّر العملية `clone` في العقد `Enemy`. عند نسخ `Guard`، انسخ البيانات المخزّنة بالقيمة (`value members`). ارجع الكائن المستقل داخل [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr)، وهو مؤشر بملكية حصرية بيحرر الكائن تلقائيًا مع المالك.

## Real-World Analogy

زي نسخة من مستند متجهّز: تغيّر اسم النسخة من غير ما تلمس الأصل.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Participants

في المثال، `Enemy` بتحدد عقد النسخ حسب النوع الفعلي (`polymorphic cloning`)، و `Guard` بتنفّذه. المستدعي (`Client`) بيمتلك النسخة الجديدة ويغيّر اسمها.

الأدوار القياسية في المثال ده:

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — كائن بيوفّر العملية `clone` لإنشاء كائن تاني (`object`) من القيم المتجهّزة. هنا: `Guard`.
- [`deep copy`](../../GLOSSARY.md#deep-copy) — بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل. هنا: `Guard::clone`.
- [`value semantics`](../../GLOSSARY.md#value-semantics) — النسخ تتعامل كقيم مستقلة حسب عقد النوع. هنا: `name_, equipment_`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

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

## Example Output

```text
template: 2 items
gate guard: 2 items
```

## When to Use

استخدمه لما الـ `objects` الموجودة شايلة إعداد مهم، والـ `Client` مش المفروض يعيد بناء نوعها الفعلي.

### Use cases

مناسب لقوالب كيانات الألعاب والمستندات؛ المثال بينسخ `string` و `std::vector` بالقيمة.

## When NOT to Use

بلاش لو النسخ العادي بالقيمة واضح وكافي.

## Advantages

بتعيد استخدام التجهيز من غير ما تكشف كل خطوات الإنشاء للـ `Client`.

## Trade-offs

لو فيه `pointers` لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. الـ `Socket` مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.

## Related Patterns

[Abstract Factory](../abstract-factory/README.ar-EG.md) · [Memento](../../behavioral/memento/README.ar-EG.md)

## Common Confusion

في `Memento`، بنرجّع نفس الكائن لحالة قديمة (`state`). أما `Prototype`، فبينشئ كائن تاني مستقل (`object`). دالة النسخ `copy constructor` لوحدها مش بتختار التنفيذ حسب النوع الفعلي؛ الميزة دي اسمها `polymorphic cloning`.

## Terms to Remember

- `Prototype` — انسخ نموذج متجهّز عشان تنشئ كائن مستقل (`object`) وتعدّله من غير ما تغيّر الأصل.
- `Concrete Prototype` — كائن بيوفّر العملية `clone` لإنشاء كائن تاني (`object`) من القيم المتجهّزة. مثال: `Guard`.
- `deep copy` — بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل. مثال: `Guard::clone`.
- `value semantics` — النسخ تتعامل كقيم مستقلة حسب عقد النوع. مثال: `name_, equipment_`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — نفس العقد (`interface`) يقبل تنفيذات مختلفة (`implementations`). في `C++`، فيه أشكال بتتحدد وقت التشغيل (`runtime`)، وأشكال وقت الترجمة (`compile time`).
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.

## Interview Question

لو المعدات بقت `std::vector<std::shared_ptr<Item>>`، هل النسخة هتفضل مستقلة؟ وضّح المشاركة.

## Mini Challenge

خلّي المعدات قابلة للتعديل، واتأكد إن تعديل النسخة مايمسش الأصل.

## اختبر فهمك

1. هل إسناد الأصل لمتغير تاني بيعمل نسخة مستقلة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** اللعبة محتاجة تنسخ أعداء من نموذج جاهز، لكن كود إنشاء الأعداء (`spawn`) مش عارف النوع الفعلي. النموذج هنا مش `template` بالمعنى الخاص بلغة `C++`.
- **الحل:** وفّر العملية `clone` في العقد `Enemy`. عند نسخ `Guard`، انسخ البيانات المخزّنة بالقيمة (`value members`). ارجع الكائن المستقل داخل `std::unique_ptr`، وهو مؤشر بملكية حصرية بيحرر الكائن تلقائيًا مع المالك.
- **`Trade-off`:** لو فيه `pointers` لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. الـ `Socket` مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.
- **افتكر:** انسخ التجهيز، مش الهوية.

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)
