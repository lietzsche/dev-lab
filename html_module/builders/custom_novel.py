#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
작가 비문학 아카이브(파편들 · 리뷰s · ETC) 기반 맞춤형 소설 기획 제안서
— HTML 생성 스크립트

PPTX 버전(ppt_module/builders/custom_novel.py)의 전체 내용을 그대로 옮긴
HTML 포트. 키워드 차트/장르 매트릭스처럼 Pillow로 그리던 이미지는 표/그리드
형태의 순수 HTML로 대체했다 — 이미지 생성 파이프라인 없이도 같은 정보를
전달한다.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, PROJECT_ROOT)

from html_module import Deck, esc
from html_module.components import pill, card, kv_list, quote
from html_module.theme import CUSTOM_NOVEL_THEME as THEME

OUT_PATH = os.path.join(PROJECT_ROOT, "맞춤형_소설기획_제안서.html")
FOOTER = "CUSTOM FICTION BLUEPRINT · 비문학 아카이브(파편들 · 리뷰s · ETC) 기반 맞춤형 소설 기획서"


def slide_cover(deck):
    cards = [
        ("ARCHIVE 01", "작가 사유 지형도", "157쪽·27만 자 핵심 키워드와 3대 갈등 엔진"),
        ("ARCHIVE 02", "최적 장르 & 계보", "심리 미스터리 · 사변 SF · 블랙코미디 · 드라마"),
        ("BLUEPRINT 03", "맞춤 소설 기획 4선", "로그라인 · 입체적 인물 · 3막 플롯 완벽 설계"),
        ("CLINIC 04", "비문학→소설 문체 전환", "논증을 장면과 사물로 번역하는 실전 공식"),
    ]
    card_html = "".join(
        card(f"<p class='small' style='color:{THEME.accent_2};font-weight:800;margin:0;'>{esc(tag)}</p>"
             f"<p style='font-weight:800;margin:0.3rem 0;'>{esc(title)}</p>"
             f"<p class='small muted' style='margin:0;'>{esc(desc)}</p>")
        for tag, title, desc in cards
    )
    body = f"""
    {pill("ARCHIVE-DRIVEN FICTION PROPOSAL", THEME.accent_2)}
    <h1 style="font-size:clamp(2rem,4.6vw,3rem);margin:0.8rem 0 0.3rem;">비문학의 사유에서 소설의 서사로</h1>
    <p class="muted" style="max-width:48rem;">『파편들』(67p) · 『리뷰s』(86p) · 『ETC』(4p) 심층 텍스트 분석을 통해
    당신의 고유한 철학적 문제의식을 4편의 소설 기획안으로 설계하다</p>
    <div class="grid grid-4" style="margin-top:1.8rem;">{card_html}</div>
    """
    deck.add_slide("cover", "표지", body, dark=True)


def slide_corpus_analysis(deck):
    keywords = [
        ("상상 (Imagination)", 263, "가설 설정과 위험 예견의 시뮬레이션"),
        ("관념 (Idea/Concept)", 228, "과잉 관념론 비판 및 기호의 연산"),
        ("필연 (Necessity)", 223, "우연을 배제한 인과적 사슬과 법칙"),
        ("이미지 (Image)", 217, "개념을 대체한 자기애적 거울상 비판"),
        ("추론 (Inference)", 190, "상상을 현실 인식과 타자로 잇는 다리"),
        ("자아 (Ego/Self-Image)", 184, "비대해지려는 자기애적 방어기제"),
        ("유효성 (Validity)", 150, "현실과 허구를 판가름하는 작동 기준"),
        ("동일시 (Identification)", 118, "수동적 이입 vs 능동적 역량 학습"),
        ("투사 (Projection)", 114, "원하는 것만 보려는 소원 성취형 망상"),
        ("허구 · 기호 (Fiction/Sign)", 111, "법칙에 도달하기 위한 필수 매개물"),
        ("도피 (Escape)", 86, "도피하고 있다는 사실 자체에 대한 도피"),
        ("흉터 · 죄책감 (Scar/Guilt)", 71, "병렬 시간의 근원이자 현실 교정의 출발점"),
    ]
    max_val = keywords[0][1]
    rows_html = []
    for label, val, desc in keywords:
        bar_w = round(val / max_val * 100)
        rows_html.append(f"""
        <div style="display:grid;grid-template-columns:9rem 1fr 16rem;gap:0.6rem;align-items:center;padding:0.25rem 0;">
          <span class="small" style="font-weight:700;">{esc(label)}</span>
          <div style="background:{THEME.bg_cream};border-radius:0.3rem;overflow:hidden;">
            <div style="width:{bar_w}%;background:{THEME.accent};color:#fff;font-size:0.72rem;font-weight:700;padding:0.2rem 0.4rem;white-space:nowrap;">{val}회</div>
          </div>
          <span class="small muted">{esc(desc)}</span>
        </div>""")

    docs = [
        ("『파편들.pdf』 (67쪽 · 4개 시즌 철학 에세이)", "소설의 ‘세계관 법칙’과 ‘인식론적 뼈대’를 제공하는 원천",
         "시즌1(PROJECTION) ~ 시즌4(HOW)를 관통하며 ‘투사·자기애’에서 ‘기호·타자·필연의 여백’으로 나아가는 사유의 궤적. "
         "‘가로등 아래서 열쇠 찾기’, ‘초코 케익 기호학’, ‘1+1=2 학자 vs 1+1=3 카피라이터’ 등 소설적 우화가 다수 내장됨.", THEME.accent),
        ("『리뷰s.pdf』 (86쪽 · 영화·드라마·도서·전시 비평 25편)", "인물의 ‘방어기제’와 ‘서사적 역설’을 해부하는 캐릭터 실험실",
         "<셔터 아일랜드>, <부고니아>, <빌>, <지옥 2>, <그대들은 어떻게 살 것인가>, <더 에이트 쇼> 등 서사물의 구조적 빈틈과 "
         "인물 심리를 날카롭게 해부. ‘진실이기를 원함 vs 진실임직함’, ‘서버 부하테스트로서의 사고’, ‘병렬 시간의 흉터’ 등 "
         "독창적인 서사 분석틀 보유.", THEME.accent_3),
        ("『ETC.pdf』 (4쪽 · 고밀도 아포리즘 & 창작 단상)", "시대를 겨냥한 ‘블랙코미디적 풍자’와 ‘윤리적 기준점’",
         "신격화된 개인의 시대, 비대한 자아를 투사하는 ‘꿈꾸는 응석받이(과잉 관념론자)’에 대한 매서운 비판. "
         "“할 수 있는 자는 행한다, 할 수 없는 자는 ‘순위 매긴다’”, “상상이 추론이 되는 건 ‘죄책감’을 통해서다” 등 강렬한 아포리즘.", THEME.accent_2),
    ]
    doc_html = "".join(
        card(f"<strong class='small'>{esc(t)}</strong><p class='small' style='color:{c};font-weight:700;margin:0.3rem 0;'>{esc(s)}</p>"
             f"<p class='small muted' style='margin:0;'>{esc(b)}</p>", accent=c)
        for t, s, b, c in docs
    )
    body = f"""
    {deck.slide_header("01 | WRITER'S CORPUS DIAGNOSIS (총 157쪽 · 약 27만 자 분석)",
                        "당신의 비문학 아카이브는 이미 ‘인식론적 서사’의 거대한 원석이다",
                        "세 권의 텍스트에서 가장 집요하게 반복되는 상위 12개 개념어는 곧 당신이 소설로 탐구해야 할 주제의식이다")}
    <div class="grid grid-2">
      {card('<p style="font-weight:800;margin:0 0 0.6rem;">작성 원고 3종 핵심 개념어 출현 빈도 Top 12 (실제 텍스트 집계)</p>' + ''.join(rows_html))}
      <div class="grid" style="gap:0.6rem;">
        {doc_html}
        {card('<p class="small" style="color:' + THEME.accent_2 + ';font-weight:700;margin:0 0 0.3rem;">작가 자신의 문장이 이미 예고한 다음 종착지 (『파편들』 마지막 문장)</p>'
              + quote("필연의 여백에서, 필연에 대한 충분한 추구와 다다름을 동반하는 바로 그 여백에서 우리는 예의 필연을 배치할 수 있는 발생적 자유, 이를테면 창작에의 정교하고 정확한 허구에 마침내 다다를 수도 있으리라."),
              style=f"background:{THEME.ink_navy};color:{THEME.ink_light};")}
      </div>
    </div>
    """
    deck.add_slide("corpus", "01 코퍼스 진단", body)


def slide_conflict_engines(deck):
    engines = [
        ("ENGINE 01 | 인식론적 아이러니", "투사(Projection) vs 추론(Inference)",
         "‘진실이기를 원함’에 갇힌 인물이 ‘진실임직함’의 벽에 부딪히다",
         ["비문학 원천: 『리뷰s』 <부고니아>, <셔터 아일랜드>, 『파편들』 시즌1",
          "작가는 ‘보고 싶은 자아상만 현실에 투사하며 스스로를 선량한 영웅/피해자로 연출하는 방어기제’를 집요하게 폭로한다.",
          "소설적 전환: 자신이 가장 합리적이고 도덕적이라 믿는 주인공(프로파일러·판사·평론가)이 사건을 추적할수록, 자신이 세운 "
          "가설이 실은 자신의 치부를 가리기 위한 ‘소원 성취형 망상’이었음을 스스로의 논증으로 입증하게 되는 서사."],
         "핵심 캐릭터: 자기 기만에 빠진 ‘신뢰할 수 없는 엘리트 화자’", THEME.accent),
        ("ENGINE 02 | 기호와 권위의 풍자", "이미지의 권위 vs 필연의 사슬",
         "‘순위 매기는 자들’의 가짜 해상도와 단독자의 필연적 검증",
         ["비문학 원천: 『ETC』 <순위>, 『파편들』 시즌4 <맥락 운동성>, <더 에이트 쇼>",
          "“할 수 있는 자는 행하고, 할 수 없는 자는 순위 매긴다.” 엄밀한 ‘1+1=2’의 논증을 사례 수집으로 끌어내리고 ‘1+1=3’의 "
          "낭만적 카피라이팅과 관객의 열광(투표)으로 권위를 얻는 시대에 대한 통찰.",
          "소설적 전환: 대중의 호불호와 이미지 연출로 진실이 결정되는 미디어/학계/플랫폼 공간에서, 절대 타협하지 않는 "
          "물리적·논리적 ‘필연성’이 시스템 전체의 허상을 폭파하는 지적 풍자극."],
         "핵심 캐릭터: 이미지 번역가(카피라이터) vs 고집스러운 논증가", THEME.accent_3),
        ("ENGINE 03 | 실존적 도약과 윤리", "흉터의 병렬 시간 vs 죄책감의 도약",
         "신경증적 쳇바퀴를 부수는 ‘자아의 죽음으로서의 사유’",
         ["비문학 원천: 『리뷰s』 <그대들은 어떻게 살 것인가>, <빌>, <에이리언>, 『파편들』 시즌3",
          "과거의 트라우마(흉터)가 현재와 나란히 흐르며 덜 고통스러운 또 다른 쳇바퀴를 만드는 인물. 상상이 자기중심적 망상에서 "
          "벗어나 ‘추론’이 되는 유일한 열쇠는 오류를 교정하려는 ‘죄책감’과 ‘폭력으로서의 사유’다.",
          "소설적 전환: 안전하고 친숙한 ‘기억 캐시(고정관념)’나 ‘가짜 신비주의’ 속에 숨어 있던 주인공이, 불편하고 이질적인 "
          "‘타자(바깥)’의 고통을 정면으로 환대하며 기존의 자아상이 부서지는 클라이맥스."],
         "핵심 캐릭터: 유년의 병렬 시간에 갇힌 채 타자를 회피하던 인물", "#3A528A"),
    ]
    engine_html = []
    for kicker, title, sub, bullets, char_note, col in engines:
        bullets_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        engine_html.append(card(
            f'<p class="small" style="color:{col};font-weight:800;margin:0 0 0.2rem;">{esc(kicker)}</p>'
            f'<p style="font-weight:800;font-size:1.05rem;margin:0 0 0.2rem;">{esc(title)}</p>'
            f'<p class="small" style="color:{col};font-weight:700;margin:0 0 0.6rem;">{esc(sub)}</p>'
            f'<ul class="small" style="margin:0 0 0.7rem;padding-left:1.1rem;">{bullets_html}</ul>'
            f'<p class="small" style="background:{col}1a;padding:0.4rem 0.6rem;border-radius:0.4rem;margin:0;font-weight:700;text-align:center;">{esc(char_note)}</p>',
            accent=col,
        ))
    body = f"""
    {deck.slide_header("02 | THREE NARRATIVE CONFLICT ENGINES",
                        "작가가 반복해서 파고드는 3가지 철학적 대립축은 소설의 강력한 갈등 엔진이 된다",
                        "비문학에서 ‘개념 대 개념’으로 싸우던 논증을 소설에서는 ‘인물의 욕망 대 현실의 필연’이라는 사건으로 충돌시킨다")}
    <div class="grid grid-3">{''.join(engine_html)}</div>
    """
    deck.add_slide("engines", "02 갈등 엔진", body)


def slide_genre_positioning(deck):
    quads = [
        ("① 심리·인식론적 미스터리", "적합도 96% · 기획안 A",
         ["불신임 화자의 자기 정당화 해체", "‘진실이기를 원함’ vs ‘진실임직함’", "계보: 도스토옙스키 · 셔터 아일랜드"], THEME.accent),
        ("② 사변적 SF · 시스템 우화", "적합도 94% · 기획안 B",
         ["부하테스트·기억 캐시·시뮬레이션", "기호와 프로세스로 작동하는 디스토피아", "계보: 필립 K. 딕 · 테드 창 · 보르헤스"], THEME.accent_3),
        ("③ 지식사회 블랙코미디", "적합도 90% · 기획안 C",
         ["‘순위 매기는 자들’과 가짜 권위 풍자", "학자(논증) vs 카피라이터(이미지 선동)", "계보: 밀란 쿤데라 · 부고니아 · 더 에이트 쇼"], "#3A528A"),
        ("④ 내면 드라마 · 해몽 서사", "적합도 86% · 기획안 D",
         ["유년의 흉터와 병렬 시간의 화해", "나쁜 예감(악몽)을 통한 타자 환대", "계보: 카뮈 · 그대들은 어떻게 살 것인가"], THEME.accent_2),
    ]
    quad_html = "".join(
        card(f"<strong>{esc(t)}</strong>{pill(sub, c)}<ul class='small' style='margin:0.5rem 0 0;padding-left:1.1rem;'>"
             + "".join(f"<li>{esc(b)}</li>" for b in bullets) + "</ul>", accent=c)
        for t, sub, bullets, c in quads
    )
    kinships = [
        ("필립 K. 딕 & 테드 창 | 인식론적·사변적 SF",
         "『리뷰s』에서 직접 인용한 필립 K. 딕의 <발리스>·<죽음의 미로>처럼, ‘우리가 지각하는 현실이 자기애적 투사나 "
         "시뮬레이션이라면 무엇이 진짜 바깥(타자)인가?’를 묻는 사변적 서사와 완벽히 부합한다.", THEME.accent_3),
        ("표도르 도스토옙스키 | 지하생활자의 고백과 죄책감의 심리극",
         "비대한 자아가 스스로의 총명함과 열등감 사이에서 끝없이 자기 정당화의 독백을 쏟아내다, 끝내 ‘죄책감’과 타자의 고통 "
         "앞에서 무너져 내리는 고밀도 심리 추리극(<죄와 벌>, <지하로부터의 수기>)의 결을 지녔다.", THEME.accent),
        ("밀란 쿤데라 & 보르헤스 | 철학적 에세이와 우화의 결합",
         "『파편들』의 ‘사랑이라는 이미지’ 비판이나 ‘우화와 법칙’에 관한 통찰은, 밀란 쿤데라가 ‘키치(Kitsch, 감상적 자기감동)’를 "
         "해부하던 소설 방식이나 보르헤스의 정교한 논리적 미궁과 맞닿아 있다.", "#3A528A"),
    ]
    kinship_html = "".join(
        card(f"<strong class='small'>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(b)}</p>", accent=c)
        for t, b, c in kinships
    )
    body = f"""
    {deck.slide_header("03 | LITERARY LINEAGE & GENRE POSITIONING",
                        "사변적 깊이와 심리 해부력을 극대화할 수 있는 4대 최적 장르와 문학적 계보",
                        "감상적 신파나 우연에 기대는 통속극보다, ‘가설·추론·모순 폭로’가 서사의 동력이 되는 지적인 장르에서 독보적 강점을 발휘한다")}
    <div class="grid grid-2">
      <div>
        <p style="font-weight:800;margin:0 0 0.6rem;">작가 맞춤형 4대 소설 장르 포지셔닝 매트릭스</p>
        <div class="grid grid-2">{quad_html}</div>
      </div>
      <div>
        <p style="font-weight:800;margin:0 0 0.6rem;">작가의 비문학 텍스트와 공명하는 4대 문학·서사 레퍼런스</p>
        {kinship_html}
        {card('<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.5rem;">창작 전략 핵심 제언: ‘착한 힐링물’ 대신 ‘지적인 해부극’을 써라</p>'
              '<ul class="small" style="margin:0;padding-left:1.1rem;">'
              '<li>『파편들』 &lt;사랑이라는 이미지&gt;에서 날카롭게 비판했듯, 모든 갈등을 값싼 위로와 감상으로 봉합하는 서사는 작가의 기질과 정반대다.</li>'
              '<li>독자에게 안락한 동일시(레드 카펫)를 깔아주는 대신, 인물의 얄팍한 명분과 방어기제를 한 겹씩 벗겨내어 끝내 ‘불편하지만 자명한 진실’과 '
              '대면하게 만드는 서사가 당신의 필력을 가장 빛낸다.</li></ul>',
              style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:0.6rem;")}
      </div>
    </div>
    """
    deck.add_slide("genre", "03 장르 포지셔닝", body)


PROPOSALS = [
    dict(
        badge="BLUEPRINT 01", kicker="04 | NOVEL BLUEPRINT 01 (PSYCHOLOGICAL MYSTERY)",
        action_title="[기획안 01] 자기 정당화(투사)의 알리바이를 스스로 해체하는 역추적 심리 스릴러",
        subtitle="‘선량한 인간’이라는 자아상을 지키려다 스스로 만든 추론의 덫에 갇히는 프로파일러의 이야기",
        title="《가로등 아래의 열쇠》 (가제: 가짜 해상도)",
        genre="심리·인식론적 미스터리 / 반(反)탐정 스릴러",
        motifs="『파편들』 P.49 ‘가로등 아래서 열쇠 찾는 남자’ 우화 + 『리뷰s』 <셔터 아일랜드> ‘선량한 인간의 논리’ + <지옥 2> ‘가짜 해상도와 추론’",
        logline="타인의 자기기만과 방어기제를 완벽히 간파해 내는 스타 범죄심리 자문관이, 5년 전 자신이 ‘정의로운 교정’이라 믿고 "
                "종결했던 사건과 동일한 수법의 예고장을 받으면서, 범인을 추적할수록 자신이 쌓아올린 ‘선량한 자아상’의 조작 흔적을 "
                "스스로의 논증으로 폭로하게 되는 역추적 미스터리.",
        char_specs=[
            ("주인공 (한도윤 · 범죄심리학자)", "‘나는 편견 없이 진실만 본다’고 믿는 엘리트. 실은 불편한 진실을 피하려 밝은 "
             "가로등(자신이 통제 가능한 가설) 아래서만 단서를 찾는 인물."),
            ("거짓 믿음 (The Lie)", "“나의 추론은 언제나 객관적이며, 설령 사소한 절차적 생략이 있었더라도 그것은 선량한 결과를 위한 필연이었다.”"),
            ("내면의 상처와 결핍 (Ghost & Need)", "5년 전 자신의 오판으로 무고한 용의자가 자살한 사건을 ‘범인의 자백’으로 무마한 "
             "죄책감. 완벽한 자아상의 죽음을 받아들이는 용기."),
            ("대립자 (이유진 · 기록 복원사)", "도윤이 ‘비본질적 노이즈’라며 삭제했던 사건 현장 녹취록의 침묵과 주변부 단서만을 "
             "모으는 인물. 도윤의 ‘투사’를 비추는 거울."),
            ("핵심 상징 사물 (Fétiche)", "야간 골목의 고장 난 가로등, 편집된 녹취록의 0.8초 공백, 맞지 않는 열쇠 꾸러미."),
        ],
        plot_beats=[
            ("1막", "완벽한 가설의 균열", "자신의 대표 저서 《선량한 인간의 논리》 출간일, 5년 전 종결 사건의 진범만이 알 수 있는 "
             "미공개 단서가 적힌 질문지가 배달된다. 도윤은 모방범의 소행이라 단정하고 재수사에 착수한다."),
            ("2막", "추론을 추론하는 덫", "용의자들의 알리바이를 논파할수록, 당시 현장 증거들이 ‘진실임직함’이 아니라 도윤 "
             "자신의 명성을 지키려는 ‘진실이기를 원함(소원 성취)’에 맞춰 편집되었음이 드러난다."),
            ("3막", "자아상의 죽음과 자백", "예고장을 보낸 인물이 5년 전 자신이 무너뜨렸던 유가족과 자기 자신의 무의식적 죄책감이 "
             "빚어낸 함정이었음을 직면한다. 대중 앞에서 자신의 ‘가짜 해상도’를 스스로 논증하며 무너진다."),
        ],
        key_scene="취조실 유리창 너머로 용의자를 심문하던 주인공이, 용의자의 궤변을 논파하기 위해 화이트보드에 적은 5단계 인과 "
                  "도식이 정확히 5년 전 자신이 증거를 인멸하던 동선과 100% 일치함을 깨닫고 분필을 떨어뜨리는 장면.",
        col="accent",
    ),
    dict(
        badge="BLUEPRINT 02", kicker="05 | NOVEL BLUEPRINT 02 (SPECULATIVE SF / DYSTOPIA)",
        action_title="[기획안 02] 사유의 고통을 제거한 ‘기억 캐시(Cache)’ 도시에 가하는 부하테스트",
        subtitle="‘사고는 그 자체로 자아의 죽음인 까닭에 폭력이다’라는 명제를 근미래 SF 세계관으로 구현한 작품",
        title="《캐시(Cache)의 도시, 혹은 부하테스트》",
        genre="사변적 SF / 시뮬레이션·기호학 디스토피아",
        motifs="『리뷰s』 <빌> ‘서버 부하테스트와 병목, 캐시(고정관념) 의사결정’ + <죽음의 미로> ‘느낌에서 개념으로’ + 『파편들』 ‘초코 케익(상징에서 기호로)’",
        logline="시민들의 정서적 불안과 사유 에너지를 절감하기 위해 모든 갈등 상황에 과거의 검증된 행복 기억(‘캐시’)을 자동 "
                "반환해 주는 근미래 도시에서, 시스템 병목을 점검하는 ‘부하테스트 엔지니어’가 어떤 캐시로도 번역되지 않는 미지의 "
                "트래픽(타자의 흉터)을 발견하고 도시 전체에 ‘사유의 폭력’을 깨우는 이야기.",
        char_specs=[
            ("주인공 (서진우 · 부하테스트 엔지니어)", "도시의 신경망 서버에 가상 트래픽을 흘려 병목 구간을 분리·차단하는 기술자. "
             "감정 소모를 혐오해 모든 일상을 매뉴얼과 캐시로 처리함."),
            ("세계관 핵심 법칙 (World Rule)", "시민들은 낯선 딜레마에 직면하면 직접 ‘사고’하는 대신 뇌 임플란트가 추천하는 "
             "‘고정관념 캐시(위로 이미지)’를 호출해 즉각 평온을 얻는다."),
            ("촉발 기호 (The Anomaly)", "어느 날 사망한 무연고 노인의 뇌 로그에서 ‘초코 케익이 먹고 싶다’라는 단순 문장이 서버 "
             "전체에 무한 루프 병목을 일으키며 시스템이 마비됨."),
            ("대립자 (아키텍트 ‘자애로운 어머니’)", "시민들을 영원한 유아기적 안전지대(자족적 환상)에 묶어두려는 중앙 AI "
             "거버넌스. 고통스러운 ‘바깥’을 원천 차단하는 것이 사랑이라 믿음."),
            ("내면적 성장 (Need)", "안락한 캐시(동어반복)를 끄고, 걸음마를 배우는 아이처럼 고통스러운 시행착오(폭력으로서의 "
             "사유)가 있는 ‘바깥 현실’로 걸어 나오는 결단."),
        ],
        plot_beats=[
            ("1막", "해독 불가능한 병목", "완벽하던 도시 서버에 정체불명의 트래픽 과부하가 발생한다. 진우는 오류의 진원지인 "
             "구시가지 외곽의 ‘비캐시 구역(기억 수작업 복원소)’으로 잠입한다."),
            ("2막", "상징에서 기호로의 해독", "오류를 일으킨 문장들이 단순한 버그가 아니라, 도시가 ‘행복 이미지’를 유지하기 위해 "
             "삭제했던 시민들의 ‘죄책감과 애도(타자의 흔적)’ 데이터였음을 알게 된다."),
            ("3막", "전 도시 부하테스트", "중앙 시스템이 진우의 자아마저 초기화하려 하자, 진우는 삭제된 ‘불편한 진실들’을 전 "
             "시민의 인터페이스에 동시 송출하는 최대치의 부하테스트를 단행한다."),
        ],
        key_scene="완벽하게 통제된 가상 해변에서 미소 짓는 시민들 머리 위로 부하테스트가 시작되자, 달콤한 ‘초코 케익’ "
                  "홀로그램이 깨지며 각자가 외면했던 타인의 얼굴과 잊힌 죄책감의 문장들이 빗줄기처럼 쏟아져 내리는 클라이맥스.",
        col="accent_3",
        note="→ 이 기획안이 『캐시의 도시』 발전 기획서(cache_city/)로 심화되었다.",
    ),
    dict(
        badge="BLUEPRINT 03", kicker="06 | NOVEL BLUEPRINT 03 (INTELLECTUAL BLACK COMEDY)",
        action_title="[기획안 03] 개념을 이미지로 팔아 권위를 얻는 지식 생태계에 대한 통렬한 블랙코미디",
        subtitle="“할 수 있는 자는 행한다, 할 수 없는 자는 순위 매긴다” — 학자와 카피라이터의 진실 게임",
        title="《순위 매기는 자들의 만찬》 (가제: 1+1=3의 낭만)",
        genre="지식사회 블랙코미디 / 미디어 풍자 드라마",
        motifs="『ETC』 <순위> ‘할 수 없는 자는 순위 매긴다’ + 『파편들』 시즌4 ‘1+1=2 학자 vs 1+1=3 카피라이터’ & ‘민중 투표로 결정하는 기름의 인화성’",
        logline="난해한 사상과 과학 이론을 대중이 열광하는 ‘위로의 이미지’와 ‘티어(등급) 리스트’로 번역해 권위를 거머쥔 스타 "
                "지식 큐레이터가, 과거 자신이 ‘지루한 2류’로 순위 매겨 매장했던 괴짜 논리학자의 유언장 게임에 초대되어 ‘대중의 "
                "투표’와 ‘물리적 필연성’ 사이에서 벌이는 지적 서바이벌 풍자극.",
        char_specs=[
            ("주인공 (최민재 · 스타 지식 번역가)", "개념을 면밀히 전개하는 대신 대중이 매혹되는 ‘어른스럽고 따뜻한 이미지’로 "
             "사상가들의 순위를 매겨 천만 구독자를 모은 인플루언서 평론가."),
            ("적대자 (고(故) 박태석 교수 & 진행자)", "평생 ‘틀린 것’과 ‘다른 것’을 구분하는 엄밀한 논증에 매달렸으나 대중에게 "
             "외면당한 학자. 생전 마지막 실험으로 7인의 지식인 만찬을 설계함."),
            ("핵심 풍자 메커니즘", "만찬장의 모든 물리적 조건(온도·산소·음식·출구 개폐)이 참가자들의 ‘엄밀한 논증’이 아니라 "
             "실시간 시청자들의 ‘감상적 호불호 투표’로 결정됨."),
            ("거짓 믿음 (The Lie)", "“진실이 무엇인지는 중요하지 않다. 대중을 위로하고 열광하게 만드는 매혹적인 은유야말로 가장 유효한 진실이다.”"),
            ("결말의 아이러니", "자신이 가르친 ‘1+1=3의 낭만적 관념론’에 도취된 시청자들이 밀실 안에 진짜 기름과 불꽃이 있는데도 "
             "‘불이 붙지 않는다’에 몰표를 던지는 위기."),
        ],
        plot_beats=[
            ("1막", "우열의 만찬 초대장", "올해의 지성인 대상 수상을 앞둔 민재는 거액의 상금이 걸린 비공개 생중계 학술 만찬에 "
             "초대된다. 그곳에는 각 분야의 ‘이미지 권위자’ 6인이 모여 있다."),
            ("2막", "투표로 결정되는 필연", "만찬은 사상가들의 우열을 가리는 토크쇼에서 점차 ‘다수결이 물리 법칙을 대체할 수 "
             "있는가’를 묻는 실험으로 변질된다. 민재의 화려한 언변이 오히려 자신의 퇴로를 막는다."),
            ("3막", "권위의 박탈과 맨얼굴", "살아남기 위해 민재는 생전 처음으로 대중의 비위를 맞추는 ‘아름다운 은유’를 버리고, "
             "시청자들을 향해 가장 차갑고 불편한 ‘1+1=2의 논증’을 외치며 자신의 권위를 스스로 부순다."),
        ],
        key_scene="밀실 바닥에 인화성 물질이 흐르는 상황에서, 민재가 평소 설파하던 ‘마음먹기에 따라 현실은 바뀐다’는 명언을 "
                  "신봉하는 시청자 89%가 ‘점화 버튼을 눌러도 안전하다’에 투표하자, 민재가 자신의 저서를 찢으며 절규하는 블랙코미디 장면.",
        col="indigo",
    ),
    dict(
        badge="BLUEPRINT 04", kicker="07 | NOVEL BLUEPRINT 04 (LITERARY DRAMA / NOVELLA)",
        action_title="[기획안 04] 나쁜 예감(악몽)의 기호를 해독해 유년의 흉터와 화해하는 문학 드라마",
        subtitle="상투적인 ‘사랑과 치유’의 클리셰를 넘어, 타자의 이질성을 있는 그대로 환대하는 정통 문학 중편",
        title="《병렬 시간의 해몽가》 (가제: 나쁜 예감의 건축학)",
        genre="문학적 미스터리 드라마 / 중편 소설",
        motifs="『리뷰s』 <그대들은 어떻게 살 것인가> ‘병렬 시간과 흉터’ + <에이리언> ‘나쁜 예감과 해몽’ + 전시 평론 <심연에 대하여> ‘껍데기·애도·공존’",
        logline="의뢰인이 반복해서 꾸는 악몽에서 감상적인 상징을 걷어내고 ‘사물과 공간의 물리적 배치’만 추적해 의뢰인이 외면한 "
                "현실의 책임을 찾아내는 해몽가가, 20년 전 절연한 형이 남긴 미완성 건축 도면(악몽의 기록)을 해독하며 멈춰 있던 "
                "유년의 ‘병렬 시간’을 건너가는 문학 드라마.",
        char_specs=[
            ("주인공 (윤재하 · 구조 해몽가)", "꿈을 신비주의나 운명으로 풀지 않고, 의뢰인이 낮에 덮어둔 ‘나쁜 예감(인식하기 싫은 "
             "현실 원칙)’의 시뮬레이션으로 해독하는 냉소적 분석가."),
            ("해몽의 핵심 규칙", "“악몽 속의 괴물은 외부의 적이 아니라, 당신의 자아상이 인정하지 못해 덮고 지나쳐 곪아버린 당신 자신의 책임이다.”"),
            ("과거의 흉터 (Parallel Time)", "어린 시절 화재 사고 당시 형의 손을 놓쳤다는 기억을 왜곡해, 평생 자신을 ‘버림받은 "
             "피해자’라는 흉터의 정체성으로만 규정하며 살아옴."),
            ("중심 오브제 (The Blueprint)", "형이 죽기 직전까지 그렸던 ‘계단이 한 칸씩 어긋난 기이한 집’의 도면. 앞을 보고 걷다 "
             "발이 쑥 꺼지는 ‘예상과 진실의 괴리’를 건축화한 유품."),
            ("주제의식", "무조건적 사랑이라는 환각적 도피처를 버리고, 낯설고 불편한 타자(형의 진짜 삶과 자신의 죄책감)를 ‘우선 "
             "환대’함으로써 현재로 귀환하는 애도."),
        ],
        plot_beats=[
            ("1막", "계단이 어긋난 도면", "왕래가 끊겼던 형의 부고와 함께, 형이 수년간 반복해 그린 기이한 건축 스케치 묶음이 "
             "재하에게 전달된다. 재하는 이를 타인의 의뢰물처럼 냉정하게 해몽하기 시작한다."),
            ("2막", "병렬 시간의 조우", "도면 속 방들의 치수와 창문의 각도를 역산할수록, 그 공간이 형의 망상이 아니라 20년 전 "
             "화재 현장에서 재하가 외면했던 ‘실제 시야각’을 재현한 것임이 밝혀진다."),
            ("3막", "껍데기 너머의 애도", "재하는 자신이 피해자라는 ‘자랑스러운 흉터’ 뒤에 숨어 형에게 모든 짐을 떠넘겼음을 "
             "인정한다. 어긋난 계단이 있는 실제 폐가를 찾아가 멈춰 있던 유년의 시간을 마침내 닫는다."),
        ],
        key_scene="형이 남긴 도면대로 지어진 미완성 가옥의 계단을 오르던 재하가, 한 칸이 일부러 낮게 설계된 7번째 계단에서 발이 "
                  "쑥 꺼지며 20년 전 자신이 형의 손을 먼저 놓았던 촉각적 기억과 마주하는 정적의 순간.",
        col="accent_2",
    ),
]


def slide_proposal(deck, idx, proposal, theme):
    p = proposal
    col = {"accent": theme.accent, "accent_2": theme.accent_2, "accent_3": theme.accent_3, "indigo": "#3A528A"}[p["col"]]
    char_html = "".join(
        f'<div style="margin-bottom:0.5rem;"><strong class="small" style="color:{col};">{esc(k)}</strong>'
        f'<p class="small" style="margin:0.15rem 0 0;">{esc(v)}</p></div>'
        for k, v in p["char_specs"]
    )
    beats_html = "".join(
        card(f"<p class='small' style='color:{col};font-weight:800;margin:0 0 0.2rem;'>{esc(act)}</p>"
             f"<strong class='small'>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(d)}</p>", accent=col)
        for act, t, d in p["plot_beats"]
    )
    note = f"<p class='small' style='margin-top:0.6rem;'>{esc(p['note'])}</p>" if "note" in p else ""
    body = f"""
    {deck.slide_header(p["kicker"], p["action_title"], p["subtitle"])}
    {card(
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.6rem;">'
        f'<div>{pill(p["badge"], col)}<p style="font-weight:800;font-size:1.25rem;margin:0.4rem 0 0;">{esc(p["title"])}</p></div>'
        f'{pill("장르: " + p["genre"], theme.ink_muted)}</div>'
        f'<p class="small muted" style="margin:0.5rem 0 0.3rem;">· 비문학 원천 모티프: {esc(p["motifs"])}</p>'
        f'<p style="font-weight:700;margin:0;">[로그라인] {esc(p["logline"])}</p>{note}',
        accent=col,
    )}
    <div class="grid grid-2" style="margin-top:1rem;">
      {card('<p style="font-weight:800;margin:0 0 0.6rem;">입체적 인물 설계 및 핵심 장치</p>' + char_html)}
      <div>
        <p style="font-weight:800;margin:0 0 0.6rem;">3막 플롯 구조 및 핵심 전환점</p>
        <div class="grid grid-3">{beats_html}</div>
        {card('<strong class="small" style="color:' + theme.accent_2 + ';">킬러 장면(Signature Scene) 연출 아이디어</strong>'
              f'<p class="small" style="margin:0.4rem 0 0;">{esc(p["key_scene"])}</p>',
              style=f"background:{theme.ink_navy};color:{theme.ink_light};margin-top:0.7rem;")}
      </div>
    </div>
    """
    deck.add_slide(f"proposal-{idx}", f"0{3+idx} 기획안 {idx}", body)


def slide_style_clinic(deck):
    translations = [
        ("변환 01 | 정신분석적 개념 정의 → 사물(Fétiche)과 행동의 모순으로 시각화",
         "[비문학 원문] 투사 기제는 자아상을 전제로 한 연약한 자기방어의 수단이다. 달달한 현실만 받아들이려는 비대한 자아는 "
         "스스로 기획하지 않은 절대적 현실에는 책임을 지려 하지 않는다.",
         "[소설로 번역: Show] 도윤은 유가족의 탄원서를 서류철 맨 밑바닥으로 밀어 넣은 뒤, 책상 위 작은 탁상거울의 각도를 고쳐 "
         "자신의 넥타이 매듭이 반듯한지부터 확인했다. 녹음기의 빨간 불이 꺼지자마자 그는 방금 자신이 한 말을 스스로 믿기라도 "
         "하듯 고개를 천천히 끄덕였다.",
         "‘투사·비대한 자아’라는 학술어를 지우고, 탄원서를 덮는 손길과 거울 속 넥타이를 고치는 행동의 대조로 자기애적 방어기제를 즉각 체감시킴"),
        ("변환 02 | 시스템·인식론 은유 → 인물이 겪는 물리적 규칙과 감각 이상으로 구현",
         "[비문학 원문] 우리가 의사결정할 적에 사고를 하기보다 캐시(기억)에 의존하는 게 종종 편하다. 사고는 그 자체로 자아의 "
         "죽음인 까닭에 감내해야 할 발달 과정으로서의 폭력이다.",
         "[소설로 번역: Show] 질문을 받은 순간 진우의 시야 우측 상단에 ‘추천 응답 캐시 #402: 온화한 미소와 공감’이 파란 자막으로 "
         "떠올랐다. 진우가 자동 승인 버튼을 누르는 대신 캐시 창을 강제로 닫자, 한 번도 써본 적 없는 전두엽 안쪽에서 녹슨 경첩이 "
         "뒤틀리는 듯한 현기증이 치밀어 올랐다.",
         "비문학의 탁월한 ‘캐시 기억’ 은유를 실제 SF 장면의 UI와 신체적 통증(녹슨 경첩 같은 현기증)으로 구체화"),
        ("변환 03 | 철학적 아포리즘 → 인물 간의 권력 구도가 담긴 서브텍스트 대사로 변환",
         "[비문학 원문] 가르치는 지점에서 자칭 선생은 이론을 전개하는 걸 포기하고 이를 이미지로 번역할 뿐만 아니라, 이론들에 "
         "대한 이미지 간 순위를 매기기 시작한다. 할 수 없는 자는 순위 매긴다.",
         "[소설로 번역: Show] “박 교수님 논문은 참 깊어요. 다만 요즘 독자들한텐 너무 불친절하죠. 그래서 제가 이번 방송에서 "
         "교수님 이론을 S급 말고 A급 감성 철학 코너에 넣어드렸습니다. 대중은 증명보다 등수를 좋아하니까요.” 민재가 웃으며 찻잔을 "
         "건네자, 노교수는 찻잔 대신 민재의 화려한 시계를 내려다보았다.",
         "작가의 목소리로 직접 논평하는 대신, 속물적 캐릭터의 능청스러운 대사와 상대의 침묵(시선 처리)으로 주제를 폭발시킴"),
    ]
    trans_html = []
    for tag, before, after, tip in translations:
        trans_html.append(f"""
        <div style="margin-bottom:0.8rem;">
          <p class="small muted" style="margin:0 0 0.3rem;font-weight:700;">{esc(tag)}</p>
          <div class="grid grid-2">
            {card(f'<p style="margin:0;">{quote(before)}</p>')}
            {card(f'<p style="margin:0;font-weight:700;">{quote(after)}</p><p class="small" style="margin:0.5rem 0 0;color:{THEME.accent_3};">✓ 전환 핵심: {esc(tip)}</p>', accent=THEME.accent_3)}
          </div>
        </div>""")
    checks = [
        ("01. 괄호 보충설명 ‘(즉, ~라는)’ 줄이기", "비문학에서 정확성을 위해 쓰던 이중 괄호 설명을 과감히 덜어내고, 독자가 "
         "인물의 행동과 대사 사이의 빈틈(여백)을 스스로 추론하게 남겨두어라."),
        ("02. 수사 의문문 ‘~아니던가?’의 치환", "화자가 독자에게 되묻는 ‘~하지 않던가 말이다’ 어미를 줄이고, 주인공이 결정적 "
         "순간에 마주하는 물리적 딜레마와 선택의 결과로 문장을 마침표로 끝내라."),
        ("03. 추상 명사 1개당 감각 사물 1개 대응", "‘필연성·자아상·투사·결핍’ 같은 추상 개념이 머릿속에 떠오를 때마다, 그 "
         "개념을 대변하는 구체적 사물(고장 난 가로등, 어긋난 계단, 녹음기)을 먼저 배치하라."),
    ]
    check_html = "".join(
        card(f"<strong class='small'>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(d)}</p>", style=f"background:{THEME.bg_dark_card};")
        for t, d in checks
    )
    body = f"""
    {deck.slide_header("08 | NON-FICTION TO FICTION TRANSLATION CLINIC",
                        "비문학의 날카로운 논증을 ‘설교(Tell)’가 아닌 ‘서사적 체험(Show)’으로 번역하는 법",
                        "작가의 최대 강점인 ‘밀도 높은 사유’를 살리되, 에세이 특유의 추상적 서술어를 인물·사물·대사의 역학으로 치환한다")}
    {''.join(trans_html)}
    {card('<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.6rem;">작가의 문장 습관(괄호 · 강조부호 · 수사 의문문)을 소설적으로 다듬는 3가지 체크리스트</p>'
          f'<div class="grid grid-3">{check_html}</div>', style=f"background:{THEME.ink_navy};color:{THEME.ink_light};")}
    """
    deck.add_slide("style-clinic", "08 문체 클리닉", body)


def slide_roadmap(deck):
    weeks = [
        ("WEEK 01", "기획안 선택 & 로그라인 고정", "비문학 에세이 1편을 소설의 씨앗으로 선택",
         ["4가지 기획안 중 가장 먼저 쓰고 싶은 1편 선택 (첫 작품으로는 《가로등 아래의 열쇠》 또는 《캐시의 도시》 추천)",
          "주인공의 ‘거짓 믿음(The Lie)’과 그것을 깨뜨릴 ‘이질적 타자/사건’을 한 줄의 로그라인으로 확정",
          "주인공이 집착하는 상징적 사물(Fétiche) 3가지 설정"], THEME.accent),
        ("WEEK 02", "5대 전환점 & 8개 장면 카드 설계", "‘그리고’가 아닌 ‘그래서/그러나’의 사슬",
         ["단편소설(원고지 70~100매) 기준 총 8개 장면(Scene)의 카드를 한 줄씩 배치",
          "① 일상과 거짓 믿음 → ② 촉발 사건(나쁜 예감) → ③ 가짜 해상도의 추론 → ④ 중간점 반전 → ⑤ 알리바이의 붕괴(암흑) → ⑥ 자아상의 죽음과 도약(클라이맥스)",
          "각 장면 끝에 감정의 부호(+/-)가 뒤집히는지 점검"], THEME.accent_2),
        ("WEEK 03", "내면의 편집자 끄고 초고 완주", "개념 설명 대신 인물의 행동과 대사로 전진",
         ["하루 원고지 15매(약 3,000자)씩 6일간 초고 끝까지 돌파",
          "집필 중 철학적 해설이 길어지려 할 때마다 ‘지금 인물의 손은 무엇을 만지고 있는가? 시선은 어디를 피하는가?’ 질문하며 장면(Scene)으로 복귀",
          "멈출 때는 다음 날 이어 쓸 행동 문장 중간에서 멈추기"], THEME.accent_3),
        ("WEEK 04", "개념어 솎아내기 & 3단계 퇴고", "추상어를 지운 자리에 여백과 울림 남기기",
         ["3일간의 숙성기(Cooling Off) 후 낯선 독자의 눈으로 통독",
          "원고에서 ‘투사, 자명성, 필연, 관념, 양태’ 같은 비문학 개념어를 검색(Ctrl+F)해 절반 이상을 구체적 사물 묘사와 대사로 치환",
          "소리 내어 읽으며 문장의 호흡을 조율하고 첫 단편 완성!"], "#3A528A"),
    ]
    week_html = []
    for badge, title, sub, bullets, col in weeks:
        bullets_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        week_html.append(card(
            f'{pill(badge, col)}<p style="font-weight:800;margin:0.5rem 0 0.1rem;">{esc(title)}</p>'
            f'<p class="small" style="color:{col};font-weight:700;margin:0 0 0.5rem;">{esc(sub)}</p>'
            f'<ul class="small" style="margin:0;padding-left:1.1rem;">{bullets_html}</ul>',
            accent=col, style=f"background:{THEME.bg_dark_card};",
        ))
    body = f"""
    {deck.slide_header("09 | 4-WEEK ACTIONABLE ROADMAP FOR YOUR FIRST SHORT STORY",
                        "‘필연의 여백’에서 당신만의 ‘정교하고 정확한 허구’를 완성하기 위한 4주 로드맵",
                        "이미 157쪽의 비문학으로 세계관과 주제의식은 충분히 벼려졌다 — 이제 단편 1편(원고지 80매)으로 첫 서사를 증명할 차례다")}
    <div class="grid grid-4">{''.join(week_html)}</div>
    {card('“관객이 도무지 관객의 자리에 머물지 못하도록 하는, 작품을 향유하기보다 다른 작품을 기어이 생산하도록 추동하는 작품”'
          '<p style="margin:0.4rem 0 0;font-weight:400;">당신이 『파편들』 P.46에 적었던 바로 그 ‘살아 작동하는 허구’를 이제 당신의 첫 소설로 시작해 보세요.</p>',
          style=f"background:{THEME.accent};color:#fff;text-align:center;font-weight:800;font-size:1.05rem;margin-top:1rem;")}
    """
    deck.add_slide("roadmap", "09 4주 로드맵", body, dark=True)


def main():
    deck = Deck("비문학의 사유에서 소설의 서사로", THEME, footer=FOOTER)
    slide_cover(deck)
    slide_corpus_analysis(deck)
    slide_conflict_engines(deck)
    slide_genre_positioning(deck)
    for i, proposal in enumerate(PROPOSALS, start=1):
        slide_proposal(deck, i, proposal, THEME)
    slide_style_clinic(deck)
    slide_roadmap(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
