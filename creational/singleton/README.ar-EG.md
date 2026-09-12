# الكائن الوحيد

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/prototype/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/adapter/README.ar-EG.md)

## الفئة

الإنشاء

## المستوى

متوسط

## في جملة واحدة

قيّد النوع بنسخة واحدة متاحة، مع حساب تكلفة الحالة العامة المشتركة.

## المشكلة

عدادين Metrics منفصلين بيقسّموا إجمالي المفروض يكون واحد للعملية كلها.

## حل بسيط في الأول

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## ليه الحل بيصعّب الدنيا

لو الـ Constructor عامة، كل Caller ممكن يعمل عداده، والإجمالي المشترك مش هيبقى مشترك.

## الفكرة الأساسية

اخفي الإنشاء، امنع النسخ، ورجّع Static محلية من دالة instance.

## مثال من الحياة

مكتب صغير عنده دفتر زوار واحد وكل المكاتب بتكتب فيه.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الكائن الوحيد](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## الأدوار

Metrics بتتحكم في عمرها وبتخزّن العداد. instance بترجع Reference مش مالكة؛ ممنوع تعمل لها delete.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>

class Metrics {
    int requests_ = 0;
    Metrics() = default;
public:
    Metrics(const Metrics&) = delete;
    Metrics& operator=(const Metrics&) = delete;
    static Metrics& instance() {
        static Metrics metrics;
        return metrics;
    }
    void record() { ++requests_; }
    int requests() const { return requests_; }
};
int main() {
    auto& first = Metrics::instance();
    auto& second = Metrics::instance();
    first.record();
    second.record();
    std::cout << "Same instance: " << std::boolalpha << (&first == &second) << '\n';
    std::cout << "Requests: " << first.requests() << '\n';
}
```

## الناتج المتوقع

```text
Same instance: true
Requests: 2
```

## إمتى تستخدمه

فكّر فيه بس لو النسخة الواحدة شرط حقيقي على مستوى العملية وعمرها مناسب.

## إمتى ما تستخدموش

بلاش لمجرد تسهيل الوصول للاعتماديات. مرّر Metrics Reference صراحة لما الاختبارات محتاجة عزل.

## المميزات

فيه نقطة تهيئة واضحة وكل المستدعين بيوصلوا لنفس النسخة.

## العيوب والمقايضات

الوصول العام بيخفي الاعتماديات وبيخلط الاختبارات. تهيئة الـ Static آمنة بين الـ Threads، لكن record مش آمنة؛ التزامن محتاج حماية، وترتيب الإغلاق ممكن يفرق.

## استخدامات تقنية

عداد تشخيص بسيط في Thread واحدة بيوضح الفكرة، مش توصية بمعمارية Metrics للإنتاج.

## أنماط مرتبطة

[abstract-factory](../abstract-factory/README.ar-EG.md) · [facade](../../structural/facade/README.ar-EG.md)

## لخبطة شائعة

إدارة Object واحدة بالـ Dependency Injection مش بالضرورة Singleton؛ النوع نفسه مش لازم يفرض التفرد.

## سؤال انترفيو

هل أمان التهيئة بين الـ Threads معناه إن requests_ آمنة؟ فرّق بين العمليتين.

## تحدي صغير

غيّر المثال عشان تمرّر عداد لمهمتين، وبعدها اختبر عدادين معزولين.

## الخلاصة

- **المشكلة:** عدادين Metrics منفصلين بيقسّموا إجمالي المفروض يكون واحد للعملية كلها.
- **الحل:** اخفي الإنشاء، امنع النسخ، ورجّع Static محلية من دالة instance.
- **المقايضة:** الوصول العام بيخفي الاعتماديات وبيخلط الاختبارات. تهيئة الـ Static آمنة بين الـ Threads، لكن record مش آمنة؛ التزامن محتاج حماية، وترتيب الإغلاق ممكن يفرق.
- **افتكر:** نسخة واحدة مش معناها مشاكل أقل.

[السابق](../../creational/prototype/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/adapter/README.ar-EG.md)
