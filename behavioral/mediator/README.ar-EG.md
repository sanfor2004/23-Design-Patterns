# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

متوسط

## In One Sentence

انقل التنسيق بين objects زميلة لـ object مخصصة.

## The Problem

حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.

## Naive Solution

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## Why It Becomes a Problem

لو كل Field تعرف التانية والزر، قواعد الـ [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها) هتتوزع والـ dependencies هتتشابك.

## The Idea

الحقول تبلغ LoginForm بـ changed ، وهي تراجع القيم وتحدّث الزر.

## Real-World Analogy

منسق الطيران بينظم التعامل بدل ما كل طيار يتفاوض مع كل طيار تاني.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## Participants

Mediator بتحدد الإشعار، Field بتبلّغ، Button بتخزن الـ state ، و LoginForm بتمتلك الزملاء وتنسقهم.

الأدوار القياسية في المثال ده:

- [`Colleague`](../../GLOSSARY.md#colleague) — object بيتم تنسيق تعاملاتها عن طريق Mediator. هنا: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — implementation فيها قواعد التنسيق بين Colleagues. هنا: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — function أو عملية بتمرّرها عشان جزء تاني يناديها وقت ما يحتاجها. هنا: `Mediator::changed`.

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
}
```

## Example Output

```text
Ready: false
Ready: true
```

## When to Use

استخدمه لما قواعد التعامل بين كذا زميل تبدأ تتشابك.

### Use cases

مناسب لتنسيق Dialogs والـ Workflows ؛ تشغيل الزر مش Authentication ولا مراجعة باسورد.

## When NOT to Use

بلاش لـ callback واحدة بسيطة أو مكونات مفيش بينها تنسيق حقيقي.

## Advantages

الحقول مش بتعرف بعضها ولا الزر، والقاعدة في مكان واحد.

## Trade-offs

الـ Mediator ممكن يكبر زيادة. LoginForm ممنوع نسخها عشان الحقول شايلة references ليها؛ النسخ هيخلّي الروابط غلط.

## Related Patterns

[Observer](../observer/README.ar-EG.md) · [Facade](../../structural/facade/README.ar-EG.md)

## Common Confusion

Observer بتذيع تغيير للمشتركين. Mediator بتحدد استجابة زملاء بعينهم لبعض، وممكن تستخدم Observer للإشعارات.

## Terms to Remember

- `Mediator` — انقل التنسيق بين objects زميلة لـ object مخصصة.
- `Colleague` — object بيتم تنسيق تعاملاتها عن طريق Mediator. مثال: `Field, Button`.
- `Concrete Mediator` — implementation فيها قواعد التنسيق بين Colleagues. مثال: `LoginForm`.
- `callback` — function أو عملية بتمرّرها عشان جزء تاني يناديها وقت ما يحتاجها. مثال: `Mediator::changed`.

## Interview Vocabulary

- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.
- [`god object`](../../GLOSSARY.md#god-object) — object بتلم مسؤوليات كتير مالهاش علاقة قوية ببعض.

## Interview Question

ليه copy constructor تلقائية خطر في LoginForm ؟

## Mini Challenge

ضيف Checkbox للشروط واطلب الشروط الثلاثة من غير ما Field تعرف الزر.

## Quick Summary

- **المشكلة:** حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.
- **الحل:** الحقول تبلغ LoginForm بـ changed ، وهي تراجع القيم وتحدّث الزر.
- **Trade-off:** الـ Mediator ممكن يكبر زيادة. LoginForm ممنوع نسخها عشان الحقول شايلة references ليها؛ النسخ هيخلّي الروابط غلط.
- **افتكر:** الزملاء يتكلموا عن طريق منسق.

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)
