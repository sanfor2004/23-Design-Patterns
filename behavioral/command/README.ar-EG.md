# Command

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/chain-of-responsibility/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/interpreter/README.ar-EG.md)

[خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [ملخص سريع](../../CHEATSHEET.ar-EG.md) · [Python](python/README.md) · [C++20](cpp/README.md)

## Category

[`Behavioral Pattern`](../../GLOSSARY.md#behavioral-pattern) — بيركز على سلوك الـ`Objects` وطريقة تعاونها.

## Difficulty

متوسط

## In One Sentence

مثّل الفعل بكائن (`object`) تقدر تخزنه وتشغّله بعدين.

## ببساطة

المحرر محتاج يفتكر التعديلات عشان المستخدم يقدر يرجع فيها.الـ`Command` بيحتفظ بالفعل وبيانات التراجع، والـ`History` بيحدد إمتى ينفّذه أو يلغيه.

## The Problem

المحرر محتاج ينفذ تعديلات ويرجع آخر تعديل من غير ما شريط الأدوات يعرف كل تفاصيل المستند.

## Naive Solution

```cpp
document.text += " world"; // no object records how to undo
```

## Why It Becomes a Problem

التعديل المباشر بيغيّر النص، بس مابيسجلش الفعل ولا الـ `state` اللي قبله.

## The Idea

خلّي الأمر `Append` يحتفظ بالمستند والمعامل المطلوب. عند التنفيذ، العملية `execute` بتحفظ النص القديم؛ وعند التراجع، العملية `undo` بترجّعه. السجل `History` بيمتلك الأوامر اللي اتنفّذت.

## Real-World Analogy

تذكرة طلب المطعم بتسجل المطلوب بعيد عن الجرسون اللي سلّمها.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Command](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## Participants

في المثال، العقد `Command` بيحدد العمليتين `execute` و `undo`. الأمر `Append` بيعدل مستند مستعار من نوع `Document`، وسجل `History` بيدير الأوامر المنفذة بترتيب المكدّس (`stack`).

الأدوار القياسية في المثال ده:

- [`Receiver`](../../GLOSSARY.md#receiver) — الـ `object` اللي بيتنفذ عليها الشغل المطلوب من `Command`. هنا: `Document`.
- [`Invoker`](../../GLOSSARY.md#invoker) — الدور اللي بيشغّل `Commands` أو بيخزنها من غير معرفة تفاصيل كل عملية. هنا: `History`.
- [`Concrete Command`](../../GLOSSARY.md#concrete-command) — تنفيذ للأمر (`Command implementation`) بيربط الفعل المطلوب بالجهة اللي هتنفّذه (`Receiver`). هنا: `Append`.

## Python Example

ابدأ بـ[مثال Python الصغير](python/README.md) و[الكود](python/main.py). توقّع [الناتج](python/expected.txt)، وبعدها شغّل وعدّل. ملاحظات المثال بالإنجليزي بتوضح الفروق مع C++20.

## Modern C++20 Example

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

## Example Output

```text
Hello world
Hello
Empty undo: Hello
```

## When to Use

استخدمه للأفعال المؤجلة والطوابير والـ `Macros` وتاريخ التراجع.

### Use cases

مناسب للمحررات وطوابير الوظائف، بس الطابور الدائم محتاج `Serialization` و `Idempotency` زيادة.

## When NOT to Use

بلاش لـ `function` بتتنادي مرة ومش محتاجة تخزين نية أو جدولة.

## Advantages

اللي بينادي مش مرتبط بكل عملية فعلية، ويقدر يحتفظ بتاريخها.

## Trade-offs

حفظ النص كله مكلف. المثال في `Thread` واحدة وبيفترض كل التعديلات عبر `History`، والمستند أطول عمراً منها؛ تعديل خارجي يبوّظ توقعات `undo`.

## Related Patterns

[Memento](../memento/README.ar-EG.md) · [Chain of Responsibility](../chain-of-responsibility/README.ar-EG.md)

## Common Confusion

الـ `Memento` بتخزن `state`، `Command` بتخزن فعل وممكن تستخدم `Snapshot` للتراجع. مش كل أمر قابل للعكس.

## Terms to Remember

- `Command` — مثّل الفعل بكائن (`object`) تقدر تخزنه وتشغّله بعدين.
- `Receiver` — الـ `object` اللي بيتنفذ عليها الشغل المطلوب من `Command`. مثال: `Document`.
- `Invoker` — الدور اللي بيشغّل `Commands` أو بيخزنها من غير معرفة تفاصيل كل عملية. مثال: `History`.
- `Concrete Command` — تنفيذ للأمر (`Command implementation`) بيربط الفعل المطلوب بالجهة اللي هتنفّذه (`Receiver`). مثال: `Append`.

## Interview Vocabulary

- [`undo`](../../GLOSSARY.md#undo) — بترجع لنتيجة سابقة باستخدام `state` محفوظة أو عملية عكسية لما ينفع.
- [`encapsulation`](../../GLOSSARY.md#encapsulation) — بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.
- [`exception safety`](../../GLOSSARY.md#exception-safety) — الضمانات اللي العملية بتحافظ عليها لو فشلت ورمت `exception`.

## Interview Question

ينفع ترجع إرسال إيميل زي ما بترجع `string`؟ فرّق بين التعويض والعكس.

## Mini Challenge

ضيف تعديلين، ارجع مرتين، واتأكد إن `undo` على تاريخ فاضي آمنة.

## اختبر فهمك

1. ليه لازم نلغي التعديلات دي بعكس ترتيب تنفيذها؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

## Quick Summary

- **المشكلة:** المحرر محتاج ينفذ تعديلات ويرجع آخر تعديل من غير ما شريط الأدوات يعرف كل تفاصيل المستند.
- **الحل:** خلّي الأمر `Append` يحتفظ بالمستند والمعامل المطلوب. عند التنفيذ، العملية `execute` بتحفظ النص القديم؛ وعند التراجع، العملية `undo` بترجّعه. السجل `History` بيمتلك الأوامر اللي اتنفّذت.
- **`Trade-off`:** حفظ النص كله مكلف. المثال في `Thread` واحدة وبيفترض كل التعديلات عبر `History`، والمستند أطول عمراً منها؛ تعديل خارجي يبوّظ توقعات `undo`.
- **افتكر:** فعل تقدر تحتفظ بيه.

[السابق](../../behavioral/chain-of-responsibility/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/interpreter/README.ar-EG.md)
