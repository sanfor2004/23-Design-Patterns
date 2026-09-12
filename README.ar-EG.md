![Sanfor2004](assets/brand/logo.svg)

# Design-Patterns-23

23 Patterns · 4 Languages · Real Examples · Simple Explanations

[Sanfor2004](https://github.com/Sanfor2004) · C++20

[English](README.md) · [العربية المصرية](README.ar-EG.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md)

ابدأ بمشكلة حقيقية. شوف الحل البسيط بيصعّب الدنيا فين. افهم النمط، شغّل C++، وقرر هل التنظيم الزيادة يستاهل.

- [مسار التعلّم](LEARNING_PATH.ar-EG.md)
- [ورقة المراجعة](CHEATSHEET.ar-EG.md)
- [خريطة العلاقات](PATTERN_MAP.ar-EG.md)
- [مقارنات](COMPARISONS.ar-EG.md)
- [C++20](CPP_EXAMPLES.md)

## ليه الريبو دي موجودة؟

فهم الـ Patterns بيبقى أسهل لما تتبّع مشكلة حقيقية في برنامج صغير. هنا هتلاقي السبب والكود والناتج والمقايضات جنب بعض، عشان تعرف إمتى التنظيم الزيادة يستاهل.

## تتنقل إزاي؟

اختار فئة من اللي تحت أو امشي مع مسار التعلّم. كل فولدر نمط فيه أربع ترجمات ورسم وفولدر `cpp/`. روابط اللغات بتفتح نفس النمط باللغة اللي تختارها.

## Creational Pattern

إزاي الـ objects بتتعمل

- [Abstract Factory](creational/abstract-factory/README.ar-EG.md) — اعمل مجموعة objects متوافقة من خلال Factory واحدة. (متوسط)
- [Builder](creational/builder/README.ar-EG.md) — جهّز object بخطوات اسمها واضح، وبعدين طلّع النتيجة. (مبتدئ)
- [Factory Method](creational/factory-method/README.ar-EG.md) — خلّي subclass تختار الـ object اللي Workflow مشتركة هتستخدمه. (مبتدئ)
- [Prototype](creational/prototype/README.ar-EG.md) — اعمل object مستقلة عن طريق نسخ نموذج متجهّز. (متوسط)
- [Singleton](creational/singleton/README.ar-EG.md) — قيّد النوع بـ instance واحدة متاحة، مع حساب تكلفة الـ shared global state. (متوسط)

## Structural Pattern

إزاي الـ objects بتركب مع بعض

- [Adapter](structural/adapter/README.ar-EG.md) — حوّل interface موجودة للشكل اللي الـ Client مستنيه. (مبتدئ)
- [Bridge](structural/bridge/README.ar-EG.md) — افصل ناحيتين بيتغيروا، واربطهم بالـ composition. (متوسط)
- [Composite](structural/composite/README.ar-EG.md) — عامل العنصر الواحد وشجرة العناصر بنفس العملية. (مبتدئ)
- [Decorator](structural/decorator/README.ar-EG.md) — ضيف behavior بإنك تلف object بواحدة تانية عندها نفس الـ interface. (مبتدئ)
- [Facade](structural/facade/README.ar-EG.md) — وفّر مدخل صغير لخطوات شائعة جوه Subsystem. (مبتدئ)
- [Flyweight](structural/flyweight/README.ar-EG.md) — شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل. (متقدم)
- [Proxy](structural/proxy/README.ar-EG.md) — تحكّم في الوصول لـ object عن طريق بديل بنفس الـ interface. (متوسط)

## Behavioral Pattern

إزاي الـ objects بتتواصل وتتصرف

- [Chain of Responsibility](behavioral/chain-of-responsibility/README.ar-EG.md) — مرّر الطلب على Handlers تقدر توقفه أو تكمّل. (متوسط)
- [Command](behavioral/command/README.ar-EG.md) — حوّل الفعل لـ object تقدر تخزنها وتشغّلها بعدين. (متوسط)
- [Interpreter](behavioral/interpreter/README.ar-EG.md) — مثّل لغة صغيرة بـ objects بتقيّم قواعدها. (متقدم)
- [Iterator](behavioral/iterator/README.ar-EG.md) — لف على مجموعة من خلال طريقة وصول ثابتة. (مبتدئ)
- [Mediator](behavioral/mediator/README.ar-EG.md) — انقل التنسيق بين objects زميلة لـ object مخصصة. (متوسط)
- [Memento](behavioral/memento/README.ar-EG.md) — احفظ state بتاعة object وارجعها من غير كشف تفاصيل النسخة المحفوظة. (متوسط)
- [Observer](behavioral/observer/README.ar-EG.md) — بلّغ الـ objects المشتركة لما الحاجة اللي بيتابعوها تتغير. (مبتدئ)
- [State](behavioral/state/README.ar-EG.md) — خلّي state بتاعة الـ object الحالية تحدد ردها وانتقالاتها. (متوسط)
- [Strategy](behavioral/strategy/README.ar-EG.md) — مرّر algorithm قابلة للتبديل للـ object اللي محتاجاها. (مبتدئ)
- [Template Method](behavioral/template-method/README.ar-EG.md) — ثبّت ترتيب الـ algorithm وخلي الـ subclasses تنفّذ خطوات مختارة. (متوسط)
- [Visitor](behavioral/visitor/README.ar-EG.md) — ضيف عمليات على أنواع عناصر ثابتة عن طريق Visitor منفصلة. (متقدم)

## افهم المشكلة. وبعدها اختار الـ abstraction.

النمط فكرة تصميم بتتكرر مع مشكلة معروفة، مش رسمة classes ننسخها في كل حتة. ابدأ ببساطة وضيف التنظيم لما تغيير حقيقي يحتاجه.

1. **قابل المشكلة** — مثال ملموس يدي التصميم سبب.
2. **اختبر الحل البسيط** — حدد الربط أو التكرار اللي عامل الصعوبة.
3. **تتبّع التصميم** — تابع ال responsibilities والملكية والمقايضات.
4. **شغّل وعدّل C++** — قارن الناتج وجرّب التحدي واختبر الحدود.

## موارد الريبو

- [المراجع](REFERENCES.md)
- [المساهمة](CONTRIBUTING.md)
- [الترخيص](LICENSE)
- [C++20](CPP_EXAMPLES.md)

## Terminology policy

بنترجم الشرح، مش المصطلحات. أسماء الـ Patterns والمصطلحات التقنية وأسماء الكود وتعبيرات المقابلات بتفضل بالإنجليزي، ومعاها شرح طبيعي بالمصري.

[Glossary — المصطلحات](GLOSSARY.md)
