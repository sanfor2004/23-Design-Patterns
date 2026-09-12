# Image assets and reproduction

Ten campaign PNGs were rendered from editable HTML/CSS and existing SVG assets. They are technical compositions, not AI-generated illustrations, application screenshots, or performance charts. All ten exports and the refreshed repository preview were visually inspected for spelling, crop safety, proportions, and legibility.

## Provenance

- [Original logo](../assets/brand/logo.svg): unmodified SVG geometry and orange strokes, rendered at the original 56:38 aspect ratio. [Brand guidance](../assets/brand/README.md) and [license exception](../LICENSE) still apply.
- [Strategy diagram](../assets/diagrams/strategy.svg): embedded unchanged, inspected before use. It connects Checkout::total(), ShippingRule, and standard/express lambdas.
- [Expected output](../behavioral/strategy/cpp/expected.txt): source for slide 04's totals; all example output tests passed during this execution.
- [Renderer](source/render.cjs): editable layout, campaign text, SVG embedding, and PNG export logic. Each export has a corresponding editable HTML below.
- [Source inspection image](source/source-assets.png): preview of the actual logo and diagram used for selection.

## GitHub upload

Use [github-social-preview.png](images/github-social-preview.png): **1280 × 640, 51,323 bytes**, opaque PNG. In repository **Settings → Social preview → Edit → Upload an image**, select this file. The image is ready; this setting has **not** been applied.

The file is below GitHub's 1 MB limit and uses its recommended 1280 × 640 size. See [official GitHub guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview), checked 2026-09-12. Uploading a file to the repository alone does not configure the preview.

## Export inventory

| PNG | Dimensions | Alt text | Editable layout |
| --- | --- | --- | --- |
| [GitHub preview](images/github-social-preview.png) | 1280 × 640 | 23 Design Patterns: GoF patterns with runnable C++20, four documentation languages, and a Strategy shipping-policy diagram. | [HTML](source/github-social-preview.html) |
| [Landscape](images/social-preview-landscape.png) | 1200 × 630 | 23 Design Patterns on warm paper, with the original Sanfor logo and a diagram connecting Checkout to an interchangeable shipping rule. | [HTML](source/social-preview-landscape.html) |
| [Square](images/social-preview-square.png) | 1080 × 1080 | 23 Design Patterns, runnable C++20, four documentation languages, and the Strategy diagram in a square layout. | [HTML](source/social-preview-square.html) |
| [Portrait](images/social-preview-portrait.png) | 1080 × 1350 | 23 Design Patterns and its Strategy shipping-policy diagram in a portrait composition. | [HTML](source/social-preview-portrait.html) |
| [Carousel 01](images/carousel-01.png) | 1080 × 1350 | Learn the change, then the pattern: a problem-first introduction to 23 Design Patterns. | [HTML](source/carousel-01.html) |
| [Carousel 02](images/carousel-02.png) | 1080 × 1350 | A diagram alone is not a decision: ask what changes and who owns it before choosing the design. | [HTML](source/carousel-02.html) |
| [Carousel 03](images/carousel-03.png) | 1080 × 1350 | Give shipping its own rule: Checkout receives a standard or express policy through ShippingRule. | [HTML](source/carousel-03.html) |
| [Carousel 04](images/carousel-04.png) | 1080 × 1350 | Same checkout, different totals: Standard 45, Express 55, Express large 120. | [HTML](source/carousel-04.html) |
| [Carousel 05](images/carousel-05.png) | 1080 × 1350 | Read it, run it, change the rule: 23 examples with expected output to inspect the abstraction. | [HTML](source/carousel-05.html) |
| [Carousel 06](images/carousel-06.png) | 1080 × 1350 | Start with Strategy: choose one pattern, run its example, and try its challenge. | [HTML](source/carousel-06.html) |

Actual byte sizes are recorded in [image-validation.json](source/image-validation.json). Campaign format sizes other than GitHub are editorial defaults, not verified requirements for every platform. All carousel slides include the same authentic diagram and brand footer; the heading and teaching point change by slide.

The original repository [SVG preview](../assets/social-preview.svg) and [PNG preview](../assets/social-preview.png) were also updated to the new display name, preserving their established layout. They are a separate 1280 × 640 alternative, not included in the ten campaign images.

## Reproduce

Requires Node.js, Playwright, and its Chromium browser. The renderer resolves assets relative to this repository and writes campaign HTML and PNG files here. It also refreshes `assets/social-preview.png` from its SVG.

If Playwright is installed in the current Node module resolution path, run from the repository root:

```sh
node Markting/source/render.cjs
```

Otherwise install Playwright in a local tool directory, or set `PLAYWRIGHT_MODULE` to the absolute path of an existing Playwright module directory. Install the matching Chromium browser with that installation's Playwright CLI. No dependency installation is performed by the renderer.

For this execution, an existing Playwright installation was reused from the neighboring portfolio's `node_modules/playwright`; its files were read only. No portfolio content, source, or package files were changed. The composition itself has no dependency on that portfolio: an independent Playwright installation works through the documented override.

The HTML embeds the SVG assets as data URLs and can be opened directly in a browser. System font fallback can vary between machines; inspect regenerated output before publishing. Run `node Markting/source/render.cjs --inspect-sources` to recreate the source asset inspection image.
