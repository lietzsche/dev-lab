# Python Backend & AI 학습 로드맵

## 과정 목표

Python 문법을 이해하고, test와 type hint를 활용해 유지보수 가능한 package를 설계하며, 동기·비동기 실행 모델을 설명할 수 있는 상태를 먼저 만든다. 그 기반 위에 동일한 지식 노트 application을 CLI, FastAPI, FastMCP, LLM interface로 확장한다.

완료 기준은 특정 library API를 외우는 것이 아니다. 아래 질문을 자신의 코드와 관찰 결과로 설명할 수 있어야 한다.

- Python의 이름, 객체, 참조, mutability가 상태 변화에 어떤 영향을 주는가?
- module import와 dependency가 언제 실행되고 어디에 cache되는가?
- iterator와 generator는 값과 실행 상태를 어떻게 보존하는가?
- thread, process, coroutine이 어떤 작업에 적합한가?
- domain, persistence, HTTP, MCP, LLM boundary를 왜 분리했는가?
- 실패, timeout, cancellation, retry, 비용을 어디에서 제어하는가?

---

## P1. 실행 모델과 기본 문법

### P1-1. 실행 환경과 첫 module

- interpreter, REPL, script, module의 차이
- `python -m`, `if __name__ == "__main__"`
- expression, statement, indentation
- `print`, `repr`, `type`

### P1-2. 이름, 객체, type

- 변수보다 정확한 개념인 name binding
- dynamic typing: 이름이 아니라 객체가 type을 가진다는 의미
- `None`, `bool`, `int`, `float`, `str`
- `id`, identity와 equality

### P1-3. 함수와 scope

- parameter, return, keyword argument
- local/global/nonlocal scope와 LEGB
- default argument가 정의 시점에 평가되는 문제 재현

### P1-4. 제어 흐름과 pattern matching

- truthiness, `if`, conditional expression
- `for`, `while`, `range`, `enumerate`, `zip`
- `break`, `continue`, loop `else`
- `match`의 적절한 사용 범위

### P1 결과물

- 문자열 명령을 받아 간단한 노트 record를 만들고 출력하는 단일 module
- 실행 방식에 따른 module 실행 시점과 name binding 설명

---

## P2. 핵심 자료구조와 문자열

### P2-1. sequence와 slicing

- `list`, `tuple`, unpacking
- indexing, slicing, shallow copy
- mutable list와 immutable tuple의 실제 차이

### P2-2. mapping과 set

- `dict`, insertion order, key/hashability
- `set`, membership, 집합 연산
- note와 tag를 어떤 구조로 표현할지 비교

### P2-3. 문자열과 byte

- Unicode code point, UTF-8, `str`과 `bytes`
- encode/decode boundary
- 문자열 formatting과 parsing

### P2-4. comprehension

- list/dict/set comprehension
- generator expression과 eager/lazy 차이 예고
- 가독성을 해치는 중첩 표현의 기준

### P2 결과물

- in-memory note collection
- tag 추가, keyword 검색, 정렬과 중복 제거

---

## P3. 객체 모델과 domain modeling

### P3-1. mutability, aliasing, copy

- 같은 객체를 가리키는 여러 이름
- shallow/deep copy
- 함수 인자 전달을 call by sharing으로 이해

### P3-2. class와 instance

- attribute lookup, instance/class attribute
- method와 `self`
- Java class 및 JavaScript prototype과 비교

### P3-3. dataclass와 value object

- `@dataclass`, equality, representation
- `frozen`, `slots`, validation의 한계
- note와 tag domain model

### P3-4. protocol과 composition

- inheritance보다 composition
- duck typing
- `typing.Protocol`을 이용한 structural subtyping

### P3 결과물

- `Note`, `Tag`, `NoteRepository` contract
- dictionary 중심 코드에서 domain object로 리팩터링

---

## P4. 오류, resource, module

### P4-1. exception과 traceback

- `try/except/else/finally`
- exception hierarchy와 `raise ... from ...`
- domain error와 infrastructure error 구분

### P4-2. context manager

- `with`가 resource lifetime을 다루는 방식
- file close 실패 실험
- class 기반 및 generator 기반 context manager

### P4-3. module, package, import

- import가 코드를 실행하고 cache하는 방식
- absolute/relative import
- circular import 문제 재현

### P4-4. project와 dependency

- virtual environment, pip, `pyproject.toml`
- distribution package와 import package
- dependency/lockfile/tool 선택 기준

### P4 결과물

- install 가능한 `knowledge_lab` package
- CLI entry point와 명확한 exception boundary

---

## P5. 함수형 도구와 lazy evaluation

### P5-1. first-class function과 closure

- 함수를 값으로 전달
- closure가 외부 상태를 보존하는 방식
- late binding 문제 재현

### P5-2. iterable과 iterator

- iterable/iterator protocol
- `iter`, `next`, `StopIteration`
- 한 번 소비되는 iterator에서 생기는 버그

### P5-3. generator

- `yield`, suspended execution state
- generator pipeline과 memory 사용 관찰
- `yield from`

### P5-4. decorator

- 함수를 감싸는 호출 구조
- `functools.wraps`
- logging/timing decorator와 framework decorator 연결

### P5 결과물

- 대량 note import를 처리하는 streaming pipeline
- 검색과 변환 pipeline의 eager/lazy 비교

---

## P6. type hint, test, 품질 도구

### P6-1. type hint의 역할

- runtime type과 static analysis의 차이
- union, optional, collection generic
- `Any`가 검사를 끄는 의미

### P6-2. generic과 protocol

- `TypeVar`, generic repository
- `Protocol`, callable type
- runtime validation과 type checking 분리

### P6-3. test 설계

- `unittest`의 arrange/act/assert
- unit/integration test 경계
- fake, stub, mock의 차이
- pytest fixture와 parametrization은 필요성이 생긴 뒤 도입

### P6-4. formatter, lint, type checker

- Ruff와 mypy 설정
- lint rule을 맹목적으로 늘리지 않는 기준
- CI에서 재현 가능한 검증 명령

### P6 결과물

- typed application service
- domain unit test와 repository contract test

---

## P7. 파일과 SQLite persistence

### P7-1. path와 file I/O

- `pathlib`, text/binary mode
- buffering, flush, atomic replace
- serialization과 domain model의 분리

### P7-2. JSON persistence

- JSON type과 Python type 차이
- schema 변경과 잘못된 data 처리
- partial write 문제 재현

### P7-3. SQLite와 transaction

- connection, cursor, parameter binding
- commit/rollback과 transaction boundary
- SQL injection 문제

### P7-4. repository adapter

- in-memory/file/SQLite 구현 교체
- dependency inversion을 과도하지 않게 적용
- migration 기초

### P7 결과물

- CLI에서 사용하는 SQLite note repository
- persistence integration test

---

## P8. 동시성과 비동기

### P8-1. blocking I/O와 thread

- call stack이 기다리는 위치
- `threading`, race condition, lock
- GIL을 만능 설명으로 사용하지 않기

### P8-2. process와 CPU-bound work

- `multiprocessing`과 serialization 비용
- thread/process 선택 실험
- shared state 최소화

### P8-3. coroutine과 event loop

- coroutine object, `async def`, `await`
- task와 event loop
- async code에서 blocking call이 만드는 문제

### P8-4. cancellation, timeout, backpressure

- structured concurrency와 task lifecycle
- timeout/cancellation 전파
- bounded queue와 생산자·소비자

### P8 결과물

- 여러 note source를 동시에 import하는 worker
- sync/thread/process/async 실행 결과 비교 문서

---

## P9. HTTP에서 FastAPI까지

### P9-1. HTTP boundary

- method, path, header, body, status code
- JSON serialization과 network failure
- 작은 표준 라이브러리 HTTP 실험

### P9-2. Pydantic validation

- domain model과 transport schema 분리
- parsing, validation, serialization
- 잘못된 입력의 error model

### P9-3. FastAPI application

- route, dependency, lifespan
- sync/async endpoint의 실행 차이
- application service 연결

### P9-4. API test와 운영 경계

- in-process API test와 실제 network test
- exception handler, logging, config
- timeout, idempotency, pagination

### P9 결과물

- note CRUD/search HTTP API
- OpenAPI schema와 integration test

---

## P10. Architecture와 production basics

### P10-1. configuration과 secret

- environment variable와 settings
- secret을 source와 log에서 분리
- development/test/production 차이

### P10-2. dependency boundary

- domain/application/adapter 책임
- framework type이 core로 새는 문제
- dependency injection의 최소 형태

### P10-3. observability

- structured log, request ID
- latency/error metric 기초
- stack trace와 사용자용 오류 분리

### P10-4. process와 deployment

- ASGI server와 worker
- graceful shutdown
- container, health check, readiness 개념

### P10 결과물

- CLI와 HTTP가 같은 application core를 재사용
- 설정·로그·종료 정책을 가진 서비스

---

## P11. MCP와 FastMCP

### P11-1. tool contract

- MCP가 해결하는 integration 문제
- tool/resource/prompt의 역할
- 평범한 Python 함수로 input/output contract 먼저 설계

### P11-2. FastMCP server

- note search/get/create tool 노출
- schema와 description이 model behavior에 미치는 영향
- stdio와 network transport 비교

### P11-3. 안전한 tool 설계

- read/write tool 구분
- validation, timeout, error, authorization boundary
- prompt injection을 application 권한과 분리

### P11-4. MCP test와 client

- tool을 deterministic하게 직접 test
- protocol integration test
- FastAPI adapter와 중복되지 않는 core 재사용

### P11 결과물

- Knowledge Lab FastMCP server
- API와 MCP가 공유하는 application service

---

## P12. LLM application

### P12-1. model I/O와 비결정성

- message, token, context window
- temperature와 structured output
- model SDK를 adapter로 격리

### P12-2. retrieval

- keyword search baseline
- chunk, embedding, vector similarity
- retrieval와 generation을 분리해 평가

### P12-3. tool calling

- model이 tool을 선택하고 결과를 다시 받는 loop
- 최대 step, timeout, 비용 제한
- tool 결과를 신뢰할 수 없는 input으로 취급

### P12-4. evaluation과 reliability

- fake model을 이용한 deterministic test
- golden dataset과 retrieval metric
- citation, hallucination, prompt injection 관찰

### P12 결과물

- 자신의 노트를 검색하고 출처와 함께 답하는 assistant
- FastMCP tool calling 경로
- offline test와 선택적인 실제 model integration test

---

## 선택 심화

핵심 과정을 완료한 뒤 관심에 따라 하나를 선택한다.

- RAG 심화: hybrid search, reranking, evaluation
- Agent engineering: state machine, durable execution, human approval
- Performance: profiling, memory, serialization, event loop tuning
- Data engineering: batch/stream ingestion, workflow orchestration
- Python internals: descriptor, bytecode, garbage collection, C extension
- 운영 심화: tracing, queue, cache, rate limit, distributed deployment

## 전체 완료 조건

- Python 객체 모델과 실행 시점을 Java/JavaScript/Rust와 비교해 설명한다.
- typed, tested package를 만들고 파일·SQLite adapter를 교체할 수 있다.
- blocking/thread/process/async 모델을 workload에 따라 선택할 수 있다.
- 하나의 application core를 CLI, FastAPI, FastMCP에서 재사용한다.
- 외부 LLM 없이도 retrieval/tool logic을 test하며, 실제 model 호출의 비용·실패·보안 경계를 설명한다.
