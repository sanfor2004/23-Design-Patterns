# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

متوسط

## In One Sentence

خلّي التنسيق بين الأطراف المتعاونة (`Colleagues`) مسؤولية منسّق مستقل (`Mediator`).

## ببساطة

زر الدخول محتاج الحقلين يبقوا مكتوب فيهم.الـ`Mediator` بيطبّق القاعدة، فكل حقل مش محتاج يعرف الحقل التاني أو الزر.

## The Problem

حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.

## Naive Solution

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## Why It Becomes a Problem

لو كل `Field` تعرف التانية والزر، قواعد الـ [`interface`](../../GLOSSARY.md#interface) هتتوزع والـ `dependencies` هتتشابك.

## The Idea

خلّي الحقول تبلغ المنسّق `LoginForm` بالتغيير عن طريق `changed`. المنسّق يراجع القيم ويحدد هل الزر يبقى متاح.

## Real-World Analogy

منسق الطيران بينظم التعامل بدل ما كل طيار يتفاوض مع كل طيار تاني.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## Participants

في المثال، العقد `Mediator` بيحدد طريقة الإشعار. الحقل `Field` بيبلّغ عن التغيير، والزر `Button` بيخزن حالته (`state`). المنسّق `LoginForm` بيمتلك المكونات دي ويطبّق قواعد التعامل بينها.

الأدوار القياسية في المثال ده:

- [`Colleague`](../../GLOSSARY.md#colleague) — كائن متعاون (`object`) بيتولى الـ `Mediator` تنسيق تعاملاته مع باقي الأطراف. هنا: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — تنفيذ (`implementation`) بيجمع قواعد التنسيق بين الأطراف المتعاونة (`Colleagues`). هنا: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — دالة (`function`) أو عملية بتمرّرها لجزء تاني، عشان يناديها وقت ما يحتاجها. هنا: `Mediator::changed`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

```cpp
#include <iostream>
#include <string>
#include <string_view>
#include <utility>

struct Mediator {
    virtual ~Mediator() = default;
    virtual void changed() = 0;
};
class Field {
    Mediator& mediator_;
    std::string value_;
public:
    explicit Field(Mediator& mediator) : mediator_(mediator) {}
    void set(std::string value) { value_ = std::move(value); mediator_.changed(); }
    bool empty() const { return value_.empty(); }
};
class Button {
    bool enabled_ = false;
public:
    void enable(bool enabled) { enabled_ = enabled; }
    bool enabled() const { return enabled_; }
};
class LoginForm final : public Mediator {
    Field username_;
    Field password_;
    Button submit_;
public:
    LoginForm() : username_(*this), password_(*this) {}
    LoginForm(const LoginForm&) = delete;
    LoginForm& operator=(const LoginForm&) = delete;
    void changed() override { submit_.enable(!username_.empty() && !password_.empty()); }
    void username(std::string value) { username_.set(std::move(value)); }
    void password(std::string value) { password_.set(std::move(value)); }
    bool ready() const { return submit_.enabled(); }
};
int main() {
    LoginForm form;
    form.username("learner");
    std::cout << "Ready: " << std::boolalpha << form.ready() << '\n';
    form.password("example");
    std::cout << "Ready: " << form.ready() << '\n';
    form.password("");
    std::cout << "Ready after clearing: " << form.ready() << '\n';
}
```

## Example Output

```text
Ready: false
Ready: true
Ready after clearing: false
```

## When to Use

استخدمه لما قواعد التعامل بين كذا زميل تبدأ تتشابك.

### Use cases

مناسب لتنسيق `Dialogs` والـ `Workflows`؛ تشغيل الزر مش `Authentication` ولا مراجعة باسورد.

## When NOT to Use

بلاش لـ `callback` واحدة بسيطة أو مكونات مفيش بينها تنسيق حقيقي.

## Advantages

الحقول مش بتعرف بعضها ولا الزر، والقاعدة في مكان واحد.

## Trade-offs

الـ `Mediator` ممكن يكبر زيادة. الـ `LoginForm` ممنوع نسخها عشان الحقول شايلة `references` ليها؛ النسخ هيخلّي الروابط غلط.

## Related Patterns

[Observer](../observer/README.ar-EG.md) · [Facade](../../structural/facade/README.ar-EG.md)

## Common Confusion

الـ `Observer` بتذيع تغيير للمشتركين. الـ `Mediator` بتحدد استجابة زملاء بعينهم لبعض، وممكن تستخدم `Observer` للإشعارات.

## Terms to Remember

- `Mediator` — خلّي التنسيق بين الأطراف المتعاونة (`Colleagues`) مسؤولية منسّق مستقل (`Mediator`).
- `Colleague` — كائن متعاون (`object`) بيتولى الـ `Mediator` تنسيق تعاملاته مع باقي الأطراف. مثال: `Field, Button`.
- `Concrete Mediator` — تنفيذ (`implementation`) بيجمع قواعد التنسيق بين الأطراف المتعاونة (`Colleagues`). مثال: `LoginForm`.
- `callback` — دالة (`function`) أو عملية بتمرّرها لجزء تاني، عشان يناديها وقت ما يحتاجها. مثال: `Mediator::changed`.

## Interview Vocabulary

- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.
- [`god object`](../../GLOSSARY.md#god-object) — كائن (`object`) بيجمع مسؤوليات كتير مالهاش علاقة قوية ببعض.

## Interview Question

ليه `copy constructor` تلقائية خطر في `LoginForm`؟

## Mini Challenge

ضيف `Checkbox` للشروط واطلب الشروط الثلاثة من غير ما `Field` تعرف الزر.

## اختبر فهمك

1. مين بيقرر حالة الزر لما حقل يبقى فاضي؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.
- **الحل:** خلّي الحقول تبلغ المنسّق `LoginForm` بالتغيير عن طريق `changed`. المنسّق يراجع القيم ويحدد هل الزر يبقى متاح.
- **`Trade-off`:** الـ `Mediator` ممكن يكبر زيادة. الـ `LoginForm` ممنوع نسخها عشان الحقول شايلة `references` ليها؛ النسخ هيخلّي الروابط غلط.
- **افتكر:** الزملاء يتكلموا عن طريق منسق.

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)
