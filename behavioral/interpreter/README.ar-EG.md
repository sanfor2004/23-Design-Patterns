# Interpreter

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/command/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/iterator/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

متقدم

## In One Sentence

مثّل لغة صغيرة بـ objects بتقيّم قواعدها.

## The Problem

قواعد السماح بتجمع أسماء Roles و AND ، ومحتاجين نبني القواعد كبيانات.

## Naive Solution

```cpp
bool allowed = roles.contains("editor") && roles.contains("verified");
```

## Why It Becomes a Problem

تعبير Boolean ثابت بسيط، بس تغيير شكل قواعد متداخلة بيحتاج تعديل كود التطبيق.

## The Idea

Role تعبير نهائي، و Both تعبير مركب بيقيّم طفلين بـ AND مع Short Circuit.

## Real-World Analogy

الجملة بتجمع كلمات بقواعد؛ هنا القاعدة بتجمع Roles باستخدام AND.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Interpreter](../../assets/diagrams/interpreter.svg)

```text
Context  -->  Both(Expression, Expression)  -->  Role / nested Both
```

## Participants

Expression بتحدد التقييم، Context بتوفر الأدوار، Role بتراجع العضوية، و Both بتمتلك التعبيرين.

الأدوار القياسية في المثال ده:

- [`Abstract Expression`](../../GLOSSARY.md#abstract-expression) — عقد تقييم العقد اللي بتمثل قواعد Interpreter. هنا: `Expression`.
- [`Terminal Expression`](../../GLOSSARY.md#terminal-expression) — تعبير مافيش جواه تعبيرات أطفال. هنا: `Role`.
- [`Nonterminal Expression`](../../GLOSSARY.md#nonterminal-expression) — تعبير بيركب تعبيرات أصغر حسب قاعدة في اللغة. هنا: `Both`.
- `Context` — البيانات اللي التعبيرات بتستخدمها وقت التقييم؛ هنا مجموعة أسماء الصلاحيات. `Context`.

## Modern C++20 Example

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

## Example Output

```text
false
true
```

## When to Use

استخدمه للغة صغيرة مستقرة، وشجرة التعبير مفيدة للبناء والفحص.

### Use cases

ينفع للغات فلترة أو أهلية صغيرة؛ مش نظام صلاحيات آمن ولا Parser عام.

## When NOT to Use

بلاش للغة كبيرة محتاجة Parser قوي ورسائل أخطاء وتحسين؛ أدوات Parsing جاهزة أنسب.

## Advantages

القواعد بتتركب بشكل Recursive وتتقيّم مع Contexts مختلفة.

## Trade-offs

كل شكل في القواعد محتاج كود. التداخل العميق ممكن يملأ الـ Stack ؛ مفيش Parser هنا، main بتبني الشجرة مباشرة.

## Related Patterns

[Composite](../../structural/composite/README.ar-EG.md) · [Visitor](../visitor/README.ar-EG.md)

## Common Confusion

Composite بتوصف الشجرة، وInterpreter بتضيف معنى القواعد وتقييمها. Visitor ممكن تضيف عمليات عليها.

## Terms to Remember

- `Interpreter` — مثّل لغة صغيرة بـ objects بتقيّم قواعدها.
- `Abstract Expression` — عقد تقييم العقد اللي بتمثل قواعد Interpreter. مثال: `Expression`.
- `Terminal Expression` — تعبير مافيش جواه تعبيرات أطفال. مثال: `Role`.
- `Nonterminal Expression` — تعبير بيركب تعبيرات أصغر حسب قاعدة في اللغة. مثال: `Both`.
- `Context` — البيانات اللي التعبيرات بتستخدمها وقت التقييم؛ هنا مجموعة أسماء الصلاحيات.

## Interview Vocabulary

- [`abstract syntax tree`](../../GLOSSARY.md#abstract-syntax-tree) — شجرة بتمثل تركيب القواعد بدل الشكل المكتوب للنص.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — بتبني تركيب من أجزاء بتوفر نفس عقد الكل.
- [`short-circuit evaluation`](../../GLOSSARY.md#short-circuit-evaluation) — بتتخطى باقي المعاملات لما نتيجة بدري تكون حسمت الإجابة.

## Interview Question

لو المستخدم كتب editor AND verified OR admin ، هتحدد أولوية العمليات فين؟

## Mini Challenge

ضيف Either للـ OR واختبر قاعدة متداخلة مع ثلاث Contexts مختلفة.

## Quick Summary

- **المشكلة:** قواعد السماح بتجمع أسماء Roles و AND ، ومحتاجين نبني القواعد كبيانات.
- **الحل:** Role تعبير نهائي، و Both تعبير مركب بيقيّم طفلين بـ AND مع Short Circuit.
- **Trade-off:** كل شكل في القواعد محتاج كود. التداخل العميق ممكن يملأ الـ Stack ؛ مفيش Parser هنا، main بتبني الشجرة مباشرة.
- **افتكر:** عقد القواعد بتدي معنى للتعبير.

[السابق](../../behavioral/command/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/iterator/README.ar-EG.md)
