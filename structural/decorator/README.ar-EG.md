# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/composite/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/facade/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

مبتدئ

## In One Sentence

ضيف behavior بإنك تلف object بواحدة تانية عندها نفس الـ [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها).

## The Problem

طلب القهوة ممكن يحتاج لبن مرة أو مرتين من غير class لكل تركيبة.

## Naive Solution

```cpp
struct CoffeeWithMilk {};
struct CoffeeWithDoubleMilk {}; // another combination
```

## Why It Becomes a Problem

classes التركيبات بتكرر السعر الأساسي، وعددها بيزيد مع كل إضافة.

## The Idea

Milk بتمتلك Drink وبتفوّض ليها قبل ما تضيف وصفها وسعرها.

## Real-World Analogy

كل طبقة تغليف بتحيط بالهدية اللي قبلها، ولسه الناتج هدية متغلفة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

## Participants

Drink العقد المشترك، Coffee الأساس، و Milk بتلف Drink واحدة. الـ Client بيمتلك الطبقة الخارجية.

الأدوار القياسية في المثال ده:

- [`Component`](../../GLOSSARY.md#component) — العقد المشترك اللي العنصر أو المجموعة أو Wrapper بتوفره. هنا: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — الـ implementation الأساسية قبل إضافة طبقات اختيارية. هنا: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — Wrapper بتحافظ على عقد Component وبتضيف responsibility محددة. هنا: `Milk`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price() const override { return inner_->price() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price() << '\n';
}
```

## Example Output

```text
coffee + milk + milk: 14
```

## When to Use

استخدمه ل behavior اختياري قابل للتركيب وبيحافظ على عقد العنصر الأصلي.

### Use cases

ينفع لطبقات ضغط وتشفير الـ Streams ، مع الانتباه للترتيب والأخطاء.

## When NOT to Use

بلاش لو قائمة مكونات وجمع أسعار كفاية؛ المثال متعمد عشان يوضح التركيب.

## Advantages

الإضافات بتتركب وقت [`runtime`](../../GLOSSARY.md#runtime) (الوقت اللي البرنامج فيه شغال بعد البناء) ، والـ base [`implementation`](../../GLOSSARY.md#implementation) (الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد interface) بيفضل صغير.

## Trade-offs

ترتيب الطبقات ممكن يغيّر الـ behavior ، وكتر الـ objects الصغيرة بيصعّب التتبع. نفس الـ interface مش ضمان لنفس الوعود المرتبطة بالـ behavior.

## Related Patterns

[Proxy](../proxy/README.ar-EG.md) · [Composite](../composite/README.ar-EG.md)

## Common Confusion

Proxy بتتحكم في الوصول، وDecorator بتضيف responsibilities ؛ شكل الـ Wrapper لوحده مش كفاية تعرف المقصود.

## Terms to Remember

- `Decorator` — ضيف behavior بإنك تلف object بواحدة تانية عندها نفس الـ interface.
- `Component` — العقد المشترك اللي العنصر أو المجموعة أو Wrapper بتوفره. مثال: `Drink`.
- `Concrete Component` — الـ implementation الأساسية قبل إضافة طبقات اختيارية. مثال: `Coffee`.
- `Concrete Decorator` — Wrapper بتحافظ على عقد Component وبتضيف responsibility محددة. مثال: `Milk`.

## Interview Vocabulary

- [`composition over inheritance`](../../GLOSSARY.md#composition-over-inheritance) — فضّل objects متعاونة لما تعبر عن التغيير أوضح من تكبير شجرة inheritance.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — بتبني تركيب من أجزاء بتوفر نفس عقد الكل.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — خلّي الجزء مركز على سبب واحد مترابط للتغيير.

## Interview Question

هل Logging قبل التشفير هيشوف نفس البيانات بعد التشفير؟

## Mini Challenge

ضيف Syrup بسعر 3 وجرّب ترتيبين، واشرح اختلاف الوصف.

## Quick Summary

- **المشكلة:** طلب القهوة ممكن يحتاج لبن مرة أو مرتين من غير class لكل تركيبة.
- **الحل:** Milk بتمتلك Drink وبتفوّض ليها قبل ما تضيف وصفها وسعرها.
- **Trade-off:** ترتيب الطبقات ممكن يغيّر الـ behavior ، وكتر الـ objects الصغيرة بيصعّب التتبع. نفس الـ interface مش ضمان لنفس الوعود المرتبطة بالـ behavior.
- **افتكر:** نفس العقد، وطبقة زيادة.

[السابق](../../structural/composite/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/facade/README.ar-EG.md)
