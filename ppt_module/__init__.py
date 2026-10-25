#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reusable pptx-generation building blocks.

See AGENTS.md at the repo root for when/how this package must be used.
"""

from .theme import Theme, DEFAULT_THEME, FONT_KR, SLIDE_W_IN, SLIDE_H_IN
from .shapes import set_font, set_slide_background, disable_shadow, add_rect
from .textbox import add_textbox, TextBoxResult
from .layout import VStack
from .text_metrics import wrap_text, count_wrapped_lines, measure_block_height_in, get_pil_font
from . import validate

__all__ = [
    "Theme", "DEFAULT_THEME", "FONT_KR", "SLIDE_W_IN", "SLIDE_H_IN",
    "set_font", "set_slide_background", "disable_shadow", "add_rect",
    "add_textbox", "TextBoxResult",
    "VStack",
    "wrap_text", "count_wrapped_lines", "measure_block_height_in", "get_pil_font",
    "validate",
]
