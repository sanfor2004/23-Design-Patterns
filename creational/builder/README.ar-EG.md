# البنّاء

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/abstract-factory/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/factory-method/README.ar-EG.md)

## الفئة

الإنشاء

## المستوى

مبتدئ

## في جملة واحدة

جهّز Object بخطوات اسمها واضح، وبعدين طلّع النتيجة.

## المشكلة

الـ Request فيها Endpoint وTimeout واختيار Retry؛ كل ما الخيارات تزيد، ترتيب الـ Arguments بيبقى أصعب.

## حل بسيط في الأول

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## ليه الحل بيصعّب الدنيا

الـ Constructor شغال، بس شوية أرقام وBooleans جنب بعض مش بيوضحوا المقصود، والغلط في ترتيبهم سهل يفوت.

## الفكرة الأساسية

خزّن الاختيارات مؤقتاً في RequestBuilder. الدوال اسمها يوضح الاختيار، وbuild تراجع القيم وترجع Request بالقيمة.

## مثال من الحياة

زي طلب ساندوتش: بتحدد الإضافات قبل ما المطبخ يجهزه.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![البنّاء](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## الأدوار

RequestBuilder بتجمع الاختيارات وتراجعها. Request بتمتلك القيم النهائية، والـ Client بيختار ترتيب الخطوات الاختيارية.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Request {
    std::string endpoint_;
    int timeout_;
    bool retry_;
public:
    Request(std::string endpoint, int timeout, bool retry)
        : endpoint_(std::move(endpoint)), timeout_(timeout), retry_(retry) {}
    void describe() const {
        std::cout << endpoint_ << " timeout=" << timeout_ << " retry=" << retry_ << '\n';
    }
};
class RequestBuilder {
    std::string endpoint_;
    int timeout_ = 30;
    bool retry_ = false;
public:
    RequestBuilder& endpoint(std::string value) { endpoint_ = std::move(value); return *this; }
    RequestBuilder& timeout(int seconds) { timeout_ = seconds; return *this; }
    RequestBuilder& retry(bool enabled) { retry_ = enabled; return *this; }
    Request build() const {
        if (endpoint_.empty() || timeout_ <= 0) throw std::invalid_argument("Invalid request");
        return Request{endpoint_, timeout_, retry_};
    }
};
int main() {
    const auto request = RequestBuilder{}.endpoint("/orders").timeout(5).retry(true).build();
    request.describe();
    try { static_cast<void>(RequestBuilder{}.build()); }
    catch (const std::invalid_argument&) { std::cout << "Invalid request rejected\n"; }
}
```

## الناتج المتوقع

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## إمتى تستخدمه

استخدمه لما الخيارات المستقلة كتير، أو محتاج نقطة واضحة لمراجعة الإنشاء.

## إمتى ما تستخدموش

بلاش مع معاملين واضحين؛ Struct صغيرة ممكن تكون أبسط.

## المميزات

مكان الاستدعاء بيوضح النية، وبتقدر ترفض إعداد ناقص قبل إخراج النتيجة.

## العيوب والمقايضات

فيه نوع زيادة هتصونه. Constructor بتاعة Request هنا عامة؛ في الإنتاج لازم تراجع القيم فيها كمان أو تمنع الوصول المباشر ليها.

## استخدامات تقنية

مناسب لإعداد HTTP Requests وتجهيز بيانات الاختبار؛ المثال مش بيعمل اتصال بالشبكة.

## أنماط مرتبطة

[factory-method](../factory-method/README.ar-EG.md) · [abstract-factory](../abstract-factory/README.ar-EG.md)

## لخبطة شائعة

Factory Method بتختار نوع المنتج جوه Workflow موروث. Builder بتجمع إعداد النتيجة على كذا خطوة.

## سؤال انترفيو

هل أي Fluent Interface تعتبر Builder؟ وضّح فين الإنشاء بينتهي.

## تحدي صغير

ارفض Timeout أكبر من 120، وجرّب آخر قيمة مقبولة وأول قيمة مرفوضة.

## الخلاصة

- **المشكلة:** الـ Request فيها Endpoint وTimeout واختيار Retry؛ كل ما الخيارات تزيد، ترتيب الـ Arguments بيبقى أصعب.
- **الحل:** خزّن الاختيارات مؤقتاً في RequestBuilder. الدوال اسمها يوضح الاختيار، وbuild تراجع القيم وترجع Request بالقيمة.
- **المقايضة:** فيه نوع زيادة هتصونه. Constructor بتاعة Request هنا عامة؛ في الإنتاج لازم تراجع القيم فيها كمان أو تمنع الوصول المباشر ليها.
- **افتكر:** اختار الخطوات، وبعدها ابنِ.

[السابق](../../creational/abstract-factory/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/factory-method/README.ar-EG.md)
