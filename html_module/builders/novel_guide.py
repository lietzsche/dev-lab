#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
소설 쓰기 마스터클래스 (The Craft of Fiction Writing) — HTML 생성 스크립트

PPTX 버전(ppt_module/builders/novel_guide.py)의 전체 내용을 그대로 옮긴
HTML 포트. 좌표 기반 배치/자동맞춤 싸움이 전부 사라진다 — 브라우저가
텍스트를 스스로 흘려 담기 때문.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, PROJECT_ROOT)

from html_module import Deck, esc
from html_module.components import pill, card, grid, kv_list, quote
from html_module.theme import NOVEL_GUIDE_THEME as THEME

OUT_PATH = os.path.join(PROJECT_ROOT, "소설쓰기_가이드.html")
FOOTER = "THE CRAFT OF FICTION WRITING · 소설 창작 실전 가이드"


def slide_cover(deck):
    modules = [
        ("PART 01", "발상과 캐릭터", "로그라인 · 욕망과 결핍"),
        ("PART 02", "플롯과 갈등", "3막 구조 · 씬의 역학"),
        ("PART 03", "시점과 문체", "POV · Show, Don't Tell"),
        ("PART 04", "퇴고와 완성", "3단계 수정 · 작가 루틴"),
    ]
    module_html = "".join(
        card(f"<p class='small' style='color:{THEME.accent_2};font-weight:800;margin:0;'>{esc(part)}</p>"
             f"<p style='font-weight:800;margin:0.3rem 0;'>{esc(title)}</p>"
             f"<p class='small muted' style='margin:0;'>{esc(desc)}</p>")
        for part, title, desc in modules
    )
    body = f"""
    {pill("CREATIVE WRITING MASTERCLASS", THEME.accent_2)}
    <h1 style="font-size:clamp(2.2rem,5vw,3.2rem);margin:0.8rem 0 0.3rem;">매혹적인 소설 쓰기의 기술</h1>
    <p class="muted" style="max-width:42rem;">아이디어의 첫 불꽃부터 마지막 문장의 퇴고까지, 독자의 밤을 빼앗는 서사 설계의 10가지 핵심 원칙</p>
    <div class="grid grid-4" style="margin-top:1.8rem;">{module_html}</div>
    """
    deck.add_slide("cover", "표지", body, dark=True)


def slide_pillars(deck):
    pillars = [
        ("01", "매혹적인 전제 (Premise)", "호기심을 점화하는 ‘만약에(What if?)’의 질문", THEME.accent,
         ["익숙한 일상 속 낯선 균열을 포착해 독자의 질문을 유도",
          "단순한 설정 나열이 아닌 주인공이 겪을 윤리적·현실적 딜레마 내포",
          "한 문장의 로그라인으로 압축될 때 서사의 방향성이 흔들리지 않음"],
         "핵심 질문: 독자가 첫 페이지를 펼칠 이유는 무엇인가?"),
        ("02", "입체적 인물 (Character)", "욕망(Want)과 결핍(Need)이 충돌하는 살아있는 주체", THEME.accent_3,
         ["완벽한 영웅보다 결함과 모순을 지닌 인물에게 독자가 감정이입",
          "외면적 목표를 추구하는 과정에서 내면의 거짓 믿음이 깨지는 성장",
          "주인공의 약점을 정확히 파고드는 대립자(Antagonist)와의 상호작용"],
         "핵심 질문: 이 인물은 무엇을 간절히 원하며 무엇을 잃을까 두려워하는가?"),
        ("03", "인과적 플롯 (Plot & Conflict)", "‘그리고’가 아닌 ‘그래서/그러나’로 연결된 사건의 사슬", THEME.accent_2,
         ["우연에 기댄 해결(데우스 엑스 마키나)을 배제하고 인물의 선택으로 전개",
          "점진적으로 판돈(Stakes)을 높여 주인공을 퇴로 없는 막다른 골목으로 압박",
          "3막 구조의 5대 전환점을 통해 긴장과 이완의 서사적 리듬을 설계"],
         "핵심 질문: 이전 사건이 다음 사건을 필연적으로 강제하는가?"),
        ("04", "감각적 장면과 문체 (Scene & Voice)", "요약 설명(Tell)을 넘어 현장을 체험하게 하는 묘사(Show)", "#8E3542",
         ["오감의 디테일과 구체적 행동으로 인물의 감정선을 시각화",
          "인물의 성격과 관계의 권력 구도가 묻어나는 입체적인 대사 설계",
          "불필요한 수식어를 덜어내고 장면의 속도에 맞춘 문장 호흡 조율"],
         "핵심 질문: 독자의 머릿속에 이 장면이 영화처럼 그려지는가?"),
    ]
    cards_html = []
    for num, title, sub, col, bullets, key_q in pillars:
        bullets_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        cards_html.append(card(
            f'<div style="display:flex;gap:0.7rem;align-items:baseline;">'
            f'<span style="background:{col};color:#fff;border-radius:999px;width:1.9rem;height:1.9rem;'
            f'display:inline-flex;align-items:center;justify-content:center;font-weight:800;flex:none;">{esc(num)}</span>'
            f'<div><strong>{esc(title)}</strong><p class="small" style="color:{col};font-weight:700;margin:0.2rem 0 0;">{esc(sub)}</p></div></div>'
            f'<ul class="small" style="margin:0.6rem 0;padding-left:1.2rem;">{bullets_html}</ul>'
            f'<p class="small" style="background:{col}1a;padding:0.4rem 0.6rem;border-radius:0.4rem;margin:0;font-weight:700;">{esc(key_q)}</p>',
            accent=col,
        ))
    body = f"""
    {deck.slide_header("01 | FICTION ARCHITECTURE",
                        "완성도 높은 소설은 소재·인물·플롯·문체의 4대 축으로 작동한다",
                        "네 가지 기둥 중 하나라도 무너지면 서사의 설득력이 급격히 약화된다")}
    <div class="grid grid-2">{''.join(cards_html)}</div>
    {card('<strong>핵심 공식</strong> · 매력적인 소재(Premise)가 독자를 부르고, 입체적인 인물(Character)이 페이지를 '
          '넘기게 하며, 단단한 플롯과 문체가 여운을 완성한다.', style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:1rem;text-align:center;")}
    """
    deck.add_slide("pillars", "01 4대 기둥", body)


def slide_logline(deck):
    formula = [
        ("1. 결핍을 지닌 주인공", "어떤 약점·상황에 처한 인물이"),
        ("2. 촉발 사건 (Inciting)", "예기치 못한 사건을 겪은 뒤"),
        ("3. 핵심 목표와 대립", "강력한 적수/장애물에 맞서"),
        ("4. 치명적 대가 (Stakes)", "무엇을 걸고 싸우는가?"),
    ]
    formula_html = "".join(
        card(f"<strong>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(d)}</p>",
             accent=THEME.accent if i == 3 else None)
        for i, (t, d) in enumerate(formula)
    )
    examples = [
        ("장르 01 · 미스터리 스릴러", "기억상실증에 걸린 형사가 살인사건을 수사하는 이야기",
         "단기 기억이 24시간마다 초기화되는 강력계 형사가, 자신의 수첩에 적힌 마지막 용의자가 바로 자신임을 알게 되면서 기억이 사라지기 전에 진범을 찾아야 하는 사투",
         "제한 시간(24시간) + 아이러니(자신이 용의자)"),
        ("장르 02 · SF / 판타지", "감정을 사고파는 미래 사회에서 벌어지는 청춘 드라마",
         "타인의 슬픔을 대신 겪어주고 돈을 버는 ‘감정 대리인’ 청년이, 의뢰인의 지워진 기억 속에서 10년 전 실종된 여동생의 흔적을 발견하고 거대 기업의 금기를 추적하는 이야기",
         "독창적 직업 + 개인적 절박함(실종된 동생)"),
        ("장르 03 · 휴먼 / 가족 드라마", "사이가 나쁜 모녀가 함께 여행을 떠나며 화해하는 소설",
         "평생 연락을 끊고 살던 어머니의 유언장 조건 때문에, 빚더미에 오른 딸이 어머니의 첫사랑을 찾아 일주일간 동행하며 몰랐던 어머니의 청춘과 마주하는 여정",
         "강제적 동행(유언 조건) + 내면적 화해"),
    ]
    example_html = []
    for genre, weak, strong, point in examples:
        example_html.append(f"""
        <div class="grid grid-2" style="margin-bottom:0.8rem;">
          {card(f'<p class="small muted" style="margin:0 0 0.3rem;">[막연한 소재] {esc(genre)}</p><p style="margin:0;">“{esc(weak)}”</p>')}
          {card(f'<p class="small" style="color:{THEME.accent};font-weight:700;margin:0 0 0.3rem;">[완성된 로그라인] {pill(point, THEME.accent)}</p><p style="margin:0;font-weight:700;">{esc(strong)}</p>', accent=THEME.accent)}
        </div>""")
    body = f"""
    {deck.slide_header("02 | IDEA & LOGLINE DESIGN",
                        "막연한 소재를 한 문장의 로그라인(Logline)으로 압축해 서사의 나침반을 세운다",
                        "좋은 로그라인은 주인공, 촉발 사건, 핵심 목표, 그리고 실패 시 치러야 할 대가(Stakes)를 명확히 보여준다")}
    <p style="font-weight:800;color:{THEME.accent};margin:0 0 0.6rem;">강력한 로그라인의 4요소 공식</p>
    <div class="grid grid-4" style="margin-bottom:1.4rem;">{formula_html}</div>
    <p style="font-weight:800;margin:0 0 0.6rem;">실전 변환 예시: 추상적 소재에서 구체적 로그라인으로</p>
    {''.join(example_html)}
    """
    deck.add_slide("logline", "02 로그라인", body)


def slide_character(deck):
    right_cards = [
        ("욕망(Want) vs 필요(Need)의 충돌",
         "주인공은 눈에 보이는 목표(성공·복수·탈출)를 향해 달리지만, 결말에 이르러 자신이 진짜 필요했던 것(신뢰·용서·진실)을 깨닫고 변화한다.", THEME.accent),
        ("적대자(Antagonist)는 주인공의 거울",
         "최고의 악역은 스스로를 선이라고 믿는 인물이다. 주인공과 같은 문제에 직면했지만 정반대의 선택을 한 그림자로 설계할 때 대립이 깊어진다.", THEME.accent_3),
        ("성격은 형용사가 아니라 ‘선택’으로 증명",
         "평화로운 순간의 친절함은 성격을 보여주지 못한다. 가장 소중한 두 가치 중 하나를 포기해야 하는 극한의 딜레마에서 내리는 선택이 진짜 캐릭터다.", THEME.accent_2),
    ]
    right_html = "".join(
        card(f"<strong>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(b)}</p>", accent=c)
        for t, b, c in right_cards
    )
    sheet = [
        ("과거의 상처 (Ghost)", "어린 시절 자신의 거짓말로 가족의 유품을 잃어버린 죄책감"),
        ("거짓 믿음 (The Lie)", "“사람은 결국 배신하지만, 사물은 절대 거짓말을 하지 않는다.”"),
        ("외면적 목표 (Want)", "불타버린 고택의 미공개 유작을 완벽히 복원해 거액의 보수를 받는 것"),
        ("내면적 성장 (Need)", "완벽한 복원보다 남겨진 유가족의 상처를 보듬고 진실을 마주하는 용기"),
    ]
    body = f"""
    {deck.slide_header("03 | CHARACTER PSYCHOLOGY",
                        "독자가 사랑하는 인물은 외면적 목표(Want)와 내면적 결핍(Need)의 간극에서 탄생한다",
                        "인물의 프로필을 나열하는 대신, 과거의 상처(Ghost)가 만든 거짓 믿음(Lie)과 행동 동기를 설계하라")}
    <div class="grid grid-2">
      {card('<p style="font-weight:800;margin:0 0 0.6rem;">인물 설계의 빙산 모델 (Character Iceberg)</p>'
            '<p class="small muted">외면적 특징과 행동(직업·말투·습관) → 외면적 목표(Want) — 수면 위 20%<br>'
            '내면의 결핍과 두려움(Need) → 거짓 믿음(The Lie) → 과거의 상처(The Ghost) — 수면 아래 80%</p>'
            '<p class="small muted">보이는 행동은 수면 위 20%일 뿐, 인물을 실제로 움직이는 동력은 수면 아래 결핍·거짓 믿음·상처다.</p>')}
      <div>{right_html}</div>
    </div>
    {card(
        '<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.6rem;">실전 캐릭터 설계 시트 예시 — &lt;폐기처분 복원가 ‘한서진’&gt;</p>'
        + kv_list(sheet),
        style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:1rem;",
    )}
    """
    deck.add_slide("character", "03 인물 설계", body)


def slide_plot_arc(deck):
    beats = [
        ("① 촉발 사건 (12%)", "일상의 균열", "주인공의 평온한 일상을 깨뜨리고 이야기 속으로 호출하는 사건", THEME.accent),
        ("② 1차 관문 (25%)", "돌아갈 다리 불태우기", "주인공이 기존 세계를 떠나 본격적인 모험·대립의 세계로 진입하는 결단", THEME.accent_3),
        ("③ 중간점 반전 (50%)", "시야의 전환", "숨겨진 진실이 드러나며 수동적 대응에서 능동적 공세로 전환되는 지점", THEME.accent_2),
        ("④ 암흑의 순간 (75%)", "최악의 패배", "모든 계획이 무너지고 가장 소중한 것을 잃을 위기에 처하는 절망의 바닥", "#8E3542"),
        ("⑤ 클라이맥스 (90%)", "최후의 대결과 각성", "내면의 거짓 믿음을 극복한 주인공이 자신의 힘으로 핵심 갈등을 매듭짓는 순간", THEME.ink_navy),
    ]
    beats_html = "".join(
        card(f"<strong style='color:{col};'>{esc(t1)}</strong><p style='font-weight:700;margin:0.3rem 0;'>{esc(t2)}</p>"
             f"<p class='small muted' style='margin:0;'>{esc(d)}</p>", accent=col)
        for t1, t2, d, col in beats
    )
    body = f"""
    {deck.slide_header("04 | THREE-ACT STRUCTURE & PLOT BEATS",
                        "3막 구조와 5대 전환점(Plot Beats)으로 독자가 책을 덮지 못하는 긴장감을 조율한다",
                        "서사의 황금 비율(1막 25% : 2막 50% : 3막 25%)을 통해 위기의 고조와 해소의 쾌감을 정교하게 배치한다")}
    {card('<p class="small muted" style="margin:0;">1막: 설정과 출발(0~25%) → 2막: 대립·역전·위기(25~75%) → 3막: 절정과 해소(75~100%). '
          '전체 곡선은 일상 세계 → 촉발 사건(12%) → 1차 관문(25%) → 중간점 반전(50%) → 암흑의 순간(75%) → 클라이맥스(90%) → 새로운 균형(100%)으로 상승·하강한다.</p>')}
    <div class="grid grid-4" style="margin-top:1rem;">{beats_html}</div>
    """
    deck.add_slide("plot-arc", "04 3막 구조", body)


def slide_scene_dynamics(deck):
    scene_steps = [
        ("1. 목표 (Goal)", "장면 시작 시 주인공이 원하는 구체적이고 가시적인 목적"),
        ("2. 충돌 (Conflict)", "목표 달성을 가로막는 상대방이나 환경과의 치열한 공방"),
        ("3. 전환/재난 (Disaster)", "‘예스, 하지만(Yes, but)’ 또는 ‘노, 심지어(No, and furthermore)’로 끝나는 위기"),
    ]
    sequel_steps = [
        ("1. 감정 반응 (Reaction)", "직전 장면의 재난/충격에 대한 인물의 정서적·신체적 여파"),
        ("2. 딜레마 (Dilemma)", "나쁜 선택지들 사이에서 최악을 피하기 위해 고뇌하는 분석 과정"),
        ("3. 새로운 결단 (Decision)", "위험을 감수하고 다음 행동 장면(Scene)의 목표를 세우는 결심"),
    ]
    layers = [
        ("내적 갈등 (Inner)", "양심 vs 욕망, 두려움 vs 의무 등 인물 내면의 심리적 분열", THEME.accent),
        ("대인 갈등 (Personal)", "연인·가족·동료·숙적과의 이해관계 충돌과 배신", THEME.accent_3),
        ("환경/사회 갈등 (Extra)", "재난, 부조리한 제도, 시간 제한 등 거대한 외부 압력", THEME.accent_2),
    ]
    step_html = lambda steps: "".join(
        card(f"<strong class='small'>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(d)}</p>")
        for t, d in steps
    )
    layer_html = "".join(
        card(f"<strong class='small' style='color:{c};'>{esc(t)}</strong><p class='small muted' style='margin:0.2rem 0 0;'>{esc(d)}</p>", accent=c)
        for t, d, c in layers
    )
    body = f"""
    {deck.slide_header("05 | SCENE & SEQUEL DYNAMICS",
                        "모든 장면(Scene)은 목표·충돌·전환으로 전진하고 반추(Sequel)로 호흡을 조절한다",
                        "외면적 사건의 속도감(Scene)과 내면적 감정 소화(Sequel)를 교차 배치해 독자의 피로도를 막고 몰입을 깊게 만든다")}
    <div class="grid grid-2">
      <div>
        {card('<p style="font-weight:800;color:' + THEME.accent + ';margin:0 0 0.6rem;">ENGINE A · 외면적 행동 장면 (Action Scene) — 사건을 발생시키고 긴장을 고조</p>'
              f'<div class="grid grid-3">{step_html(scene_steps)}</div>', accent=THEME.accent)}
        {card('<p style="font-weight:800;color:' + THEME.accent_3 + ';margin:0 0 0.6rem;">ENGINE B · 내면적 반추 장면 (Reaction Sequel) — 감정을 납득시키고 다음 목표를 수립</p>'
              f'<div class="grid grid-3">{step_html(sequel_steps)}</div>', accent=THEME.accent_3, style="margin-top:0.9rem;")}
      </div>
      <div>
        {card('<p style="font-weight:800;margin:0 0 0.6rem;">입체적 서사를 만드는 갈등의 3중 레이어</p>' + layer_html)}
        {card('<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.5rem;">장면 생존 테스트 (Scene Value Test)</p>'
              '<ul class="small" style="margin:0;padding-left:1.1rem;">'
              '<li>장면의 시작과 끝 사이에 인물의 상황·감정의 부호(+/-)가 바뀌었는가?</li>'
              '<li>플롯을 전진시키거나 인물의 핵심 본성을 드러내는가?</li></ul>'
              '<p class="small" style="margin:0.4rem 0 0;">→ 둘 다 아니라면 아무리 문장이 아름다워도 과감히 삭제하라.</p>',
              style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:0.9rem;")}
      </div>
    </div>
    """
    deck.add_slide("scene-dynamics", "05 장면·반추", body)


def slide_pov(deck):
    rows = [
        ("1인칭 주인공 시점\n(‘나’의 서술)", "오직 ‘나’가 보고 듣고 추측한 정보만 서술 가능",
         "독자와 주인공의 즉각적 밀착 · 화자의 독특한 목소리·유머 극대화 · ‘신뢰할 수 없는 화자’ 트릭에 유리",
         "주인공이 없는 현장의 사건 서술 불가 · 지나친 자기연민이나 독백 과잉 위험",
         "청춘 성장소설, 느와르, 심리 미스터리, 고백록", True),
        ("3인칭 제한 시점\n(현대 소설의 표준)", "초점화된 특정 인물(‘그/그녀’)의 내면과 시선에만 밀착",
         "1인칭의 깊은 정서적 몰입감과 3인칭의 객관적 묘사력을 동시에 확보 · 서사적 거리를 유연하게 줌인/줌아웃",
         "초점 인물이 눈치채지 못한 자신의 표정·모습을 직접 묘사하는 실수 주의",
         "현대 문학 전반, 장르소설, 장편 드라마의 가장 안정적 선택", False),
        ("3인칭 전지적 시점\n(신적 조망)", "모든 인물의 내면, 과거·미래, 보이지 않는 사건까지 통찰",
         "방대한 세계관과 시대상을 조망 · 인물 간의 오해와 극적 아이러니를 독자에게 입체적으로 제시",
         "한 장면에서 여러 인물의 속마음을 오가면(Head-hopping) 긴장감 급감",
         "대하 역사소설, 가족 사가(Saga), 우화적·철학적 서사", False),
        ("다중 교차 시점\n(챕터별 3인칭/1인칭)", "챕터나 절(Section) 단위로 시점 인물을 교대하며 서술",
         "주인공과 적대자 양측의 정당성 부여 · 시점 교차 절단신공(Cliffhanger)으로 페이지 터너 효과 극대화",
         "시점 인물 간 목소리가 비슷하면 독자가 화자를 혼동 · 서사 밀도가 낮은 시점 챕터가 지루해짐",
         "군상극, 범죄 스릴러, 거대 판타지, 로맨스(쌍방 시점)", False),
    ]
    rows_html = []
    for name, scope, pros, cons, genres, hl in rows:
        bg = f"background:{THEME.accent}14;" if hl else ""
        rows_html.append(f"""<tr style="{bg}">
          <td style="font-weight:700;color:{THEME.accent if hl else THEME.ink_navy};">{esc(name)}</td>
          <td>{esc(scope)}</td><td>{esc(pros)}</td><td>{esc(cons)}</td><td>{esc(genres)}</td>
        </tr>""")
    body = f"""
    {deck.slide_header("06 | POINT OF VIEW (POV) & NARRATIVE DISTANCE",
                        "누구의 눈으로 어디까지 보여줄 것인가: 시점(POV)이 소설의 몰입도를 결정한다",
                        "각 시점의 정보 통제 범위와 심리적 거리를 이해하고, 한 장면 안에서는 단일 시점을 엄격히 유지하라")}
    <table class="cmp"><thead><tr><th>시점 유형</th><th>정보 통제와 서술 범위</th><th>서사적 강점 (Pros)</th><th>주의할 함정 (Cons)</th><th>적합한 장르</th></tr></thead>
    <tbody>{''.join(rows_html)}</tbody></table>
    {card('<strong>초보 작가의 대표적 실수 ‘시점 널뛰기(Head-Hopping)’ 금지</strong> · 한 장면 안에서는 카메라를 한 인물의 '
          '어깨 위에만 고정하고, 타인의 속마음은 표정·행동으로만 추론하게 하라.',
          style=f"background:{THEME.accent_2}22;margin-top:1rem;")}
    """
    deck.add_slide("pov", "06 시점", body)


def slide_show_dont_tell(deck):
    clinics = [
        ("CASE 01 · 감정과 심리 묘사",
         "지은은 면접 결과를 기다리며 너무나 불안하고 초조해서 견딜 수가 없었다.",
         "지은은 식어버린 머그잔 손잡이를 만지작거리다, 기어이 무릎 위에 올려둔 냅킨 모서리를 손톱 끝으로 잘게 찢어놓았다.",
         "시각·촉각 행동으로 불안감 체감"),
        ("CASE 02 · 인물의 성격 제시",
         "민수는 피도 눈물도 없이 냉정하고 계산적인 성격의 소유자였다.",
         "민수는 오열하는 동생의 어깨 너머로 벽시계의 분침을 먼저 확인한 뒤, 지갑에서 명함 한 장만 꺼내 식탁 끝에 소리 없이 내려놓았다.",
         "시계 확인 + 명함 한 장으로 냉담함 증명"),
        ("CASE 03 · 공간과 분위기 구축",
         "그곳은 오랫동안 사람이 살지 않아 무척 음산하고 불길한 폐가였다.",
         "문지방을 넘자 젖은 곰팡이 냄새가 훅 끼쳤고, 깨진 유리창 틈으로 스며든 바람에 들뜬 벽지가 뱀 허물처럼 바스락거렸다.",
         "후각(곰팡이) + 청각(벽지 소리) 입체화"),
    ]
    clinic_html = []
    for case, tell, show, note in clinics:
        clinic_html.append(f"""
        <div class="grid grid-2" style="margin-bottom:0.7rem;">
          {card(f'<p class="small muted" style="margin:0 0 0.3rem;">{esc(case)} — [요약 설명: Tell]</p><p style="margin:0;">{quote(tell)}</p>')}
          {card(f'<p class="small" style="color:{THEME.accent_3};font-weight:700;margin:0 0 0.3rem;">[Show] {pill(note, THEME.accent_3)}</p><p style="margin:0;font-weight:700;">{quote(show)}</p>', accent=THEME.accent_3)}
        </div>""")
    d_rules = [
        ("01. 정보 브리핑 대사 금지", "독자에게 배경설정을 알려주려고 인물끼리 이미 아는 사실을 말하게 하지 마라. 대사는 정보 전달이 아니라 ‘심리전’이다."),
        ("02. 서브텍스트(행간) 활용", "인물이 속마음을 정직하게 다 말하면 긴장이 사라진다. 정작 하고 싶은 말은 숨기고 엉뚱한 화제로 감정을 우회시켜라."),
        ("03. 지문과 행동 비트 결합", "“~라고 슬프게 말했다” 같은 부사형 전달동사를 줄이고, 대사 사이사이에 시선 회피나 침묵 같은 행동 비트(Action Beat)를 넣어라."),
    ]
    rule_html = "".join(
        card(f"<strong>{esc(t)}</strong><p class='small muted' style='margin:0.3rem 0 0;'>{esc(d)}</p>", style=f"background:{THEME.bg_dark_card};")
        for t, d in d_rules
    )
    body = f"""
    {deck.slide_header("07 | STYLE & DESCRIPTION CLINIC (SHOW, DON'T TELL)",
                        "감정을 단어로 요약(Tell)하지 말고, 오감과 행동의 디테일로 독자가 직접 느끼게 하라(Show)",
                        "추상적인 감정어(슬펐다, 화났다, 불안했다)를 지우고 그 감정이 만들어내는 신체 반응과 사물의 이미지로 치환한다")}
    {''.join(clinic_html)}
    {card('<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.6rem;">살아 숨 쉬는 대사(Dialogue)를 쓰는 3가지 실전 원칙</p>'
          f'<div class="grid grid-3">{rule_html}</div>', style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:1rem;")}
    """
    deck.add_slide("show-dont-tell", "07 Show/Tell", body)


def slide_revision(deck):
    passes = [
        ("PASS 01", "1차 구조 퇴고 (Macro / Structural Edit)", "나무가 아닌 숲을 보며 서사의 뼈대와 인과관계를 재조립하는 단계",
         ["주인공의 욕망과 행동이 시작부터 클라이맥스까지 일관되게 이어지는가?",
          "중반부가 늘어지지 않는가? (기능이 겹치는 장면과 인물을 과감히 통합·삭제)",
          "복선이 회수되었으며, 결말이 우연이 아닌 주인공의 선택으로 해결되는가?"], THEME.accent),
        ("PASS 02", "2차 장면·리듬 퇴고 (Scene & Pacing Edit)", "각 장면의 밀도와 대화의 텐션, 시점의 일관성을 조율하는 단계",
         ["각 장면의 첫 문장이 흥미롭고 마지막 문장이 다음 장면을 궁금하게 만드는가?",
          "한 장면 안에서 시점(POV)이 흔들리거나 설명(Tell)이 과도한 구간은 없는가?",
          "긴박한 장면에서는 단문으로 속도를 높이고, 정서적 장면에서는 호흡을 늦추었는가?"], THEME.accent_3),
        ("PASS 03", "3차 문장·윤문 퇴고 (Line Edit & Proofreading)", "소리 내어 읽으며 군더더기 수식어를 덜어내고 문장의 음악성을 다듬는 단계",
         ["상투적 부사(‘매우, 정말, 문득, 갑자기’)와 번역투(‘~에 다름 아니다, ~로부터’) 제거",
          "한 문장에 중복된 주어(‘그는 ~ 그의 ~’)와 불필요한 피동형(‘~되어졌다’) 교정",
          "육성으로 낭독(Read Aloud)했을 때 숨이 차거나 어색하게 걸리는 대사 수정"], THEME.accent_2),
    ]
    pass_html = []
    for badge, title, sub, checks, col in passes:
        checks_html = "".join(f"<li>{esc(c)}</li>" for c in checks)
        pass_html.append(card(
            f'{pill(badge, col)}<p style="font-weight:800;margin:0.5rem 0 0.1rem;">{esc(title)}</p>'
            f'<p class="small" style="color:{col};font-weight:700;margin:0 0 0.5rem;">{esc(sub)}</p>'
            f'<ul class="small" style="margin:0;padding-left:1.1rem;">{checks_html}</ul>',
            accent=col,
        ))
    body = f"""
    {deck.slide_header("08 | DRAFTING & 3-PASS REVISION PROCESS",
                        "초고는 뜨거운 가슴으로 거침없이 쓰고, 퇴고는 차가운 머리로 3단계에 걸쳐 조각한다",
                        "완벽주의 때문에 첫 장만 무한히 고치는 함정에서 벗어나, 구조·장면·문장의 순서로 해상도를 높여가며 다듬는다")}
    <div class="grid grid-2">
      <div>
        {card(f'<p style="font-weight:800;color:{THEME.accent};margin:0 0 0.5rem;">초고 완주의 제1원칙</p>'
              + quote("초고를 쓸 때는 내면의 편집자를 방문 밖에 가두어라.")
              + '<p class="small">백지 위에서는 그 어떤 퇴고도 불가능하다. 문장이 거칠고 설정에 구멍이 나더라도 일단 결말의 '
              '마침표까지 달려가 전체 윤곽을 확보하는 것이 최우선이다.</p>')}
        {card('<p style="font-weight:800;margin:0 0 0.5rem;">소설 완성 에너지 배분 비율</p>'
              f'<div style="display:flex;border-radius:0.4rem;overflow:hidden;font-size:0.8rem;font-weight:700;color:#fff;text-align:center;">'
              f'<div style="flex:20;background:{THEME.accent_2};padding:0.4rem 0;">20%</div>'
              f'<div style="flex:30;background:{THEME.accent_3};padding:0.4rem 0;">30%</div>'
              f'<div style="flex:50;background:{THEME.accent};padding:0.4rem 0;">50% (퇴고)</div></div>'
              '<p class="small muted" style="margin:0.6rem 0 0;">기획·구조 설계(20%) · 초고 집필(30%) · 3단계 퇴고 및 윤문(50%) — 진짜 소설은 퇴고에서 태어난다.</p>',
              style="margin-top:0.9rem;")}
        {card('<p style="font-weight:800;color:' + THEME.accent_2 + ';margin:0 0 0.5rem;">필수 과정: 원고 숙성기 (Cooling Off)</p>'
              '<p class="small">초고 완성 직후에는 머릿속 설정과 실제 문장을 구별하지 못한다. 최소 며칠~2주간 원고를 서랍에 '
              '넣어두었다가 ‘낯선 독자의 눈’으로 다시 읽어라.</p>', style=f"background:{THEME.ink_navy};color:{THEME.ink_light};margin-top:0.9rem;")}
      </div>
      <div class="grid" style="gap:0.7rem;">{''.join(pass_html)}</div>
    </div>
    """
    deck.add_slide("revision", "08 3단계 퇴고", body)


def slide_closing(deck):
    habits = [
        ("HABIT 01", "영감이 아닌 ‘분량 루틴’으로 써라", "영감은 기다리는 자가 아니라 쓰고 있는 자에게 찾아온다.",
         ["매일 같은 시간, 같은 장소에서 정해진 분량(예: 하루 1,000자~2,000자 또는 45분)을 채우는 시스템 구축",
          "다음 날 글쓰기가 막막하지 않도록, 오늘 가장 잘 써지는 장면의 문장 중간에서 멈추는 ‘헤밍웨이 기법’ 활용",
          "하루 1,500자씩 60일이면 단편 3편 또는 경장편 1권 분량(원고지 450매)이 완성된다"], THEME.accent),
        ("HABIT 02", "일상을 채집하는 ‘작가의 수집함’", "독창적인 디테일은 책상 위 공상이 아니라 날것의 관찰에서 나온다.",
         ["지하철에서 들은 기묘한 대화 한 줄, 독특한 직업군의 은어, 계절별 빛과 냄새를 메모장에 즉시 기록",
          "마음에 드는 소설을 읽을 때는 독자로서 한 번, 작가로서 ‘어떻게 이 감정을 설계했는가’ 분석하며 한 번 더 필사·해부",
          "막힐 때마다 꺼내 쓸 수 있는 나만의 ‘인물·장면·어휘 창고’를 상시 비축"], THEME.accent_2),
        ("HABIT 03", "미완성 대작보다 ‘완성된 단편 한 편’", "결말까지 도달해 본 경험만이 작가를 다음 단계로 성장시킨다.",
         ["처음부터 거대한 10권짜리 세계관에 매몰되기보다, 원고지 70~100매 분량의 단편으로 기승전결 완주 훈련",
          "첫 초고가 마음에 들지 않는 것은 당신의 재능이 부족해서가 아니라 안목이 높기 때문임을 기억",
          "오늘 당장 주인공의 이름과 그가 처한 첫 번째 작은 위기 한 줄을 적는 것으로 시작하라"], THEME.accent_3),
    ]
    habit_html = []
    for badge, title, q, bullets, col in habits:
        bullets_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        habit_html.append(card(
            f'{pill(badge, col)}<p style="font-weight:800;margin:0.5rem 0 0.6rem;">{esc(title)}</p>'
            + quote(q) +
            f'<ul class="small" style="margin:0.5rem 0 0;padding-left:1.1rem;">{bullets_html}</ul>',
            accent=col, style=f"background:{THEME.bg_dark_card};",
        ))
    body = f"""
    {deck.slide_header("09 | THE WRITER'S HABIT & NEXT STEPS",
                        "완벽한 첫 문장을 기다리지 말고, 지금 당장 첫 장면을 시작하라",
                        "재능보다 강력한 것은 매일 책상 앞에 앉는 루틴과 끝까지 마침표를 찍어본 완주의 근육이다")}
    <div class="grid grid-3">{''.join(habit_html)}</div>
    {card('“최악의 초고라도 백지보다는 언제나 위대하다. 백지는 고칠 수 없지만, 쓰인 문장은 반드시 빛나게 다듬을 수 있다.”'
          '<p style="margin:0.4rem 0 0;font-weight:400;">오늘 당신의 첫 번째 문장을 시작하세요 — Happy Writing!</p>',
          style=f"background:{THEME.accent};color:#fff;text-align:center;font-weight:800;font-size:1.1rem;margin-top:1rem;")}
    """
    deck.add_slide("closing", "09 마무리", body, dark=True)


def main():
    deck = Deck("매혹적인 소설 쓰기의 기술", THEME, footer=FOOTER)
    slide_cover(deck)
    slide_pillars(deck)
    slide_logline(deck)
    slide_character(deck)
    slide_plot_arc(deck)
    slide_scene_dynamics(deck)
    slide_pov(deck)
    slide_show_dont_tell(deck)
    slide_revision(deck)
    slide_closing(deck)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(deck.render())
    print("Saved:", OUT_PATH)


if __name__ == "__main__":
    main()
