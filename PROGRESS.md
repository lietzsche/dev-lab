# 전체 학습 진행 상황

## 현재

- 프로젝트: Python Knowledge Lab
- 단계: P4-4 project와 dependency
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

## 현재 작은 단계

- P4-4 project와 dependency
- 상태: 완료
- 완료: distribution 이름 `knowledge-lab`과 import package 이름 `knowledge_lab`이 서로 다른 경계의 식별자임을 확인했다.
- 완료: import된 module 객체의 `__name__`이 import package 이름을 사용하는 것을 확인했다.
- 완료: `sys.executable`, `sys.prefix`, `sys.base_prefix`를 비교해 `.venv` interpreter와 기반 Python의 경계를 확인했다.
- 완료: `sys.prefix != sys.base_prefix`가 `True`인 virtual environment 실행 상태를 확인했다.
- 완료: `python -m pip show`와 `importlib.metadata.distribution()`이 같은 설치 환경의 distribution 이름과 version을 조회하는 것을 확인했다.
- 완료: editable install이 `.venv`의 metadata와 작업 중인 source directory를 연결해 `PYTHONPATH` 없이 import되는 것을 확인했다.
- 완료: `tomllib`으로 `pyproject.toml`의 build backend와 project metadata를 읽고 두 section의 역할을 구분했다.
- 완료: TOML을 읽은 뒤 file resource는 닫히고 별도로 생성된 config dict는 계속 사용되는 소유권 경계를 확인했다.
- 완료: build requirement인 setuptools가 격리된 build 환경에서 사용될 수 있으며 현재 runtime 환경에는 설치되지 않은 것을 확인했다.
- 완료: `[project].dependencies`가 비어 있어 애플리케이션 runtime dependency도 없음을 `pip freeze`와 비교했다.
- 완료: `[project].dependencies`가 설치 시 distribution의 `Requires-Dist` metadata로 변환되는 경계를 확인했다.
- 완료: dependency가 없는 metadata의 `None`을 빈 list로 정규화해 선언 상태와 비교했다.
- 완료: `[project.scripts]`의 `knowledge_lab.__main__:main`이 `.venv/bin/knowledge-lab` wrapper로 생성되는 것을 확인했다.
- 완료: console script의 shebang, import, 함수 호출을 거쳐 `python -m knowledge_lab`과 같은 entry point가 실행되는 것을 확인했다.
- 완료: `pip check`로 현재 environment에 누락되거나 충돌하는 requirement가 없음을 확인했다.
- 완료: dependency 선언, 설치 environment snapshot, lockfile의 서로 다른 역할을 구분했다.
- 완료: 외부 runtime dependency가 없는 현재 단계에서는 별도 lockfile을 만들지 않고 표준 `venv`, pip, `pyproject.toml`을 유지하기로 했다.
- 완료: project metadata와 console entry point의 공개 behavior를 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## 진행 규칙

이해 여부는 별도 주관식 문서가 아니라 실행 결과와 대화로 확인한다. 소단원을 완료하면 관련 변경을 커밋·푸시한 뒤 대기한다. 사용자가 명시적으로 다음 진행을 요청하기 전에는 다음 소단원을 시작하지 않는다.
