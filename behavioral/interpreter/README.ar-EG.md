# المفسّر

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/command/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/iterator/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متقدم

## في جملة واحدة

مثّل لغة صغيرة بـ Objects بتقيّم قواعدها.

## المشكلة

قواعد السماح بتجمع أسماء Roles وAND، ومحتاجين نبني القواعد كبيانات.

## حل بسيط في الأول

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## ليه الحل بيصعّب الدنيا

تعبير Boolean ثابت بسيط، بس تغيير شكل قواعد متداخلة بيحتاج تعديل كود التطبيق.

## الفكرة الأساسية

Role تعبير نهائي، وBoth تعبير مركب بيقيّم طفلين بـ AND مع Short Circuit.

## مثال من الحياة

الجملة بتجمع كلمات بقواعد؛ هنا القاعدة بتجمع Roles باستخدام AND.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المفسّر](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## الأدوار

Expression بتحدد التقييم، Context بتوفر الأدوار، Role بتراجع العضوية، وBoth بتمتلك التعبيرين.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
false
true
```

## إمتى تستخدمه

استخدمه للغة صغيرة مستقرة، وشجرة التعبير مفيدة للبناء والفحص.

## إمتى ما تستخدموش

بلاش للغة كبيرة محتاجة Parser قوي ورسائل أخطاء وتحسين؛ أدوات Parsing جاهزة أنسب.

## المميزات

القواعد بتتركب بشكل Recursive وتتقيّم مع Contexts مختلفة.

## العيوب والمقايضات

كل شكل في القواعد محتاج كود. التداخل العميق ممكن يملأ الـ Stack؛ مفيش Parser هنا، main بتبني الشجرة مباشرة.

## استخدامات تقنية

ينفع للغات فلترة أو أهلية صغيرة؛ مش نظام صلاحيات آمن ولا Parser عام.

## أنماط مرتبطة

[composite](../../structural/composite/README.ar-EG.md) · [visitor](../visitor/README.ar-EG.md)

## لخبطة شائعة

Composite بتوصف الشجرة، وInterpreter بتضيف معنى القواعد وتقييمها. Visitor ممكن تضيف عمليات عليها.

## سؤال انترفيو

لو المستخدم كتب editor AND verified OR admin، هتحدد أولوية العمليات فين؟

## تحدي صغير

ضيف Either للـ OR واختبر قاعدة متداخلة مع ثلاث Contexts مختلفة.

## الخلاصة

- **المشكلة:** قواعد السماح بتجمع أسماء Roles وAND، ومحتاجين نبني القواعد كبيانات.
- **الحل:** Role تعبير نهائي، وBoth تعبير مركب بيقيّم طفلين بـ AND مع Short Circuit.
- **المقايضة:** كل شكل في القواعد محتاج كود. التداخل العميق ممكن يملأ الـ Stack؛ مفيش Parser هنا، main بتبني الشجرة مباشرة.
- **افتكر:** عقد القواعد بتدي معنى للتعبير.

[السابق](../../behavioral/command/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/iterator/README.ar-EG.md)
