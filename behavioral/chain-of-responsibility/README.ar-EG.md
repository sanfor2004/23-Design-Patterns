# Chain of Responsibility

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/proxy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/command/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على السلوك (`behavior`) والتعاون بين الكائنات (`objects`)، وده واحد من أغراض الـ `Design Patterns`.

## Difficulty

متوسط

## In One Sentence

مرّر الطلب على سلسلة معالجات (`Handlers`)؛ كل واحدة تقدر توقفه أو تمرّره للي بعدها.

## The Problem

الطلب لازم يعدّي فحص الهوية وحد الإنفاق، وكل مدخل ممكن يحتاج سياسة مختلفة.

## Naive Solution

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## Why It Becomes a Problem

شرط واحد كويس في الأول؛ نسخه وتعديله لكذا مسار بيصعّب إعادة الاستخدام وترتيب السياسات.

## The Idea

خلّي كل معالج (`Handler`) يعمل فحصه، ويمرّر الطلب للي بعده بس لو الفحص نجح. في المثال ده، الطلب بيتقبل بعد نجاح كل الفحوصات.

## Real-World Analogy

الدعم الفني يحل الطلب أو يبعته للمختص اللي بعده.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Chain of Responsibility](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## Participants

في المثال، كل `Handler` بتمتلك اللي بعدها. فحص الهوية موجود في `Auth`، وفحص المبلغ في `Limit`. المستدعي (`Client`) بيختار ترتيب السلسلة.

الأدوار القياسية في المثال ده:

- [`Handler`](../../GLOSSARY.md#handler) — دور بيعمل معالجة للطلب أو يبعته للي بعده. هنا: `Handler`.
- [`Concrete Handler`](../../GLOSSARY.md#concrete-handler) — معالج (`Handler`) بينفّذ قاعدة معينة. هنا: `Auth, Limit`.
- [`chain termination`](../../GLOSSARY.md#chain-termination) — القاعدة اللي بتحدد السلسلة تقف إمتى وإيه يحصل بعد آخر `Handler`. هنا: `Handler::handle`.

## Modern C++20 Example

```cpp
#include <initializer_list>
#include <iostream>
#include <memory>
#include <utility>

struct Request { bool authenticated; int amount; };
class Handler {
    std::unique_ptr<Handler> next_;
protected:
    virtual bool accepts(const Request& request) const = 0;
public:
    explicit Handler(std::unique_ptr<Handler> next = {}) : next_(std::move(next)) {}
    virtual ~Handler() = default;
    bool handle(const Request& request) const {
        if (!accepts(request)) return false;
        return next_ ? next_->handle(request) : true;
    }
};
class Auth final : public Handler {
    bool accepts(const Request& request) const override { return request.authenticated; }
public:
    using Handler::Handler;
};
class Limit final : public Handler {
    bool accepts(const Request& request) const override { return request.amount > 0 && request.amount <= 100; }
public:
    using Handler::Handler;
};
int main() {
    const Auth chain{std::make_unique<Limit>()};
    for (const auto& request : {Request{false, 20}, Request{true, 200}, Request{true, 20}})
        std::cout << (chain.handle(request) ? "Accepted" : "Rejected") << '\n';
}
```

## Example Output

```text
Rejected
Rejected
Accepted
```

## When to Use

استخدمه لما ترتيب الفحوصات أو اختيارها محتاج تركيب مستقل.

### Use cases

مناسب للـ `Validation` والـ `Middleware`. النسخة دي بتطلب موافقة الكل، مش أول `Handler` ناجحة بس.

## When NOT to Use

بلاش لو فحصين ثابتين في مكان واحد؛ الشرط الأول أبسط.

## Advantages

تقدر تعيد استخدام الفحوصات وترتبها من غير `Conditional` ضخمة.

## Trade-offs

الترتيب بيأثر، ولازم سياسة واضحة لنهاية السلسلة. هنا بنقبل بعد نجاح الكل؛ سلاسل تانية ممكن ترفض الطلب غير المعالج.

## Related Patterns

[Decorator](../../structural/decorator/README.ar-EG.md) · [Command](../command/README.ar-EG.md)

## Common Confusion

الـ `Decorator` بتضيف طبقات `behavior`؛ السلسلة دي ممكن توقف قبل باقي الخطوات. الـ `Command` بتمثل الطلب كـ `object`.

## Terms to Remember

- `Chain of Responsibility` — مرّر الطلب على سلسلة معالجات (`Handlers`)؛ كل واحدة تقدر توقفه أو تمرّره للي بعدها.
- `Handler` — دور بيعمل معالجة للطلب أو يبعته للي بعده. مثال: `Handler`.
- `Concrete Handler` — معالج (`Handler`) بينفّذ قاعدة معينة. مثال: `Auth, Limit`.
- `chain termination` — القاعدة اللي بتحدد السلسلة تقف إمتى وإيه يحصل بعد آخر `Handler`. مثال: `Handler::handle`.

## Interview Vocabulary

- [`delegation`](../../GLOSSARY.md#delegation) — الكائن بيفوّض جزء من شغله لكائن متعاون معاه (`object`)، بدل ما ينفّذ كل حاجة بنفسه.
- [`object composition`](../../GLOSSARY.md#object-composition) — بتوصل الكائنات (`objects`) ببعض عشان تبني سلوك متكامل (`behavior`) أو تركيب أكبر.
- [`loose coupling`](../../GLOSSARY.md#loose-coupling) — كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.

## Interview Question

لو `Limit` مكلفة وجت الأول، إيه اللي هيحصل لطلب غير مسجل؟

## Mini Challenge

ضيف فحص وضع الصيانة، واتأكد إن المرفوض ما يوصلش للفحوصات اللي بعده.

## Quick Summary

- **المشكلة:** الطلب لازم يعدّي فحص الهوية وحد الإنفاق، وكل مدخل ممكن يحتاج سياسة مختلفة.
- **الحل:** خلّي كل معالج (`Handler`) يعمل فحصه، ويمرّر الطلب للي بعده بس لو الفحص نجح. في المثال ده، الطلب بيتقبل بعد نجاح كل الفحوصات.
- **`Trade-off`:** الترتيب بيأثر، ولازم سياسة واضحة لنهاية السلسلة. هنا بنقبل بعد نجاح الكل؛ سلاسل تانية ممكن ترفض الطلب غير المعالج.
- **افتكر:** عالجه، أو مرّره.

[السابق](../../structural/proxy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/command/README.ar-EG.md)
