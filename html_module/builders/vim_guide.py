#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vim으로 소설 쓰기 — 실전 가이드 HTML 생성 스크립트

코드가 아니라 원고(prose)를 쓰는 사람 기준으로 꼭 필요한 것만 담은
압축 치트시트. html_module을 그대로 재사용.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, PROJECT_ROOT)

from html_module import Deck, esc
from html_module.components import pill, card, kv_list
from html_module.theme import CACHE_CITY_THEME as THEME

OUT_PATH = os.path.join(PROJECT_ROOT, "vim_가이드.html")
FOOTER = "Vim으로 소설 쓰기 · 실전 가이드"


def cheat_table(headers, rows):
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body_rows = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>"
        for row in rows
    )
    return f'<table class="cmp"><thead><tr>{thead}</tr></thead><tbody>{body_rows}</tbody></table>'


def slide_modes(deck):
    body = f"""
    {pill("VIM · 모드 기반 에디터", THEME.accent_2)}
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem);margin:0.6rem 0 0.4rem;">Vim의 전부는 ‘모드’다</h1>
    <p class="muted" style="max-width:46rem;">명령 수십 개를 외울 필요 없다. 지금 내가 어느 모드에 있는지만
    항상 알고 있으면 된다 — 나머지는 그 안에서 쓰는 단축키일 뿐이다.</p>
    <div class="grid grid-2" style="margin-top:1.2rem;">
      {card('<strong>Normal 모드 (기본값)</strong>'
            '<p class="small" style="margin:0.4rem 0 0;">파일을 열면 항상 이 모드로 시작한다. 글자를 치면 '
            '타이핑되는 게 아니라 ‘명령’으로 해석된다 (예: j는 아래로 이동). 이동·삭제·복사·저장 같은 '
            '명령은 전부 여기서 친다.</p>', accent=THEME.accent)}
      {card('<strong>Insert 모드 (타이핑)</strong>'
            '<p class="small" style="margin:0.4rem 0 0;"><code>i</code>를 눌러야 들어간다. 여기서만 '
            '글자가 실제로 입력된다. 한글은 평소 쓰던 입력기(IME)가 그대로 작동한다 — 별도 설정 필요 '
            '없음. 다 썼으면 <code>Esc</code>로 Normal로 돌아간다.</p>', accent=THEME.accent_3)}
    </div>
    {card('<strong>헤매면 무조건 <code>Esc</code>.</strong> 어느 모드에 있든 Esc를 누르면 Normal 모드로 '
          '돌아온다. 화면에 이상한 글자가 찍히거나 명령이 안 먹히면, 십중팔구 지금 모드를 헷갈린 것이다 '
          '— Esc부터 누르고 다시 생각할 것.',
          style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:0.8rem;font-size:1.05rem;")}
    """
    deck.add_slide("modes", "모드", body, dark=True)


def slide_quickstart(deck):
    steps = [
        ("1. 파일 열기", "터미널에서 <code>vim cache_city/원고/1장_히트율_99.7%.md</code> 입력 후 Enter."),
        ("2. 쓰기 시작", "<code>i</code>를 누른다 (화면 아래 <code>-- INSERT --</code>가 뜨면 성공). 이제부터 "
         "치는 대로 글자가 입력된다."),
        ("3. 쓰기 멈출 때", "<code>Esc</code>를 눌러 Normal 모드로 돌아간다. 이동·저장 같은 명령은 Insert "
         "상태에서는 먹히지 않는다."),
        ("4. 저장", "Normal 모드에서 <code>:w</code> 입력 후 Enter. 화면 맨 아래에 명령이 입력되는 줄이 "
         "뜨는 걸 볼 수 있다."),
        ("5. 저장하고 끝내기", "Normal 모드에서 <code>:wq</code> 입력 후 Enter. 저장과 종료를 한 번에 한다."),
    ]
    steps_html = "".join(
        card(f"<strong class='small' style='color:{THEME.accent};'>{esc(t)}</strong>"
             f"<p class='small' style='margin:0.4rem 0 0;'>{d}</p>", accent=THEME.accent)
        for t, d in steps
    )
    body = f"""
    {deck.slide_header("지금 당장 쓰기 시작하는 법", "이 다섯 단계만 알면 오늘부터 Vim으로 쓸 수 있다", None)}
    <div class="grid grid-2">{steps_html}</div>
    {card('<strong>자주 하는 실수</strong> · <code>:wq</code>를 쳤는데 안 꺼지고 이상한 반응이 온다면, '
          '아직 Insert 모드일 수 있다 — <code>Esc</code>를 먼저 누르고 다시 <code>:wq</code>를 입력할 것.')}
    """
    deck.add_slide("quickstart", "빠른 시작", body)


def slide_movement(deck):
    rows = [
        ("h / j / k / l", "왼쪽 / 아래 / 위 / 오른쪽으로 한 칸 이동"),
        ("w / b", "다음 단어 시작 / 이전 단어 시작으로 이동"),
        ("0 / $", "줄 맨 앞 / 줄 맨 끝으로 이동"),
        ("gg / G", "문서 맨 처음 / 문서 맨 끝으로 이동"),
        ("{숫자}G", "해당 줄 번호로 이동 (예: 10G → 10번째 줄)"),
        ("Ctrl-f / Ctrl-b", "한 화면 아래로 / 위로 스크롤"),
        ("/단어 + Enter", "아래 방향으로 ‘단어’ 검색"),
        ("n / N", "검색한 단어의 다음 위치 / 이전 위치로 이동"),
    ]
    body = f"""
    {deck.slide_header("이동", "커서를 옮기는 명령들 (전부 Normal 모드에서)", None)}
    {cheat_table(["명령", "동작"], rows)}
    """
    deck.add_slide("movement", "이동", body)


def slide_editing(deck):
    rows = [
        ("i / a", "현재 글자 앞 / 뒤에서 Insert 모드 시작"),
        ("I / A", "줄 맨 앞 / 맨 끝에서 Insert 모드 시작"),
        ("o / O", "아래 / 위에 새 줄을 만들고 Insert 모드 시작"),
        ("x", "커서 위 글자 한 개 삭제"),
        ("dd", "현재 줄 전체 삭제 (잘라내기 — 다시 붙여넣기 가능)"),
        ("dw", "커서부터 다음 단어 시작까지 삭제"),
        ("d$", "커서부터 줄 끝까지 삭제"),
        ("cw", "커서부터 단어 끝까지 삭제하고 바로 Insert 모드로 (수정할 때 가장 유용)"),
        ("yy", "현재 줄 복사 (잘라내지 않음)"),
        ("p / P", "복사/삭제한 내용을 커서 뒤 / 앞에 붙여넣기"),
        ("u", "방금 한 일 되돌리기 (undo) — 여러 번 누르면 더 이전으로"),
        ("Ctrl-r", "되돌린 것을 다시 적용 (redo)"),
        (".", "방금 한 편집 명령을 그대로 한 번 더 반복"),
    ]
    body = f"""
    {deck.slide_header("편집", "삽입 진입·삭제·복사·되돌리기", None)}
    {cheat_table(["명령", "동작"], rows)}
    """
    deck.add_slide("editing", "편집", body, dark=True)


def slide_search_replace(deck):
    rows = [
        (":w", "저장"),
        (":q", "종료 (저장 안 한 변경이 있으면 거부됨)"),
        (":wq 또는 :x", "저장하고 종료"),
        (":q!", "저장하지 않고 강제 종료 (실수로 망쳤을 때)"),
        ("/찾을말 + Enter", "아래쪽으로 검색"),
        (":%s/old/new/g", "문서 전체에서 old를 new로 전부 치환"),
        (":%s/old/new/gc", "치환할 때마다 확인(y/n)을 물어봄 — 안전하게 바꿀 때"),
    ]
    body = f"""
    {deck.slide_header("저장·종료·검색·치환", "콜론(:)으로 시작하는 명령들", None)}
    {cheat_table(["명령", "동작"], rows)}
    """
    deck.add_slide("search", "검색·치환", body)


def slide_prose_tips(deck):
    body = f"""
    {deck.slide_header("산문 쓰기에 유용한 팁", "소설 원고 작업에서 특히 쓸 만한 것들", None)}
    <div class="grid grid-2">
      {card('<strong>단어 수 세기</strong>'
            '<p class="small" style="margin:0.4rem 0;">Normal 모드에서 <code>g</code> 다음 <code>Ctrl-g</code> '
            '— 화면 아래에 줄 수·단어 수·글자 수가 뜬다.</p>')}
      {card('<strong>자동 줄바꿈 보기</strong>'
            '<p class="small" style="margin:0.4rem 0;"><code>:set wrap linebreak</code> — 긴 문장이 화면 '
            '끝에서 단어 중간이 아니라 단어 단위로 꺾여 보인다. 파일 내용 자체는 바뀌지 않는다 '
            '(보이는 방식만 바뀜).</p>')}
      {card('<strong>두 줄 합치기</strong>'
            '<p class="small" style="margin:0.4rem 0;">Normal 모드에서 <code>J</code> — 현재 줄과 다음 줄을 '
            '한 줄로 합친다. 문단을 다시 다듬을 때 유용.</p>')}
      {card('<strong>한글 입력</strong>'
            '<p class="small" style="margin:0.4rem 0;">Insert 모드에서는 평소 쓰는 한글 입력기가 그대로 '
            '작동한다. Vim 쪽에서 따로 설정할 게 없다.</p>')}
    </div>
    """
    deck.add_slide("prose-tips", "집필 팁", body)


def slide_troubleshooting(deck):
    rows = [
        ("화면에 이상한 글자가 찍히거나 명령이 안 먹힐 때", "Esc를 눌러 Normal 모드로 돌아간 뒤 다시 시도"),
        (":wq를 쳤는데 안 꺼질 때", "아직 Insert 모드였을 수 있다 — Esc를 먼저, 그다음 :wq"),
        ("실수로 문단을 통째로 지웠을 때", "u를 눌러 되돌리기. 여러 번 누르면 계속 이전으로 돌아간다"),
        ("저장 없이 그냥 나가고 싶을 때 (연습 중 실수했을 때)", ":q! 입력"),
        ("지금 몇 번째 줄인지 모를 때", "Normal 모드에서 Ctrl-g — 화면 아래에 현재 줄 번호가 뜬다"),
    ]
    body = f"""
    {deck.slide_header("막혔을 때", "자주 만나는 상황과 탈출법", None)}
    {cheat_table(["상황", "해결"], rows)}
    """
    deck.add_slide("troubleshooting", "막혔을 때", body, dark=True)


def main():
    deck = Deck("Vim으로 소설 쓰기 — 실전 가이드", THEME, footer=FOOTER)
    slide_modes(deck)
    slide_quickstart(deck)
    slide_movement(deck)
    slide_editing(deck)
    slide_search_replace(deck)
    slide_prose_tips(deck)
    slide_troubleshooting(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
