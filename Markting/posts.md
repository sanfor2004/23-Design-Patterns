# 23 Design Patterns — launch posts

Prepared 2026-09-12. These are finished drafts, not published posts. First-person drafts are for Sanfor2004, the repository owner. Community selection, rules, account permissions, and native tag availability still require a publishing-time check. The repository URL comes from the configured remote; public availability could not be independently fetched during preparation.

## LI-01 — LinkedIn launch

Purpose/angle: introduce a problem-first learning resource.

**Copy to publish:**

```text
Knowing a design pattern's name is easier than knowing when to use it.

23 Design Patterns is a C++20 learning repository built around that gap. Each pattern starts with a concrete problem, examines a naive solution, and explains where the design begins to strain before introducing the abstraction.

You can follow the responsibilities in a diagram, run a standalone example, compare its expected output, and try a small challenge. The explanations are available in English, Egyptian Arabic, Simplified Chinese, and Italian, with technical terminology kept in English.

The goal is a practical decision: can you explain what this pattern makes easier to change, and what complexity it adds?

Start with Strategy. The example gives a checkout an interchangeable shipping rule, so standard and express policies produce different totals without rewriting the checkout calculation. Then read the trade-offs before deciding whether the same separation helps your code.

Explore the learning path and choose one example to run:
https://github.com/sanfor2004/Design-Patterns-23

#DesignPatterns #CPP #SoftwareDesign
```

**Attachment:** [images/social-preview-landscape.png](images/social-preview-landscape.png). Alt: “23 Design Patterns, runnable C++20 in four documentation languages, with a Strategy diagram connecting Checkout to an interchangeable shipping rule.”

**Publishing note:** Paste as a native post; upload the image separately.

**Internal evidence:** [catalog](../README.md), [learning path](../LEARNING_PATH.md), [Strategy source](../behavioral/strategy/cpp/main.cpp).

**Tags to use:** #DesignPatterns #CPP #SoftwareDesign, already at the end.

## LI-02 — LinkedIn technical follow-up

Purpose/angle: show a concrete representation choice.

**Copy to publish:**

```text
A Strategy example does not need a class hierarchy to show an interchangeable algorithm.

In 23 Design Patterns, Checkout receives a ShippingRule represented by std::function<int(int)>. The client supplies a standard or express lambda. Checkout::total() adds the selected shipping cost to the subtotal.

This makes the variation visible: the checkout calculation stays in one place while the supplied policy changes. For a subtotal of 40, the example prints 45 for standard shipping and 55 for express. The express policy returns free shipping when the subtotal reaches 100.

There is a boundary to the lesson. A callable keeps this example small, but it does not model every ownership, allocation, or performance concern in a larger application. The output checks validate the demonstration, not every possible input.

Read the Strategy article, run the example, and try its challenge:
https://github.com/sanfor2004/Design-Patterns-23

#CPP #DesignPatterns
```

**Attachment:** [images/carousel-04.png](images/carousel-04.png). Alt: “Same checkout, different totals: Standard 45, Express 55, Express large 120; expected output from the Strategy example.”

**Publishing note:** Technical follow-up; do not present this as a performance benchmark.

**Internal evidence:** [Strategy source](../behavioral/strategy/cpp/main.cpp), [expected output](../behavioral/strategy/cpp/expected.txt), [test scope](../CPP_EXAMPLES.md).

**Tags to use:** #CPP #DesignPatterns, already at the end.

## X-01 — X launch thread

Purpose/angle: move from memorization to a runnable example.

**Copy to publish — post 1:**

```text
1/4 A pattern name does not tell you when to use it. 23 Design Patterns connects each GoF pattern to a concrete problem, a diagram, and a runnable C++20 example.
```

**Copy to publish — post 2:**

```text
2/4 Start with Strategy: Checkout receives a ShippingRule. Standard and express lambdas change the shipping policy while Checkout::total() keeps the shared calculation in one place.
```

**Copy to publish — post 3:**

```text
3/4 Run the example and compare: Standard: 45; Express: 55; Express large: 120. Then read the trade-offs and try the challenge. Explanations come in English, Egyptian Arabic, Simplified Chinese, and Italian.
```

**Copy to publish — post 4:**

```text
4/4 Pick one pattern whose problem you recognize. Read why it exists, run its C++20 example, and decide whether the extra structure helps your code.
https://github.com/sanfor2004/Design-Patterns-23
#DesignPatterns #CPP
```

**Attachment:** Post 1: [images/social-preview-landscape.png](images/social-preview-landscape.png), same alt text as LI-01. Posts 2–4: text only.

**Publishing note:** Publish in order as replies. Raw Unicode character counts, including literal URLs, are recorded in [validation.md](validation.md); platform-weighted counting is not claimed.

**Internal evidence:** [Strategy](../behavioral/strategy/README.md), [catalog](../README.md).

**Tags to use:** #DesignPatterns #CPP, already in post 4 only.

## X-02 — X announcement

Purpose/angle: concise introduction.

**Copy to publish:**

```text
Pattern names are easy to memorize, harder to apply. 23 Design Patterns pairs GoF explanations with runnable C++20 and diagrams so you can trace the trade-offs. Explore:
https://github.com/sanfor2004/Design-Patterns-23
#DesignPatterns #CPP
```

**Attachment:** [images/social-preview-landscape.png](images/social-preview-landscape.png), same alt text as LI-01.

**Publishing note:** Alternative to the thread for an initial announcement; avoid posting both together.

**Internal evidence:** [catalog](../README.md), [build guide](../CPP_EXAMPLES.md).

**Tags to use:** #DesignPatterns #CPP, already at the end.

## X-03 — X follow-up

Purpose/angle: focus on one design decision.

**Copy to publish:**

```text
Shipping policies change. In the Strategy example, Checkout takes a callable rule, so standard and express totals share one calculation. Run it and inspect the boundary:
https://github.com/sanfor2004/Design-Patterns-23
#CPP
```

**Attachment:** Text only.

**Publishing note:** Use after the launch, with no claim about campaign results.

**Internal evidence:** [Strategy source](../behavioral/strategy/cpp/main.cpp).

**Tags to use:** #CPP, already at the end.

## RD-01 — Reddit project story

Purpose/angle: feedback from learners.

**Copy to publish:**

```text
Title: A problem-first guide to the 23 GoF patterns, with runnable C++20 examples

I'm the maintainer of 23 Design Patterns, a learning repository covering the 23 Gang of Four patterns. I'd like feedback on whether its structure helps people move from recognizing a pattern to deciding when to use it.

The gap I want the material to address is concrete: a class diagram can show the finished design without explaining what made that structure useful. Each article therefore starts with a problem and a naive solution before introducing the pattern. It also includes responsibilities, trade-offs, situations where the pattern is a poor fit, interview vocabulary, and a mini challenge.

Each pattern has a standalone C++20 program and an expected-output file. You can build the examples with CMake and use CTest to compare the demonstrated output. The articles are available in English, Egyptian Arabic, Simplified Chinese, and Italian; the code and technical terms stay consistent across them.

For example, Strategy uses a checkout with an injected shipping rule. Standard and express lambdas change the policy while the shared calculation remains in Checkout::total(). This gives the diagram something observable to explain.

These are small teaching programs, not production libraries. The output tests cover the demonstrated cases, and the examples don't establish that a pattern is the right choice for every related problem.

Repository: https://github.com/sanfor2004/Design-Patterns-23

Which pattern would benefit most from a stronger naive-solution example, and what change would you use to expose its limitation?
```

**Attachment:** Text only.

**Publishing note:** General draft for a programming-learning community. No subreddit rules or flair options were verified; select a destination and check its self-promotion rules first.

**Internal evidence:** [Strategy article](../behavioral/strategy/README.md), [contribution guidance](../CONTRIBUTING.md).

**Tags to use:** Editorial topics: design patterns, C++20, learning resources. Suggested flair: “Project” only if offered and permitted; do not paste keywords into the post.

## RD-02 — Reddit technical discussion

Purpose/angle: callable Strategy versus interface-based teaching.

**Copy to publish:**

```text
Title: Teaching Strategy in C++20 with a callable: what does the small example leave out?

I maintain 23 Design Patterns, and one teaching decision in its Strategy example is to represent the policy as std::function<int(int)> rather than an abstract base class with concrete strategy subclasses.

The problem being modeled is shipping variation. Checkout needs to compute a total, while the shipping policy can be standard or express. Repeating the calculation for each policy would mix the shared work with the changing rule.

The example defines ShippingRule as the callable type and receives it through Checkout's constructor. Checkout::total() checks the subtotal and adds shipping_(subtotal). The client supplies two lambdas: standard shipping returns 5; express shipping returns 15 below a subtotal of 100 and zero at or above that threshold.

The resulting program is short enough to inspect as a complete example. It prints Standard: 45, Express: 55, and Express large: 120. The repository includes that expected output and a CTest comparison, so readers can connect the design to visible behavior.

The tradeoff is in what this representation emphasizes. It makes the interchangeable algorithm easy to see, but it gives less space to explicit interface contracts and object lifetime discussions than a hierarchy would. It also doesn't demonstrate or measure the runtime costs of std::function. Those costs should not be inferred from a three-line output sample.

My current preference for this example is to keep the first lesson focused on where the policy enters the calculation, then use the explanation and challenge to discuss the design boundary. The repository also includes the other GoF patterns, diagrams, and four documentation languages for readers who want to compare approaches.

Source and explanation: https://github.com/sanfor2004/Design-Patterns-23

When teaching this particular example, what requirement would you introduce first to make an explicit strategy interface worth showing alongside the callable version?
```

**Attachment:** Text only.

**Publishing note:** General C++ discussion draft. Check the chosen community's promotion and discussion requirements before posting; this is not a verified subreddit submission.

**Internal evidence:** [Strategy source](../behavioral/strategy/cpp/main.cpp), [expected output](../behavioral/strategy/cpp/expected.txt).

**Tags to use:** Editorial topics: C++20, Strategy, std::function, software design. Suggested flair: “Discussion” only if the destination offers and permits it.

## HN-01 — Hacker News submission package

Purpose/angle: factual introduction to runnable educational material.

**Copy to publish — choose one title:**

1. 23 Design Patterns: GoF explanations with runnable C++20 examples
2. A problem-first guide to GoF patterns in four documentation languages
3. Learning GoF patterns through small C++20 programs and expected output

**Destination:** https://github.com/sanfor2004/Design-Patterns-23

**Copy to publish — author comment:**

```text
I'm the maintainer. This repository connects each GoF pattern to a concrete problem, a naive solution, a diagram, and a complete C++20 example. The intent is to help readers explain why the abstraction exists before copying its structure.

There are 23 examples, each with expected output and a CMake/CTest workflow. Documentation is available in English, Egyptian Arabic, Simplified Chinese, and Italian. Strategy is a small place to start: Checkout receives a shipping callable, and standard/express lambdas change the policy while sharing the total calculation.

The examples are teaching material. Output checks validate demonstrated cases, not production readiness, performance, or every input. I'd especially value feedback on examples where the naive solution doesn't make the eventual trade-off clear enough.
```

**Attachment:** Text only; [images/github-social-preview.png](images/github-social-preview.png) is for repository sharing elsewhere, not an HN upload.

**Publishing note:** Use a regular submission. No Show HN claim is made for this documentation-led launch; [Show HN guidance](https://news.ycombinator.com/showhn.html) excludes general reading material and stresses a substantive artifact people can try. The runnable examples alone do not establish eligibility for this specific submission. Author should be available to answer questions.

**Internal evidence:** [catalog](../README.md), [build guide](../CPP_EXAMPLES.md).

**Tags to use:** Editorial title topics only: GoF, C++20, design patterns, education. HN has no tag field in this package.

## DEV-01 — DEV Community article

Purpose/angle: teach the repository's workflow through Strategy.

**Tags to use:** `cpp`, `designpatterns`, `beginners`, `programming`, supplied separately for the editor. Availability and current native-tag limits were not verified.

**Copy to publish:**

```markdown
# Learn the problem before the pattern: a C++20 Strategy walkthrough

Summary: 23 Design Patterns connects the Gang of Four patterns to concrete problems, diagrams, runnable C++20 programs, and expected output. Here is how one shipping example turns a pattern name into a design decision.

## The gap between recognition and use

Recognizing a diagram is only one part of learning a design pattern. The harder question is why a program should take that shape. What is changing? Which responsibility needs to move? What becomes easier to understand, and what becomes harder?

I maintain 23 Design Patterns to give those questions a concrete setting. Each article begins with a problem and a naive solution before presenting the pattern. The explanation then connects responsibilities to code, output, trade-offs, and a mini challenge. The result is a sequence readers can inspect instead of a structure they are asked to accept on its name alone.

The repository covers all 23 GoF patterns. Its documentation is available in English, Egyptian Arabic, Simplified Chinese, and Italian. Technical terminology and code identifiers stay in English so readers can connect the explanation to the source and to conversations about software design.

## Find the changing policy

The Strategy example models checkout shipping. The shared job is to add a shipping cost to a subtotal. The changing part is the rule that determines that cost.

Standard shipping costs 5. Express shipping costs 15 when the subtotal is below 100 and is free when the subtotal reaches that threshold. Those rules are deliberately small. Their purpose is to make the variation easy to see without requiring a larger application around it.

If every shipping option owned a separate copy of the total calculation, changing the shared calculation would involve repeated work. The design instead gives Checkout one responsibility for calculating the total and receives the shipping decision from outside.

## Represent the algorithm as a callable

The source defines ShippingRule as std::function<int(int)>. Checkout stores one of these callables, receives it through its constructor, and rejects an empty rule. Its total() method rejects a negative subtotal and then returns the subtotal plus the result of the shipping rule.

The client constructs two checkout objects. One receives a lambda that returns the standard cost. The other receives a lambda that implements the express threshold. Both objects use the same Checkout::total() implementation.

This is the central Strategy relationship: the context uses an interchangeable algorithm supplied by its client. The example does not need an inheritance hierarchy to make that relationship visible. In this implementation, a callable is enough to express the varying policy.

That choice has a teaching boundary. It keeps the first example compact, but it does not settle how a larger application should model strategy state, lifetimes, or performance. It also does not measure the costs of std::function. Those questions need requirements and evidence beyond this demonstration.

## Connect the diagram to visible behavior

The diagram follows Checkout::total() to ShippingRule and then to the standard or express lambda. The source follows the same path, so the names in the visual have concrete counterparts in the program.

Running the example produces:

    Standard: 45
    Express: 55
    Express large: 120

The first two lines use a subtotal of 40. The third uses 120, where the express shipping rule returns zero. Readers can therefore trace each printed number back to a specific policy decision.

The repository stores these lines in expected.txt beside main.cpp. CTest runs each example and compares its output with the corresponding file, normalizing Windows line endings. That check catches differences in the demonstrated behavior. It is not a substitute for testing every input or for evaluating production requirements.

## Try the workflow yourself

With a C++20 compiler and CMake 3.20 or newer, configure the repository, build the examples, and run the output checks:

    cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
    cmake --build build --config Debug
    ctest --test-dir build -C Debug --output-on-failure

On Windows, use a Visual Studio developer shell with the C++ build tools installed. The build guide explains configuration choices and how to build just one pattern.

For a first exercise, read Strategy's problem and naive solution before the source. Predict the three totals, run the program, and explain which part changes when a shipping policy changes. Then try the article's mini challenge and compare the responsibilities again.

The useful result is not merely a program that compiles. It is an explanation you can defend: the shipping policy varies independently of the shared total calculation, and the client chooses the policy. You can then judge whether that separation earns its place in your own code.

## Use the same questions on the next pattern

The learning path, cheat sheet, relationship map, and comparisons provide other ways into the repository. Use them when two patterns seem similar or when you need a smaller starting point.

These examples are educational, not a production pattern library. Begin with a problem you recognize, inspect the trade-offs, and keep the simpler solution when the extra structure does not help.

Explore [23 Design Patterns](https://github.com/sanfor2004/Design-Patterns-23) and start with the Strategy article linked from the catalog.
```

**Attachment:** [images/social-preview-landscape.png](images/social-preview-landscape.png), same alt text as LI-01.

**Publishing note:** Paste the Markdown article into the editor and set native tags separately. Preview code blocks and cover cropping before publishing.

**Internal evidence:** [Strategy article](../behavioral/strategy/README.md), [source](../behavioral/strategy/cpp/main.cpp), [build guide](../CPP_EXAMPLES.md), [output comparator](../cmake/CheckOutput.cmake).

## FB-01 — Facebook launch

Purpose/angle: approachable learning workflow.

**Copy to publish:**

```text
Ever recognize a design pattern diagram but struggle to explain why the code needs it?

23 Design Patterns connects that diagram to a concrete problem, a simple first solution, and a runnable C++20 example. Each article includes the expected output and the trade-offs, so you can follow the design and decide when the extra structure helps.

The explanations come in English, Egyptian Arabic, Simplified Chinese, and Italian. Start with Strategy: a checkout receives a shipping rule, and changing the supplied policy changes the total while keeping the calculation in one place.

Choose one pattern, run its example, and try its mini challenge:
https://github.com/sanfor2004/Design-Patterns-23

#DesignPatterns #LearnProgramming
```

**Attachment:** [images/social-preview-square.png](images/social-preview-square.png). Alt: “23 Design Patterns on a warm paper background, with the Strategy shipping-policy diagram and four documentation languages.”

**Publishing note:** Check group-specific promotional rules if sharing to a group.

**Internal evidence:** [catalog](../README.md), [Strategy article](../behavioral/strategy/README.md).

**Tags to use:** #DesignPatterns #LearnProgramming, already in the copy.

## IG-01 — Instagram six-slide carousel

Purpose/angle: demonstrate the path from problem to observable output.

**Copy to publish — slide text and matching visual:**

| Slide / image | Heading | Supporting copy | Alt text |
| --- | --- | --- | --- |
| [01](images/carousel-01.png) | Learn the change. Then the pattern. | 23 Design Patterns. Runnable C++20 • Diagrams • Four languages. | A problem-first introduction to 23 Design Patterns with a Strategy diagram. |
| [02](images/carousel-02.png) | A diagram alone is not a decision. | What changes? Who owns it? Read the motivation, naive solution, and trade-offs. | Questions about change and ownership above the Checkout-to-ShippingRule diagram. |
| [03](images/carousel-03.png) | Give shipping its own rule. | Strategy: Checkout + ShippingRule. One checkout receives a standard or express policy. | Strategy separates the checkout calculation from an interchangeable shipping policy. |
| [04](images/carousel-04.png) | Same checkout. Different totals. | Standard: 45. Express: 55. Express large: 120. Expected output from the Strategy C++20 example. | Three actual expected totals from the standard and express shipping example. |
| [05](images/carousel-05.png) | Read it. Run it. Change the rule. | 23 examples with expected output. Compare behavior, then judge the abstraction. | A learning workflow that connects reading, execution, and policy changes. |
| [06](images/carousel-06.png) | Start with Strategy. | Explore 23 Design Patterns. Choose one pattern. Run its example. Try its challenge. | Invitation to begin with the Strategy example in 23 Design Patterns. |

**Copy to publish — caption:**

```text
A pattern name does not explain the decision behind it.

23 Design Patterns starts with concrete problems, then connects the design to runnable C++20 and expected output. In Strategy, a checkout receives a shipping rule: standard and express policies change the result while the shared calculation stays in one place.

Swipe through the example, then explore the repository at github.com/sanfor2004/Design-Patterns-23 and start with Strategy.

#DesignPatterns #CPP #SoftwareDesign #LearnProgramming
```

**Attachment:** All six linked PNGs in numerical order; alt text in the table.

**Publishing note:** The caption supplies a readable destination, not a claim that body links are clickable. No “link in bio” assumption. If configuring a profile link later, update the caption to match that actual setup.

**Internal evidence:** [Strategy source](../behavioral/strategy/cpp/main.cpp), [expected output](../behavioral/strategy/cpp/expected.txt), [catalog](../README.md).

**Tags to use:** #DesignPatterns #CPP #SoftwareDesign #LearnProgramming, already in the caption only.

## UP-01 — Cross-platform follow-up

Purpose/angle: revisit a verified lesson without inventing launch progress.

**Copy to publish — short, X:**

```text
A diagram leaves the result abstract. The Strategy example pairs a shipping-policy diagram with C++20 and expected totals so you can trace the change. Which rule would you try next?
https://github.com/sanfor2004/Design-Patterns-23
#CPP
```

**Copy to publish — medium, LinkedIn/Facebook:**

```text
A useful pattern explanation should connect responsibilities to something you can observe.

In 23 Design Patterns, the Strategy diagram leads from Checkout::total() to a ShippingRule supplied by the client. The C++20 program then shows how standard and express shipping produce different totals through the same calculation.

The source, diagram, and expected output give readers three ways to inspect that relationship. The trade-offs section helps them judge whether the same separation belongs in their own program.

Explore the example: https://github.com/sanfor2004/Design-Patterns-23

Which shipping rule would you add to test where this design starts to strain?

#DesignPatterns #CPP
```

**Attachment:** Short: text only. Medium: [images/social-preview-portrait.png](images/social-preview-portrait.png). Alt: “23 Design Patterns with a Strategy diagram showing an interchangeable shipping policy, in a portrait composition.”

**Publishing note:** Choose one appropriate length per channel. For Reddit or DEV, adapt to native formats and remove hashtags; the supplied versions target X, LinkedIn, and Facebook only.

**Internal evidence:** [Strategy article](../behavioral/strategy/README.md), [source](../behavioral/strategy/cpp/main.cpp).

**Tags to use:** Short #CPP; medium #DesignPatterns #CPP. Both are already included.
