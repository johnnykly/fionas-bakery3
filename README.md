# Fiona's Bakery

A redesign of [fionasbakery.se](https://fionasbakery.se/), a made-to-order konditori in Arlöv run by Fiona Hua. The site is in Swedish and is a plain static site: HTML, CSS and a small amount of vanilla JavaScript.

The design is called "Färgburkarna". Pages are built from light slabs in sugarpaste colours: rose, butter and pistachio on a sugar-white ground. Text is plum and actions are berry red. Type is Caprasimo for headings and Figtree for body text, both self-hosted.

## Structure

| Path | What it is |
|---|---|
| `site/` | The production site, ready to upload to any static host (One.com, Netlify, etc.) |
| `src/` | Source: `pages.py` (page markup), `style.css`, `main.js`, `build.py`, Phosphor icons |
| `img/` | Fiona's cake photos (JPEG and WebP) with provenance sidecars |
| `fonts/` | Self-hosted Caprasimo and Figtree (woff2) |
| `preview/` | Single-file preview with all pages hash-routed, used for the shareable preview link |
| `brandkit/` | Brand-kit concept board (draft; the cake in panel 8 is AI-generated, not Fiona's work) |
| `PRODUCT.md`, `DESIGN.md` | Product facts and the design system (tokens, rules, exceptions) |

## Pages

- `index.html`
- `tartor.html`
- `smaker-priser.html`
- `om-fiona.html`
- `fragor.html`
- `bestall.html`
- `404.html`

## Build

```bash
cd src && python3 build.py
```

This regenerates both `site/` and `preview/index.html` from the source.

## To preview locally

```bash
cd site && python3 -m http.server 8000
```

## Before going live

- The order form builds an email (mailto plus a copy button). There's no backend yet.
- Get confirmation from Fiona on:
  - the service area (Malmö, Lund, Burlöv, about 15 km)
  - the allergy answer in the FAQ
  - a portrait of herself, if she has one
- Add a privacy policy if analytics or a form backend is added.
