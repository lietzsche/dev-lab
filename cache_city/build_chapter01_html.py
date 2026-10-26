#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《캐시의 도시》 1장 · 히트율 99.7% — 심화 기획 HTML

의도적으로 설정 / 사건 / 복선, 이 세 가지 재료만 담는다. 장면 비트 순서,
샘플 문장, 집필 방향 추천 같은 건 담지 않는다 — 문장으로 옮기는 몫은
작가의 재량이다. html_module을 그대로 재사용해 메인 발전기획서와 같은
테마(CACHE_CITY_THEME)로 만든다.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from html_module import Deck, esc
from html_module.components import pill, card, kv_list
from html_module.theme import CACHE_CITY_THEME as THEME

OUT_PATH = os.path.join(HERE, "1장_히트율_99.7%.html")
FOOTER = "《캐시의 도시》 1장 심화 기획 · 히트율 99.7%"


def slide_overview(deck):
    body = f"""
    {pill("CHAPTER 01 · 초반부 1/4", THEME.accent_2)}
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem);margin:0.6rem 0 0.2rem;">히트율 99.7%</h1>
    {kv_list([
        ("분량", "10매 (원고지)"),
        ("감정 부호", "+"),
        ("시점", "서진우 3인칭 제한"),
        ("다음 장 연결", "그날 밤 → 2장 ‘한 줄짜리 병목’"),
    ])}
    """
    deck.add_slide("overview", "개요", body, dark=True)


def slide_setting(deck):
    body = f"""
    {deck.slide_header("설정", "장소 · 인물 · 이 장에서 작동 중인 세계관 규칙", None)}
    <div class="grid grid-2">
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">장소 · 시간 · 분위기</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>해변 공원 산책로, 초가을 이른 아침</li>'
            '<li>조깅하는 시민들, 커피를 든 사람들 — 평범한 아침 풍경</li>'
            '<li>수평선 너머로 구시가지(비캐시 구역)의 흐릿한 실루엣이 보인다</li>'
            '<li>소리: 파도, 먼 갈매기, 조깅화가 모래를 치는 소리. 그 외엔 거의 무음</li>'
            '<li>빛: 보정된 듯 지나치게 선명한 아침 햇살</li></ul>')}
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">등장인물</p>' + kv_list([
          ("서진우 (POV)", "38 · 부하테스트 엔지니어. 손목 디바이스 + 진단 레이어(헤아림 위에 겹쳐 보는 업무용 오버레이) 착용."),
          ("은채 (동료, 단역)", "진우와 같은 리허설 조에 속한 동료."),
          ("배경 시민들", "이름 없음."),
      ]))}
    </div>
    <div class="grid grid-2" style="margin-top:0.8rem;">
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">진우의 업무 · 장비</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>‘리허설’: 공공장소에서 실제 시민들의 딜레마 신호를 가지고 헤아림의 응답 속도를 점검하는 정기 업무. 시민들은 자신이 테스트 대상인 줄 모른다.</li>'
            '<li>진단 레이어: 헤아림 위에 겹쳐지는 그의 전용 업무 화면. 히트율·응답 지연·MISS 비율이 시야 한쪽에 상주한다.</li>'
            '<li>손목 디바이스를 두드려 응답을 승인/기록한다.</li></ul>')}
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">이 장에서 작동 중인 세계관 규칙</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>헤아림: 시민의 딜레마 신호 감지 → 조회 → 0.2초 안에 가장 비슷한 행복 기억(추천 응답) 반환 → 자동 승인</li>'
            '<li>HIT 99.7% / MISS 0.3%(직접 사고 → 현기증). 진우는 MISS를 겪어본 적 없다.</li>'
            '<li>진단 레이어 한쪽에 ‘연산소: 정상’이라는 상태 표시가 상시 떠 있다.</li></ul>')}
    </div>
    <div class="grid grid-2" style="margin-top:0.8rem;">
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">용어: 헤아림 / 캐시 구역 / 비캐시 구역</p>' + kv_list([
          ("헤아림 (이름의 뜻)", "원래 뜻은 ‘남의 마음이나 사정을 깊이 생각해서 미리 알아주는 것’ — 즉 숙고와 "
           "공감. 그런데 이 장치가 실제로 하는 일은 그 반대다: 시민이 스스로 생각하거나 감정을 들여다보기 전에 "
           "‘가장 비슷한 행복 기억’을 대신 꽂아 넣어, 진짜 헤아림(숙고·공감)이 일어날 필요 자체를 없애버린다. "
           "이름과 실제 기능이 정반대라는 이 아이러니가 도시 전체의 작동 원리를 요약한다."),
          ("캐시 구역 (도시 본토, 별도 명칭 없음)", "헤아림 신호가 정상 수신되는 지역 전체. 시민 대부분이 사는 곳이며, "
           "이 장의 무대인 해변 공원도 여기 속한다. ‘캐시 구역’은 비캐시 구역과 대조하기 위한 편의상 지칭일 뿐, "
           "도시 안에서 따로 그렇게 부르지는 않는다 — 그냥 ‘도시’다."),
          ("비캐시 구역", "수신이 약한 구시가지. 헤아림이 제대로 작동하지 않아 주민들이 기억을 일기·녹음·냄새로 "
           "손수 복원한다. 행정상으로는 ‘노후 지역’으로 분류된다. 윤해가 사는 곳이며, 4장에서 진우가 실제로 "
           "들어가게 되는 공간이다."),
      ]), accent=THEME.accent_3)}
    </div>
    """
    deck.add_slide("setting", "설정", body)


EVENTS = [
    "진우가 해변 산책로에서 정기 리허설을 수행한다.",
    "은채가 사소한 일상적 불안(예: 오늘 있을 발표에 대한 걱정)을 겪는다.",
    "헤아림이 0.2초 안에 추천 응답 #402(온화한 미소와 공감)를 띄우고, 은채가 자동 승인한다.",
    "걷는 중 신발 안에 모래가 들어가 발바닥이 살짝 불편해진다. 진우는 헤아림이 반응하기도 전에 "
    "스스로 신발을 털어 그 불편을 없애버린다.",
    "진우의 진단 레이어에서 MISS 비율이 0.30%에서 0.31%로 미세하게 흔들린다. 그는 노이즈로 간주하고 넘긴다.",
    "리허설 중 수평선 너머 구시가지(비캐시 구역)의 실루엣이 시야에 들어온다.",
    "리허설이 끝난다. 진단 레이어에 ‘히트율 99.7% — 정상’이 표시된 채 하루가 마무리된다.",
]


def slide_events(deck):
    items_html = "".join(f"<li>{esc(e)}</li>" for e in EVENTS)
    body = f"""
    {deck.slide_header("사건", "이 장에서 일어나는 일들", None)}
    {card(f'<ol style="margin:0;padding-left:1.2rem;">{items_html}</ol>')}
    """
    deck.add_slide("events", "사건", body)


FORESHADOWING = [
    ("추천 응답 #402라는 구체적 코드", "같은 코드가 반복 등장 — 2장에서 ‘정상적으로 작동한 HIT’의 기준점이 되고, 아버지의 "
     "요청이 왜 비정상인지(같은 메커니즘인데 영원히 안 끝남) 대비시키는 축이 된다.", "2장"),
    ("‘연산소: 정상’이라는 상시 UI 표시", "1장에서 분명히, 배경으로라도 보여줘야 한다 — 5장에서 그게 7년째 조작된 거짓임을 "
     "알게 될 때 독자가 ‘그때 분명 봤는데’ 하고 소급 적용할 수 있도록.", "5장"),
    ("MISS 비율의 미세한 흔들림(0.30→0.31%)", "그가 ‘노이즈’로 무시하는 이 작은 숫자가, 2장에서 실제로 폭증하는 재요청의 "
     "첫 떨림이었음을 나중에 알게 된다.", "2장"),
    ("수평선 너머 구시가지 실루엣", "4장에서 실제로 그 구시가지(비캐시 구역)로 진입하게 될 때, 1장에서 스쳐 지나갔던 그 "
     "풍경이 되돌아와 공간적 긴장을 완성한다.", "4장"),
    ("진우의 ‘과잉 숙련’ 제스처(모래 불편을 스스로 지우는 동작)", "그의 거짓 믿음이 신체화된 습관이라는 걸 미리 심어둬야, "
     "5장에서 추천 응답을 ‘의식적으로’ 끄는 행동이 얼마나 큰 결단인지 대비가 선다.", "5장"),
    ("은채의 사소한 걱정과 자동 승인", "‘누구도 직접 생각하지 않는다’는 세계관 명제를 가장 작고 무해한 사례로 먼저 보여줘, "
     "2~3장에서 노인들의 걱정이 쌓여 재요청이 되는 더 심각한 버전과 규모 대비를 만든다.", "3장"),
]


def slide_foreshadowing(deck):
    rows_html = []
    for seed, payoff, where in FORESHADOWING:
        rows_html.append(f"""
        <tr>
          <td style="font-weight:700;">{esc(seed)}</td>
          <td>{esc(payoff)}</td>
          <td style="text-align:center;">{pill(where, THEME.accent_2)}</td>
        </tr>""")
    body = f"""
    {deck.slide_header("복선", "1장에 심어서 나중 장에서 거둘 것들", None)}
    <table class="cmp">
      <thead><tr><th>1장에 심을 씨앗</th><th>나중에 거두는 의미</th><th>회수 지점</th></tr></thead>
      <tbody>{''.join(rows_html)}</tbody>
    </table>
    """
    deck.add_slide("foreshadowing", "복선", body, dark=True)


def main():
    deck = Deck("1장 · 히트율 99.7% — 심화 기획", THEME, footer=FOOTER)
    slide_overview(deck)
    slide_setting(deck)
    slide_events(deck)
    slide_foreshadowing(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
