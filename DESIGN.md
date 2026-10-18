---
name: Fiona's Bakery
description: Färgburkarna – a sugarpaste world of rolled paste slabs, deep gel ink and occasion colour pots.
colors:
  berry: "#7E4E31"
  berry-deep: "#613A23"
  plum: "#3B2A21"
  plum-soft: "#5E4B40"
  sugar: "#FFFDF9"
  rose: "#F6EEE1"
  butter: "#FBF6EE"
  pistachio: "#E9D8C5"
  rose-gel: "#CDB494"
  butter-gel: "#D8C29C"
  pistachio-gel: "#A98466"
  line: "rgba(59,42,33,.14)"
  placeholder: "#7C6C62"
typography:
  display:
    fontFamily: "Caprasimo, Cooper Black, Georgia, serif"
    fontSize: "clamp(2.6rem, 6.2vw, 5.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Caprasimo, Cooper Black, Georgia, serif"
    fontSize: "clamp(2rem, 4.2vw, 3.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Caprasimo, Cooper Black, Georgia, serif"
    fontSize: "clamp(1.35rem, 2vw, 1.7rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  numeral:
    fontFamily: "Caprasimo, Cooper Black, Georgia, serif"
    fontSize: "clamp(3.4rem, 9vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: "-0.02em"
    fontFeature: "tnum"
  lede:
    fontFamily: "Figtree, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.06rem, 1.4vw, 1.2rem)"
    fontWeight: 400
    lineHeight: 1.65
  body:
    fontFamily: "Figtree, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Figtree, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
    lineHeight: 1
  subtitle:
    fontFamily: "Caprasimo, Cooper Black, Georgia, serif"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.2
  small:
    fontFamily: "Figtree, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.94rem"
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: "Figtree, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 500
    lineHeight: 1.3
rounded:
  slab: "clamp(22px, 3vw, 40px)"
  inner: "clamp(16px, 2vw, 26px)"
  layer: "18px"
  field: "14px"
  pill: "999px"
spacing:
  seam: "clamp(12px, 1.6vw, 20px)"
  gutter: "clamp(16px, 4vw, 40px)"
  slab-pad: "clamp(24px, 5vw, 64px)"
  max: "1240px"
components:
  button-gel:
    backgroundColor: "{colors.berry}"
    textColor: "{colors.sugar}"
    rounded: "{rounded.pill}"
    padding: "1em 1.5em"
    typography: "{typography.label}"
  button-gel-hover:
    backgroundColor: "{colors.berry-deep}"
    textColor: "{colors.sugar}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.plum}"
    rounded: "{rounded.pill}"
    padding: "1em 1.5em"
    typography: "{typography.label}"
  button-line-hover:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.sugar}"
  nav-tab:
    backgroundColor: "{colors.rose}"
    textColor: "{colors.plum}"
    rounded: "{rounded.pill}"
    padding: "0.8em 1.15em"
  nav-tab-order:
    backgroundColor: "{colors.berry}"
    textColor: "{colors.sugar}"
    rounded: "{rounded.pill}"
    padding: "0.8em 1.15em"
  slab:
    backgroundColor: "{colors.rose}"
    textColor: "{colors.plum}"
    rounded: "{rounded.slab}"
    padding: "{spacing.slab-pad}"
  slab-footer:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.sugar}"
    rounded: "{rounded.slab}"
    padding: "{spacing.slab-pad}"
  colour-pot:
    backgroundColor: "{colors.rose}"
    rounded: "{rounded.pill}"
    size: "48px"
  tag:
    backgroundColor: "{colors.sugar}"
    textColor: "{colors.plum}"
    rounded: "{rounded.pill}"
    padding: "0.55em 0.8em"
  chip:
    backgroundColor: "{colors.sugar}"
    textColor: "{colors.plum}"
    rounded: "{rounded.pill}"
    padding: "0.65em 1em"
  chip-selected:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.sugar}"
  input:
    backgroundColor: "{colors.sugar}"
    textColor: "{colors.plum}"
    rounded: "{rounded.field}"
    padding: "0.9em 1em"
---

# Design System: Fiona's Bakery

## Overview

**Creative North Star: "Färgburkarna"**

The site is tinted like Fiona's sugarpaste. Every region of a page is a rolled slab of light paste (rose, butter, pistachio, or sugar white) with softly rounded edges, laid on a sugar ground with narrow seams between slabs. Deep gel colours carry everything that must be read or pressed: plum ink for type, berry for actions. The colour pots (round swatches ringed with the deeper gel drop of their paste) are both the palette and the control: each occasion belongs to one of three paste families, and choosing an occasion re-tints the page.

Hierarchy comes from overlap, not from boxes. A photo slab lifts over the edge of a text slab; a range of cake slabs steps down across a pistachio ground and spills into the next section. The only elevation in the world is that lift. Romance (bröllop, sockerblommor) and play (barnkalas, student, fest) share one palette, so the site is never wedding-only and never childish.

The world is single-theme and light by design: paste is pale, ink is deep, and there is no dark mode to maintain. There are no dark surfaces; the footer is a crème (rose) slab like the rest.

**Key Characteristics:**
- Whole-region paste slabs (radius clamp(22px,3vw,40px)) separated by 12–20px seams, never full-bleed white sections.
- Plum ink and berry actions; paste colours are grounds, never text.
- Three paste families (rose, butter, pistachio); the occasion → family mapping is fixed and drives live re-tinting.
- Colour pots, paste-pill nav tabs with a gel-ring current state, and pill buttons are the component family.
- Overlap and one soft lift shadow are the only depth.
- Caprasimo display over Figtree text, both self-hosted.

## Colors

A pastel paste family for grounds, one gel ring per paste for emphasis, and two deep inks that carry all reading and acting.

### Primary
- **Berry Gel** (berry): the action colour. Primary pill buttons, the "Beställ" nav tab, links, focus outlines, range-thumb ring, the checked toggle, invalid-field rings, caret. Hover and pressed states deepen to **Deep Berry** (berry-deep), which also colours inline error text.

### Neutral
- **Plum Ink** (plum): all headings and body text, the line button, the selected chip.
- **Soft Plum** (plum-soft): secondary copy – ledes on sugar, captions, `dt` labels, scale ticks.
- **Sugar** (sugar): page ground, inner cards inside slabs (meter, summary, steps, FAQ at rest), tags, fields, and text on berry/plum.
- **Paste Line** (line): the 1.5px inset hairline on chips, closed FAQ rows and FAQ toggles. Fields use the same plum at 12% (30% on hover).
- **Placeholder Plum** (placeholder): field placeholder text only.

### Paste slabs (grounds)
Three pastes only, plus sugar.
- **Rose** (rose): bröllop and sockerblommor; the default hero tint, the Fiona section, the Tårtor and Frågor nav tabs.
- **Butter** (butter): barnkalas & dop and fest / födelsedag; the price calculator, the mobile estimate bar, the Smaker & priser tab.
- **Pistachio** (pistachio): student and bakelser & företag; the hero's default photo slab, the range and closing slabs, the Om Fiona tab.

Home slab sequence: hero rose, range pistachio, calculator butter, Fiona rose, closing call to action pistachio. The flavour builder sits on a lifted sugar slab.

### Gel rings
Each paste has a deeper drop of itself: **Rose Gel**, **Butter Gel**, **Pistachio Gel**. They appear only as rings and dots: the 5px inset ring of a colour pot, the current-page ring on a nav tab, the dot on a tag, the ring on numbered steps, the filled track of the range slider (butter gel), and the rose-mark leaf (pistachio gel). A slab class sets both, as `--c` (paste) and `--g` (gel).

### Named Rules
**The Occasion Owns Its Family Rule.** Three paste families carry every occasion: **rose** is bröllop and sockerblommor, **butter** is barn/dop and fest/födelsedag, **pistachio** is student and bakelser/företag; "alla" falls back to sugar pots and a rose head. Never reassign an occasion's family on a new surface and never add a fourth paste. Adjacent slabs never share a colour: a re-tinted surface pairs its tint with a different family (`--tint` / `--tint-2`: bröllop rose/pistachio, barn butter/rose, fest butter/pistachio, student pistachio/rose, företag pistachio/butter), and page slab sequences alternate. Interactions re-tint by swapping `--tint` / `--tint-2` (home hero, order card) or `--c` (gallery page head).

**The Ink Carries, Paste Grounds Rule.** Text and actions are always plum or berry on paste or sugar. Paste and gel colours are never used for text.

**The Gel Is A Ring Rule.** Gel colours appear as rings, dots and tracks, never as filled slabs or buttons.

## Typography

**Display Font:** Caprasimo (with Cooper Black, Georgia, serif), self-hosted woff2 in `fonts/`
**Body Font:** Figtree 400–700 plus italic (with Avenir Next, Segoe UI, system-ui), self-hosted woff2 in `fonts/`

**Character:** A soft, piped-icing display face with rounded terminals over a friendly geometric sans. The display face does headings and numbers; Figtree does everything you read or operate.

### Hierarchy
- **Display** (h1): page titles. The home hero sets it slightly smaller, clamp(2.5rem,5vw,4.4rem), to fit beside the photo slab.
- **Headline** (h2): section heads inside slabs; `text-wrap: balance`.
- **Title** (h3): step, price-row and flavour-group heads. FAQ questions use the display face at clamp(1.15rem,1.8vw,1.35rem)/1.3.
- **Numeral**: prices and estimates (price calculator, order summary at clamp(3rem,6vw,4.6rem), mobile bar at 1.6rem), always tabular and animated by the ticker.
- **Lede**: section openers, soft plum on sugar and plum on tinted slabs; measure 36em.
- **Body**: 17px/1.65 Figtree, plum.
- **Label**: buttons, legends (700), small headings inside the hero picker and footer (600–700 Figtree at 1rem or less, no tracking, no uppercase).

### Named Rules
**The Numbers Are Icing Rule.** Every price, count and estimate is set in Caprasimo with tabular figures and changes by ticking (520ms, exponential ease-out; instant under reduced motion), never by jumping.

**The No Eyebrow Rule.** Headings stand alone. No kicker, eyebrow or uppercase tracked label above a heading; small sub-heads are sentence-case Figtree.

## Layout

A centred column (max 1240px, gutter clamp(16px,4vw,40px)) holds a stack of slabs. Sections are separated by seams of clamp(12px,1.6vw,20px) on the sugar ground, so the page reads as paste pieces laid side by side on a board, not as white bands.

Composition within slabs is a 12-column grid used for overlap: the home hero puts the words slab across columns 1–8 and the photo slab across 7–12, dropped down by clamp(48px,7vw,96px) and lifted over it. The "range" row steps four cake slabs down at staggered offsets with −28px overlaps and a −72px spill into the next slab; the calculator's sugar meter spills into the Fiona section below. Slab padding is clamp(24px,5vw,64px).

At ≤900px, grids collapse to one column; overlapping photo slabs move below their text slab and pull up by about 90–96px, centred at 72–84% width, so the overlap survives on phones. Nav collapses to a "Meny" pill that opens a sugar slab list. At ≤980px the order page gains a fixed butter estimate bar at the bottom (top radius 22px). Mobile gallery is two columns with 10px gaps.

### Named Rules
**The Seam Rule.** Between slabs, show 12–20px of sugar ground. Never butt slabs together edge to edge and never use a white full-bleed section as a separator.

## Elevation & Depth

Depth is overlap plus one lift. Slabs are flat at rest; a slab or photo that sits over another receives the lift shadow, a long, soft, plum-tinted drop. Small objects (pots, tags, tile names, layers) carry a miniature version of the same drop. Hover moves things up 1–3px; it does not add new shadows.

### Shadow Vocabulary
- **Lift** (`box-shadow: 0 22px 44px -26px rgba(59,42,33,.38), 0 3px 8px -4px rgba(59,42,33,.12)`): overlapping photo slabs, the sugar meter and summary slabs, the menu button, lightbox controls, the cake plate.
- **Crumb** (`0 6px 14px -10px rgba(59,42,33,.6)`): tags and gallery tile names.
- **Pot drop** (`0 8px 16px -10px rgba(59,42,33,.5)`): under colour pots.
- **Berry glow** (`0 12px 24px -14px rgba(126,78,49,.7)`): under the gel button only.

### Named Rules
**The Only Lift Rule.** The lift shadow means "this sits on top of something". Never put it on a slab that does not overlap or float, and never use borders or boxed cards to create hierarchy.

## Shapes

Everything is rolled: no sharp corners anywhere. Slabs use the slab radius, anything nested inside a slab (photos, price rows, steps, FAQ rows, gallery tiles) uses the inner radius, and every control (buttons, tabs, chips, tags, stepper, toggle) is a full pill or a circle. Fields and bands sit between at 14px. Cake-layer bars in the flavour cross-section use 18px with a flatter 10px base on the top tier. Borders are replaced by inset hairline rings.

## Components

### Buttons
Round, confident pills.
- **Shape:** full pill (999px), 2px transparent border reserved for the line variant.
- **Gel (primary):** berry with sugar text, berry glow beneath, trailing arrow icon.
- **Hover / Focus:** deepens to berry-deep and rises 2px; icon slides 3px right; focus is a 2.5px berry outline offset 3px. Transitions are 0.3s on the expo-out ease `cubic-bezier(.16,1,.3,1)`.
- **Line (secondary):** transparent with a 2px plum border and plum text; fills plum with sugar text on hover.
- **Go link:** text link in berry with an arrow that slides on hover, for "see more" moves.

### Colour Pots (signature)
- **Style:** a 48px circle (42px on phones) filled with the paste, a 5px inset gel ring, a pot drop, and a Figtree label beneath.
- **State:** hover lifts 3px; selected adds a sugar gap ring and a plum outer ring (`0 0 0 3px sugar, 0 0 0 5.5px plum`) and bolds the label. Used as buttons (`aria-pressed`, home hero), radio labels (order form) and filters (gallery). Selecting a pot re-tints its owning surface over 0.7s.

### Navigation
- **Style:** a row of paste-pill tabs, plum Figtree 500 at 0.96rem: Tårtor rose, Smaker & priser butter, Om Fiona pistachio, Frågor rose, Beställ berry.
- **States:** hover draws a 2px inset gel ring and lifts 1px; the current page has a 2.5px inset gel ring and weight 700. The "Beställ" tab is always berry with sugar text; current state is berry-deep with a rose ring.
- **Mobile:** ≤900px, a sugar "Meny" pill with the lift opens a sugar slab with stacked tabs.

### Tags
- **Style:** sugar pill, plum 600 at 0.78rem, crumb shadow, with a 9px gel dot before the text (dot colour from the slab class).

### Chips
- **Style:** sugar pill with a 1.5px paste-line inset ring; hover darkens the ring to plum.
- **Selected:** plum fill, sugar text, no ring. Used for flavour choices.

### Cards / Containers
There are no boxed cards. Containers are slabs: paste ground, slab radius, slab padding, no border, flat unless overlapping (then the lift). Nested content sits on sugar or paste at the inner radius. The footer is a crème (rose) slab with plum text.

### Inputs / Fields
- **Style:** sugar fill, 14px radius, Figtree 500 1rem plum, 1.5px inset ring at 12% plum (30% on hover).
- **Focus:** 2px berry inset ring plus a 4px berry halo at 15%.
- **Error:** 2px berry inset ring; message in berry-deep 600 at 0.88rem.
- **Stepper:** sugar pill with 44px round buttons (rose on hover) and a Caprasimo 1.5rem number.
- **Toggle:** 52×30 pill, plum at 18% off, berry on, sugar knob.
- **Range:** 14px pill track filled with butter gel, 32px sugar thumb with a 7px berry ring.

### Order Bands
Inline notices inside the order card: 14px radius, sugar ground, soft-plum icon. A confirmation band is sugar at 70%. **The short-notice warning is a solid berry band with sugar text and icon.** This is a recorded craft-floor deviation, kept because it is the one message that must interrupt the form; it is not a pattern for other notices or surfaces.

### Flavour Cross-Section
A stacked cake of rounded layer bars (sugar top, then pistachio mousse, butter sponge and rose mousse tiers overlapping by −6px) on a sugar plate inside the lifted sugar builder slab; tiers re-colour over 0.5s as flavour chips change. Beside it, price rows at the inner radius with Caprasimo amounts.

### Gallery Tiles
Square tiles at the inner radius on their paste colour; image scales 1.04 on hover over 0.9s; a sugar name label rises in on hover/focus (always shown on touch and small screens). Opens a sugar-veiled lightbox with round sugar controls.

## Scale exceptions

- The home hero headline runs smaller than `display` (clamp 2.5rem to 4.4rem) so the occasion pots stay inside the first viewport.
- The order summary estimate uses a reduced numeral (clamp 3rem to 4.6rem) because it lives in the narrow sidebar.
- A cake layer's lower corners use 10px so the stacked layers read as one cake. Focus outlines use a 6px radius.
- In CSS these map to `--fs-subtitle`, `--fs-small`, `--fs-caption`, `--r-field` and `--r-layer`.

## Do's and Don'ts

### Do:
- **Do** build every region as a paste slab (`--c` paste + `--g` gel) on the sugar ground with a 12–20px seam.
- **Do** use the three-family occasion map (rose: bröllop, sockerblommor; butter: barn, fest; pistachio: student, bakelser/företag) wherever an occasion appears, and keep adjacent slabs in different families.
- **Do** create hierarchy by overlapping slabs and lifting the top one with the lift shadow.
- **Do** set type and actions in plum and berry; set every price in Caprasimo with tabular figures and tick it.
- **Do** keep controls round: pill buttons, paste-pill tabs, colour pots, dotted tags.
- **Do** honour reduced motion: re-tints, ticks and hover lifts collapse to instant.

### Don't:
- **Don't** use eyebrows, kickers or uppercase tracked labels above headings.
- **Don't** use boxed cards or bordered panels to structure content. A single 1.5px paste-line hairline is allowed only to set a sub-part apart inside a slab (the hero's occasion picker, the footer fine print).
- **Don't** use stripes, gradients or patterned fills on slabs; paste is a flat colour. (The range slider's hard-stop fill is a control track, not a surface.)
- **Don't** separate sections with full-bleed white bands.
- **Don't** fill a surface with a gel colour or set text in a paste or gel colour.
- **Don't** add a dark theme; the world is single light by design.
- **Don't** extend the solid berry warning band to other notices.
