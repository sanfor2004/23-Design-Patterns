# Flyweight

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/facade/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/proxy/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

متقدم

## In One Sentence

شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل.

## The Problem

المستند فيه حروف مكررة كتير؛ تخزين شكل الحرف كامل لكل مكان بيهدر الذاكرة.

## Naive Solution

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## Why It Becomes a Problem

نسخ نفس الشكل لكل ظهور بيخلّي الذاكرة تزيد بعدد المواضع بدل عدد الأشكال المختلفة.

## The Idea

خزّن Glyph حسب الحرف في Pool. PlacedGlyph بتشارك const Glyph وبتحتفظ بمكان x لوحدها.

## Real-World Analogy

كذا قارئ بيستخدموا نفس المرجع، وكل واحد عنده علامة صفحة بتاعته.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Flyweight](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## Participants

Glyph شايلة الشكل المشترك، GlyphPool بتوحّد نسخه، و PlacedGlyph شايلة الموضع و shared [`ownership`](../../GLOSSARY.md#ownership) (مين مسؤول يخلي المورد عايش ومين يحرره في الآخر).

الأدوار القياسية في المثال ده:

- [`intrinsic state`](../../GLOSSARY.md#intrinsic-state) — بيانات مستقلة عن مكان الاستخدام، فالـ Flyweight تقدر تشاركها. هنا: `Glyph::shape`.
- [`extrinsic state`](../../GLOSSARY.md#extrinsic-state) — بيانات تخص كل استخدام وبتفضل بره الـ Flyweight المشتركة. هنا: `PlacedGlyph::x`.
- [`Flyweight Factory`](../../GLOSSARY.md#flyweight-factory) — جزء بيبحث بالمفتاح ويرجع Flyweight مشتركة. هنا: `GlyphPool`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Glyph {
    const std::string shape;
    explicit Glyph(std::string value) : shape(std::move(value)) {}
};
class GlyphPool {
    std::map<char, std::shared_ptr<const Glyph>> glyphs_;
public:
    std::shared_ptr<const Glyph> get(char symbol) {
        auto& glyph = glyphs_[symbol];
        if (!glyph) glyph = std::make_shared<const Glyph>(std::string(1, symbol));
        return glyph;
    }
};
struct PlacedGlyph {
    std::shared_ptr<const Glyph> glyph;
    int x;
    void draw() const { std::cout << glyph->shape << " at " << x << '\n'; }
};
int main() {
    GlyphPool pool;
    const PlacedGlyph first{pool.get('A'), 0};
    const PlacedGlyph second{pool.get('A'), 10};
    first.draw();
    second.draw();
    std::cout << "Shared shape: " << std::boolalpha << (first.glyph == second.glyph) << '\n';
}
```

## Example Output

```text
A at 0
A at 10
Shared shape: true
```

## When to Use

استخدمه بعد قياس تكرار كبير لبيانات ثابتة بين objects كتير.

### Use cases

أشكال الحروف وتعريفات أرضية الألعاب والأسماء المتكررة مرشحين مناسبين لو القياس أكد ده.

## When NOT to Use

بلاش مع بيانات قليلة أو متغيرة لكل نسخة، أو لو البحث أغلى من التوفير.

## Advantages

المواضع بتستخدم نفس الشكل مع احتفاظ كل واحد بمكانه.

## Trade-offs

الـ Pool بتحتفظ بالعناصر، والـ map والـ [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) (smart pointer بتشارك ownership؛ الـ object بتتحرر لما آخر مرجع مالك يختفي) ليهم تكلفة. النص هنا صغير ومفيش ادعاء بقياس توفير ذاكرة؛ الوصول للـ Pool مش متزامن.

## Related Patterns

[Composite](../composite/README.ar-EG.md) · [Prototype](../../creational/prototype/README.ar-EG.md)

## Common Confusion

Prototype بتنسخ الإعداد لـ object جديدة. Flyweight بتشارك الـ intrinsic state عن قصد.

## Terms to Remember

- `Flyweight` — شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل.
- `intrinsic state` — بيانات مستقلة عن مكان الاستخدام، فالـ Flyweight تقدر تشاركها. مثال: `Glyph::shape`.
- `extrinsic state` — بيانات تخص كل استخدام وبتفضل بره الـ Flyweight المشتركة. مثال: `PlacedGlyph::x`.
- `Flyweight Factory` — جزء بيبحث بالمفتاح ويرجع Flyweight مشتركة. مثال: `GlyphPool`.

## Interview Vocabulary

- [`interning`](../../GLOSSARY.md#interning) — بتعيد استخدام تمثيل واحد للقيم المتساوية عن طريق pool للبحث.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.
- [`memory allocation`](../../GLOSSARY.md#memory-allocation) — حجز مساحة للبيانات؛ تكلفته وطريقة فشله حسب الآلية المستخدمة.

## Interview Question

لو الخط وحجمه بيغيّروا الشكل، إيه اللي لازم يدخل في مفتاح الـ Pool ؟

## Mini Challenge

ضيف معرف الخط للمفتاح، واتأكد إن المفاتيح المتساوية بتشارك والمختلفة لأ.

## Quick Summary

- **المشكلة:** المستند فيه حروف مكررة كتير؛ تخزين شكل الحرف كامل لكل مكان بيهدر الذاكرة.
- **الحل:** خزّن Glyph حسب الحرف في Pool. PlacedGlyph بتشارك const Glyph وبتحتفظ بمكان x لوحدها.
- **Trade-off:** الـ Pool بتحتفظ بالعناصر، والـ map والـ std::shared_ptr ليهم تكلفة. النص هنا صغير ومفيش ادعاء بقياس توفير ذاكرة؛ الوصول للـ Pool مش متزامن.
- **افتكر:** شارك الشكل، وافصل المكان.

[السابق](../../structural/facade/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/proxy/README.ar-EG.md)
