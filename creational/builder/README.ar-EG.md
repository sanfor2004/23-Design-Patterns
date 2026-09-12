# Builder

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../creational/abstract-factory/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/factory-method/README.ar-EG.md)

## Category

[`Creational Pattern`](../../GLOSSARY.md#creational-pattern) — بيركز على إنشاء الكائنات وتجهيزها (`object creation`)، وده واحد من أغراض الـ `Design Patterns`.

## Difficulty

مبتدئ

## In One Sentence

جهّز الكائن (`object`) بخطوات أساميها واضحة، وبعدين طلّع النتيجة.

## The Problem

طلب الاتصال (`Request`) فيه عنوان (`Endpoint`)، ومهلة انتظار (`Timeout`)، واختيار لإعادة المحاولة (`Retry`). كل ما الخيارات تزيد، ترتيب المعاملات (`Arguments`) بيبقى أصعب.

## Naive Solution

```cpp
Request request{"/orders", 5, true}; // what does true mean?
```

## Why It Becomes a Problem

الـ `constructor` شغال، بس شوية أرقام و `Booleans` جنب بعض مش بيوضحوا المقصود، والغلط في ترتيبهم سهل يفوت.

## The Idea

خزّن الاختيارات مؤقتًا في `RequestBuilder`. سمّي كل عملية باسم يوضح الاختيار اللي بتضبطه. في الآخر، الدالة `build` بتراجع القيم وترجع النتيجة من نوع `Request` بالقيمة.

## Real-World Analogy

زي طلب ساندوتش: بتحدد الإضافات قبل ما المطبخ يجهزه.

## Structure

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![Builder](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

## Participants

في المثال، `RequestBuilder` بتجمع الاختيارات وتراجعها. الكائن الناتج، من نوع `Request`، بيمتلك القيم النهائية. المستدعي (`Client`) بيختار ترتيب الخطوات الاختيارية.

الأدوار القياسية في المثال ده:

- [`Product`](../../GLOSSARY.md#product) — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. هنا: `Request`.
- [`fluent interface`](../../GLOSSARY.md#fluent-interface) — عقد (`interface`) بيسمح تكتب سلسلة استدعاءات بشكل مقروء؛ ده لوحده مش معناه إنك بتستخدم `Builder`. هنا: `RequestBuilder.endpoint().timeout().retry()`.
- [`constructor`](../../GLOSSARY.md#constructor) — العملية الخاصة اللي بتجهّز `instance` جديدة وقت إنشائها. هنا: `Request::Request`.

## Modern C++20 Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Request {
    std::string endpoint_;
    int timeout_;
    bool retry_;
public:
    Request(std::string endpoint, int timeout, bool retry)
        : endpoint_(std::move(endpoint)), timeout_(timeout), retry_(retry) {}
    void describe() const {
        std::cout << endpoint_ << " timeout=" << timeout_ << " retry=" << retry_ << '\n';
    }
};
class RequestBuilder {
    std::string endpoint_;
    int timeout_ = 30;
    bool retry_ = false;
public:
    RequestBuilder& endpoint(std::string value) { endpoint_ = std::move(value); return *this; }
    RequestBuilder& timeout(int seconds) { timeout_ = seconds; return *this; }
    RequestBuilder& retry(bool enabled) { retry_ = enabled; return *this; }
    Request build() const {
        if (endpoint_.empty() || timeout_ <= 0) throw std::invalid_argument("Invalid request");
        return Request{endpoint_, timeout_, retry_};
    }
};
int main() {
    const auto request = RequestBuilder{}.endpoint("/orders").timeout(5).retry(true).build();
    request.describe();
    try { static_cast<void>(RequestBuilder{}.build()); }
    catch (const std::invalid_argument&) { std::cout << "Invalid request rejected\n"; }
}
```

## Example Output

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## When to Use

استخدمه لما الخيارات المستقلة كتير، أو محتاج نقطة واضحة لمراجعة الإنشاء.

### Use cases

مناسب لإعداد `HTTP Requests` وتجهيز بيانات الاختبار؛ المثال مش بيعمل اتصال بالشبكة.

## When NOT to Use

بلاش مع معاملين واضحين؛ الـ `struct` صغيرة ممكن تكون أبسط.

## Advantages

مكان الاستدعاء بيوضح النية، وبتقدر ترفض إعداد ناقص قبل إخراج النتيجة.

## Trade-offs

فيه نوع زيادة هتصونه. الـ `constructor` بتاعة `Request` هنا عامة؛ في الإنتاج لازم تراجع القيم فيها كمان أو تمنع الوصول المباشر ليها.

## Related Patterns

[Factory Method](../factory-method/README.ar-EG.md) · [Abstract Factory](../abstract-factory/README.ar-EG.md)

## Common Confusion

الـ `Factory Method` بتختار نوع المنتج جوه `Workflow` موروث. الـ `Builder` بتجمع إعداد النتيجة على كذا خطوة.

## Terms to Remember

- `Builder` — جهّز الكائن (`object`) بخطوات أساميها واضحة، وبعدين طلّع النتيجة.
- `Product` — العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه. مثال: `Request`.
- `fluent interface` — عقد (`interface`) بيسمح تكتب سلسلة استدعاءات بشكل مقروء؛ ده لوحده مش معناه إنك بتستخدم `Builder`. مثال: `RequestBuilder.endpoint().timeout().retry()`.
- `constructor` — العملية الخاصة اللي بتجهّز `instance` جديدة وقت إنشائها. مثال: `Request::Request`.

## Interview Vocabulary

- [`object creation`](../../GLOSSARY.md#object-creation) — اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).
- [`separation of concerns`](../../GLOSSARY.md#separation-of-concerns) — بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.
- [`single responsibility`](../../GLOSSARY.md#single-responsibility) — خلّي الجزء مركز على سبب واحد مترابط للتغيير.

## Interview Question

هل أي `fluent interface` تعتبر `Builder`؟ وضّح فين الإنشاء بينتهي.

## Mini Challenge

ارفض `Timeout` أكبر من 120، وجرّب آخر قيمة مقبولة وأول قيمة مرفوضة.

## Quick Summary

- **المشكلة:** طلب الاتصال (`Request`) فيه عنوان (`Endpoint`)، ومهلة انتظار (`Timeout`)، واختيار لإعادة المحاولة (`Retry`). كل ما الخيارات تزيد، ترتيب المعاملات (`Arguments`) بيبقى أصعب.
- **الحل:** خزّن الاختيارات مؤقتًا في `RequestBuilder`. سمّي كل عملية باسم يوضح الاختيار اللي بتضبطه. في الآخر، الدالة `build` بتراجع القيم وترجع النتيجة من نوع `Request` بالقيمة.
- **`Trade-off`:** فيه نوع زيادة هتصونه. الـ `constructor` بتاعة `Request` هنا عامة؛ في الإنتاج لازم تراجع القيم فيها كمان أو تمنع الوصول المباشر ليها.
- **افتكر:** اختار الخطوات، وبعدها ابنِ.

[السابق](../../creational/abstract-factory/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../creational/factory-method/README.ar-EG.md)
