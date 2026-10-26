#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pixel-accurate(ish) text measurement used to size text boxes *before* they
are drawn, instead of guessing a height and hoping the text fits.

This is the fix for the root cause of overlapping / out-of-frame text in the
existing build_*.py scripts: those scripts hard-code a box height per call
site with no relationship to the actual font size, line count, or wrapping
width, so any text that is longer than the author guessed silently overflows
the box and collides with whatever is drawn below it.
"""

import os
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont

_FONT_CANDIDATES = {
    True: [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
        "/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ],
    False: [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
        "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ],
}

# Screen-rendering DPI assumption used only to translate point sizes into the
# pixel grid Pillow measures in; it cancels out as long as it's used
# consistently for both font loading and width conversion below.
_DPI = 96.0
# PowerPoint's single-line height is noticeably taller than a font's raw
# glyph bounding box (it reserves room for ascenders/descenders). 1.2 is the
# typical Latin single-spacing leading multiplier, but this project is
# overwhelmingly Korean/CJK text, whose fonts commonly reserve ~25-30% extra
# vertical room per line (full-width glyphs carry more built-in leading than
# Latin text does). Measured against real LibreOffice/PowerPoint renders that
# still showed visible overlap at 1.2, 1.3 tracks CJK line height much more
# closely.
_LEADING_FACTOR = 1.3
_PARAGRAPH_GAP_FACTOR = 0.12
_DRAW = ImageDraw.Draw(Image.new("RGB", (4, 4)))


@lru_cache(maxsize=64)
def get_pil_font(size_pt, bold=False):
    px = max(1, round(size_pt * _DPI / 72.0))
    for path in _FONT_CANDIDATES[bool(bold)]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, px)
            except Exception:
                pass
    return ImageFont.load_default()


def _text_width_px(text, font):
    return _DRAW.textlength(text, font=font)


def _wrap_single_line(line, font, max_width_px):
    """Greedy word-wrap with a character-level fallback for tokens (common in
    unspaced Korean/CJK runs) that are themselves wider than the box."""
    if line == "":
        return [""]

    lines = []
    current = ""
    for word in line.split(" "):
        piece = word
        while piece:
            trial = f"{current} {piece}".strip() if current else piece
            if _text_width_px(trial, font) <= max_width_px:
                current = trial
                piece = ""
            elif current:
                lines.append(current)
                current = ""
            else:
                lo, hi, fit = 1, len(piece), 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if _text_width_px(piece[:mid], font) <= max_width_px:
                        fit = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1
                lines.append(piece[:fit])
                piece = piece[fit:]
    if current:
        lines.append(current)
    return lines if lines else [""]


def wrap_text(text, size_pt, width_in, bold=False):
    """Returns the list of visually-wrapped lines `text` would occupy in a
    box `width_in` inches wide. Explicit "\\n" in `text` are treated as hard
    paragraph breaks (matching how add_textbox() in this package renders them
    as separate DrawingML paragraphs, NOT how a bare run.text="a\\nb" renders
    in raw python-pptx, which is as a single unbroken line)."""
    font = get_pil_font(size_pt, bold=bold)
    max_width_px = max(width_in, 0.05) * _DPI
    out = []
    for para in str(text).split("\n"):
        out.extend(_wrap_single_line(para, font, max_width_px))
    return out


def count_wrapped_lines(text, size_pt, width_in, bold=False):
    return max(len(wrap_text(text, size_pt, width_in, bold=bold)), 1)


def line_height_in(size_pt, line_spacing=1.0):
    return (size_pt * _LEADING_FACTOR * line_spacing) / 72.0


def measure_block_height_in(text, size_pt, width_in, bold=False, line_spacing=1.0, safety_margin=1.12):
    """Estimated rendered height (inches) of `text` word-wrapped to
    `width_in` inches, at `size_pt`. `safety_margin` pads the result to
    absorb the gap between this heuristic and the real PowerPoint/LibreOffice
    layout engine -- better to reserve a hair too much height than to repeat
    the overlap bug this module exists to fix."""
    n_lines = count_wrapped_lines(text, size_pt, width_in, bold=bold)
    hard_breaks = max(len(str(text).split("\n")) - 1, 0)
    paragraph_gaps = hard_breaks * size_pt * _PARAGRAPH_GAP_FACTOR / 72.0
    return n_lines * line_height_in(size_pt, line_spacing=line_spacing) * safety_margin + paragraph_gaps
