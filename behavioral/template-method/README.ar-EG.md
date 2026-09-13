# Template Method

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** ثبّت ترتيب خطوات الحل (`algorithm`)، وسيب تنفيذ خطوات معينة للأنواع المشتقة (`subclasses`).

## المشكلة

التقارير بتشترك في بداية وقراءة وتنسيق ونهاية، بس مصدر البيانات أو التنسيق مختلف. دوال كاملة لكل تقرير بتكرر الترتيب وممكن تختلف لما خطوة مشتركة تتعدل.

## الحل ببساطة

التقارير بتبدأ وتقرا البيانات وتنسّقها وبعدين تخلص.الـ`Template Method` بيحافظ على الترتيب في مكان واحد، والـ`subclass` بتنفّذ الجزء المتغير. ثبّت ترتيب الخطوات في `Report::generate`، وهي دالة مش `virtual`. جواها، نادِ `read` وبعدها `format`؛ الاتنين متعرّفين باستخدام `protected` و`virtual` عشان الأنواع المشتقة تقدر تغيّر تنفيذهم.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Template Method](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

في المثال، `Report` بتحدد ترتيب خطوات الحل، و `TextReport` بتنفّذ الخطوات المتغيرة. المستدعي (`Client`) بيبدأ العملية عن طريق `generate`.

الأدوار القياسية في المثال ده:

- [`Abstract Class`](../../GLOSSARY.md#abstract-class-template-method-role) — دور `Template Method` اللي ماسك `algorithm skeleton` وبيعلن الخطوات المتغيرة. هنا: `Report`.
- [`Concrete Class`](../../GLOSSARY.md#concrete-class-template-method-role) — دور `Template Method` اللي بيوفر الخطوات المتغيرة. هنا: `TextReport`.
- [`hook method`](../../GLOSSARY.md#hook-method) — عملية للتوسعة بتناديها خطوات ثابتة، وممكن يكون ليها `implementation` افتراضية. هنا: `read, format`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Report:
    def generate(self):
        print("Begin report")
        data = self.read()
        self.format(data)
        print("End report")

    def read(self):
        raise NotImplementedError

    def format(self, data):
        raise NotImplementedError


class TextReport(Report):
    def read(self):
        return "sales=42"

    def format(self, data):
        print(data)


if __name__ == "__main__":
    TextReport().generate()
```

### Python output

```text
Begin report
sales=42
End report
```

## C++20 example

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

### C++20 output

```text
Begin report
sales=42
End report
```

## قارن اللغتين

Both versions use Inheritance to keep the sequence in `generate` and vary individual steps. C++ marks the steps virtual and keeps the workflow non-virtual. Python can override any method, so keeping the sequence fixed is a design convention. Injected callables are an alternative when Composition fits better.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لتسلسل ثابت فيه نقاط توسعة قليلة وواضحة بالـ [`inheritance`](../../GLOSSARY.md#inheritance).

### Use cases

مناسب للاستيراد والتقارير لما الهيكل ثابت.

**التكلفة:** استخدام `Inheritance` بيخلّي الـ`subclass` تعتمد على عقد الـ`base class`. الـ `End` مش مضمونة لو `read` أو `format` رمت `Exception`؛ تنظيف الموارد الحقيقي محتاج [`RAII`](../../GLOSSARY.md#raii)، مش الاعتماد على آخر خطوة.

## جرّب تجاوب

1. أنهي method بتحدد الترتيب، وأنهي methods ممكن تختلف؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `CsvReport` وراجع الترتيب، وبعدها جرّب `Exception` في التنسيق وناقش تنظيف الموارد.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
