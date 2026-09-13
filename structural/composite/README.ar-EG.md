# Composite

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** عامل العنصر الواحد وشجرة العناصر بنفس العملية.

## المشكلة

متصفح الملفات محتاج يحسب حجم ملف أو فولدر جواه فولدرات تانية. الـ `Loops` مخصوصة لكل عمق بتتكسر لما التداخل يزيد، وبتكرر سؤال: ده ملف ولا فولدر؟

## الحل ببساطة

المجلد فيه ملفات ومجلدات تانية.الـ`Composite` بيوفر `bytes` للاتنين، فالمستدعي يطلب الحجم من غير ما يمشي بنفسه في كل مستوى. خلّي الملف `File` والفولدر `Folder` ينفّذوا نفس العقد `Entry`. لحساب الحجم، الفولدر بيسأل كل عنصر جواه عن حجمه؛ القاعدة بتتكرر مع كل مستوى (`recursion`).

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Composite](../../assets/diagrams/composite.svg)

```text
Client::bytes()  -->  Entry  -->  File / Folder[Entry]
```

في المثال، `Entry` بتحدد العملية `bytes`. الملف `File` بيرجع حجمه، والفولدر `Folder` بيجمع أحجام العناصر اللي جواه. الفولدر بيمتلك العناصر باستخدام [`std::unique_ptr`](../../GLOSSARY.md#stdunique_ptr)، عشان تتحرر تلقائيًا معاه.

الأدوار القياسية في المثال ده:

- [`Component`](../../GLOSSARY.md#component) — العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره. هنا: `Entry`.
- [`Leaf`](../../GLOSSARY.md#leaf) — عنصر (`Component`) مافيهوش عناصر تحته. هنا: `File`.
- [`ownership`](../../GLOSSARY.md#ownership) — مين مسؤول يخلي المورد عايش ومين يحرره في الآخر. هنا: `Folder::children_`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class File:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Negative size")
        self.size = size

    def bytes(self):
        return self.size


class Folder:
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def bytes(self):
        return sum(child.bytes() for child in self.children)


def main():
    root = Folder()
    print("Empty:", root.bytes(), "bytes")
    images = Folder()
    images.add(File(20))
    root.add(File(10))
    root.add(images)
    print("Total:", root.bytes(), "bytes")
    try:
        File(-1)
    except ValueError:
        print("Negative size rejected")


if __name__ == "__main__":
    main()
```

### Python output

```text
Empty: 0 bytes
Total: 30 bytes
Negative size rejected
```

## C++20 example

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
    std::cout << "Empty: " << Folder{}.bytes() << " bytes\n";
    try { const File invalid{-1}; }
    catch (const std::invalid_argument&) { std::cout << "Negative size rejected\n"; }
}
```

### C++20 output

```text
Total: 30 bytes
Empty: 0 bytes
Negative size rejected
```

## قارن اللغتين

Python uses a list of Objects that offer `bytes`; C++ uses a common Entry Interface and exclusive Ownership with `unique_ptr`. Python references allow accidental shared children or cycles. Keep this example a tree; garbage collection does not make recursive traversal of a cycle safe.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لشجرة جزء وكل حقيقية، وعملية مفيدة تنفع للورقة والمجموعة.

### Use cases

ينفع لشجر الملفات وقوائم الـ [`interface`](../../GLOSSARY.md#interface) ومشاهد من غير مشاركة عقد.

**التكلفة:** العمق الكبير ممكن يملأ الـ `Stack`، والجمع ممكن يتجاوز سعة `int`. ماتفرضش عمليات المجموعات على الورق.

## جرّب تجاوب

1. ليه `Folder` فاضية تقدر ترجع صفر بنفس الـ`Interface` بتاعة `File`؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف فولدر فاضي ومستوى تداخل كمان، وراجع الأحجام وفكّر في نوع أوسع للأرقام.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
