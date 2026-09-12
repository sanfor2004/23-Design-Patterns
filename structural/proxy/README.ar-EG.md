# الوكيل

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/flyweight/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/chain-of-responsibility/README.ar-EG.md)

## الفئة

التركيب

## المستوى

متوسط

## في جملة واحدة

تحكّم في الوصول لـ Object عن طريق بديل بنفس الواجهة.

## المشكلة

معرض الصور ممكن يجهّز صور كتير بس يعرض كام واحدة.

## حل بسيط في الأول

```cpp
DiskImage image; // loads even if never displayed
```

## ليه الحل بيصعّب الدنيا

إنشاء الصور التقيلة فوراً بيحمّل حاجات قبل ما حد يطلب عرضها.

## الفكرة الأساسية

LazyImage بتنفذ Image، وبتعمل DiskImage عند أول display وبعد كده تعيد استخدامها.

## مثال من الحياة

إيصال طلب كتاب بيمثل الكتاب المخزّن لحد ما أمين المكتبة يجيبه.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الوكيل](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## الأدوار

Image الواجهة المشتركة، DiskImage الشغل الفعلي، وLazyImage بتمتلك الصورة اللي بتتعمل عند الطلب.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() const = 0;
};
struct DiskImage final : Image {
    DiskImage() { std::cout << "Load image\n"; }
    void display() const override { std::cout << "Display image\n"; }
};
class LazyImage final : public Image {
    mutable std::unique_ptr<DiskImage> image_;
public:
    void display() const override {
        if (!image_) image_ = std::make_unique<DiskImage>();
        image_->display();
    }
};
int main() {
    const LazyImage image;
    std::cout << "Proxy ready\n";
    image.display();
    image.display();
}
```

## الناتج المتوقع

```text
Proxy ready
Load image
Display image
Display image
```

## إمتى تستخدمه

استخدمه للتحميل عند الطلب أو فحص الوصول أو الوصول البعيد مع واجهة ثابتة.

## إمتى ما تستخدموش

بلاش لو الإنشاء رخيص وسياسة الوصول مش بتضيف قيمة.

## المميزات

الـ Client بيستخدم نفس display والإنشاء بيتأجل.

## العيوب والمقايضات

أول استدعاء هيدفع تكلفة التحميل. mutable هنا للـ Logical Constness مش أمان التزامن؛ وفشل التحميل محتاج سياسة.

## استخدامات تقنية

ينفع للوسائط عند الطلب وبوابات الصلاحيات وRemote Stubs، وكل واحدة ليها طريقة فشل مختلفة.

## أنماط مرتبطة

[decorator](../decorator/README.ar-EG.md) · [adapter](../adapter/README.ar-EG.md)

## لخبطة شائعة

Decorator بتضيف سلوك، Proxy بتتحكم إمتى وهل نوصل للأصل؛ الرسم ممكن يبقى شبه بعض.

## سؤال انترفيو

لو التحميل رمى Exception، تعيد المحاولة المرة الجاية ولا تفتكر الفشل؟

## تحدي صغير

عدّ مرات التحميل مع ثلاث مرات عرض، وجرّب Loader بتفشل مرة عشان تختبر سياسة المحاولة.

## الخلاصة

- **المشكلة:** معرض الصور ممكن يجهّز صور كتير بس يعرض كام واحدة.
- **الحل:** LazyImage بتنفذ Image، وبتعمل DiskImage عند أول display وبعد كده تعيد استخدامها.
- **المقايضة:** أول استدعاء هيدفع تكلفة التحميل. mutable هنا للـ Logical Constness مش أمان التزامن؛ وفشل التحميل محتاج سياسة.
- **افتكر:** بديل بينك وبين الأصل.

[السابق](../../structural/flyweight/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/chain-of-responsibility/README.ar-EG.md)
