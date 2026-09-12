# المركّب

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/bridge/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/decorator/README.ar-EG.md)

## الفئة

التركيب

## المستوى

مبتدئ

## في جملة واحدة

عامل العنصر الواحد وشجرة العناصر بنفس العملية.

## المشكلة

متصفح الملفات محتاج يحسب حجم ملف أو فولدر جواه فولدرات تانية.

## حل بسيط في الأول

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## ليه الحل بيصعّب الدنيا

Loops مخصوصة لكل عمق بتتكسر لما التداخل يزيد، وبتكرر سؤال: ده ملف ولا فولدر؟

## الفكرة الأساسية

خلّي File وFolder ينفذوا Entry. الفولدر يسأل كل طفل عن حجمه بشكل Recursive.

## مثال من الحياة

كرتونة الشحن ممكن تشيل طرود أو كراتين أصغر؛ حساب الوزن بيتكرر بنفس القاعدة.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![المركّب](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## الأدوار

Entry بتحدد bytes. File بترجع حجمها، وFolder بتمتلك الأطفال بـ unique_ptr وبتجمع نتايجهم.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <utility>
#include <vector>

struct Entry {
    virtual ~Entry() = default;
    virtual int bytes() const = 0;
};
class File final : public Entry {
    int size_;
public:
    explicit File(int size) : size_(size) {
        if (size < 0) throw std::invalid_argument("Negative size");
    }
    int bytes() const override { return size_; }
};
class Folder final : public Entry {
    std::vector<std::unique_ptr<Entry>> children_;
public:
    void add(std::unique_ptr<Entry> child) {
        if (!child) throw std::invalid_argument("Null child");
        children_.push_back(std::move(child));
    }
    int bytes() const override {
        int total = 0;
        for (const auto& child : children_) total += child->bytes();
        return total;
    }
};
int main() {
    auto images = std::make_unique<Folder>();
    images->add(std::make_unique<File>(20));
    Folder root;
    root.add(std::make_unique<File>(10));
    root.add(std::move(images));
    std::cout << "Total: " << root.bytes() << " bytes\n";
}
```

## الناتج المتوقع

```text
Total: 30 bytes
```

## إمتى تستخدمه

استخدمه لشجرة جزء وكل حقيقية، وعملية مفيدة تنفع للورقة والمجموعة.

## إمتى ما تستخدموش

بلاش لقائمة مسطحة أو Graph فيها مشاركة ودورات؛ ملكية الشجرة مش هتمثلها صح.

## المميزات

الـ Client يحسب إجمالي فرع من غير ما يعرف عمقه أو شكله.

## العيوب والمقايضات

العمق الكبير ممكن يملأ الـ Stack، والجمع ممكن يتجاوز سعة int. ماتفرضش عمليات المجموعات على الورق.

## استخدامات تقنية

ينفع لشجر الملفات وقوائم الواجهة ومشاهد من غير مشاركة عقد.

## أنماط مرتبطة

[decorator](../decorator/README.ar-EG.md) · [iterator](../../behavioral/iterator/README.ar-EG.md)

## لخبطة شائعة

Decorator بتلف عنصر واحد لإضافة سلوك؛ Composite بتجمع أطفال عشان تمثل كل. الاتنين ممكن يستخدموا نفس الواجهة بشكل متكرر.

## سؤال انترفيو

ليه add في Folder مش Entry؟ إضافة طفل لملف معناها إيه؟

## تحدي صغير

ضيف فولدر فاضي ومستوى تداخل كمان، وراجع الأحجام وفكّر في نوع أوسع للأرقام.

## الخلاصة

- **المشكلة:** متصفح الملفات محتاج يحسب حجم ملف أو فولدر جواه فولدرات تانية.
- **الحل:** خلّي File وFolder ينفذوا Entry. الفولدر يسأل كل طفل عن حجمه بشكل Recursive.
- **المقايضة:** العمق الكبير ممكن يملأ الـ Stack، والجمع ممكن يتجاوز سعة int. ماتفرضش عمليات المجموعات على الورق.
- **افتكر:** المجموعة بتجاوب زي عنصر.

[السابق](../../structural/bridge/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/decorator/README.ar-EG.md)
