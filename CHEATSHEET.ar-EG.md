# ورقة المراجعة

[دليل الأنماط](README.ar-EG.md)

مساعدة للاختيار بين الـ 23 نمط. «بلاش لما» مهمة زي «استخدمه لما».

| دليل الأنماط | الفئة | استخدمه لما | بلاش لما | طريقة تفتكره |
| --- | --- | --- | --- | --- |
| [`Abstract Factory`](creational/abstract-factory/README.ar-EG.md) | `Creational Pattern` | استخدمه لما كذا نوع من المنتجات لازم يتغيروا مع بعض، والـ `Client` ماينفعش يختار الـ `classes` بنفسه. | بلاش لو عندك نوع واحد ثابت، أو لو الاختيارات المستقلة مطلوبة أصلاً. | طقم متوافق من `Factory` واحدة. |
| [`Builder`](creational/builder/README.ar-EG.md) | `Creational Pattern` | استخدمه لما الخيارات المستقلة كتير، أو محتاج نقطة واضحة لمراجعة الإنشاء. | بلاش مع معاملين واضحين؛ الـ `struct` صغيرة ممكن تكون أبسط. | اختار الخطوات، وبعدها ابنِ. |
| [`Factory Method`](creational/factory-method/README.ar-EG.md) | `Creational Pattern` | استخدمه لما `Workflow` مبنية أصلاً على الـ `inheritance` ومحتاجة نقطة إنشاء قابلة للتوسيع. | بلاش لو تمرير `Sender` جاهزة لـ `function` كفاية؛ الـ `inheritance` ساعتها زيادة. | ثبّت الخطوات، وغيّر الإنشاء. |
| [`Prototype`](creational/prototype/README.ar-EG.md) | `Creational Pattern` | استخدمه لما الـ `objects` الموجودة شايلة إعداد مهم، والـ `Client` مش المفروض يعيد بناء نوعها الفعلي. | بلاش لو النسخ العادي بالقيمة واضح وكافي. | انسخ التجهيز، مش الهوية. |
| [`Singleton`](creational/singleton/README.ar-EG.md) | `Creational Pattern` | فكّر فيه بس لو الـ `instance` الواحدة شرط حقيقي على مستوى العملية وعمرها مناسب. | بلاش لمجرد تسهيل الوصول للـ `dependencies`. مرّر `Metrics reference` صراحة لما الاختبارات محتاجة عزل. | وجود نسخة واحدة (`instance`) مش معناه مشاكل أقل. |
| [`Adapter`](structural/adapter/README.ar-EG.md) | `Structural Pattern` | استخدمه عند التعامل مع `API` موجودة مش قادر أو مش مناسب تغيّرها. | بلاش لو أنت مالك الطرفين وتوحيد الـ `interface` أبسط. | حوّل عند نقطة الاتصال. |
| [`Bridge`](structural/bridge/README.ar-EG.md) | `Structural Pattern` | استخدمه لما ناحيتين من التغيير هيعملوا عدد كبير من الـ `subclasses` لكل التركيبات. | بلاش لو فيه ناحية بسيطة واحدة ومتغير لـ `function` كفاية. | ناحيتين، ووصلة واحدة. |
| [`Composite`](structural/composite/README.ar-EG.md) | `Structural Pattern` | استخدمه لشجرة جزء وكل حقيقية، وعملية مفيدة تنفع للورقة والمجموعة. | بلاش لقائمة مسطحة أو `Graph` فيها مشاركة ودورات؛ الـ `tree ownership` مش هتمثلها صح. | المجموعة بتجاوب زي عنصر. |
| [`Decorator`](structural/decorator/README.ar-EG.md) | `Structural Pattern` | استخدمه لإضافة سلوك اختياري (`behavior`) قابل للتركيب وبيحافظ على عقد العنصر الأصلي. | بلاش لو قائمة مكونات وجمع أسعار كفاية؛ المثال متعمد عشان يوضح التركيب. | نفس العقد، وطبقة زيادة. |
| [`Facade`](structural/facade/README.ar-EG.md) | `Structural Pattern` | استخدمه لما مستدعين كتير محتاجين نفس الجزء المفيد من نظام معقد. | بلاش لو مجرد تمرير لـ `function` من غير تبسيط حقيقي. | باب واحد لكذا خدمة. |
| [`Flyweight`](structural/flyweight/README.ar-EG.md) | `Structural Pattern` | استخدمه بعد قياس تكرار كبير لبيانات ثابتة بين `objects` كتير. | بلاش مع بيانات قليلة أو متغيرة لكل نسخة، أو لو البحث أغلى من التوفير. | شارك الشكل، وافصل المكان. |
| [`Proxy`](structural/proxy/README.ar-EG.md) | `Structural Pattern` | استخدمه للتحميل عند الطلب أو فحص الوصول أو الوصول البعيد مع `interface` ثابتة. | بلاش لو الإنشاء رخيص وسياسة الوصول مش بتضيف قيمة. | بديل بينك وبين الأصل. |
| [`Chain of Responsibility`](behavioral/chain-of-responsibility/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما ترتيب الفحوصات أو اختيارها محتاج تركيب مستقل. | بلاش لو فحصين ثابتين في مكان واحد؛ الشرط الأول أبسط. | عالجه، أو مرّره. |
| [`Command`](behavioral/command/README.ar-EG.md) | `Behavioral Pattern` | استخدمه للأفعال المؤجلة والطوابير والـ `Macros` وتاريخ التراجع. | بلاش لـ `function` بتتنادي مرة ومش محتاجة تخزين نية أو جدولة. | فعل تقدر تحتفظ بيه. |
| [`Interpreter`](behavioral/interpreter/README.ar-EG.md) | `Behavioral Pattern` | استخدمه للغة صغيرة مستقرة، وشجرة التعبير مفيدة للبناء والفحص. | بلاش للغة كبيرة محتاجة `Parser` قوي ورسائل أخطاء وتحسين؛ أدوات `Parsing` جاهزة أنسب. | عقد القواعد بتدي معنى للتعبير. |
| [`Iterator`](behavioral/iterator/README.ar-EG.md) | `Behavioral Pattern` | استخدم `Iterators` أو `Ranges` قياسية عشان تعرض المرور من غير كشف التخزين. | بلاش `Iterator` مخصصة لو `const iterators` موجودة أو `Range` كفاية؛ الـ `implementation` هنا للتعليم. | امشي على البيانات من غير ما تفتح الـ `container`. |
| [`Mediator`](behavioral/mediator/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما قواعد التعامل بين كذا زميل تبدأ تتشابك. | بلاش لـ `callback` واحدة بسيطة أو مكونات مفيش بينها تنسيق حقيقي. | الزملاء يتكلموا عن طريق منسق. |
| [`Memento`](behavioral/memento/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لنقاط رجوع تقدر فيها الـ `object` تحدد نسخة متسقة من الـ `state` بتاعتها. | بلاش لو الـ `state` ضخمة أو الموارد ماينفعش ترجع، أو تسجيل العملية العكسية أرخص. | افتكر الـ `state` من غير ما تكشفها. |
| [`Observer`](behavioral/observer/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما تغيير واحد ليه كذا مستهلك بيسجلوا نفسهم باستقلال. | بلاش لـ `dependency` ثابتة واحدة أو لما محتاج اتساق `Transaction` قوي. | انشر التغيير، وسيب المشترك يرد. |
| [`State`](behavioral/state/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما الـ `behavior` حسب الـ `state` والانتقالات يتوزعوا على كذا عملية. | بلاش لو المطلوب تبديل بسيط (`toggle`)، أو لو جدول صغير باستخدام `enum` بيعبّر عن الحالات بوضوح. | نفس الـ `event`، حالة مختلفة، رد مختلف. |
| [`Strategy`](behavioral/strategy/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما الـ `algorithms` بتتغير باستقلال والـ `Client` محتاج يختار سياسة. | بلاش لـ `algorithm` ثابتة واحدة أو شرط واضح مش محتاج توسعة فعلية. | نفس المهمة، اختار الـ `algorithm`. |
| [`Template Method`](behavioral/template-method/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لتسلسل ثابت فيه نقاط توسعة قليلة وواضحة بالـ `inheritance`. | بلاش لو الخطوات لازم يتغير ترتيبها وقت `runtime` أو الـ `composition` أوضح. | ثبّت الوصفة، وغيّر الخطوات. |
| [`Visitor`](behavioral/visitor/README.ar-EG.md) | `Behavioral Pattern` | استخدمه لما أنواع العناصر ثابتة والعمليات الجديدة كتير. | بلاش لو الأنواع الجديدة بتزيد باستمرار أو كشف تفاصيلها هيكسر الـ `encapsulation`. | أنواع ثابتة، عمليات جديدة. |
