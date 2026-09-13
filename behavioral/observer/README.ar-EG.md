# Observer

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** بلّغ المشتركين (`Observers`) لما يحصل تغيير في المصدر اللي بيتابعوه (`Subject`).

## المشكلة

تغيير المخزون لازم يحدّث الشاشات المهتمة من غير ما `Stock` تعرف كل نوع شاشة. استدعاء كل مستهلك باسمه بيربط الناشر بالقائمة الحالية، وإضافة مستهلك تحتاج تعديل الناشر.

## الحل ببساطة

كذا شاشة ممكن تحتاج آخر كمية في المخزون.الـ`Observer` بيسمح بالاشتراك، فـ`Stock` يبعت التحديث من غير ما يكتب استدعاء مخصوص لكل شاشة. خلّي المصدر `Stock` يحتفظ بمراجع مش مالكة (`weak references`) للمشتركين من نوع `Listener`. عند التغيير، ابعت التحديث للمشتركين اللي لسه موجودين.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Observer](../../assets/diagrams/observer.svg)

```text
Stock::set()  -->  weak Listener subscriptions  -->  Display::update()
```

في المثال، المصدر هو `Stock`، وعقد استقبال الإشعارات هو `Listener`، والشاشة المشتركة هي `Display`. المستدعي (`Client`) بيمتلك المشتركين. المصدر بيستخدم [`std::weak_ptr`](../../GLOSSARY.md#stdweak_ptr)، وهي مراجع مش مالكة، عشان ما يطوّلش عمر المشتركين.

الأدوار القياسية في المثال ده:

- [`Subject`](../../GLOSSARY.md#subject) — المصدر اللي بيعلن تغييراته للـ `Observers` المسجلين. هنا: `Stock`.
- [`Observer interface`](../../GLOSSARY.md#observer-interface) — عقد `callback` اللي المشتركين بينفذوه. هنا: `Listener`.
- [`Concrete Observer`](../../GLOSSARY.md#concrete-observer) — تنفيذ للمشترك (`Observer implementation`) بيحدد استجابته للإشعارات (`notifications`). هنا: `Display`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Stock:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def set(self, quantity):
        for listener in self.listeners.copy():
            listener(quantity)


def screen(quantity):
    print("Screen:", quantity)


def log(quantity):
    print("Log:", quantity)


def main():
    stock = Stock()
    stock.subscribe(screen)
    stock.subscribe(log)
    stock.set(4)
    stock.unsubscribe(screen)
    stock.set(0)
    stock.unsubscribe(log)
    stock.set(8)
    print("No subscribers")


if __name__ == "__main__":
    main()
```

### Python output

```text
Screen: 4
Log: 4
Log: 0
No subscribers
```

## C++20 example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

struct Listener {
    virtual ~Listener() = default;
    virtual void update(int stock) = 0;
};
class Stock {
    std::vector<std::weak_ptr<Listener>> listeners_;
public:
    void subscribe(const std::shared_ptr<Listener>& listener) { listeners_.push_back(listener); }
    void set(int quantity) {
        std::erase_if(listeners_, [](const auto& item) { return item.expired(); });
        const auto snapshot = listeners_;
        for (const auto& item : snapshot)
            if (auto listener = item.lock()) listener->update(quantity);
    }
};
struct Display final : Listener {
    void update(int stock) override { std::cout << "Stock: " << stock << '\n'; }
};
int main() {
    Stock stock;
    auto display = std::make_shared<Display>();
    stock.subscribe(display);
    stock.set(4);
    display.reset();
    stock.set(0);
    std::cout << "Expired listener skipped\n";
    auto screen = std::make_shared<Display>();
    auto log = std::make_shared<Display>();
    stock.subscribe(screen);
    stock.subscribe(log);
    stock.set(2);
}
```

### C++20 output

```text
Stock: 4
Expired listener skipped
Stock: 2
Stock: 2
```

## قارن اللغتين

Python stores callbacks with strong references and removes them explicitly. C++ uses `weak_ptr` and skips expired listeners. Neither version sends notifications asynchronously. A snapshot makes changes to subscriptions affect the next notification.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما تغيير واحد ليه كذا مستهلك بيسجلوا نفسهم باستقلال.

### Use cases

مناسب لتحديث `UI` والـ `events` المحلية؛ ضمانات الـ `events` الموزعة موضوع تاني.

**التكلفة:** لازم تحدد ترتيب الـ`callbacks` وإيه اللي يحصل لو واحدة رمت `exception`. الإشعارات هنا متزامنة (`synchronous`) ومفيش حماية للـ`threads`. بننسخ قائمة الاشتراكات قبل الإرسال، فإضافة مشترك جديد مش بتغيّر الجولة الحالية. النسخة دي مش بتمنع `callback` من إطلاق إشعار جديد أثناء تنفيذها.

## جرّب تجاوب

1. إيه الفرق بين `unsubscribe` في Python وانتهاء `weak_ptr` في C++؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف مشتركين، امسح واحد، واتأكد إن الباقي بس يستقبل. عرّف عملية إلغاء اشتراك صريحة.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
