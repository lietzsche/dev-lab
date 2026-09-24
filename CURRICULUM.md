# JavaScript Runtime & TypeScript Systems 커리큘럼

## 목적

JS runtime과 type 경계로 agent UI·자동화 도구를 개발한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: JavaScript 경험
- 최종 실습: agent dashboard·Playwright·CLI 연결
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **T1** | JS 실행 | stack·heap·task queue | 순서 예측 |
| **T2** | TS 타입 | inference·emit·diagnostic | compile/runtime 비교 |
| **T3** | Runtime 경계 | payload·validation·source map | 깨진 외부 값 차단 |
| **T4** | Node | process·stream·fd | child·signal 재현 |
| **T5** | Web·React | render·state·network | race·stale state |
| **T6** | 품질·운영 | unit·e2e·bundle·trace | 회귀 CI 검출 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **T1-1** | value·prototype | value·prototype의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **T1-2** | closure·this·module | closure·this·module의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T1-1 |
| **T1-3** | event loop·Promise | event loop·Promise의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T1-2 |
| **T2-1** | structural typing | structural typing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T1-3 |
| **T2-2** | union·narrowing | union·narrowing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T2-1 |
| **T2-3** | generic·variance | generic·variance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T2-2 |
| **T3-1** | unknown·validation | unknown·validation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T2-3 |
| **T3-2** | typed error | typed error의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T3-1 |
| **T3-3** | ESM·package | ESM·package의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T3-2 |
| **T4-1** | stream·backpressure | stream·backpressure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T3-3 |
| **T4-2** | CLI·signal | CLI·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T4-1 |
| **T4-3** | worker concurrency | worker concurrency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T4-2 |
| **T5-1** | browser lifecycle | browser lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T4-3 |
| **T5-2** | React effect | React effect의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T5-1 |
| **T5-3** | API cache·form | API cache·form의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T5-2 |
| **T6-1** | test boundary | test boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T5-3 |
| **T6-2** | Playwright flaky | Playwright flaky의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T6-1 |
| **T6-3** | observability·release | observability·release의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | T6-2 |

## 상세 커리큘럼

### [T1-1] value·prototype

- 목표: value·prototype의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: stack·heap·task queue를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 순서 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T1-2] closure·this·module

- 목표: closure·this·module의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: stack·heap·task queue를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 순서 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T1-3] event loop·Promise

- 목표: event loop·Promise의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: stack·heap·task queue를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 순서 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T2-1] structural typing

- 목표: structural typing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inference·emit·diagnostic를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile/runtime 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T2-2] union·narrowing

- 목표: union·narrowing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inference·emit·diagnostic를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile/runtime 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T2-3] generic·variance

- 목표: generic·variance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inference·emit·diagnostic를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile/runtime 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T3-1] unknown·validation

- 목표: unknown·validation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: payload·validation·source map를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 깨진 외부 값 차단 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T3-2] typed error

- 목표: typed error의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: payload·validation·source map를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 깨진 외부 값 차단 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T3-3] ESM·package

- 목표: ESM·package의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: payload·validation·source map를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 깨진 외부 값 차단 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T4-1] stream·backpressure

- 목표: stream·backpressure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: process·stream·fd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: child·signal 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T4-2] CLI·signal

- 목표: CLI·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: process·stream·fd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: child·signal 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T4-3] worker concurrency

- 목표: worker concurrency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: process·stream·fd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: child·signal 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T5-1] browser lifecycle

- 목표: browser lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: render·state·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·stale state 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T5-2] React effect

- 목표: React effect의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: render·state·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·stale state 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T5-3] API cache·form

- 목표: API cache·form의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: render·state·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·stale state 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T6-1] test boundary

- 목표: test boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: unit·e2e·bundle·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 회귀 CI 검출 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T6-2] Playwright flaky

- 목표: Playwright flaky의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: unit·e2e·bundle·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 회귀 CI 검출 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [T6-3] observability·release

- 목표: observability·release의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: unit·e2e·bundle·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 회귀 CI 검출 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
