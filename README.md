# QuxKit — brand

Public mark assets for the [QuxKit](https://github.com/QuxKit) family, so that
package READMEs, docs sites and slide decks can hit a stable image URL.

**This repository holds artwork only.** No product code lives here.

## The system

Each product is the same faceted crystal, cut in its own stone.

| Folder | Product | Stone |
|---|---|---|
| `quxkit/` | QuxKit (umbrella) | Blue crystal |
| `billing-kit/` | `@quxkit/billing-kit` | Blue |
| `tenant-kit/` | `@quxkit/tenant-kit` | Green |
| `identity-kit/` | `@quxkit/identity-kit` | Gold |
| `ai-member/` | AI Member | Purple crystal brain |
| `keystone/` | Keystone | — |

## Using a mark

Hotlink the raw URL — that is what this repository is for:

```md
<img src="https://raw.githubusercontent.com/QuxKit/quxkit-brand/main/billing-kit/sizes/billing-kit-128.png"
     width="72" align="right" alt="">
```

Each product folder carries `<name>-icon.png` (the mark on its app-tile),
`<name>-glyph.png` (the bare crystal on transparent), an `.svg` vector trace,
and `sizes/` with 32–512px square exports of both the tile and the glyph.
QuxKit adds 16, 180 and 460 for favicon and org-avatar slots.

Contrast note: the navy-tile QuxKit mark is for light surfaces, the white-tile
one for dark. The umbrella mark keeps its tile — it is a near-white crystal
with no distinct hue, so it does not read isolated.

`scripts/isolate-glyphs.py` is how the bare glyphs were lifted off their tiles;
`BRAND.md` is the fuller internal note on the system.

## Licence

© BRETT. The QuxKit marks are trademarks — hotlink them to refer to QuxKit
products; do not modify them or use them to brand anything else.
