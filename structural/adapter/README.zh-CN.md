# 适配器

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../creational/singleton/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/bridge/README.zh-CN.md)

## 类别

结构型

## 难度

入门

## 一句话说明

把已有接口转换成调用方期待的接口。

## 问题

仪表盘使用摄氏度，旧传感器却返回华氏度。

## 最初的简单方案

```cpp
double displayed = sensor.fahrenheit(); // UI expects Celsius
```

## 为什么难以维护

直接传值会显示错误单位；到处写换算公式又会重复兼容逻辑。

## 核心思路

用 CelsiusAdapter 实现 Temperature，在边界处调用借用的旧传感器并换算。

## 生活类比

旅行插头连接不同插座；这里还需要转换数值含义。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![适配器](../../assets/diagrams/adapter.svg)

```text
display(Temperature)  -->  CelsiusAdapter  -->  LegacyThermometer
```

## 参与者

Temperature 是目标接口，LegacyThermometer 是旧 API，适配器借用传感器，display 只依赖目标接口。

## 现代 C++20 完整可运行示例

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

## 预期输出

```text
25 C
```

## 何时使用

适合不能或不宜修改的已有 API 边界。

## 何时不该使用

双方接口都由你控制，统一接口更简单时，不必适配。

## 优点

换算集中在一处，显示逻辑也能使用其他 Temperature 实现。

## 缺点与权衡

仅改方法名可能掩盖语义差异；引用不拥有传感器，因此传感器必须活得更久。

## 技术应用场景

适合旧 API 集成和单位转换，但精度与错误处理仍需明确约定。

## 相关模式

[facade](../facade/README.zh-CN.md) · [bridge](../bridge/README.zh-CN.md)

## 常见混淆

外观简化子系统；适配器使已有接口满足目标契约。

## 面试问题

如果源接口异步而目标接口同步，适配器总能保持原有行为吗？

## 小练习

让旧传感器返回可配置的华氏温度，测试冰点和沸点。

## 小结

- **问题:** 仪表盘使用摄氏度，旧传感器却返回华氏度。
- **方案:** 用 CelsiusAdapter 实现 Temperature，在边界处调用借用的旧传感器并换算。
- **权衡:** 仅改方法名可能掩盖语义差异；引用不拥有传感器，因此传感器必须活得更久。
- **记忆提示:** 在边界完成转换。

[上一个](../../creational/singleton/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../structural/bridge/README.zh-CN.md)
