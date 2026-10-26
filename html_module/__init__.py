#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lightweight HTML deck builder — the replacement for ``ppt_module``.

This repo moved off PPTX entirely. The old module existed only to fight two
PPTX-specific problems: python-pptx's ``<a:spAutoFit/>`` default silently
resizing shapes, and having to hand-measure text to avoid overlap in a format
with no native reflow. HTML/CSS reflows text itself, so neither problem
exists here — this module is deliberately much smaller.
"""

from .theme import Theme, FONT_STACK
from .render import Deck, esc
from . import components

__all__ = ["Theme", "FONT_STACK", "Deck", "esc", "components"]
