# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — بيركز على إنشاء الـ`Objects` وإعدادها.

## Difficulty

مبتدئ

## In One Sentence

خلّي الـ `subclass` هي اللي تحدد الـ `concrete object` اللي خطوات الشغل المشتركة (`workflow`) هتستخدمه.

## ببساطة

مهمة التنبيه بتبعت نفس الرسالة، بس وسيلة الإرسال بتختلف.الخطوات بتنادي `Factory Method`، وكل `subclass` بتعمل الـ`Sender` المناسب.

## The Problem

مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة `Sender` مختلفة.

## Naive Solution

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Why It Becomes a Problem

تثبيت `EmailSender` جوه `run` بيربط الخطوات بالإيميل؛ نسخ `run` للـ `Console` بيكرر نفس المنطق.

ده `tight coupling`: خطوات الشغل مرتبطة بنوع `Sender` بعينه، فتغيير الإرسال ممكن يحتاج تعديل نفس الخطوات.

## The Idea

حط خطوات الشغل المشتركة في `AlertJob`. خلّي إنشاء المرسِل مسؤولية الدالة `make_sender`، والأنواع المشتقة تغيّر تنفيذها باستخدام `override`.

## Real-World Analogy

مكتب التوصيل عنده نفس خطوات الشحن، وكل فرع بيختار وسيلة النقل.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Participants

في المثال، `AlertJob` ماسكة خطوات الشغل. اختيار طريقة الإنشاء بيتغير في `EmailJob` و `ConsoleJob`، وعقد الإرسال هو `Sender`. بنستخدم [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) لامتلاك المنتج وتحريره تلقائيًا لما المالك يتدمر.

الأدوار القياسية في المثال ده:

- [`Creator`](../../GLOSSARY.md#creator) — الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها. هنا: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — نوع مشتق (`subclass`) من `Creator`، مسؤول عن إنشاء منتج معين (`Product`). هنا: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. هنا: `Sender`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <memory>
#include <string_view>

struct Sender {
    virtual ~Sender() = default;
    virtual void send(std::string_view message) const = 0;
};
struct EmailSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Email: " << message << '\n'; }
};
struct ConsoleSender final : Sender {
    void send(std::string_view message) const override { std::cout << "Console: " << message << '\n'; }
};
class AlertJob {
protected:
    virtual std::unique_ptr<Sender> make_sender() const = 0;
public:
    virtual ~AlertJob() = default;
    void run() const {
        const auto sender = make_sender();
        sender->send("build complete");
    }
};
class EmailJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<EmailSender>(); }
};
class ConsoleJob final : public AlertJob {
    std::unique_ptr<Sender> make_sender() const override { return std::make_unique<ConsoleSender>(); }
};
int main() {
    EmailJob{}.run();
    ConsoleJob{}.run();
}
```

## Example Output

```text
Email: build complete
Console: build complete
```

## When to Use

استخدمه لما `Workflow` مبنية أصلاً على الـ [`inheritance`](../../GLOSSARY.md#inheritance) ومحتاجة نقطة إنشاء قابلة للتوسيع.

### Use cases

مناسب لتصدير بصيغ مختلفة أو `Jobs` حسب البيئة؛ الـ `Senders` هنا بتطبع بس.

## When NOT to Use

بلاش لو تمرير `Sender` جاهزة لـ `function` كفاية؛ الـ `inheritance` ساعتها زيادة.

## Advantages

الخطوات بتفضل في مكان واحد، واختيار المنتج بيتغير.

## Trade-offs

كل اختيار جديد ممكن يحتاج نوع مشتق (`subclass`). خد بالك من الاستدعاء أثناء الإنشاء: لو ناديت `virtual method` من دالة الإنشاء (`constructor`) في النوع الأساسي (`base class`)، النداء مش هيوصل لتنفيذ النوع المشتق (`derived class`). المقصود بـ [`implementation`](../../GLOSSARY.md#implementation) هو الكود الفعلي اللي بينفّذ العملية.

## Related Patterns

[Abstract Factory](../abstract-factory/README.ar-EG.md) · [Template Method](../../behavioral/template-method/README.ar-EG.md)

## Common Confusion

وجود دالة عادية (`function`) فيها `switch` لاختيار المنتج بنسميه `Simple Factory`. أما هنا، فبنستخدم نقطة توسعة بالوراثة (`inheritance`). نمط `Abstract Factory` بينظم إنشاء عيلة منتجات مرتبطة.

## Terms to Remember

- `Factory Method` — خلّي الـ `subclass` هي اللي تحدد الـ `concrete object` اللي خطوات الشغل المشتركة (`workflow`) هتستخدمه.
- `Creator` — الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها. مثال: `AlertJob`.
- `Concrete Creator` — نوع مشتق (`subclass`) من `Creator`، مسؤول عن إنشاء منتج معين (`Product`). مثال: `EmailJob, ConsoleJob`.
- `Product` — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. مثال: `Sender`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).
- [`tight coupling`](../../GLOSSARY.md#tight-coupling) — الأجزاء معتمدة بقوة على التفاصيل الداخلية لبعض، فالتغيير في واحد بينتشر للباقي.
- [`inheritance`](../../GLOSSARY.md#inheritance) — بتبني نوع مشتق (`derived class`) على أساس نوع موجود (`base class`)، عشان تعيد استخدام العقد أو تخصصه.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — خلّي التوسيع ممكن من غير تعديل الكود المستقر، عند حدود مختارة بوضوح. التعبير هو `open for extension, closed for modification`.

## Interview Question

ليه `run` بتنادي `make_sender` بعد الإنشاء، مش من `constructor` بتاعة `AlertJob`؟

## Mini Challenge

ضيف `FileJob` بتكتب في ملف مؤقت، واتأكد من محتواه.

## اختبر فهمك

1. اختيار الـ`Sender` بيحصل فين، وإيه الخطوات اللي بتفضل مشتركة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة `Sender` مختلفة.
- **الحل:** حط خطوات الشغل المشتركة في `AlertJob`. خلّي إنشاء المرسِل مسؤولية الدالة `make_sender`، والأنواع المشتقة تغيّر تنفيذها باستخدام `override`.
- **`Trade-off`:** كل اختيار جديد ممكن يحتاج نوع مشتق (`subclass`). خد بالك من الاستدعاء أثناء الإنشاء: لو ناديت `virtual method` من دالة الإنشاء (`constructor`) في النوع الأساسي (`base class`)، النداء مش هيوصل لتنفيذ النوع المشتق (`derived class`). المقصود بـ `implementation` هو الكود الفعلي اللي بينفّذ العملية.
- **افتكر:** ثبّت الخطوات، وغيّر الإنشاء.

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)
