#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
《캐시의 도시》 1장 · 히트율 99.7% — 심화 장 단위 기획 HTML

메인 발전기획서(build_cache_city_html.py)의 1장 카드를 한 문단 수준에서
장소/시간/인물/비트/복선/묘사용 사건까지로 확장한 단독 문서. html_module을
그대로 재사용해 같은 테마(CACHE_CITY_THEME)로 만든다.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from html_module import Deck, esc
from html_module.components import pill, card, kv_list, quote
from html_module.theme import CACHE_CITY_THEME as THEME

OUT_PATH = os.path.join(HERE, "1장_히트율_99.7%.html")
FOOTER = "《캐시의 도시》 1장 심화 기획 · 히트율 99.7%"


def slide_overview(deck):
    body = f"""
    {pill("CHAPTER 01 · 초반부 1/4", THEME.accent_2)}
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem);margin:0.6rem 0 0.2rem;">히트율 99.7%</h1>
    <p class="muted" style="max-width:48rem;">
    도시가 완벽하게 ‘정상’으로 보이는 하루. 그러나 아무도 진짜로 생각하지 않는다 —
    그 사실만 독자가 먼저 눈치채게 만드는 장.</p>
    {kv_list([
        ("분량", "10매 (원고지)"),
        ("감정 부호", "+ (평온 · 그러나 서늘한 안도)"),
        ("시점", "서진우 3인칭 제한"),
        ("장소·시간", "해변 공원 · 초가을 이른 아침"),
        ("이 장의 기능", "‘정상’의 기준선을 보여줘서, 2장의 ‘병목’이 왜 사건인지 독자가 체감하게 만든다"),
        ("다음 장과의 연결", "그런데 바로 그날 밤 → 2장 ‘한 줄짜리 병목’"),
    ])}
    """
    deck.add_slide("overview", "개요", body, dark=True)


def slide_setting(deck):
    body = f"""
    {deck.slide_header("설정 · 이 장이 벌어지는 자리", "해변 공원, 초가을 이른 아침",
                        "날씨·빛·소리를 ‘완벽하게 필터링된 쾌적함’으로 쓸 것 — 그 쾌적함 자체가 이 장의 불안의 재료다")}
    <div class="grid grid-2">
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">공간</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>해변을 따라 난 산책로 · 조깅하는 시민들, 커피를 든 사람들 — 겉보기엔 평범한 아침 풍경</li>'
            '<li>수평선 너머로 구시가지(비캐시 구역)의 흐릿한 실루엣이 보이지만, 아무도 그쪽을 오래 보지 않는다</li>'
            '<li>진우는 이 공원을 ‘현장’으로 쓴다 — 실제 시민들의 딜레마 신호를 가지고 헤아림의 응답 속도를 점검하는 정기 리허설 장소</li></ul>')}
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">분위기 · 날씨</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>빛이 지나치게 선명하다 — 보정된 듯한 쾌적함. 바람은 적당히, 파도는 일정한 리듬으로</li>'
            '<li>소리는 거의 없다: 파도, 먼 갈매기, 조깅화가 모래를 치는 소리 정도. 도시 전체가 ‘조용히 잘 작동 중’</li>'
            '<li>침묵이 평화가 아니라 ‘소음 제거’처럼 느껴지게 쓸 것 — 너무 깨끗해서 오히려 섬뜩한 질감</li></ul>')}
    </div>
    <div class="grid grid-2" style="margin-top:0.8rem;">
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">등장인물</p>' + kv_list([
          ("서진우 (POV)", "38 · 부하테스트 엔지니어. 손목 디바이스 + 진단 레이어(헤아림 위에 겹쳐 보는 업무용 오버레이)를 쓴다."),
          ("은채 (동료, 단역)", "진우와 같은 리허설 조에 속한 동료. 이 장에서만 쓰이는 ‘평범한 시민 딜레마’의 체화 — 이후 재등장은 선택사항."),
          ("배경 시민들", "이름 없음. 도시의 ‘정상성’을 보여주는 합창 같은 존재."),
      ]))}
      {card('<p style="font-weight:800;margin:0 0 0.5rem;">진우의 장비 · 업무 디테일</p>'
            '<ul class="small" style="margin:0;padding-left:1.1rem;">'
            '<li>헤아림(시민용) 위에 겹쳐지는 진단 레이어 — 히트율·응답 지연·MISS 비율이 그의 시야 한쪽에 작게 상주</li>'
            '<li>손목 디바이스를 ‘톡, 톡’ 두드려 응답을 승인/기록 — 이 동작이 그의 몸에 완전히 밴 습관이라는 걸 보여줄 것</li>'
            '<li>‘리허설’이라는 명목: 실제 공공장소에서 실제 딜레마 신호를 가지고 시스템을 점검 — 시민들은 자신이 테스트 대상인 줄 모른다</li></ul>')}
    </div>
    """
    deck.add_slide("setting", "설정", body)


def slide_world(deck):
    body = f"""
    {deck.slide_header("세계관 · 이 장에서 ‘설명 없이’ 보여줘야 할 규칙",
                        "헤아림의 평소 작동 방식을 대사 한 줄 없이 체감시킨다",
                        "이미 세계관 규칙 문서에 정의된 헤아림/HIT·MISS를 이 장에서 ‘처음 실연’한다 — 숫자·UI·신체 반응으로만")}
    <div class="grid grid-3">
      {card('<strong>헤아림의 평소 흐름</strong>'
            '<p class="small muted" style="margin:0.4rem 0 0;">시민의 딜레마 신호 감지 → 헤아림 조회 → 0.2초 안에 가장 '
            '비슷한 행복 기억(추천 응답) 반환 → 자동 승인. 이 장에서는 이 흐름이 ‘매끄럽고 다정한 것’으로 느껴지도록 쓸 것 — '
            '독자가 불편해지는 건 그 매끄러움이 ‘너무’ 완벽하기 때문이어야 한다.</p>', accent=THEME.accent)}
      {card('<strong>HIT 99.7% / MISS 0.3%</strong>'
            '<p class="small muted" style="margin:0.4rem 0 0;">99.7%라는 숫자를 진우의 시야 한쪽에 상시 떠 있는 작은 '
            '디아그노스틱 숫자로 등장시킨다. MISS(0.3%, 직접 사고 → 현기증)는 이 장에서는 ‘그런 게 있다’ 정도로만, 진우 본인은 '
            '한 번도 겪어본 적 없는 먼 개념처럼 다룬다 — 5장에서 그가 처음 겪을 현기증의 낙차를 위해.</p>', accent=THEME.accent_3)}
      {card('<strong>연산소(사고 서버)</strong>'
            '<p class="small muted" style="margin:0.4rem 0 0;">진단 레이어 한 귀퉁이에 ‘연산소: 정상’이라는 상태 표시가 늘 '
            '떠 있다는 것만 이 장에서 각인시킨다. 이 장에서는 그냥 배경 UI처럼 — 독자가 나중(5장)에 그 표시가 7년째 조작된 거짓이었음을 '
            '알게 될 때, ‘아, 1장에서 분명 봤었는데’ 하고 돌아보게 만드는 장치.</p>', accent=THEME.accent_2)}
    </div>
    """
    deck.add_slide("world", "세계관", body, dark=True)


BEATS = [
    ("비트 01 · 오프닝 이미지", "해변 산책로. 조깅하는 사람들과 커피를 든 사람들 사이로 진우가 걷는다. 그의 시야 한쪽에만 "
     "보이는 숫자들(히트율 99.7%, 응답 지연 0.2초)로 독자에게 이 세계의 ‘정상 상태’를 처음 보여준다."),
    ("비트 02 · 업무를 행동으로", "누군가의 ‘딜레마 신호’가 그의 진단 레이어에 뜬다. 그의 손목 디바이스가 스톱워치처럼 "
     "반짝이고, 그는 익숙하게 반응 시간을 잰다 — 대사 없이, 숙련된 동작으로."),
    ("비트 03 · 은채 등장", "동료 은채가 다가와 사소한 불안(예: 오늘 있을 평가 발표가 걱정된다는 정도의 일상적 걱정)을 "
     "토로한다. 아주 작고 현실적인 걱정이어야 한다 — 비극이 아니라 ‘누구나 겪는 찜찜함’."),
    ("비트 04 · HIT의 실연", "헤아림이 0.2초 안에 추천 응답 #402(온화한 미소와 공감)를 띄우고, 은채는 자동으로 승인한다. "
     "둘 다 그걸 ‘다정함’이라고 느낀다 — 독자만 그 매끄러움의 섬뜩함을 눈치채야 한다."),
    ("비트 05 · 진우의 과잉 숙련", "진우 자신도 신발에 모래가 들어간 사소한 불편 같은 걸 겪자, 헤아림이 뜨기도 전에 "
     "스스로 먼저 그 감각을 지워버리는 제스처를 보인다 — 그의 거짓 믿음(‘생각은 비용이다’)을 대사 없이 행동으로 증명."),
    ("비트 06 · 미세한 이상치 (복선)", "진단 레이어에서 MISS 비율이 0.30%에서 0.31%로, 거의 보이지 않게 흔들린다. 진우는 "
     "‘노이즈’라며 손목을 한 번 두드려 확인란을 닫아버린다."),
    ("비트 07 · 수평선의 구시가지 (복선)", "멀리 구시가지의 흐릿한 실루엣이 보인다. 짧은 생각 — ‘저긴 신경 쓸 거 없다’ — "
     "로 도시 전체의 통념을 암시한다. 대사로 설명하지 말고 시선이 그냥 미끄러지듯 지나가게."),
    ("비트 08 · 닫는 이미지", "리허설이 끝난다. 진우가 떠나는 등 뒤로 ‘99.7% — 정상’이라는 숫자가 화면에 고정된다. "
     "문장은 평온하지만, 마지막 한 줄은 어딘가 비어 있는 울림으로 끝낼 것."),
]


def slide_beats(deck):
    beats_html = "".join(
        card(f"<strong class='small' style='color:{THEME.accent};'>{esc(t)}</strong>"
             f"<p class='small' style='margin:0.4rem 0 0;'>{esc(d)}</p>", accent=THEME.accent)
        for t, d in BEATS
    )
    body = f"""
    {deck.slide_header("장면 비트 · 8단계로 세분화", "대사보다 행동과 UI, 숫자로 전개한다",
                        "각 비트는 1~2 문단 분량을 가정. 전체 10매 중 비트 03~05(은채·HIT 실연)에 가장 많은 분량을 배정할 것")}
    <div class="grid grid-2">{beats_html}</div>
    """
    deck.add_slide("beats", "장면 비트", body)


FORESHADOWING = [
    ("추천 응답 #402라는 구체적 코드", "같은 코드가 반복 등장 — 2장에서 ‘정상적으로 작동한 HIT’의 기준점이 되고, 아버지의 "
     "요청이 왜 비정상인지(같은 메커니즘인데 영원히 안 끝남) 대비시키는 축이 된다.", "2장"),
    ("‘연산소: 정상’이라는 상시 UI 표시", "1장에서 분명히, 배경으로라도 보여줘야 한다 — 5장에서 그게 7년째 조작된 "
     "거짓임을 알게 될 때 독자가 ‘그때 분명 봤는데’ 하고 소급 적용할 수 있도록.", "5장"),
    ("MISS 비율의 미세한 흔들림(0.30→0.31%)", "그가 ‘노이즈’로 무시하는 이 작은 숫자가, 2장에서 실제로 폭증하는 재요청의 "
     "첫 떨림이었음을 나중에 알게 된다.", "2장"),
    ("수평선 너머 구시가지 실루엣 + ‘신경 쓸 거 없다’는 통념", "4장에서 실제로 그 구시가지(비캐시 구역)로 진입하게 될 때, "
     "1장에서 스쳐 지나갔던 그 풍경이 되돌아와 공간적 긴장을 완성한다.", "4장"),
    ("진우의 ‘과잉 숙련’ 제스처(모래 불편을 스스로 지우는 동작)", "그의 거짓 믿음이 신체화된 습관이라는 걸 미리 "
     "심어둬야, 5장에서 추천 응답을 ‘의식적으로’ 끄는 행동이 얼마나 큰 결단인지 대비가 선다.", "5장"),
    ("은채의 사소한 걱정과 자동 승인", "‘누구도 직접 생각하지 않는다’는 세계관 명제를 가장 작고 무해한 사례로 먼저 "
     "보여줘, 2~3장에서 노인들의 걱정이 쌓여 재요청이 되는 더 심각한 버전과 규모 대비를 만든다.", "3장"),
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
    {deck.slide_header("복선 · 씨앗과 회수", "1장에 심어서 나중 장에서 거둘 것들",
                        "표의 ‘씨앗’ 열은 1장 안에서 반드시 등장해야 하는 구체적 디테일, ‘회수’는 그게 나중에 의미를 얻는 지점")}
    <table class="cmp">
      <thead><tr><th>1장에 심을 씨앗</th><th>나중에 거두는 의미</th><th>회수 지점</th></tr></thead>
      <tbody>{''.join(rows_html)}</tbody>
    </table>
    """
    deck.add_slide("foreshadowing", "복선", body, dark=True)


DETAILS = [
    "파란 자막의 질감: 깜빡이지 않고 그냥 ‘이미 거기 있던 것’처럼 나타난다 — 알림음도, 등장 애니메이션도 없다.",
    "숫자가 올라가는 소리가 없다는 사실 자체: 조용함이 쾌적함이 아니라 ‘소거’처럼 느껴지게.",
    "신발 속 모래, 파도가 모래를 끌어가는 소리, 멀리 갈매기 울음 — 공원의 물리적 질감.",
    "손목 디바이스의 ‘톡, 톡’ 소리 — 승인 제스처가 몸에 밴 습관임을 반복해서 보여줄 것.",
    "아침 햇살이 ‘지나치게 선명한’ 느낌 — 보정된 듯한 쾌적함, 필터링된 완벽함.",
    "은채의 표정 변화: 불안 → 추천 응답 수락 후 ‘무해한 미소’로 바뀌는 그 전환의 빠르기(0.2초)를 체감되게 묘사.",
    "(선택) 멀리 포장마차나 빵집에서 풍기는 달콤한 냄새 한 줄 — 나중(8장)에 돌아보면 소름 돋는 아주 희미한 초코 케익 모티프.",
]


def slide_details(deck):
    items_html = "".join(f"<li>{esc(d)}</li>" for d in DETAILS)
    body = f"""
    {deck.slide_header("묘사에 필요한 사건·디테일 체크리스트",
                        "이 장을 실제로 쓸 때 빠뜨리면 안 되는 감각 디테일",
                        "전부 다 쓸 필요는 없다 — 다만 비트 01·04·08에는 최소 하나씩 들어가야 ‘설명’이 아니라 ‘체험’이 된다")}
    {card('<ul style="margin:0;padding-left:1.2rem;">' + items_html + '</ul>')}
    """
    deck.add_slide("details", "묘사 체크리스트", body)


def slide_sample_openings(deck):
    samples = [
        "히트율은 99.7퍼센트였다. 나머지 0.3퍼센트는, 진우가 알기로는, 존재하지 않는 숫자나 다름없었다.",
        "파도가 모래를 끌어가는 소리 사이로, 누군가의 딜레마 신호가 뜨고 0.2초 뒤에 사라졌다. 사라졌다는 것 말고는, "
        "아무 일도 없었다는 뜻이었다.",
        "은채가 걱정을 꺼내 놓는 데는 삼 초가 걸렸고, 그 걱정이 사라지는 데는 0.2초가 걸렸다. 진우는 그 비율이 "
        "마음에 들었다.",
    ]
    samples_html = "".join(
        card(f"<p style='margin:0;'>{quote(s)}</p>")
        for s in samples
    )
    body = f"""
    {deck.slide_header("샘플 도입부 문장 (3안)", "톤을 잡기 위한 출발점 — 그대로 쓰기보다 다시 쓰는 재료로",
                        "셋 다 ‘숫자’로 문을 여는 방식이다. 숫자 대신 감각으로 여는 4안이 필요하면 다음 라운드에 추가 가능")}
    {samples_html}
    """
    deck.add_slide("samples", "샘플 문장", body, dark=True)


def slide_open_questions(deck):
    questions = [
        ("은채를 재등장시킬 것인가", "이 장에서만 쓰고 버리는 단역으로 둘지, 후반부(7장 ‘응답 없음’)에서 캐시가 꺼진 "
         "순간 다시 마주치는 인물로 재활용할지. 추천: 재활용 — 1장의 무해한 불안과 7장의 무응답을 같은 얼굴로 대비시키면 "
         "울림이 커진다."),
        ("진단 레이어를 얼마나 노출할 것인가", "너무 많이 보여주면 설명적이 되고, 너무 적으면 2장에서 ‘진우가 이런 걸 "
         "볼 수 있는 사람’이라는 복귀가 약해진다. 추천: 1장에서는 숫자 3개(히트율·응답 지연·MISS 비율) 정도로만 제한."),
        ("초코 케익 모티프를 미리 심을 것인가", "8장 결말의 ‘진짜 케익’과 조응시키려면 아주 희미하게(포장마차 냄새 한 줄) "
         "심어두는 편이 효과적이다. 다만 너무 또렷하면 1장에서 독자가 미리 눈치채 버려 2장의 충격이 줄어든다 — "
         "‘문장 하나, 설명 없이’ 원칙을 지킬 것."),
        ("은채의 걱정 내용을 얼마나 구체화할 것인가", "지나치게 구체적이면 이 장이 은채의 이야기가 되어버린다. 한 줄 "
         "정도의 일상적 걱정(발표, 면접 결과 등)으로 제한해 ‘누구나 겪는 작은 불안’의 표본으로만 쓸 것."),
    ]
    q_html = "".join(
        card(f"<strong class='small'>{esc(q)}</strong><p class='small muted' style='margin:0.4rem 0 0;'>{esc(a)}</p>")
        for q, a in questions
    )
    body = f"""
    {deck.slide_header("작가가 정할 것", "추천안은 붙여 두었다 — 작가의 판단이 다르면 그쪽이 맞다", None)}
    <div class="grid grid-2">{q_html}</div>
    """
    deck.add_slide("questions", "작가가 정할 것", body)


def main():
    deck = Deck("1장 · 히트율 99.7% — 심화 기획", THEME, footer=FOOTER)
    slide_overview(deck)
    slide_setting(deck)
    slide_world(deck)
    slide_beats(deck)
    slide_foreshadowing(deck)
    slide_details(deck)
    slide_sample_openings(deck)
    slide_open_questions(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
