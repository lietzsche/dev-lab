# Python Knowledge Lab

Python 문법을 외우는 데서 끝나지 않고, 하나의 **지식 노트 서비스**를 계속 확장하며 Python의 실행 모델과 백엔드·AI 생태계를 함께 익히는 학습 저장소다.

Java, JavaScript, TypeScript 경험이 있는 개발자를 기준으로 프로그래밍 입문 설명은 줄이고, Python에서 특히 달라지는 아래 주제에 집중한다.

- 이름과 객체, mutability, identity
- dynamic typing과 type hint의 실제 역할
- iterable, iterator, generator와 lazy evaluation
- exception, context manager, decorator
- package, virtual environment, test와 정적 분석
- thread, process, coroutine과 `asyncio`
- HTTP API, MCP tool, LLM application의 경계

## 학습 브랜치

이 저장소는 과목별 장기 브랜치로 학습 자료와 진도를 관리한다.

- `main`: Python
- `learn/git-internals`: Git 내부 구조와 협업 워크플로우
- 향후 다른 과목: `learn/<subject>`

각 과목 브랜치는 독립된 학습 과정이며 서로 병합하지 않는다. 브랜치를 전환해 해당
과목의 문서, 코드 및 진도를 이어서 관리한다.

## 최종적으로 만들 것

학습 중 만드는 코드는 버리지 않고 다음 형태로 성장시킨다.

```text
작은 함수와 자료구조
    ↓
지식 노트 CLI
    ↓
파일·SQLite 저장소
    ↓
동시성·비동기 작업
    ↓
FastAPI 지식 노트 API
    ↓
FastMCP 도구 서버
    ↓
LLM이 검색·요약·도구 호출을 수행하는 애플리케이션
```

최종 결과물의 가칭은 `Knowledge Lab`이다. 노트를 생성하고 태그와 키워드로 검색하며, 같은 application service를 CLI, HTTP, MCP가 서로 다른 adapter로 사용하게 만든다. 마지막에는 LLM이 MCP tool을 통해 노트를 찾고 출처가 포함된 답변을 생성하도록 확장한다.

## 학습 방식

각 소단원 안에서도 개념을 한꺼번에 설명하거나 전체 과제를 먼저 던지지 않는다. 다음 짧은 주기를 한 개념씩 반복한다.

```text
개념 하나 설명 + 대화 속 최소 예제
→ 학습자가 같은 개념을 직접 구현
→ 실행 결과와 코드를 확인
→ 필요한 피드백과 수정
→ 확인된 뒤 다음 개념
```

소단원의 여러 개념을 모두 확인하면 마지막에 실제 프로젝트 코드로 연결하고 검증한다.

기본기 학습 코드는 소단원별 module로 분리한다. `__main__.py`에는 학습 내용을 쌓지 않고 현재 실행할 module을 import해 호출하는 조립 코드만 둔다. 학습이 실제 애플리케이션으로 성장하면 단계별 module의 코드를 `domain`, `application`, `adapters` 같은 역할 중심 module로 옮긴다.

처음부터 FastAPI나 LLM SDK를 사용하지 않는다. 동기 함수와 blocking I/O를 먼저 관찰한 뒤 `asyncio`를 도입하고, HTTP의 request/response 경계를 이해한 뒤 FastAPI를 사용한다. 일반 함수로 tool contract를 설계한 뒤 FastMCP로 노출한다.

학습 과정에서는 아래 질문을 반복한다.

1. 이 이름이 가리키는 객체는 어디에 있고 mutable한가?
2. 상태는 누가 소유하고 변경하는가?
3. 이 코드는 import 시점, 호출 시점, event loop, thread, process 중 어디에서 실행되는가?
4. 실패는 exception, 반환값, HTTP 응답, MCP 오류 중 어느 경계로 전달되는가?

한 번에 한 소단원만 진행한다. 과제와 피드백이 끝나면 완료 상태에서 멈추고, 학습자가 `넘어가자`고 요청하면 다음 단원을 시작한다.

별도의 주관식 학습 일지나 실행 결과 문서는 작성하지 않는다. 이해 여부는 실행 결과와 대화로 확인하며, 소단원이 완료되면 관련 코드와 진도 문서를 검증·커밋하고 원격 저장소에 푸시한다.

## 시작하기

Python 3.12 이상을 권장한다. 저장소 루트에서 setup script를 실행하면 `.venv`를 만들고 package를 editable mode로 설치한다.

```bash
./scripts/setup.sh
source .venv/bin/activate
python -m knowledge_lab
pytest
```

직접 설정할 때는 다음 명령이 같은 작업을 수행한다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[quality,test]"
python -m knowledge_lab
pytest
```

VS Code에서는 workspace를 WSL에서 열고 `.venv/bin/python`을 interpreter로 선택한다. editor와 terminal이 같은 interpreter를 사용하면 `src` layout의 `knowledge_lab` import도 동일하게 해석된다.

설치하지 않고 확인할 때는 다음처럼 실행할 수 있다.

```bash
PYTHONPATH=src python3 -m knowledge_lab
PYTHONPATH=src python3 -m pytest
```

현재 첫 단계와 다음 과제는 [PROGRESS.md](PROGRESS.md), 전체 순서는 [CURRICULUM.md](CURRICULUM.md)를 따른다.

## 저장소 구조

```text
dev-lab/
├── src/knowledge_lab/     # 단계가 진행될수록 성장하는 실제 패키지
│   ├── __main__.py        # 실행할 학습 module을 조립하는 진입점
│   └── lessons/           # 기본기 소단원별 학습 module
├── tests/                 # 표준 unittest에서 시작해 pytest로 확장
├── examples/              # 학습 과정에서 확인을 마친 재사용 가능한 예제
├── scripts/setup.sh       # 가상환경 생성과 editable install 자동화
├── AGENTS.md              # AI와 함께 공부할 때의 진행 규칙
├── CURRICULUM.md          # 전체 학습 로드맵
├── PROGRESS.md            # 현재 학습 위치
└── pyproject.toml         # package와 tool 설정의 정본
```

처음에는 의도적으로 외부 runtime dependency가 없다. FastAPI, Pydantic, FastMCP, LLM SDK 등은 해당 단계에서 역할과 비용을 비교한 뒤 추가한다.

## 현재 검증 명령

```bash
./scripts/check.sh
```

이 script는 source를 수정하지 않고 Ruff formatter, Ruff linter, mypy,
pytest를 차례로 실행한다. 하나라도 실패하면 즉시 non-zero status로 종료한다.
