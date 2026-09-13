# 전체 학습 진행 상황

## 현재

- 프로젝트: Python Knowledge Lab
- 단계: P7-3 SQLite와 transaction
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

## 현재 작은 단계

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

## 진행 규칙

이해 여부는 별도 주관식 문서가 아니라 실행 결과와 대화로 확인한다. 소단원을 완료하면 관련 변경을 커밋·푸시한 뒤 대기한다. 사용자가 명시적으로 다음 진행을 요청하기 전에는 다음 소단원을 시작하지 않는다.
