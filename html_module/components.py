#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small HTML snippet builders shared across the deck scripts.

These just return strings (no DOM, no measuring) — the layout rules live in
``render.py``'s CSS, and the browser does the actual box-fitting.
"""

from .render import esc


def pill(label, color):
    return f'<span class="pill" style="background:{color};">{esc(label)}</span>'


def card(inner_html, accent=None, style=""):
    cls = "card accent-bar" if accent else "card"
    border = f"border-left-color:{accent};" if accent else ""
    return f'<div class="{cls}" style="{border}{style}">{inner_html}</div>'


def grid(children_html, cols=2):
    return f'<div class="grid grid-{cols}">{"".join(children_html)}</div>'


def kv_list(pairs):
    rows = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in pairs)
    return f'<dl class="kv">{rows}</dl>'


def quote(text):
    return f'<p class="quote">“{esc(text)}”</p>'


def compare_table(headers, rows, revised_col=-1):
    """``rows`` is a list of tuples matching ``headers`` length. The column
    at ``revised_col`` gets the accent-highlighted "revised" style."""
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body_rows = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            cls = ' class="revised"' if i == revised_col or (revised_col < 0 and i == len(row) + revised_col) else ""
            cells.append(f"<td{cls}>{esc(cell)}</td>")
        body_rows.append(f"<tr>{''.join(cells)}</tr>")
    return (
        '<table class="cmp"><thead><tr>' + thead + "</tr></thead>"
        "<tbody>" + "".join(body_rows) + "</tbody></table>"
    )
