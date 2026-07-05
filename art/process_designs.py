#!/usr/bin/env python3
"""
STRYV design -> print-ready files.

Drop your exported design PNGs into art/input/ and run this. For each input it writes
to art/output/:
  <name>-transparent.png : art with the white background removed, 300 DPI  (for LIGHT shirts)
  <name>-reversed.png    : dark-shirt version (black ink -> white, red/other colors kept),
                           background transparent, 300 DPI                 (for DARK shirts)

Both are stamped at 300 DPI and (optionally) scaled to a target print width so they upload
clean to Apliiq / any POD editor.

Usage:
  python3 art/process_designs.py                 # process all PNGs in art/input/
  python3 art/process_designs.py --width 4000    # also scale outputs to 4000px wide
  python3 art/process_designs.py --white-thresh 230 --black-thresh 70   # tune edges

Suggested widths: back graphic ~3600-4200 (12-14" @300DPI); chest mark ~1000-1400.
"""
import argparse
import glob
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
IN_DIR = os.path.join(HERE, "input")
OUT_DIR = os.path.join(HERE, "output")
DPI = (300, 300)


def load_rgba(path):
    return np.array(Image.open(path).convert("RGBA"), dtype=np.uint8)


def bg_mask(arr, white_thresh):
    """True where the pixel is (near-)white background."""
    rgb = arr[..., :3].astype(np.int16)
    return np.all(rgb >= white_thresh, axis=-1)


def ink_mask(arr, black_thresh):
    """True where the pixel is (near-)black ink."""
    rgb = arr[..., :3].astype(np.int16)
    return np.all(rgb <= black_thresh, axis=-1)


def make_transparent(arr, white_thresh):
    out = arr.copy()
    out[bg_mask(out, white_thresh), 3] = 0
    return out


def make_reversed(arr, white_thresh, black_thresh):
    out = arr.copy()
    bg = bg_mask(out, white_thresh)
    ink = ink_mask(out, black_thresh) & ~bg
    out[ink, :3] = 255            # black ink -> white
    out[bg, 3] = 0                # background -> transparent
    return out


def save(arr, path, width=None):
    img = Image.fromarray(arr, "RGBA")
    if width and img.width != width:
        h = round(img.height * width / img.width)
        img = img.resize((width, h), Image.LANCZOS)
    img.save(path, dpi=DPI)
    print(f"  wrote {os.path.relpath(path, HERE)}  ({img.width}x{img.height} @300DPI)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=None, help="scale outputs to this pixel width")
    ap.add_argument("--white-thresh", type=int, default=235, help="0-255; higher = less removed")
    ap.add_argument("--black-thresh", type=int, default=60, help="0-255; higher = more counts as ink")
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    inputs = sorted(glob.glob(os.path.join(IN_DIR, "*.png")) +
                    glob.glob(os.path.join(IN_DIR, "*.jpg")) +
                    glob.glob(os.path.join(IN_DIR, "*.jpeg")))
    if not inputs:
        print(f"No images found in {os.path.relpath(IN_DIR, HERE)}/ — drop your design PNGs there first.")
        return

    for path in inputs:
        name = os.path.splitext(os.path.basename(path))[0]
        print(f"{name}:")
        arr = load_rgba(path)
        save(make_transparent(arr, args.white_thresh),
             os.path.join(OUT_DIR, f"{name}-transparent.png"), args.width)
        save(make_reversed(arr, args.white_thresh, args.black_thresh),
             os.path.join(OUT_DIR, f"{name}-reversed.png"), args.width)


if __name__ == "__main__":
    main()
