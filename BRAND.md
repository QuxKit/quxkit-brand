# QuxKit — brand assets

The crystal system for the QuxKit family. Each product is the same faceted mark,
cut in its own stone; ai_member is a faceted crystal brain. Taglines and product
labels have been removed; the raster renders are the faithful masters and the
`.svg` files are clean vector traces (vtracer, polygon mode) for scaling.

## Products & colours

| Folder | Product | Stone |
|---|---|---|
| `quxkit/` | QuxKit (umbrella) | Blue crystal |
| `billing-kit/` | @quxkit/billing-kit | Blue |
| `identity-kit/` | @quxkit/identity-kit | Gold |
| `mail-kit/` | @quxkit/mail-kit | Ruby |
| `tenant-kit/` | @quxkit/tenant-kit | Green |
| `ai-member/` | AI Member / AI Memory | Purple crystal brain |

## What's in each product folder

- `*-icon.png` / `*-brain.png` — the cleaned mark on its app-tile (label removed, square)
- `*-glyph.png` — the **bare crystal on transparent**: tile, drop-shadow and paper
  all stripped, for the four products (`billing-kit`, `tenant-kit`, `identity-kit`,
  `ai-member`). Produced by `scripts/isolate-glyphs.py`.
- `*-icon-alt.png` — a second generated variant, kept as an option
- `*.svg` — scalable vector trace of the mark
- `sizes/` — square PNG exports of the tiled icon **and** the glyph
  (`*-glyph-{512,256,128,64,32}.png`); QuxKit also 16, 180, 460

## Isolating the bare glyphs

`scripts/isolate-glyphs.py` lifts each crystal off its tile. The crystals split by
material, so it uses two recipes: the **colored** stones (blue/green/gold) are
isolated by flooding every desaturated pixel inward from the border — that eats
paper + gray drop-shadow + white tile in one sweep while the saturated facets wall
off the interior highlights; the **crystal brain** is itself light and low-saturation,
so instead `rembg` lifts the whole tile off the paper and a tight near-white flood
removes just the white tile, stopping at the lavender edge. The QuxKit umbrella mark
is a near-white crystal with no distinct hue, so it is *not* auto-isolated — it keeps
its designed app-tile (`quxkit-icon-light/dark`).

## QuxKit extras

- `quxkit-wordmark.png` — mark + wordmark, **no tagline**
- `quxkit-lockup-crystal.png` / `quxkit-lockup-mono.png` — lockups, tagline cropped
- `quxkit-icon-light.png` / `quxkit-icon-dark.png` — app-icon on white / navy

## Reference & source

- `reference/` — the original brand sheet and the family board (all four + brain)
- `_source/` — the untouched 1024² renders

## Slots

- **Favicon:** `quxkit/sizes/quxkit-32.png` (and `-16`)
- **GitHub / npm org avatar:** `quxkit/sizes/quxkit-460.png`
- **Per-package README / npm icon:** each product's `sizes/*-256.png`

Notes: the SVG traces are colour-traces of the renders — scalable and faithful
in shape, but open them to confirm before using at hero scale. For a perfectly
crisp production mark you would still redraw from these as a guide.
