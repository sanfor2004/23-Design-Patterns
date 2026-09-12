# Prototype

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Design Pattern بيركز على إزاي نعمل objects ونجهّزها.

## Difficulty

متوسط

## In One Sentence

اعمل object مستقلة عن طريق نسخ نموذج متجهّز.

## The Problem

اللعبة محتاجة أعداء من template جاهزة، وكود الـ Spawn مش عارف النوع الفعلي.

## Naive Solution

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## Why It Becomes a Problem

إنشاء Guard افتراضية كل مرة بيكرر التجهيز وبيضيّع أي معدات مخصصة في النموذج.

## The Idea

وفّر clone في Enemy. Guard بتنسخ الـ Value Members وترجع [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) (smart pointer بملكية حصرية، بتحرر الـ object لما المالك يتدمر) لـ object مستقلة.

## Real-World Analogy

زي نسخة من مستند متجهّز: تغيّر اسم النسخة من غير ما تلمس الأصل.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Prototype](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## Participants

Enemy بتحدد polymorphic cloning ، و Guard بتنفذه؛ الـ Client بيمتلك النسخة ويغيّر اسمها.

الأدوار القياسية في المثال ده:

- [`Concrete Prototype`](../../GLOSSARY.md#concrete-prototype) — object فيها clone بتعمل object تانية من القيم المتجهّزة. هنا: `Guard`.
- [`deep copy`](../../GLOSSARY.md#deep-copy) — بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل. هنا: `Guard::clone`.
- [`value semantics`](../../GLOSSARY.md#value-semantics) — النسخ تتعامل كقيم مستقلة حسب عقد النوع. هنا: `name_, equipment_`.

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

استخدمه لما الـ objects الموجودة شايلة إعداد مهم، والـ Client مش المفروض يعيد بناء نوعها الفعلي.

### Use cases

مناسب لقوالب كيانات الألعاب والمستندات؛ المثال بينسخ string و std::vector بالقيمة.

## When NOT to Use

بلاش لو النسخ العادي بالقيمة واضح وكافي.

## Advantages

بتعيد استخدام التجهيز من غير ما تكشف كل خطوات الإنشاء للـ Client.

## Trade-offs

لو فيه pointers لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. Socket مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.

## Related Patterns

[Abstract Factory](../abstract-factory/README.ar-EG.md) · [Memento](../../behavioral/memento/README.ar-EG.md)

## Common Confusion

Memento بترجّع نفس الـ object ل state قديمة. Prototype بتعمل object تانية، والـ copy constructor لوحدها مش بتوفر polymorphic cloning.

## Terms to Remember

- `Prototype` — اعمل object مستقلة عن طريق نسخ نموذج متجهّز.
- `Concrete Prototype` — object فيها clone بتعمل object تانية من القيم المتجهّزة. مثال: `Guard`.
- `deep copy` — بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل. مثال: `Guard::clone`.
- `value semantics` — النسخ تتعامل كقيم مستقلة حسب عقد النوع. مثال: `name_, equipment_`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز القيم الأولية وبدء lifetime بتاعة object.
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — نفس interface تشتغل مع implementations مختلفة؛ C++ فيها أشكال وقت runtime وأشكال وقت compile time.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.

## Interview Question

لو المعدات بقت `std::vector<std::shared_ptr<Item>>`، هل النسخة هتفضل مستقلة؟ وضّح المشاركة.

## Mini Challenge

خلّي المعدات قابلة للتعديل، واتأكد إن تعديل النسخة مايمسش الأصل.

## Quick Summary

- **المشكلة:** اللعبة محتاجة أعداء من template جاهزة، وكود الـ Spawn مش عارف النوع الفعلي.
- **الحل:** وفّر clone في Enemy. Guard بتنسخ الـ Value Members وترجع std::unique_ptr لـ object مستقلة.
- **Trade-off:** لو فيه pointers لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. Socket مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.
- **افتكر:** انسخ التجهيز، مش الهوية.

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)
