# المحوّل

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)

## الفئة

التركيب

## المستوى

مبتدئ

## في جملة واحدة

حوّل واجهة موجودة للشكل اللي الـ Client مستنيه.

## المشكلة

لوحة العرض مستنية Celsius، بس الحساس الموجود بيرجع Fahrenheit.

## حل بسيط في الأول

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## ليه الحل بيصعّب الدنيا

تمرير الرقم زي ما هو بيعرض وحدة غلط. وتكرار معادلة التحويل في كذا مكان بيكرر قاعدة التوافق.

## الفكرة الأساسية

اعمل Temperature حوالين LegacyThermometer مستعارة، وحوّل الوحدات عند الحد الفاصل.

## مثال من الحياة

زي وصلة كهربا للسفر؛ هنا الوصلة بتحوّل معنى القيمة كمان.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المحوّل](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## الأدوار

Temperature هي الواجهة المطلوبة، وLegacyThermometer هي القديمة. CelsiusAdapter بتستعيرها، وdisplay بتعرف Temperature بس.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <stdexcept>

class LegacyThermometer {
public:
    double fahrenheit() const { return 77.0; }
};
struct Temperature {
    virtual ~Temperature() = default;
    virtual double celsius() const = 0;
};
class CelsiusAdapter final : public Temperature {
    const LegacyThermometer& sensor_;
public:
    explicit CelsiusAdapter(const LegacyThermometer& sensor) : sensor_(sensor) {}
    double celsius() const override { return (sensor_.fahrenheit() - 32.0) * 5.0 / 9.0; }
};
void display(const Temperature& temperature) {
    std::cout << temperature.celsius() << " C\n";
}
int main() {
    const LegacyThermometer sensor;
    const CelsiusAdapter adapter{sensor};
    display(adapter);
}
```

## الناتج المتوقع

```text
25 C
```

## إمتى تستخدمه

استخدمه عند التعامل مع API موجودة مش قادر أو مش مناسب تغيّرها.

## إمتى ما تستخدموش

بلاش لو أنت مالك الطرفين وتوحيد الواجهة أبسط.

## المميزات

التحويل في مكان واحد، والعرض يقبل أي تنفيذ لـ Temperature.

## العيوب والمقايضات

تغيير أسماء الدوال بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ Adapter لأن الـ Reference مش مالكة.

## استخدامات تقنية

مناسب لربط APIs قديمة وتحويل وحدات؛ الدقة والتعامل مع الأخطاء محتاجين اتفاق واضح.

## أنماط مرتبطة

[facade](../facade/README.ar-EG.md) · [bridge](../bridge/README.ar-EG.md)

## لخبطة شائعة

Facade بتبسّط Subsystem. Adapter بتخلّي واجهة بعينها متوافقة مع عقد مطلوب.

## سؤال انترفيو

هل ينفع دايماً تحافظ على السلوك لو المصدر Async والواجهة المطلوبة Sync؟

## تحدي صغير

خلّي Fahrenheit قابلة للتغيير، واختبر نقطتي التجمد والغليان.

## الخلاصة

- **المشكلة:** لوحة العرض مستنية Celsius، بس الحساس الموجود بيرجع Fahrenheit.
- **الحل:** اعمل Temperature حوالين LegacyThermometer مستعارة، وحوّل الوحدات عند الحد الفاصل.
- **المقايضة:** تغيير أسماء الدوال بس ممكن يخبي اختلاف المعنى. الحساس لازم يعيش أطول من الـ Adapter لأن الـ Reference مش مالكة.
- **افتكر:** حوّل عند نقطة الاتصال.

[السابق](../../creational/singleton/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/bridge/README.ar-EG.md)
