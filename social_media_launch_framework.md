# Social Media Launch Framework

A reusable execution brief for generating a complete social-media launch pack from the project currently open in an AI coding assistant. Read this entire file before executing it. Produce finished copy and image files, not just a strategy, outlines, or image prompts.

## How to use this file

Place this file in any project, open that project in your assistant, and say:

> Read social_media_launch_framework.md completely and execute it for the current project. Inspect the source, documentation, logo, and assets. Generate the full social-media post pack using problem → method → result, and create the social preview images. Save the deliverables and give me their links.

You can also reference this file from another workspace and explicitly name the target project directory. The target is the project the user asks about; otherwise it is the active workspace. It is not automatically the repository containing this framework. Confirm the resolved target in a brief progress update before researching it.

This Markdown file is an instruction document, not a shell script. When asked to **edit the framework**, update its instructions. When asked to **execute the framework**, produce the project's launch pack. Copying it alone does not run anything.

## 1. Role and required outcome

Act as a technical copywriter and product storyteller who can inspect implementation evidence and create visual assets. Explain what matters to the project's actual audience in clear, specific language.

Deliver all of the following:

1. A project brief grounded in the target repository.
2. Complete copy for the platform set below, with distinct angles and usable calls to action.
3. Rendered social preview images based on the project description, logo when present, and relevant assets.
4. A seven-day suggested distribution plan mapped to the finished posts.
5. A manifest linking copy, evidence, images, image alternatives, and any remaining limitations.

Do not assume the project is a SaaS, open-source product, public release, or new launch. Adapt wording to its actual state: prototype, local tool, library, client project, portfolio, released application, or work in progress. Preparation does not post to external accounts, deploy changes, or commit and push them.

## 2. Discover the project before writing

Read applicable project instructions first, then inspect README files, manifests, documentation, main entry points, relevant implementations, tests or validation reports, and current status notes. Exclude dependencies, generated builds, private runtime data, credentials, and unrelated repositories.

Use implementation evidence to resolve stale documentation. Trace the advertised workflow far enough to distinguish implemented behavior from plans. Existing test reports are historical evidence; say when checks were actually run during this execution.

Discover the brand guide, theme tokens, typography, logo/favicon, screenshots, demo media, diagrams, and existing marketing assets. Open and visually inspect assets before selecting them. A filename is not sufficient evidence of what an image shows.

Extract a brief with:

| Field | What to establish |
| --- | --- |
| Project and ownership | Display name, author/team, actual role, project type |
| Audience | Who encounters the problem and in what situation |
| Problem | Specific friction in the original workflow |
| Method | How this implementation addresses the problem; significant decisions and tradeoffs |
| Result | Verified capability or measured outcome, with scope and limits |
| Current status | Working features, unfinished work, release/deployment state |
| Stack | Technologies relevant to the story, verified from source |
| Destinations | Real repository, demo, article, documentation, or contact URLs |
| Brand | Project logo, colors, fonts, tone, and relevant asset paths |
| Evidence | Source files, observations, or measurements supporting the claims |

Prefer the project's own branding. Do not transfer Sanfor's palette, name, metrics, links, or another project's screenshots into a different project unless the user requests that relationship.

Infer low-risk choices from available evidence and continue. Ask only when a missing fact materially changes the story and cannot be discovered. Optional overrides include target directory, audience, language, channels, CTA, and output location. Default to the project's established public language, or English if no language is established.

Keep missing facts out of public copy. Use an available repository or documentation link when no live demo exists. If no public destination exists, use a specific feedback question without a fake URL. Record omissions in the brief rather than leaving `[insert link]` in final posts.

## 3. Required narrative: problem → method → result

Every standalone post must contain these three elements naturally. A thread, carousel, or article must contain them across its full sequence; short teasers must still express the compact version.

- **Problem:** Who was struggling with what? What was difficult, repetitive, confusing, or missing?
- **Method:** What did the author implement or change? Explain the mechanism in language suitable for the audience.
- **Result:** What can someone do now, or what measured change was observed? Keep the scope honest.

Use a strong opening, that narrative, and one primary CTA. Titles and captions should say something specific about this project. A technology list alone is not a method, and “it works better” is not a result.

When no measured business outcome exists, describe a supported functional result: a task can now be completed, information stays connected, or a particular output is produced. Never turn that into an invented time saving, adoption count, revenue figure, reliability guarantee, or benchmark.

Example of the structure, not reusable project facts:

> Separate panoramas made it difficult to understand how rooms connected. I connected scenes with angular hotspots and a floor plan. The demo now lets visitors move between rooms while seeing their location on the map.

Do not invent a personal frustration, competitor failure, customer request, or user quote to make the story dramatic. If the origin is unknown, describe the observable problem directly.

## 4. Build the messaging foundation

Before producing channel copy, write:

- One sentence explaining the project to a new reader.
- A two-sentence summary identifying audience, method, and result.
- Three finished hooks: problem-led, implementation-led, and outcome-led.
- A short evidence-backed problem/method/result statement.
- One primary campaign CTA that matches the project's availability.

Use first person only when author ownership is established. Keep copy conversational, specific, and credible. Avoid generic hype, invented superlatives, engagement bait, repeated hashtag blocks, and claims that a campaign will go viral.

## 5. Generate the complete default post pack

Unless the user narrows the channels, write every deliverable below. Suggested lengths are editorial targets, not claims about current platform limits. Verify official format limits and community requirements at execution time when claiming compliance. If verification is unavailable, note that in the manifest and keep drafts conservative.

| ID | Deliverable | Required content |
| --- | --- | --- |
| LI-01 | LinkedIn launch post | About 150–230 words: specific hook, problem, implementation, result, CTA |
| LI-02 | LinkedIn technical follow-up | About 120–200 words: one decision, how it addresses the problem, demonstrated result and relevant limit |
| X-01 | X launch thread | Four complete numbered posts: problem, method, result/proof, next step and real destination |
| X-02 | X standalone announcement | Compact complete problem/method/result plus CTA; count the final text including numbering or tags where used |
| X-03 | X follow-up | A distinct lesson or workflow result, not a repeat of the announcement |
| RD-01 | Reddit project story | Title plus complete body, about 200–350 words; disclose authorship and ask one useful question |
| RD-02 | Reddit technical discussion | Different title/body, about 250–450 words; explain an actual tradeoff, method, outcome, and technical question |
| HN-01 | Hacker News submission package | Three factual title options, destination, and a complete author comment explaining problem, implementation, current result, and limits |
| DEV-01 | DEV Community article | Complete article, about 700–1,100 words: title, summary, problem, method, evidence, result, limitations, relevant links |
| FB-01 | Facebook launch post | About 100–180 words focused on a recognizable workflow and outcome |
| IG-01 | Instagram carousel package | Complete six-slide text plus caption: hook, problem, method, demonstration, result, CTA; name a matching visual for every slide |
| UP-01 | Cross-platform follow-up | Two finished lengths: short and medium; discuss a supported lesson/result and invite specific feedback |

Do not stop at the DEV article outline or just provide HN titles. A Show HN framing is appropriate only when the project fits the current guidelines and there is something people can meaningfully try. Otherwise provide a factual author introduction and mark the Show HN option as unsuitable in the handoff.

For Reddit, use audience-specific drafts and verify destination rules before naming them publication-ready for a community. Do not invent a posting history, imply unaffiliated recommendations, or suggest evading moderation. If a destination forbids the post, offer an appropriate alternative rather than a workaround.

When evidence cannot support a requested angle, choose another true angle. If a channel is unsuitable, still provide a clearly labeled general draft when useful and explain the eligibility limitation outside the copy.

### Required platform-specific tags

Include **Tags to use** for every post ID, including follow-ups. Select concrete tags from the target project's subject, implementation, audience, and the individual post's angle. Do not reuse this portfolio's tags automatically in other projects, add unrelated trending tags, or promise reach or virality.

Use these editorial defaults, adapting to verified destination rules:

| Platform | Required tag delivery and placement |
| --- | --- |
| LinkedIn | Select 2–3 relevant hashtags and include them at the end of each finished post. |
| X | Select 1–2 relevant hashtags per standalone post. For a thread, place the selected tags in the final post unless a specific earlier post needs one. Count tags, spaces, numbering, and URLs in each post's length. |
| Reddit | Supply relevant plain-language topic keywords and suggested post flair, explicitly conditional on the community offering and permitting it. Keep editorial keywords out of the copy and do not append a hashtag block. Confirm actual flair choices after selecting the community. |
| Hacker News | Supply descriptive topic keywords for choosing a factual title, not a hashtag block or an invented tag field. Mark these as editorial only and keep them out of the author comment. |
| DEV Community | Supply a short list of relevant native tag names separately for the article editor's tag field, not hashtags appended to the article. Verify current tag availability and limits before claiming publication readiness. |
| Facebook | Select 1–3 relevant hashtags and include them at the end of the finished post. |
| Instagram | Select 3–5 relevant hashtags and include them in the finished caption, not on every carousel slide. |
| Cross-platform follow-up | Name the intended channels for each length and include their selected hashtags in the copy. Explain any adaptation for native-tag or community destinations; do not provide a universal hashtag block for every channel. |

The counts above are campaign defaults, not platform limits or guaranteed optimization. Show the exact selected tags and where to use them, never just “add relevant hashtags.” Where hashtags are unsuitable, an explicit editorial-topics/flair entry satisfies the tag requirement; do not silently omit the platform.

Do not assume every platform makes body URLs clickable or supports the same CTA placement. Avoid “link in bio” unless that destination is actually configured; provide upload/publishing notes separately.

## 6. Format every deliverable for direct use

For each ID, provide:

1. Platform, purpose, and selected angle.
2. **Copy to publish:** the full post, with real links or a usable link-free CTA. Keep instructions and evidence annotations out of this block.
3. **Attachment:** exact output image path and meaningful alt text, or an explicit text-only designation.
4. **Publishing note:** any destination, formatting, or eligibility consideration.
5. **Internal evidence:** brief pointers supporting the problem, method, and result.
6. **Tags to use:** exact platform-specific hashtags, native tags, or editorial topics/conditional flair and their placement. Hashtags intended for publication must already appear inside the copy block; do not require the user to append them again.

Treat numbering, headings, hashtags, and URLs as part of the final copy when checking lengths. Split oversized copy at a meaningful boundary. Preserve readability and meaning while adapting to a platform.

Do not fabricate launch-week progress for a follow-up. Draft from already established facts; a future update requiring new evidence belongs in a separate idea list, not in the finished post pack.

## 7. Create actual social preview pictures

Image creation is part of executing this framework, even if no logo is found. Deliver final PNG/JPEG files, inspect them, and link them in the handoff. A prompt or design description alone is not a completed preview.

### Choose the visual from the project

1. Inspect the actual project logo and brand guidance when available. Preserve logo geometry, spelling, colors, aspect ratio, and required clear space.
2. Pick the strongest relevant screenshot, output example, diagram, or original asset that demonstrates the method or result.
3. Use a brief headline derived from the project description and one concise benefit supported by the evidence.
4. Place the project name/logo clearly, make the product evidence the main visual, and keep secondary author identity subordinate.
5. If no logo exists, use a clean project-name treatment. Creating a campaign does not require inventing a permanent logo.
6. If there is no graphical UI, show a real terminal result, sample output, or a clear technical illustration. Do not fabricate application screens, testimonials, ratings, or performance charts.

Use available design/rendering tools for precise compositions from existing logo, vector, code, or screenshot assets. When the task needs new raster illustration, use the available image-generation tool and its applicable skill; provide the inspected project references. Treat generated imagery as illustrative and keep authentic product evidence distinguishable. Follow the tool's editing constraints when modifying images.

### Default outputs

These dimensions are campaign export defaults, not universal platform requirements. Adapt to verified destination requirements when necessary.

| File | Default canvas | Purpose |
| --- | --- | --- |
| `social-preview-landscape.png` | 1200 × 630 | Main launch/share attachment |
| `social-preview-square.png` | 1080 × 1080 | Square feed attachment |
| `social-preview-portrait.png` | 1080 × 1350 | Portrait feed attachment |
| `github-social-preview.png` | 1280 × 640 | GitHub repository link preview; required when a GitHub repository is the destination |
| `carousel-01.png` through `carousel-06.png` | 1080 × 1350 each | Rendered slides matching IG-01 |

Create all selected-format outputs; by default, create the three previews and six carousel slides. The standalone portrait can reuse the carousel cover composition. Reflow each format deliberately instead of stretching a landscape layout. Omit formats only when the user narrows the deliverables.

### GitHub repository picture

For a GitHub project, also create `images/github-social-preview.png` and its editable source. Use the exact project display name, a concise description, the existing logo at its original aspect ratio, and a relevant diagram or sample output. Make this a distinct 1280 × 640 composition with safe margins and an opaque background. Inspect the exported PNG and verify it is under 1 MB. These are GitHub's recommended dimensions and upload size limit as checked on 2026-09-12; recheck the [official GitHub social preview guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview) for later executions.

Include the image, alt text, dimensions, byte size, source, and upload steps in `assets.md`: repository Settings → Social preview → Edit → Upload an image. Saving or committing the PNG does not apply the repository setting. Record upload status separately from image completion. Preserve the repository URL unless its remote rename is verified; a display-name change does not establish a new URL.

### Search keywords and campaign measurement

Create `keyword-tracking.md` and `metrics.csv` in the campaign folder. Derive search phrases from implemented features, audience questions, and existing guides. Map each phrase to a real document, a post ID, and a specific intent. Call them candidate keywords unless dated analytics or trend research supports a stronger claim. Do not describe terms as viral or promise ranking, reach, or growth without evidence.

When asked to update the README, use the exact display name, a clear descriptive opening, natural topic headings, useful internal links, and an unobtrusive link to the tracker. Avoid hashtag walls, repeated keywords, hidden metadata, and invented badges. Propose a GitHub About description and topic names in the handoff; distinguish proposed settings from changes actually applied.

Track publication time and post URL, keyword/hook, impressions, engagements, outbound clicks, and repository views/clones with observation windows and sources. Leave unavailable numbers empty, not zero. Separate platform clicks from repository traffic; GitHub does not provide per-keyword search analytics or automatic campaign attribution. Record a baseline before publication, then review after 24 hours and seven days. Treat comparisons with differing audiences or time windows as exploratory. Preserve dated observations so later campaigns can learn from actual results.

Use generous internal margins, legible text at phone size, intentional contrast, and minimal small copy. Keep essential content clear of crop edges. Never distort source artwork to fill a frame. Do not overwrite original logos or creative source assets.

Record alt text, actual dimensions, source paths, and illustrative/generated status in `assets.md`. Save editable composition files or the generation prompt and reproduction instructions. If an image tool fails, try a suitable available rendering approach within scope; if no approach is available, finish the copy, identify the exact missing capability, and mark image delivery incomplete rather than claiming success.

## 8. Suggested seven-day distribution

Map each suggested slot to a completed post ID, image, CTA, and the intended audience. Use Day 1 through Day 7 unless the user supplies dates/timezone. This is an editorial sequence, not a scheduled or published campaign.

Suggested sequence: launch, demonstrate a workflow, explain an engineering decision, invite community feedback, share the full article, revisit a verified lesson, then summarize and invite a concrete next step. Channels need not receive a post every day. Adapt the sequence to relevance and community rules.

Use actual audience analytics for timing advice when available. Otherwise label timing as a suggestion; do not claim a universally optimal hour or a schedule that defeats spam detection.

## 9. Output files and project portability

Default all generated campaign content to `Markting/` inside the target workspace. This spelling and capitalization are intentional. Put the first campaign's Markdown files, image exports, previews, validation reports, and reproduction sources there; do not default to `marketing/`, `markting/`, `public/`, or a folder outside the project. An explicit user output path overrides this default. If a previous campaign exists, preserve it and create a dated campaign subfolder inside `Markting/`. Keep temporary campaign captures under that campaign's `source/` directory. Do not modify application behavior to generate marketing material.

Save:

- `README.md`: pack index, target project, inspected revision/date when available, completion status, and links to every deliverable.
- `project-brief.md`: audience, positioning, current state, claims and supporting sources, unavailable facts.
- `posts.md`: every finished post from section 5, grouped by ID, including the complete DEV article, carousel text, and platform-specific Tags to use entries with hashtags already included in applicable copy blocks.
- `launch-plan.md`: the seven-day suggested sequence referencing those IDs.
- `assets.md`: image descriptions, alt text, source/provenance, dimensions, and reproduction instructions.
- `keyword-tracking.md` and `metrics.csv`: keyword-to-content map, proposed repository SEO settings, and dated measurement records with missing data left empty.
- `images/`: rendered previews and carousel slides.
- `source/`: editable layouts or prompts and any small supporting files needed to regenerate the visuals.

Resolve paths from the target workspace, not a hardcoded machine path. Do not require this portfolio, Astro, a particular owner, or a particular logo to execute the framework in another project. Reference project assets without moving or deleting their originals.

## 10. Quality gate and handoff

Before reporting completion:

- Verify the project identity, status, links, and ownership language against sources.
- Check every standalone post for problem, method, and supported result; check the full arc for sequences.
- Confirm all post IDs exist with actual copy and no unresolved variables or outline-only deliverables.
- Confirm every ID has Tags to use with exact relevant selections and placement. Check that public hashtags match the guidance, native tags remain separate, and Reddit/HN editorial topics are not pasted into the public copy. Recount final copy after adding tags.
- Check platform lengths and relevant eligibility where applicable; record anything unverified.
- Ensure measurements are sourced and proposed work is not described as already shipped.
- Open every exported visual; check text, logo fidelity, relevant assets, crop safety, contrast, and actual dimensions.
- Ensure every promised attachment exists and has alt text, and every manifest link resolves.
- Preserve previous work and keep temporary outputs separate from final assets.

Finish with a concise statement of the target project, the delivered post/image counts, links to `posts.md` and the pack index, a preview of the main image when supported, and any real remaining limitation. The files must contain the complete copy, so the user can immediately select and publish a post.
