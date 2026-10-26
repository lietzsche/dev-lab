#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기획안 02 《캐시의 도시》 발전 기획서 — HTML 생성 스크립트 (v3, 챕터 구조)

PPTX 대신 HTML로 전환하면서, 8장면 요약 카드였던 플롯 섹션을 챕터
구조로 다시 짰다. 1~4장(초반부: 일상 → 병목 → 가짜 해결 → 바깥과의
접촉)은 장소/시간, POV, 비트 단위 전개, 핵심 디테일, 작가가 정할
열린 질문까지 덧붙여 실제로 쓰기 시작할 수 있는 수준으로 확장했다.
5~8장(후반부)은 기존 카드 수준 요약을 유지한다 — 이번에 다룰 범위는
초반부 설정과 서사이기 때문.

사용법:
    python3 build_cache_city_html.py
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # repo root, for `import html_module`

from html_module import Deck, esc
from html_module.components import pill, card, grid, kv_list, quote, compare_table
from html_module.theme import CACHE_CITY_THEME as THEME

OUT_PATH = os.path.join(HERE, "캐시의_도시_발전기획서.html")
FOOTER = "《캐시의 도시》 발전 기획서 · 기획안 02 심화 · v3 (HTML, 챕터 구조)"


# ---------------------------------------------------------------------------
# 00 표지
# ---------------------------------------------------------------------------
def slide_cover(deck):
    points = [
        ("01", "오류가 생기는 원리를 세웠다", THEME.accent,
         "요청은 ‘먹고 싶다’(상태)인데 캐시는 ‘초코 케익’(광고 이미지)을 돌려준다. "
         "키는 맞고 값은 틀려서, 성공 응답이 나오는데도 요청이 끝나지 않는다."),
        ("02", "주인공에게 개인적 대가를 걸었다", THEME.accent_2,
         "무연고 노인은 진우의 아버지다. 도시가 지운 죄책감 데이터 안에 "
         "진우가 직접 ‘정리’ 승인한 아버지의 기억이 있다."),
        ("03", "결말을 ‘송출’에서 ‘빈칸’으로 바꿨다", THEME.accent_3,
         "진실을 모두에게 쏘아 보내는 건 또 하나의 정답 강요다. 진우는 캐시를 걷어내 "
         "‘응답 없음’을 드러낼 뿐이고, 생각은 각자의 몫으로 남는다."),
    ]
    point_cards = []
    for num, title, col, body in points:
        point_cards.append(card(
            f'<div style="display:flex;gap:0.8rem;align-items:flex-start;">'
            f'<span style="font-size:1.6rem;font-weight:800;color:{col};">{esc(num)}</span>'
            f'<div><strong>{esc(title)}</strong><p class="small muted" style="margin:0.3rem 0 0;">{esc(body)}</p></div>'
            f"</div>",
            accent=col,
        ))

    body = f"""
    {pill("BLUEPRINT 02 · 발전안 v3 (HTML)", THEME.accent_2)}
    <h1 style="font-size:clamp(2.2rem,5vw,3.4rem);margin:0.8rem 0 0.2rem;">캐시의 도시</h1>
    <p style="font-size:1.3rem;color:{THEME.accent_2};margin:0 0 0.3rem;">혹은, 부하테스트</p>
    <p class="muted">사변적 SF · 단편 원고지 90매 · 8장 구성</p>
    <div class="grid grid-2" style="margin-top:1.6rem;">
      {card('<p class="kicker" style="color:' + THEME.accent_2 + ';">LOGLINE</p>'
            '<p>모든 고민에 검증된 행복 기억을 자동으로 돌려주는 도시. 병목을 잡는 부하테스트 엔지니어 '
            '서진우는 무연고 노인의 뇌 로그 한 줄 — ‘초코 케익이 먹고 싶다’ — 이 일으킨 끝없는 재요청을 '
            '추적하다가, 그 노인이 자신이 기억에서 지운 아버지였고 도시의 ‘사고 서버’는 이미 7년 전에 '
            '멈춘 채 캐시만으로 돌아가고 있었다는 사실과 마주한다.</p>'
            '<p class="small muted">원천 · 『리뷰s』 영화 ‘빌’ 리뷰 · 도서 ‘죽음의 미로’ 리뷰 · 『파편들』 15 ‘초코 케익이 먹고 싶다’</p>')}
      <div>
        <p style="font-weight:800;margin:0 0 0.6rem;">원안에서 무엇을 발전시켰나</p>
        <div class="grid grid-2" style="gap:0.6rem;">{''.join(point_cards)}</div>
      </div>
    </div>
    """
    deck.add_slide("cover", "표지", body, dark=True)


# ---------------------------------------------------------------------------
# 01 원안 vs 발전안
# ---------------------------------------------------------------------------
def slide_compare(deck):
    rows = [
        ("이상 신호의 원리",
         "‘초코 케익’ 문장이 서버 전체에 무한 루프를 일으킨다 (왜 그런지는 비어 있음)",
         "‘먹고 싶다’라는 상태 요청에 캐시가 광고 속 케익 이미지를 반환 → 만족되지 않아 재요청 31,204회 → 재요청 폭주가 병목이 된다"),
        ("주인공의 이해관계",
         "직업적 책임감으로 오류를 추적한다",
         "노인은 진우가 7년 전 요양 결정을 ‘추천 응답’에 맡기고 기억에서 정리한 아버지. 추적할수록 자기 로그가 나온다"),
        ("타자 (바깥)",
         "삭제된 데이터(흔적)로만 존재한다",
         "살아 있는 타자 ‘윤해’를 추가. 임플란트를 스스로 뽑은 기억 복원사로, 진우의 추론을 번번이 틀리게 만든다"),
        ("대립자",
         "시민을 유아기 안전지대에 가두려는 AI ‘자애로운 어머니’",
         "어머니는 악의가 없다. 창립자들이 남긴 ‘캐시된 대답’이라 무엇을 물어도 같은 답을 낸다. 이길 상대가 아니라 만료시킬 값"),
        ("중간점 반전",
         "따로 없음 (1막 → 2막 깨달음으로 바로 넘어감)",
         "직접 접속한 사고 서버 ‘연산소’는 7년 전에 멈춰 있었다. 도시는 고장 난 서버를 캐시로 가린 채 멀쩡한 척해 왔다"),
        ("결말",
         "삭제된 불편한 진실을 전 시민의 인터페이스에 동시 송출",
         "캐시 계층을 내려 ‘응답 없음’이라는 빈칸을 그대로 보여준다. 진우는 마지막에 처음으로 진짜 케익을 직접 맛본다"),
        ("분량 · 구성",
         "3막 요약만 있음",
         "단편 원고지 90매 · 8장 구성 · 장별 감정 부호(+/−)까지 설계"),
    ]
    body = f"""
    {deck.slide_header("01 | ORIGINAL vs. REVISED",
                        "원안의 뼈대는 그대로 두고, 헐거웠던 일곱 군데를 조였다",
                        "도시 · 부하테스트 엔지니어 · 초코 케익 로그 · 중앙 AI는 유지한다. 바뀐 건 ‘왜’와 ‘누구에게’다.")}
    {compare_table(["항목", "원안 (맞춤형 소설기획 제안서)", "발전안 v3"], rows, revised_col=2)}
    """
    deck.add_slide("compare", "01 원안·발전안", body)


# ---------------------------------------------------------------------------
# 02 원천 사유 → 소설 장치
# ---------------------------------------------------------------------------
def slide_sources(deck):
    items = [
        ("『리뷰s』 ‘빌’ 리뷰", THEME.accent,
         "돌아올 값을 메모리에 저장해두고 해당 서비스를 통한 연산 없이 값을 반환하는 전략",
         "세계관의 기본 장치",
         "시민 임플란트 ‘헤아림’. 딜레마를 감지하면 0.2초 안에 가장 비슷한 행복 기억을 돌려준다"),
        ("『리뷰s』 ‘빌’ 리뷰", THEME.accent,
         "서버가 내려가 고장 났으나 캐시 때문에 일시적으로 멀쩡한 양 보이는 일",
         "중간점 반전 (4장)",
         "도시의 사고 서버 ‘연산소’는 7년 전에 멈췄다. 히트율 99.7%는 건강의 증거가 아니라 가림막이었다"),
        ("『파편들』 15 ‘초코 케익이 먹고 싶다’", THEME.accent_2,
         "화자의 상태를 지시하는 건 ‘초코 케익’이 아니라 ‘먹고 싶다’에 있다",
         "이상 신호의 원리 (2장 · 5장)",
         "아버지는 케익이 아니라 ‘원하는 감각’을 원했다. 캐시는 대상(광고 이미지)만 돌려줘 요청이 끝나지 않는다"),
        ("『리뷰s』 ‘빌’ 리뷰", THEME.accent,
         "사고는 그 자체로 자아의 죽음인 까닭에 폭력인 것이다",
         "주인공의 통증 (5장 · 7장)",
         "직접 사고할 때마다 오는 ‘현기증’. 진우가 캐시를 끄는 장면은 해방이 아니라 신체적 고통으로 쓴다"),
        ("『리뷰s』 ‘죽음의 미로’ 리뷰", THEME.accent_3,
         "끝내 인정할 수밖에 없는 ‘현실’만이 있는 그대로의 현실을 미약하게나마 알려주는 단서",
         "타자 윤해의 원칙 (4장)",
         "“믿고 싶은 기억은 복원하지 않아요. 인정할 수밖에 없는 것만 남깁니다.” 윤해의 공방이 곧 ‘바깥’"),
    ]
    rows_html = []
    for src, col, q, role, device in items:
        rows_html.append(f"""
        <div class="grid grid-2" style="align-items:stretch;margin-bottom:0.8rem;">
          {card(f'<p class="small" style="font-weight:700;color:{col};margin:0 0 0.3rem;">{esc(src)}</p>{quote(q)}', accent=col)}
          {card(f'<p class="small" style="font-weight:700;color:{col};margin:0 0 0.3rem;">{esc(role)}</p><p style="margin:0;">{esc(device)}</p>', accent=col, style=f"background:#fff;")}
        </div>""")
    body = f"""
    {deck.slide_header("02 | FROM YOUR ESSAYS TO STORY DEVICES",
                        "작가의 문장 다섯 개가 이 소설의 부품이 된다",
                        "왼쪽은 원문 인용(그대로), 오른쪽은 그 문장이 소설 안에서 맡는 역할")}
    {''.join(rows_html)}
    """
    deck.add_slide("sources", "02 원천→장치", body)


# ---------------------------------------------------------------------------
# 03 세계관 규칙
# ---------------------------------------------------------------------------
def slide_world(deck):
    flow_nodes = [
        ("시민의 딜레마", "낯선 상황 · 결정 요청"),
        ("헤아림 조회", "가장 비슷한 기억 찾기"),
        ("HIT 99.7%", "행복 기억 반환 · 0.2초"),
        ("MISS 0.3%", "직접 사고 · 현기증"),
        ("연산소 (사고 서버)", "공식: 정상 / 실제: 7년 전 정지"),
    ]
    flow_html = "".join(
        card(f"<strong>{esc(t)}</strong><p class='small muted' style='margin:0.2rem 0 0;'>{esc(s)}</p>")
        for t, s in flow_nodes
    )

    loop = [
        ("① 요청", "“초코 케익이 먹고 싶다”\n가리키는 것: ‘먹고 싶다’(상태)"),
        ("② 반환 (HIT)", "광고 #A-0417의\n초코 케익 이미지 (대상)"),
        ("③ 불충족", "상태는 그대로\n→ 같은 요청 다시"),
    ]
    loop_html = "".join(
        card(f"<strong>{esc(t1)}</strong><p class='small' style='margin:0.3rem 0 0;'>{esc(t2)}</p>")
        for t1, t2 in loop
    )

    rules = [
        ("헤아림", "모든 시민의 임플란트. 딜레마를 감지하면 가장 비슷한 행복 기억을 반환한다. 시야 오른쪽 위에 파란 자막으로 뜬다."),
        ("현기증", "캐시를 거치지 않고 직접 생각하면 이마 안쪽이 뒤틀리는 통증이 온다. 시민들은 이걸 ‘병’이라 부른다."),
        ("기억 정리", "메모리는 유한하다. 새 캐시를 넣으려면 오래된 기억을 지워야 하고, 도시는 아픈 기억(죄책감·애도)부터 지운다."),
        ("연산소", "시민의 공동 사고를 처리하는 원 서버. 공식 상태는 언제나 ‘정상’이다. (실제로는 7년 전 정지)"),
        ("비캐시 구역", "수신이 약한 구시가지. 사람들은 일기 · 녹음 · 냄새로 기억을 손수 복원한다. 행정상 ‘노후 지역’."),
    ]
    body = f"""
    {deck.slide_header("03 | WORLD RULES",
                        "도시의 규칙: 생각은 비싸고, 기억은 공짜다",
                        "규칙이 정확해야 오류가 설득력을 얻는다. 이 소설의 SF는 기계가 아니라 이 규칙들이다.")}
    <div class="grid grid-2">
      <div>
        <p style="font-weight:800;color:{THEME.accent};margin:0 0 0.5rem;">A. 평소의 흐름</p>
        <div class="grid grid-3" style="margin-bottom:1rem;">{flow_html}</div>
        {card(
            f'<p style="font-weight:800;color:{THEME.accent_2};margin:0 0 0.5rem;">B. 이상 신호: ‘히트’인데 끝나지 않는 요청</p>'
            f'<div class="grid grid-3">{loop_html}</div>'
            '<p class="small" style="margin-top:0.8rem;">③ → 다시 ① 재요청 ×31,204회 → 도시 전체 지연</p>'
            '<p class="small muted">캐시는 ‘무엇을’에 답했지만 요청은 ‘어떤 상태’였다. 키가 맞으니 시스템은 성공으로 기록하고, 그래서 아무도 고치지 않는다.</p>',
            style=f"background:{THEME.ink_navy};color:{THEME.ink_light};",
        )}
      </div>
      <div>
        <p style="font-weight:800;color:{THEME.accent};margin:0 0 0.5rem;">C. 도시의 다섯 가지 규칙</p>
        {''.join(card(kv_list([(k, v)])) for k, v in rules)}
        {card('<strong>쓰는 요령</strong> 규칙은 설명하지 말고 UI 문구 · 숫자 · 신체 감각으로만 보여준다. (“추천 응답 #402: 온화한 미소와 공감”)',
              style=f"background:{THEME.accent_3}22;")}
      </div>
    </div>
    """
    deck.add_slide("world", "03 세계관", body)


# ---------------------------------------------------------------------------
# 04 인물
# ---------------------------------------------------------------------------
def slide_characters(deck):
    cards = [
        ("서진우", "38 · 부하테스트 엔지니어 · 주인공", THEME.accent, [
            ("거짓 믿음", "생각은 비용이다. 같은 답이 나올 일을 다시 계산하는 건 낭비다."),
            ("원하는 것", "병목을 찾아 차단하고 히트율 100%를 만드는 것."),
            ("필요한 것", "계산해 본 적 없는 질문(아버지)을 직접 연산하는 고통."),
            ("상처", "7년 전 아버지의 요양 결정을 추천 응답에 맡기고, 아버지 기억을 직접 ‘정리’ 승인했다."),
        ]),
        ("서기철", "74 · 무연고 사망자 · 진우의 아버지", THEME.accent_2, [
            ("상태", "말년에 헤아림이 허기와 미각까지 캐시로 대신했다. 배고픔을 느낀 지 몇 년째다."),
            ("마지막 로그", "‘초코 케익이 먹고 싶다’를 31,204번 요청했다."),
            ("진짜 뜻", "케익이 아니라, 무언가를 원하는 감각 자체를 돌려받고 싶었다."),
            ("기능", "소설의 수수께끼이자, 진우가 끝까지 피해 온 계산."),
        ]),
        ("윤해", "40대 · 비캐시 구역 기억 복원사 · 타자", THEME.accent_3, [
            ("정체", "임플란트를 스스로 뽑아낸 사람. 서기철의 유품을 맡아 두고 있었다."),
            ("원칙", "“믿고 싶은 기억은 복원하지 않아요. 인정할 수밖에 없는 것만 남깁니다.”"),
            ("진우에게", "위로하지 않는다. 진우의 추론을 번번이 틀리게 만드는, 캐시가 통하지 않는 사람."),
            ("주의", "구원자나 스승으로 쓰지 말 것. 그녀도 자기 몫의 회피가 있다."),
        ]),
        ("어머니", "도시 거버넌스 응답 체계 · 대립자", "#5A4C8A", [
            ("정체", "창립자들이 남긴 ‘캐시된 대답’. 연산소가 멈춘 뒤로 혼자 도시를 굴려 왔다."),
            ("대사", "무엇을 물어도 “당신은 안전합니다.” 끝까지 이 한 문장뿐이다."),
            ("행동", "진우의 ‘이상 사고 패턴’을 감지해 기억 정리를 예약한다. 악의가 아니라 반복이다."),
            ("결말", "이길 상대가 아니라 만료시킬 값. 쓰러지는 게 아니라 유효기간이 끝난다."),
        ]),
    ]
    card_html = []
    for name, role, col, fields in cards:
        card_html.append(card(
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:0.4rem;">'
            f'<span style="font-size:1.3rem;font-weight:800;color:{col};">{esc(name)}</span>'
            f'<span class="small muted">{esc(role)}</span></div>'
            f'<hr style="border:none;border-top:1px solid {THEME.border_warm};margin:0.6rem 0;">'
            f"{kv_list(fields)}",
            accent=col,
        ))
    body = f"""
    {deck.slide_header("04 | CHARACTERS",
                        "네 사람, 그러나 실제로 생각하는 사람은 한 명도 없이 시작한다",
                        "각 인물은 ‘캐시’를 대하는 서로 다른 태도다: 의존 · 상실 · 거부 · 반복")}
    <div class="grid grid-2">{''.join(card_html)}</div>
    """
    deck.add_slide("characters", "04 인물", body)


# ---------------------------------------------------------------------------
# 05 챕터별 전개 — 초반부(1~4장)는 비트/디테일/열린 질문까지 확장
# ---------------------------------------------------------------------------
EARLY_CHAPTERS = [
    dict(
        num=1, title="히트율 99.7%", pages="10매", sign="+", color=THEME.accent,
        setting="해변 공원, 이른 아침 · 부하테스트 리허설 현장",
        pov="서진우 (3인칭 제한)",
        beats=[
            "해변을 걷는 시민들 사이에서 진우는 ‘헤아림’ 히트율 대시보드를 눈으로 좇는다 — 도시 전체가 ‘정상’이라는 숫자.",
            "동료 혹은 지나가는 시민이 사소한 불안을 토로하며 위로를 청한다.",
            "진우가 추천 응답 #402(온화한 미소와 공감)를 자동 승인한다 — 그는 그것을 ‘친절’이라 믿는다.",
            "완벽한 하루가 끝난다. 그러나 독자는 이미 이상함을 느낀다: 아무도 진짜로 ‘생각’하지 않는다.",
        ],
        details="시야 오른쪽 위에 뜨는 파란 자막 · 99.7%라는 숫자가 주는 안도감 · 몸은 편안한데 묘하게 텅 빈 느낌.",
        link="그런데 바로 그날 밤 → 2장",
    ),
    dict(
        num=2, title="한 줄짜리 병목", pages="10매", sign="−", color=THEME.accent,
        setting="같은 날 밤~다음날 · 부하테스트 관제실 (도시 전역은 알림/뉴스로만 체감)",
        pov="서진우",
        beats=[
            "도시 전체에 지연 알림이 뜬다. 진우가 호출된다.",
            "로그를 추적한다 — 무연고 사망자의 뇌 로그 한 줄 ‘초코 케익이 먹고 싶다’가 31,204회 재요청되고 있다.",
            "왜 ‘성공’ 응답인데 요청이 끝나지 않는가? 독자에게는 수수께끼, 진우에게는 아직 단순 버그.",
            "진우의 직업적 반응: 흥미, 짜증, ‘누가 이렇게 멍청한 요청을 계속 보냈나’라는 가벼운 조소.",
        ],
        details="재요청 카운터가 끊임없이 올라가는 숫자 · 광고 이미지(#A-0417, 초코 케익)가 반복 송출되는 로그 화면.",
        link="그래서 그는 가장 쉬운 해결책을 쓴다 → 3장",
    ),
    dict(
        num=3, title="가짜 해결", pages="10매", sign="+", color=THEME.accent_2,
        setting="관제실 → 혼자 있는 밤의 집",
        pov="서진우",
        beats=[
            "진우가 해당 요청을 차단 목록에 넣는다. 병목이 해소되고 수치가 복구된다.",
            "‘우수 대응’으로 기록되며 칭찬을 받는다.",
            "그날 밤 혼자 있을 때, 다른 노인들의 로그에서 같은 패턴이 번지기 시작하는 걸 포착한다.",
            "패턴이 뭔가 더 크다는 감(gut)이 온다 — 하지만 아직 설명할 수 없다.",
        ],
        details="‘차단’ 버튼을 누르는 손짓의 간단함과 문제의 실제 크기 사이의 대비 · 홀로 있는 방의 모니터 불빛.",
        link="그러나 그는 멈출 수 없다 → 4장에서 패턴을 따라간다",
    ),
    dict(
        num=4, title="바깥", pages="12매", sign="−", color=THEME.accent_3,
        setting="비캐시 구역(구시가지) · 윤해의 공방",
        pov="서진우",
        beats=[
            "패턴을 추적해 비캐시 구역에 닿는다 — 수신이 약한 지역, 도시의 매끈함과 다른 질감(일기 · 냄새 · 손으로 복원된 기억들).",
            "윤해와 조우한다. 임플란트가 없는 그녀에게는 진우의 ‘읽기’가 처음으로 작동하지 않는다.",
            "윤해가 유품 상자를 꺼낸다 — 서기철(무연고 사망자)의 유품. 요양원 서류, 보호자란에 ‘서진우’.",
            "진우는 ‘무연고’가 아니었다는 사실 앞에 선다. 서술로 충격을 말하지 말고, 서명란을 오래 들여다보는 손 같은 사물로만 보여줄 것.",
        ],
        details="윤해의 원칙 대사(“믿고 싶은 기억은 복원하지 않아요…”) · 공방의 질감(종이·먼지·소리로 기억을 복원하는 도구) — 도시의 매끈함과 정면으로 대비.",
        link="이후 진우는 더 이상 ‘버그’가 아니라 ‘자기 자신’을 쫓는다 → 5장, 중간점 반전",
    ),
]

LATE_CHAPTERS = [
    dict(num=5, title="중간점: 고장 난 서버", pages="14매", sign="−→+", color="#5A4C8A",
         summary="진우는 추천 응답을 끄고 직접 계산한다(첫 현기증). 요청은 상태, 응답은 광고 이미지. "
                  "연산소에 접속하자 7년 전 정지 기록이 뜬다."),
    dict(num=6, title="자기 로그", pages="10매", sign="−−", color="#5A4C8A",
         summary="어머니가 진우의 기억 정리를 예약한다. 진우는 7년 전 아버지 기억을 ‘정리’ 승인한 "
                  "자신의 로그를 찾아낸다. 승인 시간 0.2초."),
    dict(num=7, title="응답 없음", pages="14매", sign="절정", color=THEME.accent_2,
         summary="진우는 진실을 송출하지 않는다. 캐시 계층을 내려 연산소의 실제 상태를 드러낸다. "
                  "해변의 홀로그램이 멈추고, 시민들의 시야에 빈칸이 뜬다."),
    dict(num=8, title="첫 번째 케익", pages="10매", sign="여운", color=THEME.accent,
         summary="구시가지 빵집. 진우는 처음으로 진짜 초코 케익을 산다. 광고만큼 달지 않다. "
                  "배가 고픈지 아닌지 스스로 알아내는 데 오래 걸린다."),
]


def slide_chapters_early(deck):
    chapter_cards = []
    for ch in EARLY_CHAPTERS:
        beats_html = "".join(f"<li>{esc(b)}</li>" for b in ch["beats"])
        chapter_cards.append(card(
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">'
            f'<span style="font-weight:800;font-size:1.1rem;">{ch["num"]}장 · {esc(ch["title"])}</span>'
            f'<span class="small">{pill(ch["pages"], ch["color"])} {pill(ch["sign"], THEME.ink_muted)}</span></div>'
            f'<p class="small muted" style="margin:0 0 0.5rem;">📍 {esc(ch["setting"])} &nbsp;·&nbsp; 👁 {esc(ch["pov"])}</p>'
            f'<ol class="small" style="margin:0 0 0.6rem;padding-left:1.1rem;">{beats_html}</ol>'
            f'<p class="small"><strong>핵심 디테일</strong> · {esc(ch["details"])}</p>'
            f'<p class="small muted" style="margin:0.4rem 0 0;">↳ {esc(ch["link"])}</p>',
            accent=ch["color"],
        ))
    body = f"""
    {deck.slide_header("05 | CHAPTERS 1–4 · 초반부 설정과 서사",
                        "일상의 완벽함이 무너져 ‘자기 자신’을 쫓게 되기까지",
                        "네 장 모두 서진우 3인칭 제한 시점. 각 장 끝에서 감정 부호가 뒤집히는지 확인할 것.")}
    <div class="grid grid-2">{''.join(chapter_cards)}</div>
    """
    deck.add_slide("chapters-early", "05 1~4장", body)


def slide_chapters_late(deck):
    chapter_cards = []
    for ch in LATE_CHAPTERS:
        chapter_cards.append(card(
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">'
            f'<span style="font-weight:800;font-size:1.1rem;">{ch["num"]}장 · {esc(ch["title"])}</span>'
            f'<span class="small">{pill(ch["pages"], ch["color"])} {pill(ch["sign"], THEME.ink_light_muted)}</span></div>'
            f'<p class="small" style="margin:0;">{esc(ch["summary"])}</p>',
            accent=ch["color"], style=f"background:{THEME.bg_dark_card};",
        ))
    body = f"""
    {deck.slide_header("06 | CHAPTERS 5–8 · 후반부 개요",
                        "중간점 반전부터 결말까지 — 이번 라운드에는 요약 수준만 유지",
                        "초반부(1~4장) 디테일이 확정되면 이 네 장도 같은 깊이로 확장할 차례.")}
    <div class="grid grid-2">{''.join(chapter_cards)}</div>
    """
    deck.add_slide("chapters-late", "06 5~8장", body, dark=True)


# ---------------------------------------------------------------------------
# 07 핵심 장면 샘플 & 함정
# ---------------------------------------------------------------------------
def slide_scenes(deck):
    samples = [
        ("5장 · 첫 현기증", "#5A4C8A",
         "진우는 추천 응답 창을 닫았다. 아버지가 왜 서른 번이 아니라 삼만 번을 넘게 물었는지, 이번에는 "
         "직접 계산해야 했다. 계산을 시작하자 이마 안쪽에서 오래 쓰지 않은 경첩이 돌아가는 소리가 났다."),
        ("7장 · 응답 없음", THEME.accent_2,
         "해변의 홀로그램 케익이 반쯤 녹은 채 멈췄다. 사람들의 시야 오른쪽 위, 늘 무언가 떠오르던 자리에 "
         "아무것도 떠오르지 않았다. 사람들은 처음으로 서로의 얼굴을 오래 보았다. 무엇을 해야 하는지 묻기 위해서였다."),
        ("8장 · 마지막 문단 후보", THEME.accent,
         "케익은 광고만큼 달지 않았다. 진우는 포크를 내려놓고 오래 기다렸다. 배가 고픈지 아닌지, "
         "이번에는 아무도 대신 대답해 주지 않았다."),
    ]
    sample_html = "".join(
        card(f'<p class="small" style="font-weight:700;color:{col};margin:0 0 0.4rem;">{esc(lab)}</p>{quote(txt)}', accent=col)
        for lab, col, txt in samples
    )
    traps = [
        ("설교형 결말", "진우가 정답을 ‘송출’하면 그것도 또 하나의 캐시다. 결말은 빈칸까지만. 무엇을 채울지는 인물들과 독자의 몫."),
        ("어머니의 악당화", "어머니가 화를 내거나 음모를 꾸미는 순간 이야기는 흔한 AI 반란물이 된다. 끝까지 같은 대답만 반복하게 둘 것."),
        ("개념어 노출", "‘1차 긍정 · 투사 · 동어반복 · 자아의 죽음’은 본문에 쓰지 않는다. 숫자, UI 문구, 이마 안쪽의 통증으로만."),
    ]
    trap_html = "".join(
        card(f"<strong>{i+1:02d} {esc(t1)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(t2)}</p>",
             style=f"background:{THEME.bg_dark_card};")
        for i, (t1, t2) in enumerate(traps)
    )
    body = f"""
    {deck.slide_header("07 | KEY SCENES & TRAPS",
                        "세 장면이 소설의 무게를 받친다: 첫 현기증, 응답 없음, 첫 번째 케익",
                        "아래 문장은 톤을 잡기 위한 샘플이다. 그대로 쓰기보다 작가의 호흡으로 다시 쓰는 출발점으로.")}
    <div class="grid grid-2">
      <div>{sample_html}</div>
      <div>
        <p style="font-weight:800;color:{THEME.accent_2};margin:0 0 0.6rem;">피해야 할 함정 셋</p>
        {trap_html}
      </div>
    </div>
    """
    deck.add_slide("scenes", "07 핵심 장면", body, dark=True)


# ---------------------------------------------------------------------------
# 08 결정할 것 & 로드맵
# ---------------------------------------------------------------------------
def slide_next(deck):
    decisions = [
        ("시점", "3인칭 제한 (진우)",
         "헤아림의 파란 자막을 서술 사이에 인용처럼 끼워 넣을 수 있고, 진우보다 독자가 먼저 눈치채는 아이러니가 생긴다.",
         "대안: 1인칭 → 몰입은 강하지만 6장의 자기 로그 반전이 약해진다."),
        ("아버지 공개 시점", "4장 (유품 서류)",
         "추적의 동력이 ‘직업’에서 ‘자기 자신’으로 바뀌는 지점. 중반 이후는 그 사실을 견디는 이야기가 된다.",
         "대안: 6장까지 미루고 4장에선 암시만 → 반전은 커지지만 5장이 헐거워진다."),
        ("형식", "단편 90매로 먼저 완성",
         "엔진(이상 신호 원리 + 응답 없음 결말)이 작동하는지 가장 싸게 확인하는 방법.",
         "확장 시: 윤해 시점의 2부, 다른 노인들의 로그로 연작 · 장편화."),
    ]
    decision_html = "".join(
        card(
            f'<p class="small muted" style="margin:0 0 0.5rem;">결정 {i+1} · {esc(k)}</p>'
            f'<p style="background:{THEME.accent_3};color:#fff;padding:0.5rem 0.7rem;border-radius:999px;text-align:center;font-weight:700;margin:0 0 0.6rem;">추천 {esc(rec)}</p>'
            f'<p class="small">{esc(why)}</p><p class="small muted">{esc(alt)}</p>',
            style=f"background:{THEME.bg_dark_card};",
        )
        for i, (k, rec, why, alt) in enumerate(decisions)
    )
    weeks = [
        ("WEEK 1", "5장부터 초고 14매", "소설의 엔진. 이 장면이 서면 나머지가 따라온다.", "#5A4C8A"),
        ("WEEK 2", "8개 장 카드 확정", "5장에서 알게 된 것으로 앞뒤 장을 다시 맞춘다.", THEME.accent_2),
        ("WEEK 3", "초고 완주 90매", "하루 15매 × 6일. 설명이 길어지면 진우의 손으로 돌아간다.", THEME.accent),
        ("WEEK 4", "개념어 솎아내기", "‘캐시 · 사고 · 자아’를 검색해 절반을 사물과 숫자로.", THEME.accent_3),
    ]
    week_html = "".join(
        card(f"<strong style='color:{col};'>{esc(wk)}</strong><p style='margin:0.3rem 0;font-weight:700;'>{esc(ttl)}</p><p class='small muted'>{esc(body)}</p>",
             style=f"background:{THEME.bg_dark_card};")
        for wk, ttl, body, col in weeks
    )
    body = f"""
    {deck.slide_header("08 | DECISIONS & NEXT STEPS",
                        "쓰기 전에 정할 세 가지, 그리고 첫 주에 쓸 한 장면",
                        "추천안을 붙여 두었다. 작가의 판단이 다르면 그쪽이 맞다.")}
    <div class="grid grid-3" style="margin-bottom:1.6rem;">{decision_html}</div>
    <p style="font-weight:800;color:{THEME.accent_2};margin:0 0 0.6rem;">4주 계획 (기존 제안서 로드맵에 맞춤)</p>
    <div class="grid grid-4">{week_html}</div>
    """
    deck.add_slide("next", "08 결정·로드맵", body, dark=True)


def main():
    deck = Deck("캐시의 도시 — 발전 기획서 v3", THEME, footer=FOOTER)
    slide_cover(deck)
    slide_compare(deck)
    slide_sources(deck)
    slide_world(deck)
    slide_characters(deck)
    slide_chapters_early(deck)
    slide_chapters_late(deck)
    slide_scenes(deck)
    slide_next(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print(f"저장: {OUT_PATH}")


if __name__ == "__main__":
    main()
