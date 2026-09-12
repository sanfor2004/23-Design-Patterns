# Composite

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/bridge/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/decorator/README.ar-EG.md)

## Category

[`Structural Pattern`](../../GLOSSARY.md#structural-pattern) — بيركز على تركيب الكائنات والأنواع (`objects` و`classes`)، وده واحد من أغراض الـ `Design Patterns`.

## Difficulty

مبتدئ

## In One Sentence

عامل العنصر الواحد وشجرة العناصر بنفس العملية.

## The Problem

متصفح الملفات محتاج يحسب حجم ملف أو فولدر جواه فولدرات تانية.

## Naive Solution

```cpp
int total = file_size;
for (int size : folder_sizes) total += size; // only one nesting level
```

## Why It Becomes a Problem

الـ `Loops` مخصوصة لكل عمق بتتكسر لما التداخل يزيد، وبتكرر سؤال: ده ملف ولا فولدر؟

## The Idea

خلّي الملف `File` والفولدر `Folder` ينفّذوا نفس العقد `Entry`. لحساب الحجم، الفولدر بيسأل كل عنصر جواه عن حجمه؛ القاعدة بتتكرر مع كل مستوى (`recursion`).

## Real-World Analogy

كرتونة الشحن ممكن تشيل طرود أو كراتين أصغر؛ حساب الوزن بيتكرر بنفس القاعدة.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Composite](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

## Participants

في المثال، `Entry` بتحدد العملية `bytes`. الملف `File` بيرجع حجمه، والفولدر `Folder` بيجمع أحجام العناصر اللي جواه. الفولدر بيمتلك العناصر باستخدام [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr)، عشان تتحرر تلقائيًا معاه.

الأدوار القياسية في المثال ده:

- [`Component`](../../GLOSSARY.md#component) — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. هنا: `Entry`.
- [`Leaf`](../../GLOSSARY.md#leaf) — عنصر (`Component`) مافيهوش عناصر تحته. هنا: `File`.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر. هنا: `Folder::children_`.

## Modern C++20 Example

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

## Example Output

```text
Total: 30 bytes
```

## When to Use

استخدمه لشجرة جزء وكل حقيقية، وعملية مفيدة تنفع للورقة والمجموعة.

### Use cases

ينفع لشجر الملفات وقوائم الـ [`interface`](../../GLOSSARY.md#interface) (العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها) ومشاهد من غير مشاركة عقد.

## When NOT to Use

بلاش لقائمة مسطحة أو `Graph` فيها مشاركة ودورات؛ الـ `tree ownership` مش هتمثلها صح.

## Advantages

الـ `Client` يحسب إجمالي فرع من غير ما يعرف عمقه أو شكله.

## Trade-offs

العمق الكبير ممكن يملأ الـ `Stack`، والجمع ممكن يتجاوز سعة `int`. ماتفرضش عمليات المجموعات على الورق.

## Related Patterns

[Decorator](../decorator/README.ar-EG.md) · [Iterator](../../behavioral/iterator/README.ar-EG.md)

## Common Confusion

الـ `Decorator` بتلف عنصر واحد لإضافة `behavior`؛ الـ `Composite` بتجمع أطفال عشان تمثل كل. الاتنين ممكن يستخدموا نفس الـ `interface` بشكل متكرر.

## Terms to Remember

- `Composite` — عامل العنصر الواحد وشجرة العناصر بنفس العملية.
- `Component` — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. مثال: `Entry`.
- `Leaf` — عنصر (`Component`) مافيهوش عناصر تحته. مثال: `File`.
- `ownership` — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر. مثال: `Folder::children_`.

## Interview Vocabulary

- [`part-whole hierarchy`](../../GLOSSARY.md#part-whole-hierarchy) — تركيب متكرر فيه مجموعات بتحتوي عناصر أو مجموعات أصغر.
- [`recursive composition`](../../GLOSSARY.md#recursive-composition) — بتبني تركيب من أجزاء بتوفر نفس عقد الكل.
- [`polymorphism`](../../GLOSSARY.md#polymorphism) — نفس العقد (`interface`) يقبل تنفيذات مختلفة (`implementations`). في `C++`، فيه أشكال بتتحدد وقت التشغيل (`runtime`)، وأشكال وقت الترجمة (`compile time`).

## Interview Question

ليه `add` في `Folder` مش `Entry`؟ إضافة طفل لملف معناها إيه؟

## Mini Challenge

ضيف فولدر فاضي ومستوى تداخل كمان، وراجع الأحجام وفكّر في نوع أوسع للأرقام.

## Quick Summary

- **المشكلة:** متصفح الملفات محتاج يحسب حجم ملف أو فولدر جواه فولدرات تانية.
- **الحل:** خلّي الملف `File` والفولدر `Folder` ينفّذوا نفس العقد `Entry`. لحساب الحجم، الفولدر بيسأل كل عنصر جواه عن حجمه؛ القاعدة بتتكرر مع كل مستوى (`recursion`).
- **`Trade-off`:** العمق الكبير ممكن يملأ الـ `Stack`، والجمع ممكن يتجاوز سعة `int`. ماتفرضش عمليات المجموعات على الورق.
- **افتكر:** المجموعة بتجاوب زي عنصر.

[السابق](../../structural/bridge/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/decorator/README.ar-EG.md)
