---
name: arcloops-brand
description: Apply the Arcloops brand (Guidelines v2, Sept 2026) to any document, deck, web page, UI, social asset or generated image. Use for any Arcloops-branded work, or when the user mentions Arcloops colors, logo, fonts, tone or brand guidelines.
---

# Arcloops brand

Use this instead of any generic or Anthropic styling. If the user supplies a newer guideline PDF, it wins over this file.

## The idea
One quiet system, one signature moment. The brand is neutral and engineering-grade (charcoal, gray, white) with a single point of color: the infinity loop.
- **Quiet mode**: charcoal, gray, white. Documents, UI, backgrounds.
- **Signature mode**: the full-saturation gradient loop, only as the logo or a few hero moments (cover, card back, section break). Loop shape only.
- If you are about to tint the loop, use it twice on one surface, or color anything else, stop. That decision belongs to the loop alone.

## Color tokens
| Token | Hex | Use |
|---|---|---|
| charcoal | #38393B | text, headings, wordmark |
| gray | #919191 | wordmark gray, numerals, chrome |
| text-muted | #6B6C6E | secondary text |
| border | #D9D9D9 | hairlines, dividers |
| surface-quiet | #F7F7F7 | quiet bands and panels |
| white | #FFFFFF | base surface |
| cyan #06DBF4 → magenta #E214B1 → amber #FCB53F | | the loop only, left to right, all three stops |

Ratio: about 90% neutral, 10% or less signature color, and that color is only ever the loop. Cyan, magenta and amber are never a background, ring, heading, button, link, badge, chart series, glow or wash. There are no success/warning/error colors yet: use size, weight, icons or text, and flag the gap. Headings stay charcoal (white on dark). Never color type.

Ready-made tokens: `assets/tokens.css`, `assets/tokens.json`.

## Typography
- **Geist**: headings and display. Bold for Display, H1, H2; SemiBold for H3.
- **Inter**: body, captions, tables, UI. Regular.
- Web: Display 40px, H1 32/1.2, H2 24/1.25, H3 18/1.3, Body 16/1.5, Caption 12/1.4.
- Print/slides: Display 40/44pt, H1 32/38, H2 24/30, H3 18/24, Body 13/20, Caption 10/14.
- Emphasis comes from size and weight, never tint.
- Font files (OFL) are in `assets/fonts/`. For web pages that cannot load remote fonts, base64 them into `@font-face`; fallback stack `-apple-system, "Segoe UI", sans-serif`.

## Logo
Use only the supplied files in `assets/logo/`. Never redraw, recolor, stretch, rotate, add frame/glow/shadow/outline, or simplify the rings.
| File | Use |
|---|---|
| `...-01-full-color` | Default on light/white backgrounds |
| `...-02-white-wordmark-color-loop` | Dark hero surfaces only (cover, card back, splash) |
| `...-03-all-white` | Dark quiet surfaces, embroidery, foil, watermark |
| `...-04-all-black` | Light one-color print, stamps, engraving |

- Clear space: one X on every side, X = cap-height of the wordmark, measured from the widest ring.
- Minimum width: 120px digital, 30mm print.
- SVG viewBox is `0 0 986.55 200`. The SVGs here already have the c2pa metadata stripped; run `scripts/strip_svg_metadata.py` on any new export.
- No standalone icon vector exists. Do not improvise one.
- One color object per surface: never pair a full-color lockup with another saturated loop.

## Decoration
Only the real loop, cropped, bled off an edge, at 6 to 10% opacity; gray/black line-art on light, white on dark (use `assets/logo/arcloops-loop-black.svg` or `arcloops-loop-white.svg`, already cropped to the loop, viewBox `437 0 275 200`). It must not read as the logo again. No plain circles or rings, glows, nebula washes or gradient panels. Generated imagery: see `references/imagery-prompts.md`.

## Layout defaults
White base, optional #F7F7F7 band, #D9D9D9 hairlines. No rounded cards, shadows or gradient backgrounds. Buttons and links stay neutral (charcoal text with underline, or charcoal fill). Slides: 16:9, white or charcoal grounds, loop in color on cover and close only. More per format in `references/applications.md`. A starter page is in `templates/one-pager.html`; fill it with `scripts/inline_assets.py template.html out.html` to get a self-contained, on-brand file.

## Voice
Direct, specific, calm. Lead with outcomes. Prefer numbers, industries and named processes. Banned: revolutionize, cutting-edge, transformative, unlock, and similar hype. Process words: advisory, research, consulting; audit, consult, train, build. Details and examples in `references/voice.md`.

## Source conflicts
The designer deck and the written rules differ in a few places (logo on cyan/magenta panels, amber RGB typo, dark-surface lockup). Read `references/source-notes.md` before using color panels or dark lockups, and ask the user when unsure.

## Open items (flag to the user, do not improvise)
1. No standalone vector icon. 2. No functional/status colors. 3. No photography direction: ask. 4. No motion spec: do not animate or simplify the rings.

## Before delivering
Run through this list, or run `python3 scripts/brand_check.py <file.html|css|svg>` for web output.
- Headings Geist and charcoal; body Inter.
- Only the neutral hexes above plus the loop.
- Loop in color at most once per surface.
- Logo from supplied files, with clear space and above minimum size.
- No color on type, buttons, links or charts.
- Copy free of hype.
