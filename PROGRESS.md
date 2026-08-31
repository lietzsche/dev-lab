# 전체 학습 진행 상황

## 현재

- 프로젝트: Python Knowledge Lab
- 단계: P4-1 exception과 traceback
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

## 현재 작은 단계

- P4-1 exception과 traceback
- 상태: 진행 중
- 완료: `raise`로 `ValueError`를 발생시키고 정상 반환이 중단되는 것을 확인했다.
- 완료: 처리되지 않은 exception이 `require_title()`에서 module 실행 경계까지 전파되는 traceback을 확인했다.
- 완료: traceback의 마지막 줄에서 최초 원인의 exception type과 message를 확인하고 위쪽 frame에서 호출 경로를 추적했다.
- 완료: `run()` 경계에서 `ValueError`만 선택적으로 처리하고 exception 객체의 type과 repr을 관찰했다.
- 완료: 처리된 exception은 호출자에게 전파되지 않아 process가 정상 종료되는 것을 확인했다.
- 완료: `try`에서는 실패 가능한 호출만 수행하고 `else`에서 성공 후속 출력을 분리했다.
- 완료: 정상 입력은 `else`, 잘못된 입력은 `except` 중 한 경로로만 실행되는 것을 확인했다.
- 완료: 정상 경로와 `ValueError` 처리 경로 모두에서 `finally`가 마지막에 실행되는 것을 확인했다.
- 완료: `EmptyTitleError`를 `ValueError`의 subclass로 정의하고 구체적인 domain 실패를 표현했다.
- 완료: subclass 객체가 기존 `except ValueError` 처리 경계에 잡히는 exception hierarchy를 확인했다.
- 완료: `ValueError`를 `InvalidNoteIdError`로 변환하면서 `raise ... from ...`으로 원인 객체를 보존했다.
- 완료: 변환된 exception의 `__cause__`가 최초 `ValueError` 객체를 참조하는 것을 type과 repr로 확인했다.
- 완료: `dict` 조회의 `KeyError`를 `NoteNotFoundError`로 변환해 infrastructure 세부사항과 domain 의미를 분리했다.
- 완료: title 검증과 exception chaining의 공개 behavior를 test로 검증했다.
- 다음 소단원은 사용자가 `넘어가자`고 요청한 뒤 시작한다.

## 진행 규칙

이해 여부는 별도 주관식 문서가 아니라 실행 결과와 대화로 확인한다. 소단원을 완료하면 관련 변경을 커밋·푸시한 뒤 대기한다. 사용자가 명시적으로 다음 진행을 요청하기 전에는 다음 소단원을 시작하지 않는다.
