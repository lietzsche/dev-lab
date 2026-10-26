#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-build safety net: scan the shapes python-pptx actually produced for
out-of-bounds placement and text-box-on-text-box overlap. This works on any
slide/presentation object regardless of how the shapes were added (hand
placed, VStack, or legacy add_rect/add_textbox calls), so it is useful both
as a final check in new scripts and as a diagnostic against the existing
build_novel_ppt.py / build_custom_novel_ppt.py output.

Run this before `prs.save(...)` -- a slide should always come back clean.
"""

from .theme import SLIDE_W_IN, SLIDE_H_IN
from .text_metrics import count_wrapped_lines, measure_block_height_in
from .textbox import MULTILINE_FIT_HEADROOM

_EMU_PER_IN = 914400.0


def _bbox_in(shape):
    return (
        shape.left / _EMU_PER_IN,
        shape.top / _EMU_PER_IN,
        shape.width / _EMU_PER_IN,
        shape.height / _EMU_PER_IN,
    )


def _visible_text(shape):
    if not getattr(shape, "has_text_frame", False):
        return ""
    return shape.text_frame.text.strip()


def _text_fit_ratio(shape):
    """Estimate how much of a text box's usable height its authored text uses.

    Coordinate-only overlap checks cannot detect text that is still inside its
    nominal shape but is packed so tightly that another renderer's font metrics
    make adjacent lines collide. Generated text boxes use one style per box, so
    the largest explicit run size is a conservative and stable measurement.
    """
    tf = shape.text_frame
    runs = [run for paragraph in tf.paragraphs for run in paragraph.runs]
    sizes = [run.font.size.pt for run in runs if run.font.size is not None]
    if not sizes:
        return None

    size_pt = max(sizes)
    bold = any(run.font.bold is True for run in runs)
    spacings = [
        paragraph.line_spacing
        for paragraph in tf.paragraphs
        if isinstance(paragraph.line_spacing, float)
    ]
    line_spacing = max(spacings, default=1.0)
    content_width = max(
        (shape.width - tf.margin_left - tf.margin_right) / _EMU_PER_IN,
        0.05,
    )
    available_height = max(
        (shape.height - tf.margin_top - tf.margin_bottom) / _EMU_PER_IN,
        0.01,
    )
    text = tf.text.replace("\v", "\n")
    required_height = measure_block_height_in(
        text,
        size_pt,
        content_width,
        bold=bold,
        line_spacing=line_spacing,
    )
    line_count = count_wrapped_lines(text, size_pt, content_width, bold=bold)
    return required_height / available_height, line_count


def _overlap_area(a, b):
    ax0, ay0, aw, ah = a
    bx0, by0, bw, bh = b
    ox = max(0.0, min(ax0 + aw, bx0 + bw) - max(ax0, bx0))
    oy = max(0.0, min(ay0 + ah, by0 + bh) - max(ay0, by0))
    return ox * oy


def check_slide(slide, slide_w_in=SLIDE_W_IN, slide_h_in=SLIDE_H_IN, index=None, tolerance_in=0.02):
    warnings = []
    label = f"slide {index}" if index is not None else "slide"
    text_boxes = []

    for shape in slide.shapes:
        if shape.left is None or shape.top is None or shape.width is None or shape.height is None:
            continue
        left, top, w, h = _bbox_in(shape)
        text = _visible_text(shape)
        tag = text.splitlines()[0][:40] if text else f"<{shape.shape_type}>"

        if (left < -tolerance_in or top < -tolerance_in
                or left + w > slide_w_in + tolerance_in or top + h > slide_h_in + tolerance_in):
            warnings.append(
                f"{label}: shape '{tag}' at ({left:.2f},{top:.2f}) size "
                f"{w:.2f}x{h:.2f}in extends outside the {slide_w_in}x{slide_h_in}in slide"
            )

        if text:
            text_boxes.append((tag, (left, top, w, h)))
            fit = _text_fit_ratio(shape)
            # Single-line boxes cannot suffer line-to-line collisions. For two
            # or more lines, enforce the same deliberate headroom as add_textbox.
            if fit is not None:
                fit_ratio, explicit_lines = fit
            else:
                fit_ratio, explicit_lines = None, 0
            if (fit_ratio is not None and explicit_lines > 1
                    and fit_ratio > MULTILINE_FIT_HEADROOM + 0.035):
                warnings.append(
                    f"{label}: text '{tag}' uses {fit_ratio:.0%} of its usable "
                    f"height (maximum {MULTILINE_FIT_HEADROOM + 0.035:.0%})"
                )

    for i in range(len(text_boxes)):
        tag_a, box_a = text_boxes[i]
        for j in range(i + 1, len(text_boxes)):
            tag_b, box_b = text_boxes[j]
            if _overlap_area(box_a, box_b) > tolerance_in * tolerance_in:
                warnings.append(f"{label}: text '{tag_a}' overlaps text '{tag_b}'")

    return warnings


def check_presentation(prs, raise_on_error=False):
    all_warnings = []
    for idx, slide in enumerate(prs.slides, start=1):
        all_warnings.extend(check_slide(slide, index=idx))

    if all_warnings:
        if raise_on_error:
            raise ValueError("PPTX layout validation failed:\n" + "\n".join(all_warnings))
        print(f"[ppt_module.validate] {len(all_warnings)} layout issue(s) found:")
        for w in all_warnings:
            print(f"  - {w}")
    return all_warnings
