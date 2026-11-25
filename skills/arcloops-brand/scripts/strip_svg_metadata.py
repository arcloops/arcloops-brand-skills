#!/usr/bin/env python3
"""Strip the large <metadata> (c2pa) block from SVG logo exports.
Usage: strip_svg_metadata.py in.svg [out.svg]   (overwrites input if no out)"""
import re, sys
src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else src
s = open(src, encoding="utf8").read()
n = re.sub(r"<metadata>.*?</metadata>", "", s, flags=re.S)
open(dst, "w", encoding="utf8").write(n)
print(f"{src}: {len(s)} -> {len(n)} bytes")
