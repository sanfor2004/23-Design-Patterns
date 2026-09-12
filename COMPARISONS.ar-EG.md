# مقارنات

[دليل الأنماط](README.ar-EG.md)

أشكال شبه بعض ممكن تحل مشاكل مختلفة. اختار حسب الهدف، وإيه اللي بيتغير، ومكان المسؤولية.


## الاستراتيجية ↔ الحالة

### المشكلة الأساسية

الاتنين بيفوضوا السلوك؛ Strategy لاختيار خوارزمية، وState لرد حسب دورة الحياة.

### فرق التركيب

Strategy عادة المستدعي بيختارها. State ممكن تبدأ انتقال السياق بعد حدث.

### استخدام شائع

اختار رسوم الشحن بـ Strategy، ومثّل باب مفتوح أو مقفول أو متقفل بمفتاح بـ State.

### قاعدة الاختيار

التغيير سببه اختيار سياسة؟ Strategy. حدث بيغيّر مرحلة حياة؟ State.

### مثال تصميم صغير

Checkout → ShippingRule مختارة؛ Door → DoorState حالية → حالة تالية.

[الاستراتيجية](behavioral/strategy/README.ar-EG.md) · [الحالة](behavioral/state/README.ar-EG.md)

### افتكر

Strategy بتختار الطريقة؛ State بتربط التصرف بمرحلة الحياة.

## المحوّل ↔ الواجهة المبسّطة

### المشكلة الأساسية

Adapter بتحل عدم توافق واجهة، وFacade بتقلل شغل استخدام نظام.

### فرق التركيب

Adapter بتنّفذ العقد المطلوب حوالين API موجودة. Facade بتعرض Workflow أصغر فوق خدمات.

### استخدام شائع

حوّل Fahrenheit لواجهة Celsius بـ Adapter، واجمع مخزون ودفع وشحن بـ Facade.

### قاعدة الاختيار

محتاج توافق مع عقد محدد؟ Adapter. محتاج مدخل أبسط؟ Facade، وممكن تستخدم Adapters جواها.

### مثال تصميم صغير

Temperature ← CelsiusAdapter → LegacyThermometer؛ Client → Checkout → خدمات.

[المحوّل](structural/adapter/README.ar-EG.md) · [الواجهة المبسّطة](structural/facade/README.ar-EG.md)

### افتكر

Adapter بتترجم واجهة؛ Facade بتبسّط خطوات شغل.

## المزيّن ↔ الوكيل

### المشكلة الأساسية

Decorator بتضيف مسؤوليات، وProxy بتتحكم في الوصول للأصل.

### فرق التركيب

الاتنين ممكن ينفذوا نفس الواجهة ويفوضوا لعنصر ملفوف. الهدف أدق من الشكل في التفريق.

### استخدام شائع

ضيف سعر اللبن أو ضغط بـ Decorator، وأجّل تحميل صورة أو افحص الوصول بـ Proxy.

### قاعدة الاختيار

الطبقة بتضيف قدرة اختيارية ولا بتحكم الوصول؟ فيه Wrappers ممكن تعمل الاتنين.

### مثال تصميم صغير

Milk(Drink) بتضيف سعر؛ LazyImage بتحدد إمتى DiskImage تتعمل.

[المزيّن](structural/decorator/README.ar-EG.md) · [الوكيل](structural/proxy/README.ar-EG.md)

### افتكر

Decorator بتزوّد إمكانيات؛ Proxy بتنظّم الوصول.

## طريقة المصنع ↔ المصنع المجرّد

### المشكلة الأساسية

Factory Method بتغيّر خطوة إنشاء؛ Abstract Factory بتوفر عيلة متوافقة من أنواع منتجات مختلفة.

### فرق التركيب

الأولى عملية قابلة للـ Override جوه Workflow. التانية Object بتعرض إنشاء منتجات مرتبطة.

### استخدام شائع

اختار Sender جوه AlertJob بالأولى؛ اعمل Button وPanel متوافقين بالتانية.

### قاعدة الاختيار

لو نقطة التوسعة إنشاء منتج جوه خطوات، اختار Factory Method. لو عيلة كاملة قابلة للتبديل، فكّر في Abstract Factory.

### مثال تصميم صغير

AlertJob::run → make_sender()؛ render → Theme.button() + Theme.panel().

[طريقة المصنع](creational/factory-method/README.ar-EG.md) · [المصنع المجرّد](creational/abstract-factory/README.ar-EG.md)

### افتكر

Factory Method بتغيّر خطوة إنشاء؛ Abstract Factory بتطلّع عيلة متوافقة.

## البنّاء ↔ طريقة المصنع

### المشكلة الأساسية

Builder بتعالج إعداد معقد؛ Factory Method بتحدد نوع المنتج اللي Workflow بتعمله.

### فرق التركيب

Builder بتجمع حالة على استدعاءات مسماة وبعدين ترجع النتيجة. Factory Method بتختار المنتج بـ Override.

### استخدام شائع

جهّز Request بـ Timeout وRetry؛ أو اختار Sender لخطوات تنبيه مشتركة.

### قاعدة الاختيار

اختيارات إنشاء كتير تشير لـ Builder. اختيار منتج بالـ Subclass يشير لـ Factory Method. Constructor بسيطة مش محتاجة أي واحدة.

### مثال تصميم صغير

RequestBuilder.endpoint(...).timeout(...).build()؛ EmailJob بتغيّر make_sender().

[البنّاء](creational/builder/README.ar-EG.md) · [طريقة المصنع](creational/factory-method/README.ar-EG.md)

### افتكر

Builder بتجهّز خطوة خطوة؛ Factory Method بتسيب اختيار المنتج للـ Subclass.

## المراقب ↔ الوسيط

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

[المراقب](behavioral/observer/README.ar-EG.md) · [الوسيط](behavioral/mediator/README.ar-EG.md)

### افتكر

Observer بتعلن التغيير؛ Mediator بتنسّق قاعدة بين أطراف.

## طريقة القالب ↔ الاستراتيجية

### المشكلة الأساسية

الاتنين بيعادوا استخدام خطوات مع تغيير سلوك، بس مكان التغيير مختلف.

### فرق التركيب

Template Method بتنادي Hooks في الابن من هيكل موروث ثابت. Strategy بتفوّض لمتعاون أو Callable ممررة.

### استخدام شائع

ثبّت ترتيب التقرير بالـ Hooks، أو بدّل قاعدة الشحن بـ Callable.

### قاعدة الاختيار

اختار Template Method لعقد توسعة بالوراثة ثابت. Strategy أنسب لو السلوك مستقل عن نوع السياق.

### مثال تصميم صغير

Report::generate → virtual format()؛ Checkout::total → ShippingRule.

[طريقة القالب](behavioral/template-method/README.ar-EG.md) · [الاستراتيجية](behavioral/strategy/README.ar-EG.md)

### افتكر

Template Method بتورّث ترتيب الخطوات؛ Strategy بتستقبل السلوك.

## المركّب ↔ المزيّن

### المشكلة الأساسية

Composite بتمثل علاقة الجزء بالكل؛ Decorator بتضيف سلوك لعنصر.

### فرق التركيب

Composite غالباً بتمتلك أطفال كتير وبتجمع عملية. Decorator بتلف واحد وتضيف على التفويض.

### استخدام شائع

اجمع أحجام فولدر متداخل بـ Composite؛ ضيف سعر اللبن حوالين Drink بـ Decorator.

### قاعدة الاختيار

مجموعة تتعامل زي ورقة؟ Composite. طبقات اختيارية حوالين واحد؟ Decorator، وممكن تلف Composite كمان.

### مثال تصميم صغير

Folder[File, Folder[File]]؛ Milk(Milk(Coffee)).

[المركّب](structural/composite/README.ar-EG.md) · [المزيّن](structural/decorator/README.ar-EG.md)

### افتكر

Composite بتجمع عناصر؛ Decorator بتضيف طبقات حوالين عنصر.
