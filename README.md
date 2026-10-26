# 소설 창작 PPTX 빌더

소설 작법 가이드와 작품 기획서를 Python으로 재현 가능하게 생성하는 프로젝트입니다.
텍스트 줄바꿈, 높이 측정, 자동 축소 및 겹침 검증은 모두 `ppt_module`에서 담당합니다.

## 환경 준비

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## PPTX 생성

저장 전에 경계 이탈, 텍스트박스 교차, 여러 줄 텍스트의 세로 여유 공간을 검사합니다.
경고가 하나라도 있으면 빌드가 실패하며 PPTX를 저장하지 않습니다.

```bash
python -m ppt_module.builders.novel_guide
python -m ppt_module.builders.custom_novel
python cache_city/build_cache_city_ppt.py
```

생성 결과:

- `소설쓰기_가이드.pptx`
- `맞춤형_소설기획_제안서.pptx`
- `cache_city/캐시의_도시_발전기획서.pptx`

`캐시의 도시`는 독립적인 PNG 미리보기 검사도 지원합니다.

```bash
python cache_city/build_cache_city_ppt.py --preview /tmp/cache_city_preview
```

## 모듈 구성

- `ppt_module/text_metrics.py`: 설치된 한글 폰트를 이용한 줄바꿈·높이 측정
- `ppt_module/textbox.py`: 실제 줄바꿈, 자동 높이, 여러 줄 안전 여백, 자동 축소
- `ppt_module/layout.py`: 커서 기반 세로 배치
- `ppt_module/validate.py`: 경계, 박스 교차, 텍스트 수용 높이 검증
- `ppt_module/builders/`: 루트 산출물을 만드는 실행 모듈
- `cache_city/build_cache_city_ppt.py`: 캐시의 도시 전용 빌더와 이중 미리보기 검사

새 PPTX 빌더를 만들거나 수정할 때는 [AGENTS.md](AGENTS.md)의 규칙을 따릅니다.
