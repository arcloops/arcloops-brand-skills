# Contributing

1. Branch from `main`, change the skill, open a PR using the template.
2. Keep `skills/arcloops-brand/SKILL.md` short. Put detail in `references/`.
3. Never edit, recolor or redraw the logo files. Replace them only with new official exports, run through `scripts/strip_svg_metadata.py`.
4. When sources disagree, record the decision in `references/source-notes.md`.
5. Run `python3 skills/arcloops-brand/scripts/brand_check.py` on any template you add.
6. Bump `version` in `.claude-plugin/plugin.json` and add a CHANGELOG entry.
