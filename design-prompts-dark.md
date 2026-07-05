# STRYV Dark Gothic Prompt Pack (Darc-Sport-inspired)

Creative front + back prompts in the **dark cinematic gothic streetwear** lane — the Darc Sport
genre — but built for **STRYV** with its own identity. Read alongside
[`design-prompts.md`](./design-prompts.md) and [`sourcing-and-ai-design.md`](./sourcing-and-ai-design.md).

## The aesthetic we're channeling
Dark, moody, cinematic. Blackletter/gothic + heavy condensed type. Distressed/grungy textures.
Classical statue & angelic imagery. A signature animal/emblem. **Monochrome black** with a single
**blood-red** or **bone-white** accent — which ties straight into STRYV's existing red "V".

> ⚠️ **Take after the vibe, not the assets.** Do NOT copy Darc's wolf, logos, or specific
> graphics — that's a knockoff and a legal risk. Give STRYV its **own** signature motif (below) so
> you build a cult brand, not a bootleg. Also keep the DSHEA-style rule from before: no other
> brand's logos/characters/real people in your generations.

## Give STRYV its own signature animal/emblem
Darc owns wolves. Pick something else strong and ownable for STRYV — options to try:
**raven/crow** (dark, sharp), **black lion / lioness** (heraldic "Athletic Club" strength),
**ram** (grit, horns read great in gothic), **serpent**, or **panther**. My pick for the
"Athletic Club" angle: a **heraldic lion or ram crest**. Generate a few and see what feels like STRYV.

## Print rules baked in (same as always)
- **"isolated on plain white background, centered"** → clean extraction (use the `art/` pipeline
  to make transparent + reversed-for-dark-shirt versions).
- **Limited palette:** black + one accent (blood red or bone white). Fewer colors = premium + cheaper.
- **Graphic/vector concepts** → run in Midjourney/Ideogram, extract, place. **Photographic/statue
  concepts** → print as detailed **DTF** full-image (they won't cleanly vectorize).
- Chest `--ar 1:1`; back `--ar 4:5`; add `--style raw --v 7` in Midjourney.
- Text-heavy pieces → **Ideogram** (accurate letters); graphics → **Midjourney**.

---

## Concept 1 — Gothic Blackletter "STRYV" (the cornerstone)

**FRONT (chest) — Ideogram:**
```
Small gothic blackletter chest logo, the word "STRYV" in an ornate medieval blackletter
typeface, single bone-white color with subtle distressed texture, isolated on plain white
background, centered, high contrast, flat print style, no shirt, no mockup
```
**BACK (statement) — Ideogram:**
```
Large gothic back print, "STRYV" in huge ornate blackletter across the top, "ATHLETIC CLUB"
in a heavy condensed gothic sans beneath, a small blood-red cross or star accent, distressed
grunge texture, dark cinematic streetwear poster, bone-white and one red accent, high contrast,
isolated on plain white background, centered
```

## Concept 2 — Classical Statue / Angelic (very "Darc")

**FRONT (chest) — Midjourney:**
```
Small chest emblem, a cracked classical marble statue face in profile, grungy halftone
texture, monochrome greyscale with one blood-red accent, gothic streetwear, isolated on
plain white background, centered, high detail --ar 1:1 --style raw --v 7
```
**BACK (statement) — Midjourney:**
```
Cinematic back graphic, a weathered classical Greek marble statue of an athlete or angel
draped in shadow, dramatic chiaroscuro lighting, distressed halftone and scratch textures,
gothic blackletter "STRYV" arched above and "ATHLETIC CLUB" below, monochrome greyscale with a
single blood-red accent, dark luxury streetwear, isolated on plain white background, centered
--ar 4:5 --style raw --v 7
```

## Concept 3 — Signature Beast Crest (build STRYV's mascot)

**FRONT (chest) — Midjourney:**
```
Small heraldic chest crest, a snarling [lion / ram / raven] head emblem, bold gothic linework,
single bone-white color, distressed texture, isolated on plain white background, centered, flat
high-contrast print style, no shirt --ar 1:1 --style raw --v 7
```
**BACK (statement) — Midjourney:**
```
Bold back graphic, a fierce heraldic [lion / ram / raven] crest inside an ornate gothic frame,
"STRYV ATHLETIC CLUB" in blackletter around it like a medieval seal, distressed grunge texture,
bone-white with a single blood-red accent, dark cinematic streetwear, flat print, isolated on
plain white background, centered --ar 4:5 --style raw --v 7
```

## Concept 4 — Dark Cinematic Scene (moody, atmospheric)

**FRONT (chest) — Ideogram:**
```
Tiny minimalist chest text "STRYV" in a sharp condensed gothic font, blood-red, isolated on
plain white background, centered, flat, high contrast, no shirt, no mockup
```
**BACK (statement) — Midjourney:**
```
Cinematic dark back print, a lone hooded figure walking through fog and rain under a single
streetlight, dramatic silhouette, heavy film grain and halftone, moody greyscale with one
blood-red accent, gothic blackletter "STRYV" overlaid, "KEEP STRYVING" small beneath, dark
streetwear poster, isolated on plain white background, centered --ar 4:5 --style raw --v 7
```

## Concept 5 — Gothic × Athletic Club Fusion (varsity meets gothic)

**FRONT (chest) — Ideogram:**
```
Small left-chest mark, a gothic-style varsity number "01" beside "STRYV" in blackletter,
bone-white with a red accent, distressed texture, isolated on plain white background, centered,
flat print style, no shirt
```
**BACK (statement) — Ideogram:**
```
Large back print fusing collegiate and gothic, "STRYV" in massive blackletter, "ATHLETIC CLUB"
in bold arched varsity lettering beneath, "EST. — KEEP STRYVING" tagline, distressed vintage
texture, bone-white with a single blood-red accent, dark streetwear, high contrast, isolated on
plain white background, centered
```

---

## Tagline options for the dark direction
- **KEEP STRYVING** (your core rallying cry — works everywhere)
- **BUILT IN THE DARK**
- **NO GODS NO LIMITS**
- **EARN YOUR PLACE**
- **THE PACK / THE CLUB**  ·  **STRENGTH IN SHADOW**

## Tuning tips
- Too clean/glossy? add `flat, screen-print, no 3D, no gradients` (for graphic concepts).
- Want grittier? add `heavy grain, halftone dots, photocopied texture, distressed edges`.
- Keep the palette to **black + one accent** — that restraint is what reads as premium/Darc-like.
- Generate **4–6 variations**, pick the strongest, then iterate that one instead of restarting.
- Lead with **Concept 1 or 3** as your hero drop — a strong wordmark + a signature crest is the
  backbone of a cult brand.

---

Once you generate a few, drop the PNG exports in `art/input/` and I'll make them print-ready
(transparent + reversed-for-dark-shirts) via the pipeline.
