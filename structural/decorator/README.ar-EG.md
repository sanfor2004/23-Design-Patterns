# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/composite/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/facade/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — بيركز على تركيب الـ`Objects` والـ`Classes` عشان تتعاون.

## Difficulty

مبتدئ

## In One Sentence

ضيف سلوك جديد (`behavior`) عن طريق كائن بيغلّف الكائن الأصلي. حافظ على نفس [`interface`](../../GLOSSARY.md#interface)، يعني نفس العمليات المتاحة للمستدعي.

## ببساطة

المشروب ممكن يكون عليه إضافات اختيارية.كل `Decorator` بيوفر نفس الـ`Interface` وبيضيف شغله قبل أو بعد استدعاء اللي جواه.

## The Problem

طلب القهوة ممكن يحتاج لبن مرة أو مرتين من غير `class` لكل تركيبة.

## Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why It Becomes a Problem

الـ `classes` التركيبات بتكرر السعر الأساسي، وعددها بيزيد مع كل إضافة.

## The Idea

خلّي طبقة الإضافة `Milk` تمتلك مشروب من نوع `Drink`. الأول بتطلب منه الوصف والسعر، وبعدها بتضيف وصفها وتكلفتها على النتيجة.

## Real-World Analogy

كل طبقة تغليف بتحيط بالهدية اللي قبلها، ولسه الناتج هدية متغلفة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Participants

في المثال، العقد المشترك هو `Drink`، والتنفيذ الأساسي هو `Coffee`. طبقة الإضافة `Milk` بتغلّف مشروب واحد. المستدعي (`Client`) بيمتلك الطبقة الخارجية.

الأدوار القياسية في المثال ده:

- [`Component`](../../GLOSSARY.md#component) — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. هنا: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — الـ `implementation` الأساسية قبل إضافة طبقات اختيارية. هنا: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — طبقة تغليف (`Wrapper`) بتحافظ على عقد `Component`، وبتضيف مسؤولية محددة (`responsibility`). هنا: `Milk`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price_cents() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price_cents() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price_cents() const override { return inner_->price_cents() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price_cents() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use

استخدمه لإضافة سلوك اختياري (`behavior`) قابل للتركيب وبيحافظ على عقد العنصر الأصلي.

### Use cases

ينفع لطبقات ضغط وتشفير الـ `Streams`، مع الانتباه للترتيب والأخطاء.

## When NOT to Use

بلاش لو قائمة مكونات وجمع أسعار كفاية؛ المثال متعمد عشان يوضح التركيب.

## Advantages

الإضافات بتتركب وقت [`runtime`](../../GLOSSARY.md#runtime)، والتنفيذ الأساسي ([`implementation`](../../GLOSSARY.md#implementation)) بيفضل صغير، يعني الكود المسؤول عن السلوك الأصلي بس.

## Trade-offs

ترتيب الطبقات ممكن يغيّر الـ `behavior`، وكتر الـ `objects` الصغيرة بيصعّب التتبع. نفس الـ `interface` مش ضمان لنفس الوعود المرتبطة بالـ `behavior`.

## Related Patterns

[Proxy](../proxy/README.ar-EG.md) · [Composite](../composite/README.ar-EG.md)

## Common Confusion

الـ `Proxy` بتتحكم في الوصول، و `Decorator` بتضيف `responsibilities`؛ شكل طبقة التغليف (`Wrapper`) لوحده مش كفاية تعرف المقصود.

## Terms to Remember

- `Decorator` — ضيف سلوك جديد (`behavior`) عن طريق كائن بيغلّف الكائن الأصلي، مع الحفاظ على نفس العقد (`interface`).
- `Component` — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. مثال: `Drink`.
- `Concrete Component` — الـ `implementation` الأساسية قبل إضافة طبقات اختيارية. مثال: `Coffee`.
- `Concrete Decorator` — طبقة تغليف (`Wrapper`) بتحافظ على عقد `Component`، وبتضيف مسؤولية محددة (`responsibility`). مثال: `Milk`.

## Interview Vocabulary

- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — فضّل تركيب الحل من كائنات متعاونة (`objects`)، لما ده يكون أوضح من توسيع شجرة الوراثة (`inheritance`).
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — بتبني تركيب من أجزاء بتوفر نفس عقد الكل.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — خلّي الجزء مركز على سبب واحد مترابط للتغيير.

## Interview Question

هل `Logging` قبل التشفير هيشوف نفس البيانات بعد التشفير؟

## Mini Challenge

ضيف `Syrup` بسعر 3 وجرّب ترتيبين، واشرح اختلاف الوصف.

## اختبر فهمك

1. ليه `Milk` تقدر تغلّف `Milk` تانية من غير معرفة النوع الفعلي؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** طلب القهوة ممكن يحتاج لبن مرة أو مرتين من غير `class` لكل تركيبة.
- **الحل:** خلّي طبقة الإضافة `Milk` تمتلك مشروب من نوع `Drink`. الأول بتطلب منه الوصف والسعر، وبعدها بتضيف وصفها وتكلفتها على النتيجة.
- **`Trade-off`:** ترتيب الطبقات ممكن يغيّر الـ `behavior`، وكتر الـ `objects` الصغيرة بيصعّب التتبع. نفس الـ `interface` مش ضمان لنفس الوعود المرتبطة بالـ `behavior`.
- **افتكر:** نفس العقد، وطبقة زيادة.

[السابق](../../structural/composite/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/facade/README.ar-EG.md)
