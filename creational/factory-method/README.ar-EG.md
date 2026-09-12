# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — Design Pattern بيركز على إزاي نعمل objects ونجهّزها.

## Difficulty

مبتدئ

## In One Sentence

خلّي subclass تختار الـ object اللي Workflow مشتركة هتستخدمه.

## The Problem

مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة Sender مختلفة.

## Naive Solution

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## Why It Becomes a Problem

تثبيت EmailSender جوه run بيربط الخطوات بالإيميل؛ نسخ run للـ Console بيكرر نفس المنطق.

ده `tight coupling`: خطوات الشغل مرتبطة بنوع Sender بعينه، فتغيير الإرسال ممكن يحتاج تعديل نفس الخطوات.

## The Idea

حط الخطوات في AlertJob وخليها تنادي make_sender القابلة للتغيير بالـ override.

## Real-World Analogy

مكتب التوصيل عنده نفس خطوات الشحن، وكل فرع بيختار وسيلة النقل.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## Participants

AlertJob ماسكة الخطوات. EmailJob و ConsoleJob بيغيّروا الإنشاء. Sender بتحدد العملية، و [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) (smart pointer بملكية حصرية، بتحرر الـ object لما المالك يتدمر) بتملك المنتج.

الأدوار القياسية في المثال ده:

- [`Creator`](../../GLOSSARY.md#creator) — الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها. هنا: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — subclass من Creator بتوفر Product معينة. هنا: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الـ object اللي كود الإنشاء بيرجعها. هنا: `Sender`.

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

استخدمه لما Workflow مبنية أصلاً على الـ [`inheritance`](../../GLOSSARY.md#inheritance) (بتعرّف derived class انطلاقاً من base class عشان تعيد استخدام العقد أو تخصصه) ومحتاجة نقطة إنشاء قابلة للتوسيع.

### Use cases

مناسب لتصدير بصيغ مختلفة أو Jobs حسب البيئة؛ الـ Senders هنا بتطبع بس.

## When NOT to Use

بلاش لو تمرير Sender جاهزة لـ function كفاية؛ الـ inheritance ساعتها زيادة.

## Advantages

الخطوات بتفضل في مكان واحد، واختيار المنتج بيتغير.

## Trade-offs

كل اختيار جديد ممكن يحتاج subclass. استدعاء الـ virtual method من constructor بتاعة base class مش هيوصل لـ [`implementation`](../../GLOSSARY.md#implementation) (الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد interface) بتاعة derived class زي ما تتوقع.

## Related Patterns

[Abstract Factory](../abstract-factory/README.ar-EG.md) · [Template Method](../../behavioral/template-method/README.ar-EG.md)

## Common Confusion

function عادية فيها switch اسمها Simple Factory ؛ هنا المقصود نقطة توسيع بالـ inheritance. Abstract Factory بتنظم عيلة منتجات.

## Terms to Remember

- `Factory Method` — خلّي subclass تختار الـ object اللي Workflow مشتركة هتستخدمه.
- `Creator` — الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها. مثال: `AlertJob`.
- `Concrete Creator` — subclass من Creator بتوفر Product معينة. مثال: `EmailJob, ConsoleJob`.
- `Product` — العقد بتاع الـ object اللي كود الإنشاء بيرجعها. مثال: `Sender`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز القيم الأولية وبدء lifetime بتاعة object.
- [`tight coupling`](../../GLOSSARY.md#tight-coupling) — الأجزاء معتمدة بقوة على التفاصيل الداخلية لبعض، فالتغيير في واحد بينتشر للباقي.
- [`inheritance`](../../GLOSSARY.md#inheritance) — بتعرّف derived class انطلاقاً من base class عشان تعيد استخدام العقد أو تخصصه.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — استهدف open for extension, closed for modification عند حدود مفيدة ومختارة بوضوح.

## Interview Question

ليه run بتنادي make_sender بعد الإنشاء، مش من constructor بتاعة AlertJob ؟

## Mini Challenge

ضيف FileJob بتكتب في ملف مؤقت، واتأكد من محتواه.

## Quick Summary

- **المشكلة:** مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة Sender مختلفة.
- **الحل:** حط الخطوات في AlertJob وخليها تنادي make_sender القابلة للتغيير بالـ override.
- **Trade-off:** كل اختيار جديد ممكن يحتاج subclass. استدعاء الـ virtual method من constructor بتاعة base class مش هيوصل لـ implementation بتاعة derived class زي ما تتوقع.
- **افتكر:** ثبّت الخطوات، وغيّر الإنشاء.

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)
