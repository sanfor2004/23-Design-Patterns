# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

مبتدئ

## In One Sentence

لف على مجموعة من خلال طريقة وصول ثابتة.

## The Problem

الـ Client محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.

## Naive Solution

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## Why It Becomes a Problem

كود الـ Index مربوط بـ std::vector عامة بيكشف التمثيل وبيوزع حساب الحدود.

## The Idea

وفّر begin و end وIterator بتدعم القراءة والزيادة والمقارنة.

## Real-World Analogy

زي مسار متحف تمشيه قطعة قطعة من غير ما تعرف قاعدة بيانات الغرف.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## Participants

Playlist بتمتلك الأغاني؛ Iterator بتستعير الـ std::vector وبتحفظ الموضع. Range-for هي الـ Client ، و static_assert بتراجع forward_iterator في C++20.

الأدوار القياسية في المثال ده:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — المجموعة اللي بتوفر iterators للمرور عليها. هنا: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — implementation بتحفظ مكان المرور في Aggregate معينة. هنا: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — iterator بتتحرك لقدام وتدعم multipass؛ نسخ مستقلة منها تقدر تمر على نفس النطاق. هنا: `std::forward_iterator`.

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
}
```

## Example Output

```text
Track 7
Track 12
Track 18
```

## When to Use

استخدم Iterators أو Ranges قياسية عشان تعرض المرور من غير كشف التخزين.

### Use cases

مناسب للمرور على الـ containers والشجر؛ اختار الفئة حسب العمليات والتكلفة الفعلية.

## When NOT to Use

بلاش Iterator مخصصة لو const iterators موجودة أو Range كفاية؛ الـ [`implementation`](../../GLOSSARY.md#implementation) (الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد interface) هنا للتعليم.

## Advantages

الـ algorithms بتستخدم بروتوكول موحد، وكل Iterator ليها موضع مستقل.

## Trade-offs

الـ Iterator مش بتطوّل عمر المجموعة. نقل أو تدمير Playlist يبطل الافتراضات، وقراءة end غير صالحة زي القياسي.

## Related Patterns

[Composite](../../structural/composite/README.ar-EG.md) · [Visitor](../visitor/README.ar-EG.md)

## Common Confusion

Visitor بتختار العملية حسب نوع العنصر. Iterator بتدير المرور من غير ما تعرف هتعمل إيه بالعنصر.

## Terms to Remember

- `Iterator` — لف على مجموعة من خلال طريقة وصول ثابتة.
- `Aggregate` — المجموعة اللي بتوفر iterators للمرور عليها. مثال: `Playlist`.
- `Concrete Iterator` — implementation بتحفظ مكان المرور في Aggregate معينة. مثال: `Playlist::Iterator`.
- `forward iterator` — iterator بتتحرك لقدام وتدعم multipass؛ نسخ مستقلة منها تقدر تمر على نفس النطاق. مثال: `std::forward_iterator`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.
- [`iterator invalidation`](../../GLOSSARY.md#iterator-invalidation) — عملية بتخلي iterator ما بقتش صالحة للاستخدام المقصود.
- [`generic programming`](../../GLOSSARY.md#generic-programming) — بتكتب algorithms على أساس متطلبات النوع بدل ما تربطها بنوع واحد.

## Interview Question

ليه المقارنة بتراجع pointer الـ std::vector كمان، مش الـ Index بس؟

## Mini Challenge

اختبر قائمة فاضية وIterator اتنين مستقلين؛ تحريك واحدة ما يحركش التانية.

## Quick Summary

- **المشكلة:** الـ Client محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.
- **الحل:** وفّر begin و end وIterator بتدعم القراءة والزيادة والمقارنة.
- **Trade-off:** الـ Iterator مش بتطوّل عمر المجموعة. نقل أو تدمير Playlist يبطل الافتراضات، وقراءة end غير صالحة زي القياسي.
- **افتكر:** امشي على البيانات من غير ما تفتح الـ container.

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)
