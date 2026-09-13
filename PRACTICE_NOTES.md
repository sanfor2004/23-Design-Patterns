# Recognition practice discussion

[Try the scenarios first](PRACTICE.md). These are possible answers, not automatic rules.

| Scenario | Possible direction | What to question |
| --- | --- | --- |
| 1 | Visitor | New element types affect every Visitor. A direct operation can be simpler. |
| 2 | Adapter | If you own both APIs, could one consistent Interface remove the mismatch? |
| 3 | Memento | Large snapshots are costly; inverse operations may be cheaper. |
| 4 | Strategy | A callable can represent the Algorithm. One stable `if` may be enough. |
| 5 | Mediator | Keep coordination focused; one callback may be enough. |
| 6 | Abstract Factory | A family matters when products should vary together. |
| 7 | Command | A callable can cover queuing. Undo needs saved information and an order policy. |
| 8 | Flyweight | Share immutable intrinsic state, keep position separate, and measure lookup overhead. |
| 9 | Observer | Define unsubscribe, Lifetime, exception, and ordering behavior. |
| 10 | Template Method | Injected callables may fit steps that vary independently or change order. |
| 11 | Composite | Both leaves and groups need a meaningful common operation. |
| 12 | Factory Method | This is an inherited creation step; a free factory function needs less structure. |
| 13 | Proxy | Lazy creation moves cost and failure to first use. |
| 14 | Builder | Named arguments may suffice when construction does not happen in stages. |
| 15 | State | A small enum and transition table may remain clearer. |
| 16 | Iterator | Prefer existing iteration protocols, iterators, or ranges. |
| 17 | Prototype | Decide what to copy and share. Assignment may not create a new Object. |
| 18 | Chain of Responsibility | Define the end-of-chain policy. Two fixed checks may need only a function. |
| 19 | Bridge | Two independent dimensions justify the separation. |
| 20 | Facade | A simpler entry point does not guarantee rollback or a transaction. |
| 21 | Decorator | Layers must preserve the contract; order can affect results. |
| 22 | Interpreter | Evaluation of a small grammar is separate from parsing a full language. |
| 23 | Singleton, only with a real invariant | One application-owned instance passed explicitly often avoids hidden dependencies. One instance does not imply thread safety. |
| 24 | Keep the simple code | A hypothetical future change is not enough reason to add an abstraction. |

For a one-minute answer, explain the problem, the changing responsibility, your design choice, its cost, and when you would remove it.
