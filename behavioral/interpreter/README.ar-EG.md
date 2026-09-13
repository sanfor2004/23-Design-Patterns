# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** مثّل قواعد لغة صغيرة بكائنات (`objects`)، بحيث كل كائن يعرف يقيّم الجزء المسؤول عنه.

## المشكلة

قواعد السماح بتجمع أسماء `Roles` و `AND`، ومحتاجين نبني القواعد كبيانات. تعبير `Boolean` ثابت بسيط، بس تغيير شكل قواعد متداخلة بيحتاج تعديل كود التطبيق.

## الحل ببساطة

قاعدة السماح ممكن تحتاج دور `editor` ودور `verified` مع بعض.كل جزء بيقيّم قاعدة، والتعبير الكبير بيتركّب من تعبيرات أصغر. مثّل فحص الدور بتعبير نهائي (`Terminal Expression`) اسمه `Role`. التعبير المركّب `Both` بيجمع تعبيرين باستخدام `AND`. لو الأول رجع نتيجة سلبية، مش محتاج تقيّم التاني؛ ده اسمه `short-circuit evaluation`.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Interpreter](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

في المثال، `Expression` بتحدد عقد التقييم. بيانات التقييم موجودة في `Context`، والتعبير `Role` بيفحص وجود دور معين. التعبير المركّب `Both` بيمتلك التعبيرين اللي بيقيّمهم.

الأدوار القياسية في المثال ده:

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — عقد تقييم العقد اللي بتمثل قواعد `Interpreter`. هنا: `Expression`.
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — تعبير مافيش جواه تعبيرات أطفال. هنا: `Role`.
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — تعبير بيركب تعبيرات أصغر حسب قاعدة في اللغة. هنا: `Both`.
- `Context` — البيانات اللي التعبيرات بتستخدمها وقت التقييم؛ هنا مجموعة أسماء الصلاحيات. `Context`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Role:
    def __init__(self, name):
        self.name = name

    def evaluate(self, context):
        return self.name in context


class Both:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, context):
        return self.left.evaluate(context) and self.right.evaluate(context)


if __name__ == "__main__":
    rule = Both(Role("editor"), Role("verified"))
    for context in [set(), {"editor"}, {"editor", "verified"}]:
        print(rule.evaluate(context))
```

### Python output

```text
False
False
True
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>

using Context = std::unordered_set<std::string>;
struct Expression {
    virtual ~Expression() = default;
    virtual bool evaluate(const Context& context) const = 0;
};
class Role final : public Expression {
    std::string name_;
public:
    explicit Role(std::string name) : name_(std::move(name)) {}
    bool evaluate(const Context& context) const override { return context.contains(name_); }
};
class Both final : public Expression {
    std::unique_ptr<Expression> left_, right_;
public:
    Both(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {
        if (!left_ || !right_) throw std::invalid_argument("Missing expression");
    }
    bool evaluate(const Context& context) const override {
        return left_->evaluate(context) && right_->evaluate(context);
    }
};
int main() {
    const Both rule{std::make_unique<Role>("editor"), std::make_unique<Role>("verified")};
    std::cout << std::boolalpha << rule.evaluate(Context{"editor"}) << '\n';
    std::cout << rule.evaluate(Context{"editor", "verified"}) << '\n';
}
```

### C++20 output

```text
false
true
```

## قارن اللغتين

Both examples build an expression tree directly; neither parses text. Python uses a set as Context and matching `evaluate` methods. C++ declares an Expression Interface. Use a direct boolean expression when rules do not need to be represented as data.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه للغة صغيرة مستقرة، وشجرة التعبير مفيدة للبناء والفحص.

### Use cases

ينفع للغات فلترة أو أهلية صغيرة؛ مش نظام صلاحيات آمن ولا `Parser` عام.

**التكلفة:** كل شكل في القواعد محتاج كود. التداخل العميق ممكن يملأ الـ `Stack`؛ مفيش `Parser` هنا، `main` بتبني الشجرة مباشرة.

## جرّب تجاوب

1. المثال بيحلّل نص، ولا بيقيّم شجرة جاهزة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Either` للـ `OR` واختبر قاعدة متداخلة مع ثلاث `Contexts` مختلفة.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
