# Arcloops Skills

Team skill repo for Claude. It currently holds one skill, **arcloops-brand**, which teaches Claude our brand (Guidelines v2, September 2026): colors, Geist/Inter typography, logo files and rules, layout, and voice.

## What's inside

```
.claude-plugin/        plugin + marketplace manifests (Claude Code / Cowork install)
skills/arcloops-brand/
  SKILL.md             the instructions Claude reads
  assets/logo/         4 lockups, SVG + PNG (metadata stripped)
  assets/fonts/        Geist + Inter variable fonts (OFL)
  assets/tokens.css    design tokens (also tokens.json)
  templates/           one-pager.html starter
  references/          voice, applications, imagery prompts, source notes, source PDFs
  scripts/             brand_check.py, strip_svg_metadata.py, inline_assets.py
package.sh             builds a zip for claude.ai upload
```

## Install (team members)

**Claude Code or Cowork (recommended):**
```
/plugin marketplace add <your-github-org>/arcloops-brand-skills
/plugin install arcloops-brand@arcloops-skills
```
Updates arrive when the repo changes (`/plugin marketplace update`).

**Claude.ai / desktop app:** run `./package.sh`, then upload `arcloops-brand.zip` in Settings > Capabilities > Skills. Repeat when the skill changes.

**Manual (Claude Code):** copy `skills/arcloops-brand` into `~/.claude/skills/`.

## Use

Ask Claude for anything Arcloops-branded ("make a one-pager for the Beximco proposal in Arcloops brand"). The skill triggers on its own from its description.

## Updating the brand

1. Edit `SKILL.md` or the files it points to. Keep `SKILL.md` short; put detail in `references/`.
2. New logo export? Run `python3 skills/arcloops-brand/scripts/strip_svg_metadata.py file.svg` before adding it.
3. Commit, push, open a PR. Bump `version` in `.claude-plugin/plugin.json`.
4. If a new guideline PDF replaces v2, add it to `references/source/` and update the tokens.

## Brand check

`python3 skills/arcloops-brand/scripts/brand_check.py page.html` flags off-palette hexes, loop colors used outside the logo, non-brand fonts and hype words.

## Build a branded page

```
python3 skills/arcloops-brand/scripts/inline_assets.py skills/arcloops-brand/templates/one-pager.html out.html
```
Produces one self-contained HTML file (fonts and logo inlined).

## Notes

- Geist and Inter are licensed under the SIL OFL (see `assets/fonts/OFL.txt`).
- Source `.ai` files are intentionally not committed (see `.gitignore`).
- Open design gaps: no standalone icon vector, no functional/status colors, no photography direction, no motion spec.
