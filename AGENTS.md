# AGENTS.md

이 저장소에서 PPTX(파워포인트) 문서를 만들거나 수정하는 작업을 할 때 반드시 지켜야 할 규칙입니다.

## 배경: 왜 이 문서가 필요한가

`ppt_module/builders/novel_guide.py`, `ppt_module/builders/custom_novel.py`는 과거 모든 도형/텍스트박스의 좌표(`left`, `top`,
`width`, `height`)를 손으로 추측한 상수로 박아넣은 스크립트입니다. 이 방식에는 두 가지 구조적
결함이 있고, 실제로 지금 산출물에서 "글자가 위아래로 겹치거나 칸 밖으로 나가는" 증상으로
나타나고 있습니다.

1. **여러 줄 문자열의 `\n`이 실제 줄바꿈이 아닙니다.** `run.text = "1번째 줄\n2번째 줄"`처럼
   하나의 run에 `\n`을 섞어 넣으면 python-pptx는 `<a:t>` 안에 리터럴 개행 문자를 그대로
   써버립니다. PowerPoint/LibreOffice는 이걸 줄바꿈으로 렌더링하지 않고 그냥 이어 붙여버립니다.
   두 스크립트에 이 패턴이 수십 군데 있습니다(`grep -c '\\n' build_*.py`로 확인 가능). 즉
   작성자가 "3줄짜리 텍스트"라고 가정하고 박스 높이를 잡아도, 실제로는 1줄로 뭉쳐지거나 전혀
   다른 폭에서 재줄바꿈되어 계산한 높이와 실제 렌더링 높이가 어긋납니다.
2. **박스 높이가 텍스트 길이·글자 크기·줄바꿈 폭과 아무 관계 없이 손으로 찍은 상수입니다.**
   텍스트가 작성자의 추측보다 길어지면 박스 밖으로 조용히 흘러넘쳐 바로 아래에 배치된 다른
   도형과 겹칩니다. 검증 코드가 전혀 없어서 이런 겹침이 빌드 시점에는 드러나지 않습니다.

위 두 문제를 근본적으로 해결한 재사용 가능한 모듈을 `ppt_module/`에 만들었고, 이 저장소의 pptx를
생성하는 세 스크립트 — `ppt_module/builders/novel_guide.py`, `ppt_module/builders/custom_novel.py`,
`cache_city/build_cache_city_ppt.py` — 모두 이미 `ppt_module/` 기반으로 재작성되어 있습니다.
**앞으로 이 스크립트들을 더 손보거나 새 PPTX 스크립트를 만들 때도 반드시 `ppt_module/`을
사용해야 합니다.** `slide.shapes.add_textbox(...)`와 `run.text = ...`를 직접 호출하는 코드를
새로 추가하지 마세요 — 같은 버그를 또 재생산하게 됩니다.

## `ppt_module/` 사용 규칙

1. **좌표를 손으로 추측해서 쌓지 말 것.** 세로로 쌓이는 블록들은 `ppt_module.layout.VStack`을
   쓰세요. `VStack.add_textbox(...)`/`add_rect(...)`는 실제로 렌더링된 높이만큼 커서를
   전진시키므로, 구조적으로 같은 스택 안에서는 겹침이 발생할 수 없습니다.
2. **텍스트에 여러 줄이 필요하면 `\n`을 문자열에 그대로 써도 됩니다** — 단,
   `ppt_module.textbox.add_textbox` (또는 `VStack.add_textbox`)를 통해서만요. 이 함수는
   `\n`마다 독립된 DrawingML 문단(`<a:p>`)과 문단 간 여백을 생성합니다. `<a:br/>`를 무시해
   앞뒤 문자열을 붙이는 일부 OOXML 뷰어에서도 줄바꿈이 보존됩니다. `shapes.py`의 `add_rect`를 제외하고, 텍스트를
   그리는 코드에서 `slide.shapes.add_textbox(...)`와 `run.text = ...`를 직접 호출하지 마세요.
3. **박스 높이는 되도록 지정하지 말고 모듈이 계산하게 두세요.** `height=`를 생략하면
   `add_textbox`가 `text_metrics`로 실제 줄바꿈 결과를 측정해 필요한 높이를 계산합니다. 디자인상
   고정 높이가 꼭 필요한 칸(예: 표 셀, 카드)에만 `height=`/`max_height=`를 지정하세요 — 이 경우
   텍스트가 안 맞으면 조용히 흘러넘치는 대신 `min_size_pt`까지 글자 크기를 자동으로 줄이고,
   그래도 안 맞으면 콘솔에 경고를 찍습니다. **이 경고가 보이면 반드시 원인(텍스트를 줄이거나,
   박스를 키우거나, 폰트를 더 줄이거나)을 해결하고 넘어가세요.**
4. **슬라이드/프레젠테이션을 저장하기 전에 항상 검증을 돌리세요.**
   ```python
   from ppt_module import validate
   warnings = validate.check_presentation(prs)
   assert not warnings, warnings
   prs.save(out_path)
   ```
   `check_presentation`은 모든 슬라이드의 모든 도형이 슬라이드 경계 밖으로 나가는지, 텍스트를
   담은 두 박스가 겹치는지를 검사합니다. VStack을 안 쓰고 좌표를 손으로 찍은 부분이 있다면
   이 검사에서 반드시 잡아내야 합니다. 경고가 하나라도 남아있는 상태로 작업을 끝내지 마세요.
5. **색/폰트는 `ppt_module.theme.Theme`를 이용하세요.** 기존 두 스크립트처럼 매 파일마다
   `RGBColor(...)` 상수를 새로 복붙하지 말고, `DEFAULT_THEME`를 쓰거나 필요하면 `Theme(...)`로
   새 팔레트를 만들어 쓰세요.

## 참고 예제

`ppt_module/example_build.py`가 위 패턴을 그대로 보여주는 실행 가능한 예시입니다.

```bash
python3 -m venv .venv && source .venv/bin/activate   # 또는 기존 가상환경 사용
pip install python-pptx Pillow
python3 -m ppt_module.example_build
```

`/tmp/ppt_module_example.pptx`가 생성되고, 콘솔에 `validate: no overlap/out-of-bounds issues
found.`가 출력되어야 정상입니다. 새 슬라이드 빌더를 작성할 때는 이 파일을 그대로 베이스로
복사해서 시작하세요 (`build_slide_* ` 함수 하나에 `VStack` 하나 또는 여러 개를 두는 구조).

## 모듈 구성

| 파일 | 역할 |
| --- | --- |
| `ppt_module/theme.py` | 색상 팔레트(`Theme`, `DEFAULT_THEME`), 폰트 이름, 슬라이드 크기 상수 |
| `ppt_module/text_metrics.py` | Pillow 기반 실제 word-wrap 시뮬레이션 + 텍스트 블록 높이 계산 |
| `ppt_module/shapes.py` | `add_rect`, `set_font`, `set_slide_background`, `disable_shadow` |
| `ppt_module/textbox.py` | 실제 줄바꿈 + 자동 높이/자동 축소를 지원하는 `add_textbox` |
| `ppt_module/layout.py` | 겹침을 구조적으로 막는 `VStack` 커서 레이아웃 |
| `ppt_module/validate.py` | 슬라이드 경계 밖/텍스트 겹침을 검사하는 `check_slide`/`check_presentation` |
| `ppt_module/example_build.py` | 위 전부를 사용하는 실행 가능한 최소 예제 |

## 세 스크립트의 현재 상태

- `ppt_module/builders/novel_guide.py`, `ppt_module/builders/custom_novel.py`, `cache_city/build_cache_city_ppt.py`
  모두 `ppt_module`에 위임하는 호환 래퍼(`add_textbox`/`rect`/`text` 등, 파일마다 이름은
  다르지만 내부 구현은 전부 `ppt_module.textbox.add_textbox` / `ppt_module.shapes.add_rect`)로
  이미 교체되어 있습니다. 각 파일의 `main()`은 저장 직전에 `validate.check_presentation(prs)`를
  호출해 경고를 출력합니다 — 아무것도 안 뜨면 정상입니다.
- 셋 다 자체 팔레트(`RGBColor` 상수)와 `add_header_and_footer`/`header()` 같은 슬라이드별
  헬퍼는 그대로 유지했습니다 (완전히 `ppt_module.theme.Theme`/`VStack`으로 통일하는 재설계는
  하지 않았음) — 다만 좌표 계산이 필요한 모든 지점에서 실측 높이(`measure_block_height_in`)를
  쓰도록 바꿨습니다.
- 이미 생성된 세 `.pptx` 파일을 고치려면, 해당 슬라이드를 만드는 함수를 고친 뒤 스크립트를
  재실행해서 pptx를 다시 생성하세요 (`python3 -m ppt_module.builders.novel_guide` 등, 각 스크립트는 저장 경로를
  스크립트 자신의 위치 기준 상대경로로 계산합니다). 기존 pptx 파일을 바이너리로 직접 패치하지
  마세요.
- `cache_city/build_cache_city_ppt.py --preview DIR`는 이 스크립트 자체에 내장된, 독립적인
  PNG 미리보기 + 글자 넘침 점검 도구입니다. `ppt_module.validate`와 측정 공식이 달라 좋은
  이중 검증 수단이니, 이 파일을 고칠 때는 두 검사를 모두 통과시키세요.

## 측정 모델에 대한 주의사항

`ppt_module.text_metrics`의 `_LEADING_FACTOR`(1.3)와 `safety_margin`(1.12)은 임의의 값이
아니라, 실제 렌더링에서 여전히 겹침이 보고된 뒤 보정한 값입니다. 한글/CJK 폰트는 Latin
폰트보다 줄 높이가 커서 1.2 같은 Latin 기준값으로는 2줄 이상인 텍스트에서 실제 렌더링보다
낮게 추정하는 경향이 있었습니다. 이 상수를 다시 낮추고 싶다면, 먼저 실제 PowerPoint/
LibreOffice 렌더 결과로 검증하세요 — `validate.check_presentation`이 통과해도 이 상수 자체가
낙관적이면 실제 문서에서는 여전히 겹칠 수 있습니다.
