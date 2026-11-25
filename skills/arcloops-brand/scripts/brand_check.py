#!/usr/bin/env python3
"""Arcloops brand lint for HTML/CSS/SVG output.
Errors: off-palette hex, non-brand fonts, hype words.
Warnings: cyan/amber used as text color (fails contrast on light), box-shadow, gradients not in cyan>magenta>amber order.
Usage: brand_check.py file [file...]"""
import re, sys
ALLOWED = {"38393b","919191","6b6c6e","d9d9d9","f7f7f7","ffffff","fff","000","000000",
           "06dbf4","e214b1","fcb53f","e6fbfe","fce8f7","fff8ec"}
HYPE = ["revolutionize","cutting-edge","cutting edge","transformative","unlock","game-changing","supercharge","seamless"]
FONT_OK = {"geist","inter","-apple-system","segoe ui","sans-serif","system-ui","monospace","serif"}
err = warn = 0
for path in sys.argv[1:]:
    t = open(path, encoding="utf8", errors="ignore").read()
    body = re.sub(r"<svg\b.*?</svg>", "", t, flags=re.S | re.I)  # inline logos are exempt
    for h in sorted(set(re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", body))):
        if h.lower() not in ALLOWED:
            print(f"ERROR {path}: off-palette #{h.lower()}"); err += 1
    for fam in re.findall(r"font-family\s*:\s*([^;}<]+)", t, flags=re.I):
        fam = re.split(r'"\s*>', fam)[0]
        for f in [x.strip(" '\"").lower() for x in fam.split(",")]:
            if f and f not in FONT_OK and not f.startswith("var("):
                print(f"ERROR {path}: non-brand font '{f}'"); err += 1
    low = t.lower()
    for w in HYPE:
        if w in low:
            print(f"ERROR {path}: hype word '{w}'"); err += 1
    for m in re.finditer(r"(?<![-\w])color\s*:\s*#(06dbf4|fcb53f)", body, flags=re.I):
        print(f"WARN  {path}: #{m.group(1).lower()} as text color. Fails contrast on light surfaces; only OK on charcoal or as very large display type."); warn += 1
    if re.search(r"box-shadow\s*:\s*(?!none)", body, flags=re.I):
        print(f"WARN  {path}: box-shadow found. Brand UI is flat; use hairlines."); warn += 1
    for g in re.findall(r"(?:linear|radial|conic)-gradient\([^;}]*\)", body, flags=re.I):
        hexes = [h.lower() for h in re.findall(r"#([0-9a-fA-F]{6})", g)]
        if hexes and hexes != ["06dbf4","e214b1","fcb53f"]:
            print(f"WARN  {path}: gradient is not cyan>magenta>amber ({g[:50]}...)"); warn += 1
print("OK" if not err and not warn else f"{err} error(s), {warn} warning(s)")
sys.exit(1 if err else 0)
