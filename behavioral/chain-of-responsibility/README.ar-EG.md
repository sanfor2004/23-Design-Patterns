# سلسلة المسؤولية

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/proxy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/command/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

مرّر الطلب على Handlers تقدر توقفه أو تكمّل.

## المشكلة

الطلب لازم يعدّي فحص الهوية وحد الإنفاق، وكل مدخل ممكن يحتاج سياسة مختلفة.

## حل بسيط في الأول

```cpp
bool accept(Request r) {
    return r.authenticated && r.amount > 0 && r.amount <= 100;
}
```

## ليه الحل بيصعّب الدنيا

شرط واحد كويس في الأول؛ نسخه وتعديله لكذا مسار بيصعّب إعادة الاستخدام وترتيب السياسات.

## الفكرة الأساسية

كل Handler تعمل فحصها وتكمّل بس لو نجح؛ آخر فحص ناجح يقبل الطلب.

## مثال من الحياة

الدعم الفني يحل الطلب أو يبعته للمختص اللي بعده.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![سلسلة المسؤولية](../../assets/diagrams/chain-of-responsibility.svg)

```text
Request  -->  Auth  -->  Limit
```

## الأدوار

Handler بتمتلك اللي بعدها. Auth بتراجع الهوية، Limit بتراجع المبلغ، والـ Client بيختار الترتيب.

## C++20 — مثال كامل قابل للتشغيل

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

## الناتج المتوقع

```text
Rejected
Rejected
Accepted
```

## إمتى تستخدمه

استخدمه لما ترتيب الفحوصات أو اختيارها محتاج تركيب مستقل.

## إمتى ما تستخدموش

بلاش لو فحصين ثابتين في مكان واحد؛ الشرط الأول أبسط.

## المميزات

تقدر تعيد استخدام الفحوصات وترتبها من غير Conditional ضخمة.

## العيوب والمقايضات

الترتيب بيأثر، ولازم سياسة واضحة لنهاية السلسلة. هنا بنقبل بعد نجاح الكل؛ سلاسل تانية ممكن ترفض الطلب غير المعالج.

## استخدامات تقنية

مناسب للـ Validation والـ Middleware. النسخة دي بتطلب موافقة الكل، مش أول Handler ناجحة بس.

## أنماط مرتبطة

[decorator](../../structural/decorator/README.ar-EG.md) · [command](../command/README.ar-EG.md)

## لخبطة شائعة

Decorator بتضيف طبقات سلوك؛ السلسلة دي ممكن توقف قبل باقي الخطوات. Command بتمثل الطلب كـ Object.

## سؤال انترفيو

لو Limit مكلفة وجت الأول، إيه اللي هيحصل لطلب غير مسجل؟

## تحدي صغير

ضيف فحص وضع الصيانة، واتأكد إن المرفوض ما يوصلش للفحوصات اللي بعده.

## الخلاصة

- **المشكلة:** الطلب لازم يعدّي فحص الهوية وحد الإنفاق، وكل مدخل ممكن يحتاج سياسة مختلفة.
- **الحل:** كل Handler تعمل فحصها وتكمّل بس لو نجح؛ آخر فحص ناجح يقبل الطلب.
- **المقايضة:** الترتيب بيأثر، ولازم سياسة واضحة لنهاية السلسلة. هنا بنقبل بعد نجاح الكل؛ سلاسل تانية ممكن ترفض الطلب غير المعالج.
- **افتكر:** عالجه، أو مرّره.

[السابق](../../structural/proxy/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/command/README.ar-EG.md)
