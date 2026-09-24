# 전체 학습 진행 상황

## 현재

- 프로젝트: Python Knowledge Lab
- 단계: P10-4 process와 deployment
- 상태: 완료

## 준비된 기반

- 전체 P1~P12 로드맵
- install 가능한 `src` layout package
- `python -m knowledge_lab` 실행 진입점
- 표준 라이브러리 기반 smoke test

## 완료한 내용

### P1-1. 실행 환경과 첫 module

- interpreter, REPL, script, module의 차이를 실행으로 확인한다.
- `python -m knowledge_lab`이 어떤 파일을 어떤 이름으로 실행하는지 관찰한다.
- expression, statement, indentation과 `repr`, `type`의 기본 형태를 익힌다.
- 독립 예제 `examples/p1_1_execution.py`의 실행 방식별 결과를 비교한다.
- `src/knowledge_lab/__main__.py`에 첫 note의 제목과 내용을 출력하는 코드를 직접 작성한다.

### P1-2. 이름, 객체, type

- 이름을 `str`과 `int` 객체에 차례로 binding하고 runtime type을 확인했다.
- 값이 없음을 나타내는 `None` 객체와 `is None`을 확인했다.
- `True`와 `False`가 `bool` 타입의 객체임을 확인했다.
- 소수점 표기를 가진 숫자가 `float` 타입의 객체임을 확인했다.
- 두 이름이 같은 객체를 가리킬 때 `id`가 같고 `is`가 `True`임을 확인했다.
- 값은 같지만 서로 다른 객체에서 `==`는 `True`, `is`는 `False`임을 확인했다.

### P1-3. 함수와 scope

- argument와 parameter의 binding, 반환 객체가 호출 위치에 연결되는 흐름을 확인했다.
- positional argument와 keyword argument의 연결 방식을 확인했다.
- local, global, enclosing, Builtins로 이름을 찾는 LEGB 규칙을 확인했다.
- 대입문으로 인해 local 이름이 판정되는 시점과 `UnboundLocalError`를 재현했다.
- `global`과 `nonlocal`의 rebinding을 확인하고, 반환값으로 상태 소유권을 명확히 하는 방식을 적용했다.
- default argument가 함수 정의 시점에 평가되어 mutable 객체가 재사용되는 문제를 재현했다.
- `None` 기본값을 사용해 호출 시점마다 새 mutable 객체를 생성하도록 수정했다.

### P1-4. 제어 흐름과 pattern matching

- 문자열의 truthiness와 `if`, conditional expression을 확인했다.
- `for`, `while`, `range`, `enumerate`, `zip`의 iteration과 이름 binding을 확인했다.
- `zip`의 짧은 입력 기준 종료와 `strict=True`의 iteration 시점 `ValueError`를 확인했다.
- `break`, `continue`, `for ... else`의 서로 다른 loop 경계를 확인했다.
- `match`의 literal, wildcard, OR pattern을 적용하고 단순 조건문과의 사용 범위를 구분했다.

### P2-1. sequence와 slicing

- list와 tuple의 생성, indexing, negative indexing을 객체 identity로 확인했다.
- slicing 범위가 start 포함·stop 제외이며 새 outer list를 만드는 것을 확인했다.
- shallow copy가 내부 mutable 객체를 공유하는 상태 변경을 재현했다.
- list의 요소 참조는 교체할 수 있지만 tuple의 요소 대입은 `TypeError`가 됨을 확인했다.
- tuple이 참조하는 내부 mutable 객체의 상태는 변경될 수 있음을 확인했다.
- 기본 unpacking의 binding과 개수 불일치 `ValueError`, starred unpacking의 나머지 list를 확인했다.

### P2-2. mapping과 set

- dict의 key-value 연결, insertion order, value 교체, `items()` unpacking을 확인했다.
- dict membership이 key를 검사하며, 누락 key의 직접 조회는 `KeyError`, `get()`은 `None`을 반환함을 확인했다.
- mutable list key의 `TypeError`와 hashable tuple key, mutable list value를 확인했다.
- set의 중복 제거, membership, `add()`와 intersection, union, difference를 확인했다.
- note를 dict로, tags를 set으로 표현하고 `find_missing_tags()`에서 누락 tag를 새 set으로 계산했다.

### P2-3. 문자열과 byte

- Unicode `str`의 code point 길이와 UTF-8 `bytes`의 바이트 길이를 비교했다.
- `encode()`와 `decode()`의 변환 방향 및 값이 보존되는 왕복 경계를 확인했다.
- 잘못된 UTF-8을 decode해 호출 시점의 `UnicodeDecodeError`와 실패 위치를 확인했다.
- f-string의 `!r` 변환과 `str.partition()`의 반환 tuple 및 구분자 누락 표현을 확인했다.
- UTF-8 payload를 note dict로 변환하는 `parse_note_payload()`를 구현하고 형식 실패를 `None`으로 구분했다.

### P2-4. comprehension

- list comprehension의 eager 평가, 변환, 필터와 새 list 생성을 확인했다.
- dict comprehension으로 제목별 길이 mapping을 만들고 set comprehension으로 정규화와 중복 제거를 수행했다.
- generator expression의 lazy 평가, 일부 소비, 남은 값의 계산과 소진 상태를 확인했다.
- 중첩 set comprehension의 순서와 가독성 범위를 확인하고 `sorted()`로 안정적인 새 list를 만들었다.
- in-memory note collection에서 대소문자 무시 keyword 검색 결과를 정렬하는 `search_note_titles()`를 구현했다.

### P3-1. mutability, aliasing, copy

- 여러 이름이 같은 mutable 객체를 참조할 때 한 경로의 변경이 다른 경로에서도 관찰되는 aliasing을 확인했다.
- shallow copy가 바깥 collection만 복사하고 내부 mutable 객체는 공유하는 것을 확인했다.
- 중첩된 tag collection까지 독립적으로 소유하도록 복사 경계를 구현했다.
- 함수 인자 전달을 객체 참조가 공유되는 call by sharing으로 확인했다.

### P3-2. class와 instance

- instance와 class attribute의 lookup 순서 및 instance별 상태 소유권을 확인했다.
- method 호출에서 instance가 `self` parameter에 binding되는 것을 확인했다.
- note마다 독립적인 title과 tag collection을 소유하도록 구현했다.

### P3-3. dataclass와 value object

- dataclass가 생성하는 초기화, representation, equality 동작을 확인했다.
- `Tag`를 값으로 비교하고 빈 이름을 검증하는 value object로 구현했다.
- `Note`가 자신의 tag collection을 소유하고 동등한 tag의 중복을 방지하도록 구현했다.

### P3-4. protocol과 composition

- 명시적 상속 없이 같은 동작을 제공하는 duck typing과 structural compatibility를 확인했다.
- `Protocol`의 runtime 검사는 method signature 전체를 보장하지 않는 한계를 재현했다.
- `NoteRepository` contract와 in-memory 구현을 만들고 collection 소유권을 확인했다.
- `NoteService`가 repository를 composition으로 전달받아 저장과 조회를 위임하도록 구현했다.

### P4-1. exception과 traceback

- `raise` 이후 정상 반환이 중단되고 처리되지 않은 exception이 module 실행 경계까지 전파되는 것을 확인했다.
- traceback에서 최초 원인의 type과 message 및 위쪽 frame의 호출 경로를 구분했다.
- `try/except/else/finally`의 정상·실패 경로와 정리 시점을 확인했다.
- 사용자 정의 domain exception과 exception hierarchy를 적용했다.
- `raise ... from ...`과 `__cause__`로 변환 전 원인 객체가 보존되는 것을 확인했다.
- `KeyError`를 `NoteNotFoundError`로 변환해 infrastructure 세부사항과 domain 의미를 분리했다.
- title 검증과 exception chaining의 공개 behavior를 test로 검증했다.

### P4-2. context manager

- `with` 진입 전, block 내부, 정상·예외 종료 후의 resource 상태를 관찰했다.
- class 기반 context manager에서 `__enter__`와 `__exit__`의 호출 및 소유권 경계를 확인했다.
- `__exit__` 반환값에 따른 exception 전파와 억제를 비교했다.
- generator 기반 context manager가 `finally`에서 resource를 해제하는 것을 확인했다.
- class 및 generator 기반 context manager의 공개 behavior를 test로 검증했다.

### P4-3. module, package, import

- module 최상위 코드와 함수 본문의 import·call 실행 시점을 구분했다.
- 같은 process의 import cache가 동일한 module 객체를 반환하는 것을 identity로 확인했다.
- `__name__`과 `__package__`로 module 정규 이름과 package 경계를 관찰했다.
- absolute import와 relative import가 같은 module 객체로 해석되는 것을 확인했다.
- 파일 직접 실행에는 알려진 parent package가 없어 relative import가 실패하는 것을 재현했다.
- circular import에서 부분 초기화된 module의 아직 생성되지 않은 attribute 접근 오류를 재현했다.
- 불필요한 반대 방향 dependency를 제거해 module 초기화 순서를 한 방향으로 만들었다.
- module dependency의 초기화 순서를 공개 behavior test로 검증했다.

### P4-4. project와 dependency

- distribution 이름과 import package 이름이 서로 다른 설치·실행 경계의 식별자임을 확인했다.
- virtual environment의 interpreter, 현재 prefix, 기반 prefix를 직접 비교했다.
- editable install이 `.venv`의 distribution metadata와 작업 중인 source를 연결하는 것을 확인했다.
- `pyproject.toml`의 build system, project metadata, runtime dependency 역할을 구분했다.
- build dependency가 runtime 환경에 반드시 설치되는 것은 아님을 격리된 build 경계로 설명했다.
- 선언된 runtime dependency와 설치된 distribution metadata를 비교했다.
- project script metadata가 `.venv/bin/knowledge-lab` console wrapper로 생성되는 것을 확인했다.
- 현재 dependency graph에는 lockfile이 필요하지 않다고 판단하고 `pip check`로 설치 정합성을 검증했다.
- project metadata와 CLI entry point 경계를 공개 behavior test로 검증했다.

### P5-1. first-class function과 closure

- 함수 이름과 별칭이 같은 함수 객체를 참조하는 것을 identity로 확인했다.
- 함수 객체를 argument와 반환값으로 전달하고 실제 호출 시점을 구분했다.
- 내부 함수가 외부 함수 호출 이후에도 closure cell을 통해 상태를 보존하는 것을 확인했다.
- factory 호출마다 독립적인 함수 객체와 closure cell이 생성되는 것을 확인했다.
- loop의 여러 함수가 같은 cell을 공유해 마지막 값을 읽는 late binding 문제를 재현했다.
- 별도의 factory 호출로 각 함수가 독립적인 cell을 소유하도록 late binding을 해결했다.
- `nonlocal` rebinding으로 closure가 여러 호출 사이의 count 상태를 보존하도록 구현했다.
- first-class function과 closure의 공개 behavior를 test로 검증했다.

### P5-2. iterable과 iterator

- iterable과 iterator가 서로 다른 객체이며 같은 iterable에서 독립적인 iterator를 만들 수 있음을 확인했다.
- `iter`, `next`, `StopIteration`을 통해 iterator가 순회 위치를 소유하고 이동하는 protocol을 관찰했다.
- `for`가 `StopIteration`을 정상적인 반복 종료로 처리하고 전달받은 iterator를 소비하는 것을 확인했다.
- 한 번 소비된 iterator를 재사용하면 두 번째 결과가 비는 버그를 재현했다.
- `NoteTitles`가 입력 list의 복사본을 소유하고 호출마다 새 iterator를 제공하도록 구현했다.
- `NoteTitleIterator`에 `__iter__`, `__next__`, index 상태, 종료 조건을 직접 구현했다.
- iterator 독립성, 지속되는 소진 상태, collection 소유권을 공개 behavior test로 검증했다.

### P5-3. generator

- generator function 호출과 첫 `next()` 사이의 lazy execution 경계를 확인했다.
- 여러 `yield` 사이에서 실행 위치와 local 상태가 보존되는 것을 확인했다.
- 함수 종료 시 `StopIteration`이 전달되고 generator가 소진 상태를 유지함을 확인했다.
- generator pipeline이 아래쪽 요청에 필요한 값만 source에서 가져오는 pull 방식을 확인했다.
- eager list와 lazy generator의 얕은 메모리 크기를 비교했다.
- `yield from`으로 여러 하위 generator의 값을 순서대로 위임했다.
- `Note` 제목을 대소문자 구분 없이 lazy하게 검색하는 streaming 함수를 구현했다.
- lazy 중단, 전체 검색, 입력 보존, 위임 순서를 공개 behavior test로 검증했다.

### P5-4. decorator

- 함수를 감싸 호출 전후 동작을 추가하면서 argument와 반환값을 보존했다.
- decorator의 import 시점 적용과 wrapper의 함수 호출 시점 실행을 구분했다.
- `functools.wraps`로 원본 함수의 이름과 문서 metadata를 보존했다.
- `time.perf_counter`를 이용해 함수 실행 시간을 측정했다.
- 인자를 받는 decorator factory가 설정값을 closure에 보존하는 과정을 확인했다.
- framework 형태의 decorator가 원본 함수를 path registry에 등록하는 방식을 구현했다.
- wrapping, metadata, timing, closure, route 등록을 공개 behavior test로 검증했다.

### P6-1. type hint의 역할

- function annotation이 runtime type을 강제하지 않는다는 점을 직접 확인했다.
- union과 optional type을 `isinstance`, `is None`으로 narrowing했다.
- optional annotation과 parameter 기본값이 서로 다른 역할임을 구분했다.
- `list[str]`으로 collection element type을 표현하고 원본 소유권을 보존했다.
- `Any`가 정적 검사를 우회하지만 runtime 안전성을 제공하지 않음을 확인했다.
- 구체적인 입력·반환 type을 기존 `Note` domain 객체 생성 경계에 적용했다.
- runtime 비강제, narrowing, collection, `Any`, domain 생성을 공개 behavior test로 검증했다.

### P6-2. generic과 protocol

- `TypeVar`로 입력 collection과 반환값 사이의 type 관계를 표현했다.
- `Generic[T]` class와 in-memory repository가 저장·반환 type 관계를 유지하도록 구현했다.
- `Protocol[T]`로 구체 구현을 상속하지 않는 구조적 repository 계약을 선언했다.
- `Callable[[T], str]`로 값과 formatter 함수 사이의 호출 계약을 표현했다.
- `@runtime_checkable`이 method signature 전체를 검증하지 않는 한계를 확인했다.
- generic repository와 protocol, callable을 기존 `Note` domain 흐름에 연결했다.
- generic 상태, 구조적 계약, callable, runtime 검사 한계를 공개 behavior test로 검증했다.

### P6-3. test 설계

- arrange, act, assert로 하나의 behavior를 읽기 쉽게 분리했다.
- 단일 함수 unit test와 실제 component를 연결한 integration test의 boundary를 구분했다.
- fake, stub, mock이 각각 상태, 고정 응답, 호출 interaction을 제공하는 차이를 확인했다.
- pytest parameterization으로 같은 behavior의 여러 입력 사례를 중복 없이 표현했다.
- pytest fixture로 준비 객체를 test마다 새로 생성해 상태를 격리했다.
- pytest를 test extra로 선언하고 기본 setup과 검증 명령에 연결했다.

### P6-4. formatter, lint, type checker

- Ruff formatter의 검사와 수정 모드를 구분하고 저장소 전체에 formatting 기준선을 적용했다.
- Ruff linter의 핵심 규칙을 선택하고 의도적인 위반은 파일 단위로만 허용했다.
- 안전한 자동 수정으로 실제 미사용 import만 제거하고 test로 동작 보존을 확인했다.
- runtime과 mypy의 type 검사 경계를 비교하고 엄격한 검사 범위를 project 설정에 고정했다.
- formatter, lint, type checker, test를 fail-fast script 하나로 재현하도록 구성했다.

### P7-1. path와 file I/O

- `Path` 객체의 조합과 상대 경로가 process의 현재 작업 directory를 기준으로 해석되는 방식을 확인했다.
- text mode와 binary mode의 encoding 책임 및 문자 수와 byte 수의 차이를 비교했다.
- buffered writer의 `write`, `flush`, `close`에 따른 data 가시성과 resource 수명을 관찰했다.
- 같은 filesystem의 임시 파일을 `replace()`해 대상 경로를 원자적으로 교체했다.
- domain 객체의 serialization과 파일 저장 I/O를 별도 함수로 분리했다.

### P7-2. JSON persistence

- Python과 JSON의 type 변환 및 문자열·파일 serialization 경계를 확인했다.
- parsing 성공과 application schema 검증을 분리하고 잘못된 data를 명시적인 오류로 변환했다.
- 과거 schema의 기본 version 해석과 새 schema 객체로의 비파괴 migration을 구현했다.
- partial write를 재현하고 serialization 선행 및 임시 파일 교체로 기존 JSON을 보호했다.

### P7-3. SQLite와 transaction

- `sqlite3`의 Connection, Cursor 객체 관계와 쿼리 실행·소진 경계를 확인했다.
- `?` parameter binding을 사용해 SQL injection 공격을 방어하고 특수문자 데이터를 안전하게 저장했다.
- 수동 commit/rollback과 `with connection:` 트랜잭션 context manager의 자동 롤백·커밋 경계를 확인했다.
- 파일 기반 다중 connection 환경에서 커밋 전/후의 트랜잭션 격리성(isolation)과 데이터 가시성을 확인했다.
- SQLite 기반의 테이블 초기화, 노트 삽입, ID 단건 조회, 키워드 검색 함수를 구현하고 공개 behavior test로 검증했다.

### P7-4. repository adapter

- 하나의 `NoteRepository` contract를 통해 in-memory, JSON, SQLite 구현을 교체했다.
- domain 객체와 persistence 표현 사이의 mapper가 값은 보존하고 객체 소유권은 분리하도록 구현했다.
- 기존 SQLite schema에 `tags_json`을 한 번만 추가하고 legacy row를 보존하는 migration을 구현했다.
- JSON atomic 저장과 SQLite transaction을 각 adapter가 소유하고, 주입받은 connection의 수명은 호출자가 관리하도록 분리했다.
- mapper, migration, adapter 교체와 파일 재접속 persistence를 공개 behavior test로 검증했다.

### P8-1. blocking I/O와 thread

- 동기 blocking 호출의 대기 위치와 순차 실행 시간을 `MainThread`와 `perf_counter()`로 관찰했다.
- `Thread.start()`와 `join()`의 실행·대기 경계를 구분하고 blocking 작업을 겹쳐 실행했다.
- worker 반환값과 shared mutable 결과 객체를 통한 명시적 결과 전달의 차이를 확인했다.
- 공유 상태의 race condition을 재현하고 GIL이 application의 복합 변경을 보호하지 않음을 구분했다.
- 하나의 `Lock`으로 critical section을 보호해 lost update를 방지하고 공개 behavior test로 검증했다.

### P8-2. process와 CPU-bound work

- CPU-bound 함수의 PID와 thread를 관찰하고 순차·thread·process pool의 실행 위치를 비교했다.
- `spawn` process가 별도 interpreter와 상태를 소유하며 argument와 결과를 pickle 기반으로 전달함을 확인했다.
- pickle payload의 값 보존, 객체 분리, 구조 검증과 payload 크기에 따른 serialization 비용을 관찰했다.
- CPython thread의 concurrency와 process의 병렬 실행 가능성을 구분하고 overhead를 포함해 실행 방식을 선택해야 함을 확인했다.
- checksum, serialization, thread/process 결과와 process 상태 분리를 공개 behavior test로 검증했다.

### P8-3. coroutine과 event loop

- coroutine 객체의 지연 실행과 `asyncio.run()`, `await`, Task의 실행·상태 경계를 확인했다.
- 순차 await와 먼저 생성한 여러 Task의 대기 시간을 비교해 event loop의 동시성을 관찰했다.
- `time.sleep()`이 event loop thread를 막는 현상을 재현하고 `asyncio.to_thread()`로 blocking 호출을 worker thread에 격리했다.
- 단일 event loop의 동시성과 thread·process의 병렬 실행을 구분하고 공개 behavior test로 검증했다.

### P8-4. cancellation, timeout, backpressure

- `TaskGroup`이 하위 Task의 정상 완료와 sibling 실패 시 취소 lifecycle을 하나의 scope에서 소유하도록 구성했다.
- 명시적 cancellation, cleanup 재전파, timeout의 `TimeoutError` 변환 경계를 확인했다.
- bounded Queue의 용량 제한과 미완료 항목 카운터를 구분하고 생산자에게 backpressure가 적용되는 것을 관찰했다.
- 종료 sentinel과 `task_done()`·`join()`을 사용해 여러 note source를 순서대로 처리하는 생산자·소비자 pipeline을 구현했다.

### P9-1. HTTP boundary

- 표준 라이브러리 request에서 method, path, query, headers, body를 분리하고 JSON `str`을 UTF-8 body bytes로 변환했다.
- 로컬 HTTP server와 실제 요청을 주고받으며 status, headers, response stream과 connection resource 수명을 확인했다.
- response body bytes를 JSON 객체로 복원하고 `HTTPError`의 protocol 실패와 `URLError`의 network 실패를 구분했다.
- 순수 변환, loopback 성공·404 응답, 하위 network 원인 보존을 공개 behavior test로 검증했다.

### P9-2. Pydantic validation

- Pydantic을 첫 runtime dependency로 도입하고 BaseModel과 Field 제약 조건을 확인했다.
- `model_validate()`의 타입 강제와 `strict=True`의 엄격한 타입 검사를 비교했다.
- `model_dump()`와 `model_dump_json()`의 직렬화 및 역직렬화 왕복을 확인했다.
- transport schema와 domain 객체 사이의 변환 및 상태 소유권 분리를 공개 behavior test로 검증했다.

### P9-3. FastAPI application

- FastAPI와 Starlette의 관계 및 TestClient를 통한 in-memory ASGI 호출을 확인했다.
- `async def` 엔드포인트의 이벤트 루프 실행과 일반 `def`의 worker thread 풀 위임을 구분했다.
- Pydantic request body 파싱, 201 Created 응답, 422 Unprocessable Entity 자동 검증을 확인했다.
- 반환 타입 힌트 불일치 시의 `ResponseValidationError`와 FastAPI 응답 검증 메커니즘을 확인했다.
- `Depends` 의존성 주입을 통해 `NoteService`를 주입받아 노트를 생성하고 조회하도록 연결했다.
- `@asynccontextmanager` 기반 `lifespan`으로 애플리케이션의 startup과 shutdown 수명을 관리했다.
- lifespan 준비 상태, sync/async 스레드 격리, payload 검증, 의존성 주입 조회의 공개 behavior를 test로 검증했다.

### P9-4. API test와 운영 경계

- TestClient의 in-process 호출과 Uvicorn loopback TCP 호출의 경계를 비교했다.
- domain 예외를 404 JSON으로 변환하고, 로그·환경 설정·client timeout의 운영 경계를 관찰했다.
- 순차 요청에서 idempotency key별 결과를 재사용하고, 정렬된 목록을 offset/limit으로 조회했다.
- 공개 API 동작을 test로 검증했다.

### P10-1. configuration과 secret

- 환경 변수 문자열을 포트 정수와 실행 모드로 변환하고 허용 범위를 검증했다.
- 검증된 값을 immutable `AppSettings`에 모으고, 토큰은 환경 변수에서 읽되 기본 객체 표현에서 숨겼다.
- production에서 토큰이 없으면 설정 객체를 만들기 전에 실패하도록 했다.
- 기본값, override, 잘못된 설정, 모드별 토큰 요구와 비노출을 공개 behavior test로 검증했다.

### P10-2. dependency boundary

- FastAPI 객체를 모르는 core 함수와 HTTP 입력을 변환하는 adapter의 책임을 분리했다.
- application 함수가 callable을 인자로 받아 실제 구현과 fake 구현을 교체할 수 있게 했다.
- FastAPI provider와 `Depends`로 endpoint 조립을 분리하고 test override 후 상태를 복원했다.
- core, application, HTTP adapter와 dependency override를 공개 behavior test로 검증했다.

### P10-3. observability

- Logger, StreamHandler, Formatter를 분리해 전역 상태 없이 메모리 버퍼로 로그를 캡처했다.
- `JsonFormatter`로 레벨·메시지·로거명 및 extra 메타데이터(event, note_id)를 구조화된 JSON으로 직렬화했다.
- `contextvars.ContextVar`를 사용해 비동기·스레드 안전한 request_id 바인딩 및 자동 주입과 리셋을 확인했다.
- `MetricsCollector`로 작업 수, 실패 수, 경과 시간을 안전하게 집계하고 예외를 재전파했다.
- 내부 스택트레이스를 JSON 로그의 exception에 보존하면서 외부 클라이언트에는 정제된 에러 응답만 전달하는 경계를 공개 behavior test로 검증했다.

### P10-4. process와 deployment

- uvicorn Config·Server 객체 생성, ASGI callable load, socket 바인딩 및 graceful shutdown 실행 경계를 확인했다.
- process 생존(liveness 200)과 traffic 수신 준비(readiness 503 → 200 → 503) 헬스체크 상태를 분리했다.
- 컨테이너 환경의 0.0.0.0 바인딩과 워커 프로세스 CLI 실행 명령 생성을 공개 behavior test로 검증했다.

## P5-2 세부 완료 기록

- P5-2 iterable과 iterator
- 상태: 완료
- 완료: list iterable과 `iter()`가 생성한 `list_iterator`가 서로 다른 객체임을 확인했다.
- 완료: 같은 iterable에서 만든 두 iterator가 독립적인 객체이고 iterator의 `iter()`는 자기 자신을 반환함을 확인했다.
- 완료: `next()` 호출마다 iterator가 다음 객체를 반환하고 자신의 순회 위치를 이동하는 것을 확인했다.
- 완료: 두 iterator가 독립적인 위치를 소유하며 값을 소비해도 원본 list는 변경되지 않음을 확인했다.
- 완료: 소진된 iterator에 `next()`를 호출해 값 대신 `StopIteration`이 발생하는 호출 시점을 traceback으로 확인했다.
- 완료: `StopIteration`을 처리한 뒤에도 iterator가 소진 상태를 유지하고 `next(iterator, default)`가 기본 객체를 반환함을 확인했다.
- 완료: 한 iterator의 소진이 같은 iterable에서 만든 다른 iterator의 순회 상태에는 영향을 주지 않음을 확인했다.
- 완료: `for`가 iterator에서 값을 차례로 소비하고 `StopIteration`을 정상적인 loop 종료로 처리함을 확인했다.
- 완료: `for` 종료 뒤 전달한 iterator가 소진 상태임을 `next(iterator, default)`로 확인했다.
- 완료: 같은 iterator를 두 번 소비하면 첫 결과만 값을 가지고 두 번째 결과는 비는 재사용 버그를 확인했다.
- 완료: list iterable은 소비할 때마다 새 iterator와 새 결과 list를 만들 수 있음을 identity로 확인했다.
- 완료: `NoteTitles.__iter__()`가 내부 list에서 새 iterator를 반환하는 사용자 정의 iterable을 구현했다.
- 완료: `iter(note_titles_collection)` 호출마다 별도 `list_iterator`가 생성되어 반복 가능한 것을 확인했다.
- 완료: `NoteTitles`가 입력 list를 복사해 내부 collection의 소유권을 분리했다.
- 완료: `NoteTitleIterator`가 자신의 index를 소유하고 `__iter__`, `__next__`, `StopIteration`으로 iterator protocol을 구현했다.
- 완료: 서로 다른 iterator가 독립적인 index 상태를 소유하는 behavior를 test로 검증했다.
- 완료: `StopIteration` 이후에도 iterator가 소진 상태를 유지하는 behavior를 test로 검증했다.
- 완료: `NoteTitles`가 외부 입력 list의 이후 변경에서 독립적인 collection을 소유함을 test로 검증했다.

## P5-3 세부 완료 기록

- P5-3 generator
- 상태: 완료
- 완료: generator function 호출은 본문을 실행하지 않고 generator 객체를 반환함을 확인했다.
- 완료: 첫 `next()`가 본문을 시작해 첫 `yield`까지 실행하는 lazy execution을 출력 순서로 확인했다.
- 완료: 다음 `next()`가 직전 `yield` 이후부터 재개되고 local `title` 상태를 보존함을 확인했다.
- 완료: 마지막 `yield` 이후 함수가 끝날 때 `StopIteration`이 전달되고 소진 상태가 유지됨을 확인했다.
- 완료: generator pipeline에서 아래쪽의 값 하나 요청이 source와 변환 단계를 필요한 지점까지만 실행함을 확인했다.
- 완료: eager list와 lazy generator가 직접 소유하는 얕은 메모리 크기를 `getsizeof()`로 비교했다.
- 완료: `yield from`이 첫 하위 generator를 소진한 뒤 두 번째 generator로 이동하며 값을 위임함을 확인했다.
- 완료: `Note` 객체의 제목을 lazy하게 검색하는 streaming 함수를 Knowledge Lab에 연결했다.
- 완료: lazy 중단, 전체 검색, 입력 보존, 위임 순서를 공개 behavior test로 검증했다.

## P5-4 세부 완료 기록

- P5-4 decorator
- 상태: 완료
- 완료: 함수를 인자로 받아 closure로 원본을 보존하는 새 wrapper 함수를 반환했다.
- 완료: wrapper가 원본 함수 호출 전후 동작과 반환값을 보존함을 확인했다.
- 완료: `@decorator`가 함수 정의 직후 이름을 wrapper 함수로 다시 binding함을 확인했다.
- 완료: decorator 본문은 module import 시점에, wrapper 본문은 함수 호출 시점에 실행됨을 확인했다.
- 완료: wrapping 후 외부 이름이 wrapper의 `__name__`과 `__doc__` metadata를 노출하는 문제를 확인했다.
- 완료: `functools.wraps`가 wrapper에 원본 함수의 `__name__`과 `__doc__` metadata를 복사함을 확인했다.
- 완료: `*args`와 `**kwargs`로 서로 다른 signature의 위치·키워드 argument를 원본 함수에 전달했다.
- 완료: `time.perf_counter`로 함수 호출 전후 경과 시간을 측정하고 원본 반환값을 보존했다.
- 완료: 인자를 받는 decorator factory가 설정값을 closure에 보존하는 세 호출 단계를 확인했다.
- 완료: framework decorator가 import 시점에 원본 함수를 path registry에 등록하고 그대로 반환함을 확인했다.
- 완료: wrapping, metadata, timing, closure, route 등록을 공개 behavior test로 검증했다.

## P6-1 세부 완료 기록

- P6-1 type hint의 역할
- 상태: 완료
- 완료: function annotation이 `__annotations__`에 저장되지만 runtime 호출과 반환 type을 강제하지 않음을 확인했다.
- 완료: `int | str` union과 `isinstance` 분기로 입력 type을 좁혀 각 type에 맞는 연산을 적용했다.
- 완료: `str | None`과 `is None` 분기로 값 부재를 명시하고 나머지 branch를 `str`로 좁혔다.
- 완료: optional annotation만으로는 argument를 생략할 수 없으며 함수 본문 진입 전 binding `TypeError`가 발생함을 확인했다.
- 완료: `None` 기본값이 `__defaults__`에 저장되고 argument 생략 시 parameter에 binding됨을 확인했다.
- 완료: `list[str]` generic annotation으로 collection과 element type을 표현하고 새 list를 반환했다.
- 완료: `Any`가 indexing을 정적으로 허용해도 실제 객체가 protocol을 지원하지 않으면 runtime `TypeError`가 발생함을 확인했다.
- 완료: 구체적인 입력과 반환 type을 사용해 정규화된 `Note`와 `Tag` domain 객체를 생성했다.
- 완료: runtime 비강제, narrowing, collection 소유권, `Any`, domain 생성을 공개 behavior test로 검증했다.

## P6-2 세부 완료 기록

- P6-2 generic과 protocol
- 상태: 완료
- 완료: `TypeVar`로 list element와 반환값이 같은 type이라는 호출별 관계를 표현했다.
- 완료: `Generic[T]` class가 저장한 상태와 반환 type의 관계를 유지하면서 runtime에는 같은 class임을 확인했다.
- 완료: generic in-memory repository가 독립적인 dict에 한 종류의 객체를 저장하고 같은 type으로 반환하도록 구현했다.
- 완료: `Protocol[T]` 계약과 generic loader를 구현해 명목 상속 없이 repository를 구조적으로 사용했다.
- 완료: `Callable[[T], str]`로 값과 formatter parameter의 type 관계 및 반환 계약을 표현했다.
- 완료: `@runtime_checkable` 검사가 method 존재만 확인하고 signature 전체를 보장하지 않음을 확인했다.
- 완료: `Repository[Note]`와 `Callable[[Note], str]`를 조합해 note 조회와 formatting 경계를 구현했다.
- 완료: generic 상태, 구조적 계약, callable, runtime 검사 한계를 공개 behavior test로 검증했다.

## P6-3 세부 완료 기록

- P6-3 test 설계
- 상태: 완료
- 완료: `unittest.TestCase`에서 arrange, act, assert를 분리해 title 정규화 behavior 하나를 검증했다.
- 완료: 단일 함수 unit test와 service·in-memory adapter를 연결한 integration test의 boundary를 구분했다.
- 완료: test 전용 fake가 실제 list 상태를 소유하도록 구현해 service를 production adapter에서 분리했다.
- 완료: 미리 준비한 note list를 반환하는 stub으로 service의 조회 경로를 고립해 검증했다.
- 완료: `unittest.mock.Mock`으로 repository의 `add` 호출 인자와 횟수를 검증했다.
- 완료: pytest parameterization으로 title 정규화의 여러 입력 사례를 하나의 behavior test에 표현했다.
- 완료: pytest fixture가 test마다 새 fake와 service를 생성해 상태를 격리함을 확인했다.
- 완료: pytest를 test extra로 선언하고 setup 및 기본 검증 명령에 연결했다.

## P6-4 세부 완료 기록

- P6-4 formatter, lint, type checker
- 상태: 완료
- 완료: Ruff formatter의 check/write 모드로 공백과 표현을 표준화하고 함수 scope는 변경하지 않음을 확인했다.
- 완료: Ruff linter가 formatting과 별개로 사용되지 않는 local 이름을 `F841`로 진단하는 방식을 확인했다.
- 완료: 프로젝트의 lint 기준을 실행 오류와 미사용 이름 중심의 `E4`, `E7`, `E9`, `F` 규칙으로 선택했다.
- 완료: 의도적인 `F401`, `E402`는 파일별로만 허용하고 실제 불필요한 import와 구분했다.
- 완료: Ruff의 안전한 자동 수정으로 실제 미사용 import만 제거하고 lint, test, 실행 결과가 보존됨을 확인했다.
- 완료: runtime은 f-string에서 정수 입력을 처리하지만 mypy는 annotation 계약 위반을 `[arg-type]`으로 진단함을 확인했다.
- 완료: 의도적으로 만든 type 오류를 제거하고 현재 lesson의 mypy 검사 기준선을 복구했다.
- 완료: mypy의 Python 버전, 검사 대상, `strict` 기준을 `pyproject.toml`에 고정하고 인자 없는 실행으로 확인했다.
- 완료: 저장소의 Python 파일 40개를 Ruff formatting 기준선에 맞추고 lint, type check, test 통과를 확인했다.
- 완료: formatter, lint, type checker, test를 fail-fast 검증 script 하나로 재현했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P7-1 세부 완료 기록

- P7-1 path와 file I/O
- 상태: 완료
- 완료: 문자열 조각을 `/` 연산자로 조합해 `Path` 객체를 만들고 이름, 확장자, 부모 경로를 조회했다.
- 완료: 상대 경로 객체 생성은 파일을 만들지 않으며 `.exists()` 호출이 현재 파일시스템 상태를 조회함을 확인했다.
- 완료: 같은 상대 경로가 module 위치가 아니라 process의 현재 작업 directory를 기준으로 절대 경로로 해석됨을 확인했다.
- 완료: text mode에서 `str`을 UTF-8로 저장하고 다시 `str`로 읽어 원본 값이 보존됨을 확인했다.
- 완료: `TemporaryDirectory`의 context 안에서 파일이 존재하고 종료 뒤 실제 directory가 정리되는 resource 수명을 확인했다.
- 완료: binary mode에서 caller가 UTF-8 encode/decode 경계를 직접 소유하고 `bytes`를 그대로 저장·복원함을 확인했다.
- 완료: 같은 내용이 Python에서는 9문자이고 UTF-8에서는 13 byte인 차이를 비교했다.
- 완료: buffered writer에 쓴 내용이 `flush()` 전에는 다른 reader에 보이지 않고 호출 후 보이는 것을 확인했다.
- 완료: file context 안팎에서 같은 writer 객체의 `closed` 상태가 `False`에서 `True`로 바뀌는 resource 수명을 확인했다.
- 완료: 같은 directory에서 완성한 임시 파일을 `Path.replace()`로 대상 이름에 원자적으로 교체했다.
- 완료: 대상 경로 이름은 유지되지만 그 이름이 가리키는 inode는 기존 파일에서 임시 파일 identity로 바뀜을 확인했다.
- 완료: immutable domain 객체를 text로 직렬화하는 책임과 이미 직렬화된 `str`을 저장하는 I/O 책임을 분리했다.
- 완료: text, binary, serialization의 공개 behavior를 임시 경로 기반 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P7-2 세부 완료 기록

- P7-2 JSON persistence
- 상태: 완료
- 완료: `json.dumps()`가 Python 객체를 JSON `str`로 만들고 `json.loads()`가 새 Python 객체로 복원하는 경계를 확인했다.
- 완료: Python의 `False`, `None`이 JSON의 `false`, `null`로 표현되고 tuple이 JSON array를 거쳐 list로 복원됨을 확인했다.
- 완료: `json.dump()`와 `json.load()`가 열린 text file 객체를 사용하고 file resource 수명은 caller의 context가 소유함을 확인했다.
- 완료: 문자열과 파일이라는 서로 다른 입력 경계에서 복원한 Python 객체가 동등함을 확인했다.
- 완료: 가공하지 않은 잘못된 JSON text를 읽을 때 `JSONDecodeError`의 message와 실패 위치가 전달됨을 확인했다.
- 완료: `json.load()`가 실패해도 `with`를 빠져나오면서 reader가 닫힌 뒤 `except`가 오류를 처리함을 확인했다.
- 완료: 문법상 유효한 JSON도 application이 기대하는 객체 구조가 아닐 수 있고, 잘못된 key 접근은 parsing 이후 `TypeError`로 드러남을 확인했다.
- 완료: `isinstance()`로 JSON 값의 top-level 구조를 검사하고 잘못된 구조를 명시적인 `ValueError`로 변환했다.
- 완료: `require_note_title()`에서 필수 field를 `str`로 검증하고 `json.loads()`의 `Any`를 그대로 신뢰하지 않는 경계를 구성했다.
- 완료: schema version이 없는 과거 JSON을 version 1로 해석하면서 입력 dict를 변경하지 않는 호환 읽기를 확인했다.
- 완료: 구버전 dict를 복사한 뒤 version과 새 field를 추가해 원본과 migration 결과의 소유권을 분리했다.
- 완료: 기존 JSON 파일을 직접 열어 직렬화하다 실패하면 앞부분만 기록되어 기존 data까지 손상되는 partial write를 재현했다.
- 완료: target file을 열기 전에 `json.dumps()`를 완료해 serialization 실패 시 기존 data가 보존됨을 확인했다.
- 완료: 같은 directory의 임시 파일에 완성된 JSON을 기록한 뒤 `replace()`해 target을 원자적으로 교체했다.
- 완료: atomic 저장의 serialization 실패 시 임시 파일과 target이 변경되지 않고 기존 JSON이 보존됨을 확인했다.
- 완료: Python에서 `bool`이 `int`의 subclass인 특성을 고려해 schema version의 정확한 JSON type을 검증했다.
- 완료: JSON 구조 검증, migration, atomic 저장의 공개 behavior를 임시 경로 기반 test로 검증했다.

## P7-3 세부 완료 기록

- P7-3 SQLite와 transaction
- 상태: 완료
- 완료: `sqlite3.connect()`로 `Connection`을 생성하고 `cursor()`를 통해 쿼리 실행 및 순회 커서를 획득했다.
- 완료: `fetchone()`이 행을 `tuple`로 반환하며 위치를 이동하고, `fetchall()`로 소진 후 다시 호출 시 `None`을 반환함을 확인했다.
- 완료: `?` parameter binding을 사용해 작은따옴표가 포함된 데이터를 안전하게 저장하고 조회했다.
- 완료: f-string 기반 동적 쿼리가 악의적 입력(`' OR '1'='1`)에 의해 전체 데이터를 유출하는 취약점을 재현하고, parameter binding이 이를 안전하게 방어함을 확인했다.
- 완료: `connection.commit()`으로 트랜잭션을 확정하고, `connection.rollback()`으로 미커밋 변경사항을 취소해 직전 커밋 상태를 복원함을 확인했다.
- 완료: `with connection:` 트랜잭션 context manager가 예외 시 자동 롤백, 정상 종료 시 자동 커밋을 수행하며 커넥션 자체는 닫지 않음을 확인했다.
- 완료: 파일 기반 DB에서 `writer_conn`의 미커밋 변경사항이 `reader_conn`에 노출되지 않고, 커밋 후 비로소 가시화되는 트랜잭션 격리성을 확인했다.
- 완료: `init_notes_table`, `insert_note`(`lastrowid`), `find_note_by_id`, `search_notes_by_title` 모듈화 함수를 구현했다.
- 완료: 테이블 초기화, 자동 증가 ID 생성, 단건 조회, SQL injection 방어 검색, 트랜잭션 롤백·커밋, 다중 연결 격리의 공개 behavior를 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P7-4 세부 완료 기록

- P7-4 repository adapter
- 상태: 완료
- 완료: `save_and_list_notes()`가 구체 저장소를 생성하지 않고 기존 `NoteRepository` contract를 통해 저장과 조회를 호출하도록 구성했다.
- 완료: `InMemoryNoteRepository`가 상태를 소유하고 입력받은 동일한 `Note` 객체를 보관함을 identity로 확인했다.
- 완료: `note_to_data()`가 domain `Note`와 `Tag`를 새 dict와 `list[str]` persistence 표현으로 변환하고 collection 소유권을 분리했다.
- 완료: `note_from_data()`가 persistence 구조를 검증하고 값이 같은 새 `Note`, tags list, `Tag` 객체로 복원했다.
- 완료: `JsonNoteRepository.all()`이 path를 소유하고 missing file은 빈 목록으로, JSON array는 새 domain 객체 목록으로 읽도록 구현했다.
- 완료: `JsonNoteRepository.add()`가 read-modify-write와 atomic JSON 저장을 수행해 기존 `NoteRepository` contract와 구조적으로 호환됨을 확인했다.
- 완료: `PRAGMA table_info(notes)`로 transaction을 변경하지 않고 기존 SQLite schema의 column을 읽어 `tags_json` 부재를 확인했다.
- 완료: 기존 row에 기본 JSON 값을 적용하면서 `tags_json` column을 한 번만 추가하는 idempotent migration을 구현했다.
- 완료: `SqliteNoteRepository`가 주입받은 connection을 닫지 않고 `add()`의 parameter binding과 transaction을 소유하도록 구현했다.
- 완료: `SqliteNoteRepository.all()`이 SQLite row와 `tags_json`을 값이 같은 새 domain `Note` 목록으로 복원하도록 구현했다.
- 완료: 같은 application 함수에서 in-memory, JSON, SQLite adapter를 교체하고 각 저장소의 객체 identity와 resource 소유권 차이를 확인했다.
- 완료: mapper, migration, adapter 교체와 실제 파일 재접속 persistence를 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P8-1 세부 완료 기록

- P8-1 blocking I/O와 thread
- 상태: 완료
- 완료: `load_note_source()`의 blocking 대기 동안 `MainThread`의 현재 call stack이 호출 지점에 머물고, 함수 반환 후에야 호출자가 다시 실행됨을 순서와 경과 시간으로 확인했다.
- 완료: 같은 thread에서 두 blocking 작업을 순차 호출하면 첫 호출이 반환된 뒤 다음 호출이 시작되어 대기 시간이 합산됨을 약 `0.4초`의 기준선으로 확인했다.
- 완료: `Thread.start()`로 별도 call stack에서 두 blocking 작업을 겹쳐 실행하고, `join()`이 완료를 기다려 전체 시간이 약 `0.2초`가 되는 것을 확인했다.
- 완료: `Thread.join()`은 worker 완료만 기다리고 target 함수의 `str` 반환값 대신 `None`을 반환함을 확인했다.
- 완료: 여러 worker에 같은 mutable 결과 목록을 전달하고 `join()` 이후 MainThread에서 target 결과를 명시적으로 관찰했다.
- 완료: 공유 상태의 `읽기 → 계산 → 쓰기` 사이에 thread 전환 지점을 두고 여러 worker가 같은 이전 값을 덮어써 갱신을 잃는 race condition을 재현했다.
- 완료: GIL은 한 시점의 Python bytecode 실행을 제한하지만 여러 동작으로 구성된 application 불변식을 보호하는 lock이 아님을 구분했다.
- 완료: 모든 worker가 하나의 `Lock` 객체를 공유하고 복합 변경을 critical section으로 묶어 lost update를 방지했다.
- 완료: blocking 호출, 순차·thread 실행, 결과 공유, Lock 보호의 공개 behavior를 scheduling 시간에 과도하게 의존하지 않는 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P8-2 세부 완료 기록

- P8-2 process와 CPU-bound work
- 상태: 완료
- 완료: `calculate_note_checksum()`가 외부 대기 없이 현재 process의 `MainThread`에서 Python 연산을 수행하는 위치와 단일 작업 시간을 확인했다.
- 완료: `spawn` context의 별도 process에서 같은 CPU-bound 함수를 실행해 부모와 다른 PID, 독립된 `MainThread`, 정상 종료 `exitcode`를 확인했다.
- 완료: `spawn` process의 list argument가 같은 객체 참조로 공유되지 않고 전달 시점의 값으로 복원되어 부모와 child가 독립된 상태를 소유함을 확인했다.
- 완료: `pickle`이 Python 객체를 immutable binary payload로 직렬화하고 값이 같은 새 객체로 복원하는 경계를 확인했다.
- 완료: pickle 입력 형식 오류와 역직렬화 후 application 구조 검증 오류를 서로 다른 exception boundary로 구분했다.
- 완료: process 전달 전후에 필요한 pickle 직렬화·복원 비용이 payload 크기에 따라 증가하는 것을 bytes 크기와 경과 시간으로 측정했다.
- 완료: 같은 CPU-bound 작업 두 개를 순차 실행과 thread pool로 실행해 동일 PID의 `MainThread`와 여러 worker thread를 구분하고 결과의 동등성을 확인했다.
- 완료: 한 번의 wall-clock 측정 차이는 interpreter warm-up과 system load가 섞이므로 GIL 아래의 CPU 병렬성 증거로 일반화할 수 없음을 구분했다.
- 완료: `ProcessPoolExecutor`와 `spawn` context로 CPU-bound 작업을 서로 다른 PID에서 실행하고 pickle 기반 결과를 입력 순서대로 복원했다.
- 완료: process 병렬 실행 가능성과 process 시작·interpreter import·serialization·통신·종료 overhead를 함께 비교했다.
- 완료: Java thread의 JVM 병렬 실행과 CPython thread의 GIL 기반 concurrency 차이를 구분했다.
- 완료: checksum 결정성, pickle 왕복과 검증, thread/process pool 결과, 부모·child 상태 분리를 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P8-3 세부 완료 기록

- P8-3 coroutine과 event loop
- 상태: 완료
- 완료: `async def` 함수 호출은 본문을 실행하지 않고 coroutine 객체를 만들며, `inspect.iscoroutine()`과 미실행 본문 출력 부재로 이를 확인했다.
- 완료: `asyncio.run()`이 동기 진입점에서 event loop를 생성·종료하고 coroutine 본문을 실행한 뒤 반환값을 동기 호출자에게 전달함을 확인했다.
- 완료: async 함수 내부의 `await`가 하위 coroutine을 실행하고 완료된 반환값을 현재 coroutine에 연결한 뒤 다음 줄로 진행하는 순서를 확인했다.
- 완료: `asyncio.create_task()`가 coroutine을 event loop에 스케줄하고 Task 객체가 pending·done 상태와 반환값을 소유하는 경계를 확인했다.
- 완료: `await asyncio.sleep()`에서 coroutine이 일시 중단되지만 다음 coroutine을 첫 완료 뒤에 생성하면 두 대기 시간이 합산됨을 약 `0.4초`의 순차 기준선으로 확인했다.
- 완료: 두 coroutine을 Task로 먼저 스케줄해 한 Task의 async 대기 동안 event loop가 다른 Task를 진행하고 전체 시간이 약 `0.2초`가 됨을 확인했다.
- 완료: async 함수 안의 `time.sleep()`이 단일 event loop thread를 점유해 이미 스케줄된 다른 Task의 진행까지 막고 시간이 약 `0.4초`로 합산되는 문제를 재현했다.
- 완료: 두 `asyncio.to_thread()` awaitable을 Task로 먼저 스케줄해 blocking 호출을 서로 다른 worker thread에 격리하고 전체 대기 시간이 약 `0.2초`로 회복됨을 확인했다.
- 완료: coroutine 생성, await 연결, Task 상태, 순차·동시 실행, blocking 호출의 thread 위임을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P8-4 세부 완료 기록

- P8-4 cancellation, timeout, backpressure
- 상태: 완료
- 완료: `TaskGroup`의 lexical scope가 여러 하위 Task의 생성을 소유하고 block 종료 시 모든 완료를 기다리는 structured concurrency의 정상 lifecycle을 확인했다.
- 완료: coroutine을 `await`하지 않아 실행되지 않는 `RuntimeWarning`을 재현하고, 실제 suspension point를 복구해 두 Task의 대기가 겹치는 것을 확인했다.
- 완료: `TaskGroup`의 한 자식이 실패하면 같은 group의 sibling Task가 취소되고, 원인 예외가 `ExceptionGroup`으로 scope 밖에 전달되는 실패 lifecycle을 확인했다.
- 완료: `Task.cancel()`의 반환값은 취소 요청 수락 여부이며 다음 suspension point에서 `CancelledError`가 전달된 뒤 Task가 `done`과 `cancelled` 상태가 됨을 확인했다.
- 완료: `asyncio.timeout()`이 deadline을 넘긴 await를 약 `0.1초`에 중단하고 context 밖에서 `TimeoutError`로 변환하며, 처리 후 현재 coroutine은 계속 실행됨을 확인했다.
- 완료: 하위 coroutine이 cancellation을 관찰하고 `finally`에서 정리한 뒤 `CancelledError`를 다시 전달해 바깥 timeout 경계가 유지되는 것을 확인했다.
- 완료: `Queue(maxsize=1)`이 가득 찼을 때 두 번째 `put()` Task가 중단되고, 소비자가 `get()`으로 공간을 만든 뒤 완료되는 backpressure를 확인했다.
- 완료: `get()`은 buffer 크기만 줄이고 `task_done()`이 별도의 미완료 항목 수를 줄이며, `join()`은 모든 항목의 처리 완료 통보까지 기다리는 것을 확인했다.
- 완료: `None` sentinel로 생산 종료를 전달하고 bounded Queue, TaskGroup, `task_done()`·`join()`을 연결한 생산자·소비자 pipeline을 구현했다.
- 완료: TaskGroup 실패, 명시적 취소, cleanup 재전파, Queue 완료 추적, bounded pipeline을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P9-1 세부 완료 기록

- P9-1 HTTP boundary
- 상태: 완료
- 완료: 표준 라이브러리 `Request` 객체를 network 전송 없이 생성하고 HTTP method, path, query, headers, body bytes를 서로 다른 transport 요소로 관찰했다.
- 완료: HTTP header 이름은 대소문자를 구분하지 않으며 `Request`의 내부 표현에서 정규화될 수 있음을 확인했다.
- 완료: Python dict를 JSON `str`로 직렬화하고 UTF-8 `bytes`로 encode해 request body로 전달하면서 문자 수와 byte 수의 차이를 확인했다.
- 완료: 로컬 HTTP server에 blocking request를 전송하고 response의 `201` status, content type, body bytes를 서로 다른 protocol 요소로 확인했다.
- 완료: response stream의 첫 `read()`가 body를 소비해 두 번째 읽기는 비고, context 종료 후 connection resource가 닫히는 수명을 확인했다.
- 완료: response body bytes를 UTF-8 JSON 문자열로 decode하고 새 Python dict로 deserialize해 transport 표현과 application 객체를 분리했다.
- 완료: 연결에 성공한 서버의 `404` response가 `HTTPError`로 전달되며 code, reason, headers, body stream과 닫아야 할 resource를 함께 소유함을 확인했다.
- 완료: HTTP response 전에 연결이 거부되면 `URLError`에 status나 body가 없고 `reason`에 `ConnectionRefusedError`가 보존됨을 확인했다.
- 완료: request 구성, JSON 왕복, loopback 성공·404 응답, network 원인 보존을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P9-2 세부 완료 기록

- P9-2 Pydantic validation
- 상태: 완료
- 완료: Pydantic `2.13.5`를 첫 runtime dependency로 선언하고 editable environment와 distribution metadata 검증을 갱신했다.
- 완료: `BaseModel.model_validate()`가 외부 문자열 값을 annotation에 맞는 `int`와 `bool`로 parsing해 새 transport schema 객체를 만들고 원본 dict는 보존함을 확인했다.
- 완료: 누락되거나 parsing할 수 없는 여러 field가 하나의 `ValidationError`에 모이고 `loc`, `type`, `msg`, `input`의 구조화된 detail로 표현됨을 확인했다.
- 완료: annotation 타입에는 맞는 빈 문자열과 정수 0도 `Field`의 길이·범위 constraint를 위반하면 구조화된 오류로 거부됨을 확인했다.
- 완료: 같은 문자열 입력을 기본 validation은 `int`와 `bool`로 coercion하지만 `strict=True`는 exact type 오류로 거부함을 확인했다.
- 완료: 검증된 model을 `model_dump()`의 새 dict와 `model_dump_json()`의 JSON str로 serialization하고, JSON에서 동등하지만 identity가 다른 새 model을 복원했다.
- 완료: HTTP transport의 `list[str]`를 별도 `list[Tag]`로 변환해 Pydantic schema와 기존 `Note` domain model의 타입과 상태 소유권을 분리했다.
- 완료: constraint 오류, 기본 parsing과 strict validation, JSON 왕복, transport-domain mapping을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P9-3 세부 완료 기록

- P9-3 FastAPI application
- 상태: 완료
- 완료: FastAPI와 Starlette 및 TestClient의 in-memory ASGI 호출 구조를 확인했다.
- 완료: `async def` 엔드포인트는 이벤트 루프 스레드에서 직접 실행되고, 일반 `def` 엔드포인트는 worker thread 풀로 위임됨을 확인했다.
- 완료: Pydantic model 기반의 request body 파싱, `201 Created` 응답, 제약 조건 위반 시의 `422 Unprocessable Entity` 자동 검증을 확인했다.
- 완료: 반환 타입 힌트와 실제 데이터의 불일치 시 발생하는 `ResponseValidationError`와 FastAPI의 응답 검증 메커니즘을 확인했다.
- 완료: `Depends`를 통해 `NoteService`를 엔드포인트에 주입하고, POST로 생성한 노트가 GET `/api/notes`에서 조회되는 애플리케이션 서비스 연동을 확인했다.
- 완료: `@asynccontextmanager` 기반의 `lifespan`으로 앱 시작(`startup`)과 종료(`shutdown`) 시점의 상태 관리와 `with TestClient(app)`의 수명 경계를 확인했다.
- 완료: lifespan 준비 상태, sync/async 스레드 격리, payload 검증, 의존성 주입 조회의 공개 behavior를 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P9-4 세부 완료 기록

- P9-4 API test와 운영 경계
- 상태: 완료
- 완료: `TestClient`의 합성 `http://testserver` URL과 같은 process PID를 관찰해 TCP socket 없이 ASGI application을 호출하는 in-process test 경계를 확인했다.
- 완료: JSON 응답을 `object`에서 시작해 필요한 dict와 `pid` 정수만 검사하며 type narrowing하는 boundary를 적용했다.
- 완료: 임시 Uvicorn server와 loopback TCP port를 통과해 `HTTPResponse`와 body bytes를 받는 실제 network test를 수행하고 response 및 server resource 정리를 확인했다.
- 완료: network test 여부는 별도 process 여부가 아니며 background thread의 server도 실제 TCP 경계를 통과할 수 있음을 같은 PID로 확인했다.
- 완료: `NoteNotFoundError`를 FastAPI exception handler에서 `404`와 구조화된 JSON error body로 변환해 domain 실패와 HTTP 표현을 분리했다.
- 완료: exception handler에서 사건명·경로·오류 타입을 일관된 `key=value` 로그로 남기고 client response와 운영 로그의 책임을 분리했다. log argument를 별도로 전달해 문자열 formatting을 기록 시점까지 미루는 방식도 확인했다.
- 완료: `get_runtime_mode()`가 호출 시점의 `KNOWLEDGE_LAB_MODE` 환경 변수를 읽고 누락 시 `development`를 반환함을 별도 process 실행으로 확인했다.
- 완료: 실제 HTTP 요청에서 client의 `timeout=0.2`가 느린 응답 대기를 `TimeoutError`로 중단하고, 호출자가 예외를 처리해 계속 실행함을 확인했다.
- 완료: client timeout 이후에도 server endpoint가 sleep 뒤 `Event.set()`까지 도달함을 확인해 client 대기 중단과 server 작업 취소가 별개임을 관찰했다.
- 완료: 같은 `POST /jobs`를 두 번 호출했을 때 count가 1에서 2로 증가해 재시도만으로 상태 변경이 중복됨을 확인했다.
- 완료: `Idempotency-Key`별 첫 생성 결과를 별도 dict에 보존해 순차 재시도 `A → A → B → A`가 `1 → 1 → 2 → 1`을 반환하고 실제 생성 count는 2번만 증가함을 확인했다. 메모리 캐시이므로 동시성·재시작 보장은 아직 다루지 않았다.
- 완료: 키를 정렬해 안정적인 순서로 `offset`과 `limit` 페이지를 나누고, 각 페이지와 관계없이 `total=3`을 반환함을 확인했다.
- 완료: `limit=0`과 음수 `offset`을 FastAPI의 `Query` 제약으로 `422` 응답으로 거부함을 확인했다.
- 완료: in-process 및 loopback API 호출, 예외 변환, 환경 설정, client timeout 이후 server 완료, 순차 idempotency, pagination을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P10-1 세부 완료 기록

- P10-1 configuration과 secret
- 상태: 완료
- 완료: `KNOWLEDGE_LAB_PORT`의 기본값과 shell에서 주입한 값을 `load_http_port()`에서 정수로 변환해 각각 `8000`, `9000`을 반환함을 확인했다.
- 완료: 정수로 변환된 값도 HTTP 포트 범위 `1..65535` 밖이면 `load_http_port()`에서 `ValueError`로 거부함을 확인했다.
- 완료: `load_settings()`에서 검증된 포트를 immutable `AppSettings` 객체로 묶고 기본값과 환경 변수 override의 dataclass 표현을 확인했다.
- 완료: 선택적 토큰을 환경 변수에서 `AppSettings`에 저장하고 `field(repr=False)`로 기본 객체 표현에 값이 노출되지 않음을 확인했다.
- 완료: 실행 모드를 development/test/production으로 제한하고 `unknown` 값을 `load_mode()`에서 `ValueError`로 거부함을 확인했다.
- 완료: production 모드에서 토큰이 `None` 또는 빈 문자열이면 `AppSettings` 생성 전에 `ValueError`로 거부하고, 토큰이 있으면 설정을 생성함을 확인했다.
- 완료: development와 test에서는 토큰 없이 실행할 수 있으며, 토큰이 있어도 기본 객체 표현과 lesson 출력에는 값이 노출되지 않음을 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P10-2 세부 완료 기록

- P10-2 dependency boundary
- 상태: 완료
- 완료: `build_note_label()`이 FastAPI 객체 없이 `title`과 `source` 문자열만 받아 결과를 만드는 core 함수임을 annotation과 실행 결과로 확인했다.
- 완료: FastAPI endpoint가 `Request.query_params`의 선택적 값을 확정된 문자열로 바꿔 framework를 모르는 `build_note_label()`에 전달함을 확인했다.
- 완료: `execute_label_use_case()`가 `Callable[[str, str], str]`을 인자로 받아 실제 builder와 fake builder를 바꿔 실행할 수 있음을 확인했다.
- 완료: FastAPI `Depends`가 `get_label_builder()` provider의 함수 객체를 endpoint에 주입하고, endpoint가 이를 application 함수에 전달함을 확인했다.
- 완료: `app.dependency_overrides`에서 production provider를 fake provider로 교체해 endpoint 응답을 바꾸고, 정리 후 원래 응답으로 복원됨을 확인했다.
- 완료: core 직접 호출, callable 주입, HTTP adapter 기본 조립, dependency override와 복원을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P10-3 세부 완료 기록

- P10-3 observability
- 상태: 완료
- 완료: `setup_memory_logger()`로 독립된 Logger, StreamHandler, Formatter를 구성하고 INFO 레벨 필터링과 포맷 경계를 확인했다.
- 완료: `JsonFormatter`를 구현해 기본 로그 속성과 `extra`로 전달된 `event`, `note_id`를 JSON으로 직렬화함을 확인했다.
- 완료: `contextvars.ContextVar`와 `bind_request_id()` 컨텍스트 매니저로 요청별 ID를 바인딩하고 `JsonFormatter`에서 자동 주입 및 종료 후 리셋을 확인했다.
- 완료: `MetricsCollector`의 `track()` 컨텍스트 매니저로 총 요청 수, 오류 수, 소요 시간을 집계하고 예외가 호출자에게 안전하게 재전파됨을 확인했다.
- 완료: `handle_note_request()`에서 사용자에게는 정제된 에러 메시지와 코드만 반환하고, 내부 로그에는 `exc_info=True`로 전체 Traceback을 JSON에 보존하는 오류 경계를 분리했다.
- 완료: 메모리 로거 레벨 필터링, JSON 직렬화, request ID 컨텍스트 전파, 메트릭 집계, 내부 스택트레이스 분리를 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## P10-4 세부 완료 기록

- P10-4 process와 deployment
- 상태: 완료
- 완료: `uvicorn.Config`가 import string과 host, port, worker 설정을 소유하지만 생성만으로 application을 import하거나 server를 시작하지 않음을 확인했다.
- 완료: `config.load()`가 같은 process에서 ASGI callable을 import하고 middleware stack을 준비하며 socket이나 worker를 시작하지 않는 경계를 확인했다.
- 완료: `uvicorn.Server` 객체 생성과 `server.run()`의 실제 socket·event loop·lifespan 시작 시점을 구분했다.
- 완료: 임시 loopback socket과 background thread로 server startup을 관찰하고 `should_exit=True`로 graceful shutdown을 요청해 thread 종료와 같은 PID 유지를 확인했다.
- 완료: `time.monotonic()` 기반 deadline으로 startup 대기를 제한하고 server 조기 종료와 timeout을 별도 오류로 구분했다.
- 완료: liveness는 process 응답 가능성, readiness는 traffic 수신 가능성을 표현하도록 상태 의미를 분리했다.
- 완료: FastAPI lifespan 전·중·후 readiness가 `503 → 200 → 503` 상태로 바뀌고 liveness는 `200`을 유지하도록 HTTP endpoint에 연결했다.
- 완료: `build_container_command()`로 컨테이너 외부 수신을 위한 `0.0.0.0` 바인딩과 포트·워커 검증 및 CLI 명령 리스트 생성을 확인했다.
- 완료: server lifecycle, health endpoint, container command 생성을 공개 behavior test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## 진행 규칙

이해 여부는 별도 주관식 문서가 아니라 실행 결과와 대화로 확인한다. 소단원을 완료하면 관련 변경을 커밋·푸시한 뒤 대기한다. 사용자가 명시적으로 다음 진행을 요청하기 전에는 다음 소단원을 시작하지 않는다.
