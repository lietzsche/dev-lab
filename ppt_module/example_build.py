#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal worked example of this package's intended usage pattern.

Run directly (`python3 ppt_module/example_build.py`) to generate a one-slide
sanity-check deck at /tmp/ppt_module_example.pptx and print the validator's
report (should be empty). New slide-building scripts should follow this
shape: a VStack per column instead of hand-picked (left, top) pairs, and a
validate.check_presentation() call right before prs.save().
"""

from pptx import Presentation
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN

from ppt_module import (
    DEFAULT_THEME, SLIDE_W_IN, SLIDE_H_IN,
    set_slide_background, add_rect, add_textbox, VStack, validate,
)

THEME = DEFAULT_THEME


def build_example_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, THEME.bg_cream)

    add_textbox(
        slide, 0.65, 0.5, 12.0, "모듈화된 PPTX 빌더 예시", 24,
        bold=True, color=THEME.ink_navy,
    )

    # A deliberately long string with embedded "\n" -- this is exactly the
    # pattern that silently collapsed into one unbroken, mis-wrapped line in
    # the legacy build_*.py scripts. Here it renders as real line breaks and
    # the box is sized to whatever height the wrapped text actually needs.
    body_text = (
        "첫째 줄: 이 텍스트박스는 높이를 직접 지정하지 않았다.\n"
        "둘째 줄: add_textbox가 실제 줄바꿈과 word-wrap 폭을 기준으로 필요한 높이를 계산한다.\n"
        "셋째 줄: 그 결과 아래 블록은 항상 이 블록의 실제 높이만큼 내려가 배치되어 겹치지 않는다."
    )

    stack = VStack(slide, left=0.65, top=1.2, width=6.0, gap=0.2)
    stack.add_textbox(body_text, 13, color=THEME.ink_slate, line_spacing=1.3)
    stack.add_rect(0.05, fill_color=THEME.border_warm)
    stack.add_textbox(
        "위 구분선 아래의 두 번째 카드 — 겹치지 않고 자동으로 이어진다.",
        13, bold=True, color=THEME.accent_rust,
    )

    # Fixed-height box on purpose, to exercise the autoshrink path: this text
    # does not fit 13pt in 0.4in, so add_textbox shrinks the font instead of
    # letting it spill into whatever is drawn next.
    add_textbox(
        slide, 0.65, 6.6, 6.0, "강제로 작은 박스에 넣은 긴 설명 텍스트 — 폭주하지 않고 글자 크기가 줄어든다.",
        13, height=0.4, color=THEME.bg_white, align=PP_ALIGN.LEFT,
    )
    add_rect(slide, 0.65, 6.6, 6.0, 0.4, fill_color=THEME.ink_navy)
    # (rect drawn after so it's visible behind the shrink-tested textbox when
    # inspecting the XML; order doesn't matter for the validator.)


def main():
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W_IN)
    prs.slide_height = Inches(SLIDE_H_IN)

    build_example_slide(prs)

    warnings = validate.check_presentation(prs)
    if not warnings:
        print("[ppt_module.example_build] validate: no overlap/out-of-bounds issues found.")

    out_path = "/tmp/ppt_module_example.pptx"
    prs.save(out_path)
    print(f"[ppt_module.example_build] saved {out_path}")


if __name__ == "__main__":
    main()
