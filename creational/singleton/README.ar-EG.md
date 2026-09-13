# Singleton

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/prototype/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/adapter/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — بيركز على إنشاء الـ`Objects` وإعدادها.

## Difficulty

متوسط

## In One Sentence

اسمح بوجود نسخة واحدة متاحة من النوع (`instance`)، وخد بالك من تكلفة الحالة العامة المشتركة (`shared global state`).

## ببساطة

كذا مستدعي محتاجين نفس عدّاد الطلبات.الـ`Singleton` بيتحكم في الإنشاء، بس مشاركة الـ`state` بتصعّب عزل الاختبارات والـ`Dependencies`.

## The Problem

عدادين `Metrics` منفصلين بيقسّموا إجمالي المفروض يكون واحد للعملية كلها.

## Naive Solution

```cpp
Metrics first;
Metrics second; // separate counters; assumes a public constructor
```

## Why It Becomes a Problem

لو الـ `constructor` عامة، كل `Caller` ممكن يعمل عداده، والإجمالي المشترك مش هيبقى مشترك.

## The Idea

اخفي الإنشاء وامنع النسخ. خلّي الدالة `instance` ترجع نفس المتغير المحلي، المعرّف بالكلمة `static`، في كل استدعاء.

## Real-World Analogy

مكتب صغير عنده دفتر زوار واحد وكل المكاتب بتكتب فيه.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Singleton](../../assets/diagrams/singleton.svg)

```text
Client A + B  -->  Metrics::instance()  -->  one Metrics
```

## Participants

في المثال، `Metrics` بتتحكم في عمر النسخة وبتخزّن العداد. الدالة `instance` بترجع مرجع مش مالك (`non-owning reference`)؛ ممنوع تحاول تحرر النسخة باستخدام `delete`.

الأدوار القياسية في المثال ده:

- [`instance`](../../GLOSSARY.md#instance) — كائن محدد (`object`) من نوع معين. هنا: `Metrics::instance()`.
- [`global state`](../../GLOSSARY.md#global-state) — بيانات أجزاء كتير تقدر توصلها، وتغييرها ممكن يأثر على كود بعيد. هنا: `Metrics::requests_`.
- [`thread-safe initialization`](../../GLOSSARY.md#thread-safe-initialization) — حماية التهيئة من الإنشاء المتزامن؛ مش معناها إن كل العمليات بعد كده `thread-safe`. هنا: `static Metrics metrics`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

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

## Example Output

```text
Same instance: true
Requests: 2
```

## When to Use

فكّر فيه بس لو الـ `instance` الواحدة شرط حقيقي على مستوى العملية وعمرها مناسب.

### Use cases

عداد تشخيص بسيط في `Thread` واحدة بيوضح الفكرة، مش توصية بمعمارية `Metrics` للإنتاج.

## When NOT to Use

بلاش لمجرد تسهيل الوصول للـ `dependencies`. مرّر `Metrics reference` صراحة لما الاختبارات محتاجة عزل.

## Advantages

فيه نقطة تهيئة واضحة وكل المستدعين بيوصلوا لنفس الـ `instance`.

## Trade-offs

الوصول العام بيخفي الـ `dependencies` وبيخلط الاختبارات. تهيئة الـ `static` آمنة بين الـ `Threads`، لكن `record` مش آمنة؛ التزامن محتاج حماية، وترتيب الإغلاق ممكن يفرق.

## Related Patterns

[Abstract Factory](../abstract-factory/README.ar-EG.md) · [Facade](../../structural/facade/README.ar-EG.md)

## Common Confusion

إدارة `object` واحدة بالـ [`dependency injection`](../../GLOSSARY.md#dependency-injection) مش بالضرورة `Singleton`؛ النوع نفسه مش لازم يفرض التفرد.

## Terms to Remember

- `Singleton` — اسمح بوجود نسخة واحدة متاحة من النوع (`instance`)، وخد بالك من تكلفة الحالة العامة المشتركة (`shared global state`).
- `instance` — كائن محدد (`object`) من نوع معين. مثال: `Metrics::instance()`.
- `global state` — بيانات أجزاء كتير تقدر توصلها، وتغييرها ممكن يأثر على كود بعيد. مثال: `Metrics::requests_`.
- `thread-safe initialization` — حماية التهيئة من الإنشاء المتزامن؛ مش معناها إن كل العمليات بعد كده `thread-safe`. مثال: `static Metrics metrics`.

## Interview Vocabulary

- [`dependency injection`](../../GLOSSARY.md#dependency-injection) — بتمرّر `dependency` من بره بدل ما الجزء اللي بيستخدمها يختارها أو يعملها بنفسه.
- [`testability`](../../GLOSSARY.md#testability) — سهولة عزل `behavior` وتشغيلها والتأكد من نتيجتها.
- [`lifetime`](../../GLOSSARY.md#lifetime) — الفترة اللي الـ `object` موجودة فيها وينفع تستخدمها حسب قواعدها.

## Interview Question

هل أمان التهيئة بين الـ `Threads` معناه إن `requests_` آمنة؟ فرّق بين العمليتين.

## Mini Challenge

غيّر المثال عشان تمرّر عداد لمهمتين، وبعدها اختبر عدادين معزولين.

## اختبر فهمك

1. إزاي اختبار يسيب `State` في العدّاد تأثر على الاختبار اللي بعده؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** عدادين `Metrics` منفصلين بيقسّموا إجمالي المفروض يكون واحد للعملية كلها.
- **الحل:** اخفي الإنشاء وامنع النسخ. خلّي الدالة `instance` ترجع نفس المتغير المحلي، المعرّف بالكلمة `static`، في كل استدعاء.
- **`Trade-off`:** الوصول العام بيخفي الـ `dependencies` وبيخلط الاختبارات. تهيئة الـ `static` آمنة بين الـ `Threads`، لكن `record` مش آمنة؛ التزامن محتاج حماية، وترتيب الإغلاق ممكن يفرق.
- **افتكر:** وجود نسخة واحدة (`instance`) مش معناه مشاكل أقل.

[السابق](../../creational/prototype/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/adapter/README.ar-EG.md)
