#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared color/font theme for pptx generation scripts."""

from dataclasses import dataclass

from pptx.dml.color import RGBColor

# The deck is primarily reviewed on Windows/PowerPoint and in VS Code's local
# webview. Malgun Gothic is available in both of those Windows renderers, which
# avoids layout shifts caused by requesting an uninstalled Noto family.
FONT_KR = "Malgun Gothic"

# Standard PowerPoint widescreen slide size used by every generator in this repo.
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5


@dataclass(frozen=True)
class Theme:
    bg_cream: RGBColor
    bg_dark: RGBColor
    bg_dark_card: RGBColor
    bg_sand: RGBColor
    bg_white: RGBColor

    ink_navy: RGBColor
    ink_slate: RGBColor
    ink_muted: RGBColor
    ink_light: RGBColor
    ink_light_muted: RGBColor

    accent_rust: RGBColor
    accent_gold: RGBColor
    accent_teal: RGBColor

    border_warm: RGBColor
    border_dark: RGBColor

    font_name: str = FONT_KR


DEFAULT_THEME = Theme(
    bg_cream=RGBColor(248, 245, 240),
    bg_dark=RGBColor(26, 33, 46),
    bg_dark_card=RGBColor(38, 47, 64),
    bg_sand=RGBColor(238, 233, 224),
    bg_white=RGBColor(255, 255, 255),
    ink_navy=RGBColor(26, 33, 46),
    ink_slate=RGBColor(85, 94, 108),
    ink_muted=RGBColor(135, 142, 153),
    ink_light=RGBColor(242, 239, 233),
    ink_light_muted=RGBColor(178, 186, 198),
    accent_rust=RGBColor(198, 83, 45),
    accent_gold=RGBColor(209, 152, 48),
    accent_teal=RGBColor(49, 107, 105),
    border_warm=RGBColor(218, 211, 199),
    border_dark=RGBColor(62, 74, 96),
)
