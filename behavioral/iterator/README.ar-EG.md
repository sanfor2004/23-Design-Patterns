# Iterator

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** لف على مجموعة من خلال طريقة وصول ثابتة.

## المشكلة

الـ `Client` محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص. كود الـ `Index` مربوط بـ `std::vector` عامة بيكشف التمثيل وبيوزع حساب الحدود.

## الحل ببساطة

المستدعي محتاج الأغاني واحدة واحدة، مش تفاصيل التخزين.الـ`Iterator` بيتابع مكانه وبيخلّي الحلقة تطلب العنصر اللي بعده. وفّر بداية النطاق ونهايته عن طريق `begin` و`end`. أداة المرور (`Iterator`) تدعم قراءة العنصر الحالي، والانتقال للي بعده، والمقارنة.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Iterator](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

في المثال، `Playlist` بتمتلك الأغاني. أداة المرور `Iterator` بتستعير التخزين، من نوع `std::vector`، وبتحتفظ بالموضع. حلقة `range-for` هي المستدعي (`Client`). بنستخدم `static_assert` للتأكد من استيفاء متطلبات `std::forward_iterator` في `C++20`.

الأدوار القياسية في المثال ده:

- [`Aggregate`](../../GLOSSARY.md#aggregate) — المجموعة اللي بتوفر `iterators` للمرور عليها. هنا: `Playlist`.
- [`Concrete Iterator`](../../GLOSSARY.md#concrete-iterator) — تنفيذ (`implementation`) بيحفظ موضع المرور في مجموعة محددة (`Aggregate`). هنا: `Playlist::Iterator`.
- [`forward iterator`](../../GLOSSARY.md#forward-iterator) — أداة مرور (`iterator`) بتتحرك لقدام، وبتدعم المرور المستقل أكتر من مرة (`multipass`). يعني نسخها المستقلة تقدر تمر على نفس النطاق. هنا: `std::forward_iterator`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Playlist:
    def __init__(self, tracks):
        self._tracks = list(tracks)

    def __iter__(self):
        return iter(self._tracks)


if __name__ == "__main__":
    playlist = Playlist([7, 12, 18])
    for track in playlist:
        print("Track", track)
    first = iter(playlist)
    second = iter(playlist)
    print("Independent:", next(first), next(second))
    print("Empty:", list(Playlist([])))
```

### Python output

```text
Track 7
Track 12
Track 18
Independent: 7 7
Empty: []
```

## C++20 example

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

### C++20 output

```text
Track 7
Track 12
Track 18
Empty: true
Independent positions: 12 7
```

## قارن اللغتين

Python delegates to the built-in list Iterator through `__iter__`; exhaustion raises StopIteration, which `for` handles. C++ demonstrates a custom forward Iterator, but returning standard iterators or ranges is usually simpler. Do not modify the collection while traversing either example.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدم `Iterators` أو `Ranges` قياسية عشان تعرض المرور من غير كشف التخزين.

### Use cases

مناسب للمرور على الـ `containers` والشجر؛ اختار الفئة حسب العمليات والتكلفة الفعلية.

**التكلفة:** الـ`Iterator` بيستعير البيانات ومش بيطوّل الـ`Lifetime` بتاعة المجموعة. لازم الـ`Playlist` تفضل موجودة وما تتنقلش أثناء استخدامه. القيمة `end` بتحدد نهاية النطاق، ومينفعش تقراها كأنها عنصر.

## جرّب تجاوب

1. هل نقدر نمشي في نفس الـ`Playlist` مرتين وكل مرة ليها مكان مستقل؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** اختبر قائمة فاضية و `Iterator` اتنين مستقلين؛ تحريك واحدة ما يحركش التانية.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
