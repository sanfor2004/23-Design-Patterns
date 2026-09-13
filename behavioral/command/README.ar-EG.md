# Command

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** مثّل الفعل بكائن (`object`) تقدر تخزنه وتشغّله بعدين.

## المشكلة

المحرر محتاج ينفذ تعديلات ويرجع آخر تعديل من غير ما شريط الأدوات يعرف كل تفاصيل المستند. التعديل المباشر بيغيّر النص، بس مابيسجلش الفعل ولا الـ `state` اللي قبله.

## الحل ببساطة

المحرر محتاج يفتكر التعديلات عشان المستخدم يقدر يرجع فيها.الـ`Command` بيحتفظ بالفعل وبيانات التراجع، والـ`History` بيحدد إمتى ينفّذه أو يلغيه. خلّي الأمر `Append` يحتفظ بالمستند والمعامل المطلوب. عند التنفيذ، العملية `execute` بتحفظ النص القديم؛ وعند التراجع، العملية `undo` بترجّعه. السجل `History` بيمتلك الأوامر اللي اتنفّذت.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Command](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

في المثال، العقد `Command` بيحدد العمليتين `execute` و `undo`. الأمر `Append` بيعدل مستند مستعار من نوع `Document`، وسجل `History` بيدير الأوامر المنفذة بترتيب المكدّس (`stack`).

الأدوار القياسية في المثال ده:

- [`Receiver`](../../GLOSSARY.md#receiver) — الـ `object` اللي بيتنفذ عليها الشغل المطلوب من `Command`. هنا: `Document`.
- [`Invoker`](../../GLOSSARY.md#invoker) — الدور اللي بيشغّل `Commands` أو بيخزنها من غير معرفة تفاصيل كل عملية. هنا: `History`.
- [`Concrete Command`](../../GLOSSARY.md#concrete-command) — تنفيذ للأمر (`Command implementation`) بيربط الفعل المطلوب بالجهة اللي هتنفّذه (`Receiver`). هنا: `Append`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Document:
    def __init__(self, text):
        self.text = text


class Append:
    def __init__(self, document, suffix):
        self.document = document
        self.suffix = suffix
        self.before = None

    def execute(self):
        self.before = self.document.text
        self.document.text += self.suffix

    def undo(self):
        self.document.text = self.before


class History:
    def __init__(self):
        self.commands = []

    def run(self, command):
        command.execute()
        self.commands.append(command)

    def undo(self):
        if self.commands:
            self.commands.pop().undo()


if __name__ == "__main__":
    document = Document("Hello")
    history = History()
    history.run(Append(document, " world"))
    history.run(Append(document, "!"))
    print(document.text)
    for _ in range(3):
        history.undo()
        print(document.text)
```

### Python output

```text
Hello world!
Hello world
Hello
Hello
```

## C++20 example

```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct Document { std::string text; };
struct Command {
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};
class Append final : public Command {
    Document& document_;
    std::string suffix_;
    std::string before_;
public:
    Append(Document& document, std::string suffix) : document_(document), suffix_(std::move(suffix)) {}
    void execute() override { before_ = document_.text; document_.text += suffix_; }
    void undo() override { document_.text = before_; }
};
class History {
    std::vector<std::unique_ptr<Command>> commands_;
public:
    void run(std::unique_ptr<Command> command) {
        if (!command) throw std::invalid_argument("Missing command");
        commands_.push_back(std::move(command));
        try { commands_.back()->execute(); }
        catch (...) { commands_.pop_back(); throw; }
    }
    void undo() {
        if (commands_.empty()) return;
        commands_.back()->undo();
        commands_.pop_back();
    }
};
int main() {
    Document document{"Hello"};
    History history;
    history.run(std::make_unique<Append>(document, " world"));
    std::cout << document.text << '\n';
    history.undo();
    std::cout << document.text << '\n';
    history.undo();
    std::cout << "Empty undo: " << document.text << '\n';
}
```

### C++20 output

```text
Hello world
Hello
Empty undo: Hello
```

## قارن اللغتين

A callable is enough for an action with no history. Here a Command Object keeps the previous text for undo. Python retains the Document; C++ borrows it and owns Commands in History. Undo assumes commands run once and are undone in reverse order, with no unrelated edits in between.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه للأفعال المؤجلة والطوابير والـ `Macros` وتاريخ التراجع.

### Use cases

مناسب للمحررات وطوابير الوظائف، بس الطابور الدائم محتاج `Serialization` و `Idempotency` زيادة.

**التكلفة:** حفظ النص كله مكلف. المثال في `Thread` واحدة وبيفترض كل التعديلات عبر `History`، والمستند أطول عمراً منها؛ تعديل خارجي يبوّظ توقعات `undo`.

## جرّب تجاوب

1. ليه لازم نلغي التعديلات دي بعكس ترتيب تنفيذها؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف تعديلين، ارجع مرتين، واتأكد إن `undo` على تاريخ فاضي آمنة.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
