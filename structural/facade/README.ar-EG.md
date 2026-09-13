# Facade

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** وفّر مدخل بسيط للخطوات الشائعة جوه نظام فرعي (`subsystem`).

## المشكلة

كل مستدعي للشراء محتاج يراجع المخزون ويدفع ويطلب الشحن بالترتيب الصح. الاستدعاءات المباشرة ممكن تنسى المخزون أو تكرر ترتيب الخطوات بشكل مختلف.

## الحل ببساطة

الشراء محتاج مراجعة مخزون ودفع وشحن بالترتيب.الـ`Facade` بيجمع الخطوات المشتركة في استدعاء واحد، بس مش بيحوّلها تلقائيًا لـ`Transaction`. وفّر عملية شراء واحدة اسمها `buy` في `Checkout`. جوه العملية، نسّق الخدمات الداخلية بالترتيب المطلوب.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Facade](../../assets/diagrams/facade.svg)

```text
Client  -->  Checkout::buy()  -->  Stock / Payment / Shipping
```

في المثال، مراجعة المخزون مسؤولية `Stock`، والدفع مسؤولية `Payment`، والشحن مسؤولية `Shipping`. المدخل المشترك `Checkout` بيرتب الخطوات دي للمستدعي.

الأدوار القياسية في المثال ده:

- [`subsystem`](../../GLOSSARY.md#subsystem) — مجموعة خدمات أو `objects` بتتعاون جوه نظام أكبر. هنا: `Stock, Payment, Shipping`.
- [`interface`](../../GLOSSARY.md#interface) — العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها. هنا: `Checkout::buy`.
- [`Client`](../../GLOSSARY.md#client-pattern-role) — الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`. هنا: `main`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Stock:
    def available(self, quantity):
        return 0 < quantity <= 3


class Payment:
    def charge(self, amount_cents):
        print("Charged", amount_cents, "cents")


class Shipping:
    def dispatch(self):
        print("Dispatched")


class Checkout:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.shipping = Shipping()

    def buy(self, quantity):
        if not self.stock.available(quantity):
            return False
        self.payment.charge(quantity * 1000)
        self.shipping.dispatch()
        return True


if __name__ == "__main__":
    checkout = Checkout()
    checkout.buy(2)
    if not checkout.buy(4):
        print("Unavailable")
    if not checkout.buy(0):
        print("Invalid quantity")
```

### Python output

```text
Charged 2000 cents
Dispatched
Unavailable
Invalid quantity
```

## C++20 example

```cpp
// Monetary amounts in this example are integer cents.
#include <iostream>

struct Stock {
    bool available(int quantity) const { return quantity > 0 && quantity <= 3; }
};
struct Payment {
    void charge(int amount_cents) const { std::cout << "Charged " << amount_cents << '\n'; }
};
struct Shipping {
    void dispatch() const { std::cout << "Dispatched\n"; }
};
class Checkout {
    Stock stock_;
    Payment payment_;
    Shipping shipping_;
public:
    bool buy(int quantity) const {
        if (!stock_.available(quantity)) return false;
        payment_.charge(quantity * 10);
        shipping_.dispatch();
        return true;
    }
};
int main() {
    const Checkout checkout{};
    if (!checkout.buy(2)) return 1;
    if (!checkout.buy(4)) std::cout << "Unavailable\n";
}
```

### C++20 output

```text
Charged 20
Dispatched
Unavailable
```

## قارن اللغتين

Both versions put the same small workflow behind `buy`. C++ stores service Objects by value; Python holds references. Neither example implements a transaction: a real shipping failure after payment needs an explicit recovery policy.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما مستدعين كتير محتاجين نفس الجزء المفيد من نظام معقد.

### Use cases

مناسب لمداخل `SDK` وحدود خدمات التطبيق؛ مفيش تكامل دفع حقيقي هنا.

**التكلفة:** الـ `Facade` ممكن تكبر وتعمل كل حاجة. المثال مش `Transaction`: فشل الدفع أو الشحن الحقيقي محتاج تعويض أو طريقة اتساق مناسبة.

## جرّب تجاوب

1. إيه اللي `buy` مش بيضمنه لو الشحن فشل بعد الدفع؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ضيف فشل شحن تجريبي وصمّم نتيجة `Refund` واضحة بدل نجاح وهمي.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
