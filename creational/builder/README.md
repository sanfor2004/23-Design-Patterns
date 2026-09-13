# Builder

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Build an Object through clear steps.

## The problem

A request has an endpoint, a timeout and a retry option; positional arguments become hard to read as options grow. The constructor works, but calls with several integers and booleans hide intent and make swapped arguments hard to notice.

## The idea

A request has several options, and a long constructor call hides what each value means. Builder collects named choices, checks them, then creates the result. Keep construction state in RequestBuilder. Named methods collect choices; build checks required values and returns a Request by value.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Builder example map](../../assets/diagrams/builder.svg)

```text
Client  -->  RequestBuilder  -->  Request
```

RequestBuilder stores temporary choices and validates them. Request owns the finished values. The client chooses the order of optional steps. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

RequestBuilder stores temporary choices and validates them. Request owns the finished values. The client chooses the order of optional steps.

Canonical roles in this example:

- [`Product`](../../GLOSSARY.md#product) — The finished object produced by the Builder. Here: `Request`.
- [`fluent interface`](../../GLOSSARY.md#fluent-interface) — An interface shaped to read as a chain of calls; it does not by itself imply Builder. Here: `RequestBuilder.endpoint().timeout().retry()`.
- [`constructor`](../../GLOSSARY.md#constructor) — The special operation that initializes a new class instance. Here: `Request::Request`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

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

## Compare the languages

Named Python arguments often make a Builder unnecessary. This example keeps separate construction steps to show the intent. `build` creates a fresh Request; as in C++, calling the public Request constructor directly bypasses Builder validation. A GoF Director is optional here, and the example builds one representation.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for objects with many independent options or a meaningful validation boundary.

### Use cases

HTTP request configuration and test fixture assembly fit; this example performs no network request.

**Cost:** There is an extra type to maintain. This Request constructor remains public, so production invariants would also need constructor validation or restricted access.

## Check yourself

1. What happens if a caller bypasses build and calls Request directly?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Reject timeouts above 120 and demonstrate both the boundary value and the first rejected value.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
