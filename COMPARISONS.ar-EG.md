# مقارنات

[دليل الأنماط](README.ar-EG.md)

أشكال شبه بعض ممكن تحل مشاكل مختلفة. اختار حسب الهدف، وإيه اللي بيتغير، ومكان الـ `responsibility`.


## Strategy ↔ State

### المشكلة الأساسية

الاتنين بيفوضوا الـ `behavior`؛ الـ `Strategy` لاختيار `algorithm`، و `State` لرد حسب `lifecycle`.

### فرق التركيب

الـ `Strategy` عادة المستدعي بيختارها. الـ `State` ممكن تبدأ انتقال الـ `Context` بعد حدث.

### استخدام شائع

اختار رسوم الشحن بـ `Strategy`، ومثّل باب مفتوح أو مقفول أو متقفل بمفتاح بـ `State`.

### قاعدة الاختيار

التغيير سببه اختيار سياسة؟ `Strategy`. حدث بيغيّر مرحلة حياة؟ `State`.

### مثال تصميم صغير

في `Checkout`، المستدعي بيختار طريقة حساب من نوع `ShippingRule`. أما الباب `Door`، فبيفوّض الاستجابة للحالة الحالية `DoorState`، واللي بتحدد الانتقال التالي.

[Strategy](behavioral/strategy/README.ar-EG.md) · [State](behavioral/state/README.ar-EG.md)

### افتكر

الـ `Strategy` بتختار الطريقة؛ الـ `State` بتربط التصرف بمرحلة الحياة.

## Adapter ↔ Facade

### المشكلة الأساسية

الـ `Adapter` بتحل عدم توافق `interface`، و `Facade` بتقلل شغل استخدام نظام.

### فرق التركيب

الـ `Adapter` بتنّفذ العقد المطلوب حوالين `API` موجودة. الـ `Facade` بتعرض `Workflow` أصغر فوق خدمات.

### استخدام شائع

حوّل `Fahrenheit` لعقد بيرجع الدرجة بوحدة `Celsius` بـ `Adapter`، واجمع مخزون ودفع وشحن بـ `Facade`.

### قاعدة الاختيار

محتاج توافق مع عقد محدد؟ `Adapter`. محتاج مدخل أبسط؟ `Facade`، وممكن تستخدم `Adapters` جواها.

### مثال تصميم صغير

طبقة `CelsiusAdapter` بتنفّذ العقد `Temperature` باستخدام الحساس القديم `LegacyThermometer`. أما المستدعي (`Client`) في مثال الشراء، فبيتعامل مع `Checkout` بدل ما ينسّق الخدمات بنفسه.

[Adapter](structural/adapter/README.ar-EG.md) · [Facade](structural/facade/README.ar-EG.md)

### افتكر

الـ `Adapter` بتترجم `interface`؛ الـ `Facade` بتبسّط خطوات شغل.

## Decorator ↔ Proxy

### المشكلة الأساسية

الـ `Decorator` بتضيف `responsibilities`، و `Proxy` بتتحكم في الوصول للأصل.

### فرق التركيب

الاتنين ممكن ينفذوا نفس الـ `interface` ويفوضوا لعنصر ملفوف. الهدف أدق من الشكل في التفريق.

### استخدام شائع

ضيف سعر اللبن أو ضغط بـ `Decorator`، وأجّل تحميل صورة أو افحص الوصول بـ `Proxy`.

### قاعدة الاختيار

الطبقة بتضيف قدرة اختيارية ولا بتحكم الوصول؟ فيه `Wrappers` ممكن تعمل الاتنين.

### مثال تصميم صغير

طبقة `Milk` بتضيف تكلفة على مشروب `Drink`. أما البديل `LazyImage`، فبيحدد إمتى ينشئ الصورة `DiskImage`.

[Decorator](structural/decorator/README.ar-EG.md) · [Proxy](structural/proxy/README.ar-EG.md)

### افتكر

الـ `Decorator` بتزوّد إمكانيات؛ الـ `Proxy` بتنظّم الوصول.

## Factory Method ↔ Abstract Factory

### المشكلة الأساسية

الـ `Factory Method` بتغيّر خطوة إنشاء؛ الـ `Abstract Factory` بتوفر عيلة متوافقة من أنواع منتجات مختلفة.

### فرق التركيب

الأولى عملية قابلة للـ `override` جوه `Workflow`. التانية `object` بتعرض إنشاء منتجات مرتبطة.

### استخدام شائع

اختار `Sender` جوه `AlertJob` بالأولى؛ اعمل `Button` و `Panel` متوافقين بالتانية.

### قاعدة الاختيار

لو نقطة التوسعة إنشاء منتج جوه خطوات، اختار `Factory Method`. لو عيلة كاملة قابلة للتبديل، فكّر في `Abstract Factory`.

### مثال تصميم صغير

الخطوات المشتركة في `AlertJob::run` بتنادي `make_sender()`. أما العرض في `render`، فبيطلب نوعين من المنتجات عن طريق `Theme::button()` و`Theme::panel()`.

[Factory Method](creational/factory-method/README.ar-EG.md) · [Abstract Factory](creational/abstract-factory/README.ar-EG.md)

### افتكر

الـ `Factory Method` بتغيّر خطوة إنشاء؛ الـ `Abstract Factory` بتطلّع عيلة متوافقة.

## Builder ↔ Factory Method

### المشكلة الأساسية

الـ `Builder` بتعالج إعداد معقد؛ الـ `Factory Method` بتحدد نوع المنتج اللي `Workflow` بتعمله.

### فرق التركيب

الـ `Builder` بتجمع حالة على استدعاءات مسماة وبعدين ترجع النتيجة. الـ `Factory Method` بتختار المنتج بـ `override`.

### استخدام شائع

جهّز `Request` بـ `Timeout` و `Retry`؛ أو اختار `Sender` لخطوات تنبيه مشتركة.

### قاعدة الاختيار

اختيارات إنشاء كتير تشير لـ `Builder`. اختيار منتج بالـ `subclass` يشير لـ `Factory Method`. الـ `constructor` بسيطة مش محتاجة أي واحدة.

### مثال تصميم صغير

في `Builder`، بتجهّز الاختيارات وبعدين تطلب النتيجة: `RequestBuilder.endpoint(...).timeout(...).build()`. أما النوع `EmailJob`، فبيغيّر تنفيذ خطوة الإنشاء `make_sender()`.

[Builder](creational/builder/README.ar-EG.md) · [Factory Method](creational/factory-method/README.ar-EG.md)

### افتكر

الـ `Builder` بتجهّز خطوة خطوة؛ الـ `Factory Method` بتسيب اختيار المنتج للـ `subclass`.

## Observer ↔ Mediator

### المشكلة الأساسية

الـ `Observer` بتوزع إشعارات التغيير؛ الـ `Mediator` بتنظم تعامل الزملاء.

### فرق التركيب

الـ `Observer` بتدير اشتراكات من غير قواعد كل مشترك. الـ `Mediator` عارفة قاعدة التنسيق وأدوار الزملاء.

### استخدام شائع

اذع تغيير المخزون للشاشات؛ أو نسّق الحقول مع إتاحة زر الإرسال.

### قاعدة الاختيار

ردود مستقلة على حدث تشير لـ `Observer`. قاعدة بتربط زملاء تشير لـ `Mediator`، وممكن تستقبل إشعارات `Observer`.

### مثال تصميم صغير

المصدر `Stock` بيبلّغ المشتركين بالتغيير. أما الحقل `Field`، فبيبلّغ المنسّق `LoginForm`، وهو اللي بيحدد حالة الزر `Button`.

[Observer](behavioral/observer/README.ar-EG.md) · [Mediator](behavioral/mediator/README.ar-EG.md)

### افتكر

الـ `Observer` بتعلن التغيير؛ الـ `Mediator` بتنسّق قاعدة بين أطراف.

## Template Method ↔ Strategy

### المشكلة الأساسية

الاتنين بيعادوا استخدام خطوات مع تغيير `behavior`، بس مكان التغيير مختلف.

### فرق التركيب

الـ `Template Method` بتنادي `Hooks` في الابن من هيكل موروث ثابت. الـ `Strategy` بتفوّض لمتعاون أو `callable` ممررة.

### استخدام شائع

ثبّت ترتيب التقرير بالـ `Hooks`، أو بدّل قاعدة الشحن بـ `callable`.

### قاعدة الاختيار

اختار `Template Method` لعقد توسعة بالـ `inheritance` ثابت. الـ `Strategy` أنسب لو الـ `behavior` مستقل عن نوع الـ `Context`.

### مثال تصميم صغير

الدالة `Report::generate` بتنادي خطوة تنسيق موروثة هي `format()`. أما `Checkout::total`، فبتفوّض حساب الرسوم لطريقة مستقلة من نوع `ShippingRule`.

[Template Method](behavioral/template-method/README.ar-EG.md) · [Strategy](behavioral/strategy/README.ar-EG.md)

### افتكر

الـ `Template Method` بتورّث ترتيب الخطوات؛ الـ `Strategy` بتستقبل الـ `behavior`.

## Composite ↔ Decorator

### المشكلة الأساسية

الـ `Composite` بتمثل علاقة الجزء بالكل؛ الـ `Decorator` بتضيف `behavior` لعنصر.

### فرق التركيب

الـ `Composite` غالباً بتمتلك أطفال كتير وبتجمع عملية. الـ `Decorator` بتلف واحد وتضيف على الـ `delegation`.

### استخدام شائع

اجمع أحجام فولدر متداخل بـ `Composite`؛ ضيف سعر اللبن حوالين `Drink` بـ `Decorator`.

### قاعدة الاختيار

مجموعة تتعامل زي ورقة؟ `Composite`. طبقات اختيارية حوالين واحد؟ `Decorator`، وممكن تلف `Composite` كمان.

### مثال تصميم صغير

الفولدر `Folder` ممكن يحتوي ملف `File` وفولدر تاني جواه ملفات. أما مشروب `Coffee`، فممكن تلفّه بطبقتين من `Milk`؛ كل طبقة بتضيف على اللي جواها.

[Composite](structural/composite/README.ar-EG.md) · [Decorator](structural/decorator/README.ar-EG.md)

### افتكر

الـ `Composite` بتجمع عناصر؛ الـ `Decorator` بتضيف طبقات حوالين عنصر.
