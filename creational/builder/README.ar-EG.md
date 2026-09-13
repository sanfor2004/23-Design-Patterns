# Builder

[English](README.md) · [مصري](README.ar-EG.md) · [خطة التعلّم](../../LEARNING_PATH.ar-EG.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**الفكرة في سطر:** جهّز الكائن (`object`) بخطوات أساميها واضحة، وبعدين طلّع النتيجة.

## المشكلة

طلب الاتصال (`Request`) فيه عنوان (`Endpoint`)، ومهلة انتظار (`Timeout`)، واختيار لإعادة المحاولة (`Retry`). كل ما الخيارات تزيد، ترتيب المعاملات (`Arguments`) بيبقى أصعب. الـ `constructor` شغال، بس شوية أرقام و `Booleans` جنب بعض مش بيوضحوا المقصود، والغلط في ترتيبهم سهل يفوت.

## الحل ببساطة

الطلب ليه اختيارات كتير، واستدعاء `constructor` طويل بيخلّي معنى القيم مش واضح.الـ`Builder` بيجمع الاختيارات بأسماء واضحة ويراجعها قبل ما يطلع النتيجة. خزّن الاختيارات مؤقتًا في `RequestBuilder`. سمّي كل عملية باسم يوضح الاختيار اللي بتضبطه. في الآخر، الدالة `build` بتراجع القيم وترجع النتيجة من نوع `Request` بالقيمة.

الـ **interface** هو الاتفاق اللي الكود المستدعي متوقعه: هيستدعي إيه، وإيه النتيجة. المثال بيحط المسؤولية دي في مكان واضح بدل ما تتكرر في كل مكان.

## اقرأ الرسمة

![خريطة مثال Builder](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

في المثال، `RequestBuilder` بتجمع الاختيارات وتراجعها. الكائن الناتج، من نوع `Request`، بيمتلك القيم النهائية. المستدعي (`Client`) بيختار ترتيب الخطوات الاختيارية.

الأدوار القياسية في المثال ده:

- [`Product`](../../GLOSSARY.md#product) — الكائن (`object`) النهائي اللي الـ`Builder` بينتجه. هنا: `Request`.
- [`fluent interface`](../../GLOSSARY.md#fluent-interface) — عقد (`interface`) بيسمح تكتب سلسلة استدعاءات بشكل مقروء؛ ده لوحده مش معناه إنك بتستخدم `Builder`. هنا: `RequestBuilder.endpoint().timeout().retry()`.
- [`constructor`](../../GLOSSARY.md#constructor) — العملية الخاصة اللي بتجهّز `instance` جديدة وقت إنشائها. هنا: `Request::Request`.

الأسهم بتوضح مسار المثال ده، مش كل تطبيق ممكن للـ pattern. [شرح الرسمة](diagram.md).

## امشِ مع الكود

ابدأ من `main` في C++ أو من آخر جزء في Python. تابع الدور اللي في نص الرسمة، وبعدين شوف الناتج. الكود الكامل موجود كمان في [ملف Python](python/main.py) و[ملف C++20](cpp/main.cpp).

## Python example

```python
class Request:
    def __init__(self, endpoint, timeout=30, retry=False):
        self.endpoint = endpoint
        self.timeout = timeout
        self.retry = retry

    def describe(self):
        print(f"{self.endpoint} timeout={self.timeout} retry={self.retry}")


class RequestBuilder:
    def __init__(self):
        self.endpoint_value = ""
        self.timeout_value = 30
        self.retry_value = False

    def endpoint(self, value):
        self.endpoint_value = value
        return self

    def timeout(self, seconds):
        self.timeout_value = seconds
        return self

    def retry(self, enabled):
        self.retry_value = enabled
        return self

    def build(self):
        if not self.endpoint_value or self.timeout_value <= 0:
            raise ValueError("Invalid request")
        return Request(self.endpoint_value, self.timeout_value, self.retry_value)


def main():
    RequestBuilder().endpoint("/orders").timeout(5).retry(True).build().describe()
    try:
        RequestBuilder().build()
    except ValueError:
        print("Invalid request rejected")
    try:
        RequestBuilder().endpoint("/orders").timeout(0).build()
    except ValueError:
        print("Zero timeout rejected")


if __name__ == "__main__":
    main()
```

### Python output

```text
/orders timeout=5 retry=True
Invalid request rejected
Zero timeout rejected
```

## C++20 example

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

### C++20 output

```text
/orders timeout=5 retry=1
Invalid request rejected
```

## قارن اللغتين

Named Python arguments often make a Builder unnecessary. This example keeps separate construction steps to show the intent. `build` creates a fresh Request; as in C++, calling the public Request constructor directly bypasses Builder validation. A GoF Director is optional here, and the example builds one representation.

الفكرة واحدة في المثالين، حتى لو تفاصيل اللغة والناتج اختلفت. اقرأ الناتجين قبل ما تغيّر أي قيمة.

## إمتى تستخدمه؟

استخدمه لما الخيارات المستقلة كتير، أو محتاج نقطة واضحة لمراجعة الإنشاء.

### Use cases

مناسب لإعداد `HTTP Requests` وتجهيز بيانات الاختبار؛ المثال مش بيعمل اتصال بالشبكة.

**التكلفة:** فيه نوع زيادة هتصونه. الـ `constructor` بتاعة `Request` هنا عامة؛ في الإنتاج لازم تراجع القيم فيها كمان أو تمنع الوصول المباشر ليها.

## جرّب تجاوب

1. إيه اللي يحصل لو المستدعي استخدم `Request` مباشرة بدل `build`؟
2. إمتى الحل البسيط في الصفحة يبقى أسهل في الصيانة؟ ادّي مثال محدد.
3. غيّر مُدخل واحد في مثال Python. توقّع الناتج واشرح أنهي جزء مسؤول عن التغيير.

**تجربة صغيرة:** ارفض `Timeout` أكبر من 120، وجرّب آخر قيمة مقبولة وأول قيمة مرفوضة.

[كل الأنماط](../../README.ar-EG.md) · [المصطلحات](../../GLOSSARY.md) · [دليل Python](../../PYTHON_EXAMPLES.md) · [دليل C++20](../../CPP_EXAMPLES.md)
