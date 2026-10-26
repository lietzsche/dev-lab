#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembles a single scrollable HTML document out of named sections.

There is no PPTX-style absolute positioning here on purpose. Every section
is normal flowing HTML/CSS (flexbox/grid), so text never overlaps — the
browser reflows it for us, which is the entire reason this module is so much
smaller than the old ``ppt_module``.
"""

import html as _html


def esc(text):
    """HTML-escapes text; also turns "\\n" into <br> for the odd multi-line
    string still carried over from the PPTX scripts' content."""
    return _html.escape(str(text), quote=False).replace("\n", "<br>")


_BASE_CSS = """
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: {font_stack};
  background: {bg_cream};
  color: {ink_navy};
  line-height: 1.6;
}
a { color: inherit; }
.toc {
  position: sticky; top: 0; z-index: 10;
  display: flex; flex-wrap: wrap; gap: 0.4rem;
  padding: 0.7rem 1rem;
  background: {ink_navy};
  border-bottom: 3px solid {accent};
}
.toc a {
  font-size: 0.78rem; font-weight: 700; text-decoration: none;
  color: {ink_light_muted};
  padding: 0.3rem 0.6rem; border-radius: 999px;
  border: 1px solid {border_dark};
  white-space: nowrap;
}
.toc a:hover { color: {ink_light}; border-color: {accent}; }
.deck-title {
  font-weight: 800; color: {accent_2}; margin-right: 0.6rem;
  font-size: 0.85rem; align-self: center;
}
.slide {
  padding: 2.4rem clamp(1rem, 5vw, 4rem);
  border-bottom: 1px solid {border_warm};
  scroll-margin-top: 3.2rem;
}
.slide.dark { background: {bg_dark}; color: {ink_light}; border-bottom-color: {border_dark}; }
.slide .kicker {
  font-size: 0.8rem; font-weight: 800; letter-spacing: 0.04em;
  color: {accent}; text-transform: uppercase; margin: 0 0 0.3rem;
}
.slide.dark .kicker { color: {accent_2}; }
.slide h2 {
  font-size: clamp(1.3rem, 2.4vw, 1.9rem); margin: 0 0 0.35rem; line-height: 1.3;
}
.slide .subtitle { color: {ink_slate}; margin: 0 0 1.4rem; max-width: 64rem; }
.slide.dark .subtitle { color: {ink_light_muted}; }
.card {
  background: {bg_white}; border: 1px solid {border_warm}; border-radius: 0.6rem;
  padding: 1rem 1.1rem;
}
.slide.dark .card { background: {bg_dark_card}; border-color: {border_dark}; }
.card.accent-bar { border-left: 4px solid {accent}; }
.grid { display: grid; gap: 0.9rem; }
.grid-2 { grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr)); }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); }
.grid-4 { grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr)); }
.pill {
  display: inline-block; font-size: 0.72rem; font-weight: 700;
  padding: 0.15rem 0.6rem; border-radius: 999px; color: #fff;
}
.kv { display: grid; grid-template-columns: 7rem 1fr; gap: 0.3rem 0.8rem; font-size: 0.92rem; }
.kv dt { font-weight: 700; color: {accent}; }
.slide.dark .kv dt { color: {accent_2}; }
.kv dd { margin: 0; }
table.cmp { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
table.cmp th, table.cmp td { text-align: left; padding: 0.55rem 0.7rem; vertical-align: top; }
table.cmp thead th { background: {ink_navy}; color: {ink_light}; }
table.cmp tbody tr:nth-child(odd) td { background: {bg_white}; }
table.cmp tbody tr:nth-child(even) td { background: {bg_cream}; }
table.cmp td.revised { background: {bg_white}; border-left: 3px solid {accent}; font-weight: 600; }
.quote {
  font-size: 1.05rem; font-style: italic; border-left: 3px solid {accent};
  padding-left: 0.8rem; margin: 0.6rem 0;
}
.muted { color: {ink_muted}; }
.slide.dark .muted { color: {ink_light_muted}; }
.small { font-size: 0.85rem; }
footer.page-footer {
  padding: 1.2rem clamp(1rem, 5vw, 4rem); font-size: 0.8rem; color: {ink_muted};
  display: flex; justify-content: space-between;
}
@media print {
  .toc { display: none; }
  .slide { break-after: page; border: none; }
}
"""


class Deck:
    """Collects ``add_slide`` calls and renders one standalone HTML file."""

    def __init__(self, title, theme, footer=""):
        self.title = title
        self.theme = theme
        self.footer = footer
        self._slides = []  # list of (id, nav_label, html)

    def add_slide(self, slide_id, nav_label, body_html, dark=False):
        self._slides.append((slide_id, nav_label, body_html, dark))
        return self

    def slide_header(self, kicker, title, subtitle=None):
        parts = [f'<p class="kicker">{esc(kicker)}</p>', f"<h2>{esc(title)}</h2>"]
        if subtitle:
            parts.append(f'<p class="subtitle">{esc(subtitle)}</p>')
        return "\n".join(parts)

    def render(self):
        t = self.theme
        # Plain str.replace, not .format(): the CSS body is full of literal
        # {braces} for rule blocks, which .format() would choke on.
        css = _BASE_CSS
        for token, value in (
            ("font_stack", t.font_stack), ("bg_cream", t.bg_cream), ("bg_dark", t.bg_dark),
            ("bg_dark_card", t.bg_dark_card), ("bg_white", t.bg_white), ("ink_navy", t.ink_navy),
            ("ink_slate", t.ink_slate), ("ink_muted", t.ink_muted), ("ink_light", t.ink_light),
            ("ink_light_muted", t.ink_light_muted), ("accent", t.accent), ("accent_2", t.accent_2),
            ("border_warm", t.border_warm), ("border_dark", t.border_dark),
        ):
            css = css.replace("{" + token + "}", value)

        toc_links = "\n".join(
            f'<a href="#{sid}">{esc(label)}</a>' for sid, label, *_ in self._slides
        )

        slides_html = []
        total = len(self._slides)
        for idx, (sid, _label, body, dark) in enumerate(self._slides, start=1):
            cls = "slide dark" if dark else "slide"
            slides_html.append(
                f'<section class="{cls}" id="{sid}">\n{body}\n'
                f'<p class="small muted" style="margin-top:1.4rem;">{idx:02d} / {total:02d}</p>\n'
                f"</section>"
            )

        return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(self.title)}</title>
<style>{css}</style>
</head>
<body>
<nav class="toc">
  <span class="deck-title">{esc(self.title)}</span>
  {toc_links}
</nav>
{''.join(slides_html)}
<footer class="page-footer"><span>{esc(self.footer)}</span><span>{total} sections</span></footer>
</body>
</html>
"""
