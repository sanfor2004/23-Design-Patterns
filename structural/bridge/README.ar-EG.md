# الجسر

[English](README.md) · [مصري](README.ar-EG.md) · [中文](README.zh-CN.md) · [Italiano](README.it.md)

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)

## الفئة

التركيب

## المستوى

متوسط

## في جملة واحدة

افصل ناحيتين بيتغيروا، واربطهم بالـ Composition.

## المشكلة

التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها.

## حل بسيط في الأول

```cpp
struct UrgentEmailNotice {};
struct UrgentSmsNotice {};
struct NormalEmailNotice {};
struct NormalSmsNotice {};
```

## ليه الحل بيصعّب الدنيا

Class لكل تركيبة أولوية وقناة بتزوّد التركيبات وبتكرر منطق الإرسال.

## الفكرة الأساسية

Notice بتفوّض الإرسال لـ Channel. UrgentNotice بتغيّر الرسالة من غير ما تختار وسيلة النقل.

## مثال من الحياة

الريموت ووصلة الاتصال بتاعته ممكن يتطوروا لوحدهم طالما بينهم بروتوكول صغير.

## رسم توضيحي أصلي

[الرسم التوضيحي](diagram.md) · [شغّل المثال](cpp/README.md)

![الجسر](../../assets/diagrams/bridge.svg)

```text
Notice / UrgentNotice  -->  Channel  -->  Email / Sms
```

## الأدوار

Notice هي التجريد، وUrgentNotice تطوير ليه. Channel عقد الإرسال، وEmail وSms بينفذوه.

## C++20 — مثال كامل قابل للتشغيل

```cpp
#include <iostream>
#include <string_view>

struct Channel {
    virtual ~Channel() = default;
    virtual void deliver(std::string_view text) const = 0;
};
struct Email final : Channel {
    void deliver(std::string_view text) const override { std::cout << "Email: " << text << '\n'; }
};
struct Sms final : Channel {
    void deliver(std::string_view text) const override { std::cout << "SMS: " << text << '\n'; }
};
class Notice {
protected:
    const Channel& channel_;
public:
    explicit Notice(const Channel& channel) : channel_(channel) {}
    virtual ~Notice() = default;
    virtual void send() const { channel_.deliver("status normal"); }
};
class UrgentNotice final : public Notice {
public:
    using Notice::Notice;
    void send() const override { channel_.deliver("URGENT: disk full"); }
};
int main() {
    const Email email;
    const Sms sms;
    Notice{email}.send();
    UrgentNotice{email}.send();
    UrgentNotice{sms}.send();
}
```

## الناتج المتوقع

```text
Email: status normal
Email: URGENT: disk full
SMS: URGENT: disk full
```

## إمتى تستخدمه

استخدمه لما ناحيتين من التغيير هيعملوا عدد كبير من الـ Subclasses لكل التركيبات.

## إمتى ما تستخدموش

بلاش لو فيه ناحية بسيطة واحدة ومتغير لدالة كفاية.

## المميزات

القناة الجديدة تشتغل مع أنواع التنبيه الموجودة من غير Classes لكل تركيبة.

## العيوب والمقايضات

فيه طبقة تفويض زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.

## استخدامات تقنية

مناسب لأشكال رسم مع Backends مختلفة، أو أنواع تنبيه بقنوات متنوعة.

## أنماط مرتبطة

[adapter](../adapter/README.ar-EG.md) · [strategy](../../behavioral/strategy/README.ar-EG.md)

## لخبطة شائعة

Adapter بتصلح عدم توافق موجود. Bridge فصل مقصود لاتجاهين بيتطوروا لوحدهم، وStrategy مركزة على سلوك قابل للتبديل.

## سؤال انترفيو

لو ضفت Push وScheduledNotice، هتحتاج كام Class بالجسر ومن غيره؟

## تحدي صغير

ضيف Push واستخدم نوعي التنبيه من غير تعديلهم.

## الخلاصة

- **المشكلة:** التنبيه بيتغير حسب الأولوية وقناة الإرسال، وكل ناحية محتاجة تتوسع لوحدها.
- **الحل:** Notice بتفوّض الإرسال لـ Channel. UrgentNotice بتغيّر الرسالة من غير ما تختار وسيلة النقل.
- **المقايضة:** فيه طبقة تفويض زيادة، ولازم الحد الفاصل يبقى واضح. القناة المستعارة لازم تعيش أطول من التنبيه.
- **افتكر:** ناحيتين، ووصلة واحدة.

[السابق](../../structural/adapter/README.ar-EG.md) · [الفئة](../README.ar-EG.md) · [التالي](../../structural/composite/README.ar-EG.md)
