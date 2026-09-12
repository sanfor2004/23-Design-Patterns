# Template Method

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/strategy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/visitor/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على السلوك (`behavior`) والتعاون بين الكائنات (`objects`)، وده واحد من أغراض الـ `Design Patterns`.

## Difficulty

متوسط

## In One Sentence

ثبّت ترتيب خطوات الحل (`algorithm`)، وسيب تنفيذ خطوات معينة للأنواع المشتقة (`subclasses`).

## The Problem

التقارير بتشترك في بداية وقراءة وتنسيق ونهاية، بس مصدر البيانات أو التنسيق مختلف.

## Naive Solution

```cpp
void text_report() { /* begin, read, format, end */ }
void html_report() { /* duplicated order, different format */ }
```

## Why It Becomes a Problem

دوال كاملة لكل تقرير بتكرر الترتيب وممكن تختلف لما خطوة مشتركة تتعدل.

## The Idea

ثبّت ترتيب الخطوات في `Report::generate`، وهي دالة مش `virtual`. جواها، نادِ `read` وبعدها `format`؛ الاتنين متعرّفين باستخدام `protected` و`virtual` عشان الأنواع المشتقة تقدر تغيّر تنفيذهم.

## Real-World Analogy

الوصفة بتثبت ترتيب التحضير مع حرية اختيار الحشو.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Template Method](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

## Participants

في المثال، `Report` بتحدد ترتيب خطوات الحل، و `TextReport` بتنفّذ الخطوات المتغيرة. المستدعي (`Client`) بيبدأ العملية عن طريق `generate`.

الأدوار القياسية في المثال ده:

- [`Abstract Class`](../../GLOSSARY.md#abstract-class-template-method-role) — دور `Template Method` اللي ماسك `algorithm skeleton` وبيعلن الخطوات المتغيرة. هنا: `Report`.
- [`Concrete Class`](../../GLOSSARY.md#concrete-class-template-method-role) — دور `Template Method` اللي بيوفر الخطوات المتغيرة. هنا: `TextReport`.
- [`hook method`](../../GLOSSARY.md#hook-method) — عملية للتوسعة بتناديها خطوات ثابتة، وممكن يكون ليها `implementation` افتراضية. هنا: `read, format`.

## Modern C++20 Example

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

## Example Output

```text
Begin report
sales=42
End report
```

## When to Use

استخدمه لتسلسل ثابت فيه نقاط توسعة قليلة وواضحة بالـ [`inheritance`](../../GLOSSARY.md#inheritance) (بتبني نوع مشتق (`derived class`) على أساس نوع موجود (`base class`)، عشان تعيد استخدام العقد أو تخصصه).

### Use cases

مناسب للاستيراد والتقارير لما الهيكل ثابت.

## When NOT to Use

بلاش لو الخطوات لازم يتغير ترتيبها وقت [`runtime`](../../GLOSSARY.md#runtime) (الوقت اللي البرنامج فيه شغال بعد البناء) أو الـ [`composition`](../../GLOSSARY.md#composition) (بتبني السلوك (`behavior`) عن طريق كائنات متعاونة (`objects`)، كل واحد منها بيستخدم أو بيحتوي كائنات تانية) أوضح.

## Advantages

الترتيب المشترك يفضل في الأساس، والابن يكتب الاختلاف بس.

## Trade-offs

الـ `inheritance` بتربط الابن بعقد الأساس. الـ `End` مش مضمونة لو `read` أو `format` رمت `Exception`؛ تنظيف الموارد الحقيقي محتاج [`RAII`](../../GLOSSARY.md#raii) (اربط المورد بعمر الكائن، عشان `destructor` تحرره تلقائياً؛ والاسم الكامل هو `Resource Acquisition Is Initialization`)، مش الاعتماد على آخر خطوة.

## Related Patterns

[Strategy](../strategy/README.ar-EG.md) · [Factory Method](../../creational/factory-method/README.ar-EG.md)

## Common Confusion

الـ `Strategy` بتحقن `behavior` قابل للتبديل. الـ `Template Method` بتستخدم `Hooks` موروثة، وممكن `Factory Method` تبقى خطوة إنشاء جوه الهيكل.

## Terms to Remember

- `Template Method` — ثبّت ترتيب خطوات الحل (`algorithm`)، وسيب تنفيذ خطوات معينة للأنواع المشتقة (`subclasses`).
- `Abstract Class` — دور `Template Method` اللي ماسك `algorithm skeleton` وبيعلن الخطوات المتغيرة. مثال: `Report`.
- `Concrete Class` — دور `Template Method` اللي بيوفر الخطوات المتغيرة. مثال: `TextReport`.
- `hook method` — عملية للتوسعة بتناديها خطوات ثابتة، وممكن يكون ليها `implementation` افتراضية. مثال: `read, format`.

## Interview Vocabulary

- [`algorithm skeleton`](../../GLOSSARY.md#algorithm-skeleton) — ترتيب `algorithm` الثابت اللي بعض خطواته ممكن تتغير.
- [`inheritance`](../../GLOSSARY.md#inheritance) — بتبني نوع مشتق (`derived class`) على أساس نوع موجود (`base class`)، عشان تعيد استخدام العقد أو تخصصه.
- [`Open/Closed Principle`](../../GLOSSARY.md#openclosed-principle) — خلّي التوسيع ممكن من غير تعديل الكود المستقر، عند حدود مختارة بوضوح. التعبير هو `open for extension, closed for modification`.

## Interview Question

ليه `generate` مش `virtual` و `read` و `format virtual`؟ ده بيوضح ثوابت إيه؟

## Mini Challenge

ضيف `CsvReport` وراجع الترتيب، وبعدها جرّب `Exception` في التنسيق وناقش تنظيف الموارد.

## Quick Summary

- **المشكلة:** التقارير بتشترك في بداية وقراءة وتنسيق ونهاية، بس مصدر البيانات أو التنسيق مختلف.
- **الحل:** ثبّت ترتيب الخطوات في `Report::generate`، وهي دالة مش `virtual`. جواها، نادِ `read` وبعدها `format`؛ الاتنين متعرّفين باستخدام `protected` و`virtual` عشان الأنواع المشتقة تقدر تغيّر تنفيذهم.
- **`Trade-off`:** الـ `inheritance` بتربط الابن بعقد الأساس. الـ `End` مش مضمونة لو `read` أو `format` رمت `Exception`؛ تنظيف الموارد الحقيقي محتاج `RAII`، مش الاعتماد على آخر خطوة.
- **افتكر:** ثبّت الوصفة، وغيّر الخطوات.

[السابق](../../behavioral/strategy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/visitor/README.ar-EG.md)
