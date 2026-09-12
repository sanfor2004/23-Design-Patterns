# المكرّر

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)

## الفئة

السلوك

## المستوى

مبتدئ

## في جملة واحدة

لف على مجموعة من خلال طريقة وصول ثابتة.

## المشكلة

الـ Client محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.

## حل بسيط في الأول

```cpp
for (std::size_t i = 0; i < tracks.size(); ++i) {
    std::cout << tracks[i];
}
```

## ليه الحل بيصعّب الدنيا

كود الـ Index مربوط بـ vector عامة بيكشف التمثيل وبيوزع حساب الحدود.

## الفكرة الأساسية

وفّر begin وend وIterator بتدعم القراءة والزيادة والمقارنة.

## مثال من الحياة

زي مسار متحف تمشيه قطعة قطعة من غير ما تعرف قاعدة بيانات الغرف.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المكرّر](../../assets/diagrams/iterator.svg)

```text
range-for client  -->  Playlist::Iterator  -->  private tracks
```

## الأدوار

Playlist بتمتلك الأغاني؛ Iterator بتستعير الـ vector وبتحفظ الموضع. Range-for هي العميل، وstatic_assert بتراجع forward_iterator في C++20.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
Track 7
Track 12
Track 18
```

## إمتى تستخدمه

استخدم Iterators أو Ranges قياسية عشان تعرض المرور من غير كشف التخزين.

## إمتى ما تستخدموش

بلاش Iterator مخصصة لو const iterators موجودة أو Range كفاية؛ التنفيذ هنا للتعليم.

## المميزات

الخوارزميات بتستخدم بروتوكول موحد، وكل Iterator ليها موضع مستقل.

## العيوب والمقايضات

الـ Iterator مش بتطوّل عمر المجموعة. نقل أو تدمير Playlist يبطل الافتراضات، وقراءة end غير صالحة زي القياسي.

## استخدامات تقنية

مناسب للمرور على الحاويات والشجر؛ اختار الفئة حسب العمليات والتكلفة الفعلية.

## أنماط مرتبطة

[composite](../../structural/composite/README.ar-EG.md) · [visitor](../visitor/README.ar-EG.md)

## لخبطة شائعة

Visitor بتختار العملية حسب نوع العنصر. Iterator بتدير المرور من غير ما تعرف هتعمل إيه بالعنصر.

## سؤال انترفيو

ليه المقارنة بتراجع Pointer الـ vector كمان، مش الـ Index بس؟

## تحدي صغير

اختبر قائمة فاضية وIterator اتنين مستقلين؛ تحريك واحدة ما يحركش التانية.

## الخلاصة

- **المشكلة:** الـ Client محتاج يقرأ أغاني القائمة من غير ما يدخل على التخزين الخاص.
- **الحل:** وفّر begin وend وIterator بتدعم القراءة والزيادة والمقارنة.
- **المقايضة:** الـ Iterator مش بتطوّل عمر المجموعة. نقل أو تدمير Playlist يبطل الافتراضات، وقراءة end غير صالحة زي القياسي.
- **افتكر:** امشي على البيانات من غير ما تفتح الحاوية.

[السابق](../../behavioral/interpreter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/mediator/README.ar-EG.md)
