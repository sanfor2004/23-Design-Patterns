# Decorator

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** ضيف سلوك جديد (`behavior`) عن طريق كائن بيغلّف الكائن الأصلي. حافظ على نفس [`interface`](../../GLOSSARY.md#interface)، يعني نفس العمليات المتاحة للمستدعي.

## المشكلة

طلب القهوة ممكن يحتاج لبن مرة أو مرتين من غير `class` لكل تركيبة. الـ `classes` التركيبات بتكرر السعر الأساسي، وعددها بيزيد مع كل إضافة.

## الحل ببساطة

المشروب ممكن يكون عليه إضافات اختيارية.كل `Decorator` بيوفر نفس الـ`Interface` وبيضيف شغله قبل أو بعد استدعاء اللي جواه. خلّي طبقة الإضافة `Milk` تمتلك مشروب من نوع `Drink`. الأول بتطلب منه الوصف والسعر، وبعدها بتضيف وصفها وتكلفتها على النتيجة.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Decorator](../../assets/diagrams/decorator.svg)

```text
Client  -->  Milk(Drink)  -->  Coffee or Milk
```

في المثال، العقد المشترك هو `Drink`، والتنفيذ الأساسي هو `Coffee`. طبقة الإضافة `Milk` بتغلّف مشروب واحد. المستدعي (`Client`) بيمتلك الطبقة الخارجية.

الأدوار القياسية في المثال ده:

- [`Component`](../../GLOSSARY.md#component) — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. هنا: `Drink`.
- [`Concrete Component`](../../GLOSSARY.md#concrete-component) — الـ `implementation` الأساسية قبل إضافة طبقات اختيارية. هنا: `Coffee`.
- [`Concrete Decorator`](../../GLOSSARY.md#concrete-decorator) — طبقة تغليف (`Wrapper`) بتحافظ على عقد `Component`، وبتضيف مسؤولية محددة (`responsibility`). هنا: `Milk`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Coffee:
    def description(self):
        return "coffee"

    def price_cents(self):
        return 1000


class Milk:
    def __init__(self, inner):
        self.inner = inner

    def description(self):
        return self.inner.description() + " + milk"

    def price_cents(self):
        return self.inner.price_cents() + 200


if __name__ == "__main__":
    drink = Milk(Milk(Coffee()))
    print(f"{drink.description()}: {drink.price_cents()} cents")
```

### Python output

```text
coffee + milk + milk: 1400 cents
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

struct Drink {
    virtual ~Drink() = default;
    virtual std::string description() const = 0;
    virtual int price_cents() const = 0;
};
struct Coffee final : Drink {
    std::string description() const override { return "coffee"; }
    int price_cents() const override { return 10; }
};
class Milk final : public Drink {
    std::unique_ptr<Drink> inner_;
public:
    explicit Milk(std::unique_ptr<Drink> inner) : inner_(std::move(inner)) {
        if (!inner_) throw std::invalid_argument("Missing drink");
    }
    std::string description() const override { return inner_->description() + " + milk"; }
    int price_cents() const override { return inner_->price_cents() + 2; }
};
int main() {
    std::unique_ptr<Drink> drink = std::make_unique<Coffee>();
    drink = std::make_unique<Milk>(std::move(drink));
    drink = std::make_unique<Milk>(std::move(drink));
    std::cout << drink->description() << ": " << drink->price_cents() << '\n';
}
```

### C++20 output

```text
coffee + milk + milk: 14
```

## قارن اللغتين

This is the GoF Object-wrapping Decorator, not Python function-decorator syntax. Python retains the wrapped drink; C++ transfers exclusive Ownership into each wrapper. Prices use integer cents. A list of ingredients is simpler if price addition is the whole problem.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لإضافة سلوك اختياري (`behavior`) قابل للتركيب وبيحافظ على عقد العنصر الأصلي.

### Use cases

ينفع لطبقات ضغط وتشفير الـ `Streams`، مع الانتباه للترتيب والأخطاء.

**التكلفة:** ترتيب الطبقات ممكن يغيّر الـ `behavior`، وكتر الـ `objects` الصغيرة بيصعّب التتبع. نفس الـ `interface` مش ضمان لنفس الوعود المرتبطة بالـ `behavior`.

## جرّب تجاوب

1. ليه `Milk` تقدر تغلّف `Milk` تانية من غير معرفة النوع الفعلي؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Syrup` بسعر 3 وجرّب ترتيبين، واشرح اختلاف الوصف.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
