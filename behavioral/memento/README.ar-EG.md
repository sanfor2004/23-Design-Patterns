# Memento

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** احفظ حالة الكائن (`state`) عشان تقدر ترجعها بعدين، من غير ما تكشف تفاصيل النسخة المحفوظة.

## المشكلة

المحرر محتاج نقطة رجوع قبل تعديل تجريبي. لو مدير التراجع بينسخ `Fields` عامة بنفسه، كل `Field` داخلية جديدة هتحتاج تعديله.

## الحل ببساطة

المحرر محتاج نقطة رجوع قبل تعديل ممكن يبوّظ النص. الـ`Memento` بيحفظ نسخة من الـ`state`، والمحرر هو اللي بيحدد إزاي يحفظها ويرجعها. خلّي المحرر `Editor` ينشئ نسخة محفوظة (`Snapshot`) فيها النص بشكل خاص. لما تحتاج ترجع، المحرر نفسه هو اللي يقرأ النسخة ويستعيد حالته.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Memento](../../assets/diagrams/memento.svg)

```text
Caretaker  -->  Editor::Snapshot  -->  Editor::restore()
```

في المثال، المحرر `Editor` هو صاحب الحالة (`state`). النسخة `Snapshot` بتحفظها بشكل خاص، والدالة `main` بتحتفظ بالنسخة من غير ما تقرأ تفاصيلها الداخلية.

الأدوار القياسية في المثال ده:

- [`Originator`](../../GLOSSARY.md#originator) — الكائن اللي يعرف يحفظ حالته (`state`) ويسترجعها. هنا: `Editor`.
- [`Caretaker`](../../GLOSSARY.md#caretaker) — الدور اللي بيحتفظ بـ `Memento` من غير ما يفتش في تمثيلها الداخلي. هنا: `main`.
- [`snapshot`](../../GLOSSARY.md#snapshot) — صورة محفوظة لجزء محدد من `state` في لحظة معينة. هنا: `Editor::Snapshot`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Snapshot:
    def __init__(self, text):
        self._text = text


class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text = text

    def save(self):
        return Snapshot(self.text)

    def restore(self, snapshot):
        self.text = snapshot._text


if __name__ == "__main__":
    editor = Editor()
    editor.write("Draft")
    checkpoint = editor.save()
    editor.write("Broken edit")
    print(editor.text)
    editor.restore(checkpoint)
    print(editor.text)
    editor.write("Another edit")
    editor.restore(checkpoint)
    print(editor.text)
```

### Python output

```text
Broken edit
Draft
Draft
```

## C++20 example

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

### C++20 output

```text
Broken edit
Draft
Restore again: Draft
```

## قارن اللغتين

Python uses an underscore to mark snapshot details as internal by convention. C++ enforces private access with a friend declaration. Both snapshots hold immutable text values here. Mutable nested State would require an explicit copy policy; neither snapshot reverses external side effects.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لنقاط رجوع تقدر فيها الـ `object` تحدد نسخة متسقة من الـ `state` بتاعتها.

### Use cases

مناسب لنقاط حفظ المحرر والمحاكاة بشرط الـ `state` تكون كاملة ومتسقة.

**التكلفة:** النسخ الكاملة بتكلف ذاكرة ووقت. استرجاع `string` مش هيرجع ملفات أو اتصالات شبكة حصلت بره.

## جرّب تجاوب

1. ليه التعديلات الجديدة لازم ما تغيّرش الـ`Snapshot` المحفوظة؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف مكان المؤشر لـ `Snapshot` واختبر رجوعه مع النص.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
