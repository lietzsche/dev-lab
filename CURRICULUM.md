# Distributed Systems Foundations 커리큘럼

## 목적

부분 실패와 동시성 아래 불변식과 복구를 설계한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Network·DB 기본
- 최종 실습: 중복·지연·partition 아래 workflow 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **D1** | 시간·실패 | clock·order·deadline | 지연·부분 실패 |
| **D2** | 복제·일관성 | version·lag·quorum | 동시 read/write |
| **D3** | 동시성 | transaction·version·lock | lost update·deadlock |
| **D4** | 메시징 | offset·ack·DLQ | crash·redelivery |
| **D5** | Workflow | outbox·saga·retry | commit/publish 실패 |
| **D6** | 운영 | trace·SLI·fault result | 부하·장애 검증 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **D1-1** | 시간과 순서 | 시간과 순서의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **D1-2** | timeout·deadline | timeout·deadline의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D1-1 |
| **D1-3** | failure model | failure model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D1-2 |
| **D2-1** | replication lag | replication lag의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D1-3 |
| **D2-2** | consistency model | consistency model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D2-1 |
| **D2-3** | quorum·split brain | quorum·split brain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D2-2 |
| **D3-1** | isolation anomaly | isolation anomaly의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D2-3 |
| **D3-2** | optimistic locking | optimistic locking의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D3-1 |
| **D3-3** | idempotency | idempotency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D3-2 |
| **D4-1** | queue·log·pubsub | queue·log·pubsub의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D3-3 |
| **D4-2** | delivery semantics | delivery semantics의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D4-1 |
| **D4-3** | ordering·backpressure | ordering·backpressure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D4-2 |
| **D5-1** | outbox·CDC | outbox·CDC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D4-3 |
| **D5-2** | saga·compensation | saga·compensation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D5-1 |
| **D5-3** | circuit breaker | circuit breaker의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D5-2 |
| **D6-1** | distributed tracing | distributed tracing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D5-3 |
| **D6-2** | SLO·load shedding | SLO·load shedding의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D6-1 |
| **D6-3** | fault injection | fault injection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | D6-2 |

## 상세 커리큘럼

### [D1-1] 시간과 순서

- 목표: 시간과 순서의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: clock·order·deadline를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 지연·부분 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D1-2] timeout·deadline

- 목표: timeout·deadline의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: clock·order·deadline를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 지연·부분 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D1-3] failure model

- 목표: failure model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: clock·order·deadline를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 지연·부분 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D2-1] replication lag

- 목표: replication lag의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: version·lag·quorum를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 동시 read/write 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D2-2] consistency model

- 목표: consistency model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: version·lag·quorum를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 동시 read/write 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D2-3] quorum·split brain

- 목표: quorum·split brain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: version·lag·quorum를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 동시 read/write 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D3-1] isolation anomaly

- 목표: isolation anomaly의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: transaction·version·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: lost update·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D3-2] optimistic locking

- 목표: optimistic locking의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: transaction·version·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: lost update·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D3-3] idempotency

- 목표: idempotency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: transaction·version·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: lost update·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D4-1] queue·log·pubsub

- 목표: queue·log·pubsub의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: offset·ack·DLQ를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: crash·redelivery 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D4-2] delivery semantics

- 목표: delivery semantics의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: offset·ack·DLQ를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: crash·redelivery 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D4-3] ordering·backpressure

- 목표: ordering·backpressure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: offset·ack·DLQ를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: crash·redelivery 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D5-1] outbox·CDC

- 목표: outbox·CDC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: outbox·saga·retry를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: commit/publish 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D5-2] saga·compensation

- 목표: saga·compensation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: outbox·saga·retry를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: commit/publish 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D5-3] circuit breaker

- 목표: circuit breaker의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: outbox·saga·retry를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: commit/publish 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D6-1] distributed tracing

- 목표: distributed tracing의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·SLI·fault result를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부하·장애 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D6-2] SLO·load shedding

- 목표: SLO·load shedding의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·SLI·fault result를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부하·장애 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [D6-3] fault injection

- 목표: fault injection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·SLI·fault result를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부하·장애 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
