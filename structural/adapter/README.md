# Adapter

[English](README.md) · [مصري](README.ar-EG.md) · [Learning path](../../LEARNING_PATH.md) · [Python](python/main.py) · [C++20](cpp/main.cpp)

**In one sentence:** Make an existing Interface fit another.

## The problem

A dashboard expects Celsius but an existing sensor exposes Fahrenheit. Passing the raw number displays the wrong unit. Scattered conversion formulas duplicate a compatibility rule.

## The idea

A sensor returns Fahrenheit, while the display expects Celsius. Adapter translates the call and value so neither side needs to change. Implement Temperature around a borrowed LegacyThermometer and convert Fahrenheit to Celsius at the boundary.

An **interface** is the behavior a caller expects. The example gives that behavior a clear owner instead of spreading the decision through callers.

## Trace the sketch

![Adapter example map](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

Temperature is the target interface. LegacyThermometer is the existing API. CelsiusAdapter borrows it; display uses only Temperature. The arrows follow this example's calls, not every possible implementation of the pattern. [Open the diagram notes](diagram.md).

## Read the code

Temperature is the target interface. LegacyThermometer is the existing API. CelsiusAdapter borrows it; display uses only Temperature.

Canonical roles in this example:

- [`Target`](../../GLOSSARY.md#target) — The interface expected by the Client. Here: `Temperature`.
- [`Adaptee`](../../GLOSSARY.md#adaptee) — The existing object whose interface needs adaptation. Here: `LegacyThermometer`.
- [`interface`](../../GLOSSARY.md#interface) — The contract of operations and observable behavior offered to a caller. Here: `Temperature`.

Start at the call in `main` or the Python `if __name__ == "__main__"` block. Follow the middle role in the sketch, then compare the printed result. The full sources below are also in [python/main.py](python/main.py) and [cpp/main.cpp](cpp/main.cpp).

## Python example

```python
class LegacyThermometer:
    def fahrenheit(self):
        return 77.0


class CelsiusAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def celsius(self):
        return (self.sensor.fahrenheit() - 32) * 5 / 9


def display(temperature):
    print(temperature.celsius(), "C")


if __name__ == "__main__":
    display(CelsiusAdapter(LegacyThermometer()))
```

### Python output

```text
25.0 C
```

## C++20 example

```cpp
#include <iostream>
#include <stdexcept>

class LegacyThermometer {
public:
    double fahrenheit() const { return 77.0; }
};
struct Temperature {
    virtual ~Temperature() = default;
    virtual double celsius() const = 0;
};
class CelsiusAdapter final : public Temperature {
    const LegacyThermometer& sensor_;
public:
    explicit CelsiusAdapter(const LegacyThermometer& sensor) : sensor_(sensor) {}
    double celsius() const override { return (sensor_.fahrenheit() - 32.0) * 5.0 / 9.0; }
};
void display(const Temperature& temperature) {
    std::cout << temperature.celsius() << " C\n";
}
int main() {
    const LegacyThermometer sensor;
    const CelsiusAdapter adapter{sensor};
    display(adapter);
}
```

### C++20 output

```text
25 C
```

## Compare the languages

Python accepts any Object with `celsius`; C++ declares Temperature as an Interface. The Python Adapter retains its sensor. The C++ reference borrows it, so the sensor must outlive the Adapter.

Both examples assign the same pattern responsibility, although their output or setup may differ. Compare the two expected-output blocks before changing an input.

## When it helps

Use it at a boundary to an existing API you cannot or should not change.

### Use cases

Legacy API integration and unit conversion are common contexts; conversion accuracy and error handling still need explicit contracts.

**Cost:** An adapter can hide semantic mismatches if it only renames methods. The sensor must outlive the adapter because the reference does not own it.

## Check yourself

1. Who converts the units, and who keeps the sensor alive?
2. When would the naive solution on this page be easier to maintain? Give a concrete example.
3. Change one input in the Python example. Predict the output and explain which responsibility handles the change.

Try this change: Test freezing and boiling points by allowing the legacy sensor to return configurable Fahrenheit values.

[All patterns](../../README.md) · [Glossary](../../GLOSSARY.md) · [C++20 build guide](../../CPP_EXAMPLES.md) · [Python guide](../../PYTHON_EXAMPLES.md)
