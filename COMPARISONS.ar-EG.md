# مقارنات

[دليل الأنماط](README.ar-EG.md)

أشكال شبه بعض ممكن تحل مشاكل مختلفة. اختار حسب الهدف، وإيه اللي بيتغير، ومكان الـ responsibility.


## Strategy ↔ State

### المشكلة الأساسية

الاتنين بيفوضوا الـ behavior ؛ Strategy لاختيار algorithm ، وState لرد حسب lifecycle.

### فرق التركيب

Strategy عادة المستدعي بيختارها. State ممكن تبدأ انتقال الـ Context بعد حدث.

### استخدام شائع

اختار رسوم الشحن بـ Strategy، ومثّل باب مفتوح أو مقفول أو متقفل بمفتاح بـ State.

### قاعدة الاختيار

التغيير سببه اختيار سياسة؟ Strategy. حدث بيغيّر مرحلة حياة؟ State.

### مثال تصميم صغير

Checkout → ShippingRule مختارة؛ Door → DoorState حالية → حالة تالية.

[Strategy](behavioral/strategy/README.ar-EG.md) · [State](behavioral/state/README.ar-EG.md)

### افتكر

Strategy بتختار الطريقة؛ State بتربط التصرف بمرحلة الحياة.

## Adapter ↔ Facade

### المشكلة الأساسية

Adapter بتحل عدم توافق interface ، وFacade بتقلل شغل استخدام نظام.

### فرق التركيب

Adapter بتنّفذ العقد المطلوب حوالين API موجودة. Facade بتعرض Workflow أصغر فوق خدمات.

### استخدام شائع

حوّل Fahrenheit ل interface Celsius بـ Adapter، واجمع مخزون ودفع وشحن بـ Facade.

### قاعدة الاختيار

محتاج توافق مع عقد محدد؟ Adapter. محتاج مدخل أبسط؟ Facade، وممكن تستخدم Adapters جواها.

### مثال تصميم صغير

Temperature ← CelsiusAdapter → LegacyThermometer ؛ Client → Checkout → خدمات.

[Adapter](structural/adapter/README.ar-EG.md) · [Facade](structural/facade/README.ar-EG.md)

### افتكر

Adapter بتترجم interface ؛ Facade بتبسّط خطوات شغل.

## Decorator ↔ Proxy

### المشكلة الأساسية

Decorator بتضيف responsibilities ، وProxy بتتحكم في الوصول للأصل.

### فرق التركيب

الاتنين ممكن ينفذوا نفس الـ interface ويفوضوا لعنصر ملفوف. الهدف أدق من الشكل في التفريق.

### استخدام شائع

ضيف سعر اللبن أو ضغط بـ Decorator، وأجّل تحميل صورة أو افحص الوصول بـ Proxy.

### قاعدة الاختيار

الطبقة بتضيف قدرة اختيارية ولا بتحكم الوصول؟ فيه Wrappers ممكن تعمل الاتنين.

### مثال تصميم صغير

Milk(Drink) بتضيف سعر؛ LazyImage بتحدد إمتى DiskImage تتعمل.

[Decorator](structural/decorator/README.ar-EG.md) · [Proxy](structural/proxy/README.ar-EG.md)

### افتكر

Decorator بتزوّد إمكانيات؛ Proxy بتنظّم الوصول.

## Factory Method ↔ Abstract Factory

### المشكلة الأساسية

Factory Method بتغيّر خطوة إنشاء؛ Abstract Factory بتوفر عيلة متوافقة من أنواع منتجات مختلفة.

### فرق التركيب

الأولى عملية قابلة للـ override جوه Workflow. التانية object بتعرض إنشاء منتجات مرتبطة.

### استخدام شائع

اختار Sender جوه AlertJob بالأولى؛ اعمل Button و Panel متوافقين بالتانية.

### قاعدة الاختيار

لو نقطة التوسعة إنشاء منتج جوه خطوات، اختار Factory Method. لو عيلة كاملة قابلة للتبديل، فكّر في Abstract Factory.

### مثال تصميم صغير

AlertJob::run → make_sender()؛ render → Theme.button() + Theme.panel().

[Factory Method](creational/factory-method/README.ar-EG.md) · [Abstract Factory](creational/abstract-factory/README.ar-EG.md)

### افتكر

Factory Method بتغيّر خطوة إنشاء؛ Abstract Factory بتطلّع عيلة متوافقة.

## Builder ↔ Factory Method

### المشكلة الأساسية

Builder بتعالج إعداد معقد؛ Factory Method بتحدد نوع المنتج اللي Workflow بتعمله.

### فرق التركيب

Builder بتجمع حالة على استدعاءات مسماة وبعدين ترجع النتيجة. Factory Method بتختار المنتج بـ override.

### استخدام شائع

جهّز Request بـ Timeout و Retry ؛ أو اختار Sender لخطوات تنبيه مشتركة.

### قاعدة الاختيار

اختيارات إنشاء كتير تشير لـ Builder. اختيار منتج بالـ subclass يشير لـ Factory Method. constructor بسيطة مش محتاجة أي واحدة.

### مثال تصميم صغير

RequestBuilder.endpoint(...).timeout(...).build()؛ EmailJob بتغيّر make_sender().

[Builder](creational/builder/README.ar-EG.md) · [Factory Method](creational/factory-method/README.ar-EG.md)

### افتكر

Builder بتجهّز خطوة خطوة؛ Factory Method بتسيب اختيار المنتج للـ subclass.

## Observer ↔ Mediator

### المشكلة الأساسية

Observer بتوزع إشعارات التغيير؛ Mediator بتنظم تعامل الزملاء.

### فرق التركيب

Observer بتدير اشتراكات من غير قواعد كل مشترك. Mediator عارفة قاعدة التنسيق وأدوار الزملاء.

### استخدام شائع

اذع تغيير المخزون للشاشات؛ أو نسّق الحقول مع إتاحة زر الإرسال.

### قاعدة الاختيار

ردود مستقلة على حدث تشير لـ Observer. قاعدة بتربط زملاء تشير لـ Mediator، وممكن تستقبل إشعارات Observer.

### مثال تصميم صغير

Stock → مشتركين؛ Field → LoginForm → Button.

[Observer](behavioral/observer/README.ar-EG.md) · [Mediator](behavioral/mediator/README.ar-EG.md)

### افتكر

Observer بتعلن التغيير؛ Mediator بتنسّق قاعدة بين أطراف.

## Template Method ↔ Strategy

### المشكلة الأساسية

الاتنين بيعادوا استخدام خطوات مع تغيير behavior ، بس مكان التغيير مختلف.

### فرق التركيب

Template Method بتنادي Hooks في الابن من هيكل موروث ثابت. Strategy بتفوّض لمتعاون أو callable ممررة.

### استخدام شائع

ثبّت ترتيب التقرير بالـ Hooks ، أو بدّل قاعدة الشحن بـ callable.

### قاعدة الاختيار

اختار Template Method لعقد توسعة بالـ inheritance ثابت. Strategy أنسب لو الـ behavior مستقل عن نوع الـ Context.

### مثال تصميم صغير

Report::generate → virtual format()؛ Checkout::total → ShippingRule.

[Template Method](behavioral/template-method/README.ar-EG.md) · [Strategy](behavioral/strategy/README.ar-EG.md)

### افتكر

Template Method بتورّث ترتيب الخطوات؛ Strategy بتستقبل الـ behavior.

## Composite ↔ Decorator

### المشكلة الأساسية

Composite بتمثل علاقة الجزء بالكل؛ Decorator بتضيف behavior لعنصر.

### فرق التركيب

Composite غالباً بتمتلك أطفال كتير وبتجمع عملية. Decorator بتلف واحد وتضيف على الـ delegation.

### استخدام شائع

اجمع أحجام فولدر متداخل بـ Composite؛ ضيف سعر اللبن حوالين Drink بـ Decorator.

### قاعدة الاختيار

مجموعة تتعامل زي ورقة؟ Composite. طبقات اختيارية حوالين واحد؟ Decorator، وممكن تلف Composite كمان.

### مثال تصميم صغير

Folder[File, Folder[File]]؛ Milk(Milk(Coffee)).

[Composite](structural/composite/README.ar-EG.md) · [Decorator](structural/decorator/README.ar-EG.md)

### افتكر

Composite بتجمع عناصر؛ Decorator بتضيف طبقات حوالين عنصر.
