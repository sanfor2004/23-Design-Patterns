# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/flyweight/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/chain-of-responsibility/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — Design Pattern بيركز على تركيب objects وclasses وعلاقتهم ببعض.

## Difficulty

متوسط

## In One Sentence

تحكّم في الوصول لـ object عن طريق بديل بنفس الـ [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها).

## The Problem

معرض الصور ممكن يجهّز صور كتير بس يعرض كام واحدة.

## Naive Solution

```cpp
DiskImage image; // loads even if never displayed
```

## Why It Becomes a Problem

إنشاء الصور التقيلة فوراً بيحمّل حاجات قبل ما حد يطلب عرضها.

## The Idea

LazyImage بتنفذ Image ، وبتعمل DiskImage عند أول display وبعد كده تعيد استخدامها.

## Real-World Analogy

إيصال طلب كتاب بيمثل الكتاب المخزّن لحد ما أمين المكتبة يجيبه.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Proxy](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## Participants

Image الـ interface المشتركة، DiskImage الشغل الفعلي، و LazyImage بتمتلك الصورة اللي بتتعمل عند الطلب.

الأدوار القياسية في المثال ده:

- [`Subject interface`](../../GLOSSARY.md#subject-interface) — العقد المشترك اللي Proxy وReal Subject بيوفروه. هنا: `Image`.
- [`Real Subject`](../../GLOSSARY.md#real-subject) — الـ object اللي بتنفذ الشغل الحقيقي ورا Proxy. هنا: `DiskImage`.
- [`lazy initialization`](../../GLOSSARY.md#lazy-initialization) — بتأجل الإنشاء لأول مرة تحتاج فيها القيمة أو المورد. هنا: `LazyImage::display`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() const = 0;
};
struct DiskImage final : Image {
    DiskImage() { std::cout << "Load image\n"; }
    void display() const override { std::cout << "Display image\n"; }
};
class LazyImage final : public Image {
    mutable std::unique_ptr<DiskImage> image_;
public:
    void display() const override {
        if (!image_) image_ = std::make_unique<DiskImage>();
        image_->display();
    }
};
int main() {
    const LazyImage image;
    std::cout << "Proxy ready\n";
    image.display();
    image.display();
}
```

## Example Output

```text
Proxy ready
Load image
Display image
Display image
```

## When to Use

استخدمه للتحميل عند الطلب أو فحص الوصول أو الوصول البعيد مع interface ثابتة.

### Use cases

ينفع للوسائط عند الطلب وبوابات الصلاحيات و Remote Stubs ، وكل واحدة ليها طريقة فشل مختلفة.

## When NOT to Use

بلاش لو الإنشاء رخيص وسياسة الوصول مش بتضيف قيمة.

## Advantages

الـ Client بيستخدم نفس display والإنشاء بيتأجل.

## Trade-offs

أول استدعاء هيدفع تكلفة التحميل. mutable هنا للـ logical constness مش أمان التزامن؛ وفشل التحميل محتاج سياسة.

## Related Patterns

[Decorator](../decorator/README.ar-EG.md) · [Adapter](../adapter/README.ar-EG.md)

## Common Confusion

Decorator بتضيف behavior ، Proxy بتتحكم إمتى وهل نوصل للأصل؛ الرسم ممكن يبقى شبه بعض.

## Terms to Remember

- `Proxy` — تحكّم في الوصول لـ object عن طريق بديل بنفس الـ interface.
- `Subject interface` — العقد المشترك اللي Proxy وReal Subject بيوفروه. مثال: `Image`.
- `Real Subject` — الـ object اللي بتنفذ الشغل الحقيقي ورا Proxy. مثال: `DiskImage`.
- `lazy initialization` — بتأجل الإنشاء لأول مرة تحتاج فيها القيمة أو المورد. مثال: `LazyImage::display`.

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — object بتطلب من object متعاونة معاها تنفذ جزء من الشغل.
- [`runtime behavior`](../../GLOSSARY.md#runtime-behavior) — اللي البرنامج بيعمله وهو شغال، بما فيه behavior بتتحدد من المدخلات.
- [`trade-off`](../../GLOSSARY.md#trade-off) — ميزة بتكسبها قصاد تكلفة أو تنازل في ناحية تانية.

## Interview Question

لو التحميل رمى Exception ، تعيد المحاولة المرة الجاية ولا تفتكر الفشل؟

## Mini Challenge

عدّ مرات التحميل مع ثلاث مرات عرض، وجرّب Loader بتفشل مرة عشان تختبر سياسة المحاولة.

## Quick Summary

- **المشكلة:** معرض الصور ممكن يجهّز صور كتير بس يعرض كام واحدة.
- **الحل:** LazyImage بتنفذ Image ، وبتعمل DiskImage عند أول display وبعد كده تعيد استخدامها.
- **Trade-off:** أول استدعاء هيدفع تكلفة التحميل. mutable هنا للـ logical constness مش أمان التزامن؛ وفشل التحميل محتاج سياسة.
- **افتكر:** بديل بينك وبين الأصل.

[السابق](../../structural/flyweight/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/chain-of-responsibility/README.ar-EG.md)
