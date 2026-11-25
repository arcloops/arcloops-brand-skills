#!/usr/bin/env python3
"""Quick Arcloops brand lint for HTML/CSS/SVG output.
Flags: loop colors used outside the logo, off-palette hexes, non-brand fonts, hype words.
Usage: brand_check.py file [file...]"""
import re, sys
ALLOWED = {"38393b","919191","6b6c6e","d9d9d9","f7f7f7","ffffff","fff","000","000000"}
LOOP = {"06dbf4","e214b1","fcb53f"}
HYPE = ["revolutionize","cutting-edge","cutting edge","transformative","unlock","game-changing","supercharge","seamless"]
FONT_OK = {"geist","inter","-apple-system","segoe ui","sans-serif","system-ui","monospace","serif"}
bad = 0
for path in sys.argv[1:]:
    t = open(path, encoding="utf8", errors="ignore").read()
    body = re.sub(r"<svg\b.*?</svg>", "", t, flags=re.S | re.I)  # inline logos are exempt
    body = "\n".join(l for l in body.splitlines() if "--loop-" not in l)  # token definitions are exempt
    for h in set(re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", body)):
        h = h.lower()
        if h in LOOP:
            print(f"{path}: loop color #{h} used outside the logo/loop"); bad += 1
        elif h not in ALLOWED:
            print(f"{path}: off-palette #{h}"); bad += 1
    for fam in re.findall(r"font-family\s*:\s*([^;}<]+)", t, flags=re.I):
        fam = re.split(r'"\s*>', fam)[0]
        for f in [x.strip(" '\"").lower() for x in fam.split(",")]:
            if f and f not in FONT_OK and not f.startswith("var("):
                print(f"{path}: non-brand font '{f}'"); bad += 1
    low = t.lower()
    for w in HYPE:
        if w in low:
            print(f"{path}: hype word '{w}'"); bad += 1
print("OK" if not bad else f"{bad} issue(s)")
sys.exit(1 if bad else 0)
