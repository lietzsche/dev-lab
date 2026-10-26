#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Color palettes shared by the HTML deck builders.

Each deck keeps its own palette (same hex values the old PPTX scripts used,
so the look carries over), expressed as plain hex strings instead of
``RGBColor`` since CSS wants hex/rgb() directly.
"""

from dataclasses import dataclass

# Windows has Malgun Gothic; macOS has Apple SD Gothic Neo; Noto Sans KR
# covers everything else (web font / Linux). Browsers pick the first match,
# so this one stack works everywhere without bundling a font file.
FONT_STACK = "'Malgun Gothic', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif"


@dataclass(frozen=True)
class Theme:
    bg_cream: str
    bg_dark: str
    bg_dark_card: str
    bg_white: str

    ink_navy: str
    ink_slate: str
    ink_muted: str
    ink_light: str
    ink_light_muted: str

    accent: str
    accent_2: str
    accent_3: str

    border_warm: str
    border_dark: str

    font_stack: str = FONT_STACK


NOVEL_GUIDE_THEME = Theme(
    bg_cream="#F8F5F0", bg_dark="#1A212E", bg_dark_card="#262F40", bg_white="#FFFFFF",
    ink_navy="#1A212E", ink_slate="#555E6C", ink_muted="#878E99",
    ink_light="#F2EFE9", ink_light_muted="#B2BAC6",
    accent="#C6532D", accent_2="#D19830", accent_3="#316B69",
    border_warm="#DAD3C7", border_dark="#3E4A60",
)

CUSTOM_NOVEL_THEME = Theme(
    bg_cream="#F6F4EF", bg_dark="#161C28", bg_dark_card="#222B3C", bg_white="#FFFFFF",
    ink_navy="#161C28", ink_slate="#4E5766", ink_muted="#828A96",
    ink_light="#F4F1EA", ink_light_muted="#AFB8C6",
    accent="#C24E2A", accent_2="#CE942C", accent_3="#2A6866",
    border_warm="#D6CFC2", border_dark="#3A465C",
)

CACHE_CITY_THEME = Theme(
    bg_cream="#F6F4EF", bg_dark="#161C28", bg_dark_card="#222B3C", bg_white="#FFFFFF",
    ink_navy="#161C28", ink_slate="#4E5766", ink_muted="#828A96",
    ink_light="#F4F1EA", ink_light_muted="#AFB8C6",
    accent="#2A6866", accent_2="#C24E2A", accent_3="#CE942C",
    border_warm="#D6CFC2", border_dark="#3A465C",
)
