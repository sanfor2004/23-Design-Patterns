# Pattern recognition practice

[Learning Path](LEARNING_PATH.md) · [Catalog](README.md)

Try these without opening the catalog. Name a possible Design Pattern, explain why it might help, and suggest a simpler alternative. More than one design can fit. Ask what must change before choosing.

1. A document tool often adds export operations, but its paragraph, image, and table types rarely change.
2. An old sensor API uses different temperature units from the rest of the service.
3. An editor needs checkpoints without exposing its private representation to the history manager.
4. Checkout callers choose different shipping calculations while the total workflow stays the same.
5. Several form fields jointly determine which controls are enabled. Calls between fields are spreading.
6. A theme switch must create matching buttons and panels. Independent choices keep producing mixed themes.
7. A menu action must be queued now, executed later, and retained for undo.
8. A large map repeats terrain descriptions. Measurements show this data dominates memory.
9. Independent views need stock updates and can join or leave while the application runs.
10. A reporting base Class fixes the read, format, and finish sequence. Subclasses customize selected steps.
11. Files and folders must answer the same size query. Folders contain more folders.
12. A job has a shared workflow, but subclasses choose which transport Object it creates.
13. Loading every thumbnail is expensive, and most are never displayed. Keep the existing display Interface.
14. Request options are collected over several screens and validated before creating a finished request.
15. A device responds differently when ready, busy, or faulted. Several operations repeat those conditions.
16. Callers need independent traversal positions in a custom collection without knowing its storage.
17. A game spawns enemies by copying selected configurations, leaving the originals unchanged.
18. Authentication and spending checks vary by entry point. A failed check must stop later checks.
19. Notices vary in urgency and channel. One subclass for every combination is becoming difficult.
20. Callers repeat stock, payment, and dispatch steps and keep getting their order wrong.
21. A stream needs optional compression and buffering layers while preserving its Interface.
22. Small access rules are trees of role checks, AND, and OR, evaluated against a user's roles.
23. A system claims it needs one process-wide counter accessible from anywhere. What justifies that requirement?
24. One function has a readable `if` for two stable cases. Is a pattern useful yet?

Write your reasoning before reading the [discussion notes](PRACTICE_NOTES.md). Then change one constraint: frequent new types, large snapshots, strict notification order, or a single fixed Dependency can change your answer.
