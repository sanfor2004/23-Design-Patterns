# Glossary

[23 Design Patterns](README.md)

Translate the explanation, not the terminology. English labels are shared across all four languages. Pattern roles refer to the examples linked from each article; a role is not always a separate class.

Use your editor or browser’s Find command to locate a term. Lowercase `state` describes an object’s condition; `State` names the Design Pattern. Likewise, lowercase `iterator` is a traversal object and `Iterator` is the pattern.

## Design Pattern

**Meaning:** A reusable design idea for a recurring problem, not code to copy unchanged.

**مصري:** فكرة تصميم بتتكرر مع نوع مشكلة معروف؛ مش كود تنقله زي ما هو.

**中文:** 针对反复出现的问题总结的设计思路，不是直接照搬的代码。

**Italiano:** Un'idea di progettazione riutilizzabile per un problema ricorrente, non codice da copiare senza adattarlo.

## Creational Pattern

**Meaning:** A Design Pattern concerned with how objects are created and configured.

**مصري:** بيركز على إنشاء الكائنات وتجهيزها (`object creation`)، وده واحد من أغراض الـ `Design Patterns`.

**中文:** 关注如何创建和配置 object 的 Design Pattern。

**Italiano:** Un Design Pattern che riguarda la creazione e configurazione degli object.

## Structural Pattern

**Meaning:** A Design Pattern concerned with how objects and classes fit together.

**مصري:** بيركز على تركيب الكائنات والأنواع (`objects` و`classes`)، وده واحد من أغراض الـ `Design Patterns`.

**中文:** 关注 object 与 class 如何组织在一起的 Design Pattern。

**Italiano:** Un Design Pattern che organizza le relazioni fra object e class.

## Behavioral Pattern

**Meaning:** A Design Pattern concerned with behavior and collaboration among objects.

**مصري:** بيركز على السلوك (`behavior`) والتعاون بين الكائنات (`objects`)، وده واحد من أغراض الـ `Design Patterns`.

**中文:** 关注 object 的 behavior 与协作方式的 Design Pattern。

**Italiano:** Un Design Pattern che organizza behavior e collaborazione fra object.

## abstraction

**Meaning:** A view that exposes the operations a caller needs while hiding irrelevant details.

**مصري:** بتظهر العمليات اللي المستدعي محتاجها وبتخفي التفاصيل اللي مش محتاج يعرفها.

**中文:** 只呈现调用方需要的操作，隐藏无关细节。

**Italiano:** Una vista che espone le operazioni necessarie e nasconde i dettagli irrilevanti per chi la usa.

## interface

**Meaning:** The contract of operations and observable behavior offered to a caller.

**مصري:** العقد اللي بيحدد العمليات المتاحة وإيه اللي المستدعي يتوقعه منها.

**中文:** 约定可调用的操作及其对外可观察行为。

**Italiano:** Il contratto delle operazioni disponibili e del comportamento osservabile da chi le usa.

## implementation

**Meaning:** The concrete code that fulfills an interface or performs an operation.

**مصري:** الكود الفعلي اللي بينفذ عملية أو بيوفّي عقد `interface`.

**中文:** 实际完成操作或履行 interface 约定的代码。

**Italiano:** Il codice concreto che esegue un'operazione o soddisfa un'interface.

## composition

**Meaning:** Building behavior by connecting objects that use or contain other objects.

**مصري:** بتبني السلوك (`behavior`) عن طريق كائنات متعاونة (`objects`)، كل واحد منها بيستخدم أو بيحتوي كائنات تانية.

**中文:** 通过连接使用或包含其他 object 的 object 来组合行为。

**Italiano:** Costruire behavior collegando object che usano o contengono altri object.

## inheritance

**Meaning:** Defining a derived class from a base class to reuse or specialize its contract and implementation.

**مصري:** بتبني نوع مشتق (`derived class`) على أساس نوع موجود (`base class`)، عشان تعيد استخدام العقد أو تخصصه.

**中文:** 从 base class 定义 derived class，复用或扩展约定及实现。

**Italiano:** Definire una derived class da una base class per riusarne o specializzarne contratto e implementation.

## encapsulation

**Meaning:** Keeping representation and invariants behind controlled operations.

**مصري:** بتحمي تمثيل البيانات والقواعد اللي لازم تفضل صحيحة وبتسمح بالتعامل معاهم من عمليات محددة.

**中文:** 把内部表示和必须保持的规则放在受控操作之后。

**Italiano:** Proteggere rappresentazione interna e invarianti mediante operazioni controllate.

## polymorphism

**Meaning:** Using one interface with different implementations; C++ supports runtime and compile-time forms.

**مصري:** نفس العقد (`interface`) يقبل تنفيذات مختلفة (`implementations`). في `C++`، فيه أشكال بتتحدد وقت التشغيل (`runtime`)، وأشكال وقت الترجمة (`compile time`).

**中文:** 同一 interface 对应不同 implementation；C++ 同时支持 runtime 与 compile time 的形式。

**Italiano:** Usare un'interface con implementation diverse; C++ offre forme a runtime e a compile time.

## coupling

**Meaning:** The degree to which changing one part requires knowledge of or changes to another.

**مصري:** قد إيه جزء مرتبط بجزء تاني لدرجة إن تغييره يحتاج معرفة أو تعديل الجزء التاني.

**中文:** 一个部分的修改需要了解或修改另一部分的程度。

**Italiano:** Quanto una parte richiede conoscenza o modifiche di un'altra quando cambia.

## tight coupling

**Meaning:** Parts depend heavily on each other's concrete details, so changes tend to spread.

**مصري:** الأجزاء معتمدة بقوة على التفاصيل الداخلية لبعض، فالتغيير في واحد بينتشر للباقي.

**中文:** 各部分过度依赖彼此的具体细节，修改容易扩散。

**Italiano:** Le parti dipendono molto dai dettagli concreti reciproci e le modifiche tendono a propagarsi.

## loose coupling

**Meaning:** Parts know only the small contracts needed to cooperate, limiting change propagation.

**مصري:** كل جزء يعرف العقد الصغير اللي محتاجه للتعاون، فالتعديلات ما تنتشرش بسهولة.

**中文:** 各部分只了解协作所需的小范围约定，限制修改传播。

**Italiano:** Le parti conoscono solo i contratti necessari a collaborare, limitando la propagazione delle modifiche.

## cohesion

**Meaning:** How closely the responsibilities within a module belong together.

**مصري:** قد إيه مسؤوليات الجزء الواحد مرتبطة ببعض وبتخدم غرض واضح.

**中文:** 一个模块内部的职责是否紧密相关并服务于明确目的。

**Italiano:** Quanto le responsabilità di un modulo sono collegate e rivolte a uno scopo coerente.

## dependency

**Meaning:** Something a piece of code needs in order to work.

**مصري:** حاجة جزء من الكود محتاجها عشان يشتغل.

**中文:** 一段代码正常工作所需要的另一部分。

**Italiano:** Qualcosa di cui una parte del codice ha bisogno per funzionare.

## dependency injection

**Meaning:** Supplying a dependency from outside instead of choosing or constructing it inside the consumer.

**مصري:** بتمرّر `dependency` من بره بدل ما الجزء اللي بيستخدمها يختارها أو يعملها بنفسه.

**中文:** 从外部传入 dependency，而不是由使用方自行选择或创建。

**Italiano:** Fornire una dependency dall'esterno invece di sceglierla o costruirla nel codice che la usa.

## delegation

**Meaning:** An object asks a collaborator to perform part of its work.

**مصري:** الكائن بيفوّض جزء من شغله لكائن متعاون معاه (`object`)، بدل ما ينفّذ كل حاجة بنفسه.

**中文:** 一个 object 把部分工作交给协作方完成。

**Italiano:** Un object affida parte del proprio lavoro a un collaboratore.

## responsibility

**Meaning:** A job or obligation assigned to a part of a design.

**مصري:** شغل أو التزام جزء معين في التصميم مسؤول عنه.

**中文:** 设计中分配给某个部分的工作或义务。

**Italiano:** Un compito o obbligo assegnato a una parte del progetto.

## separation of concerns

**Meaning:** Keeping distinct kinds of responsibility apart so they can change independently.

**مصري:** بتفصل أنواع الشغل المختلفة عشان كل نوع يقدر يتغير لوحده.

**中文:** 把不同关注点分开，使它们能够独立变化。

**Italiano:** Tenere separate responsabilità di natura diversa perché possano cambiare indipendentemente.

## object composition

**Meaning:** Connecting objects to form a larger behavior or structure.

**مصري:** بتوصل الكائنات (`objects`) ببعض عشان تبني سلوك متكامل (`behavior`) أو تركيب أكبر.

**中文:** 连接多个 object，形成更大的行为或结构。

**Italiano:** Collegare object per costruire una struttura o un comportamento più ampio.

## object

**Meaning:** An entity with identity and lifetime; in C++, an object occupies storage.

**مصري:** كيان له هوية و `lifetime`؛ في `C++` الـ `object` بتشغل مساحة تخزين.

**中文:** 具有身份和 lifetime 的实体；在 C++ 中 object 占用存储空间。

**Italiano:** Un'entità con identità e lifetime; in C++ un object occupa memoria.

## class

**Meaning:** A C++ user-defined type that groups data and operations.

**مصري:** نوع بتعرّفه في `C++` وبتجمع فيه بيانات وعمليات مرتبطة.

**中文:** 在 C++ 中把相关数据和操作组织起来的自定义类型。

**Italiano:** Un tipo definito dall'utente in C++ che raggruppa dati e operazioni.

## instance

**Meaning:** A particular object of a type.

**مصري:** كائن محدد (`object`) من نوع معين.

**中文:** 某个类型的一个具体 object。

**Italiano:** Un particolare object appartenente a un tipo.

## client

**Meaning:** Code that uses an interface or collaborates with a pattern's objects.

**مصري:** الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`.

**中文:** 使用 interface 或与模式中的 object 协作的代码。

**Italiano:** Il codice che usa un'interface o collabora con gli object del pattern.

## concrete class

**Meaning:** A class that can be instantiated and supplies the required operations.

**مصري:** الـ `class` ينفع تعمل منها `instance` وبتوفر العمليات المطلوبة.

**中文:** 可以创建 instance 并提供所需操作的 class。

**Italiano:** Una class di cui si possono creare instance e che fornisce le operazioni richieste.

## abstract class

**Meaning:** A class that cannot be instantiated directly, typically because some virtual operations are pure.

**مصري:** الـ `class` ما ينفعش تعمل منها `instance` مباشرة؛ غالباً فيها عمليات `pure virtual`.

**中文:** 不能直接创建 instance 的 class，通常包含 pure virtual 操作。

**Italiano:** Una class non istanziabile direttamente, di solito con operazioni pure virtual.

## base class

**Meaning:** The class from which another class inherits.

**مصري:** الـ `class` اللي `class` تانية بتورّث منها.

**中文:** 另一 class 所继承的 class。

**Italiano:** La class da cui un'altra class eredita.

## derived class

**Meaning:** A class that inherits from a base class; also called a subclass.

**مصري:** الـ `class` بتورّث من `base class`، واسمها كمان `subclass`.

**中文:** 继承自 base class 的 class，也称 subclass。

**Italiano:** Una class che eredita da una base class; detta anche subclass.

## constructor

**Meaning:** The special operation that initializes a new class instance.

**مصري:** العملية الخاصة اللي بتجهّز `instance` جديدة وقت إنشائها.

**中文:** 创建 class instance 时负责初始化的特殊操作。

**Italiano:** L'operazione speciale che inizializza una nuova instance di una class.

## destructor

**Meaning:** The special operation run when a class instance's lifetime ends.

**مصري:** العملية الخاصة اللي بتتنفذ لما `lifetime` بتاعة `instance` تنتهي.

**中文:** class instance 的 lifetime 结束时执行的特殊操作。

**Italiano:** L'operazione speciale eseguita al termine della lifetime di una instance.

## method

**Meaning:** An operation associated with an object or class; usually a member function in C++.

**مصري:** عملية مرتبطة بـ `object` أو `class`؛ غالباً `member function` في `C++`.

**中文:** 与 object 或 class 关联的操作，在 C++ 中通常是 member function。

**Italiano:** Un'operazione associata a un object o a una class; in C++ solitamente una member function.

## function

**Meaning:** A callable unit of code with a declared input and result contract.

**مصري:** جزء كود تقدر تناديه، وله مدخلات ونتيجة متفق عليهم.

**中文:** 可调用的代码单元，具有明确的输入与结果约定。

**Italiano:** Un'unità di codice richiamabile con un contratto per ingressi e risultato.

## callback

**Meaning:** A function or operation supplied to be called when another operation needs it.

**مصري:** دالة (`function`) أو عملية بتمرّرها لجزء تاني، عشان يناديها وقت ما يحتاجها.

**中文:** 传给另一部分、在需要时由它调用的 function 或操作。

**Italiano:** Una function o operazione fornita perché un'altra parte possa richiamarla quando serve.

## event

**Meaning:** An occurrence that code can react to, such as an input or state change.

**مصري:** حاجة حصلت والكود ممكن يرد عليها، زي مدخل جديد أو تغيير `state`.

**中文:** 代码可以响应的事情，例如输入或 state 变化。

**Italiano:** Un fatto a cui il codice può reagire, come un input o una modifica di state.

## state

**Meaning:** The information that describes an object's current condition.

**مصري:** المعلومات اللي بتوصف وضع الـ `object` دلوقتي.

**中文:** 描述 object 当前状况的信息。

**Italiano:** Le informazioni che descrivono la condizione corrente di un object.

## behavior

**Meaning:** What an object or operation does in response to input and state.

**مصري:** اللي `object` أو عملية بتعمله بناءً على المدخلات والـ `state`.

**中文:** object 或操作根据输入和 state 所执行的动作。

**Italiano:** Ciò che un object o un'operazione fa in risposta a input e state.

## algorithm

**Meaning:** A defined procedure for solving a class of problems.

**مصري:** خطوات محددة لحل نوع معين من المشاكل.

**中文:** 解决某类问题的一套明确步骤。

**Italiano:** Una procedura definita per risolvere una categoria di problemi.

## runtime

**Meaning:** The period when a compiled program is executing.

**مصري:** الوقت اللي البرنامج فيه شغال بعد البناء.

**中文:** 编译后的程序正在执行的阶段。

**Italiano:** Il periodo in cui il programma compilato è in esecuzione.

## compile time

**Meaning:** The period when source code is checked and translated into a program.

**مصري:** المرحلة اللي فيها `source code` بيتراجع وبيتحول لبرنامج.

**中文:** 检查 source code 并将其转换为程序的阶段。

**Italiano:** La fase in cui il source code viene controllato e tradotto in un programma.

## memory allocation

**Meaning:** Obtaining storage for data; its cost and failure behavior depend on the mechanism.

**مصري:** حجز مساحة للبيانات؛ تكلفته وطريقة فشله حسب الآلية المستخدمة.

**中文:** 为数据取得存储空间，其成本和失败方式取决于所用机制。

**Italiano:** Ottenere spazio per i dati; costi e possibilità di errore dipendono dal meccanismo.

## ownership

**Meaning:** Responsibility for keeping a resource alive and eventually releasing it.

**مصري:** مين مسؤول يخلي المورد عايش ومين يحرره في الآخر.

**中文:** 负责维持资源存活并最终释放资源的责任。

**Italiano:** La responsabilità di mantenere una risorsa valida e infine rilasciarla.

## lifetime

**Meaning:** The interval during which an object exists and may be used according to its rules.

**مصري:** الفترة اللي الـ `object` موجودة فيها وينفع تستخدمها حسب قواعدها.

**中文:** object 存在且可按规则使用的时间区间。

**Italiano:** L'intervallo in cui un object esiste e può essere usato secondo le sue regole.

## smart pointer

**Meaning:** An object that wraps pointer access with a lifetime or ownership policy.

**مصري:** الـ `object` بتغلف `pointer` ومعاها قواعد واضحة للـ `ownership` أو `lifetime`.

**中文:** 为 pointer 的访问附加 lifetime 或 ownership 规则的 object。

**Italiano:** Un object che avvolge un pointer con una politica di lifetime o ownership.

## RAII

**Meaning:** Resource Acquisition Is Initialization: tie resource ownership to object lifetime so destruction releases it.

**مصري:** اربط المورد بعمر الكائن، عشان `destructor` تحرره تلقائياً؛ والاسم الكامل هو `Resource Acquisition Is Initialization`.

**中文:** Resource Acquisition Is Initialization：把资源 ownership 绑定到 object lifetime，在析构时释放资源。

**Italiano:** Resource Acquisition Is Initialization: legare l'ownership di una risorsa alla lifetime di un object, così la distruzione la rilascia.

## STL

**Meaning:** Standard Template Library: the generic containers, iterators, and algorithms associated with the C++ standard library.

**مصري:** `Standard Template Library`: الـ `containers` والـ `iterators` والـ `algorithms` العامة المرتبطة بمكتبة `C++` القياسية.

**中文:** Standard Template Library：与 C++ 标准库相关的通用 container、iterator 和 algorithm。

**Italiano:** Standard Template Library: container, iterator e algorithm generici associati alla libreria standard C++.

## container

**Meaning:** An object that stores a collection of elements.

**مصري:** الـ `object` بتخزّن مجموعة عناصر.

**中文:** 保存一组元素的 object。

**Italiano:** Un object che conserva una raccolta di elementi.

## iterator

**Meaning:** An object representing a traversal position and the operations valid at that position.

**مصري:** الـ `object` بتمثل مكانك أثناء المرور والعمليات المسموحة في المكان ده.

**中文:** 表示遍历位置及该位置上可用操作的 object。

**Italiano:** Un object che rappresenta una posizione di attraversamento e le operazioni consentite.

## template

**Meaning:** A C++ facility for defining families of types or functions parameterized at compile time.

**مصري:** وسيلة في `C++` لتعريف عيلة `types` أو `functions` بمعاملات بتتحدد وقت `compile time`.

**中文:** C++ 中在 compile time 通过参数定义一组 type 或 function 的机制。

**Italiano:** Un meccanismo C++ per definire famiglie di tipi o function parametrizzate a compile time.

## generic programming

**Meaning:** Writing algorithms against requirements on types rather than one concrete type.

**مصري:** بتكتب `algorithms` على أساس متطلبات النوع بدل ما تربطها بنوع واحد.

**中文:** 根据类型需要满足的要求编写 algorithm，而不是绑定一个具体类型。

**Italiano:** Scrivere algorithm basati sui requisiti dei tipi invece che su un solo tipo concreto.

## trade-off

**Meaning:** A benefit gained at the cost of another desirable property.

**مصري:** ميزة بتكسبها قصاد تكلفة أو تنازل في ناحية تانية.

**中文:** 获得一种好处时付出的另一种代价。

**Italiano:** Un vantaggio ottenuto rinunciando a un'altra proprietà desiderabile.

## use case

**Meaning:** A concrete situation in which a design is useful.

**مصري:** موقف محدد التصميم بينفع فيه.

**中文:** 某种设计能发挥作用的具体场景。

**Italiano:** Una situazione concreta in cui un progetto è utile.

## extensibility

**Meaning:** How readily new behavior can be added without disrupting existing code.

**مصري:** سهولة إضافة `behavior` جديدة من غير ما تلخبط الكود الموجود.

**中文:** 增加新 behavior 而不破坏现有代码的容易程度。

**Italiano:** Quanto è facile aggiungere behavior senza compromettere il codice esistente.

## maintainability

**Meaning:** How readily code can be understood, corrected, and changed over time.

**مصري:** سهولة فهم الكود وتصليحه وتعديله مع الوقت.

**中文:** 长期理解、修正和修改代码的容易程度。

**Italiano:** Quanto è facile capire, correggere e modificare il codice nel tempo.

## testability

**Meaning:** How readily behavior can be isolated, exercised, and checked.

**مصري:** سهولة عزل `behavior` وتشغيلها والتأكد من نتيجتها.

**中文:** 隔离、执行并检查 behavior 的容易程度。

**Italiano:** Quanto è facile isolare, esercitare e verificare un behavior.

## scalability

**Meaning:** How a system handles growth in workload or data with added resources.

**مصري:** قدرة النظام يتعامل مع زيادة الشغل أو البيانات لما تزود موارده.

**中文:** 系统在增加资源后应对工作量或数据增长的能力。

**Italiano:** La capacità di sostenere più lavoro o dati mediante risorse aggiuntive.

## refactoring

**Meaning:** Changing internal structure while preserving externally observable behavior.

**مصري:** بتغيّر تركيب الكود من جوه مع الحفاظ على `behavior` اللي باينة للمستخدم.

**中文:** 调整内部结构，同时保持对外可观察的 behavior。

**Italiano:** Cambiare la struttura interna preservando il behavior osservabile dall'esterno.

## anti-pattern

**Meaning:** A recurring approach whose apparent convenience repeatedly leads to poor outcomes in a context.

**مصري:** حل بيتكرر وشكله مريح، بس بيؤدي لمشاكل متكررة في سياق معين.

**中文:** 在特定场景中看似方便、却反复产生不良结果的做法。

**Italiano:** Un approccio ricorrente che sembra conveniente ma produce ripetutamente problemi in un contesto.

## code smell

**Meaning:** A sign worth investigating, not automatic proof that code is wrong.

**مصري:** علامة تستاهل تراجع الكود بسببها، مش دليل لوحدها إن الكود غلط.

**中文:** 值得进一步检查的迹象，并不自动证明代码有错。

**Italiano:** Un indizio da approfondire, non una prova automatica che il codice sia sbagliato.

## composition over inheritance

**Meaning:** Prefer collaborating objects when they express variation more clearly than extending a class hierarchy.

**مصري:** فضّل تركيب الحل من كائنات متعاونة (`objects`)، لما ده يكون أوضح من توسيع شجرة الوراثة (`inheritance`).

**中文:** 当协作 object 能更清楚地表达变化时，优先使用它们而不是扩展 inheritance 层次。

**Italiano:** Preferire object collaboranti quando esprimono la variazione meglio di una gerarchia di inheritance.

## program to an interface, not an implementation

**Meaning:** Depend on the promised contract instead of a particular concrete implementation.

**مصري:** اعتمد على العقد المعلن بدل تفاصيل `implementation` بعينها.

**中文:** 依赖公开约定，而不是某个具体 implementation。

**Italiano:** Dipendere dal contratto promesso anziché da una particolare implementation concreta.

## favor loose coupling

**Meaning:** Limit knowledge of concrete collaborators to reduce how far changes spread.

**مصري:** قلّل معرفة كل جزء بتفاصيل اللي بيتعاون معاهم عشان التغيير ما ينتشرش.

**中文:** 限制对具体协作方的了解，减少修改传播。

**Italiano:** Limitare la conoscenza dei collaboratori concreti per contenere la propagazione delle modifiche.

## encapsulate what varies

**Meaning:** Put a changing design decision behind a stable boundary.

**مصري:** حط القرار اللي بيتغير ورا حدود ثابتة وواضحة.

**中文:** 把会变化的设计决策放在稳定边界之后。

**Italiano:** Racchiudere una decisione variabile dietro un confine stabile.

## single responsibility

**Meaning:** Keep a module focused on one coherent reason to change.

**مصري:** خلّي الجزء مركز على سبب واحد مترابط للتغيير.

**中文:** 让一个模块围绕一个连贯的变化原因组织职责。

**Italiano:** Concentrare un modulo su un motivo coerente di cambiamento.

## Single Responsibility Principle

**Meaning:** Organize a module around one responsibility so unrelated change pressures do not mix.

**مصري:** نظّم الجزء حوالين `responsibility` واحدة عشان أسباب التغيير المختلفة ما تتخلطش.

**中文:** 围绕一种 responsibility 组织模块，避免混合互不相关的修改压力。

**Italiano:** Organizzare un modulo attorno a una responsibility, evitando pressioni di cambiamento non correlate.

## Open/Closed Principle

**Meaning:** Aim for open for extension, closed for modification at a useful, chosen boundary.

**مصري:** خلّي التوسيع ممكن من غير تعديل الكود المستقر، عند حدود مختارة بوضوح. التعبير هو `open for extension, closed for modification`.

**中文:** 在选定的有效边界上追求 open for extension, closed for modification。

**Italiano:** Mirare a open for extension, closed for modification lungo un confine scelto e utile.

## open for extension, closed for modification

**Meaning:** Add intended variations through extension points without editing stable client logic.

**مصري:** ضيف التغييرات المقصودة من نقاط توسعة بدل تعديل منطق `client` المستقر.

**中文:** 通过扩展点增加预期变化，而不修改稳定的 client 逻辑。

**Italiano:** Aggiungere le variazioni previste attraverso punti di estensione senza modificare la logica client stabile.

## dependency inversion

**Meaning:** High-level policy and low-level details depend on abstractions rather than policy depending directly on details.

**مصري:** السياسة العامة والتفاصيل يعتمدوا على `abstractions` بدل ما السياسة تتربط بالتفاصيل مباشرة.

**中文:** 高层规则和底层细节都依赖 abstraction，而不是让高层规则直接依赖细节。

**Italiano:** Politiche di alto livello e dettagli dipendono da abstraction, invece di legare direttamente le politiche ai dettagli.

## SOLID

**Meaning:** A group of five object-oriented design principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

**مصري:** خمس مبادئ للتصميم: `Single Responsibility` و `Open`/`Closed` و `Liskov Substitution` و `Interface Segregation` و `Dependency Inversion`.

**中文:** 五项面向对象设计原则：Single Responsibility、Open/Closed、Liskov Substitution、Interface Segregation 和 Dependency Inversion。

**Italiano:** Cinque principi: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation e Dependency Inversion.

## object creation

**Meaning:** Choosing a concrete type and establishing an object's initial values and lifetime.

**مصري:** اختيار النوع الفعلي وتجهيز قيمه الأولية. من هنا بيبدأ عمر الكائن (`lifetime`).

**中文:** 选择具体类型，建立 object 的初始值并开始其 lifetime。

**Italiano:** Scegliere il tipo concreto e stabilire valori iniziali e lifetime di un object.

## runtime behavior

**Meaning:** What the program does while executing, including behavior selected from runtime input.

**مصري:** اللي البرنامج بيعمله وهو شغال، بما فيه `behavior` بتتحدد من المدخلات.

**中文:** 程序执行时实际发生的动作，包括由运行时输入选择的 behavior。

**Italiano:** Ciò che il programma fa durante l'esecuzione, incluso il behavior scelto dagli input.

## compile-time dependency

**Meaning:** A dependency needed to compile a unit of code, such as a type declaration in a header.

**مصري:** الـ `dependency` لازمة عشان تترجم جزء كود، زي تعريف نوع في `header`.

**中文:** 编译一段代码所需的 dependency，例如 header 中的类型声明。

**Italiano:** Una dependency necessaria a compilare codice, come una dichiarazione di tipo in un header.

## interchangeable behavior

**Meaning:** Different behaviors that can be supplied through the same contract.

**مصري:** سلوكيات مختلفة (`behaviors`) تقدر تختار أي واحدة منها من خلال نفس العقد.

**中文:** 可以通过同一约定提供的不同 behavior。

**Italiano:** Behavior diversi fornibili attraverso lo stesso contratto.

## encapsulate an algorithm

**Meaning:** Put an algorithm behind an operation that hides its internal steps.

**مصري:** حط `algorithm` ورا عملية بتخفي خطواتها الداخلية.

**中文:** 把 algorithm 放在隐藏其内部步骤的操作之后。

**Italiano:** Racchiudere un algorithm dietro un'operazione che ne nasconde i passi interni.

## runtime selection

**Meaning:** Choosing an implementation while the program is executing.

**مصري:** اختيار `implementation` والبرنامج شغال.

**中文:** 在程序执行期间选择 implementation。

**Italiano:** Scegliere un'implementation durante l'esecuzione del programma.

## type erasure

**Meaning:** Hiding a concrete type behind a uniform runtime interface, as std::function does for callables.

**مصري:** بتخفي النوع الفعلي ورا `interface` موحدة وقت `runtime`، زي `std::function` مع `callables`.

**中文:** 把具体类型隐藏在统一的 runtime interface 后面，例如 std::function 对 callable 的处理。

**Italiano:** Nascondere un tipo concreto dietro un'interface uniforme a runtime, come std::function per i callable.

## one-to-many dependency

**Meaning:** One source has multiple dependents that react to its changes.

**مصري:** مصدر واحد ليه أكتر من طرف بيتأثروا بتغييره.

**中文:** 一个来源发生变化时，有多个依赖方需要响应。

**Italiano:** Una sorgente ha più dipendenti che reagiscono ai suoi cambiamenti.

## subscription lifetime

**Meaning:** The interval in which a listener is registered and eligible for notification.

**مصري:** الفترة اللي المستمع فيها مسجل وينفع توصله `notification`.

**中文:** 监听方已注册且可以接收通知的时间区间。

**Italiano:** Il periodo in cui un listener è registrato e può ricevere notifiche.

## state transition

**Meaning:** A move from one modeled condition to another after an event.

**مصري:** انتقال من وضع ممثّل في التصميم لوضع تاني بعد `event`.

**中文:** 在 event 后从一个建模状态转到另一个状态。

**Italiano:** Il passaggio fra due condizioni modellate in seguito a un event.

## algorithm skeleton

**Meaning:** The fixed sequence of an algorithm whose selected steps can vary.

**مصري:** ترتيب `algorithm` الثابت اللي بعض خطواته ممكن تتغير.

**中文:** 某些步骤可以变化、整体顺序保持固定的 algorithm 框架。

**Italiano:** La sequenza fissa di un algorithm di cui alcuni passi possono variare.

## hook method

**Meaning:** An extension operation called by a fixed workflow; it may have a default implementation.

**مصري:** عملية للتوسعة بتناديها خطوات ثابتة، وممكن يكون ليها `implementation` افتراضية.

**中文:** 由固定流程调用的扩展操作，可以有默认 implementation。

**Italiano:** Un'operazione di estensione richiamata da un flusso fisso, eventualmente con implementation predefinita.

## double dispatch

**Meaning:** Selecting behavior using two runtime types; classic Visitor combines two virtual calls with overload resolution.

**مصري:** اختيار `behavior` بناءً على نوعين وقت `runtime`؛ الـ `Visitor` التقليدية بتجمع نداءين `virtual` مع `overload resolution`.

**中文:** 依据两个 runtime 类型选择 behavior；经典 Visitor 结合两次 virtual 调用与 overload resolution。

**Italiano:** Selezionare behavior usando due tipi a runtime; il Visitor classico combina due chiamate virtual con overload resolution.

## overload resolution

**Meaning:** Compile-time selection among functions with the same name using the argument types.

**مصري:** اختيار `function` من كذا واحدة بنفس الاسم حسب أنواع المعاملات وقت `compile time`.

**中文:** 在 compile time 根据参数类型，从同名 function 中选择匹配项。

**Italiano:** La scelta a compile time fra function omonime in base ai tipi degli argomenti.

## deep copy

**Meaning:** Copying owned nested data so the new object does not share that mutable data with the original.

**مصري:** بتنسخ البيانات الداخلية المملوكة عشان تعديل النسخة ما يغيرش الأصل.

**中文:** 复制所拥有的嵌套数据，使新 object 不与原 object 共享这些可变数据。

**Italiano:** Copiare i dati interni posseduti perché il nuovo object non condivida quei dati modificabili con l'originale.

## value semantics

**Meaning:** Copies behave as independent values according to the type's contract.

**مصري:** النسخ تتعامل كقيم مستقلة حسب عقد النوع.

**中文:** 按照类型约定，副本表现为独立的值。

**Italiano:** Le copie si comportano come valori indipendenti secondo il contratto del tipo.

## global state

**Meaning:** Data reachable broadly across a program whose changes can affect distant code.

**مصري:** بيانات أجزاء كتير تقدر توصلها، وتغييرها ممكن يأثر على كود بعيد.

**中文:** 程序中广泛可访问、修改后可能影响远处代码的数据。

**Italiano:** Dati accessibili da molte parti del programma, le cui modifiche possono influire su codice distante.

## thread-safe initialization

**Meaning:** Initialization protected against concurrent construction; it does not make later operations thread-safe.

**مصري:** حماية التهيئة من الإنشاء المتزامن؛ مش معناها إن كل العمليات بعد كده `thread-safe`.

**中文:** 避免并发重复构造的初始化保障，不代表后续操作也 thread-safe。

**Italiano:** Inizializzazione protetta dalla costruzione concorrente; non rende thread-safe le operazioni successive.

## fluent interface

**Meaning:** An interface shaped to read as a chain of calls; it does not by itself imply Builder.

**مصري:** عقد (`interface`) بيسمح تكتب سلسلة استدعاءات بشكل مقروء؛ ده لوحده مش معناه إنك بتستخدم `Builder`.

**中文:** 设计成链式调用的 interface；它本身并不等于 Builder。

**Italiano:** Un'interface pensata come catena leggibile di chiamate; da sola non implica Builder.

## intrinsic state

**Meaning:** Data independent of an occurrence's context that a Flyweight can share.

**مصري:** بيانات مستقلة عن مكان الاستخدام، فالـ `Flyweight` تقدر تشاركها.

**中文:** 不依赖具体使用位置、可由 Flyweight 共享的数据。

**Italiano:** Dati indipendenti dal contesto della singola occorrenza, condivisibili da un Flyweight.

## extrinsic state

**Meaning:** Per-occurrence data kept outside a shared Flyweight.

**مصري:** بيانات تخص كل استخدام وبتفضل بره الـ `Flyweight` المشتركة.

**中文:** 每次使用独有、保存在共享 Flyweight 外部的数据。

**Italiano:** Dati specifici di un'occorrenza conservati fuori dal Flyweight condiviso.

## interning

**Meaning:** Reusing one representation for equivalent values through a lookup pool.

**مصري:** بتعيد استخدام تمثيل واحد للقيم المتساوية عن طريق `pool` للبحث.

**中文:** 通过查找池为等价值复用同一个表示。

**Italiano:** Riutilizzare una rappresentazione per valori equivalenti attraverso un pool di ricerca.

## lazy initialization

**Meaning:** Deferring creation until the value or resource is first needed.

**مصري:** بتأجل الإنشاء لأول مرة تحتاج فيها القيمة أو المورد.

**中文:** 把创建推迟到首次需要值或资源时。

**Italiano:** Rinviare la creazione fino al primo utilizzo del valore o della risorsa.

## part-whole hierarchy

**Meaning:** A recursive structure in which groups contain leaves or smaller groups.

**مصري:** تركيب متكرر فيه مجموعات بتحتوي عناصر أو مجموعات أصغر.

**中文:** 分组包含叶子或更小分组的递归结构。

**Italiano:** Una struttura ricorsiva in cui gruppi contengono foglie o gruppi più piccoli.

## recursive composition

**Meaning:** Building a structure from parts that expose the same contract as the whole.

**مصري:** بتبني تركيب من أجزاء بتوفر نفس عقد الكل.

**中文:** 由提供与整体相同约定的部分递归构建结构。

**Italiano:** Costruire ricorsivamente una struttura con parti che espongono il contratto dell'insieme.

## chain termination

**Meaning:** The rule for stopping a chain and deciding what happens after the last handler.

**مصري:** القاعدة اللي بتحدد السلسلة تقف إمتى وإيه يحصل بعد آخر `Handler`.

**中文:** 决定处理链何时停止以及最后一个 Handler 之后如何处理的规则。

**Italiano:** La regola che ferma una catena e stabilisce cosa succede dopo l'ultimo Handler.

## undo

**Meaning:** Restoring an earlier logical result, using saved state or an inverse operation when possible.

**مصري:** بترجع لنتيجة سابقة باستخدام `state` محفوظة أو عملية عكسية لما ينفع.

**中文:** 在可行时用保存的 state 或逆操作恢复之前的逻辑结果。

**Italiano:** Ripristinare un risultato precedente con state salvato o un'operazione inversa, quando possibile.

## exception safety

**Meaning:** The guarantees an operation preserves if it fails by throwing an exception.

**مصري:** الضمانات اللي العملية بتحافظ عليها لو فشلت ورمت `exception`.

**中文:** 操作抛出 exception 时仍能保持的保证。

**Italiano:** Le garanzie mantenute da un'operazione quando fallisce lanciando un'exception.

## snapshot

**Meaning:** A captured representation of selected state at a point in time.

**مصري:** صورة محفوظة لجزء محدد من `state` في لحظة معينة.

**中文:** 某一时刻所选 state 的保存表示。

**Italiano:** Una rappresentazione di uno state selezionato in un dato momento.

## abstract syntax tree

**Meaning:** A tree representing grammatical structure rather than the original text's surface formatting.

**مصري:** شجرة بتمثل تركيب القواعد بدل الشكل المكتوب للنص.

**中文:** 表示语法结构、而不是原始文本表面格式的树。

**Italiano:** Un albero che rappresenta la struttura grammaticale anziché la forma testuale originale.

## short-circuit evaluation

**Meaning:** Skipping later operands when an earlier result already determines the answer.

**مصري:** بتتخطى باقي المعاملات لما نتيجة بدري تكون حسمت الإجابة.

**中文:** 当前面的结果已决定答案时，跳过后续操作数的求值。

**Italiano:** Saltare gli operandi successivi quando un risultato precedente determina già la risposta.

## iterator invalidation

**Meaning:** An operation makes an iterator no longer valid for its intended use.

**مصري:** عملية بتخلي `iterator` ما بقتش صالحة للاستخدام المقصود.

**中文:** 某个操作导致 iterator 不再适合原本的使用方式。

**Italiano:** Un'operazione rende un iterator non più valido per l'uso previsto.

## forward iterator

**Meaning:** An iterator supporting forward traversal and the multipass guarantee, allowing independent copies to traverse the same range.

**مصري:** أداة مرور (`iterator`) بتتحرك لقدام، وبتدعم المرور المستقل أكتر من مرة (`multipass`). يعني نسخها المستقلة تقدر تمر على نفس النطاق.

**中文:** 支持向前遍历与 multipass 保证的 iterator，独立副本可以遍历同一范围。

**Italiano:** Un iterator con avanzamento e garanzia multipass: copie indipendenti possono percorrere lo stesso intervallo.

## god object

**Meaning:** An object accumulating too many unrelated responsibilities.

**مصري:** كائن (`object`) بيجمع مسؤوليات كتير مالهاش علاقة قوية ببعض.

**中文:** 积累过多无关职责的 object。

**Italiano:** Un object che accumula troppe responsabilità non correlate.

## UML

**Meaning:** Unified Modeling Language, a notation family for describing software structure and interactions.

**مصري:** `Unified Modeling Language`: طرق رسم لوصف تركيب البرامج والتفاعلات بينها.

**中文:** Unified Modeling Language：描述软件结构与交互的一组建模记法。

**Italiano:** Unified Modeling Language, una famiglia di notazioni per descrivere struttura e interazioni del software.

## class diagram

**Meaning:** A structural diagram showing classes, their contracts, and relationships.

**مصري:** رسم بيوضح `classes` وعقودها والعلاقات بينها.

**中文:** 展示 class、约定及相互关系的结构图。

**Italiano:** Un diagramma strutturale di class, contratti e relazioni.

## sequence diagram

**Meaning:** A diagram showing interactions in their execution order.

**مصري:** رسم بيوضح التفاعلات بالترتيب اللي بتحصل بيه.

**中文:** 按执行顺序展示交互的图。

**Italiano:** Un diagramma che mostra le interazioni nel loro ordine di esecuzione.

## lifecycle

**Meaning:** The modeled stages and transitions of a domain entity, distinct from a C++ object's lifetime.

**مصري:** المراحل والانتقالات اللي بنمثلها لكيان في المشكلة؛ مش نفس `lifetime` بتاعة `object` في `C++`.

**中文:** 领域实体的建模阶段与转换，不等于 C++ object 的 lifetime。

**Italiano:** Le fasi e transizioni modellate di un'entità del dominio, distinte dalla lifetime di un object C++.

## std::unique_ptr

**Meaning:** A smart pointer with exclusive ownership that releases its object when the owner is destroyed.

**مصري:** مؤشر ذكي (`smart pointer`) بملكية حصرية؛ بيحرر الكائن لما المالك يتدمر.

**中文:** 具有独占 ownership 的 smart pointer，在所有者销毁时释放 object。

**Italiano:** Uno smart pointer con ownership esclusiva che rilascia l'object alla distruzione del proprietario.

## std::shared_ptr

**Meaning:** A smart pointer sharing ownership; the managed object is released when the last owning reference disappears.

**مصري:** مؤشر ذكي (`smart pointer`) بيشارك الملكية (`ownership`)؛ الكائن بيتحرر لما آخر مرجع مالك يختفي.

**中文:** 共享 ownership 的 smart pointer，最后一个拥有引用消失时释放 object。

**Italiano:** Uno smart pointer con ownership condivisa; l'object viene rilasciato quando scompare l'ultimo riferimento proprietario.

## std::weak_ptr

**Meaning:** A non-owning observer of shared ownership; lock attempts to obtain a temporary shared_ptr.

**مصري:** مرجع مش مالك لملكية مشتركة؛ الـ `lock` بتحاول تجيب `shared_ptr` مؤقتة.

**中文:** 观察共享 ownership 但不拥有 object；lock 尝试取得临时 shared_ptr。

**Italiano:** Un riferimento non proprietario a ownership condivisa; lock tenta di ottenere uno shared_ptr temporaneo.

## std::vector

**Meaning:** A standard container storing elements contiguously with a size that can change.

**مصري:** الـ `container` قياسية بتخزن العناصر جنب بعض وحجمها ممكن يتغير.

**中文:** 连续保存元素、大小可变的标准 container。

**Italiano:** Un container standard con elementi contigui e dimensione modificabile.

## std::function

**Meaning:** A type-erased wrapper that stores a callable with a chosen signature.

**مصري:** الـ `Wrapper` بتخزن `callable` بتوقيع محدد وبتخفي نوعها الفعلي.

**中文:** 保存指定签名 callable 并隐藏其具体类型的包装器。

**Italiano:** Un wrapper con type erasure che conserva un callable con una firma scelta.

## virtual

**Meaning:** A C++ keyword enabling derived implementations to be selected through a base interface.

**مصري:** كلمة `C++` بتسمح باختيار `implementation` من `derived class` من خلال `interface` الأساس.

**中文:** 允许通过 base interface 选择 derived implementation 的 C++ 关键字。

**Italiano:** Una parola chiave C++ che consente di selezionare implementation derivate tramite l'interface base.

## override

**Meaning:** A C++ specifier asking the compiler to verify that a method overrides a base virtual method.

**مصري:** محدد في `C++` بيطلب من المترجم يتأكد إن `method` بتعيد تعريف `virtual method` في الأساس.

**中文:** 要求编译器确认 method 覆盖了 base virtual method 的 C++ 指定符。

**Italiano:** Uno specificatore C++ che fa verificare che un method ridefinisca un virtual method della base.

## const

**Meaning:** A C++ qualifier restricting modification through a particular access path; it is not a thread-safety guarantee.

**مصري:** محدد بيقيّد التعديل من طريق وصول معين؛ مش ضمان لأمان التزامن.

**中文:** 限制通过某种访问方式进行修改的 C++ 限定符，并不保证线程安全。

**Italiano:** Un qualificatore C++ che limita le modifiche attraverso un accesso; non garantisce sicurezza fra thread.

## type

**Meaning:** A specification of the values and operations supported by an entity.

**مصري:** وصف للقيم والعمليات اللي الكيان بيدعمها.

**中文:** 规定实体支持哪些值和操作的描述。

**Italiano:** La specifica dei valori e delle operazioni supportati da un'entità.

## pointer

**Meaning:** A value that can refer to an object or function; a raw pointer does not by itself express ownership.

**مصري:** قيمة ممكن تشير لـ `object` أو `function`؛ الـ `raw pointer` لوحدها ما بتحددش `ownership`.

**中文:** 可指向 object 或 function 的值；raw pointer 本身不表示 ownership。

**Italiano:** Un valore che può riferirsi a un object o function; un raw pointer da solo non esprime ownership.

## reference

**Meaning:** An alias referring to an existing entity, not ownership by itself.

**مصري:** اسم بديل لكيان موجود، مش `ownership` لوحده.

**中文:** 现有实体的别名，本身不代表 ownership。

**Italiano:** Un alias di un'entità esistente, che da solo non esprime ownership.

## callable

**Meaning:** Something invocable with function-call syntax, such as a lambda or function object.

**مصري:** حاجة ينفع تناديها بصيغة `function`، زي `lambda` أو `function object`.

**中文:** 可用 function 调用语法执行的实体，例如 lambda 或 function object。

**Italiano:** Qualcosa di invocabile con la sintassi di chiamata, come una lambda o un function object.

## lambda

**Meaning:** A C++ expression that creates a callable and may capture surrounding values.

**مصري:** تعبير `C++` بيعمل `callable` وممكن يحتفظ بقيم من حواليه.

**中文:** 创建 callable、并可捕获周围值的 C++ 表达式。

**Italiano:** Un'espressione C++ che crea un callable e può catturare valori circostanti.

## Product

**Meaning:** The contract of an object returned by creation code.

**مصري:** العقد بتاع الكائن (`object`) اللي كود الإنشاء بيرجعه.

**中文:** 创建代码返回的 object 所提供的约定。

**Italiano:** Il contratto dell'object restituito dal codice di creazione.

## Concrete Product

**Meaning:** A particular implementation of a Product contract.

**مصري:** تنفيذ فعلي (`implementation`) لعقد المنتج (`Product`).

**中文:** Product 约定的一种具体 implementation。

**Italiano:** Una particolare implementation del contratto Product.

## Concrete Factory

**Meaning:** An implementation that creates one matching Product family.

**مصري:** تنفيذ فعلي (`implementation`) بينشئ عيلة منتجات متوافقة (`Product family`).

**中文:** 创建一组配套 Product 的 implementation。

**Italiano:** Un'implementation che crea una famiglia coerente di Product.

## Creator

**Meaning:** The base role that owns a workflow and declares its creation operation.

**مصري:** الدور الأساسي اللي ماسك الخطوات وبيعلن عملية الإنشاء اللي بيحتاجها.

**中文:** 拥有公共流程并声明创建操作的基础角色。

**Italiano:** Il ruolo base che contiene il flusso e dichiara l'operazione di creazione.

## Concrete Creator

**Meaning:** A Creator subclass that supplies a particular Product.

**مصري:** نوع مشتق (`subclass`) من `Creator`، مسؤول عن إنشاء منتج معين (`Product`).

**中文:** 提供某种 Product 的 Creator subclass。

**Italiano:** Una subclass di Creator che fornisce un particolare Product.

## Concrete Prototype

**Meaning:** An object whose clone operation produces another object from its configured values.

**مصري:** كائن بيوفّر العملية `clone` لإنشاء كائن تاني (`object`) من القيم المتجهّزة.

**中文:** 通过 clone 操作按已配置值创建另一 object 的 object。

**Italiano:** Un object la cui operazione clone crea un altro object dai valori configurati.

## Target

**Meaning:** The interface expected by the Client.

**مصري:** الـ `interface` اللي `Client` متوقع يتعامل معاها.

**中文:** Client 期望使用的 interface。

**Italiano:** L'interface attesa dal Client.

## Adaptee

**Meaning:** The existing object whose interface needs adaptation.

**مصري:** الـ `object` الموجودة اللي `interface` بتاعتها محتاجة تتوافق مع المطلوب.

**中文:** 其现有 interface 需要适配的 object。

**Italiano:** L'object esistente la cui interface deve essere adattata.

## Abstraction (Bridge role)

**Meaning:** The high-level side of Bridge that delegates implementation work.

**مصري:** الناحية اللي بتوفر العمليات الأساسية في `Bridge` وبتفوّض شغل التنفيذ.

**中文:** Bridge 中提供高层操作并委托实现工作的角色。

**Italiano:** Il lato di alto livello di Bridge che delega il lavoro di implementazione.

## Refined Abstraction

**Meaning:** A specialization of Abstraction independent of the implementation side.

**مصري:** تخصيص لـ `Abstraction` مستقل عن ناحية التنفيذ.

**中文:** 独立于实现侧的 Abstraction 特化。

**Italiano:** Una specializzazione di Abstraction indipendente dal lato implementativo.

## Implementor

**Meaning:** The contract used by a Bridge Abstraction for lower-level work.

**مصري:** العقد اللي `Abstraction` بتستخدمه للشغل في الناحية التانية من `Bridge`.

**中文:** Bridge 的 Abstraction 用于底层工作的约定。

**Italiano:** Il contratto usato dall'Abstraction di Bridge per il lavoro di livello inferiore.

## Concrete Implementor

**Meaning:** A particular implementation of the Implementor contract.

**مصري:** تنفيذ محدد (`implementation`) لعقد `Implementor`.

**中文:** Implementor 约定的一种具体 implementation。

**Italiano:** Una particolare implementation del contratto Implementor.

## Component

**Meaning:** The common contract exposed by leaves, groups, or wrappers.

**مصري:** العقد المشترك اللي العنصر أو المجموعة أو `Wrapper` بتوفره.

**中文:** 叶子、分组或包装层共同提供的约定。

**Italiano:** Il contratto comune esposto da foglie, gruppi o wrapper.

## Leaf

**Meaning:** A Component with no child Components.

**مصري:** عنصر (`Component`) مافيهوش عناصر تحته.

**中文:** 不含子 Component 的 Component。

**Italiano:** Un Component senza Component figli.

## Concrete Component

**Meaning:** The basic implementation before optional wrappers are added.

**مصري:** الـ `implementation` الأساسية قبل إضافة طبقات اختيارية.

**中文:** 添加可选包装层之前的基础 implementation。

**Italiano:** L'implementation di base prima dell'aggiunta di wrapper facoltativi.

## Concrete Decorator

**Meaning:** A wrapper that keeps the Component contract and adds a specific responsibility.

**مصري:** طبقة تغليف (`Wrapper`) بتحافظ على عقد `Component`، وبتضيف مسؤولية محددة (`responsibility`).

**中文:** 保留 Component 约定并增加某项 responsibility 的包装层。

**Italiano:** Un wrapper che mantiene il contratto Component e aggiunge una responsibility specifica.

## subsystem

**Meaning:** A group of cooperating services or objects within a larger system.

**مصري:** مجموعة خدمات أو `objects` بتتعاون جوه نظام أكبر.

**中文:** 较大系统中相互协作的一组服务或 object。

**Italiano:** Un gruppo di servizi o object collaboranti dentro un sistema più ampio.

## Flyweight Factory

**Meaning:** A lookup service that returns a shared Flyweight for a key.

**مصري:** جزء بيبحث بالمفتاح ويرجع `Flyweight` مشتركة.

**中文:** 按键查找并返回共享 Flyweight 的服务。

**Italiano:** Un servizio di ricerca che restituisce un Flyweight condiviso per una chiave.

## Subject interface

**Meaning:** The shared contract offered by a Proxy and its Real Subject.

**مصري:** العقد المشترك اللي `Proxy` و `Real Subject` بيوفروه.

**中文:** Proxy 与 Real Subject 共同提供的约定。

**Italiano:** Il contratto condiviso da Proxy e Real Subject.

## Real Subject

**Meaning:** The object that does the work behind a Proxy.

**مصري:** الـ `object` اللي بتنفذ الشغل الحقيقي ورا `Proxy`.

**中文:** 在 Proxy 后面实际完成工作的 object。

**Italiano:** L'object che svolge il lavoro dietro un Proxy.

## Handler

**Meaning:** A role that handles a request or passes it to its successor.

**مصري:** دور بيعمل معالجة للطلب أو يبعته للي بعده.

**中文:** 处理请求或把请求传给后继的角色。

**Italiano:** Un ruolo che elabora una richiesta o la passa al successore.

## Concrete Handler

**Meaning:** A Handler implementing one particular processing rule.

**مصري:** معالج (`Handler`) بينفّذ قاعدة معينة.

**中文:** 实现某项处理规则的 Handler。

**Italiano:** Un Handler che implementa una specifica regola di elaborazione.

## Receiver

**Meaning:** The object that performs the work requested by a Command.

**مصري:** الـ `object` اللي بيتنفذ عليها الشغل المطلوب من `Command`.

**中文:** 执行 Command 所请求工作的 object。

**Italiano:** L'object che svolge il lavoro richiesto da un Command.

## Invoker

**Meaning:** The role that starts or stores Commands without knowing each operation's details.

**مصري:** الدور اللي بيشغّل `Commands` أو بيخزنها من غير معرفة تفاصيل كل عملية.

**中文:** 启动或保存 Command、无需了解每项操作细节的角色。

**Italiano:** Il ruolo che avvia o conserva Command senza conoscere i dettagli delle singole operazioni.

## Concrete Command

**Meaning:** A Command implementation that binds a Receiver and an action.

**مصري:** تنفيذ للأمر (`Command implementation`) بيربط الفعل المطلوب بالجهة اللي هتنفّذه (`Receiver`).

**中文:** 把 Receiver 与动作绑定起来的 Command implementation。

**Italiano:** Un'implementation di Command che collega un Receiver a un'azione.

## Abstract Expression

**Meaning:** The contract for evaluating nodes in an Interpreter grammar.

**مصري:** عقد تقييم العقد اللي بتمثل قواعد `Interpreter`.

**中文:** 对 Interpreter 语法节点求值的约定。

**Italiano:** Il contratto per valutare i nodi della grammatica di Interpreter.

## Terminal Expression

**Meaning:** An expression with no child expressions.

**مصري:** تعبير مافيش جواه تعبيرات أطفال.

**中文:** 不含子表达式的表达式。

**Italiano:** Un'espressione senza espressioni figlie.

## Nonterminal Expression

**Meaning:** An expression that combines child expressions according to a grammar rule.

**مصري:** تعبير بيركب تعبيرات أصغر حسب قاعدة في اللغة.

**中文:** 按照语法规则组合子表达式的表达式。

**Italiano:** Un'espressione che combina espressioni figlie secondo una regola grammaticale.

## Context

**Meaning:** In Strategy and State, the object that uses a Strategy or delegates behavior to its current State. In Interpreter, the data expressions consult during evaluation, such as variable values or available roles.

**مصري:** في `Strategy` و `State`، دي الكائن اللي بيستخدم `Strategy`، أو بيفوّض تنفيذ السلوك (`behavior`) للحالة الحالية (`State`). في `Interpreter`، ده البيانات اللي الـ `expressions` بترجع لها وقت التقييم، زي قيم المتغيرات أو الأدوار المتاحة.

**中文:** 在 Strategy 和 State 中，指使用 Strategy 或把 behavior 委托给当前 State 的 object。在 Interpreter 中，指 expressions 求值时读取的数据，例如变量值或可用角色。

**Italiano:** In Strategy e State, l'object che usa una Strategy o delega il behavior allo State corrente. In Interpreter, sono i dati consultati dalle expressions durante la valutazione, per esempio i valori delle variabili o i ruoli disponibili.

## Aggregate

**Meaning:** The collection that provides access to iterators.

**مصري:** المجموعة اللي بتوفر `iterators` للمرور عليها.

**中文:** 提供 iterator 访问能力的集合。

**Italiano:** La raccolta che fornisce accesso tramite iterator.

## Concrete Iterator

**Meaning:** An implementation that stores a traversal position for a particular Aggregate.

**مصري:** تنفيذ (`implementation`) بيحفظ موضع المرور في مجموعة محددة (`Aggregate`).

**中文:** 为某种 Aggregate 保存遍历位置的 implementation。

**Italiano:** Un'implementation che conserva una posizione di attraversamento per un particolare Aggregate.

## Colleague

**Meaning:** An object whose interactions are coordinated by a Mediator.

**مصري:** كائن متعاون (`object`) بيتولى الـ `Mediator` تنسيق تعاملاته مع باقي الأطراف.

**中文:** 其交互由 Mediator 协调的 object。

**Italiano:** Un object le cui interazioni vengono coordinate da un Mediator.

## Concrete Mediator

**Meaning:** An implementation that contains the coordination rules for its Colleagues.

**مصري:** تنفيذ (`implementation`) بيجمع قواعد التنسيق بين الأطراف المتعاونة (`Colleagues`).

**中文:** 保存 Colleague 之间协调规则的 implementation。

**Italiano:** Un'implementation che contiene le regole di coordinazione dei Colleague.

## Originator

**Meaning:** The object that knows how to capture and restore its own state.

**مصري:** الكائن اللي يعرف يحفظ حالته (`state`) ويسترجعها.

**中文:** 知道如何保存和恢复自身 state 的 object。

**Italiano:** L'object che sa acquisire e ripristinare il proprio state.

## Caretaker

**Meaning:** The role that keeps a Memento without inspecting its private representation.

**مصري:** الدور اللي بيحتفظ بـ `Memento` من غير ما يفتش في تمثيلها الداخلي.

**中文:** 保存 Memento、但不检查其私有表示的角色。

**Italiano:** Il ruolo che conserva un Memento senza ispezionarne la rappresentazione privata.

## Subject

**Meaning:** The publisher whose changes are announced to registered Observers.

**مصري:** المصدر اللي بيعلن تغييراته للـ `Observers` المسجلين.

**中文:** 把自身变化通知给已注册 Observer 的发布方。

**Italiano:** Il publisher che comunica i propri cambiamenti agli Observer registrati.

## Concrete Observer

**Meaning:** An Observer implementation that reacts to notifications.

**مصري:** تنفيذ للمشترك (`Observer implementation`) بيحدد استجابته للإشعارات (`notifications`).

**中文:** 响应通知的 Observer implementation。

**Italiano:** Un'implementation di Observer che reagisce alle notifiche.

## Strategy interface

**Meaning:** The contract for interchangeable algorithms used by a Context.

**مصري:** عقد الـ `algorithms` القابلة للتبديل اللي `Context` بتستخدمها.

**中文:** Context 所使用的可替换 algorithm 的约定。

**Italiano:** Il contratto degli algorithm intercambiabili usati da un Context.

## Concrete Strategy

**Meaning:** A particular implementation of a Strategy interface, possibly a callable rather than a class.

**مصري:** تنفيذ محدد لعقد `Strategy interface`. ممكن تمثّله بحاجة قابلة للاستدعاء (`callable`)، ومش لازم يكون `class` مستقلة.

**中文:** Strategy interface 的一种具体 implementation，可以是 callable 而不必是 class。

**Italiano:** Una particolare implementation della Strategy interface, anche un callable invece di una class.

## Concrete State

**Meaning:** An implementation defining behavior and transitions for one State.

**مصري:** تنفيذ لحالة معينة (`Concrete State`) بيحدد سلوكها (`behavior`) والانتقالات المتاحة منها.

**中文:** 为某个 State 定义 behavior 和转换规则的 implementation。

**Italiano:** Un'implementation che definisce behavior e transizioni di uno State.

## Abstract Class (Template Method role)

**Meaning:** The Template Method role that owns the algorithm skeleton and declares variable steps.

**مصري:** دور `Template Method` اللي ماسك `algorithm skeleton` وبيعلن الخطوات المتغيرة.

**中文:** Template Method 中拥有 algorithm skeleton 并声明可变步骤的角色。

**Italiano:** Il ruolo di Template Method che contiene l'algorithm skeleton e dichiara i passi variabili.

## Concrete Class (Template Method role)

**Meaning:** The Template Method role that supplies the variable steps.

**مصري:** دور `Template Method` اللي بيوفر الخطوات المتغيرة.

**中文:** Template Method 中提供可变步骤的角色。

**Italiano:** Il ruolo di Template Method che fornisce i passi variabili.

## Element

**Meaning:** The contract for objects that accept a Visitor.

**مصري:** عقد الـ `objects` اللي بتقبل `Visitor`.

**中文:** 接受 Visitor 的 object 所提供的约定。

**Italiano:** Il contratto degli object che accettano un Visitor.

## Concrete Element

**Meaning:** An Element implementation that selects its matching Visitor overload.

**مصري:** تنفيذ للعنصر (`Element implementation`) بيختار الاستدعاء المناسب لنوعه من عمليات الزيارة (`Visitor overload`).

**中文:** 选择与自身类型匹配的 Visitor overload 的 Element implementation。

**Italiano:** Un'implementation di Element che seleziona l'overload di Visitor adatto al proprio tipo.

## Concrete Visitor

**Meaning:** A Visitor implementation containing one operation for every supported Element type.

**مصري:** تنفيذ للزائر (`Visitor implementation`) فيه عملية لكل نوع عنصر مدعوم (`Element`).

**中文:** 为每种受支持的 Element 类型提供操作的 Visitor implementation。

**Italiano:** Un'implementation di Visitor con un'operazione per ogni tipo Element supportato.

## Client (pattern role)

**Meaning:** Code that uses an interface or collaborates with a pattern's objects.

**مصري:** الكود اللي بيستخدم `interface` أو بيتعامل مع `objects` بتاعة الـ `Pattern`.

**中文:** 使用 interface 或与模式中的 object 协作的代码。

**Italiano:** Il codice che usa un'interface o collabora con gli object del pattern.

## Observer interface

**Meaning:** The callback contract implemented by subscribers.

**مصري:** عقد `callback` اللي المشتركين بينفذوه.

**中文:** 订阅方实现的 callback 约定。

**Italiano:** Il contratto di callback implementato dagli iscritti.

## State interface

**Meaning:** The contract through which a Context delegates state-dependent behavior.

**مصري:** العقد اللي `Context` بتفوّض من خلاله `behavior` المعتمدة على `state`.

**中文:** Context 用于委托与 state 有关的 behavior 的约定。

**Italiano:** Il contratto con cui un Context delega il behavior dipendente dallo state.
