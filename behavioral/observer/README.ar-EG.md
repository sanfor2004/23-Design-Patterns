# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

مبتدئ

## In One Sentence

بلّغ المشتركين (`Observers`) لما يحصل تغيير في المصدر اللي بيتابعوه (`Subject`).

## ببساطة

كذا شاشة ممكن تحتاج آخر كمية في المخزون.الـ`Observer` بيسمح بالاشتراك، فـ`Stock` يبعت التحديث من غير ما يكتب استدعاء مخصوص لكل شاشة.

## The Problem

تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما `Stock` تعرف كل نوع شاشة.

## Naive Solution

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## Why It Becomes a Problem

استدعاء كل مستهلك باسمه بيربط الناشر بالقائمة الحالية، وإضافة مستهلك تحتاج تعديل الناشر.

## The Idea

خلّي المصدر `Stock` يحتفظ بمراجع مش مالكة (`weak references`) للمشتركين من نوع `Listener`. عند التغيير، ابعت التحديث للمشتركين اللي لسه موجودين.

## Real-World Analogy

المشتركين يوصلهم تنبيه توفر المنتج طول ما الاشتراك شغال.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Observer](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## Participants

في المثال، المصدر هو `Stock`، وعقد استقبال الإشعارات هو `Listener`، والشاشة المشتركة هي `Display`. المستدعي (`Client`) بيمتلك المشتركين. المصدر بيستخدم [`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr)، وهي مراجع مش مالكة، عشان ما يطوّلش عمر المشتركين.

الأدوار القياسية في المثال ده:

- [`Subject`](../../GLOSSARY.md#subject) — المصدر اللي بيعلن تغييراته للـ `Observers` المسجلين. هنا: `Stock`.
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — عقد `callback` اللي المشتركين بينفذوه. هنا: `Listener`.
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — تنفيذ للمشترك (`Observer implementation`) بيحدد استجابته للإشعارات (`notifications`). هنا: `Display`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

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
    auto screen = std::make_shared<Display>();
    auto log = std::make_shared<Display>();
    stock.subscribe(screen);
    stock.subscribe(log);
    stock.set(2);
}
```

## Example Output

```text
Stock: 4
Expired listener skipped
Stock: 2
Stock: 2
```

## When to Use

استخدمه لما تغيير واحد ليه كذا مستهلك بيسجلوا نفسهم باستقلال.

### Use cases

مناسب لتحديث `UI` والـ `events` المحلية؛ ضمانات الـ `events` الموزعة موضوع تاني.

## When NOT to Use

بلاش لـ `dependency` ثابتة واحدة أو لما محتاج اتساق `Transaction` قوي.

## Advantages

المشتركين يدخلوا ويخرجوا من غير تعديل كود الناشر.

## Trade-offs

لازم تحدد ترتيب الـ`callbacks` وإيه اللي يحصل لو واحدة رمت `exception`. الإشعارات هنا متزامنة (`synchronous`) ومفيش حماية للـ`threads`. بننسخ قائمة الاشتراكات قبل الإرسال، فإضافة مشترك جديد مش بتغيّر الجولة الحالية. النسخة دي مش بتمنع `callback` من إطلاق إشعار جديد أثناء تنفيذها.

## Related Patterns

[Mediator](../mediator/README.ar-EG.md) · [State](../state/README.ar-EG.md)

## Common Confusion

الـ `Mediator` بتحدد قواعد تنسيق زملاء معروفين. الـ `Observer` بتذيع إشعار من غير فرض علاقة بينهم.

## Terms to Remember

- `Observer` — بلّغ المشتركين (`Observers`) لما يحصل تغيير في المصدر اللي بيتابعوه (`Subject`).
- `Subject` — المصدر اللي بيعلن تغييراته للـ `Observers` المسجلين. مثال: `Stock`.
- `Observer interface` — عقد `callback` اللي المشتركين بينفذوه. مثال: `Listener`.
- `Concrete Observer` — تنفيذ للمشترك (`Observer implementation`) بيحدد استجابته للإشعارات (`notifications`). مثال: `Display`.

## Interview Vocabulary

- [`one-to-many dependency`](../../GLOSSARY.md#one-to-many-dependency) — مصدر واحد ليه أكتر من طرف بيتأثروا بتغييره.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`subscription lifetime`](../../GLOSSARY.md#subscription-lifetime) — الفترة اللي المستمع فيها مسجل وينفع توصله `notification`.

## Interview Question

ليه نخزن `std::weak_ptr` ونحوّلها لـ [`std::shared_ptr`](../../GLOSSARY.md#stdshared_ptr) وقت الـ `callback`؟

## Mini Challenge

ضيف مشتركين، امسح واحد، واتأكد إن الباقي بس يستقبل. عرّف عملية إلغاء اشتراك صريحة.

## اختبر فهمك

1. إيه الفرق بين `unsubscribe` في Python وانتهاء `weak_ptr` في C++؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما `Stock` تعرف كل نوع شاشة.
- **الحل:** خلّي المصدر `Stock` يحتفظ بمراجع مش مالكة (`weak references`) للمشتركين من نوع `Listener`. عند التغيير، ابعت التحديث للمشتركين اللي لسه موجودين.
- **`Trade-off`:** لازم تحدد ترتيب الـ`callbacks` وإيه اللي يحصل لو واحدة رمت `exception`. الإشعارات هنا متزامنة (`synchronous`) ومفيش حماية للـ`threads`. بننسخ قائمة الاشتراكات قبل الإرسال، فإضافة مشترك جديد مش بتغيّر الجولة الحالية. النسخة دي مش بتمنع `callback` من إطلاق إشعار جديد أثناء تنفيذها.
- **افتكر:** انشر التغيير، وسيب المشترك يرد.

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)
