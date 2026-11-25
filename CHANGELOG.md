# Changelog

## 1.2.0
- Color policy rewritten: cyan, magenta and amber are brand colors usable as solid fields, buttons, highlights, numerals and chart series; neutrals dominate by area; gradient only cyan > magenta > amber. Skill now forbids black-and-white-only output.
- Added measured contrast rules, tints, proposed status colors, and logo-on-color file mapping.
- Added `references/ui-patterns.md` and templates: landing, dashboard, mobile-app (one-pager recolored).
- Added `arcloops-loop-color.svg`.
- `inline_assets.py` scopes SVG ids and classes per logo (fixes clashes when several logos share a page).
- `brand_check.py` updated for the new palette (errors vs warnings).
- Source notes record the owner decision on color.

## 1.1.1
- Repo is public: updated LICENSE.md and README install steps.

## 1.1.0
- Added cropped loop-only SVGs for decoration (`arcloops-loop-black/white.svg`).
- Added `references/source-notes.md` documenting conflicts between the guideline sources.
- Added `templates/one-pager.html` and `scripts/inline_assets.py`.
- Added CONTRIBUTING, PR template and license notes.

## 1.0.0
- Initial skill: tokens, typography, logos, voice, applications, brand check script.
