# Distributed Systems Foundations 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **D1-1** | system model·safety·liveness | system model·safety·liveness의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **D1-2** | physical·monotonic clock | physical·monotonic clock의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-1 | 대기 | - |
| **D1-3** | logical clock·causal order | logical clock·causal order의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-2 | 대기 | - |
| **D1-4** | partial failure·failure detector | partial failure·failure detector의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-3 | 대기 | - |
| **D1-5** | timeout·deadline·cancellation budget | timeout·deadline·cancellation budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-4 | 대기 | - |
| **D2-1** | replication topology·lag | replication topology·lag의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-5 | 대기 | - |
| **D2-2** | leader election·term·fencing | leader election·term·fencing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-1 | 대기 | - |
| **D2-3** | quorum read/write | quorum read/write의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-2 | 대기 | - |
| **D2-4** | linearizable·sequential·eventual | linearizable·sequential·eventual의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-3 | 대기 | - |
| **D2-5** | CAP·PACELC를 실제 latency와 연결 | CAP·PACELC를 실제 latency와 연결의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-4 | 대기 | - |
| **D3-1** | ACID boundary·commit outcome | ACID boundary·commit outcome의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-5 | 대기 | - |
| **D3-2** | isolation anomaly·MVCC | isolation anomaly·MVCC의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-1 | 대기 | - |
| **D3-3** | optimistic concurrency·CAS | optimistic concurrency·CAS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-2 | 대기 | - |
| **D3-4** | pessimistic lock·deadlock | pessimistic lock·deadlock의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-3 | 대기 | - |
| **D3-5** | distributed lock·lease·fencing | distributed lock·lease·fencing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-4 | 대기 | - |
| **D4-1** | queue·pubsub·append log | queue·pubsub·append log의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-5 | 대기 | - |
| **D4-2** | partition·ordering·consumer group | partition·ordering·consumer group의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-1 | 대기 | - |
| **D4-3** | at-most/at-least/effectively-once | at-most/at-least/effectively-once의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-2 | 대기 | - |
| **D4-4** | ack·retry·DLQ·poison message | ack·retry·DLQ·poison message의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-3 | 대기 | - |
| **D4-5** | backpressure·flow control·load shedding | backpressure·flow control·load shedding의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-4 | 대기 | - |
| **D5-1** | idempotency key·dedup store | idempotency key·dedup store의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-5 | 대기 | - |
| **D5-2** | transactional outbox·CDC | transactional outbox·CDC의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-1 | 대기 | - |
| **D5-3** | saga orchestration·choreography | saga orchestration·choreography의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-2 | 대기 | - |
| **D5-4** | compensation·semantic rollback | compensation·semantic rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-3 | 대기 | - |
| **D5-5** | workflow checkpoint·recovery | workflow checkpoint·recovery의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-4 | 대기 | - |
| **D6-1** | retry·backoff·jitter·budget | retry·backoff·jitter·budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-5 | 대기 | - |
| **D6-2** | circuit breaker·bulkhead | circuit breaker·bulkhead의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-1 | 대기 | - |
| **D6-3** | distributed tracing·correlation | distributed tracing·correlation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-2 | 대기 | - |
| **D6-4** | SLI·SLO·error budget·capacity | SLI·SLO·error budget·capacity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-3 | 대기 | - |
| **D6-5** | fault injection·load test·incident review | fault injection·load test·incident review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-4 | 대기 | - |

## 세부 기록

### D1-1. system model·safety·liveness

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D1-2. physical·monotonic clock

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D1-3. logical clock·causal order

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D1-4. partial failure·failure detector

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D1-5. timeout·deadline·cancellation budget

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D2-1. replication topology·lag

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D2-2. leader election·term·fencing

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D2-3. quorum read/write

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D2-4. linearizable·sequential·eventual

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D2-5. CAP·PACELC를 실제 latency와 연결

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D3-1. ACID boundary·commit outcome

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D3-2. isolation anomaly·MVCC

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D3-3. optimistic concurrency·CAS

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D3-4. pessimistic lock·deadlock

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D3-5. distributed lock·lease·fencing

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D4-1. queue·pubsub·append log

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D4-2. partition·ordering·consumer group

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D4-3. at-most/at-least/effectively-once

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D4-4. ack·retry·DLQ·poison message

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D4-5. backpressure·flow control·load shedding

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D5-1. idempotency key·dedup store

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D5-2. transactional outbox·CDC

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D5-3. saga orchestration·choreography

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D5-4. compensation·semantic rollback

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D5-5. workflow checkpoint·recovery

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D6-1. retry·backoff·jitter·budget

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D6-2. circuit breaker·bulkhead

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D6-3. distributed tracing·correlation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D6-4. SLI·SLO·error budget·capacity

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### D6-5. fault injection·load test·incident review

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
