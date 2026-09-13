# Mediator

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** خلّي التنسيق بين الأطراف المتعاونة (`Colleagues`) مسؤولية منسّق مستقل (`Mediator`).

## المشكلة

حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال. لو كل `Field` تعرف التانية والزر، قواعد الـ [`interface`](../../GLOSSARY.md#interface) هتتوزع والـ `dependencies` هتتشابك.

## الحل ببساطة

زر الدخول محتاج الحقلين يبقوا مكتوب فيهم.الـ`Mediator` بيطبّق القاعدة، فكل حقل مش محتاج يعرف الحقل التاني أو الزر. خلّي الحقول تبلغ المنسّق `LoginForm` بالتغيير عن طريق `changed`. المنسّق يراجع القيم ويحدد هل الزر يبقى متاح.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Mediator](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

في المثال، العقد `Mediator` بيحدد طريقة الإشعار. الحقل `Field` بيبلّغ عن التغيير، والزر `Button` بيخزن حالته (`state`). المنسّق `LoginForm` بيمتلك المكونات دي ويطبّق قواعد التعامل بينها.

الأدوار القياسية في المثال ده:

- [`Colleague`](../../GLOSSARY.md#colleague) — كائن متعاون (`object`) بيتولى الـ `Mediator` تنسيق تعاملاته مع باقي الأطراف. هنا: `Field, Button`.
- [`Concrete Mediator`](../../GLOSSARY.md#concrete-mediator) — تنفيذ (`implementation`) بيجمع قواعد التنسيق بين الأطراف المتعاونة (`Colleagues`). هنا: `LoginForm`.
- [`callback`](../../GLOSSARY.md#callback) — دالة (`function`) أو عملية بتمرّرها لجزء تاني، عشان يناديها وقت ما يحتاجها. هنا: `Mediator::changed`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Field:
    def __init__(self, changed):
        self.changed = changed
        self.value = ""

    def set(self, value):
        self.value = value
        self.changed()


class Button:
    def __init__(self):
        self.enabled = False


class LoginForm:
    def __init__(self):
        self.username = Field(self.changed)
        self.password = Field(self.changed)
        self.submit = Button()

    def changed(self):
        self.submit.enabled = bool(self.username.value and self.password.value)


if __name__ == "__main__":
    form = LoginForm()
    form.username.set("learner")
    print("Ready:", form.submit.enabled)
    form.password.set("example")
    print("Ready:", form.submit.enabled)
    form.password.set("")
    print("Ready:", form.submit.enabled)
```

### Python output

```text
Ready: False
Ready: True
Ready: False
```

## C++20 example

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

### C++20 output

```text
Ready: false
Ready: true
Ready after clearing: false
```

## قارن اللغتين

Python Fields call a bound method on their Mediator. C++ Fields borrow a Mediator reference, and LoginForm disables copying to protect those links. Python can collect reference cycles, but copying this form still needs care: a shallow copy would share Fields and callbacks.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما قواعد التعامل بين كذا زميل تبدأ تتشابك.

### Use cases

مناسب لتنسيق `Dialogs` والـ `Workflows`؛ تشغيل الزر مش `Authentication` ولا مراجعة باسورد.

**التكلفة:** الـ `Mediator` ممكن يكبر زيادة. الـ `LoginForm` ممنوع نسخها عشان الحقول شايلة `references` ليها؛ النسخ هيخلّي الروابط غلط.

## جرّب تجاوب

1. مين بيقرر حالة الزر لما حقل يبقى فاضي؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف `Checkbox` للشروط واطلب الشروط الثلاثة من غير ما `Field` تعرف الزر.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
