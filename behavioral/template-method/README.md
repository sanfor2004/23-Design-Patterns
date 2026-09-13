# Template Method

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Keep the sequence and let subclasses fill in steps.

## The problem

Reports share begin, read, format and end steps but vary their data access or formatting. Separate complete report functions duplicate ordering and can drift when a shared step changes.

## The idea

Reports all begin, read data, format it, and finish. Template Method keeps that order in one method while a subclass supplies the changing steps. Report::generate is nonvirtual and calls protected virtual read and format hooks in a fixed order.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Template Method example map](../../assets/diagrams/template-method.svg)

```text
Report::generate()  -->  read() + format()  -->  TextReport overrides
```

Report owns the algorithm skeleton; TextReport implements variation points. The client calls generate through the public workflow. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Report owns the algorithm skeleton; TextReport implements variation points. The client calls generate through the public workflow.

Canonical roles in this example:

- [`Abstract Class`](../../GLOSSARY.md#abstract-class-template-method-role) — The Template Method role that owns the algorithm skeleton and declares variable steps. Here: `Report`.
- [`Concrete Class`](../../GLOSSARY.md#concrete-class-template-method-role) — The Template Method role that supplies the variable steps. Here: `TextReport`.
- [`hook method`](../../GLOSSARY.md#hook-method) — An extension operation called by a fixed workflow; it may have a default implementation. Here: `read, format`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class Report:
    def generate(self):
        print("Begin report")
        data = self.read()
        self.format(data)
        print("End report")

    def read(self):
        raise NotImplementedError

    def format(self, data):
        raise NotImplementedError


class TextReport(Report):
    def read(self):
        return "sales=42"

    def format(self, data):
        print(data)


if __name__ == "__main__":
    TextReport().generate()
```

### Python output

```text
Begin report
sales=42
End report
```

## C++20 example

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Report {
protected:
    virtual std::string read() const = 0;
    virtual void format(std::string_view data) const = 0;
public:
    virtual ~Report() = default;
    void generate() const {
        std::cout << "Begin report\n";
        const auto data = read();
        format(data);
        std::cout << "End report\n";
    }
};
class TextReport final : public Report {
    std::string read() const override { return "sales=42"; }
    void format(std::string_view data) const override { std::cout << data << '\n'; }
};
int main() { TextReport{}.generate(); }
```

### C++20 output

```text
Begin report
sales=42
End report
```

## Compare the languages

Both versions use Inheritance to keep the sequence in `generate` and vary individual steps. C++ marks the steps virtual and keeps the workflow non-virtual. Python can override any method, so keeping the sequence fixed is a design convention. Injected callables are an alternative when Composition fits better.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it for a stable sequence with a few well-defined subclass extension points.

### Use cases

Import pipelines and report generation fit when the skeleton is stable.

**Cost:** Inheritance couples subclasses to the base protocol. End is not guaranteed if read or format throws; use [`RAII`](../../GLOSSARY.md#raii) for real resource cleanup rather than treating the final step as a destructor.

## Check yourself

1. Which method owns the step order, and which methods can vary?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Add CsvReport and verify the begin/end order; then simulate a formatting exception and discuss cleanup.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
