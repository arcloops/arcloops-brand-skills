# Arcloops Skills

Team skill repo for Claude. It currently holds one skill, **arcloops-brand**, which teaches Claude our brand (Guidelines v2, September 2026): the full color system (neutrals plus cyan, magenta and amber and the gradient loop), Geist/Inter typography, logo files and rules, UI/web/mobile patterns, and voice.

## What's inside

```
.claude-plugin/        plugin + marketplace manifests (Claude Code / Cowork install)
skills/arcloops-brand/
  SKILL.md             the instructions Claude reads
  assets/logo/         4 lockups, SVG + PNG (metadata stripped)
  assets/fonts/        Geist + Inter variable fonts (OFL)
  assets/tokens.css    design tokens (also tokens.json)
  templates/           one-pager, landing page, dashboard, mobile app screens (HTML)
  references/          UI patterns, voice, applications, imagery prompts, source notes, source PDFs
  scripts/             brand_check.py, strip_svg_metadata.py, inline_assets.py
package.sh             builds a zip for claude.ai upload
```

## Install (anyone)

**Claude Code or Cowork (recommended):**
```
/plugin marketplace add <your-github-org>/arcloops-brand-skills
/plugin install arcloops-brand@arcloops-skills
```
No GitHub login is needed because the repo is public. Updates arrive when the repo changes (`/plugin marketplace update`).

**Claude.ai / desktop app:** download `arcloops-brand.zip` from the latest [Release](../../releases/latest) (or build it with `./package.sh`), then upload it in Settings > Capabilities > Skills. Repeat when the skill changes. Do not use GitHub's "Download ZIP" button: the folder layout will be wrong.

**Manual (Claude Code):** copy `skills/arcloops-brand` into `~/.claude/skills/`.

## Use

Ask Claude for anything Arcloops-branded ("make a one-pager for the Beximco proposal in Arcloops brand"). The skill triggers on its own from its description.

## Updating the brand

1. Edit `SKILL.md` or the files it points to. Keep `SKILL.md` short; put detail in `references/`.
2. New logo export? Run `python3 skills/arcloops-brand/scripts/strip_svg_metadata.py file.svg` before adding it.
3. Commit, push, open a PR. Bump `version` in `.claude-plugin/plugin.json`.
4. If a new guideline PDF replaces v2, add it to `references/source/` and update the tokens.

## Brand check

`python3 skills/arcloops-brand/scripts/brand_check.py page.html` errors on off-palette hexes, non-brand fonts and hype words, and warns on cyan/amber used as text, shadows and gradients out of order.

## Build a branded page

```
python3 skills/arcloops-brand/scripts/inline_assets.py skills/arcloops-brand/templates/landing.html out.html
```
Templates: `one-pager`, `landing`, `dashboard`, `mobile-app`. Produces one self-contained HTML file (fonts and logos inlined, ids scoped so several logos can share a page).

## Notes

- Geist and Inter are licensed under the SIL OFL (see `assets/fonts/OFL.txt`).
- Source `.ai` files are intentionally not committed (see `.gitignore`).
- Open design gaps: no standalone icon vector, status colors are a proposed extension, no photography direction, no motion spec.
