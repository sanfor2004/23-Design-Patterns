# الاستراتيجية

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/state/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/template-method/README.ar-EG.md)

## الفئة

السلوك

## المستوى

مبتدئ

## في جملة واحدة

مرّر خوارزمية قابلة للتبديل للـ Object اللي محتاجاها.

## المشكلة

إجمالي الشراء محتاج سياسات شحن مختلفة من غير حشر كل سياسة جوه Checkout.

## حل بسيط في الأول

```cpp
int fee = express ? (subtotal >= 100 ? 0 : 15) : 5;
```

## ليه الحل بيصعّب الدنيا

شرط واحد مقروء؛ تكرار فروع السياسات في كذا مسار بيصعّب إضافة القواعد واختبارها.

## الفكرة الأساسية

Checkout بتمتلك Callable اسمها ShippingRule وبتسألها عن الرسوم؛ المستدعي بيختار القاعدة وقت الإنشاء.

## مثال من الحياة

اختار تخطيط طريق للمشي أو السواقة، والوجهة واحدة.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الاستراتيجية](../../assets/diagrams/strategy.svg)

```text
Checkout::total()  -->  ShippingRule  -->  standard / express lambda
```

## الأدوار

Checkout السياق، ShippingRule عقد السلوك، والـ Lambdas بتنّفذ الشحن العادي والسريع.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <functional>
#include <iostream>
#include <stdexcept>
#include <utility>

using ShippingRule = std::function<int(int)>;
class Checkout {
    ShippingRule shipping_;
public:
    explicit Checkout(ShippingRule shipping) : shipping_(std::move(shipping)) {
        if (!shipping_) throw std::invalid_argument("Missing shipping rule");
    }
    int total(int subtotal) const {
        if (subtotal < 0) throw std::invalid_argument("Negative subtotal");
        return subtotal + shipping_(subtotal);
    }
};
int main() {
    const Checkout standard{[](int) { return 5; }};
    const Checkout express{[](int subtotal) { return subtotal >= 100 ? 0 : 15; }};
    std::cout << "Standard: " << standard.total(40) << '\n';
    std::cout << "Express: " << express.total(40) << '\n';
    std::cout << "Express large: " << express.total(120) << '\n';
}
```

## الناتج المتوقع

```text
Standard: 45
Express: 55
Express large: 120
```

## إمتى تستخدمه

استخدمه لما الخوارزميات بتتغير باستقلال والـ Client محتاج يختار سياسة.

## إمتى ما تستخدموش

بلاش لخوارزمية ثابتة واحدة أو شرط واضح مش محتاج توسعة فعلية.

## المميزات

كل سياسة تتختبر لوحدها، وحساب الإجمالي يفضل مشترك.

## العيوب والمقايضات

std::function فيها Type Erasure وممكن تخصص ذاكرة؛ Template أو Function Pointer ممكن يناسبوا قيود تانية. راجع الرسوم لو كود خارجي ممكن يرجع قيم غير صالحة.

## استخدامات تقنية

مناسب للتسعير والترتيب وسياسات إعادة المحاولة.

## أنماط مرتبطة

[state](../state/README.ar-EG.md) · [template-method](../template-method/README.ar-EG.md)

## لخبطة شائعة

State بتمثل دورة حياة وانتقالات، Strategy بتختار خوارزمية. Template Method بتغيّر خطوات موروثة بدل Callable محقونة.

## سؤال انترفيو

استبدال std::function بـ Template Parameter هيأثر إزاي على الاختيار وقت التشغيل والترجمة؟

## تحدي صغير

ضيف شحن مجاني من 80 واختبر 79 و80 و81.

## الخلاصة

- **المشكلة:** إجمالي الشراء محتاج سياسات شحن مختلفة من غير حشر كل سياسة جوه Checkout.
- **الحل:** Checkout بتمتلك Callable اسمها ShippingRule وبتسألها عن الرسوم؛ المستدعي بيختار القاعدة وقت الإنشاء.
- **المقايضة:** std::function فيها Type Erasure وممكن تخصص ذاكرة؛ Template أو Function Pointer ممكن يناسبوا قيود تانية. راجع الرسوم لو كود خارجي ممكن يرجع قيم غير صالحة.
- **افتكر:** نفس المهمة، اختار الخوارزمية.

[السابق](../../behavioral/state/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/template-method/README.ar-EG.md)
