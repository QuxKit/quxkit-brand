#!/usr/bin/env python3
"""Isolate each product crystal to a bare glyph on transparent — no tile, no paper.

Two recipes, because the crystals split by material:
  * Colored crystals (billing blue, tenant green, identity gold) — flood-fill every
    DESATURATED pixel inward from the border. That eats paper + gray drop-shadow +
    white tile in one connected sweep; the saturated facets wall off the interior
    highlights so they survive. A component pass then drops any desaturated speck
    (the warm shadow crumb in a corner) the fill couldn't reach.
  * The crystal brain (ai-member) is itself light and low-saturation, so a desat key
    eats through it. Instead: rembg lifts the whole tile off the paper, then a TIGHT
    near-white flood-fill removes only the white tile, stopping at the lavender edge.
"""
import sys, colorsys
from collections import deque
from PIL import Image
from rembg import remove, new_session

BRAND = sys.argv[1] if len(sys.argv) > 1 else "."
SIZES = [512, 256, 128, 64, 32]

def flood(im, predicate):
    px = im.load(); w, h = im.size
    seen = bytearray(w * h); dq = deque()
    for x in range(w): dq.append((x, 0)); dq.append((x, h - 1))
    for y in range(h): dq.append((0, y)); dq.append((w - 1, y))
    while dq:
        x, y = dq.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y * w + x]: continue
        seen[y * w + x] = 1
        r, g, b, a = px[x, y]
        if a == 0 or predicate(r, g, b):
            px[x, y] = (r, g, b, 0)
            dq.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)])
    return im

def drop_specks(im, min_sat=0.14, min_frac=0.06):
    """Keep only the crystal: drop opaque components that are either desaturated
    (gray/warm shadow crumbs) or small next to the largest facet mass (the tan
    drop-shadow L in a corner that the fill couldn't reach from the border)."""
    px = im.load(); w, h = im.size
    seen = bytearray(w * h); comps = []
    for sy in range(h):
        for sx in range(w):
            if seen[sy*w+sx] or px[sx, sy][3] == 0: continue
            comp = []; dq = deque([(sx, sy)]); ssum = 0.0
            while dq:
                x, y = dq.popleft()
                if x < 0 or y < 0 or x >= w or y >= h or seen[y*w+x] or px[x, y][3] == 0: continue
                seen[y*w+x] = 1; comp.append((x, y))
                r, g, b, _ = px[x, y]
                ssum += colorsys.rgb_to_hsv(r/255, g/255, b/255)[1]
                dq.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
            comps.append((comp, ssum/len(comp)))
    biggest = max(len(c) for c, _ in comps) if comps else 0
    for comp, msat in comps:
        if msat < min_sat or len(comp) < min_frac * biggest:
            for x, y in comp: px[x, y] = (0, 0, 0, 0)
    return im

def square_pad(im, pad=0.09):
    bb = im.getbbox()
    if bb: im = im.crop(bb)
    w, h = im.size; side = int(max(w, h) * (1 + pad * 2))
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(im, ((side - w)//2, (side - h)//2), im)
    return canvas

def colored(src):
    im = Image.open(src).convert("RGBA")
    im = flood(im, lambda r, g, b: (lambda hsv: hsv[2] > 0.42 and hsv[1] < 0.22)(colorsys.rgb_to_hsv(r/255, g/255, b/255)))
    im = drop_specks(im)
    return square_pad(im)

_SESS = None
def brain(src):
    global _SESS
    if _SESS is None: _SESS = new_session("isnet-general-use")
    im = Image.open(src).convert("RGBA")
    im = remove(im, session=_SESS)
    im = flood(im, lambda r, g, b: r > 222 and g > 222 and b > 222)
    return square_pad(im)

JOBS = [
    ("billing-kit", "billing-kit/billing-kit-icon.png", colored),
    ("tenant-kit",  "tenant-kit/tenant-kit-icon.png",   colored),
    ("identity-kit","identity-kit/identity-kit-icon.png",colored),
    ("ai-member",   "ai-member/ai-member-brain.png",     brain),
]

import os
for key, rel, fn in JOBS:
    src = os.path.join(BRAND, rel)
    glyph = fn(src)
    prod = os.path.dirname(src)
    master = os.path.join(prod, f"{key}-glyph.png")
    glyph.save(master)
    sd = os.path.join(prod, "sizes"); os.makedirs(sd, exist_ok=True)
    for s in SIZES:
        glyph.resize((s, s), Image.LANCZOS).save(os.path.join(sd, f"{key}-glyph-{s}.png"))
    print(f"{key}: glyph {glyph.size} -> {master}")
print("done")
