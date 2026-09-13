# Glossary

[23 Design Patterns](README.md)

Translate the explanation, not the terminology. English labels are shared across English and Egyptian Arabic. Pattern roles refer to the examples linked from each article; a role is not always a separate class.

Use your editor or browser’s Find command to locate a term. Lowercase `state` describes an object’s condition; `State` names the Design Pattern. Likewise, lowercase `iterator` is a traversal object and `Iterator` is the pattern.

## Design Pattern

**Meaning:** A reusable design idea for a recurring problem, not code to copy unchanged.

**مصري:** فكرة تصميم بتتكرر مع نوع مشكلة معروف؛ مش كود تنقله زي ما هو.



## Creational Pattern

**Meaning:** A Design Pattern concerned with how objects are created and configured.

**مصري:** بيركز على إنشاء الكائنات وتجهيزها (`object creation`)، وده واحد من أغراض الـ `Design Patterns`.



## Structural Pattern

**Meaning:** A Design Pattern concerned with how objects and classes fit together.

**مصري:** بيركز على تركيب الكائنات والأنواع (`objects` و`classes`)، وده واحد من أغراض الـ `Design Patterns`.



## Behavioral Pattern

**Meaning:** A Design Pattern concerned with behavior and collaboration among objects.

**مصري:** بيركز على السلوك (`behavior`) والتعاون بين الكائنات (`objects`)، وده واحد من أغراض الـ `Design Patterns`.



## abstraction

**Meaning:** A view that exposes the operations a caller needs while hiding irrelevant details.

**مصري:** بتظهر العمليات اللي المستدعي محتاجها وبتخفي التفاصيل اللي مش محتاج يعرفها.



## interface

**Meaning:** The contract of operations and observable behavior offered to a caller.

**مصري:** العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها.



## implementation

**Meaning:** The concrete code that fulfills an interface or performs an operation.

**مصري:** الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد `interface`.



## composition

**Meaning:** Building behavior by connecting objects that use or contain other objects.

**مصري:** بتبني السلوك (`behavior`) عن طريق كائنات متعاونة (`objects`)، كل واحد منها بيستخدم أو بيحتوي كائنات تانية.



## inheritance

**Meaning:** Defining a derived class from a base class to reuse or specialize its contract and implementation.

**مصري:** بتبني نوع مشتق (`derived class`) على أساس نوع موجود (`base class`)، عشان تعيد استخدام العقد أو تخصصه.



## encapsulation

**Meaning:** Keeping representation and invariants behind controlled operations.

**مصري:** بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.



## polymorphism

**Meaning:** Using one interface with different implementations; C++ supports runtime and compile-time forms.

**مصري:** نفس العقد (`interface`) يقبل تنفيذات مختلفة (`implementations`). في `C++`، فيه أشكال بتتحدد وقت التشغيل (`runtime`)، وأشكال وقت الترجمة (`compile time`).



## coupling

**Meaning:** The degree to which changing one part requires knowledge of or changes to another.

**مصري:** قد إيه جزء مرتبط بجزء تاني لدرجة إن تغييره يحتاج معرفة أو تعديل الجزء التاني.



## tight coupling

**Meaning:** Parts depend heavily on each other's concrete details, so changes tend to spread.

**مصري:** الأجزاء معتمدة بقوة على التفاصيل الداخلية لبعض، فالتغيير في واحد بينتشر للباقي.



## loose coupling

**Meaning:** Parts know only the small contracts needed to cooperate, limiting change propagation.

**مصري:** كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.



## cohesion

**Meaning:** How closely the responsibilities within a module belong together.

**مصري:** قد إيه مسؤوليات الجزء الواحد مرتبطة ببعض وبتخدم غرض واضح.



## dependency

**Meaning:** Something a piece of code needs in order to work.

**مصري:** حاجة جزء من الكود محتاجها عشان يشتغل.



## dependency injection

**Meaning:** Supplying a dependency from outside instead of choosing or constructing it inside the consumer.

**مصري:** بتمرّر `dependency` من بره بدل ما الجزء اللي بيستخدمها يختارها أو يعملها بنفسه.



## delegation

**Meaning:** An object asks a collaborator to perform part of its work.

**مصري:** الكائن بيفوّض جزء من شغله لكائن متعاون معاه (`object`)، بدل ما ينفّذ كل حاجة بنفسه.



## responsibility

**Meaning:** A job or obligation assigned to a part of a design.

**مصري:** شغل أو التزام جزء معين في التصميم مسؤول عنه.



## separation of concerns

**Meaning:** Keeping distinct kinds of responsibility apart so they can change independently.

**مصري:** بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.



## object composition

**Meaning:** Connecting objects to form a larger behavior or structure.

**مصري:** بتوصل الكائنات (`objects`) ببعض عشان تبني سلوك متكامل (`behavior`) أو تركيب أكبر.



## object

**Meaning:** An entity with identity and lifetime; in C++, an object occupies storage.

**مصري:** كيان له هوية و `lifetime`؛ في `C++` الـ `object` بتشغل مساحة تخزين.



## class

**Meaning:** A C++ user-defined type that groups data and operations.

**مصري:** نوع بتعرّفه في `C++` وبتجمع فيه بيانات وعمليات مرتبطة.



## instance

**Meaning:** A particular object of a type.

**مصري:** كائن محدد (`object`) من نوع معين.



## client

**Meaning:** Code that uses an interface or collaborates with a pattern's objects.

**مصري:** الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`.



## concrete class

**Meaning:** A class that can be instantiated and supplies the required operations.

**مصري:** الـ `class` ينفع تعمل منها `instance` وبتوفر العمليات المطلوبة.



## abstract class

**Meaning:** A class that cannot be instantiated directly, typically because some virtual operations are pure.

**مصري:** الـ `class` ما ينفعش تعمل منها `instance` مباشرة؛ غالباً فيها عمليات `pure virtual`.



## base class

**Meaning:** The class from which another class inherits.

**مصري:** الـ `class` اللي `class` تانية بتورّث منها.



## derived class

**Meaning:** A class that inherits from a base class; also called a subclass.

**مصري:** الـ `class` بتورّث من `base class`، واسمها كمان `subclass`.



## constructor

**Meaning:** The special operation that initializes a new class instance.

**مصري:** العملية الخاصة اللي بتجهّز `instance` جديدة وقت إنشائها.



## destructor

**Meaning:** The special operation run when a class instance's lifetime ends.

**مصري:** العملية الخاصة اللي بتتنفذ لما `lifetime` بتاعة `instance` تنتهي.



## method

**Meaning:** An operation associated with an object or class; usually a member function in C++.

**مصري:** عملية مرتبطة بـ `object` أو `class`؛ غالباً `member function` في `C++`.



## function

**Meaning:** A callable unit of code with a declared input and result contract.

**مصري:** جزء كود تقدر تناديه، وله مدخلات ونتيجة متفق عليهم.



## callback

**Meaning:** A function or operation supplied to be called when another operation needs it.

**مصري:** دالة (`function`) أو عملية بتمرّرها لجزء تاني، عشان يناديها وقت ما يحتاجها.



## event

**Meaning:** An occurrence that code can react to, such as an input or state change.

**مصري:** حاجة حصلت والكود ممكن يرد عليها، زي مدخل جديد أو تغيير `state`.



## state

**Meaning:** The information that describes an object's current condition.

**مصري:** المعلومات اللي بتوصف وضع الـ `object` دلوقتي.



## behavior

**Meaning:** What an object or operation does in response to input and state.

**مصري:** اللي `object` أو عملية بتعمله بناءً على المدخلات والـ `state`.



## algorithm

**Meaning:** A defined procedure for solving a class of problems.

**مصري:** خطوات محددة لحل نوع معين من المشاكل.



## runtime

**Meaning:** The period when a compiled program is executing.

**مصري:** الوقت اللي البرنامج فيه شغال بعد البناء.



## compile time

**Meaning:** The period when source code is checked and translated into a program.

**مصري:** المرحلة اللي فيها `source code` بيتراجع وبيتحول لبرنامج.



## memory allocation

**Meaning:** Obtaining storage for data; its cost and failure behavior depend on the mechanism.

**مصري:** حجز مساحة للبيانات؛ تكلفته وطريقة فشله حسب الآلية المستخدمة.



## ownership

**Meaning:** Responsibility for keeping a resource alive and eventually releasing it.

**مصري:** مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.



## lifetime

**Meaning:** The interval during which an object exists and may be used according to its rules.

**مصري:** الفترة اللي الـ `object` موجودة فيها وينفع تستخدمها حسب قواعدها.



## smart pointer

**Meaning:** An object that wraps pointer access with a lifetime or ownership policy.

**مصري:** الـ `object` بتغلف `pointer` ومعاها قواعد واضحة للـ `ownership` أو `lifetime`.



## RAII

**Meaning:** Resource Acquisition Is Initialization: tie resource ownership to object lifetime so destruction releases it.

**مصري:** اربط المورد بعمر الكائن، عشان `destructor` تحرره تلقائياً؛ والاسم الكامل هو `Resource Acquisition Is Initialization`.



## STL

**Meaning:** Standard Template Library: the generic containers, iterators, and algorithms associated with the C++ standard library.

**مصري:** `Standard Template Library`: الـ `containers` والـ `iterators` والـ `algorithms` العامة المرتبطة بمكتبة `C++` القياسية.



## container

**Meaning:** An object that stores a collection of elements.

**مصري:** الـ `object` بتخزّن مجموعة عناصر.



## iterator

**Meaning:** An object representing a traversal position and the operations valid at that position.

**مصري:** الـ `object` بتمثل مكانك أثناء المرور والعمليات المسموحة في المكان ده.



## template

**Meaning:** A C++ facility for defining families of types or functions parameterized at compile time.

**مصري:** وسيلة في `C++` لتعريف عيلة `types` أو `functions` بمعاملات بتتحدد وقت `compile time`.



## generic programming

**Meaning:** Writing algorithms against requirements on types rather than one concrete type.

**مصري:** بتكتب `algorithms` على أساس متطلبات النوع بدل ما تربطها بنوع واحد.



## trade-off

**Meaning:** A benefit gained at the cost of another desirable property.

**مصري:** ميزة بتكسبها قصاد تكلفة أو تنازل في ناحية تانية.



## use case

**Meaning:** A concrete situation in which a design is useful.

**مصري:** موقف محدد التصميم بينفع فيه.



## extensibility

**Meaning:** How readily new behavior can be added without disrupting existing code.

**مصري:** سهولة إضافة `behavior` جديدة من غير ما تلخبط الكود الموجود.



## maintainability

**Meaning:** How readily code can be understood, corrected, and changed over time.

**مصري:** سهولة فهم الكود وتصليحه وتعديله مع الوقت.



## testability

**Meaning:** How readily behavior can be isolated, exercised, and checked.

**مصري:** سهولة عزل `behavior` وتشغيلها والتأكد من نتيجتها.



## scalability

**Meaning:** How a system handles growth in workload or data with added resources.

**مصري:** قدرة النظام يتعامل مع زيادة الشغل أو البيانات لما تزود موارده.



## refactoring

**Meaning:** Changing internal structure while preserving externally observable behavior.

**مصري:** بتغيّر تركيب الكود من جوه مع الحفاظ على `behavior` اللي باينة للمستخدم.



## anti-pattern

**Meaning:** A recurring approach whose apparent convenience repeatedly leads to poor outcomes in a context.

**مصري:** حل بيتكرر وشكله مريح، بس بيؤدي لمشاكل متكررة في سياق معين.



## code smell

**Meaning:** A sign worth investigating, not automatic proof that code is wrong.

**مصري:** علامة تستاهل تراجع الكود بسببها، مش دليل لوحدها إن الكود غلط.



## composition over inheritance

**Meaning:** Prefer collaborating objects when they express variation more clearly than extending a class hierarchy.

**مصري:** فضّل تركيب الحل من كائنات متعاونة (`objects`)، لما ده يكون أوضح من توسيع شجرة الوراثة (`inheritance`).



## program to an interface, not an implementation

**Meaning:** Depend on the promised contract instead of a particular concrete implementation.

**مصري:** اعتمد على العقد المعلن بدل تفاصيل `implementation` بعينها.



## favor loose coupling

**Meaning:** Limit knowledge of concrete collaborators to reduce how far changes spread.

**مصري:** قلّل معرفة كل جزء بتفاصيل اللي بيتعاون معاهم عشان التغيير ما ينتشرش.



## encapsulate what varies

**Meaning:** Put a changing design decision behind a stable boundary.

**مصري:** حط القرار اللي بيتغير ورا حدود ثابتة وواضحة.



## single responsibility

**Meaning:** Keep a module focused on one coherent reason to change.

**مصري:** خلّي الجزء مركز على سبب واحد مترابط للتغيير.



## Single Responsibility Principle

**Meaning:** Organize a module around one responsibility so unrelated change pressures do not mix.

**مصري:** نظّم الجزء حوالين `responsibility` واحدة عشان أسباب التغيير المختلفة ما تتخلطش.



## Open/Closed Principle

**Meaning:** Aim for open for extension, closed for modification at a useful, chosen boundary.

**مصري:** خلّي التوسيع ممكن من غير تعديل الكود المستقر، عند حدود مختارة بوضوح. التعبير هو `open for extension, closed for modification`.



## open for extension, closed for modification

**Meaning:** Add intended variations through extension points without editing stable client logic.

**مصري:** ضيف التغييرات المقصودة من نقاط توسعة بدل تعديل منطق `client` المستقر.



## dependency inversion

**Meaning:** High-level policy and low-level details depend on abstractions rather than policy depending directly on details.

**مصري:** السياسة العامة والتفاصيل يعتمدوا على `abstractions` بدل ما السياسة تتربط بالتفاصيل مباشرة.



## SOLID

**Meaning:** A group of five object-oriented design principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

**مصري:** خمس مبادئ للتصميم: `Single Responsibility` و `Open`/`Closed` و `Liskov Substitution` و `Interface Segregation` و `Dependency Inversion`.



## object creation

**Meaning:** Choosing a concrete type and establishing an object's initial values and lifetime.

**مصري:** اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).



## runtime behavior

**Meaning:** What the program does while executing, including behavior selected from runtime input.

**مصري:** اللي البرنامج بيعمله وهو شغال، بما فيه `behavior` بتتحدد من المدخلات.



## compile-time dependency

**Meaning:** A dependency needed to compile a unit of code, such as a type declaration in a header.

**مصري:** الـ `dependency` لازمة عشان تترجم جزء كود، زي تعريف نوع في `header`.



## interchangeable behavior

**Meaning:** Different behaviors that can be supplied through the same contract.

**مصري:** سلوكيات مختلفة (`behaviors`) تقدر تختار أي واحدة منها من خلال نفس العقد.



## encapsulate an algorithm

**Meaning:** Put an algorithm behind an operation that hides its internal steps.

**مصري:** حط `algorithm` ورا عملية بتخفي خطواتها الداخلية.



## runtime selection

**Meaning:** Choosing an implementation while the program is executing.

**مصري:** اختيار `implementation` والبرنامج شغال.



## type erasure

**Meaning:** Hiding a concrete type behind a uniform runtime interface, as std::function does for callables.

**مصري:** بتخفي النوع الفعلي ورا `interface` موحدة وقت `runtime`، زي `std::function` مع `callables`.



## one-to-many dependency

**Meaning:** One source has multiple dependents that react to its changes.

**مصري:** مصدر واحد ليه أكتر من طرف بيتأثروا بتغييره.



## subscription lifetime

**Meaning:** The interval in which a listener is registered and eligible for notification.

**مصري:** الفترة اللي المستمع فيها مسجل وينفع توصله `notification`.



## state transition

**Meaning:** A move from one modeled condition to another after an event.

**مصري:** انتقال من وضع ممثّل في التصميم لوضع تاني بعد `event`.



## algorithm skeleton

**Meaning:** The fixed sequence of an algorithm whose selected steps can vary.

**مصري:** ترتيب `algorithm` الثابت اللي بعض خطواته ممكن تتغير.



## hook method

**Meaning:** An extension operation called by a fixed workflow; it may have a default implementation.

**مصري:** عملية للتوسعة بتناديها خطوات ثابتة، وممكن يكون ليها `implementation` افتراضية.



## double dispatch

**Meaning:** Selecting behavior using two runtime types; classic Visitor combines two virtual calls with overload resolution.

**مصري:** اختيار `behavior` بناءً على نوعين وقت `runtime`؛ الـ `Visitor` التقليدية بتجمع نداءين `virtual` مع `overload resolution`.



## overload resolution

**Meaning:** Compile-time selection among functions with the same name using the argument types.

**مصري:** اختيار `function` من كذا واحدة بنفس الاسم حسب أنواع المعاملات وقت `compile time`.



## deep copy

**Meaning:** Copying owned nested data so the new object does not share that mutable data with the original.

**مصري:** بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل.



## value semantics

**Meaning:** Copies behave as independent values according to the type's contract.

**مصري:** النسخ تتعامل كقيم مستقلة حسب عقد النوع.



## global state

**Meaning:** Data reachable broadly across a program whose changes can affect distant code.

**مصري:** بيانات أجزاء كتير تقدر توصلها، وتغييرها ممكن يأثر على كود بعيد.



## thread-safe initialization

**Meaning:** Initialization protected against concurrent construction; it does not make later operations thread-safe.

**مصري:** حماية التهيئة من الإنشاء المتزامن؛ مش معناها إن كل العمليات بعد كده `thread-safe`.



## fluent interface

**Meaning:** An interface shaped to read as a chain of calls; it does not by itself imply Builder.

**مصري:** عقد (`interface`) بيسمح تكتب سلسلة استدعاءات بشكل مقروء؛ ده لوحده مش معناه إنك بتستخدم `Builder`.



## intrinsic state

**Meaning:** Data independent of an occurrence's context that a Flyweight can share.

**مصري:** بيانات مستقلة عن مكان الاستخدام، فالـ `Flyweight` تقدر تشاركها.



## extrinsic state

**Meaning:** Per-occurrence data kept outside a shared Flyweight.

**مصري:** بيانات تخص كل استخدام وبتفضل بره الـ `Flyweight` المشتركة.



## interning

**Meaning:** Reusing one representation for equivalent values through a lookup pool.

**مصري:** بتعيد استخدام تمثيل واحد للقيم المتساوية عن طريق `pool` للبحث.



## lazy initialization

**Meaning:** Deferring creation until the value or resource is first needed.

**مصري:** بتأجل الإنشاء لأول مرة تحتاج فيها القيمة أو المورد.



## part-whole hierarchy

**Meaning:** A recursive structure in which groups contain leaves or smaller groups.

**مصري:** تركيب متكرر فيه مجموعات بتحتوي عناصر أو مجموعات أصغر.



## recursive composition

**Meaning:** Building a structure from parts that expose the same contract as the whole.

**مصري:** بتبني تركيب من أجزاء بتوفر نفس عقد الكل.



## chain termination

**Meaning:** The rule for stopping a chain and deciding what happens after the last handler.

**مصري:** القاعدة اللي بتحدد السلسلة تقف إمتى وإيه يحصل بعد آخر `Handler`.



## undo

**Meaning:** Restoring an earlier logical result, using saved state or an inverse operation when possible.

**مصري:** بترجع لنتيجة سابقة باستخدام `state` محفوظة أو عملية عكسية لما ينفع.



## exception safety

**Meaning:** The guarantees an operation preserves if it fails by throwing an exception.

**مصري:** الضمانات اللي العملية بتحافظ عليها لو فشلت ورمت `exception`.



## snapshot

**Meaning:** A captured representation of selected state at a point in time.

**مصري:** صورة محفوظة لجزء محدد من `state` في لحظة معينة.



## abstract syntax tree

**Meaning:** A tree representing grammatical structure rather than the original text's surface formatting.

**مصري:** شجرة بتمثل تركيب القواعد بدل الشكل المكتوب للنص.



## short-circuit evaluation

**Meaning:** Skipping later operands when an earlier result already determines the answer.

**مصري:** بتتخطى باقي المعاملات لما نتيجة بدري تكون حسمت الإجابة.



## iterator invalidation

**Meaning:** An operation makes an iterator no longer valid for its intended use.

**مصري:** عملية بتخلي `iterator` ما بقتش صالحة للاستخدام المقصود.



## forward iterator

**Meaning:** An iterator supporting forward traversal and the multipass guarantee, allowing independent copies to traverse the same range.

**مصري:** أداة مرور (`iterator`) بتتحرك لقدام، وبتدعم المرور المستقل أكتر من مرة (`multipass`). يعني نسخها المستقلة تقدر تمر على نفس النطاق.



## god object

**Meaning:** An object accumulating too many unrelated responsibilities.

**مصري:** كائن (`object`) بيجمع مسؤوليات كتير مالهاش علاقة قوية ببعض.



## UML

**Meaning:** Unified Modeling Language, a notation family for describing software structure and interactions.

**مصري:** `Unified Modeling Language`: طرق رسم لوصف تركيب البرامج والتفاعلات بينها.



## class diagram

**Meaning:** A structural diagram showing classes, their contracts, and relationships.

**مصري:** رسم بيوضح `classes` وعقودها والعلاقات بينها.



## sequence diagram

**Meaning:** A diagram showing interactions in their execution order.

**مصري:** رسم بيوضح التفاعلات بالترتيب اللي بتحصل بيه.



## lifecycle

**Meaning:** The modeled stages and transitions of a domain entity, distinct from a C++ object's lifetime.

**مصري:** المراحل والانتقالات اللي بنمثلها لكيان في المشكلة؛ مش نفس `lifetime` بتاعة `object` في `C++`.



## std::unique_ptr

**Meaning:** A smart pointer with exclusive ownership that releases its object when the owner is destroyed.

**مصري:** مؤشر ذكي (`smart pointer`) بملكية حصرية؛ بيحرر الكائن لما المالك يتدمر.



## std::shared_ptr

**Meaning:** A smart pointer sharing ownership; the managed object is released when the last owning reference disappears.

**مصري:** مؤشر ذكي (`smart pointer`) بيشارك الملكية (`ownership`)؛ الكائن بيتحرر لما آخر مرجع مالك يختفي.



## std::weak_ptr

**Meaning:** A non-owning observer of shared ownership; lock attempts to obtain a temporary shared_ptr.

**مصري:** مرجع مش مالك لملكية مشتركة؛ الـ `lock` بتحاول تجيب `shared_ptr` مؤقتة.



## std::vector

**Meaning:** A standard container storing elements contiguously with a size that can change.

**مصري:** الـ `container` قياسية بتخزن العناصر جنب بعض وحجمها ممكن يتغير.



## std::function

**Meaning:** A type-erased wrapper that stores a callable with a chosen signature.

**مصري:** الـ `Wrapper` بتخزن `callable` بتوقيع محدد وبتخفي نوعها الفعلي.



## virtual

**Meaning:** A C++ keyword enabling derived implementations to be selected through a base interface.

**مصري:** كلمة `C++` بتسمح باختيار `implementation` من `derived class` من خلال `interface` الأساس.



## override

**Meaning:** A C++ specifier asking the compiler to verify that a method overrides a base virtual method.

**مصري:** محدد في `C++` بيطلب من المترجم يتأكد إن `method` بتعيد تعريف `virtual method` في الأساس.



## const

**Meaning:** A C++ qualifier restricting modification through a particular access path; it is not a thread-safety guarantee.

**مصري:** محدد بيقيّد التعديل من طريق وصول معين؛ مش ضمان لأمان التزامن.



## type

**Meaning:** A specification of the values and operations supported by an entity.

**مصري:** وصف للقيم والعمليات اللي الكيان بيدعمها.



## pointer

**Meaning:** A value that can refer to an object or function; a raw pointer does not by itself express ownership.

**مصري:** قيمة ممكن تشير لـ `object` أو `function`؛ الـ `raw pointer` لوحدها ما بتحددش `ownership`.



## reference

**Meaning:** An alias referring to an existing entity, not ownership by itself.

**مصري:** اسم بديل لكيان موجود، مش `ownership` لوحده.



## callable

**Meaning:** Something invocable with function-call syntax, such as a lambda or function object.

**مصري:** حاجة ينفع تناديها بصيغة `function`، زي `lambda` أو `function object`.



## lambda

**Meaning:** A C++ expression that creates a callable and may capture surrounding values.

**مصري:** تعبير `C++` بيعمل `callable` وممكن يحتفظ بقيم من حواليه.



## Product

**Meaning:** The object a creation pattern produces. Some patterns also define a common Product interface.

**مصري:** الكائن (`object`) اللي نمط الإنشاء بينتجه. بعض الأنماط بتحدد له `Product interface` مشترك.



## Concrete Product

**Meaning:** A particular implementation of a Product contract.

**مصري:** تنفيذ فعلي (`implementation`) لعقد المنتج (`Product`).



## Concrete Factory

**Meaning:** An implementation that creates one matching Product family.

**مصري:** تنفيذ فعلي (`implementation`) بينشئ عيلة منتجات متوافقة (`Product family`).



## Creator

**Meaning:** The base role that owns a workflow and declares its creation operation.

**مصري:** الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها.



## Concrete Creator

**Meaning:** A Creator subclass that supplies a particular Product.

**مصري:** نوع مشتق (`subclass`) من `Creator`، مسؤول عن إنشاء منتج معين (`Product`).



## Concrete Prototype

**Meaning:** An object whose clone operation produces another object from its configured values.

**مصري:** كائن بيوفّر العملية `clone` لإنشاء كائن تاني (`object`) من القيم المتجهّزة.



## Target

**Meaning:** The interface expected by the Client.

**مصري:** الـ `interface` اللي `Client` متوقع يتعامل معاها.



## Adaptee

**Meaning:** The existing object whose interface needs adaptation.

**مصري:** الـ `object` الموجودة اللي `interface` بتاعتها محتاجة تتوافق مع المطلوب.



## Abstraction (Bridge role)

**Meaning:** The high-level side of Bridge that delegates implementation work.

**مصري:** الناحية اللي بتوفر العمليات الأساسية في `Bridge` وبتفوّض شغل التنفيذ.



## Refined Abstraction

**Meaning:** A specialization of Abstraction independent of the implementation side.

**مصري:** تخصيص لـ `Abstraction` مستقل عن ناحية التنفيذ.



## Implementor

**Meaning:** The contract used by a Bridge Abstraction for lower-level work.

**مصري:** العقد اللي `Abstraction` بتستخدمه للشغل في الناحية التانية من `Bridge`.



## Concrete Implementor

**Meaning:** A particular implementation of the Implementor contract.

**مصري:** تنفيذ محدد (`implementation`) لعقد `Implementor`.



## Component

**Meaning:** The common contract exposed by leaves, groups, or wrappers.

**مصري:** العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره.



## Leaf

**Meaning:** A Component with no child Components.

**مصري:** عنصر (`Component`) مافيهوش عناصر تحته.



## Concrete Component

**Meaning:** The basic implementation before optional wrappers are added.

**مصري:** الـ `implementation` الأساسية قبل إضافة طبقات اختيارية.



## Concrete Decorator

**Meaning:** A wrapper that keeps the Component contract and adds a specific responsibility.

**مصري:** طبقة تغليف (`Wrapper`) بتحافظ على عقد `Component`، وبتضيف مسؤولية محددة (`responsibility`).



## subsystem

**Meaning:** A group of cooperating services or objects within a larger system.

**مصري:** مجموعة خدمات أو `objects` بتتعاون جوه نظام أكبر.



## Flyweight Factory

**Meaning:** A lookup service that returns a shared Flyweight for a key.

**مصري:** جزء بيبحث بالمفتاح ويرجع `Flyweight` مشتركة.



## Subject interface

**Meaning:** The shared contract offered by a Proxy and its Real Subject.

**مصري:** العقد المشترك اللي `Proxy` و `Real Subject` بيوفروه.



## Real Subject

**Meaning:** The object that does the work behind a Proxy.

**مصري:** الـ `object` اللي بتنفذ الشغل الحقيقي ورا `Proxy`.



## Handler

**Meaning:** A role that handles a request or passes it to its successor.

**مصري:** دور بيعمل معالجة للطلب أو يبعته للي بعده.



## Concrete Handler

**Meaning:** A Handler implementing one particular processing rule.

**مصري:** معالج (`Handler`) بينفّذ قاعدة معينة.



## Receiver

**Meaning:** The object that performs the work requested by a Command.

**مصري:** الـ `object` اللي بيتنفذ عليها الشغل المطلوب من `Command`.



## Invoker

**Meaning:** The role that starts or stores Commands without knowing each operation's details.

**مصري:** الدور اللي بيشغّل `Commands` أو بيخزنها من غير معرفة تفاصيل كل عملية.



## Concrete Command

**Meaning:** A Command implementation that binds a Receiver and an action.

**مصري:** تنفيذ للأمر (`Command implementation`) بيربط الفعل المطلوب بالجهة اللي هتنفّذه (`Receiver`).



## Abstract Expression

**Meaning:** The contract for evaluating nodes in an Interpreter grammar.

**مصري:** عقد تقييم العقد اللي بتمثل قواعد `Interpreter`.



## Terminal Expression

**Meaning:** An expression with no child expressions.

**مصري:** تعبير مافيش جواه تعبيرات أطفال.



## Nonterminal Expression

**Meaning:** An expression that combines child expressions according to a grammar rule.

**مصري:** تعبير بيركب تعبيرات أصغر حسب قاعدة في اللغة.



## Context

**Meaning:** In Strategy and State, the object that uses a Strategy or delegates behavior to its current State. In Interpreter, the data expressions consult during evaluation, such as variable values or available roles.

**مصري:** في `Strategy` و `State`، دي الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). في `Interpreter`، ده البيانات اللي الـ `expressions` بترجع لها وقت التقييم، زي قيم المتغيرات أو الأدوار المتاحة.



## Aggregate

**Meaning:** The collection that provides access to iterators.

**مصري:** المجموعة اللي بتوفر `iterators` للمرور عليها.



## Concrete Iterator

**Meaning:** An implementation that stores a traversal position for a particular Aggregate.

**مصري:** تنفيذ (`implementation`) بيحفظ موضع المرور في مجموعة محددة (`Aggregate`).



## Colleague

**Meaning:** An object whose interactions are coordinated by a Mediator.

**مصري:** كائن متعاون (`object`) بيتولى الـ `Mediator` تنسيق تعاملاته مع باقي الأطراف.



## Concrete Mediator

**Meaning:** An implementation that contains the coordination rules for its Colleagues.

**مصري:** تنفيذ (`implementation`) بيجمع قواعد التنسيق بين الأطراف المتعاونة (`Colleagues`).



## Originator

**Meaning:** The object that knows how to capture and restore its own state.

**مصري:** الكائن اللي يعرف يحفظ حالته (`state`) ويسترجعها.



## Caretaker

**Meaning:** The role that keeps a Memento without inspecting its private representation.

**مصري:** الدور اللي بيحتفظ بـ `Memento` من غير ما يفتش في تمثيلها الداخلي.



## Subject

**Meaning:** The publisher whose changes are announced to registered Observers.

**مصري:** المصدر اللي بيعلن تغييراته للـ `Observers` المسجلين.



## Concrete Observer

**Meaning:** An Observer implementation that reacts to notifications.

**مصري:** تنفيذ للمشترك (`Observer implementation`) بيحدد استجابته للإشعارات (`notifications`).



## Strategy interface

**Meaning:** The contract for interchangeable algorithms used by a Context.

**مصري:** بتحدد العقد المشترك للـ`algorithms` المختلفة. الـ`Context` بيعتمد على العقد ده بدل `implementation` محدد.



## Concrete Strategy

**Meaning:** A particular implementation of a Strategy interface, possibly a callable rather than a class.

**مصري:** تنفيذ محدد لعقد `Strategy interface`. ممكن تمثّله بحاجة قابلة للاستدعاء (`callable`)، ومش لازم يكون `class` مستقلة.



## Concrete State

**Meaning:** An implementation defining behavior and transitions for one State.

**مصري:** تنفيذ لحالة معينة (`Concrete State`) بيحدد سلوكها (`behavior`) والانتقالات المتاحة منها.



## Abstract Class (Template Method role)

**Meaning:** The Template Method role that owns the algorithm skeleton and declares variable steps.

**مصري:** دور `Template Method` اللي ماسك `algorithm skeleton` وبيعلن الخطوات المتغيرة.



## Concrete Class (Template Method role)

**Meaning:** The Template Method role that supplies the variable steps.

**مصري:** دور `Template Method` اللي بيوفر الخطوات المتغيرة.



## Element

**Meaning:** The contract for objects that accept a Visitor.

**مصري:** عقد الـ `objects` اللي بتقبل `Visitor`.



## Concrete Element

**Meaning:** An Element implementation that selects its matching Visitor overload.

**مصري:** تنفيذ للعنصر (`Element implementation`) بيختار الاستدعاء المناسب لنوعه من عمليات الزيارة (`Visitor overload`).



## Concrete Visitor

**Meaning:** A Visitor implementation containing one operation for every supported Element type.

**مصري:** تنفيذ للزائر (`Visitor implementation`) فيه عملية لكل نوع عنصر مدعوم (`Element`).



## Client (pattern role)

**Meaning:** Code that uses an interface or collaborates with a pattern's objects.

**مصري:** الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`.



## Observer interface

**Meaning:** The callback contract implemented by subscribers.

**مصري:** عقد `callback` اللي المشتركين بينفذوه.



## State interface

**Meaning:** The contract through which a Context delegates state-dependent behavior.

**مصري:** العقد اللي `Context` بتفوّض من خلاله `behavior` المعتمدة على `state`.
