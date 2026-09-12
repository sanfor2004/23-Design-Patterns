# 代理

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[上一个](../../structural/flyweight/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/chain-of-responsibility/README.zh-CN.md)

## 类别

结构型

## 难度

中级

## 一句话说明

通过相同接口的替身控制对真实对象的访问。

## 问题

图库可能准备很多图片，但只展示其中几张。

## 最初的简单方案

```cpp
DiskImage image; // loads even if never displayed
```

## 为什么难以维护

立即创建所有重型图片，会在真正显示前做大量不必要的加载。

## 核心思路

LazyImage 实现 Image，在第一次 display 时创建 DiskImage，之后复用。

## 生活类比

图书申请单先代表库房里的书，需要时再由管理员取出。

## 原创结构图

[结构图](diagram.md) · [运行示例](cpp/README.md)

![代理](../../assets/diagrams/proxy.svg)

```text
Client(Image)  -->  LazyImage  -->  DiskImage
```

## 参与者

Image 是共同接口，DiskImage 完成真实工作，LazyImage 拥有延迟创建的对象。

## 现代 C++20 完整可运行示例

```cpp
#include <iostream>
#include <memory>

struct Image {
    virtual ~Image() = default;
    virtual void display() const = 0;
};
struct DiskImage final : Image {
    DiskImage() { std::cout << "Load image\n"; }
    void display() const override { std::cout << "Display image\n"; }
};
class LazyImage final : public Image {
    mutable std::unique_ptr<DiskImage> image_;
public:
    void display() const override {
        if (!image_) image_ = std::make_unique<DiskImage>();
        image_->display();
    }
};
int main() {
    const LazyImage image;
    std::cout << "Proxy ready\n";
    image.display();
    image.display();
}
```

## 预期输出

```text
Proxy ready
Load image
Display image
Display image
```

## 何时使用

适合延迟初始化、访问检查或远程访问，同时希望保留稳定接口的场景。

## 何时不该使用

直接创建很便宜，访问策略也没有价值时，不必代理。

## 优点

调用方沿用 display 接口，创建成本推迟到真正使用。

## 缺点与权衡

首次调用承担加载成本。mutable 表示逻辑常量性，不代表并发 display 安全；加载失败也需要策略。

## 技术应用场景

可用于媒体延迟访问、授权入口和远程对象桩，但失败语义各不相同。

## 相关模式

[decorator](../decorator/README.zh-CN.md) · [adapter](../adapter/README.zh-CN.md)

## 常见混淆

装饰器增加行为；代理控制何时、是否访问目标，类图可能相似。

## 面试问题

加载抛出异常后，下次应重试还是保留失败状态？说明契约。

## 小练习

连续显示三次统计加载次数，再加入首次失败的加载器测试重试策略。

## 小结

- **问题:** 图库可能准备很多图片，但只展示其中几张。
- **方案:** LazyImage 实现 Image，在第一次 display 时创建 DiskImage，之后复用。
- **权衡:** 首次调用承担加载成本。mutable 表示逻辑常量性，不代表并发 display 安全；加载失败也需要策略。
- **记忆提示:** 替身控制真实访问。

[上一个](../../structural/flyweight/README.zh-CN.md) · [类别](../README.zh-CN.md) · [下一个](../../behavioral/chain-of-responsibility/README.zh-CN.md)
