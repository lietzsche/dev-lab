#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Low-level python-pptx shape helpers shared by every slide builder."""

from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

from .theme import FONT_KR


def set_font(run, size_pt, bold=False, italic=False, color=None, font_name=FONT_KR):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = parse_xml(f'<a:ea xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="{font_name}"/>')
        rPr.append(ea)
    else:
        ea.set("typeface", font_name)


def set_slide_background(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def disable_shadow(shape):
    """Removes the default PowerPoint/Impress drop shadow for flat editorial cards."""
    shape.shadow.inherit = False
    spPr = shape._element.spPr
    for child in list(spPr):
        if child.tag.endswith("effectLst"):
            spPr.remove(child)
    spPr.append(parse_xml('<a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>'))


def add_rect(slide, left, top, width, height, fill_color=None, line_color=None, line_pt=1.0,
             rounded=False, radius=0.04):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(shape_type, Inches(left), Inches(top), Inches(width), Inches(height))
    if rounded and shape.adjustments:
        shape.adjustments[0] = radius
    if fill_color is not None:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color is not None:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_pt)
    else:
        shape.line.fill.background()
    disable_shadow(shape)
    return shape
