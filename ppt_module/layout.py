#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cursor-based vertical layout.

The legacy scripts place every shape at a hand-picked absolute (left, top)
coordinate, so stacking element B under element A requires guessing A's
height correctly -- guess too small and B overlaps A's text. VStack removes
the guess: each `add_*` call places its shape at the stack's current cursor
and advances the cursor by that shape's *actual* rendered height (as
measured by text_metrics / returned by textbox.add_textbox), plus a gap.
Two blocks added to the same VStack can never overlap by construction.
"""

from .textbox import add_textbox as _add_textbox
from .shapes import add_rect as _add_rect


class VStack:
    def __init__(self, slide, left, top, width, gap=0.12):
        self.slide = slide
        self.left = left
        self.width = width
        self.gap = gap
        self.cursor_y = top

    @property
    def y(self):
        return self.cursor_y

    def add_textbox(self, text, size_pt, **kwargs):
        kwargs.setdefault("width", self.width)
        width = kwargs.pop("width")
        result = _add_textbox(self.slide, self.left, self.cursor_y, width, text, size_pt, **kwargs)
        self.cursor_y += result.height_in + self.gap
        return result

    def add_rect(self, height_in, **kwargs):
        kwargs.setdefault("width", self.width)
        width = kwargs.pop("width")
        shape = _add_rect(self.slide, self.left, self.cursor_y, width, height_in, **kwargs)
        self.cursor_y += height_in + self.gap
        return shape

    def add_space(self, height_in):
        self.cursor_y += height_in

    def skip_gap(self):
        """Cancel the gap added by the previous add_* call, for when the next
        block should sit flush against the last one (e.g. a colored strip
        under a card header)."""
        self.cursor_y -= self.gap
