#!/usr/bin/env python3
"""Fill brand placeholders in an HTML template so it is fully self-contained.
Placeholders:
  {{FONTS}}        -> @font-face rules with base64 Geist + Inter variable fonts
  {{TOKENS}}       -> contents of assets/tokens.css (without @font-face lines)
  {{LOGO:01}}      -> inline SVG of lockup 01 (also 02, 03, 04)
  {{LOOP:black}}   -> inline cropped loop SVG (also white)
Usage: inline_assets.py template.html out.html"""
import base64, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
a = root / "assets"
names = {"01": "arcloops-logo-01-full-color", "02": "arcloops-logo-02-white-wordmark-color-loop",
         "03": "arcloops-logo-03-all-white", "04": "arcloops-logo-04-all-black"}
def b64(p): return base64.b64encode(p.read_bytes()).decode()
fonts = "".join(
    f'@font-face{{font-family:"{fam}";src:url(data:font/ttf;base64,{b64(a/"fonts"/f)}) format("truetype");font-weight:100 900;font-display:swap}}\n'
    for fam, f in (("Geist", "Geist-Variable.ttf"), ("Inter", "Inter-Variable.ttf")))
tokens = "\n".join(l for l in (a/"tokens.css").read_text().splitlines() if not l.startswith("@font-face") and "--loop-" not in l)
def svg(p): return re.sub(r"<\?xml.*?\?>", "", p.read_text(encoding="utf8")).strip()
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf8")
t = t.replace("{{FONTS}}", fonts).replace("{{TOKENS}}", tokens)
t = re.sub(r"\{\{LOGO:(0[1-4])\}\}", lambda m: svg(a/"logo"/f"{names[m.group(1)]}.svg"), t)
t = re.sub(r"\{\{LOOP:(black|white)\}\}", lambda m: svg(a/"logo"/f"arcloops-loop-{m.group(1)}.svg"), t)
pathlib.Path(sys.argv[2]).write_text(t, encoding="utf8")
print(f"wrote {sys.argv[2]} ({len(t)//1024} KB)")
