# الوسيط

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

انقل التنسيق بين Objects زميلة لـ Object مخصصة.

## المشكلة

حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.

## حل بسيط في الأول

```cpp
// Each field directly updates the button and reads its sibling.
submit.enable(!username.empty() && !password.empty());
```

## ليه الحل بيصعّب الدنيا

لو كل Field تعرف التانية والزر، قواعد الواجهة هتتوزع والاعتماديات هتتشابك.

## الفكرة الأساسية

الحقول تبلغ LoginForm بـ changed، وهي تراجع القيم وتحدّث الزر.

## مثال من الحياة

منسق الطيران بينظم التعامل بدل ما كل طيار يتفاوض مع كل طيار تاني.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الوسيط](../../assets/diagrams/mediator.svg)

```text
Field::set()  -->  LoginForm(Mediator)  -->  Button::enable()
```

## الأدوار

Mediator بتحدد الإشعار، Field بتبلّغ، Button بتخزن الحالة، وLoginForm بتمتلك الزملاء وتنسقهم.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
Ready: false
Ready: true
```

## إمتى تستخدمه

استخدمه لما قواعد التعامل بين كذا زميل تبدأ تتشابك.

## إمتى ما تستخدموش

بلاش لـ Callback واحدة بسيطة أو مكونات مفيش بينها تنسيق حقيقي.

## المميزات

الحقول مش بتعرف بعضها ولا الزر، والقاعدة في مكان واحد.

## العيوب والمقايضات

الوسيط ممكن يكبر زيادة. LoginForm ممنوع نسخها عشان الحقول شايلة References ليها؛ النسخ هيخلّي الروابط غلط.

## استخدامات تقنية

مناسب لتنسيق Dialogs والـ Workflows؛ تشغيل الزر مش Authentication ولا مراجعة باسورد.

## أنماط مرتبطة

[observer](../observer/README.ar-EG.md) · [facade](../../structural/facade/README.ar-EG.md)

## لخبطة شائعة

Observer بتذيع تغيير للمشتركين. Mediator بتحدد استجابة زملاء بعينهم لبعض، وممكن تستخدم Observer للإشعارات.

## سؤال انترفيو

ليه Copy Constructor تلقائية خطر في LoginForm؟

## تحدي صغير

ضيف Checkbox للشروط واطلب الشروط الثلاثة من غير ما Field تعرف الزر.

## الخلاصة

- **المشكلة:** حقلي الاسم والباسورد مع بعض بيحددوا هل زر الدخول شغال.
- **الحل:** الحقول تبلغ LoginForm بـ changed، وهي تراجع القيم وتحدّث الزر.
- **المقايضة:** الوسيط ممكن يكبر زيادة. LoginForm ممنوع نسخها عشان الحقول شايلة References ليها؛ النسخ هيخلّي الروابط غلط.
- **افتكر:** الزملاء يتكلموا عن طريق منسق.

[السابق](../../behavioral/iterator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/memento/README.ar-EG.md)
