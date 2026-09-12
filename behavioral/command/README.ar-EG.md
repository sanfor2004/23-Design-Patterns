# الأمر

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../behavioral/chain-of-responsibility/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/interpreter/README.ar-EG.md)

## الفئة

السلوك

## المستوى

متوسط

## في جملة واحدة

حوّل الفعل لـ Object تقدر تخزنها وتشغّلها بعدين.

## المشكلة

المحرر محتاج ينفذ تعديلات ويرجع آخر تعديل من غير ما شريط الأدوات يعرف كل تفاصيل المستند.

## حل بسيط في الأول

```cpp
document.text += " world"; // no object records how to undo
```

## ليه الحل بيصعّب الدنيا

التعديل المباشر بيغيّر النص، بس مابيسجلش الفعل ولا الحالة اللي قبله.

## الفكرة الأساسية

Append بتحتفظ بالمستند والمعامل؛ execute بتحفظ النص القديم وundo بترجعه. History بتمتلك الأوامر المنفذة.

## مثال من الحياة

تذكرة طلب المطعم بتسجل المطلوب بعيد عن الجرسون اللي سلّمها.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الأمر](../../assets/diagrams/command.svg)

```text
History  -->  Command  -->  Append → Document
```

## الأدوار

Command بتحدد execute وundo، Append بتعدل Document مستعارة، وHistory بتدير Stack الأوامر.

## C++20 — مثال كامل قابل للتشغيل

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
}
```

## الناتج المتوقع

```text
Hello world
Hello
```

## إمتى تستخدمه

استخدمه للأفعال المؤجلة والطوابير والـ Macros وتاريخ التراجع.

## إمتى ما تستخدموش

بلاش لدالة بتتنادي مرة ومش محتاجة تخزين نية أو جدولة.

## المميزات

اللي بينادي مش مرتبط بكل عملية فعلية، ويقدر يحتفظ بتاريخها.

## العيوب والمقايضات

حفظ النص كله مكلف. المثال في Thread واحدة وبيفترض كل التعديلات عبر History، والمستند أطول عمراً منها؛ تعديل خارجي يبوّظ توقعات undo.

## استخدامات تقنية

مناسب للمحررات وطوابير الوظائف، بس الطابور الدائم محتاج Serialization وIdempotency زيادة.

## أنماط مرتبطة

[memento](../memento/README.ar-EG.md) · [chain-of-responsibility](../chain-of-responsibility/README.ar-EG.md)

## لخبطة شائعة

Memento بتخزن حالة، Command بتخزن فعل وممكن تستخدم Snapshot للتراجع. مش كل أمر قابل للعكس.

## سؤال انترفيو

ينفع ترجع إرسال إيميل زي ما بترجع string؟ فرّق بين التعويض والعكس.

## تحدي صغير

ضيف تعديلين، ارجع مرتين، واتأكد إن undo على تاريخ فاضي آمنة.

## الخلاصة

- **المشكلة:** المحرر محتاج ينفذ تعديلات ويرجع آخر تعديل من غير ما شريط الأدوات يعرف كل تفاصيل المستند.
- **الحل:** Append بتحتفظ بالمستند والمعامل؛ execute بتحفظ النص القديم وundo بترجعه. History بتمتلك الأوامر المنفذة.
- **المقايضة:** حفظ النص كله مكلف. المثال في Thread واحدة وبيفترض كل التعديلات عبر History، والمستند أطول عمراً منها؛ تعديل خارجي يبوّظ توقعات undo.
- **افتكر:** فعل تقدر تحتفظ بيه.

[السابق](../../behavioral/chain-of-responsibility/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../behavioral/interpreter/README.ar-EG.md)
