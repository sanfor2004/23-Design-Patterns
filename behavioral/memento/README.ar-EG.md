# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — Design Pattern بيركز على behavior وتعاون objects مع بعض.

## Difficulty

متوسط

## In One Sentence

احفظ state بتاعة object وارجعها من غير كشف تفاصيل النسخة المحفوظة.

## The Problem

المحرر محتاج نقطة رجوع قبل تعديل تجريبي.

## Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why It Becomes a Problem

لو مدير التراجع بينسخ Fields عامة بنفسه، كل Field داخلية جديدة هتحتاج تعديله.

## The Idea

Editor بتعمل Snapshot بنص خاص، وبعدها تقرأها عشان ترجع نفسها.

## Real-World Analogy

Checkpoint اللعبة بترجعك لنقطة قديمة من غير ما تعرض لك صيغة البيانات.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Participants

Editor هي صاحبة الـ state ، Snapshot بتحفظها بشكل خاص، و main بتحتفظ بيها من غير ما تفتش جواها.

الأدوار القياسية في المثال ده:

- [`Originator`](../../GLOSSARY.md#originator) — الـ object اللي عارفة تحفظ state بتاعتها وترجعها. هنا: `Editor`.
- [`Caretaker`](../../GLOSSARY.md#caretaker) — الدور اللي بيحتفظ بـ Memento من غير ما يفتش في تمثيلها الداخلي. هنا: `main`.
- [`snapshot`](../../GLOSSARY.md#snapshot) — صورة محفوظة لجزء محدد من state في لحظة معينة. هنا: `Editor::Snapshot`.

## Modern C++20 Example

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

## Example Output

```text
Broken edit
Draft
```

## When to Use

استخدمه لنقاط رجوع تقدر فيها الـ object تحدد نسخة متسقة من الـ state بتاعتها.

### Use cases

مناسب لنقاط حفظ المحرر والمحاكاة بشرط الـ state تكون كاملة ومتسقة.

## When NOT to Use

بلاش لو الـ state ضخمة أو الموارد ماينفعش ترجع، أو تسجيل العملية العكسية أرخص.

## Advantages

شكل الـ state المحفوظة بيفضل خاص، ومدير الحفظ مش بينسخ الحقول بنفسه.

## Trade-offs

النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع string مش هيرجع ملفات أو اتصالات شبكة حصلت بره.

## Related Patterns

[Command](../command/README.ar-EG.md) · [Prototype](../../creational/prototype/README.ar-EG.md)

## Common Confusion

Command بتسجل فعل، Memento بتسجل state. Prototype بتعمل object تانية بدل استرجاع دي.

## Terms to Remember

- `Memento` — احفظ state بتاعة object وارجعها من غير كشف تفاصيل النسخة المحفوظة.
- `Originator` — الـ object اللي عارفة تحفظ state بتاعتها وترجعها. مثال: `Editor`.
- `Caretaker` — الدور اللي بيحتفظ بـ Memento من غير ما يفتش في تمثيلها الداخلي. مثال: `main`.
- `snapshot` — صورة محفوظة لجزء محدد من state في لحظة معينة. مثال: `Editor::Snapshot`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.
- [`undo`](../../GLOSSARY.md#undo) — بترجع لنتيجة سابقة باستخدام state محفوظة أو عملية عكسية لما ينفع.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.

## Interview Question

لو Editor ضافت مكان المؤشر، مين لازم يتعدل عشان الرجوع يفضل صح؟

## Mini Challenge

ضيف مكان المؤشر لـ Snapshot واختبر رجوعه مع النص.

## Quick Summary

- **المشكلة:** المحرر محتاج نقطة رجوع قبل تعديل تجريبي.
- **الحل:** Editor بتعمل Snapshot بنص خاص، وبعدها تقرأها عشان ترجع نفسها.
- **Trade-off:** النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع string مش هيرجع ملفات أو اتصالات شبكة حصلت بره.
- **افتكر:** افتكر الـ state من غير ما تكشفها.

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)
