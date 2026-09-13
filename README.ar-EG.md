![Sanfor2004](assets/brand/logo.svg)

# 23 Design Patterns

23 Design Patterns · أربع لغات · أمثلة قابلة للتشغيل · شرح واضح

[Sanfor2004](https://github.com/Sanfor2004) · Python + C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

ابدأ بمشكلة حقيقية. شوف الحل البسيط بيصعّب الدنيا فين. افهم النمط، شغّل Python وC++20، وقرر هل التنظيم الزيادة يستاهل.

- [مسار التعلّم](LEARNING_PATH.ar-EG.md)
- [أمثلة Python](PYTHON_EXAMPLES.md)
- [ورقة المراجعة](CHEATSHEET.ar-EG.md)
- [خريطة العلاقات](PATTERN_MAP.ar-EG.md)
- [مقارنات](COMPARISONS.ar-EG.md)
- [C++20](CPP_EXAMPLES.md)

## طريقتين لدراسة كل Design Pattern

**Python** بيقلّل تفاصيل الكتابة عشان فكرة الـ`Design Pattern` تبقى واضحة. ابدأ بـ[أمثلة Python](PYTHON_EXAMPLES.md)، وشغّل وعدّل بنفسك.

**C++20** بيساعدك تدرس تفاصيل التنفيذ، زي `Ownership` و`Lifetime` و`static typing` و`Runtime dispatch` و`RAII`. قارن النسختين؛ نفس الفكرة مش لازم تستخدم نفس شكل الكود.

اتبع [ترتيب التعلّم](LEARNING_PATH.ar-EG.md): ابدأ بـ`Strategy` و`Observer` و`Factory Method` و`Adapter` و`Decorator`، وكمّل الـ23 لحد `Singleton` في الآخر. كل فولدر فيه `python/` و`cpp/`، ومع كل مثال README والكود والناتج المتوقع.


## ليه الريبو دي موجودة؟

فهم الـ `Patterns` بيبقى أسهل لما تتبّع مشكلة حقيقية في برنامج صغير. هنا هتلاقي السبب والكود والناتج والمقايضات جنب بعض، عشان تعرف إمتى التنظيم الزيادة يستاهل.

## تتنقل إزاي؟

اختار فئة من اللي تحت أو امشي مع مسار التعلّم. كل فولدر نمط فيه أربع ترجمات ورسم وفولدرات `python/` و`cpp/`. روابط اللغات بتفتح نفس النمط باللغة اللي تختارها.

## Creational Pattern

إزاي بننشئ الكائنات؟ المصطلح هنا هو `object creation`.

- [`Abstract Factory`](creational/abstract-factory/README.ar-EG.md) — أنشئ مجموعة كائنات مرتبطة ومتوافقة مع بعض (`family of related objects`) باستخدام `Factory` واحدة. (متوسط)
- [`Builder`](creational/builder/README.ar-EG.md) — جهّز الكائن (`object`) بخطوات أساميها واضحة، وبعدين طلّع النتيجة. (مبتدئ)
- [`Factory Method`](creational/factory-method/README.ar-EG.md) — خلّي الـ `subclass` هي اللي تحدد الـ `concrete object` اللي خطوات الشغل المشتركة (`workflow`) هتستخدمه. (مبتدئ)
- [`Prototype`](creational/prototype/README.ar-EG.md) — انسخ نموذج متجهّز عشان تنشئ كائن مستقل (`object`) وتعدّله من غير ما تغيّر الأصل. (متوسط)
- [`Singleton`](creational/singleton/README.ar-EG.md) — اسمح بوجود نسخة واحدة متاحة من النوع (`instance`)، وخد بالك من تكلفة الحالة العامة المشتركة (`shared global state`). (متوسط)

## Structural Pattern

إزاي بنركّب الكائنات مع بعض؟ المصطلح هنا هو `object composition`.

- [`Adapter`](structural/adapter/README.ar-EG.md) — وفّق طريقة التعامل الحالية (`interface`) مع العقد اللي الكود المستدعي (`Client`) محتاجه. (مبتدئ)
- [`Bridge`](structural/bridge/README.ar-EG.md) — افصل ناحيتين بيتغيروا بشكل مستقل، واربطهم عن طريق التركيب (`composition`). (متوسط)
- [`Composite`](structural/composite/README.ar-EG.md) — عامل العنصر الواحد وشجرة العناصر بنفس العملية. (مبتدئ)
- [`Decorator`](structural/decorator/README.ar-EG.md) — ضيف سلوك جديد (`behavior`) عن طريق كائن بيغلّف الكائن الأصلي، مع الحفاظ على نفس العقد (`interface`). (مبتدئ)
- [`Facade`](structural/facade/README.ar-EG.md) — وفّر مدخل بسيط للخطوات الشائعة جوه نظام فرعي (`subsystem`). (مبتدئ)
- [`Flyweight`](structural/flyweight/README.ar-EG.md) — شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل. (متقدم)
- [`Proxy`](structural/proxy/README.ar-EG.md) — تحكّم في الوصول للكائن (`object`) عن طريق بديل بيوفّر نفس العقد (`interface`). (متوسط)

## Behavioral Pattern

إزاي الكائنات بتتواصل، وإيه اللي بيحدد سلوكها؟ هنركز هنا على `behavior` والتعاون بينها.

- [`Chain of Responsibility`](behavioral/chain-of-responsibility/README.ar-EG.md) — مرّر الطلب على سلسلة معالجات (`Handlers`)؛ كل واحدة تقدر توقفه أو تمرّره للي بعدها. (متوسط)
- [`Command`](behavioral/command/README.ar-EG.md) — مثّل الفعل بكائن (`object`) تقدر تخزنه وتشغّله بعدين. (متوسط)
- [`Interpreter`](behavioral/interpreter/README.ar-EG.md) — مثّل قواعد لغة صغيرة بكائنات (`objects`)، بحيث كل كائن يعرف يقيّم الجزء المسؤول عنه. (متقدم)
- [`Iterator`](behavioral/iterator/README.ar-EG.md) — لف على مجموعة من خلال طريقة وصول ثابتة. (مبتدئ)
- [`Mediator`](behavioral/mediator/README.ar-EG.md) — خلّي التنسيق بين الأطراف المتعاونة (`Colleagues`) مسؤولية منسّق مستقل (`Mediator`). (متوسط)
- [`Memento`](behavioral/memento/README.ar-EG.md) — احفظ حالة الكائن (`state`) عشان تقدر ترجعها بعدين، من غير ما تكشف تفاصيل النسخة المحفوظة. (متوسط)
- [`Observer`](behavioral/observer/README.ar-EG.md) — بلّغ المشتركين (`Observers`) لما يحصل تغيير في المصدر اللي بيتابعوه (`Subject`). (مبتدئ)
- [`State`](behavioral/state/README.ar-EG.md) — خلّي الحالة الحالية للكائن (`state`) هي اللي تحدد استجابته والانتقالات المتاحة ليه. (متوسط)
- [`Strategy`](behavioral/strategy/README.ar-EG.md) — افصل طريقة الحساب (`algorithm`) عن الكائن اللي بيستخدمها، عشان تقدر تختار طريقة بديلة لنفس المهمة. (مبتدئ)
- [`Template Method`](behavioral/template-method/README.ar-EG.md) — ثبّت ترتيب خطوات الحل (`algorithm`)، وسيب تنفيذ خطوات معينة للأنواع المشتقة (`subclasses`). (متوسط)
- [`Visitor`](behavioral/visitor/README.ar-EG.md) — ضيف عمليات جديدة على مجموعة أنواع ثابتة، وحط العمليات دي في `Visitor` منفصلة. (متقدم)

## افهم المشكلة. وبعدها اختار الـ `abstraction`.

النمط فكرة تصميم بتتكرر مع مشكلة معروفة، مش رسمة `classes` ننسخها في كل حتة. ابدأ ببساطة وضيف التنظيم لما تغيير حقيقي يحتاجه.

1. **قابل المشكلة** — مثال ملموس يدي التصميم سبب.
2. **اختبر الحل البسيط** — حدد الربط أو التكرار اللي عامل الصعوبة.
3. **تتبّع التصميم** — تابع مسؤوليات الأجزاء (`responsibilities`)، والملكية (`ownership`)، والمقايضات (`trade-offs`).
4. **شغّل وعدّل Python وC++20** — قارن الناتج وجرّب التحدي واختبر الحدود.

## موارد الريبو

- [المراجع](REFERENCES.md)
- [المساهمة](CONTRIBUTING.md)
- [الترخيص](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

بنترجم الشرح، مش المصطلحات. أسماء الـ `Patterns` والمصطلحات التقنية وأسماء الكود وتعبيرات المقابلات بتفضل بالإنجليزي، ومعاها شرح طبيعي بالمصري.

[`Glossary` — المصطلحات](GLOSSARY.md)
