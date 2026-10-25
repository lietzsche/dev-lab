#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Textbox helper that measures text before drawing it.

Two concrete bugs in the legacy build_novel_ppt.py / build_custom_novel_ppt.py
scripts are fixed here:

1. ``run.text = "line one\\nline two"`` does NOT create a line break in
   python-pptx -- it writes a literal ``\\n`` character into a single
   ``<a:t>`` run, which PowerPoint/LibreOffice render as nothing (the two
   lines get mashed together) rather than as two lines. Every multi-line
   string in the legacy scripts (dozens of call sites) is silently affected.
   ``add_textbox`` here splits on "\\n" and emits a real ``<a:br/>`` between
   segments.

2. Box heights in the legacy scripts are hand-picked constants with no
   relation to the actual text length / font size / wrap width, so anything
   longer than the author guessed overflows the box and collides with
   whatever is drawn below it. ``add_textbox`` here measures the text via
   ``text_metrics`` and either (a) computes the height itself, or (b), if a
   fixed height/max_height is given and the text doesn't fit, shrinks the
   font size (PowerPoint's own "shrink text on overflow" behavior) down to
   ``min_size_pt`` before giving up and *loudly* warning -- it never just
   lets text silently spill out of its box.
"""

from dataclasses import dataclass

from pptx.util import Inches
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE

from .theme import FONT_KR, DEFAULT_THEME
from .shapes import set_font
from .text_metrics import measure_block_height_in

_VERT_MARGIN_RATIO = 0.7  # matches the legacy scripts' top/bottom margin convention


@dataclass
class TextBoxResult:
    shape: object
    text_frame: object
    left_in: float
    top_in: float
    width_in: float
    height_in: float
    size_pt: float
    overflowed: bool  # True if the text still doesn't fit even at min_size_pt


def _shrink_to_fit(text, width_in, avail_height_in, start_size_pt, bold, line_spacing, min_size_pt, step=0.5):
    size = start_size_pt
    while size > min_size_pt:
        if measure_block_height_in(text, size, width_in, bold=bold, line_spacing=line_spacing) <= avail_height_in:
            return size, False
        size -= step
    overflow = measure_block_height_in(text, min_size_pt, width_in, bold=bold, line_spacing=line_spacing) > avail_height_in
    return min_size_pt, overflow


def _write_runs(paragraph, text, size_pt, bold, italic, color, font_name):
    segments = str(text).split("\n")
    for i, seg in enumerate(segments):
        if i > 0:
            paragraph.add_line_break()
        run = paragraph.add_run()
        run.text = seg
        set_font(run, size_pt, bold=bold, italic=italic, color=color, font_name=font_name)


def add_textbox(slide, left, top, width, text, size_pt, *,
                 height=None, min_height=0.18, max_height=None,
                 bold=False, italic=False, color=None,
                 align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
                 line_spacing=1.25, margin_in=0.06, font_name=FONT_KR,
                 min_size_pt=8.0, autoshrink=True, warn=True):
    """Adds a textbox whose height is derived from the text unless `height`
    is given, and whose font shrinks (rather than overflows) when the text
    doesn't fit `height`/`max_height`. Returns a TextBoxResult so callers
    (e.g. layout.VStack) know the box's *actual* rendered height.
    """
    if color is None:
        color = DEFAULT_THEME.ink_navy

    content_width_in = max(width - 2 * margin_in, 0.1)
    v_margin_in = margin_in * _VERT_MARGIN_RATIO
    overflowed = False

    if height is None:
        needed_text_h = measure_block_height_in(text, size_pt, content_width_in, bold=bold, line_spacing=line_spacing)
        box_h = needed_text_h + 2 * v_margin_in
        if max_height is not None and box_h > max_height:
            avail = max_height - 2 * v_margin_in
            size_pt, overflowed = _shrink_to_fit(text, content_width_in, avail, size_pt, bold, line_spacing, min_size_pt)
            box_h = max_height
        box_h = max(box_h, min_height)
    else:
        box_h = height
        if autoshrink:
            avail = max(box_h - 2 * v_margin_in, 0.02)
            needed_text_h = measure_block_height_in(text, size_pt, content_width_in, bold=bold, line_spacing=line_spacing)
            if needed_text_h > avail:
                size_pt, overflowed = _shrink_to_fit(text, content_width_in, avail, size_pt, bold, line_spacing, min_size_pt)

    if overflowed and warn:
        preview = str(text).strip().splitlines()[0][:40] if str(text).strip() else ""
        print(
            f"[ppt_module.textbox] WARNING: text still overflows its box even at "
            f"{min_size_pt}pt -- '{preview}...' in a {width:.2f}x{box_h:.2f}in box at "
            f"({left:.2f}, {top:.2f})"
        )

    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(box_h))
    tf = tb.text_frame
    tf.word_wrap = True
    # python-pptx defaults new textboxes to SHAPE_TO_FIT_TEXT (<a:spAutoFit/>):
    # PowerPoint/LibreOffice silently RESIZE the shape to fit its text on open,
    # growing it past whatever height we just computed and overlapping
    # whatever sits below. TEXT_TO_FIT_SHAPE (<a:normAutofit/>) does the
    # opposite -- it shrinks the font to the box using the real renderer's
    # own metrics, which is also a backstop against any remaining error in
    # our own Pillow-based height estimate.
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf.vertical_anchor = anchor
    tf.margin_left = Inches(margin_in)
    tf.margin_right = Inches(margin_in)
    tf.margin_top = Inches(v_margin_in)
    tf.margin_bottom = Inches(v_margin_in)

    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    if text:
        _write_runs(p, text, size_pt, bold, italic, color, font_name)

    return TextBoxResult(
        shape=tb, text_frame=tf,
        left_in=left, top_in=top, width_in=width, height_in=box_h,
        size_pt=size_pt, overflowed=overflowed,
    )
