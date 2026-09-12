# المراقب

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)

## الفئة

السلوك

## المستوى

مبتدئ

## في جملة واحدة

بلّغ الـ Objects المشتركة لما الحاجة اللي بيتابعوها تتغير.

## المشكلة

تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما Stock تعرف كل نوع شاشة.

## حل بسيط في الأول

```cpp
display.update(quantity);
email.update(quantity); // publisher names every consumer
```

## ليه الحل بيصعّب الدنيا

استدعاء كل مستهلك باسمه بيربط الناشر بالقائمة الحالية، وإضافة مستهلك تحتاج تعديل الناشر.

## الفكرة الأساسية

Stock بتخزن weak references لـ Listener وبتبعت التحديث للنسخ اللي لسه عايشة.

## مثال من الحياة

المشتركين يوصلهم تنبيه توفر المنتج طول ما الاشتراك شغال.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المراقب](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

## الأدوار

Stock المصدر، Listener واجهة الاستقبال، وDisplay مشتركة. الـ Client بيمتلك المشتركين، وweak_ptr مش بتطوّل عمرهم.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
}
```

## الناتج المتوقع

```text
Stock: 4
Expired listener skipped
```

## إمتى تستخدمه

استخدمه لما تغيير واحد ليه كذا مستهلك بيسجلوا نفسهم باستقلال.

## إمتى ما تستخدموش

بلاش لاعتمادية ثابتة واحدة أو لما محتاج اتساق Transaction قوي.

## المميزات

المشتركين يدخلوا ويخرجوا من غير تعديل كود الناشر.

## العيوب والمقايضات

ترتيب الـ Callbacks والـ Exceptions محتاج سياسة. المثال Sync بيمرر الاستثناء ومش Thread-safe. نسخة القائمة بتسمح بتغيير الاشتراكات بس مش بتمنع إشعارات Recursive.

## استخدامات تقنية

مناسب لتحديث UI والأحداث المحلية؛ ضمانات الأحداث الموزعة موضوع تاني.

## أنماط مرتبطة

[mediator](../mediator/README.ar-EG.md) · [state](../state/README.ar-EG.md)

## لخبطة شائعة

Mediator بتحدد قواعد تنسيق زملاء معروفين. Observer بتذيع إشعار من غير فرض علاقة بينهم.

## سؤال انترفيو

ليه نخزن weak_ptr ونحوّلها لـ shared_ptr وقت الـ Callback؟

## تحدي صغير

ضيف مشتركين، امسح واحد، واتأكد إن الباقي بس يستقبل. عرّف عملية إلغاء اشتراك صريحة.

## الخلاصة

- **المشكلة:** تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما Stock تعرف كل نوع شاشة.
- **الحل:** Stock بتخزن weak references لـ Listener وبتبعت التحديث للنسخ اللي لسه عايشة.
- **المقايضة:** ترتيب الـ Callbacks والـ Exceptions محتاج سياسة. المثال Sync بيمرر الاستثناء ومش Thread-safe. نسخة القائمة بتسمح بتغيير الاشتراكات بس مش بتمنع إشعارات Recursive.
- **افتكر:** انشر التغيير، وسيب المشترك يرد.

[السابق](../../behavioral/memento/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/state/README.ar-EG.md)
