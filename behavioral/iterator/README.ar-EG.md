# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

مبتدئ

## In One Sentence

لف على مجموعة من خلال طريقة وصول ثابتة.

## ببساطة

المستدعي محتاج الأغاني واحدة واحدة، مش تفاصيل التخزين.الـ`Iterator` بيتابع مكانه وبيخلّي الحلقة تطلب العنصر اللي بعده.

## The Problem

الـ `Client` محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.

## Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why It Becomes a Problem

كود الـ `Index` مربوط بـ `std::vector` عامة بيكشف التمثيل وبيوزع حساب الحدود.

## The Idea

وفّر بداية النطاق ونهايته عن طريق `begin` و`end`. أداة المرور (`Iterator`) تدعم قراءة العنصر الحالي، والانتقال للي بعده، والمقارنة.

## Real-World Analogy

زي مسار متحف تمشيه قطعة قطعة من غير ما تعرف قاعدة بيانات الغرف.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Participants

في المثال، `Playlist` بتمتلك الأغاني. أداة المرور `Iterator` بتستعير التخزين، من نوع `std::vector`، وبتحتفظ بالموضع. حلقة `range-for` هي المستدعي (`Client`). بنستخدم `static_assert` للتأكد من استيفاء متطلبات `std::forward_iterator` في `C++20`.

الأدوار القياسية في المثال ده:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — المجموعة اللي بتوفر `iterators` للمرور عليها. هنا: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — تنفيذ (`implementation`) بيحفظ موضع المرور في مجموعة محددة (`Aggregate`). هنا: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — أداة مرور (`iterator`) بتتحرك لقدام، وبتدعم المرور المستقل أكتر من مرة (`multipass`). يعني نسخها المستقلة تقدر تمر على نفس النطاق. هنا: `std::forward_iterator`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
#include <cstddef>
#include <iostream>
#include <iterator>
#include <utility>
#include <vector>

class Playlist {
    std::vector<int> tracks_;
public:
    explicit Playlist(std::vector<int> tracks) : tracks_(std::move(tracks)) {}
    class Iterator {
        const std::vector<int>* tracks_ = nullptr;
        std::size_t index_ = 0;
    public:
        using value_type = int;
        using difference_type = std::ptrdiff_t;
        using iterator_concept = std::forward_iterator_tag;
        Iterator() = default;
        Iterator(const std::vector<int>& tracks, std::size_t index) : tracks_(&tracks), index_(index) {}
        const int& operator*() const { return (*tracks_)[index_]; }
        Iterator& operator++() { ++index_; return *this; }
        Iterator operator++(int) { auto old = *this; ++*this; return old; }
        bool operator==(const Iterator&) const = default;
    };
    Iterator begin() const { return Iterator{tracks_, 0}; }
    Iterator end() const { return Iterator{tracks_, tracks_.size()}; }
};
static_assert(std::forward_iterator<Playlist::Iterator>);
int main() {
    const Playlist playlist{{7, 12, 18}};
    for (int track : playlist) std::cout << "Track " << track << '\n';
    const Playlist empty{{}};
    std::cout << "Empty: " << std::boolalpha << (empty.begin() == empty.end()) << '\n';
    auto first = playlist.begin();
    const auto copy = first;
    ++first;
    std::cout << "Independent positions: " << *first << ' ' << *copy << '\n';
}
```

## Example Output

```text
Track 7
Track 12
Track 18
Empty: true
Independent positions: 12 7
```

## When to Use

استخدم `Iterators` أو `Ranges` قياسية عشان تعرض المرور من غير كشف التخزين.

### Use cases

مناسب للمرور على الـ `containers` والشجر؛ اختار الفئة حسب العمليات والتكلفة الفعلية.

## When NOT to Use

بلاش `Iterator` مخصصة لو `const iterators` موجودة أو `Range` كفاية؛ الـ [`implementation`](../../GLOSSARY.md#implementation) هنا للتعليم.

## Advantages

الـ `algorithms` بتستخدم بروتوكول موحد، وكل `Iterator` ليها موضع مستقل.

## Trade-offs

الـ`Iterator` بيستعير البيانات ومش بيطوّل الـ`Lifetime` بتاعة المجموعة. لازم الـ`Playlist` تفضل موجودة وما تتنقلش أثناء استخدامه. القيمة `end` بتحدد نهاية النطاق، ومينفعش تقراها كأنها عنصر.

## Related Patterns

[Composite](../../structural/composite/README.ar-EG.md) · [Visitor](../visitor/README.ar-EG.md)

## Common Confusion

الـ `Visitor` بتختار العملية حسب نوع العنصر. الـ `Iterator` بتدير المرور من غير ما تعرف هتعمل إيه بالعنصر.

## Terms to Remember

- `Iterator` — لف على مجموعة من خلال طريقة وصول ثابتة.
- `Aggregate` — المجموعة اللي بتوفر `iterators` للمرور عليها. مثال: `Playlist`.
- `Concrete Iterator` — تنفيذ (`implementation`) بيحفظ موضع المرور في مجموعة محددة (`Aggregate`). مثال: `Playlist::Iterator`.
- `forward iterator` — أداة مرور (`iterator`) بتتحرك لقدام، وبتدعم المرور المستقل أكتر من مرة (`multipass`). يعني نسخها المستقلة تقدر تمر على نفس النطاق. مثال: `std::forward_iterator`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.
- [`iterator invalidation`](../../GLOSSARY.md#iterator-invalidation) — عملية بتخلي `iterator` ما بقتش صالحة للاستخدام المقصود.
- [`generic programming`](../../GLOSSARY.md#generic-programming) — بتكتب `algorithms` على أساس متطلبات النوع بدل ما تربطها بنوع واحد.

## Interview Question

ليه المقارنة بتراجع `pointer` الـ `std::vector` كمان، مش الـ `Index` بس؟

## Mini Challenge

اختبر قائمة فاضية و `Iterator` اتنين مستقلين؛ تحريك واحدة ما يحركش التانية.

## اختبر فهمك

1. هل نقدر نمشي في نفس الـ`Playlist` مرتين وكل مرة ليها مكان مستقل؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** الـ `Client` محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.
- **الحل:** وفّر بداية النطاق ونهايته عن طريق `begin` و`end`. أداة المرور (`Iterator`) تدعم قراءة العنصر الحالي، والانتقال للي بعده، والمقارنة.
- **`Trade-off`:** الـ`Iterator` بيستعير البيانات ومش بيطوّل الـ`Lifetime` بتاعة المجموعة. لازم الـ`Playlist` تفضل موجودة وما تتنقلش أثناء استخدامه. القيمة `end` بتحدد نهاية النطاق، ومينفعش تقراها كأنها عنصر.
- **افتكر:** امشي على البيانات من غير ما تفتح الـ `container`.

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)
