# art/ — STRYV design files → print-ready output

Drop your exported design PNGs here and the script turns them into upload-ready print files
(transparent background + a white/reversed version for dark shirts, stamped 300 DPI).

## How to use

1. **Export** each STRYV design from your AI tool / Kittl as a **PNG** (highest resolution).
2. **Save them into `art/input/`** with clear names, e.g.:
   - `stryv-wordmark.png`  (the small chest mark)
   - `stryv-back.png`      (the ATHLETIC CLUB back graphic)
3. **Run the script** from the repo root:
   ```bash
   pip install Pillow numpy      # first time only
   python3 art/process_designs.py --width 4000     # back graphic
   # or process the chest mark smaller:
   python3 art/process_designs.py --width 1200
   ```
4. **Grab your files** from `art/output/`:
   - `*-transparent.png` → use on **light** garments (black/red art, clear background)
   - `*-reversed.png`   → use on **dark** garments (black ink flipped to white, red kept)

## Options

- `--width N` — scale the output to N pixels wide. Suggested: **back ~3600–4200** (12–14" @300DPI),
  **chest mark ~1000–1400**. Omit to keep native size.
- `--white-thresh` (default 235) — raise if bits of background remain; lower if edges get eaten.
- `--black-thresh` (default 60) — raise if dark-but-not-black parts should flip to white in the
  reversed version; lower to be stricter about what counts as "ink".

## Notes

- Works best on art with a **clean white/near-white background** (which your AI prompts were
  written to produce). Busy or textured backgrounds may need a manual cleanup pass in Photopea/Kittl.
- The reversed version keeps **any colored pixels** (like the red V) as-is — only near-black ink
  flips to white. Check the output and tune `--black-thresh` if needed.
- For the wordmark you'll reuse everywhere (products + neck label), consider **vectorizing** it in
  Kittl too, so it stays razor-sharp at any size.

Once your files are in `art/input/`, I can run this for you and tune the thresholds to your
actual designs — just let me know they're added.
