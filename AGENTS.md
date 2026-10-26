# AGENTS.md

이 저장소에서 소설 작법 가이드/기획서 문서를 만들거나 수정할 때 반드시 지켜야 할 규칙입니다.

## 배경: 왜 PPTX를 버리고 HTML로 왔는가

이 프로젝트는 원래 python-pptx로 PPTX를 생성했다. 겹치는 텍스트, 칸 밖으로 넘치는
글자 문제를 고치려고 `ppt_module`(텍스트 측정, 자동 높이 계산, 자동 축소, 겹침
검증기)을 만들어 수차례 보강했지만, 근본 원인은 PPTX/python-pptx 자체에 있었다:

- python-pptx 텍스트박스는 좌표를 손으로 지정해야 하고, 실제 렌더링 폭/줄높이는
  뷰어(PowerPoint·LibreOffice)마다 달라서 아무리 정교하게 측정해도 100% 일치시킬 수 없다.
- 텍스트박스의 기본 자동맞춤(`<a:spAutoFit/>`)이 렌더링 시점에 도형 크기 자체를
  다시 키워버려, 저장 시점에 계산한 높이가 열어볼 때는 무의미해지는 경우가 있었다.

**그래서 이 저장소는 PPTX를 완전히 버리고 HTML/CSS로 옮겼다.** 브라우저는 텍스트를
스스로 흘려 담는다(reflow) — 겹침이나 칸 밖 이탈이라는 문제 자체가 발생하지 않는다.
옛 `ppt_module`과 세 개의 `.pptx` 산출물, 그 빌더 스크립트는 모두 삭제했다. 지금 이
저장소의 문서 생성 수단은 `html_module`뿐이다.

## `html_module/` 사용 규칙

1. **새 문서/기획서 스크립트는 반드시 `html_module`을 쓴다.** `Deck`(섹션을 모아 한
   장의 HTML로 조립), `components.py`의 `card`/`pill`/`grid`/`kv_list`/`quote`/
   `compare_table`을 재사용하라. raw `<div>`/`<table>` 문자열을 매번 새로 조립하지
   말고, 이미 있는 헬퍼로 표현 가능한지 먼저 확인할 것.
2. **텍스트는 escape해서 넣는다.** `html_module.esc()`를 거치지 않은 사용자/컨텐츠
   문자열을 그대로 f-string에 꽂지 말 것 (XSS와 무관하더라도, `<`/`&` 같은 문자가
   깨진 HTML을 만든다). `esc()`는 `"\n"`도 `<br>`로 바꿔준다.
3. **좌표를 계산하지 않는다.** 레이아웃은 CSS grid/flexbox(`grid grid-2/3/4` 클래스)
   로 표현한다. 폭·높이를 px/in로 지정하거나 줄바꿈 위치를 직접 계산하는 코드를
   추가했다면 설계가 잘못된 것 — 그 문제는 브라우저가 이미 풀어준다.
4. **색/폰트는 `html_module.theme.Theme`를 쓴다.** 덱마다 `NOVEL_GUIDE_THEME`,
   `CUSTOM_NOVEL_THEME`, `CACHE_CITY_THEME` 같은 팔레트가 이미 있다. 새 덱을 만들
   때 `RGBColor`/hex 상수를 새로 복붙하지 말고 `Theme(...)`를 하나 더 정의하라.
5. **빌더는 `html_module/builders/` 또는 해당 프로젝트 폴더(예: `cache_city/`)에
   둔다.** 출력 파일은 스크립트 위치 기준 상대경로로 계산해 저장할 것 — 절대경로를
   하드코딩하지 않는다.
6. **검증은 따로 필요 없다.** `ppt_module.validate` 같은 겹침 검사기는 존재하지
   않는다 — HTML/CSS 자체가 겹침을 만들지 않기 때문이다. 다만 생성 후
   `python3 -c "html=open(path,encoding='utf-8').read(); ..."` 같은 간단한 구조
   점검(여는/닫는 태그 균형, `</html>` 존재)은 커밋 전에 한 번 돌려 확인하는 습관을
   유지하라.

## 모듈 구성

| 파일 | 역할 |
| --- | --- |
| `html_module/theme.py` | 덱별 색상 팔레트(`Theme`), 웹 폰트 스택(`FONT_STACK`) |
| `html_module/render.py` | `esc()`, 섹션을 모아 TOC 포함 한 장의 HTML로 조립하는 `Deck` |
| `html_module/components.py` | `card`, `pill`, `grid`, `kv_list`, `quote`, `compare_table` |
| `html_module/builders/novel_guide.py` | 《매혹적인 소설 쓰기의 기술》 생성 → `소설쓰기_가이드.html` |
| `html_module/builders/custom_novel.py` | 《비문학의 사유에서 소설의 서사로》 생성 → `맞춤형_소설기획_제안서.html` |
| `cache_city/build_cache_city_html.py` | 《캐시의 도시》 발전 기획서 생성 → `cache_city/캐시의_도시_발전기획서.html` |

## 《캐시의 도시》 기획서의 챕터 구조

`cache_city/build_cache_city_html.py`는 원래 8장면 요약 카드였던 플롯을 챕터
구조로 다시 짰다. `EARLY_CHAPTERS`(1~4장, 초반부: 일상 → 병목 → 가짜 해결 → 바깥과의
접촉)는 각 챕터마다 장소/시간, POV, 비트 단위 전개, 핵심 디테일, 작가가 정할 열린
질문까지 담아 실제로 쓰기 시작할 수 있는 수준으로 확장했다. `LATE_CHAPTERS`(5~8장,
후반부)는 기존 카드 수준 요약을 유지한다 — 다음 라운드에서 초반부와 같은 깊이로
확장할 대상. 이 구조를 더 다듬을 때는 `EARLY_CHAPTERS`/`LATE_CHAPTERS` 딕셔너리에
필드를 추가/수정하고, `slide_chapters_early`/`slide_chapters_late`가 그 필드를
그대로 렌더링하는지 확인할 것.

## 과거 PPTX 산출물에 대한 방침

`ppt_module`, 세 개의 `.pptx` 파일, PPTX 빌더 스크립트는 저장소에서 완전히
삭제했다 (git 히스토리에는 남아 있다). 되돌리거나 PPTX를 다시 생성해야 하는 요청이
오면, 삭제 이전 커밋에서 해당 파일들을 복원하기보다는 — 왜 PPTX가 필요한지 먼저
확인하라. 이 문서 맨 위의 배경 설명대로, PPTX 자동맞춤 문제는 모듈 코드로는 완전히
해결되지 않았다.
