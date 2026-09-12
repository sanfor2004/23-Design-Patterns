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

## الإنشاء

إزاي الـ Objects بتتعمل

- [المصنع المجرّد](creational/abstract-factory/README.ar-EG.md) — اعمل مجموعة Objects متوافقة من خلال Factory واحدة. (متوسط)
- [البنّاء](creational/builder/README.ar-EG.md) — جهّز Object بخطوات اسمها واضح، وبعدين طلّع النتيجة. (مبتدئ)
- [طريقة المصنع](creational/factory-method/README.ar-EG.md) — خلّي Subclass تختار الـ Object اللي Workflow مشتركة هتستخدمه. (مبتدئ)
- [النموذج الأولي](creational/prototype/README.ar-EG.md) — اعمل Object مستقلة عن طريق نسخ نموذج متجهّز. (متوسط)
- [الكائن الوحيد](creational/singleton/README.ar-EG.md) — قيّد النوع بنسخة واحدة متاحة، مع حساب تكلفة الحالة العامة المشتركة. (متوسط)

## التركيب

إزاي الـ Objects بتركب مع بعض

- [المحوّل](structural/adapter/README.ar-EG.md) — حوّل واجهة موجودة للشكل اللي الـ Client مستنيه. (مبتدئ)
- [الجسر](structural/bridge/README.ar-EG.md) — افصل ناحيتين بيتغيروا، واربطهم بالـ Composition. (متوسط)
- [المركّب](structural/composite/README.ar-EG.md) — عامل العنصر الواحد وشجرة العناصر بنفس العملية. (مبتدئ)
- [المزيّن](structural/decorator/README.ar-EG.md) — ضيف سلوك بإنك تلف Object بواحدة تانية عندها نفس الواجهة. (مبتدئ)
- [الواجهة المبسّطة](structural/facade/README.ar-EG.md) — وفّر مدخل صغير لخطوات شائعة جوه Subsystem. (مبتدئ)
- [الكائن خفيف الوزن](structural/flyweight/README.ar-EG.md) — شارك البيانات الثابتة، وخلي سياق كل ظهور منفصل. (متقدم)
- [الوكيل](structural/proxy/README.ar-EG.md) — تحكّم في الوصول لـ Object عن طريق بديل بنفس الواجهة. (متوسط)

## السلوك

إزاي الـ Objects بتتواصل وتتصرف

- [سلسلة المسؤولية](behavioral/chain-of-responsibility/README.ar-EG.md) — مرّر الطلب على Handlers تقدر توقفه أو تكمّل. (متوسط)
- [الأمر](behavioral/command/README.ar-EG.md) — حوّل الفعل لـ Object تقدر تخزنها وتشغّلها بعدين. (متوسط)
- [المفسّر](behavioral/interpreter/README.ar-EG.md) — مثّل لغة صغيرة بـ Objects بتقيّم قواعدها. (متقدم)
- [المكرّر](behavioral/iterator/README.ar-EG.md) — لف على مجموعة من خلال طريقة وصول ثابتة. (مبتدئ)
- [الوسيط](behavioral/mediator/README.ar-EG.md) — انقل التنسيق بين Objects زميلة لـ Object مخصصة. (متوسط)
- [التذكار](behavioral/memento/README.ar-EG.md) — احفظ حالة Object وارجعها من غير كشف تفاصيل النسخة المحفوظة. (متوسط)
- [المراقب](behavioral/observer/README.ar-EG.md) — بلّغ الـ Objects المشتركة لما الحاجة اللي بيتابعوها تتغير. (مبتدئ)
- [الحالة](behavioral/state/README.ar-EG.md) — خلّي حالة الـ Object الحالية تحدد ردها وانتقالاتها. (متوسط)
- [الاستراتيجية](behavioral/strategy/README.ar-EG.md) — مرّر خوارزمية قابلة للتبديل للـ Object اللي محتاجاها. (مبتدئ)
- [طريقة القالب](behavioral/template-method/README.ar-EG.md) — ثبّت ترتيب الخوارزمية وخلي الـ Subclasses تنفّذ خطوات مختارة. (متوسط)
- [الزائر](behavioral/visitor/README.ar-EG.md) — ضيف عمليات على أنواع عناصر ثابتة عن طريق Visitor منفصلة. (متقدم)

## افهم المشكلة. وبعدها اختار التجريد.

النمط فكرة تصميم بتتكرر مع مشكلة معروفة، مش رسمة Classes ننسخها في كل حتة. ابدأ ببساطة وضيف التنظيم لما تغيير حقيقي يحتاجه.

1. **قابل المشكلة** — مثال ملموس يدي التصميم سبب.
2. **اختبر الحل البسيط** — حدد الربط أو التكرار اللي عامل الصعوبة.
3. **تتبّع التصميم** — تابع المسؤوليات والملكية والمقايضات.
4. **شغّل وعدّل C++** — قارن الناتج وجرّب التحدي واختبر الحدود.

## موارد الريبو

- [المراجع](REFERENCES.md)
- [المساهمة](CONTRIBUTING.md)
- [الترخيص](LICENSE)
- [C++20](CPP_EXAMPLES.md)
