# 소설 창작 HTML 기획서 빌더

소설 작법 가이드와 작품 기획서를 Python으로 재현 가능하게 생성하는 프로젝트입니다.
PPTX에서 HTML로 전환했습니다 — 브라우저가 텍스트를 직접 흘려 담기 때문에
좌표 계산이나 겹침 검증이 필요 없고, 외부 라이브러리 설치 없이(표준 라이브러리만)
생성·조회할 수 있습니다.

## 환경 준비

추가 설치가 필요 없습니다. Python 3 표준 라이브러리만 사용합니다.

## HTML 생성

```bash
python3 html_module/builders/novel_guide.py
python3 html_module/builders/custom_novel.py
python3 cache_city/build_cache_city_html.py
```

생성 결과:

- `소설쓰기_가이드.html`
- `맞춤형_소설기획_제안서.html`
- `cache_city/캐시의_도시_발전기획서.html`

생성된 `.html` 파일은 더블클릭하거나 브라우저로 바로 열어서 보면 됩니다.

## 모듈 구성

- `html_module/theme.py`: 덱별 색상 팔레트 (`Theme`), 웹 폰트 스택
- `html_module/render.py`: 섹션들을 모아 사이드 TOC가 있는 한 장의 HTML로 조립하는 `Deck`
- `html_module/components.py`: `card`, `pill`, `grid`, `kv_list`, `quote`, `compare_table` 등 재사용 스니펫
- `html_module/builders/`: 루트 산출물(`소설쓰기_가이드`, `맞춤형_소설기획_제안서`)을 만드는 실행 모듈
- `cache_city/build_cache_city_html.py`: 《캐시의 도시》 발전 기획서 전용 빌더 (챕터 구조)

새 HTML 빌더를 만들거나 수정할 때는 [AGENTS.md](AGENTS.md)의 규칙을 따릅니다.
