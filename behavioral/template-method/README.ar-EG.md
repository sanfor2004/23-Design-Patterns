# طريقة القالب

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/strategy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/visitor/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

ثبّت ترتيب الخوارزمية وخلي الـ Subclasses تنفّذ خطوات مختارة.

## المشكلة

التقارير بتشترك في بداية وقراءة وتنسيق ونهاية، بس مصدر البيانات أو التنسيق مختلف.

## حل بسيط في الأول

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## ليه الحل بيصعّب الدنيا

دوال كاملة لكل تقرير بتكرر الترتيب وممكن تختلف لما خطوة مشتركة تتعدل.

## الفكرة الأساسية

Report::generate مش Virtual، وبتنادي read وformat المحميتين والـ Virtual بالترتيب.

## مثال من الحياة

الوصفة بتثبت ترتيب التحضير مع حرية اختيار الحشو.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![طريقة القالب](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## الأدوار

Report ماسكة هيكل الخطوات، TextReport بتنّفذ الاختلاف، والـ Client بينادي generate.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Report {
protected:
    virtual std::string read() const = 0;
    virtual void format(std::string_view data) const = 0;
public:
    virtual ~Report() = default;
    void generate() const {
        std::cout << "Begin report\n";
        const auto data = read();
        format(data);
        std::cout << "End report\n";
    }
};
class TextReport final : public Report {
    std::string read() const override { return "sales=42"; }
    void format(std::string_view data) const override { std::cout << data << '\n'; }
};
int main() { TextReport{}.generate(); }
```

## الناتج المتوقع

```text
Begin report
sales=42
End report
```

## إمتى تستخدمه

استخدمه لتسلسل ثابت فيه نقاط توسعة قليلة وواضحة بالوراثة.

## إمتى ما تستخدموش

بلاش لو الخطوات لازم يتغير ترتيبها وقت التشغيل أو الـ Composition أوضح.

## المميزات

الترتيب المشترك يفضل في الأساس، والابن يكتب الاختلاف بس.

## العيوب والمقايضات

الوراثة بتربط الابن بعقد الأساس. End مش مضمونة لو read أوformat رمت Exception؛ تنظيف الموارد الحقيقي محتاج RAII، مش الاعتماد على آخر خطوة.

## استخدامات تقنية

مناسب للاستيراد والتقارير لما الهيكل ثابت.

## أنماط مرتبطة

[strategy](../strategy/README.ar-EG.md) · [factory-method](../../creational/factory-method/README.ar-EG.md)

## لخبطة شائعة

Strategy بتحقن سلوك قابل للتبديل. Template Method بتستخدم Hooks موروثة، وممكن Factory Method تبقى خطوة إنشاء جوه الهيكل.

## سؤال انترفيو

ليه generate مش Virtual وread وformat Virtual؟ ده بيوضح ثوابت إيه؟

## تحدي صغير

ضيف CsvReport وراجع الترتيب، وبعدها جرّب Exception في التنسيق وناقش تنظيف الموارد.

## الخلاصة

- **المشكلة:** التقارير بتشترك في بداية وقراءة وتنسيق ونهاية، بس مصدر البيانات أو التنسيق مختلف.
- **الحل:** Report::generate مش Virtual، وبتنادي read وformat المحميتين والـ Virtual بالترتيب.
- **المقايضة:** الوراثة بتربط الابن بعقد الأساس. End مش مضمونة لو read أوformat رمت Exception؛ تنظيف الموارد الحقيقي محتاج RAII، مش الاعتماد على آخر خطوة.
- **افتكر:** ثبّت الوصفة، وغيّر الخطوات.

[السابق](../../behavioral/strategy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/visitor/README.ar-EG.md)
