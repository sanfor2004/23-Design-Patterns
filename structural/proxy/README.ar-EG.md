# Proxy

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** تحكّم في الوصول للكائن (`object`) عن طريق بديل بيوفّر نفس [`interface`](../../GLOSSARY.md#interface)، يعني نفس العقد اللي المستدعي بيتعامل معاه.

## المشكلة

معرض الصور ممكن يجهّز صور كتير بس يعرض كام واحدة. إنشاء الصور التقيلة فوراً بيحمّل حاجات قبل ما حد يطلب عرضها.

## الحل ببساطة

معرض الصور مش محتاج يحمّل كل صورة قبل ما حد يشوفها.الـ`Proxy` هنا بيوفر `display`، وبيجهّز الصورة عند أول استخدام وبعدين يعيد استخدامها. خلّي البديل `LazyImage` ينفّذ العقد `Image`. عند أول استدعاء للعملية `display`، أنشئ الصورة الفعلية `DiskImage`؛ وبعد كده أعد استخدامها.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Proxy](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

في المثال، العقد المشترك هو `Image`، والشغل الفعلي موجود في `DiskImage`. البديل `LazyImage` بيمتلك الصورة اللي بينشئها عند أول طلب للعرض.

الأدوار القياسية في المثال ده:

- [`Subject interface`](../../GLOSSARY.md#subject-interface) — العقد المشترك اللي `Proxy` و `Real Subject` بيوفروه. هنا: `Image`.
- [`Real Subject`](../../GLOSSARY.md#real-subject) — الـ `object` اللي بتنفذ الشغل الحقيقي ورا `Proxy`. هنا: `DiskImage`.
- [`lazy initialization`](../../GLOSSARY.md#lazy-initialization) — بتأجل الإنشاء لأول مرة تحتاج فيها القيمة أو المورد. هنا: `LazyImage::display`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class DiskImage:
    def __init__(self):
        print("Load image")

    def display(self):
        print("Display image")


class LazyImage:
    def __init__(self):
        self.image = None

    def display(self):
        if self.image is None:
            self.image = DiskImage()
        self.image.display()


if __name__ == "__main__":
    image = LazyImage()
    print("Proxy ready")
    image.display()
    image.display()
```

### Python output

```text
Proxy ready
Load image
Display image
Display image
```

## C++20 example

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

### C++20 output

```text
Proxy ready
Load image
Display image
Display image
```

## قارن اللغتين

Python starts with `None`; C++ starts with an empty `unique_ptr`. Both create the real image on the first call. C++ uses `mutable` to cache inside a const operation. Neither version synchronizes concurrent calls or demonstrates access control; this is a virtual Proxy for lazy loading.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه للتحميل عند الطلب أو فحص الوصول أو الوصول البعيد مع `interface` ثابتة.

### Use cases

ينفع للوسائط عند الطلب وبوابات الصلاحيات و `Remote Stubs`، وكل واحدة ليها طريقة فشل مختلفة.

**التكلفة:** أول استدعاء هيدفع تكلفة التحميل. الـ `mutable` هنا للـ `logical constness` مش أمان التزامن؛ وفشل التحميل محتاج سياسة.

## جرّب تجاوب

1. بعد استدعاء `display` مرتين، كام صورة فعلية اتعملت وإمتى؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** عدّ مرات التحميل مع ثلاث مرات عرض، وجرّب `Loader` بتفشل مرة عشان تختبر سياسة المحاولة.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
