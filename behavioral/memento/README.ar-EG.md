# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

متوسط

## In One Sentence

احفظ حالة الكائن (`state`) عشان تقدر ترجعها بعدين، من غير ما تكشف تفاصيل النسخة المحفوظة.

## ببساطة

المحرر محتاج نقطة رجوع قبل تعديل ممكن يبوّظ النص. الـ`Memento` بيحفظ نسخة من الـ`state`، والمحرر هو اللي بيحدد إزاي يحفظها ويرجعها.

## The Problem

المحرر محتاج نقطة رجوع قبل تعديل تجريبي.

## Naive Solution

```cpp
std::string old_text = editor.text(); // caretaker knows what state to copy
```

## Why It Becomes a Problem

لو مدير التراجع بينسخ `Fields` عامة بنفسه، كل `Field` داخلية جديدة هتحتاج تعديله.

## The Idea

خلّي المحرر `Editor` ينشئ نسخة محفوظة (`Snapshot`) فيها النص بشكل خاص. لما تحتاج ترجع، المحرر نفسه هو اللي يقرأ النسخة ويستعيد حالته.

## Real-World Analogy

الـ `Checkpoint` اللعبة بترجعك لنقطة قديمة من غير ما تعرض لك صيغة البيانات.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

## Participants

في المثال، المحرر `Editor` هو صاحب الحالة (`state`). النسخة `Snapshot` بتحفظها بشكل خاص، والدالة `main` بتحتفظ بالنسخة من غير ما تقرأ تفاصيلها الداخلية.

الأدوار القياسية في المثال ده:

- [`Originator`](../../GLOSSARY.md#originator) — الكائن اللي يعرف يحفظ حالته (`state`) ويسترجعها. هنا: `Editor`.
- [`Caretaker`](../../GLOSSARY.md#caretaker) — الدور اللي بيحتفظ بـ `Memento` من غير ما يفتش في تمثيلها الداخلي. هنا: `main`.
- [`snapshot`](../../GLOSSARY.md#snapshot) — صورة محفوظة لجزء محدد من `state` في لحظة معينة. هنا: `Editor::Snapshot`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

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
    editor.write("Another edit");
    editor.restore(checkpoint);
    std::cout << "Restore again: " << editor.text() << '\n';
}
```

## Example Output

```text
Broken edit
Draft
Restore again: Draft
```

## When to Use

استخدمه لنقاط رجوع تقدر فيها الـ `object` تحدد نسخة متسقة من الـ `state` بتاعتها.

### Use cases

مناسب لنقاط حفظ المحرر والمحاكاة بشرط الـ `state` تكون كاملة ومتسقة.

## When NOT to Use

بلاش لو الـ `state` ضخمة أو الموارد ماينفعش ترجع، أو تسجيل العملية العكسية أرخص.

## Advantages

شكل الـ `state` المحفوظة بيفضل خاص، ومدير الحفظ مش بينسخ الحقول بنفسه.

## Trade-offs

النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع `string` مش هيرجع ملفات أو اتصالات شبكة حصلت بره.

## Related Patterns

[Command](../command/README.ar-EG.md) · [Prototype](../../creational/prototype/README.ar-EG.md)

## Common Confusion

الـ `Command` بتسجل فعل، `Memento` بتسجل `state`. الـ `Prototype` بتعمل `object` تانية بدل استرجاع دي.

## Terms to Remember

- `Memento` — احفظ حالة الكائن (`state`) عشان تقدر ترجعها بعدين، من غير ما تكشف تفاصيل النسخة المحفوظة.
- `Originator` — الكائن اللي يعرف يحفظ حالته (`state`) ويسترجعها. مثال: `Editor`.
- `Caretaker` — الدور اللي بيحتفظ بـ `Memento` من غير ما يفتش في تمثيلها الداخلي. مثال: `main`.
- `snapshot` — صورة محفوظة لجزء محدد من `state` في لحظة معينة. مثال: `Editor::Snapshot`.

## Interview Vocabulary

- [`encapsulation`](../../GLOSSARY.md#encapsulation) — بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.
- [`undo`](../../GLOSSARY.md#undo) — بترجع لنتيجة سابقة باستخدام `state` محفوظة أو عملية عكسية لما ينفع.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.

## Interview Question

لو `Editor` ضافت مكان المؤشر، مين لازم يتعدل عشان الرجوع يفضل صح؟

## Mini Challenge

ضيف مكان المؤشر لـ `Snapshot` واختبر رجوعه مع النص.

## اختبر فهمك

1. ليه التعديلات الجديدة لازم ما تغيّرش الـ`Snapshot` المحفوظة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** المحرر محتاج نقطة رجوع قبل تعديل تجريبي.
- **الحل:** خلّي المحرر `Editor` ينشئ نسخة محفوظة (`Snapshot`) فيها النص بشكل خاص. لما تحتاج ترجع، المحرر نفسه هو اللي يقرأ النسخة ويستعيد حالته.
- **`Trade-off`:** النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع `string` مش هيرجع ملفات أو اتصالات شبكة حصلت بره.
- **افتكر:** افتكر الـ `state` من غير ما تكشفها.

[السابق](../../behavioral/mediator/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/observer/README.ar-EG.md)
