---
name: arcloops-brand
description: Apply the Arcloops brand (Guidelines v2, Sept 2026) to any document, deck, web page, dashboard, mobile app screen, social asset or generated image. Use for any Arcloops-branded work, or when the user mentions Arcloops colors, logo, fonts, tone or brand guidelines.
---

# Arcloops brand

Use this instead of any generic or Anthropic styling. If the user supplies a newer guideline PDF, it wins over this file.

**Do not deliver black-and-white work.** Arcloops is a neutral base with real color: cyan, magenta and amber carry the brand, and the gradient loop is the signature. A screen that is only charcoal, gray and white is wrong. Every layout needs a deliberate color move (see Color roles).

## The idea
A quiet, engineering-grade neutral base (charcoal, gray, white) with a vivid three-color accent set (cyan, magenta, amber) that all come from the infinity loop. Three levels:
- **Quiet**: neutrals only. Long-form text, tables, forms, letterhead bodies.
- **Accent**: solid brand colors used on purpose: color-blocked panels, buttons, highlights, big numerals, chart series, status. This is the normal state of UI, web and social work.
- **Signature**: the full gradient loop (cyan to magenta to amber). Covers, hero sections, card back, section breaks, splash and onboarding screens.

## Color
| Token | Hex | Role |
|---|---|---|
| charcoal | #38393B | text, dark surfaces, primary buttons on light |
| gray | #919191 | numerals, chrome, secondary lines |
| text-muted | #6B6C6E | secondary text |
| border | #D9D9D9 | hairlines |
| surface-quiet | #F7F7F7 | quiet bands and panels |
| white | #FFFFFF | base surface |
| cyan | #06DBF4 | interactive accent, links and focus on dark, info, selected state |
| magenta | #E214B1 | emphasis, key CTA, error, big highlights |
| amber | #FCB53F | warm highlight, warning, badges, callouts |
| gradient | cyan #06DBF4 → magenta #E214B1 → amber #FCB53F | always left to right (or top to bottom), always all three, always this order |
| tints | #E6FBFE cyan, #FCE8F7 magenta, #FFF8EC amber | flat wash panels and chip backgrounds |

### Color roles (what makes a design not black and white)
- Pick **one lead accent per screen or page** (cyan, magenta or amber) and use the other two sparingly. The set together appears in ARC triads, charts and the gradient.
- Every page or screen has **at least one color moment**: a color-blocked section, an accent button, a colored numeral set, a gradient hairline, or the full loop. Long documents may keep it to the cover and section dividers.
- Neutrals still dominate by area (about 70%). One large color field per screen at most.
- Gradient is allowed on the loop, hero fields, and thin 2 to 4px rules. Never on body text, never reversed, never with other colors mixed in.
- Do not invent new hues. Tints of the three brand colors are fine (tokens above).

### Contrast rules (measured)
- On **cyan** or **amber**: charcoal text only (6.9 and 6.5 : 1). Never white.
- On **magenta**: white text, 18px+ semibold or larger (4.2 : 1). For smaller labels use a charcoal button instead.
- On **charcoal**: white, cyan and amber text are all fine. Magenta text on charcoal fails: decorative only.
- On **white or #F7F7F7**: do not set body or small text in cyan or amber (1.7 : 1). Magenta only for large or bold text. Colored display numerals/letters (40px+) are fine.
- Links: charcoal underlined on light, cyan on dark. Focus ring: 2px magenta on light, cyan on dark.

### Status (proposed UI extension, flag it to the owner)
Info cyan, success cyan with a check icon, warning amber, error magenta. Always add an icon and a text label; color is never the only signal.

Tokens: `assets/tokens.css`, `assets/tokens.json`.

## Typography
- **Geist**: headings, display, numerals. Bold for Display, H1, H2; SemiBold for H3 and button labels.
- **Inter**: body, captions, tables, inputs, UI. Regular (Medium for small labels).
- Web: Display 40px (up to 64 to 96 in heroes), H1 32/1.2, H2 24/1.25, H3 18/1.3, Body 16/1.5, Caption 12/1.4. Mobile body 16, minimum 12.
- Print/slides: Display 40/44pt, H1 32/38, H2 24/30, H3 18/24, Body 13/20, Caption 10/14.
- Large display letters or numbers may be colored (as in the A / R / C triad). Reading text stays charcoal or white.
- Font files (OFL) in `assets/fonts/`. For standalone pages use `scripts/inline_assets.py` (base64 fonts). Fallback stack `-apple-system, "Segoe UI", sans-serif`.

## Logo
Use only the supplied files in `assets/logo/`. Never redraw, recolor, stretch, rotate, outline, add glow or shadow, or simplify the rings.
| Surface | File |
|---|---|
| White or #F7F7F7 (default) | `-01-full-color` |
| Charcoal or dark hero | `-02-white-wordmark-color-loop` (loop in color) or `-03-all-white` |
| Cyan or magenta panel | `-03-all-white` (as in the designer deck) |
| Amber panel, light one-color print, stamps | `-04-all-black` |
| Embroidery, foil, watermark | `-03` or `-04` |

- Clear space: one X on every side, X = cap-height of the wordmark. Minimum width 120px digital, 30mm print. viewBox `0 0 986.55 200`.
- No standalone icon exists. Do not improvise one. Ask the brand owner.
- Do not put the full-color lockup on a colored panel. If a gradient loop is the hero, do not also use a second gradient loop.
- Loop-only files for hero art and texture: `arcloops-loop-color.svg`, `-black.svg`, `-white.svg` (viewBox `437 0 275 200`).

## Decoration
- Texture: the loop cropped, bled off an edge, 6 to 10% opacity, black/gray on light, white on dark. Must not read as the logo again.
- Hero: the full-color loop large on charcoal, cropped by the edge or centered.
- Allowed shapes: concentric thin arcs and orbit linework in brand colors. Not allowed: solid blobs, glows, stock gradients, generic icons or flat illustrations. Imagery rules in `references/imagery-prompts.md`.

## Layout defaults
White base, optional #F7F7F7 band, #D9D9D9 hairlines. Square corners or at most 8px radius; no drop shadows (hairlines instead; mobile sheets may float). Slides: 16:9, white, charcoal or one brand-color ground, color loop on cover and close. Patterns and ideas for web, dashboards and mobile apps: `references/ui-patterns.md`. Per-format notes: `references/applications.md`. Starters in `templates/` (one-pager, landing page, dashboard, mobile app screens), filled with `scripts/inline_assets.py template.html out.html`.

## Voice
Direct, specific, calm. Lead with outcomes. Numbers, industries and named processes over adjectives. Banned: revolutionize, cutting-edge, transformative, unlock, and similar. Process words: advisory, research, consulting; audit, consult, train, build. See `references/voice.md`.

## Source conflicts and open items
The written rules and the designer deck differ in places; the color policy above follows the brand owner's decision of Nov 2026 (see `references/source-notes.md`). Still open, ask the owner: standalone icon, photography direction, motion spec, final status colors.

## Before delivering
- Not black and white: at least one deliberate color move, and the loop or an accent visible where it fits.
- Headings Geist, body Inter, reading text charcoal or white.
- Contrast rules above respected (charcoal on cyan/amber, white on magenta only large).
- Logo from supplied files, right file for the surface, clear space kept.
- Gradient only cyan → magenta → amber, no shadows, no foreign hues.
- Copy free of hype. For web output run `python3 scripts/brand_check.py file.html`.
