# Factory Method

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** خلّي الـ `subclass` هي اللي تحدد الـ `concrete object` اللي خطوات الشغل المشتركة (`workflow`) هتستخدمه.

## المشكلة

مهمة التنبيه بتبعت نفس رسالة الانتهاء، بس كل بيئة محتاجة `Sender` مختلفة. تثبيت `EmailSender` جوه `run` بيربط الخطوات بالإيميل؛ نسخ `run` للـ `Console` بيكرر نفس المنطق.

ده `tight coupling`: خطوات الشغل مرتبطة بنوع `Sender` بعينه، فتغيير الإرسال ممكن يحتاج تعديل نفس الخطوات.

## الحل ببساطة

مهمة التنبيه بتبعت نفس الرسالة، بس وسيلة الإرسال بتختلف.الخطوات بتنادي `Factory Method`، وكل `subclass` بتعمل الـ`Sender` المناسب. حط خطوات الشغل المشتركة في `AlertJob`. خلّي إنشاء المرسِل مسؤولية الدالة `make_sender`، والأنواع المشتقة تغيّر تنفيذها باستخدام `override`.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Factory Method](../../assets/diagrams/factory-method.svg)

```text
AlertJob::run  -->  make_sender()  -->  Sender
```

في المثال، `AlertJob` ماسكة خطوات الشغل. اختيار طريقة الإنشاء بيتغير في `EmailJob` و `ConsoleJob`، وعقد الإرسال هو `Sender`. بنستخدم [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr) لامتلاك المنتج وتحريره تلقائيًا لما المالك يتدمر.

الأدوار القياسية في المثال ده:

- [`Creator`](../../GLOSSARY.md#creator) — الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها. هنا: `AlertJob`.
- [`Concrete Creator`](../../GLOSSARY.md#concrete-creator) — نوع مشتق (`subclass`) من `Creator`، مسؤول عن إنشاء منتج معين (`Product`). هنا: `EmailJob, ConsoleJob`.
- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. هنا: `Sender`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class EmailSender:
    def send(self, message):
        print("Email:", message)


class ConsoleSender:
    def send(self, message):
        print("Console:", message)


class AlertJob:
    def make_sender(self):
        raise NotImplementedError

    def run(self):
        sender = self.make_sender()
        sender.send("build complete")


class EmailJob(AlertJob):
    def make_sender(self):
        return EmailSender()


class ConsoleJob(AlertJob):
    def make_sender(self):
        return ConsoleSender()


if __name__ == "__main__":
    EmailJob().run()
    ConsoleJob().run()
```

### Python output

```text
Email: build complete
Console: build complete
```

## C++20 example

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

### C++20 output

```text
Email: build complete
Console: build complete
```

## قارن اللغتين

Both versions keep a workflow in a base Class and override its creation method. Python checks the returned Object when `send` is called; C++ declares a Sender Interface and transfers Ownership with `unique_ptr`. A standalone factory function is often enough outside an inherited workflow.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما `Workflow` مبنية أصلاً على الـ [`inheritance`](../../GLOSSARY.md#inheritance) ومحتاجة نقطة إنشاء قابلة للتوسيع.

### Use cases

مناسب لتصدير بصيغ مختلفة أو `Jobs` حسب البيئة؛ الـ `Senders` هنا بتطبع بس.

**التكلفة:** كل اختيار جديد ممكن يحتاج نوع مشتق (`subclass`). خد بالك من الاستدعاء أثناء الإنشاء: لو ناديت `virtual method` من دالة الإنشاء (`constructor`) في النوع الأساسي (`base class`)، النداء مش هيوصل لتنفيذ النوع المشتق (`derived class`). المقصود بـ [`implementation`](../../GLOSSARY.md#implementation) هو الكود الفعلي اللي بينفّذ العملية.

## جرّب تجاوب

1. اختيار الـ`Sender` بيحصل فين، وإيه الخطوات اللي بتفضل مشتركة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `FileJob` بتكتب في ملف مؤقت، واتأكد من محتواه.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
