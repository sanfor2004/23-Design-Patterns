# طريقة المصنع

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)

## الفئة

الإنشاء

## المستوى

مبتدئ

## في جملة واحدة

خلّي Subclass تختار الـ Object اللي Workflow مشتركة هتستخدمه.

## المشكلة

مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة Sender مختلفة.

## حل بسيط في الأول

```cpp
void run() {
    EmailSender sender;
    sender.send("build complete");
}
```

## ليه الحل بيصعّب الدنيا

تثبيت EmailSender جوه run بيربط الخطوات بالإيميل؛ نسخ run للـ Console بيكرر نفس المنطق.

## الفكرة الأساسية

حط الخطوات في AlertJob وخليها تنادي make_sender القابلة للتغيير بالـ Override.

## مثال من الحياة

مكتب التوصيل عنده نفس خطوات الشحن، وكل فرع بيختار وسيلة النقل.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![طريقة المصنع](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

## الأدوار

AlertJob ماسكة الخطوات. EmailJob وConsoleJob بيغيّروا الإنشاء. Sender بتحدد العملية، وunique_ptr بتملك المنتج.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
Email: build complete
Console: build complete
```

## إمتى تستخدمه

استخدمه لما Workflow مبنية أصلاً على الوراثة ومحتاجة نقطة إنشاء قابلة للتوسيع.

## إمتى ما تستخدموش

بلاش لو تمرير Sender جاهزة لدالة كفاية؛ الوراثة ساعتها زيادة.

## المميزات

الخطوات بتفضل في مكان واحد، واختيار المنتج بيتغير.

## العيوب والمقايضات

كل اختيار جديد ممكن يحتاج Subclass. استدعاء الدالة الافتراضية من Constructor الأساس مش هيوصل لتنفيذ الابن زي ما تتوقع.

## استخدامات تقنية

مناسب لتصدير بصيغ مختلفة أو Jobs حسب البيئة؛ الـ Senders هنا بتطبع بس.

## أنماط مرتبطة

[abstract-factory](../abstract-factory/README.ar-EG.md) · [template-method](../../behavioral/template-method/README.ar-EG.md)

## لخبطة شائعة

دالة عادية فيها switch اسمها Simple Factory؛ هنا المقصود نقطة توسيع بالوراثة. Abstract Factory بتنظم عيلة منتجات.

## سؤال انترفيو

ليه run بتنادي make_sender بعد الإنشاء، مش من Constructor بتاعة AlertJob؟

## تحدي صغير

ضيف FileJob بتكتب في ملف مؤقت، واتأكد من محتواه.

## الخلاصة

- **المشكلة:** مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة Sender مختلفة.
- **الحل:** حط الخطوات في AlertJob وخليها تنادي make_sender القابلة للتغيير بالـ Override.
- **المقايضة:** كل اختيار جديد ممكن يحتاج Subclass. استدعاء الدالة الافتراضية من Constructor الأساس مش هيوصل لتنفيذ الابن زي ما تتوقع.
- **افتكر:** ثبّت الخطوات، وغيّر الإنشاء.

[السابق](../../creational/builder/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/prototype/README.ar-EG.md)
