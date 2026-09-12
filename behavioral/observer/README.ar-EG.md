# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

مبتدئ

## In One Sentence

بلّغ الـ objects المشتركة لما الحاجة اللي بيتابعوها تتغير.

## The Problem

تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما Stock تعرف كل نوع شاشة.

## Naive Solution

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## Why It Becomes a Problem

استدعاء كل مستهلك باسمه بيربط الناشر بالقائمة الحالية، وإضافة مستهلك تحتاج تعديل الناشر.

## The Idea

Stock بتخزن weak references لـ Listener وبتبعت التحديث للنسخ اللي لسه عايشة.

## Real-World Analogy

المشتركين يوصلهم تنبيه توفر المنتج طول ما الاشتراك شغال.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Observer](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## Participants

Stock المصدر، Listener [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها) الاستقبال، و Display مشتركة. الـ Client بيمتلك المشتركين، و [`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr) (مرجع مش مالك لملكية مشتركة؛ lock بتحاول تجيب shared_ptr مؤقتة) مش بتطوّل عمرهم.

الأدوار القياسية في المثال ده:

- [`Subject`](../../GLOSSARY.md#subject) — المصدر اللي بيعلن تغييراته للـ Observers المسجلين. هنا: `Stock`.
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — عقد callback اللي المشتركين بينفذوه. هنا: `Listener`.
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — implementation لـ Observer بترد على notifications. هنا: `Display`.

## Modern C++20 Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
}
```

## Example Output

```text
Stock: 4
Expired listener skipped
```

## When to Use

استخدمه لما تغيير واحد ليه كذا مستهلك بيسجلوا نفسهم باستقلال.

### Use cases

مناسب لتحديث UI والـ events المحلية؛ ضمانات الـ events الموزعة موضوع تاني.

## When NOT to Use

بلاش لـ dependency ثابتة واحدة أو لما محتاج اتساق Transaction قوي.

## Advantages

المشتركين يدخلوا ويخرجوا من غير تعديل كود الناشر.

## Trade-offs

ترتيب الـ callbacks والـ Exceptions محتاج سياسة. المثال Sync بيمرر الاستثناء ومش Thread-safe. نسخة القائمة بتسمح بتغيير الاشتراكات بس مش بتمنع إشعارات Recursive.

## Related Patterns

[Mediator](../mediator/README.ar-EG.md) · [State](../state/README.ar-EG.md)

## Common Confusion

Mediator بتحدد قواعد تنسيق زملاء معروفين. Observer بتذيع إشعار من غير فرض علاقة بينهم.

## Terms to Remember

- `Observer` — بلّغ الـ objects المشتركة لما الحاجة اللي بيتابعوها تتغير.
- `Subject` — المصدر اللي بيعلن تغييراته للـ Observers المسجلين. مثال: `Stock`.
- `Observer interface` — عقد callback اللي المشتركين بينفذوه. مثال: `Listener`.
- `Concrete Observer` — implementation لـ Observer بترد على notifications. مثال: `Display`.

## Interview Vocabulary

- [`one-to-many dependency`](../../GLOSSARY.md#one-to-many-dependency) — مصدر واحد ليه أكتر من طرف بيتأثروا بتغييره.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`subscription lifetime`](../../GLOSSARY.md#subscription-lifetime) — الفترة اللي المستمع فيها مسجل وينفع توصله notification.

## Interview Question

ليه نخزن std::weak_ptr ونحوّلها لـ [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) (smart pointer بتشارك ownership؛ الـ object بتتحرر لما آخر مرجع مالك يختفي) وقت الـ callback ؟

## Mini Challenge

ضيف مشتركين، امسح واحد، واتأكد إن الباقي بس يستقبل. عرّف عملية إلغاء اشتراك صريحة.

## Quick Summary

- **المشكلة:** تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما Stock تعرف كل نوع شاشة.
- **الحل:** Stock بتخزن weak references لـ Listener وبتبعت التحديث للنسخ اللي لسه عايشة.
- **Trade-off:** ترتيب الـ callbacks والـ Exceptions محتاج سياسة. المثال Sync بيمرر الاستثناء ومش Thread-safe. نسخة القائمة بتسمح بتغيير الاشتراكات بس مش بتمنع إشعارات Recursive.
- **افتكر:** انشر التغيير، وسيب المشترك يرد.

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)
