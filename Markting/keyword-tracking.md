# Search keywords, SEO, and launch measurement

These are **candidate search phrases**, derived from repository content, not verified trending or viral keywords. No search-volume or campaign analytics were supplied. The README now uses a descriptive introduction, useful topic links, and a runnable quick start. This follows [Google's people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content); it does not establish a ranking improvement.

## Keyword-to-content map

| Candidate phrase | Reader intent | Relevant destination | Post IDs | Status |
| --- | --- | --- | --- | --- |
| 23 design patterns | Find the complete catalog | [README](../README.md) | LI-01, X-02 | Candidate; unmeasured |
| GoF design patterns C++ | Learn GoF through code | [build guide](../CPP_EXAMPLES.md) | X-01, DEV-01 | Candidate; unmeasured |
| design patterns C++20 examples | Run modern C++ examples | [build guide](../CPP_EXAMPLES.md) | FB-01, HN-01 | Candidate; unmeasured |
| Strategy pattern C++ example | Understand interchangeable algorithms | [Strategy](../behavioral/strategy/README.md) | LI-02, X-03, IG-01, UP-01 | Candidate; unmeasured |
| Strategy vs State | Choose between related patterns | [comparisons](../COMPARISONS.md) | Future content angle; no post claimed |
| design patterns cheat sheet | Review responsibilities and trade-offs | [cheat sheet](../CHEATSHEET.md) | LI-01, DEV-01 | Candidate; unmeasured |
| design patterns interview preparation | Explain trade-offs in interviews | [learning path](../LEARNING_PATH.md) | RD-01 | Candidate; unmeasured |
| شرح Design Patterns بالمصري | Read explanations in Egyptian Arabic | [Arabic catalog](../README.ar-EG.md) | LI-01, FB-01 | Candidate; unmeasured |
| C++ 设计模式 | Read Simplified Chinese explanations | [Chinese catalog](../README.zh-CN.md) | X-01 | Candidate; unmeasured |
| design pattern C++ italiano | Read Italian explanations | [Italian catalog](../README.it.md) | FB-01 | Candidate; unmeasured |

## Proposed GitHub About settings

**Description:** Learn all 23 GoF design patterns with runnable C++20 examples, diagrams, trade-offs, and explanations in English, Egyptian Arabic, Chinese, and Italian.

**Topics:** `design-patterns`, `gof`, `cpp`, `cpp20`, `object-oriented-programming`, `software-design`, `learning-resources`, `interview-preparation`.

These are proposals; no remote settings were changed. The display name is **23 Design Patterns**, while the existing repository slug remains `Design-Patterns-23`. Update destinations only after a remote rename is completed and verified.

## Record observations

Use [metrics.csv](metrics.csv). Empty metrics mean unavailable or not collected, not zero. Preserve raw exports or screenshots with observation dates when available, without committing private account information.

1. Before publishing, record the baseline window and available repository views, unique visitors, clones, and total stars. Keep repository rows separate from post rows.
2. At publication, record post ID, actual URL, candidate phrase, hook, and publication timestamp including timezone.
3. At 24 hours and seven days, add new rows with source, exact observation window, impressions, engagements, outbound clicks, and meaningful replies where available.
4. Compare like-for-like platform definitions and windows. Calculate click-through rate as outbound clicks / impressions only when both measures are available for that same post and period. Engagement rate is engagements / impressions under the platform's documented definition. Zero impressions yields no rate.
5. Record a conclusion and the next experiment. Test one hook or subject change at a time when practical; different audiences and timing still limit causal conclusions.

[GitHub Traffic](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository) provides recent views/clones, popular content, and referring sites; the visitor and clone history covers 14 days, so preserve observations regularly. Its data uses UTC. Referrer reporting excludes search engines and GitHub itself: it is not a search-keyword analytics report.

Repository traffic cannot automatically identify which campaign keyword drove a visit. UTM parameters alone do not create GitHub campaign reporting. Use native post analytics for clicks and label repository changes as coincident observations, not attributed conversions. Google Search Console would require a separate site you can verify; this pack does not install it on github.com.

## Weekly decision log

| Review | Evidence available | Decision |
| --- | --- | --- |
| 2026-09-12 preparation | Repository source and fresh example checks; no audience analytics | Start with the concrete Strategy workflow; collect baseline before posting |

Do not label a keyword viral from a single post or an increase without a comparable baseline. Keep useful educational content as the reason for each keyword, following [Google's advice on natural link text](https://developers.google.com/search/docs/crawling-indexing/links-crawlable).
