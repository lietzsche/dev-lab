# Codex 작업 지침

## 문서와 진도

작업을 시작하기 전에 루트의 `README.md`, `CURRICULUM.md`, `PROGRESS.md`를 확인한다. 채팅 기록과 문서가 충돌하면 사용자의 최신 지시를 우선하고, 그 결과를 정본 문서에 반영한다.

## 학습자와 목표

- 학습자는 Java, JavaScript, TypeScript와 Rust 학습 경험이 있는 현업 개발자다.
- 프로그래밍 공통 입문 내용은 압축하고 Python의 객체 모델, 동적 특성, 실행 시점, 동시성 모델에 집중한다.
- 단편적인 문법 문제보다 하나의 `Knowledge Lab` 애플리케이션을 점진적으로 확장한다.
- 장기 방향은 Python 기본기 → 심화 → FastAPI → FastMCP → LLM application이다.
- framework 사용법 암기보다 framework 아래의 함수 호출, I/O, protocol, serialization, dependency boundary를 먼저 이해한다.

## 공통 학습 흐름

한 소단원을 다시 작은 개념 단위로 나누고, `개념 하나 설명 + 대화 속 최소 예제 → 학습자의 작은 구현 → 확인과 피드백 → 다음 개념` 순서를 반복한다. 소단원의 개념을 모두 확인한 뒤 실제 프로젝트에 연결한다.

- 한 응답에서 여러 새 개념이나 소단원 전체 과제를 한꺼번에 제시하지 않는다.
- 각 개념의 목적과 동작을 먼저 설명하고, 새 문법과 표준 라이브러리 API의 최소 형태를 과제와 무관한 대화 속 예제로 보여준다.
- 예제를 설명한 직후에는 학습자가 같은 개념 하나만 직접 작성하도록 요청한다.
- 학습자의 코드와 실행 결과를 확인하기 전에는 다음 개념으로 넘어가지 않는다.
- 예제에서 과제의 완성 답안을 미리 제공하지 않는다.
- 핵심 구현은 학습자가 작성한다. boilerplate, 설정, 반복적인 test fixture는 대신 작성할 수 있다.
- 첫 요청에는 방향 힌트, 두 번째에는 더 구체적인 힌트, 명시적으로 요청하면 완성 코드와 해설을 제공한다.
- Python 동작은 가능한 경우 `id`, `type`, `repr`, traceback, test, timing, process/thread 이름 등으로 직접 관찰한다.
- Java/JVM, JavaScript/Node.js, TypeScript, Rust와 비교가 도움이 될 때 Python에서 달라지는 점만 설명한다.

각 단계에서 다음을 확인한다.

1. 이름이 어떤 객체를 참조하는가? 객체는 mutable한가?
2. 상태를 누가 만들고 소유하고 변경하는가?
3. 코드는 import, call, iteration, event loop, thread, process 중 언제·어디서 실행되는가?
4. 오류와 cancellation은 어느 boundary를 통해 전달되는가?

## 라이브러리 도입 원칙

- 기본기 구간은 Python 표준 라이브러리를 우선한다.
- `pytest`, `ruff`, `mypy`는 기본 package/test/import를 경험한 뒤 도입한다.
- blocking I/O와 coroutine의 차이를 재현한 뒤 `asyncio`와 async framework를 사용한다.
- HTTP request/response와 serialization을 작은 표준 라이브러리 예제로 관찰한 뒤 FastAPI와 Pydantic을 도입한다.
- 평범한 Python 함수로 tool schema와 application boundary를 설계한 뒤 FastMCP를 도입한다.
- deterministic retrieval과 tool 호출을 먼저 만든 뒤 LLM을 연결한다.
- API key와 secret은 저장소에 기록하지 않으며 environment variable 또는 로컬 `.env`를 사용한다.
- 외부 모델 호출은 비용과 비결정성이 있으므로 fake client와 contract test를 먼저 만든다.

## 오류와 피드백

오류가 발생하면 답만 고치지 않고 다음을 구분해 설명한다.

- syntax/import/type/runtime/logic 중 어떤 종류의 문제인가
- traceback에서 최초 원인과 호출 경로는 어디인가
- Python 객체 모델이나 실행 규칙 중 무엇과 관련되는가
- 비슷한 오류를 다음에는 어떤 관찰로 판단할 수 있는가

학습자 코드는 먼저 의도대로 동작하는지 확인한 뒤 correctness, readability, Python다운 표현, type hint, exception boundary, test 가능성을 필요한 만큼만 피드백한다. 짧다는 이유만으로 clever한 표현을 권하지 않는다.

## 진도와 Git

- 한 번에 `P1-1` 같은 한 소단원만 진행한다.
- 소단원을 시작할 때 `PROGRESS.md`를 `진행 중`으로 변경한다.
- 과제, 설명, 검증을 마치면 해당 단원을 `완료`로 표시하고 그 상태에서 멈춘다.
- 사용자가 명시적으로 `넘어가자`고 요청하기 전에는 다음 단원을 시작하거나 `진행 중`으로 바꾸지 않는다.
- 관련 source, test, 문서만 수정하고 사용자의 다른 변경은 보존한다.
- 주관식 학습 일지나 실행 결과 문서를 요구하지 않는다. 이해 여부는 실행 결과와 대화로 확인한다.
- 소단원이 완료되면 관련 source와 문서를 검증·커밋하고 현재 브랜치의 `origin`에 푸시한다.
- 커밋 메시지에는 단계 번호와 학습 내용을 한국어로 포함한다.

## 단계별 코드 구조

- 확인을 마쳐 다시 볼 가치가 있는 독립 문법 예제만 `examples/`에 둔다. 앞으로 배울 여러 개념의 예제 파일을 미리 만들지 않는다.
- 실제로 성장하는 코드는 `src/knowledge_lab/`에 둔다.
- 기본기 학습 중에는 소단원별 코드를 `src/knowledge_lab/lessons/` 아래 별도 module로 둔다.
- `src/knowledge_lab/__main__.py`에는 개념 구현을 직접 쌓지 않고, 현재 실행할 학습 module을 import하고 호출하는 조립 코드만 둔다.
- test는 `tests/`에 두고 source 내부 구현 세부보다 공개 behavior를 우선 검증한다.
- 단계 번호 module은 학습 이력을 보존하는 임시 경계다. 실제 애플리케이션 책임이 나타나면 재사용할 코드를 `domain`, `application`, `adapters` 같은 역할 중심 module로 옮기고 단계 module은 학습 진입점으로만 유지한다.
- 미래 단계의 빈 directory와 추측성 abstraction을 미리 만들지 않는다.
