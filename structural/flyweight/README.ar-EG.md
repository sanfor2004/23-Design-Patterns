# الكائن خفيف الوزن

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/facade/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/proxy/README.ar-EG.md)

## الفئة

التركيب

## المستوى

متقدم

## في جملة واحدة

شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل.

## المشكلة

المستند فيه حروف مكررة كتير؛ تخزين شكل الحرف كامل لكل مكان بيهدر الذاكرة.

## حل بسيط في الأول

```cpp
std::string shape1 = "A";
std::string shape2 = "A"; // repeated immutable data per placement
```

## ليه الحل بيصعّب الدنيا

نسخ نفس الشكل لكل ظهور بيخلّي الذاكرة تزيد بعدد المواضع بدل عدد الأشكال المختلفة.

## الفكرة الأساسية

خزّن Glyph حسب الحرف في Pool. PlacedGlyph بتشارك const Glyph وبتحتفظ بمكان x لوحدها.

## مثال من الحياة

كذا قارئ بيستخدموا نفس المرجع، وكل واحد عنده علامة صفحة بتاعته.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الكائن خفيف الوزن](../../assets/diagrams/flyweight.svg)

```text
PlacedGlyph(x)  -->  GlyphPool::get  -->  shared const Glyph
```

## الأدوار

Glyph شايلة الشكل المشترك، GlyphPool بتوحّد نسخه، وPlacedGlyph شايلة الموضع وملكية مشتركة.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <utility>

struct Glyph {
    const std::string shape;
    explicit Glyph(std::string value) : shape(std::move(value)) {}
};
class GlyphPool {
    std::map<char, std::shared_ptr<const Glyph>> glyphs_;
public:
    std::shared_ptr<const Glyph> get(char symbol) {
        auto& glyph = glyphs_[symbol];
        if (!glyph) glyph = std::make_shared<const Glyph>(std::string(1, symbol));
        return glyph;
    }
};
struct PlacedGlyph {
    std::shared_ptr<const Glyph> glyph;
    int x;
    void draw() const { std::cout << glyph->shape << " at " << x << '\n'; }
};
int main() {
    GlyphPool pool;
    const PlacedGlyph first{pool.get('A'), 0};
    const PlacedGlyph second{pool.get('A'), 10};
    first.draw();
    second.draw();
    std::cout << "Shared shape: " << std::boolalpha << (first.glyph == second.glyph) << '\n';
}
```

## الناتج المتوقع

```text
A at 0
A at 10
Shared shape: true
```

## إمتى تستخدمه

استخدمه بعد قياس تكرار كبير لبيانات ثابتة بين Objects كتير.

## إمتى ما تستخدموش

بلاش مع بيانات قليلة أو متغيرة لكل نسخة، أو لو البحث أغلى من التوفير.

## المميزات

المواضع بتستخدم نفس الشكل مع احتفاظ كل واحد بمكانه.

## العيوب والمقايضات

الـ Pool بتحتفظ بالعناصر، والـ map والـ shared_ptr ليهم تكلفة. النص هنا صغير ومفيش ادعاء بقياس توفير ذاكرة؛ الوصول للـ Pool مش متزامن.

## استخدامات تقنية

أشكال الحروف وتعريفات أرضية الألعاب والأسماء المتكررة مرشحين مناسبين لو القياس أكد ده.

## أنماط مرتبطة

[composite](../composite/README.ar-EG.md) · [prototype](../../creational/prototype/README.ar-EG.md)

## لخبطة شائعة

Prototype بتنسخ الإعداد لـ Object جديدة. Flyweight بتشارك الحالة الداخلية عن قصد.

## سؤال انترفيو

لو الخط وحجمه بيغيّروا الشكل، إيه اللي لازم يدخل في مفتاح الـ Pool؟

## تحدي صغير

ضيف معرف الخط للمفتاح، واتأكد إن المفاتيح المتساوية بتشارك والمختلفة لأ.

## الخلاصة

- **المشكلة:** المستند فيه حروف مكررة كتير؛ تخزين شكل الحرف كامل لكل مكان بيهدر الذاكرة.
- **الحل:** خزّن Glyph حسب الحرف في Pool. PlacedGlyph بتشارك const Glyph وبتحتفظ بمكان x لوحدها.
- **المقايضة:** الـ Pool بتحتفظ بالعناصر، والـ map والـ shared_ptr ليهم تكلفة. النص هنا صغير ومفيش ادعاء بقياس توفير ذاكرة؛ الوصول للـ Pool مش متزامن.
- **افتكر:** شارك الشكل، وافصل المكان.

[السابق](../../structural/facade/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/proxy/README.ar-EG.md)
