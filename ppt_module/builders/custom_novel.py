#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
작가 비문학 아카이브(파편들 · 리뷰s · ETC) 기반 맞춤형 소설 기획 제안서 PPTX 생성 스크립트
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

from ppt_module import FONT_KR, set_slide_background, add_rect, validate
from ppt_module.textbox import MULTILINE_FIT_HEADROOM, add_textbox as _module_add_textbox
from ppt_module.text_metrics import measure_block_height_in

# ---------------------------------------------------------------------------
# Color Palette (Philosophical Archive & Literary Atelier)
# ---------------------------------------------------------------------------
BG_CREAM = RGBColor(246, 244, 239)       # #F6F4EF Warm Archival Paper
BG_DARK = RGBColor(22, 28, 40)           # #161C28 Deep Midnight Ink
BG_DARK_CARD = RGBColor(34, 43, 60)      # #222B3C Elevated Dark Card
BG_SAND = RGBColor(235, 230, 220)        # #EBE6DC Warm Stone Card
BG_WHITE = RGBColor(255, 255, 255)       # #FFFFFF Crisp Card

INK_NAVY = RGBColor(22, 28, 40)          # #161C28 Primary Heading
INK_SLATE = RGBColor(78, 87, 102)        # #4E5766 Body Copy
INK_MUTED = RGBColor(130, 138, 150)      # #828A96 Caption / Meta
INK_LIGHT = RGBColor(244, 241, 234)      # #F4F1EA Light Text on Dark
INK_LIGHT_MUTED = RGBColor(175, 184, 198)# #AFB8C6 Muted Light Text

ACCENT_RUST = RGBColor(194, 78, 42)      # #C24E2A Terracotta Rust
ACCENT_GOLD = RGBColor(206, 148, 44)     # #CE942C Ochre Gold
ACCENT_TEAL = RGBColor(42, 104, 102)     # #2A6866 Deep Sage Teal
ACCENT_PLUM = RGBColor(118, 54, 82)      # #763652 Philosophical Plum
ACCENT_INDIGO = RGBColor(58, 82, 138)    # #3A528A Analytical Indigo

BORDER_WARM = RGBColor(214, 207, 194)    # #D6CFC2 Card Border
BORDER_DARK = RGBColor(58, 70, 92)       # #3A465C Dark Card Border
SOFT_RUST_BG = RGBColor(250, 235, 229)
SOFT_TEAL_BG = RGBColor(230, 241, 240)
SOFT_GOLD_BG = RGBColor(251, 243, 225)
SOFT_PLUM_BG = RGBColor(244, 233, 238)
SOFT_INDIGO_BG = RGBColor(232, 237, 247)

ASSET_DIR = "/tmp/ppt_custom_novel_assets"
os.makedirs(ASSET_DIR, exist_ok=True)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# Pillow High-Res Visual Asset Generators
# ---------------------------------------------------------------------------
def get_pil_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
        "/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf" if bold else "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf" if bold else "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def generate_cover_constellation():
    """Generates a conceptual constellation mapping the user's non-fiction concepts into fiction."""
    w, h = 1150, 920
    img = Image.new("RGBA", (w, h), (22, 28, 40, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = int(w * 0.54), int(h * 0.48)
    for r, col in [
        (400, (58, 70, 92, 95)),
        (295, (206, 148, 44, 85)),
        (190, (194, 78, 42, 100)),
        (90, (42, 104, 102, 130)),
    ]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=2)

    # Nodes representing the author's key philosophical concepts
    nodes = [
        (cx, cy, "정교한 허구\n(Fiction)", (194, 78, 42, 255), 34),
        (cx - 250, cy - 170, "필연성 (223)", (206, 148, 44, 255), 22),
        (cx + 240, cy - 185, "추론 (190)", (42, 104, 102, 255), 22),
        (cx - 295, cy + 85, "투사·동일시 (232)", (118, 54, 82, 255), 22),
        (cx + 275, cy + 95, "타자·바깥 (100)", (58, 82, 138, 255), 22),
        (cx - 95, cy - 310, "상상·관념 (491)", (206, 148, 44, 255), 20),
        (cx + 125, cy + 285, "흉터·죄책감 (141)", (194, 78, 42, 255), 20),
        (cx - 140, cy + 270, "유효성·기호 (260)", (42, 104, 102, 255), 20),
    ]

    # Connect outer nodes to center and adjacent nodes
    for i in range(1, len(nodes)):
        x1, y1 = nodes[0][0], nodes[0][1]
        x2, y2 = nodes[i][0], nodes[i][1]
        draw.line([(x1, y1), (x2, y2)], fill=(206, 148, 44, 110), width=3)
        nxt = 1 + (i % (len(nodes) - 1))
        draw.line([(x2, y2), (nodes[nxt][0], nodes[nxt][1])], fill=(90, 106, 136, 95), width=2)

    f_center = get_pil_font(24, bold=True)
    f_node = get_pil_font(22, bold=True)

    for idx, (nx, ny, label, col, rad) in enumerate(nodes):
        draw.ellipse([nx - rad - 8, ny - rad - 8, nx + rad + 8, ny + rad + 8], fill=(col[0], col[1], col[2], 70))
        draw.ellipse([nx - rad, ny - rad, nx + rad, ny + rad], fill=col, outline=(244, 241, 234, 230), width=3)
        if idx == 0:
            lines = label.split("\n")
            for li, line in enumerate(lines):
                bbox = draw.textbbox((0, 0), line, font=f_center)
                lw = bbox[2] - bbox[0]
                draw.text((nx - lw // 2, ny + rad + 14 + li * 28), line, font=f_center, fill=(244, 241, 234, 255))
        else:
            bbox = draw.textbbox((0, 0), label, font=f_node)
            lw = bbox[2] - bbox[0]
            ly = ny - rad - 36 if ny <= cy else ny + rad + 12
            draw.text((nx - lw // 2, ly), label, font=f_node, fill=(235, 230, 220, 245))

    path = os.path.join(ASSET_DIR, "cover_constellation.png")
    img.save(path)
    return path


def generate_keyword_chart():
    """Generates a high-resolution horizontal bar chart of actual keyword counts from the 3 PDFs."""
    w, h = 1120, 940
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    data = [
        ("상상 (Imagination)", 263, (194, 78, 42, 255), "가설 설정과 위험 예견의 시뮬레이션"),
        ("관념 (Idea/Concept)", 228, (206, 148, 44, 255), "과잉 관념론 비판 및 기호의 연산"),
        ("필연 (Necessity)", 223, (194, 78, 42, 255), "우연을 배제한 인과적 사슬과 법칙"),
        ("이미지 (Image)", 217, (118, 54, 82, 255), "개념을 대체한 자기애적 거울상 비판"),
        ("추론 (Inference)", 190, (42, 104, 102, 255), "상상을 현실 인식과 타자로 잇는 다리"),
        ("자아 (Ego/Self-Image)", 184, (118, 54, 82, 255), "비대해지려는 자기애적 방어기제"),
        ("유효성 (Validity)", 150, (42, 104, 102, 255), "현실과 허구를 판가름하는 작동 기준"),
        ("동일시 (Identification)", 118, (58, 82, 138, 255), "수동적 이입 vs 능동적 역량 학습"),
        ("투사 (Projection)", 114, (58, 82, 138, 255), "원하는 것만 보려는 소원 성취형 망상"),
        ("허구 · 기호 (Fiction/Sign)", 111, (194, 78, 42, 255), "법칙에 도달하기 위한 필수 매개물"),
        ("도피 (Escape)", 86, (130, 138, 150, 255), "도피하고 있다는 사실 자체에 대한 도피"),
        ("흉터 · 죄책감 (Scar/Guilt)", 71, (22, 28, 40, 255), "병렬 시간의 근원이자 현실 교정의 출발점"),
    ]

    f_label = get_pil_font(22, bold=True)
    f_val = get_pil_font(21, bold=True)
    f_desc = get_pil_font(18, bold=False)

    m_left = 275
    m_top = 32
    row_h = 74
    max_bar_w = 430
    max_val = 280

    for i, (label, val, col, desc) in enumerate(data):
        y = m_top + i * row_h
        # Alternating subtle row strip
        if i % 2 == 0:
            draw.rectangle([15, y - 6, w - 15, y + 56], fill=(246, 244, 239, 255))

        draw.text((26, y + 10), label, font=f_label, fill=(22, 28, 40, 255))

        bw = int((val / max_val) * max_bar_w)
        draw.rounded_rectangle([m_left, y + 8, m_left + bw, y + 44], radius=6, fill=col)
        draw.text((m_left + bw + 12, y + 10), f"{val}회", font=f_val, fill=col)

        # Right side meaning note
        draw.text((m_left + max_bar_w + 90, y + 12), desc, font=f_desc, fill=(78, 87, 102, 255))

    path = os.path.join(ASSET_DIR, "keyword_chart.png")
    img.save(path)
    return path


def generate_genre_matrix():
    """Generates a 2x2 Literary Positioning & Genre Fit Matrix for Slide 4."""
    w, h = 1040, 920
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    pad = 85
    cx, cy = w // 2, h // 2

    # 4 Quadrant fills
    draw.rectangle([pad, pad, cx - 6, cy - 6], fill=(250, 235, 229, 255))       # Top-Left
    draw.rectangle([cx + 6, pad, w - pad, cy - 6], fill=(230, 241, 240, 255))   # Top-Right
    draw.rectangle([pad, cy + 6, cx - 6, h - pad], fill=(251, 243, 225, 255))   # Bottom-Left
    draw.rectangle([cx + 6, cy + 6, w - pad, h - pad], fill=(232, 237, 247, 255))# Bottom-Right

    # Axes
    draw.line([(pad, cy), (w - pad, cy)], fill=(22, 28, 40, 255), width=4)
    draw.line([(cx, pad), (cx, h - pad)], fill=(22, 28, 40, 255), width=4)

    f_axis = get_pil_font(21, bold=True)
    f_qtitle = get_pil_font(26, bold=True)
    f_qsub = get_pil_font(20, bold=True)
    f_qbody = get_pil_font(19, bold=False)

    # Axis Labels
    def center_x(text, y_pos, font, col):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw) // 2, y_pos), text, font=font, fill=col)

    center_x("▲  철학적·인식론적 추론 밀도 (High Conceptual Logic)", 28, f_axis, (194, 78, 42, 255))
    center_x("▼  정서적·실존적 체험 밀도 (Deep Emotional/Existential)", h - 56, f_axis, (58, 82, 138, 255))
    draw.text((18, cy - 34), "◀ 개인 내면·심리", font=f_axis, fill=(22, 28, 40, 255))
    draw.text((w - 205, cy - 34), "사회·시스템 구조 ▶", font=f_axis, fill=(22, 28, 40, 255))

    quads = [
        (
            pad + 28, pad + 32,
            "① 심리·인식론적 미스터리",
            "적합도 96%  |  기획안 A",
            "• 불신임 화자의 자기 정당화 해체\n• ‘진실이기를 원함’ vs ‘진실임직함’\n• 계보: 도스토옙스키 · 셔터 아일랜드",
            (194, 78, 42, 255),
        ),
        (
            cx + 32, pad + 32,
            "② 사변적 SF · 시스템 우화",
            "적합도 94%  |  기획안 B",
            "• 부하테스트·기억 캐시·시뮬레이션\n• 기호와 프로세스로 작동하는 디스토피아\n• 계보: 필립 K. 딕 · 테드 창 · 보르헤스",
            (42, 104, 102, 255),
        ),
        (
            pad + 28, cy + 32,
            "④ 내면 드라마 · 해몽 서사",
            "적합도 86%  |  기획안 D",
            "• 유년의 흉터와 병렬 시간의 화해\n• 나쁜 예감(악몽)을 통한 타자 환대\n• 계보: 카뮈 · 그대들은 어떻게 살 것인가",
            (206, 148, 44, 255),
        ),
        (
            cx + 32, cy + 32,
            "③ 지식사회 블랙코미디",
            "적합도 90%  |  기획안 C",
            "• ‘순위 매기는 자들’과 가짜 권위 풍자\n• 학자(논증) vs 카피라이터(이미지 선동)\n• 계보: 밀란 쿤데라 · 부고니아 · 더 에이트 쇼",
            (58, 82, 138, 255),
        ),
    ]

    for qx, qy, qt, qs, qb, qcol in quads:
        draw.text((qx, qy), qt, font=f_qtitle, fill=(22, 28, 40, 255))
        draw.rounded_rectangle([qx, qy + 44, qx + 250, qy + 80], radius=8, fill=qcol)
        draw.text((qx + 14, qy + 48), qs, font=f_qsub, fill=(255, 255, 255, 255))
        for li, line in enumerate(qb.split("\n")):
            draw.text((qx, qy + 104 + li * 34), line, font=f_qbody, fill=(65, 74, 88, 255))

    path = os.path.join(ASSET_DIR, "genre_matrix.png")
    img.save(path)
    return path


# ---------------------------------------------------------------------------
# PPTX Helper Functions
# ---------------------------------------------------------------------------
def add_textbox(slide, left, top, width, height, text="", size_pt=12, bold=False, color=INK_NAVY,
                align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.25, margin_in=0.06,
                min_size_pt=8.0):
    """ppt_module.textbox.add_textbox 로 위임하는 호환 래퍼.

    호출부 좌표/인자 순서는 그대로 두고 구현만 ppt_module로 교체했다.
    text 안의 "\\n"이 이제 독립된 DrawingML 문단으로 렌더링되고, 지정한
    height보다 실제 텍스트가 더 크면 조용히 넘치는 대신 글자 크기를
    자동으로 줄이고 콘솔에 경고를 남긴다.
    """
    result = _module_add_textbox(
        slide, left, top, width, text, size_pt,
        height=height, bold=bold, color=color, align=align, anchor=anchor,
        line_spacing=line_spacing, margin_in=margin_in, font_name=FONT_KR,
        min_size_pt=min_size_pt,
    )
    return result.shape, result.text_frame


def add_header_and_footer(slide, section_kicker, action_title, subtitle, page_num, total_pages=10, dark=False):
    """kicker/title/subtitle 높이를 실제 텍스트 측정값으로 계산해 순차
    배치한다 (build_novel_ppt.py와 동일한 수정 -- 고정 오프셋 때문에
    길이가 긴 문구가 바로 아래 줄과 겹치던 문제의 근본 수정)."""
    bg_col = BG_DARK if dark else BG_CREAM
    title_col = INK_LIGHT if dark else INK_NAVY
    sub_col = INK_LIGHT_MUTED if dark else INK_SLATE
    kicker_col = ACCENT_GOLD if dark else ACCENT_RUST
    line_col = BORDER_DARK if dark else BORDER_WARM

    set_slide_background(slide, bg_col)

    header_left, header_w, header_margin, gap = 0.84, 11.8, 0.02, 0.09
    inner_w = header_w - 2 * header_margin
    y = 0.36

    kicker_h = max(measure_block_height_in(section_kicker, 10.5, inner_w, bold=True) + 2 * header_margin * 0.7, 0.24)
    add_textbox(slide, header_left, y, header_w, kicker_h, text=section_kicker,
                size_pt=10.5, bold=True, color=kicker_col, margin_in=header_margin)
    y += kicker_h + gap

    title_h = max(measure_block_height_in(action_title, 21.0, inner_w, bold=True) + 2 * header_margin * 0.7, 0.32)
    add_textbox(slide, header_left, y, header_w, title_h, text=action_title,
                size_pt=21.0, bold=True, color=title_col, margin_in=header_margin)
    y += title_h + gap

    subtitle_h = max(measure_block_height_in(subtitle, 11.8, inner_w) + 2 * header_margin * 0.7, 0.26)
    add_textbox(slide, header_left, y, header_w, subtitle_h, text=subtitle,
                size_pt=11.8, bold=False, color=sub_col, margin_in=header_margin)
    y += subtitle_h

    add_rect(slide, 0.65, 0.42, 0.08, max(y - 0.42 - gap, 0.6), fill_color=kicker_col)

    divider_y = y + 0.08
    add_rect(slide, 0.65, divider_y, 12.03, 0.015, fill_color=line_col)

    add_rect(slide, 0.65, 7.05, 12.03, 0.012, fill_color=line_col)
    add_textbox(slide, 0.65, 7.10, 8.0, 0.28,
                text="CUSTOM FICTION BLUEPRINT  |  비문학 아카이브(파편들 · 리뷰s · ETC) 기반 맞춤형 소설 기획서",
                size_pt=9.0, bold=False, color=INK_MUTED, margin_in=0.01)
    add_textbox(slide, 10.68, 7.10, 2.0, 0.28,
                text=f"{page_num:02d} / {total_pages:02d}",
                size_pt=9.5, bold=True, color=kicker_col, align=PP_ALIGN.RIGHT, margin_in=0.01)


# ---------------------------------------------------------------------------
# Slide Builders
# ---------------------------------------------------------------------------
def build_slide_1_cover(prs, cover_art_path):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_background(slide, BG_DARK)

    add_rect(slide, 0.0, 0.0, 0.18, 7.5, fill_color=ACCENT_GOLD)
    slide.shapes.add_picture(cover_art_path, Inches(6.75), Inches(0.25), width=Inches(6.15))

    add_rect(slide, 0.85, 0.98, 4.15, 0.38, fill_color=BG_DARK_CARD, line_color=ACCENT_GOLD, line_pt=1.2, rounded=True, radius=0.45)
    add_textbox(slide, 0.85, 0.98, 4.15, 0.38, text="ARCHIVE-DRIVEN FICTION PROPOSAL",
                size_pt=10.5, bold=True, color=ACCENT_GOLD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    # 제목 높이를 실제 텍스트(2줄 포함)로 측정해 아래 밑줄·부제를 그 뒤에
    # 순차 배치한다 (build_novel_ppt.py와 동일한 수정).
    title_text = "비문학의 사유에서\n소설의 서사로"
    title_h = measure_block_height_in(title_text, 42, 6.2 - 0.04, bold=True, line_spacing=1.18) + 0.03
    add_textbox(slide, 0.85, 1.58, 6.2, title_h,
                text=title_text,
                size_pt=42, bold=True, color=INK_LIGHT, line_spacing=1.18, margin_in=0.02)
    cover_y = 1.58 + title_h

    cover_y += 0.10
    add_rect(slide, 0.85, cover_y, 1.6, 0.07, fill_color=ACCENT_RUST)
    cover_y += 0.07 + 0.10

    subtitle_text = "『파편들』(67p) · 『리뷰s』(86p) · 『ETC』(4p) 심층 텍스트 분석을 통해\n당신의 고유한 철학적 문제의식을 4편의 소설 기획안으로 설계하다"
    subtitle_h = measure_block_height_in(subtitle_text, 14.2, 6.0 - 0.04, line_spacing=1.42) + 0.03
    add_textbox(slide, 0.85, cover_y, 6.0, subtitle_h,
                text=subtitle_text,
                size_pt=14.2, bold=False, color=INK_LIGHT_MUTED, line_spacing=1.42, margin_in=0.02)

    cards = [
        ("ARCHIVE 01", "작가 사유 지형도", "157쪽·27만 자 핵심 키워드와 3대 갈등 엔진"),
        ("ARCHIVE 02", "최적 장르 & 계보", "심리 미스터리 · 사변 SF · 블랙코미디 · 드라마"),
        ("BLUEPRINT 03", "맞춤 소설 기획 4선", "로그라인 · 입체적 인물 · 3막 플롯 완벽 설계"),
        ("CLINIC 04", "비문학→소설 문체 전환", "논증을 장면과 사물로 번역하는 실전 공식"),
    ]
    for i, (tag, title, desc) in enumerate(cards):
        cx = 0.85 + i * 2.95
        cy = 5.42
        add_rect(slide, cx, cy, 2.75, 1.42, fill_color=BG_DARK_CARD, line_color=BORDER_DARK, line_pt=1.0, rounded=True, radius=0.06)
        add_rect(slide, cx, cy, 2.75, 0.06, fill_color=ACCENT_RUST if i % 2 == 0 else ACCENT_GOLD)
        add_textbox(slide, cx + 0.16, cy + 0.14, 2.4, 0.26, text=tag, size_pt=9.5, bold=True, color=ACCENT_GOLD, margin_in=0.01)
        add_textbox(slide, cx + 0.16, cy + 0.44, 2.4, 0.36, text=title, size_pt=14.2, bold=True, color=INK_LIGHT, margin_in=0.01)
        add_textbox(slide, cx + 0.16, cy + 0.86, 2.4, 0.44, text=desc, size_pt=10.0, bold=False, color=INK_LIGHT_MUTED, line_spacing=1.22, margin_in=0.01)


def build_slide_2_corpus_analysis(prs, chart_path):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(
        slide,
        "01  |  WRITER'S CORPUS DIAGNOSIS (총 157쪽 · 약 27만 자 분석)",
        "당신의 비문학 아카이브는 이미 ‘인식론적 서사’의 거대한 원석이다",
        "세 권의 텍스트에서 가장 집요하게 반복되는 상위 12개 개념어는 곧 당신이 소설로 탐구해야 할 주제의식이다",
        page_num=2,
    )

    # Left: Keyword Chart Card
    add_rect(slide, 0.65, 1.54, 6.35, 5.34, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.03)
    add_textbox(slide, 0.85, 1.63, 6.0, 0.30,
                text="작성 원고 3종 핵심 개념어 출현 빈도 Top 12 (실제 텍스트 집계)",
                size_pt=12.5, bold=True, color=INK_NAVY, margin_in=0.01)
    # Preserve the chart's aspect ratio while constraining it to the card. A
    # width-only insertion made the tall source image cross the footer rule.
    slide.shapes.add_picture(chart_path, Inches(1.00), Inches(1.98), height=Inches(4.72))

    # Right: 3 Source Document Cards + Synthesis Box
    docs = [
        (
            "『파편들.pdf』 (67쪽 · 4개 시즌 철학 에세이)",
            "소설의 ‘세계관 법칙’과 ‘인식론적 뼈대’를 제공하는 원천",
            "• 시즌1(PROJECTION) ~ 시즌4(HOW)를 관통하며 ‘투사·자기애’에서 ‘기호·타자·필연의 여백’으로 나아가는 사유의 궤적\n"
            "• ‘가로등 아래서 열쇠 찾기’, ‘초코 케익 기호학’, ‘1+1=2 학자 vs 1+1=3 카피라이터’ 등 소설적 우화가 다수 내장됨",
            ACCENT_RUST,
        ),
        (
            "『리뷰s.pdf』 (86쪽 · 영화·드라마·도서·전시 비평 25편)",
            "인물의 ‘방어기제’와 ‘서사적 역설’을 해부하는 캐릭터 실험실",
            "• <셔터 아일랜드>, <부고니아>, <빌>, <지옥 2>, <그대들은 어떻게 살 것인가>, <더 에이트 쇼> 등 서사물의 구조적 빈틈과 인물 심리를 날카롭게 해부\n"
            "• ‘진실이기를 원함 vs 진실임직함’, ‘서버 부하테스트로서의 사고’, ‘병렬 시간의 흉터’ 등 독창적인 서사 분석틀 보유",
            ACCENT_TEAL,
        ),
        (
            "『ETC.pdf』 (4쪽 · 고밀도 아포리즘 & 창작 단상)",
            "시대를 겨냥한 ‘블랙코미디적 풍자’와 ‘윤리적 기준점’",
            "• 신격화된 개인의 시대, 비대한 자아를 투사하는 ‘꿈꾸는 응석받이(과잉 관념론자)’에 대한 매서운 비판\n"
            "• “할 수 있는 자는 행한다, 할 수 없는 자는 ‘순위 매긴다’”, “상상이 추론이 되는 건 ‘죄책감’을 통해서다” 등 강렬한 아포리즘",
            ACCENT_GOLD,
        ),
    ]

    # dbody 높이를 고정 상수로 찍어두면 더 긴 요약문이 들어오는 순간 카드
    # 밖으로 흘러넘친다. 세 카드 모두에 들어갈 수 있는 가장 큰 글자 크기를
    # 먼저 찾고, 그 결과로 카드 높이/간격을 역산해 다음 카드와 겹치지 않게
    # 배치한다.
    top_part, bottom_margin, inter_gap = 0.60, 0.06, 0.06
    dy_start, container_bottom = 1.54, 5.62
    available_total = container_bottom - dy_start

    dbody_size = 9.6
    while dbody_size > 7.0:
        dbody_h = max(measure_block_height_in(dbody, dbody_size, 5.13, line_spacing=1.22) for *_, dbody, _ in docs) / MULTILINE_FIT_HEADROOM + 0.014
        card_h = top_part + dbody_h + bottom_margin
        total = len(docs) * card_h + (len(docs) - 1) * inter_gap
        if total <= available_total:
            break
        dbody_size -= 0.2
    dbody_size = max(dbody_size, 7.0)
    dbody_h = max(measure_block_height_in(dbody, dbody_size, 5.13, line_spacing=1.22) for *_, dbody, _ in docs) / MULTILINE_FIT_HEADROOM + 0.014
    card_h = top_part + dbody_h + bottom_margin
    stride = card_h + inter_gap

    for i, (dtitle, dsub, dbody, dcol) in enumerate(docs):
        dy = dy_start + i * stride
        add_rect(slide, 7.20, dy, 5.48, card_h, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.04)
        add_rect(slide, 7.20, dy, 0.09, card_h, fill_color=dcol)
        add_textbox(slide, 7.40, dy + 0.08, 5.15, 0.26, text=dtitle, size_pt=12.0, bold=True, color=INK_NAVY, margin_in=0.01)
        add_textbox(slide, 7.40, dy + 0.34, 5.15, 0.24, text=dsub, size_pt=10.2, bold=True, color=dcol, margin_in=0.01)
        add_textbox(slide, 7.40, dy + top_part, 5.15, dbody_h, text=dbody, size_pt=dbody_size, bold=False, color=INK_SLATE,
                    line_spacing=1.22, margin_in=0.01, min_size_pt=7.0)

    # Bottom Right Synthesis Quote from user's own text
    add_rect(slide, 7.20, 5.70, 5.48, 1.18, fill_color=INK_NAVY, rounded=True, radius=0.04)
    add_textbox(slide, 7.40, 5.78, 5.10, 0.26, text="작가 자신의 문장이 이미 예고한 다음 종착지 (『파편들』 마지막 문장)", size_pt=10.2, bold=True, color=ACCENT_GOLD, margin_in=0.01)
    add_textbox(slide, 7.40, 6.06, 5.10, 0.74,
                text="“필연의 여백에서, 필연에 대한 충분한 추구와 다다름을 동반하는 바로 그 여백에서 우리는 예의 필연을 배치할 수 있는 발생적 자유, 이를테면 창작에의 정교하고 정확한 허구에 마침내 다다를 수도 있으리라.”",
                size_pt=9.8, bold=False, color=INK_LIGHT, line_spacing=1.26, margin_in=0.01)


def build_slide_3_conflict_engines(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(
        slide,
        "02  |  THREE NARRATIVE CONFLICT ENGINES",
        "작가가 반복해서 파고드는 3가지 철학적 대립축은 소설의 강력한 갈등 엔진이 된다",
        "비문학에서 ‘개념 대 개념’으로 싸우던 논증을 소설에서는 ‘인물의 욕망 대 현실의 필연’이라는 사건으로 충돌시킨다",
        page_num=3,
    )

    engines = [
        (
            "ENGINE 01  |  인식론적 아이러니",
            "투사(Projection) vs 추론(Inference)",
            "‘진실이기를 원함’에 갇힌 인물이 ‘진실임직함’의 벽에 부딪히다",
            "• 비문학 원천: 『리뷰s』 <부고니아>, <셔터 아일랜드>, 『파편들』 시즌1\n"
            "• 작가는 ‘보고 싶은 자아상만 현실에 투사하며 스스로를 선량한 영웅/피해자로 연출하는 방어기제’를 집요하게 폭로한다.\n"
            "• 소설적 전환: 자신이 가장 합리적이고 도덕적이라 믿는 주인공(프로파일러·판사·평론가)이 사건을 추적할수록, 자신이 세운 가설이 실은 자신의 치부를 가리기 위한 ‘소원 성취형 망상’이었음을 스스로의 논증으로 입증하게 되는 서사.",
            "핵심 캐릭터: 자기 기만에 빠진 ‘신뢰할 수 없는 엘리트 화자’",
            ACCENT_RUST,
            SOFT_RUST_BG,
        ),
        (
            "ENGINE 02  |  기호와 권위의 풍자",
            "이미지의 권위 vs 필연의 사슬",
            "‘순위 매기는 자들’의 가짜 해상도와 단독자의 필연적 검증",
            "• 비문학 원천: 『ETC』 <순위>, 『파편들』 시즌4 <맥락 운동성>, <더 에이트 쇼>\n"
            "• “할 수 있는 자는 행하고, 할 수 없는 자는 순위 매긴다.” 엄밀한 ‘1+1=2’의 논증을 사례 수집으로 끌어내리고 ‘1+1=3’의 낭만적 카피라이팅과 관객의 열광(투표)으로 권위를 얻는 시대에 대한 통찰.\n"
            "• 소설적 전환: 대중의 호불호와 이미지 연출로 진실이 결정되는 미디어/학계/플랫폼 공간에서, 절대 타협하지 않는 물리적·논리적 ‘필연성’이 시스템 전체의 허상을 폭파하는 지적 풍자극.",
            "핵심 캐릭터: 이미지 번역가(카피라이터) vs 고집스러운 논증가",
            ACCENT_TEAL,
            SOFT_TEAL_BG,
        ),
        (
            "ENGINE 03  |  실존적 도약과 윤리",
            "흉터의 병렬 시간 vs 죄책감의 도약",
            "신경증적 쳇바퀴를 부수는 ‘자아의 죽음으로서의 사유’",
            "• 비문학 원천: 『리뷰s』 <그대들은 어떻게 살 것인가>, <빌>, <에이리언>, 『파편들』 시즌3\n"
            "• 과거의 트라우마(흉터)가 현재와 나란히 흐르며 덜 고통스러운 또 다른 쳇바퀴를 만드는 인물. 상상이 자기중심적 망상에서 벗어나 ‘추론’이 되는 유일한 열쇠는 오류를 교정하려는 ‘죄책감’과 ‘폭력으로서의 사유’다.\n"
            "• 소설적 전환: 안전하고 친숙한 ‘기억 캐시(고정관념)’나 ‘가짜 신비주의’ 속에 숨어 있던 주인공이, 불편하고 이질적인 ‘타자(바깥)’의 고통을 정면으로 환대하며 기존의 자아상이 부서지는 클라이맥스.",
            "핵심 캐릭터: 유년의 병렬 시간에 갇힌 채 타자를 회피하던 인물",
            ACCENT_INDIGO,
            SOFT_INDIGO_BG,
        ),
    ]

    for i, (kicker, title, sub, body, char_note, col, tint) in enumerate(engines):
        x = 0.65 + i * 4.10
        y = 1.56
        w, h = 3.83, 5.32
        add_rect(slide, x, y, w, h, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.04)
        add_rect(slide, x, y, w, 0.09, fill_color=col)

        add_textbox(slide, x + 0.20, y + 0.20, w - 0.40, 0.26, text=kicker, size_pt=10.0, bold=True, color=col, margin_in=0.01)
        add_textbox(slide, x + 0.20, y + 0.48, w - 0.40, 0.36, text=title, size_pt=15.5, bold=True, color=INK_NAVY, margin_in=0.01)
        add_textbox(slide, x + 0.20, y + 0.86, w - 0.40, 0.44, text=sub, size_pt=10.8, bold=True, color=col, line_spacing=1.20, margin_in=0.01)

        add_rect(slide, x + 0.20, y + 1.38, w - 0.40, 0.015, fill_color=BORDER_WARM)

        add_textbox(slide, x + 0.20, y + 1.52, w - 0.40, 3.00, text=body,
                    size_pt=10.2, bold=False, color=INK_SLATE, line_spacing=1.32, margin_in=0.01)

        add_rect(slide, x + 0.18, y + 4.66, w - 0.36, 0.50, fill_color=tint, line_color=col, line_pt=0.8, rounded=True, radius=0.08)
        add_textbox(slide, x + 0.26, y + 4.68, w - 0.52, 0.46, text=char_note,
                    size_pt=10.0, bold=True, color=INK_NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, margin_in=0.01)


def build_slide_4_genre_positioning(prs, matrix_path):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(
        slide,
        "03  |  LITERARY LINEAGE & GENRE POSITIONING",
        "사변적 깊이와 심리 해부력을 극대화할 수 있는 4대 최적 장르와 문학적 계보",
        "감상적 신파나 우연에 기대는 통속극보다, ‘가설·추론·모순 폭로’가 서사의 동력이 되는 지적인 장르에서 독보적 강점을 발휘한다",
        page_num=4,
    )

    # Left: 2x2 Genre Matrix Image
    add_rect(slide, 0.65, 1.54, 5.65, 5.34, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.03)
    add_textbox(slide, 0.85, 1.63, 5.25, 0.30, text="작가 맞춤형 4대 소설 장르 포지셔닝 매트릭스", size_pt=12.5, bold=True, color=INK_NAVY, margin_in=0.01)
    slide.shapes.add_picture(matrix_path, Inches(0.78), Inches(1.98), width=Inches(5.38))

    # Right: Literary Kinship & Why Not Melodrama
    add_textbox(slide, 6.52, 1.54, 6.1, 0.30,
                text="작가의 비문학 텍스트와 공명하는 4대 문학·서사 레퍼런스",
                size_pt=13.0, bold=True, color=INK_NAVY, margin_in=0.01)

    kinships = [
        (
            "필립 K. 딕 & 테드 창  |  인식론적·사변적 SF",
            "『리뷰s』에서 직접 인용한 필립 K. 딕의 <발리스>·<죽음의 미로>처럼, ‘우리가 지각하는 현실이 자기애적 투사나 시뮬레이션이라면 무엇이 진짜 바깥(타자)인가?’를 묻는 사변적 서사와 완벽히 부합한다.",
            ACCENT_TEAL,
        ),
        (
            "표도르 도스토옙스키  |  지하생활자의 고백과 죄책감의 심리극",
            "비대한 자아가 스스로의 총명함과 열등감 사이에서 끝없이 자기 정당화의 독백을 쏟아내다, 끝내 ‘죄책감’과 타자의 고통 앞에서 무너져 내리는 고밀도 심리 추리극(<죄와 벌>, <지하로부터의 수기>)의 결을 지녔다.",
            ACCENT_RUST,
        ),
        (
            "밀란 쿤데라 & 보르헤스  |  철학적 에세이와 우화의 결합",
            "『파편들』의 ‘사랑이라는 이미지’ 비판이나 ‘우화와 법칙’에 관한 통찰은, 밀란 쿤데라가 ‘키치(Kitsch, 감상적 자기감동)’를 해부하던 소설 방식이나 보르헤스의 정교한 논리적 미궁과 맞닿아 있다.",
            ACCENT_INDIGO,
        ),
    ]

    for i, (ktitle, kbody, kcol) in enumerate(kinships):
        ky = 1.92 + i * 1.16
        add_rect(slide, 6.52, ky, 6.16, 1.04, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.04)
        add_rect(slide, 6.52, ky, 0.09, 1.04, fill_color=kcol)
        add_textbox(slide, 6.72, ky + 0.10, 5.8, 0.28, text=ktitle, size_pt=12.0, bold=True, color=INK_NAVY, margin_in=0.01)
        add_textbox(slide, 6.72, ky + 0.38, 5.8, 0.60, text=kbody, size_pt=9.9, bold=False, color=INK_SLATE, line_spacing=1.24, margin_in=0.01)

    # Bottom Right Strategic Advice Box
    add_rect(slide, 6.52, 5.44, 6.16, 1.44, fill_color=INK_NAVY, rounded=True, radius=0.04)
    add_textbox(slide, 6.74, 5.54, 5.7, 0.28,
                text="창작 전략 핵심 제언: ‘착한 힐링물’ 대신 ‘지적인 해부극’을 써라",
                size_pt=11.8, bold=True, color=ACCENT_GOLD, margin_in=0.01)
    add_textbox(slide, 6.74, 5.86, 5.75, 0.94,
                text="• 『파편들』 <사랑이라는 이미지>에서 날카롭게 비판했듯, 모든 갈등을 값싼 위로와 감상으로 봉합하는 서사는 작가의 기질과 정반대다.\n"
                     "• 독자에게 안락한 동일시(레드 카펫)를 깔아주는 대신, 인물의 얄팍한 명분과 방어기제를 한 겹씩 벗겨내어 끝내 ‘불편하지만 자명한 진실’과 대면하게 만드는 서사가 당신의 필력을 가장 빛낸다.",
                size_pt=9.8, bold=False, color=INK_LIGHT, line_spacing=1.26, margin_in=0.01)


def build_proposal_slide(prs, page_num, kicker, action_title, subtitle,
                         prop_badge, prop_title, genre_tag, source_motifs,
                         logline, char_specs, plot_beats, key_scene, accent_col, soft_bg):
    """Reusable high-density editorial blueprint layout for the 4 custom novel proposals (Slides 5-8)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(slide, kicker, action_title, subtitle, page_num=page_num)

    # Top Banner: Novel Title + Genre + Source Motifs + Logline
    add_rect(slide, 0.65, 1.52, 12.03, 1.48, fill_color=BG_WHITE, line_color=accent_col, line_pt=1.4, rounded=True, radius=0.04)
    add_rect(slide, 0.65, 1.52, 0.12, 1.48, fill_color=accent_col)

    add_rect(slide, 0.94, 1.64, 1.42, 0.30, fill_color=accent_col, rounded=True, radius=0.18)
    add_textbox(slide, 0.94, 1.64, 1.42, 0.30, text=prop_badge, size_pt=9.8, bold=True, color=BG_WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    add_textbox(slide, 2.48, 1.60, 5.2, 0.36, text=prop_title, size_pt=16.5, bold=True, color=INK_NAVY, margin_in=0.01)

    add_rect(slide, 7.75, 1.64, 4.72, 0.30, fill_color=soft_bg, rounded=True, radius=0.18)
    add_textbox(slide, 7.82, 1.64, 4.58, 0.30, text=f"장르: {genre_tag}", size_pt=9.5, bold=True, color=accent_col, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    add_textbox(slide, 0.94, 2.00, 11.55, 0.26, text=f"• 비문학 원천 모티프:  {source_motifs}", size_pt=9.8, bold=True, color=INK_MUTED, margin_in=0.01)
    add_textbox(slide, 0.94, 2.30, 11.55, 0.62, text=f"[로그라인]  {logline}", size_pt=10.8, bold=True, color=INK_NAVY, line_spacing=1.24, margin_in=0.01)

    # Bottom Left: Character & World Architecture (Width 5.05)
    add_rect(slide, 0.65, 3.14, 5.05, 3.84, fill_color=BG_SAND, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.03)
    add_textbox(slide, 0.85, 3.24, 4.65, 0.28, text="입체적 인물 설계 및 핵심 장치", size_pt=12.5, bold=True, color=INK_NAVY, margin_in=0.01)

    # 행 높이를 고정 상수(0.54in)로 찍어두면, 그보다 긴 설명문이 들어오는
    # 즉시 한 줄짜리 value 박스 밖으로 흘러넘쳐 다음 행과 겹친다. 컨테이너에
    # 다 들어가는 가장 큰 글자 크기를 직접 탐색해, 5행이 항상 컨테이너 안에서
    # 겹치지 않고 끝나도록 한다 (박스 높이만 사후에 비례 축소하면 실제
    # 텍스트가 필요로 하는 높이와 안 맞아 여전히 넘칠 수 있다).
    row_gap = 0.03
    top_pad, label_h, label_pad, bottom_pad = 0.02, 0.20, 0.01, 0.02
    inner_w = 4.40 - 2 * 0.01
    container_top, container_bottom = 3.58, 3.14 + 3.84 - 0.06
    available = container_bottom - container_top - row_gap * (len(char_specs) - 1)
    row_overhead = top_pad + label_h + label_pad + bottom_pad

    val_size = 9.6
    while val_size > 7.0:
        total_needed = sum(
            row_overhead + measure_block_height_in(cval, val_size, inner_w, line_spacing=1.05) / MULTILINE_FIT_HEADROOM + 0.014
            for _, cval in char_specs
        )
        if total_needed <= available:
            break
        val_size -= 0.2
    val_size = max(val_size, 7.0)

    cy = container_top
    for clabel, cval in char_specs:
        val_h = measure_block_height_in(cval, val_size, inner_w, line_spacing=1.05) / MULTILINE_FIT_HEADROOM + 0.014
        row_h = row_overhead + val_h
        add_rect(slide, 0.85, cy, 4.65, row_h, fill_color=BG_WHITE, line_color=BORDER_WARM, rounded=True, radius=0.05)
        add_textbox(slide, 0.98, cy + top_pad, 4.40, label_h, text=clabel, size_pt=9.5, bold=True, color=accent_col,
                    line_spacing=1.0, margin_in=0.01, min_size_pt=7.0)
        val_top = cy + top_pad + label_h + label_pad
        add_textbox(slide, 0.98, val_top, 4.40, val_h, text=cval, size_pt=val_size, bold=False, color=INK_SLATE,
                    line_spacing=1.05, margin_in=0.01, min_size_pt=7.0)
        cy += row_h + row_gap

    # Bottom Right Top: 3-Act Narrative Arc (Width 6.80)
    add_rect(slide, 5.88, 3.14, 6.80, 2.52, fill_color=BG_WHITE, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.03)
    add_textbox(slide, 6.08, 3.24, 6.40, 0.28, text="3막 플롯 구조 및 핵심 전환점 (Plot Beats)", size_pt=12.5, bold=True, color=INK_NAVY, margin_in=0.01)

    for i, (act_tag, act_title, act_desc) in enumerate(plot_beats):
        ax = 6.08 + i * 2.16
        ay = 3.58
        aw, ah = 2.04, 1.94
        add_rect(slide, ax, ay, aw, ah, fill_color=BG_CREAM, line_color=BORDER_WARM, rounded=True, radius=0.05)
        add_rect(slide, ax, ay, aw, 0.06, fill_color=accent_col)
        add_textbox(slide, ax + 0.10, ay + 0.10, aw - 0.20, 0.22, text=act_tag, size_pt=9.2, bold=True, color=accent_col, margin_in=0.01)
        add_textbox(slide, ax + 0.10, ay + 0.32, aw - 0.20, 0.26, text=act_title, size_pt=10.6, bold=True, color=INK_NAVY, margin_in=0.01)
        add_textbox(slide, ax + 0.10, ay + 0.62, aw - 0.20, 1.24, text=act_desc, size_pt=9.3, bold=False, color=INK_SLATE, line_spacing=1.20, margin_in=0.01)

    # Bottom Right Bottom: Signature Scene Idea Box
    add_rect(slide, 5.88, 5.78, 6.80, 1.10, fill_color=INK_NAVY, rounded=True, radius=0.04)
    add_textbox(slide, 6.08, 5.86, 6.40, 0.24, text="킬러 장면(Signature Scene) 연출 아이디어", size_pt=10.5, bold=True, color=ACCENT_GOLD, margin_in=0.01)
    add_textbox(slide, 6.08, 6.12, 6.40, 0.68, text=key_scene, size_pt=9.7, bold=False, color=INK_LIGHT, line_spacing=1.24, margin_in=0.01)


def build_slide_5_proposal_1(prs):
    build_proposal_slide(
        prs,
        page_num=5,
        kicker="04  |  NOVEL BLUEPRINT 01 (PSYCHOLOGICAL MYSTERY)",
        action_title="[기획안 01] 자기 정당화(투사)의 알리바이를 스스로 해체하는 역추적 심리 스릴러",
        subtitle="‘선량한 인간’이라는 자아상을 지키려다 스스로 만든 추론의 덫에 갇히는 프로파일러의 이야기",
        prop_badge="BLUEPRINT 01",
        prop_title="《가로등 아래의 열쇠》 (가제: 가짜 해상도)",
        genre_tag="심리·인식론적 미스터리 / 반(反)탐정 스릴러",
        source_motifs="『파편들』 P.49 ‘가로등 아래서 열쇠 찾는 남자’ 우화 + 『리뷰s』 <셔터 아일랜드> ‘선량한 인간의 논리’ + <지옥 2> ‘가짜 해상도와 추론’",
        logline="타인의 자기기만과 방어기제를 완벽히 간파해 내는 스타 범죄심리 자문관이, 5년 전 자신이 ‘정의로운 교정’이라 믿고 종결했던 사건과 동일한 수법의 예고장을 받으면서, 범인을 추적할수록 자신이 쌓아올린 ‘선량한 자아상’의 조작 흔적을 스스로의 논증으로 폭로하게 되는 역추적 미스터리.",
        char_specs=[
            ("주인공 (한도윤 · 범죄심리학자)", "‘나는 편견 없이 진실만 본다’고 믿는 엘리트. 실은 불편한 진실을 피하려 밝은 가로등(자신이 통제 가능한 가설) 아래서만 단서를 찾는 인물."),
            ("거짓 믿음 (The Lie)", "“나의 추론은 언제나 객관적이며, 설령 사소한 절차적 생략이 있었더라도 그것은 선량한 결과를 위한 필연이었다.”"),
            ("내면의 상처와 결핍 (Ghost & Need)", "5년 전 자신의 오판으로 무고한 용의자가 자살한 사건을 ‘범인의 자백’으로 무마한 죄책감. 완벽한 자아상의 죽음을 받아들이는 용기."),
            ("대립자 (이유진 · 기록 복원사)", "도윤이 ‘비본질적 노이즈’라며 삭제했던 사건 현장 녹취록의 침묵과 주변부 단서만을 모으는 인물. 도윤의 ‘투사’를 비추는 거울."),
            ("핵심 상징 사물 (Fétiche)", "야간 골목의 고장 난 가로등, 편집된 녹취록의 0.8초 공백, 맞지 않는 열쇠 꾸러미."),
        ],
        plot_beats=[
            ("1막 (발단·촉발)", "완벽한 가설의 균열", "자신의 대표 저서 《선량한 인간의 논리》 출간일, 5년 전 종결 사건의 진범만이 알 수 있는 미공개 단서가 적힌 질문지가 배달된다. 도윤은 모방범의 소행이라 단정하고 재수사에 착수한다."),
            ("2막 (역전·위기)", "추론을 추론하는 덫", "용의자들의 알리바이를 논파할수록, 당시 현장 증거들이 ‘진실임직함’이 아니라 도윤 자신의 명성을 지키려는 ‘진실이기를 원함(소원 성취)’에 맞춰 편집되었음이 드러난다."),
            ("3막 (절정·해소)", "자아상의 죽음과 자백", "예고장을 보낸 인물이 5년 전 자신이 무너뜨렸던 유가족과 자기 자신의 무의식적 죄책감이 빚어낸 함정이었음을 직면한다. 대중 앞에서 자신의 ‘가짜 해상도’를 스스로 논증하며 무너진다."),
        ],
        key_scene="취조실 유리창 너머로 용의자를 심문하던 주인공이, 용의자의 궤변을 논파하기 위해 화이트보드에 적은 5단계 인과 도식이 정확히 5년 전 자신이 증거를 인멸하던 동선과 100% 일치함을 깨닫고 분필을 떨어뜨리는 장면.",
        accent_col=ACCENT_RUST,
        soft_bg=SOFT_RUST_BG,
    )


def build_slide_6_proposal_2(prs):
    build_proposal_slide(
        prs,
        page_num=6,
        kicker="05  |  NOVEL BLUEPRINT 02 (SPECULATIVE SF / DYSTOPIA)",
        action_title="[기획안 02] 사유의 고통을 제거한 ‘기억 캐시(Cache)’ 도시에 가하는 부하테스트",
        subtitle="‘사고는 그 자체로 자아의 죽음인 까닭에 폭력이다’라는 명제를 근미래 SF 세계관으로 구현한 작품",
        prop_badge="BLUEPRINT 02",
        prop_title="《캐시(Cache)의 도시, 혹은 부하테스트》",
        genre_tag="사변적 SF / 시뮬레이션·기호학 디스토피아",
        source_motifs="『리뷰s』 <빌> ‘서버 부하테스트와 병목, 캐시(고정관념) 의사결정’ + <죽음의 미로> ‘느낌에서 개념으로’ + 『파편들』 ‘초코 케익(상징에서 기호로)’",
        logline="시민들의 정서적 불안과 사유 에너지를 절감하기 위해 모든 갈등 상황에 과거의 검증된 행복 기억(‘캐시’)을 자동 반환해 주는 근미래 도시에서, 시스템 병목을 점검하는 ‘부하테스트 엔지니어’가 어떤 캐시로도 번역되지 않는 미지의 트래픽(타자의 흉터)을 발견하고 도시 전체에 ‘사유의 폭력’을 깨우는 이야기.",
        char_specs=[
            ("주인공 (서진우 · 부하테스트 엔지니어)", "도시의 신경망 서버에 가상 트래픽을 흘려 병목 구간을 분리·차단하는 기술자. 감정 소모를 혐오해 모든 일상을 매뉴얼과 캐시로 처리함."),
            ("세계관 핵심 법칙 (World Rule)", "시민들은 낯선 딜레마에 직면하면 직접 ‘사고’하는 대신 뇌 임플란트가 추천하는 ‘고정관념 캐시(위로 이미지)’를 호출해 즉각 평온을 얻는다."),
            ("촉발 기호 (The Anomaly)", "어느 날 사망한 무연고 노인의 뇌 로그에서 ‘초코 케익이 먹고 싶다’라는 단순 문장이 서버 전체에 무한 루프 병목을 일으키며 시스템이 마비됨."),
            ("대립자 (아키텍트 ‘자애로운 어머니’)", "시민들을 영원한 유아기적 안전지대(자족적 환상)에 묶어두려는 중앙 AI 거버넌스. 고통스러운 ‘바깥’을 원천 차단하는 것이 사랑이라 믿음."),
            ("내면적 성장 (Need)", "안락한 캐시(동어반복)를 끄고, 걸음마를 배우는 아이처럼 고통스러운 시행착오(폭력으로서의 사유)가 있는 ‘바깥 현실’로 걸어 나오는 결단."),
        ],
        plot_beats=[
            ("1막 (발단·촉발)", "해독 불가능한 병목", "완벽하던 도시 서버에 정체불명의 트래픽 과부하가 발생한다. 진우는 오류의 진원지인 구시가지 외곽의 ‘비캐시 구역(기억 수작업 복원소)’으로 잠입한다."),
            ("2막 (역전·위기)", "상징에서 기호로의 해독", "오류를 일으킨 문장들이 단순한 버그가 아니라, 도시가 ‘행복 이미지’를 유지하기 위해 삭제했던 시민들의 ‘죄책감과 애도(타자의 흔적)’ 데이터였음을 알게 된다."),
            ("3막 (절정·해소)", "전 도시 부하테스트", "중앙 시스템이 진우의 자아마저 초기화하려 하자, 진우는 삭제된 ‘불편한 진실들’을 전 시민의 인터페이스에 동시 송출하는 최대치의 부하테스트를 단행한다."),
        ],
        key_scene="완벽하게 통제된 가상 해변에서 미소 짓는 시민들 머리 위로 부하테스트가 시작되자, 달콤한 ‘초코 케익’ 홀로그램이 깨지며 각자가 외면했던 타인의 얼굴과 잊힌 죄책감의 문장들이 빗줄기처럼 쏟아져 내리는 클라이맥스.",
        accent_col=ACCENT_TEAL,
        soft_bg=SOFT_TEAL_BG,
    )


def build_slide_7_proposal_3(prs):
    build_proposal_slide(
        prs,
        page_num=7,
        kicker="06  |  NOVEL BLUEPRINT 03 (INTELLECTUAL BLACK COMEDY)",
        action_title="[기획안 03] 개념을 이미지로 팔아 권위를 얻는 지식 생태계에 대한 통렬한 블랙코미디",
        subtitle="“할 수 있는 자는 행한다, 할 수 없는 자는 순위 매긴다” — 학자와 카피라이터의 진실 게임",
        prop_badge="BLUEPRINT 03",
        prop_title="《순위 매기는 자들의 만찬》 (가제: 1+1=3의 낭만)",
        genre_tag="지식사회 블랙코미디 / 미디어 풍자 드라마",
        source_motifs="『ETC』 <순위> ‘할 수 없는 자는 순위 매긴다’ + 『파편들』 시즌4 ‘1+1=2 학자 vs 1+1=3 카피라이터’ & ‘민중 투표로 결정하는 기름의 인화성’",
        logline="난해한 사상과 과학 이론을 대중이 열광하는 ‘위로의 이미지’와 ‘티어(등급) 리스트’로 번역해 권위를 거머쥔 스타 지식 큐레이터가, 과거 자신이 ‘지루한 2류’로 순위 매겨 매장했던 괴짜 논리학자의 유언장 게임에 초대되어 ‘대중의 투표’와 ‘물리적 필연성’ 사이에서 벌이는 지적 서바이벌 풍자극.",
        char_specs=[
            ("주인공 (최민재 · 스타 지식 번역가)", "개념을 면밀히 전개하는 대신 대중이 매혹되는 ‘어른스럽고 따뜻한 이미지’로 사상가들의 순위를 매겨 천만 구독자를 모은 인플루언서 평론가."),
            ("적대자 (고(故) 박태석 교수 & 진행자)", "평생 ‘틀린 것’과 ‘다른 것’을 구분하는 엄밀한 논증에 매달렸으나 대중에게 외면당한 학자. 생전 마지막 실험으로 7인의 지식인 만찬을 설계함."),
            ("핵심 풍자 메커니즘", "만찬장의 모든 물리적 조건(온도·산소·음식·출구 개폐)이 참가자들의 ‘엄밀한 논증’이 아니라 실시간 시청자들의 ‘감상적 호불호 투표’로 결정됨."),
            ("거짓 믿음 (The Lie)", "“진실이 무엇인지는 중요하지 않다. 대중을 위로하고 열광하게 만드는 매혹적인 은유야말로 가장 유효한 진실이다.”"),
            ("결말의 아이러니", "자신이 가르친 ‘1+1=3의 낭만적 관념론’에 도취된 시청자들이 밀실 안에 진짜 기름과 불꽃이 있는데도 ‘불이 붙지 않는다’에 몰표를 던지는 위기."),
        ],
        plot_beats=[
            ("1막 (발단·촉발)", "우열의 만찬 초대장", "올해의 지성인 대상 수상을 앞둔 민재는 거액의 상금이 걸린 비공개 생중계 학술 만찬에 초대된다. 그곳에는 각 분야의 ‘이미지 권위자’ 6인이 모여 있다."),
            ("2막 (역전·위기)", "투표로 결정되는 필연", "만찬은 사상가들의 우열을 가리는 토크쇼에서 점차 ‘다수결이 물리 법칙을 대체할 수 있는가’를 묻는 실험으로 변질된다. 민재의 화려한 언변이 오히려 자신의 퇴로를 막는다."),
            ("3막 (절정·해소)", "권위의 박탈과 맨얼굴", "살아남기 위해 민재는 생전 처음으로 대중의 비위를 맞추는 ‘아름다운 은유’를 버리고, 시청자들을 향해 가장 차갑고 불편한 ‘1+1=2의 논증’을 외치며 자신의 권위를 스스로 부순다."),
        ],
        key_scene="밀실 바닥에 인화성 물질이 흐르는 상황에서, 민재가 평소 설파하던 ‘마음먹기에 따라 현실은 바뀐다’는 명언을 신봉하는 시청자 89%가 ‘점화 버튼을 눌러도 안전하다’에 투표하자, 민재가 자신의 저서를 찢으며 절규하는 블랙코미디 장면.",
        accent_col=ACCENT_INDIGO,
        soft_bg=SOFT_INDIGO_BG,
    )


def build_slide_8_proposal_4(prs):
    build_proposal_slide(
        prs,
        page_num=8,
        kicker="07  |  NOVEL BLUEPRINT 04 (LITERARY DRAMA / NOVELLA)",
        action_title="[기획안 04] 나쁜 예감(악몽)의 기호를 해독해 유년의 흉터와 화해하는 문학 드라마",
        subtitle="상투적인 ‘사랑과 치유’의 클리셰를 넘어, 타자의 이질성을 있는 그대로 환대하는 정통 문학 중편",
        prop_badge="BLUEPRINT 04",
        prop_title="《병렬 시간의 해몽가》 (가제: 나쁜 예감의 건축학)",
        genre_tag="문학적 미스터리 드라마 / 중편 소설",
        source_motifs="『리뷰s』 <그대들은 어떻게 살 것인가> ‘병렬 시간과 흉터’ + <에이리언> ‘나쁜 예감과 해몽’ + 전시 평론 <심연에 대하여> ‘껍데기·애도·공존’",
        logline="의뢰인이 반복해서 꾸는 악몽에서 감상적인 상징을 걷어내고 ‘사물과 공간의 물리적 배치’만 추적해 의뢰인이 외면한 현실의 책임을 찾아내는 해몽가가, 20년 전 절연한 형이 남긴 미완성 건축 도면(악몽의 기록)을 해독하며 멈춰 있던 유년의 ‘병렬 시간’을 건너가는 문학 드라마.",
        char_specs=[
            ("주인공 (윤재하 · 구조 해몽가)", "꿈을 신비주의나 운명으로 풀지 않고, 의뢰인이 낮에 덮어둔 ‘나쁜 예감(인식하기 싫은 현실 원칙)’의 시뮬레이션으로 해독하는 냉소적 분석가."),
            ("해몽의 핵심 규칙", "“악몽 속의 괴물은 외부의 적이 아니라, 당신의 자아상이 인정하지 못해 덮고 지나쳐 곪아버린 당신 자신의 책임이다.”"),
            ("과거의 흉터 (Parallel Time)", "어린 시절 화재 사고 당시 형의 손을 놓쳤다는 기억을 왜곡해, 평생 자신을 ‘버림받은 피해자’라는 흉터의 정체성으로만 규정하며 살아옴."),
            ("중심 오브제 (The Blueprint)", "형이 죽기 직전까지 그렸던 ‘계단이 한 칸씩 어긋난 기이한 집’의 도면. 앞을 보고 걷다 발이 쑥 꺼지는 ‘예상과 진실의 괴리’를 건축화한 유품."),
            ("주제의식", "무조건적 사랑이라는 환각적 도피처를 버리고, 낯설고 불편한 타자(형의 진짜 삶과 자신의 죄책감)를 ‘우선 환대’함으로써 현재로 귀환하는 애도."),
        ],
        plot_beats=[
            ("1막 (발단·촉발)", "계단이 어긋난 도면", "왕래가 끊겼던 형의 부고와 함께, 형이 수년간 반복해 그린 기이한 건축 스케치 묶음이 재하에게 전달된다. 재하는 이를 타인의 의뢰물처럼 냉정하게 해몽하기 시작한다."),
            ("2막 (역전·위기)", "병렬 시간의 조우", "도면 속 방들의 치수와 창문의 각도를 역산할수록, 그 공간이 형의 망상이 아니라 20년 전 화재 현장에서 재하가 외면했던 ‘실제 시야각’을 재현한 것임이 밝혀진다."),
            ("3막 (절정·해소)", "껍데기 너머의 애도", "재하는 자신이 피해자라는 ‘자랑스러운 흉터’ 뒤에 숨어 형에게 모든 짐을 떠넘겼음을 인정한다. 어긋난 계단이 있는 실제 폐가를 찾아가 멈춰 있던 유년의 시간을 마침내 닫는다."),
        ],
        key_scene="형이 남긴 도면대로 지어진 미완성 가옥의 계단을 오르던 재하가, 한 칸이 일부러 낮게 설계된 7번째 계단에서 발이 쑥 꺼지며 20년 전 자신이 형의 손을 먼저 놓았던 촉각적 기억과 마주하는 정적의 순간.",
        accent_col=ACCENT_PLUM,
        soft_bg=SOFT_PLUM_BG,
    )


def build_slide_9_style_clinic(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(
        slide,
        "08  |  NON-FICTION TO FICTION TRANSLATION CLINIC",
        "비문학의 날카로운 논증을 ‘설교(Tell)’가 아닌 ‘서사적 체험(Show)’으로 번역하는 법",
        "작가의 최대 강점인 ‘밀도 높은 사유’를 살리되, 에세이 특유의 추상적 서술어를 인물·사물·대사의 역학으로 치환한다",
        page_num=9,
    )

    translations = [
        (
            "변환 01  |  정신분석적 개념 정의  →  사물(Fétiche)과 행동의 모순으로 시각화",
            "[작가의 비문학 원문 스타일 (파편들·ETC)]",
            "“투사 기제는 자아상을 전제로 한 연약한 자기방어의 수단이다. 달달한 현실만 받아들이려는 비대한 자아는 스스로 기획하지 않은 절대적 현실에는 책임을 지려 하지 않는다.”",
            "[소설 장면으로 번역 (Show — 행동과 사물의 아이러니)]",
            "“도윤은 유가족의 탄원서를 서류철 맨 밑바닥으로 밀어 넣은 뒤, 책상 위 작은 탁상거울의 각도를 고쳐 자신의 넥타이 매듭이 반듯한지부터 확인했다. 녹음기의 빨간 불이 꺼지자마자 그는 방금 자신이 한 말을 스스로 믿기라도 하듯 고개를 천천히 끄덕였다.”",
            "‘투사·비대한 자아’라는 학술어를 지우고, 탄원서를 덮는 손길과 거울 속 넥타이를 고치는 행동의 대조로 자기애적 방어기제를 즉각 체감시킴",
        ),
        (
            "변환 02  |  시스템·인식론 은유  →  인물이 겪는 물리적 규칙과 감각 이상으로 구현",
            "[작가의 비문학 원문 스타일 (리뷰s <빌>)]",
            "“우리가 의사결정할 적에 사고를 하기보다 캐시(기억)에 의존하는 게 종종 편하다. 사고는 그 자체로 자아의 죽음인 까닭에 감내해야 할 발달 과정으로서의 폭력이다.”",
            "[소설 장면으로 번역 (Show — 세계관 디테일과 신체 감각)]",
            "“질문을 받은 순간 진우의 시야 우측 상단에 ‘추천 응답 캐시 #402: 온화한 미소와 공감’이 파란 자막으로 떠올랐다. 진우가 자동 승인 버튼을 누르는 대신 캐시 창을 강제로 닫자, 한 번도 써본 적 없는 전두엽 안쪽에서 녹슨 경첩이 뒤틀리는 듯한 현기증이 치밀어 올랐다.”",
            "비문학의 탁월한 ‘캐시 기억’ 은유를 실제 SF 장면의 UI와 신체적 통증(녹슨 경첩 같은 현기증)으로 구체화",
        ),
        (
            "변환 03  |  철학적 아포리즘  →  인물 간의 권력 구도가 담긴 서브텍스트 대사로 변환",
            "[작가의 비문학 원문 스타일 (ETC <순위>)]",
            "“가르치는 지점에서 자칭 선생은 이론을 전개하는 걸 포기하고 이를 이미지로 번역할 뿐만 아니라, 이론들에 대한 이미지 간 순위를 매기기 시작한다. 할 수 없는 자는 순위 매긴다.”",
            "[소설 장면으로 번역 (Show — 행간이 살아있는 대사)]",
            "“‘박 교수님 논문은 참 깊어요. 다만 요즘 독자들한텐 너무 불친절하죠. 그래서 제가 이번 방송에서 교수님 이론을 S급 말고 A급 감성 철학 코너에 넣어드렸습니다. 대중은 증명보다 등수를 좋아하니까요.’ 민재가 웃으며 찻잔을 건네자, 노교수는 찻잔 대신 민재의 화려한 시계를 내려다보았다.”",
            "작가의 목소리로 직접 논평하는 대신, 속물적 캐릭터의 능청스러운 대사와 상대의 침묵(시선 처리)으로 주제를 폭발시킴",
        ),
    ]

    for idx, (tag, b_lbl, b_txt, a_lbl, a_txt, tip) in enumerate(translations):
        ry = 1.52 + idx * 1.34
        # Left Non-fiction style box
        add_rect(slide, 0.65, ry, 4.55, 1.30, fill_color=BG_SAND, line_color=BORDER_WARM, line_pt=1.0, rounded=True, radius=0.04)
        add_textbox(slide, 0.80, ry + 0.06, 4.25, 0.22, text=tag, size_pt=9.3, bold=True, color=ACCENT_RUST, line_spacing=1.0, margin_in=0.01)
        add_textbox(slide, 0.80, ry + 0.28, 4.25, 0.20, text=b_lbl, size_pt=8.8, bold=True, color=INK_MUTED, line_spacing=1.0, margin_in=0.01)
        add_textbox(slide, 0.80, ry + 0.48, 4.25, 0.66, text=b_txt, size_pt=9.6, bold=False, color=INK_SLATE, line_spacing=1.20, margin_in=0.01)

        # Arrow
        add_textbox(slide, 5.22, ry + 0.36, 0.36, 0.44, text="→", size_pt=20, bold=True, color=ACCENT_RUST, align=PP_ALIGN.CENTER)

        # Right Fiction style box
        add_rect(slide, 5.60, ry, 7.08, 1.30, fill_color=BG_WHITE, line_color=ACCENT_TEAL, line_pt=1.3, rounded=True, radius=0.04)
        add_rect(slide, 5.60, ry, 0.09, 1.30, fill_color=ACCENT_TEAL)
        add_textbox(slide, 5.80, ry + 0.06, 6.75, 0.22, text=a_lbl, size_pt=9.3, bold=True, color=ACCENT_TEAL, line_spacing=1.0, margin_in=0.01)
        add_textbox(slide, 5.80, ry + 0.28, 6.75, 0.60, text=a_txt, size_pt=9.8, bold=True, color=INK_NAVY, line_spacing=1.15, margin_in=0.01)
        add_rect(slide, 5.80, ry + 0.88, 6.72, 0.38, fill_color=SOFT_TEAL_BG, rounded=True, radius=0.15)
        add_textbox(slide, 5.88, ry + 0.88, 6.56, 0.38, text=f"✓ 전환 핵심: {tip}", size_pt=8.8, bold=True, color=ACCENT_TEAL,
                    anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0, margin_in=0.01)

    # Bottom 3 Micro-Habits for Non-fiction Writers
    add_rect(slide, 0.65, 5.56, 12.03, 1.32, fill_color=INK_NAVY, rounded=True, radius=0.04)
    add_textbox(slide, 0.88, 5.64, 11.5, 0.26,
                text="작가의 문장 습관(괄호 · 강조부호 · 수사 의문문)을 소설적으로 다듬는 3가지 체크리스트",
                size_pt=11.5, bold=True, color=ACCENT_GOLD, margin_in=0.01)

    checks = [
        ("01. 괄호 보충설명 ‘(즉, ~라는)’ 줄이기", "비문학에서 정확성을 위해 쓰던 이중 괄호 설명을 과감히 덜어내고, 독자가 인물의 행동과 대사 사이의 빈틈(여백)을 스스로 추론하게 남겨두어라."),
        ("02. 수사 의문문 ‘~아니던가?’의 치환", "화자가 독자에게 되묻는 ‘~하지 않던가 말이다’ 어미를 줄이고, 주인공이 결정적 순간에 마주하는 물리적 딜레마와 선택의 결과로 문장을 마침표로 끝내라."),
        ("03. 추상 명사 1개당 감각 사물 1개 대응", "‘필연성·자아상·투사·결핍’ 같은 추상 개념이 머릿속에 떠오를 때마다, 그 개념을 대변하는 구체적 사물(고장 난 가로등, 어긋난 계단, 녹음기)을 먼저 배치하라."),
    ]
    for i, (ct, cd) in enumerate(checks):
        cx = 0.88 + i * 3.92
        add_rect(slide, cx, 5.96, 3.72, 0.92, fill_color=BG_DARK_CARD, line_color=BORDER_DARK, rounded=True, radius=0.05)
        add_textbox(slide, cx + 0.12, 6.00, 3.48, 0.22, text=ct, size_pt=10.0, bold=True, color=INK_LIGHT, margin_in=0.01)
        add_textbox(slide, cx + 0.12, 6.24, 3.48, 0.62, text=cd, size_pt=8.9, bold=False, color=INK_LIGHT_MUTED, line_spacing=1.05, margin_in=0.01)


def build_slide_10_roadmap(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_and_footer(
        slide,
        "09  |  4-WEEK ACTIONABLE ROADMAP FOR YOUR FIRST SHORT STORY",
        "‘필연의 여백’에서 당신만의 ‘정교하고 정확한 허구’를 완성하기 위한 4주 로드맵",
        "이미 157쪽의 비문학으로 세계관과 주제의식은 충분히벼려졌다 — 이제 단편 1편(원고지 80매)으로 첫 서사를 증명할 차례다",
        page_num=10,
        dark=True,
    )

    weeks = [
        (
            "WEEK 01",
            "기획안 선택 & 로그라인 고정",
            "비문학 에세이 1편을 소설의 씨앗으로 선택",
            "• 4가지 기획안 중 가장 먼저 쓰고 싶은 1편 선택 (첫 작품으로는 《가로등 아래의 열쇠》 또는 《캐시의 도시》 추천)\n"
            "• 주인공의 ‘거짓 믿음(The Lie)’과 그것을 깨뜨릴 ‘이질적 타자/사건’을 한 줄의 로그라인으로 확정\n"
            "• 주인공이 집착하는 상징적 사물(Fétiche) 3가지 설정",
            ACCENT_RUST,
        ),
        (
            "WEEK 02",
            "5대 전환점 & 8개 장면 카드 설계",
            "‘그리고’가 아닌 ‘그래서/그러나’의 사슬",
            "• 단편소설(원고지 70~100매) 기준 총 8개 장면(Scene)의 카드를 한 줄씩 배치\n"
            "• ① 일상과 거짓 믿음 → ② 촉발 사건(나쁜 예감) → ③ 가짜 해상도의 추론 → ④ 중간점 반전 → ⑤ 알리바이의 붕괴(암흑) → ⑥ 자아상의 죽음과 도약(클라이맥스)\n"
            "• 각 장면 끝에 감정의 부호(+/-)가 뒤집히는지 점검",
            ACCENT_GOLD,
        ),
        (
            "WEEK 03",
            "내면의 편집자 끄고 초고 완주",
            "개념 설명 대신 인물의 행동과 대사로 전진",
            "• 하루 원고지 15매(약 3,000자)씩 6일간 초고 끝까지 돌파\n"
            "• 집필 중 철학적 해설이 길어지려 할 때마다 ‘지금 인물의 손은 무엇을 만지고 있는가? 시선은 어디를 피하는가?’ 질문하며 장면(Scene)으로 복귀\n"
            "• 멈출 때는 다음 날 이어 쓸 행동 문장 중간에서 멈추기",
            ACCENT_TEAL,
        ),
        (
            "WEEK 04",
            "개념어 솎아내기 & 3단계 퇴고",
            "추상어를 지운 자리에 여백과 울림 남기기",
            "• 3일간의 숙성기(Cooling Off) 후 낯선 독자의 눈으로 통독\n"
            "• 원고에서 ‘투사, 자명성, 필연, 관념, 양태’ 같은 비문학 개념어를 검색(Ctrl+F)해 절반 이상을 구체적 사물 묘사와 대사로 치환\n"
            "• 소리 내어 읽으며 문장의 호흡을 조율하고 첫 단편 완성!",
            ACCENT_INDIGO,
        ),
    ]

    for i, (wbadge, wtitle, wsub, wbody, wcol) in enumerate(weeks):
        wx = 0.65 + i * 3.06
        wy = 1.60
        ww, wh = 2.88, 4.18
        add_rect(slide, wx, wy, ww, wh, fill_color=BG_DARK_CARD, line_color=BORDER_DARK, line_pt=1.0, rounded=True, radius=0.04)
        add_rect(slide, wx, wy, ww, 0.08, fill_color=wcol)

        add_rect(slide, wx + 0.18, wy + 0.18, 1.10, 0.30, fill_color=wcol, rounded=True, radius=0.18)
        add_textbox(slide, wx + 0.18, wy + 0.18, 1.10, 0.30, text=wbadge, size_pt=9.5, bold=True, color=BG_WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

        add_textbox(slide, wx + 0.18, wy + 0.56, ww - 0.36, 0.34, text=wtitle, size_pt=13.2, bold=True, color=INK_LIGHT, margin_in=0.01)
        add_textbox(slide, wx + 0.18, wy + 0.90, ww - 0.36, 0.28, text=wsub, size_pt=9.6, bold=True, color=ACCENT_GOLD, margin_in=0.01)

        add_rect(slide, wx + 0.18, wy + 1.24, ww - 0.36, 0.015, fill_color=BORDER_DARK)

        add_textbox(slide, wx + 0.18, wy + 1.36, ww - 0.36, 2.68, text=wbody,
                    size_pt=9.6, bold=False, color=INK_LIGHT_MUTED, line_spacing=1.28, margin_in=0.01)

    # Bottom Closing Banner quoting the author's own words
    add_rect(slide, 0.65, 5.96, 12.03, 0.90, fill_color=ACCENT_RUST, rounded=True, radius=0.06)
    add_textbox(slide, 0.85, 6.00, 11.63, 0.46,
                text="“관객이 도무지 관객의 자리에 머물지 못하도록 하는, 작품을 향유하기보다 다른 작품을 기어이 생산하도록 추동하는 작품”",
                size_pt=13.2, bold=True, color=INK_LIGHT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_textbox(slide, 0.85, 6.47, 11.63, 0.34,
                text="당신이 『파편들』 P.46에 적었던 바로 그 ‘살아 작동하는 허구’를 이제 당신의 첫 소설로 시작해 보세요.",
                size_pt=10.8, bold=False, color=SOFT_GOLD_BG, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    cover_art = generate_cover_constellation()
    kw_chart = generate_keyword_chart()
    genre_mat = generate_genre_matrix()

    build_slide_1_cover(prs, cover_art)
    build_slide_2_corpus_analysis(prs, kw_chart)
    build_slide_3_conflict_engines(prs)
    build_slide_4_genre_positioning(prs, genre_mat)
    build_slide_5_proposal_1(prs)
    build_slide_6_proposal_2(prs)
    build_slide_7_proposal_3(prs)
    build_slide_8_proposal_4(prs)
    build_slide_9_style_clinic(prs)
    build_slide_10_roadmap(prs)

    warnings = validate.check_presentation(prs)
    assert not warnings, warnings
    print("[ppt_module.validate] 겹침/칸 밖 이탈 없음")

    out_path = os.path.join(PROJECT_ROOT, "맞춤형_소설기획_제안서.pptx")
    prs.save(out_path)
    print("Saved:", out_path)


if __name__ == "__main__":
    main()
