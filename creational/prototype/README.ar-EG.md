# النموذج الأولي

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)

## الفئة

الإنشاء

## المستوى

متوسط

## في جملة واحدة

اعمل Object مستقلة عن طريق نسخ نموذج متجهّز.

## المشكلة

اللعبة محتاجة أعداء من Template جاهزة، وكود الـ Spawn مش عارف النوع الفعلي.

## حل بسيط في الأول

```cpp
Guard another;
another.rename("gate guard"); // must repeat any custom setup
```

## ليه الحل بيصعّب الدنيا

إنشاء Guard افتراضية كل مرة بيكرر التجهيز وبيضيّع أي معدات مخصصة في النموذج.

## الفكرة الأساسية

وفّر clone في Enemy. Guard بتنسخ الـ Value Members وترجع unique_ptr لـ Object مستقلة.

## مثال من الحياة

زي نسخة من مستند متجهّز: تغيّر اسم النسخة من غير ما تلمس الأصل.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![النموذج الأولي](../../assets/diagrams/prototype.svg)

```text
Client  -->  Enemy::clone()  -->  independent Guard
```

## الأدوار

Enemy بتحدد النسخ متعدد الأشكال، وGuard بتنفذه؛ الـ Client بيمتلك النسخة ويغيّر اسمها.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <utility>
#include <vector>

struct Enemy {
    virtual ~Enemy() = default;
    virtual std::unique_ptr<Enemy> clone() const = 0;
    virtual void rename(std::string name) = 0;
    virtual void describe() const = 0;
};
class Guard final : public Enemy {
    std::string name_ = "template";
    std::vector<std::string> equipment_{"shield", "spear"};
public:
    std::unique_ptr<Enemy> clone() const override { return std::make_unique<Guard>(*this); }
    void rename(std::string name) override { name_ = std::move(name); }
    void describe() const override {
        std::cout << name_ << ": " << equipment_.size() << " items\n";
    }
};
int main() {
    const Guard prototype;
    auto copy = prototype.clone();
    copy->rename("gate guard");
    prototype.describe();
    copy->describe();
}
```

## الناتج المتوقع

```text
template: 2 items
gate guard: 2 items
```

## إمتى تستخدمه

استخدمه لما الـ Objects الموجودة شايلة إعداد مهم، والـ Client مش المفروض يعيد بناء نوعها الفعلي.

## إمتى ما تستخدموش

بلاش لو النسخ العادي بالقيمة واضح وكافي.

## المميزات

بتعيد استخدام التجهيز من غير ما تكشف كل خطوات الإنشاء للـ Client.

## العيوب والمقايضات

لو فيه Pointers لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. Socket مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.

## استخدامات تقنية

مناسب لقوالب كيانات الألعاب والمستندات؛ المثال بينسخ string وvector بالقيمة.

## أنماط مرتبطة

[abstract-factory](../abstract-factory/README.ar-EG.md) · [memento](../../behavioral/memento/README.ar-EG.md)

## لخبطة شائعة

Memento بترجّع نفس الـ Object لحالة قديمة. Prototype بتعمل Object تانية، والـ Copy Constructor لوحدها مش بتوفر نسخ Polymorphic.

## سؤال انترفيو

لو المعدات بقت vector<shared_ptr<Item>>، هل النسخة هتفضل مستقلة؟ وضّح المشاركة.

## تحدي صغير

خلّي المعدات قابلة للتعديل، واتأكد إن تعديل النسخة مايمسش الأصل.

## الخلاصة

- **المشكلة:** اللعبة محتاجة أعداء من Template جاهزة، وكود الـ Spawn مش عارف النوع الفعلي.
- **الحل:** وفّر clone في Enemy. Guard بتنسخ الـ Value Members وترجع unique_ptr لـ Object مستقلة.
- **المقايضة:** لو فيه Pointers لازم تحدد هتنسخ بعمق ولا هتشارك البيانات. Socket مفتوحة أو مورد حصري ممكن ماينفعش يتنسخ.
- **افتكر:** انسخ التجهيز، مش الهوية.

[السابق](../../creational/factory-method/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/singleton/README.ar-EG.md)
