# التذكار

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

احفظ حالة Object وارجعها من غير كشف تفاصيل النسخة المحفوظة.

## المشكلة

المحرر محتاج نقطة رجوع قبل تعديل تجريبي.

## حل بسيط في الأول

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## ليه الحل بيصعّب الدنيا

لو مدير التراجع بينسخ Fields عامة بنفسه، كل Field داخلية جديدة هتحتاج تعديله.

## الفكرة الأساسية

Editor بتعمل Snapshot بنص خاص، وبعدها تقرأها عشان ترجع نفسها.

## مثال من الحياة

Checkpoint اللعبة بترجعك لنقطة قديمة من غير ما تعرض لك صيغة البيانات.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![التذكار](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## الأدوار

Editor هي صاحبة الحالة، Snapshot بتحفظها بشكل خاص، وmain بتحتفظ بيها من غير ما تفتش جواها.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <string>
#include <utility>

class Editor {
    std::string text_;
public:
    class Snapshot {
        friend class Editor;
        std::string text_;
        explicit Snapshot(std::string text) : text_(std::move(text)) {}
    };
    void write(std::string text) { text_ = std::move(text); }
    Snapshot save() const { return Snapshot{text_}; }
    void restore(const Snapshot& snapshot) { text_ = snapshot.text_; }
    const std::string& text() const { return text_; }
};
int main() {
    Editor editor;
    editor.write("Draft");
    const auto checkpoint = editor.save();
    editor.write("Broken edit");
    std::cout << editor.text() << '\n';
    editor.restore(checkpoint);
    std::cout << editor.text() << '\n';
}
```

## الناتج المتوقع

```text
Broken edit
Draft
```

## إمتى تستخدمه

استخدمه لنقاط رجوع تقدر فيها الـ Object تحدد نسخة متسقة من حالتها.

## إمتى ما تستخدموش

بلاش لو الحالة ضخمة أو الموارد ماينفعش ترجع، أو تسجيل العملية العكسية أرخص.

## المميزات

شكل الحالة المحفوظة بيفضل خاص، ومدير الحفظ مش بينسخ الحقول بنفسه.

## العيوب والمقايضات

النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع string مش هيرجع ملفات أو اتصالات شبكة حصلت بره.

## استخدامات تقنية

مناسب لنقاط حفظ المحرر والمحاكاة بشرط الحالة تكون كاملة ومتسقة.

## أنماط مرتبطة

[command](../command/README.ar-EG.md) · [prototype](../../creational/prototype/README.ar-EG.md)

## لخبطة شائعة

Command بتسجل فعل، Memento بتسجل حالة. Prototype بتعمل Object تانية بدل استرجاع دي.

## سؤال انترفيو

لو Editor ضافت مكان المؤشر، مين لازم يتعدل عشان الرجوع يفضل صح؟

## تحدي صغير

ضيف مكان المؤشر لـ Snapshot واختبر رجوعه مع النص.

## الخلاصة

- **المشكلة:** المحرر محتاج نقطة رجوع قبل تعديل تجريبي.
- **الحل:** Editor بتعمل Snapshot بنص خاص، وبعدها تقرأها عشان ترجع نفسها.
- **المقايضة:** النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع string مش هيرجع ملفات أو اتصالات شبكة حصلت بره.
- **افتكر:** افتكر الحالة من غير ما تكشفها.

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)
