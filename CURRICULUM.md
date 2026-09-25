# Distributed Systems Foundations 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Model·Time·Failure 단계에서 가정과 불변식을 먼저 명시할 수 있는가?
- Replication·Consistency 단계에서 업무 요구에 맞는 consistency 선택할 수 있는가?
- Transaction·Concurrency 단계에서 DB와 application 불변식 결합할 수 있는가?
- Messaging·Streaming 단계에서 delivery보다 business effect 기준 설계할 수 있는가?
- Workflow·Data consistency 단계에서 중단 후 재개 가능한 long-running process할 수 있는가?
- Reliability·Operation 단계에서 운영에서 가정을 검증하는 방법 확립할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **D1** | Model·Time·Failure | 5 | 가정과 불변식을 먼저 명시 |
| **D2** | Replication·Consistency | 5 | 업무 요구에 맞는 consistency 선택 |
| **D3** | Transaction·Concurrency | 5 | DB와 application 불변식 결합 |
| **D4** | Messaging·Streaming | 5 | delivery보다 business effect 기준 설계 |
| **D5** | Workflow·Data consistency | 5 | 중단 후 재개 가능한 long-running process |
| **D6** | Reliability·Operation | 5 | 운영에서 가정을 검증하는 방법 확립 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **D1-1** | system model·safety·liveness | system model·safety·liveness의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **D1-2** | physical·monotonic clock | physical·monotonic clock의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-1 |
| **D1-3** | logical clock·causal order | logical clock·causal order의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-2 |
| **D1-4** | partial failure·failure detector | partial failure·failure detector의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-3 |
| **D1-5** | timeout·deadline·cancellation budget | timeout·deadline·cancellation budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-4 |
| **D2-1** | replication topology·lag | replication topology·lag의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D1-5 |
| **D2-2** | leader election·term·fencing | leader election·term·fencing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-1 |
| **D2-3** | quorum read/write | quorum read/write의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-2 |
| **D2-4** | linearizable·sequential·eventual | linearizable·sequential·eventual의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-3 |
| **D2-5** | CAP·PACELC를 실제 latency와 연결 | CAP·PACELC를 실제 latency와 연결의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-4 |
| **D3-1** | ACID boundary·commit outcome | ACID boundary·commit outcome의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D2-5 |
| **D3-2** | isolation anomaly·MVCC | isolation anomaly·MVCC의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-1 |
| **D3-3** | optimistic concurrency·CAS | optimistic concurrency·CAS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-2 |
| **D3-4** | pessimistic lock·deadlock | pessimistic lock·deadlock의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-3 |
| **D3-5** | distributed lock·lease·fencing | distributed lock·lease·fencing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-4 |
| **D4-1** | queue·pubsub·append log | queue·pubsub·append log의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D3-5 |
| **D4-2** | partition·ordering·consumer group | partition·ordering·consumer group의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-1 |
| **D4-3** | at-most/at-least/effectively-once | at-most/at-least/effectively-once의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-2 |
| **D4-4** | ack·retry·DLQ·poison message | ack·retry·DLQ·poison message의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-3 |
| **D4-5** | backpressure·flow control·load shedding | backpressure·flow control·load shedding의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-4 |
| **D5-1** | idempotency key·dedup store | idempotency key·dedup store의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D4-5 |
| **D5-2** | transactional outbox·CDC | transactional outbox·CDC의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-1 |
| **D5-3** | saga orchestration·choreography | saga orchestration·choreography의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-2 |
| **D5-4** | compensation·semantic rollback | compensation·semantic rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-3 |
| **D5-5** | workflow checkpoint·recovery | workflow checkpoint·recovery의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-4 |
| **D6-1** | retry·backoff·jitter·budget | retry·backoff·jitter·budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D5-5 |
| **D6-2** | circuit breaker·bulkhead | circuit breaker·bulkhead의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-1 |
| **D6-3** | distributed tracing·correlation | distributed tracing·correlation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-2 |
| **D6-4** | SLI·SLO·error budget·capacity | SLI·SLO·error budget·capacity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-3 |
| **D6-5** | fault injection·load test·incident review | fault injection·load test·incident review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | D6-4 |

## D1. Model·Time·Failure

- 관찰 축: state machine·clock·order·failure detector
- 통합 실습: delay·clock skew·crash·partition 주입
- 핵심 실패: timeout을 failure로 오판·unknown outcome

### [D1-1] system model·safety·liveness

- 이해할 것: system model·safety·liveness을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: state machine·clock·order·failure detector 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: delay·clock skew·crash·partition 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: timeout을 failure로 오판·unknown outcome 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D1-2] physical·monotonic clock

- 이해할 것: physical·monotonic clock을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: state machine·clock·order·failure detector 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: delay·clock skew·crash·partition 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: timeout을 failure로 오판·unknown outcome 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D1-3] logical clock·causal order

- 이해할 것: logical clock·causal order을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: state machine·clock·order·failure detector 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: delay·clock skew·crash·partition 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: timeout을 failure로 오판·unknown outcome 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D1-4] partial failure·failure detector

- 이해할 것: partial failure·failure detector을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: state machine·clock·order·failure detector 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: delay·clock skew·crash·partition 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: timeout을 failure로 오판·unknown outcome 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D1-5] timeout·deadline·cancellation budget

- 이해할 것: timeout·deadline·cancellation budget을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: state machine·clock·order·failure detector 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: delay·clock skew·crash·partition 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: timeout을 failure로 오판·unknown outcome 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D1 단계 결과물

- 가정과 불변식을 먼저 명시.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## D2. Replication·Consistency

- 관찰 축: leader·log·quorum·lag·read guarantee
- 통합 실습: replica delay와 failover 관찰
- 핵심 실패: split brain·stale read·lost acknowledged write

### [D2-1] replication topology·lag

- 이해할 것: replication topology·lag을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: leader·log·quorum·lag·read guarantee 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: replica delay와 failover 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: split brain·stale read·lost acknowledged write 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D2-2] leader election·term·fencing

- 이해할 것: leader election·term·fencing을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: leader·log·quorum·lag·read guarantee 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: replica delay와 failover 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: split brain·stale read·lost acknowledged write 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D2-3] quorum read/write

- 이해할 것: quorum read/write을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: leader·log·quorum·lag·read guarantee 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: replica delay와 failover 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: split brain·stale read·lost acknowledged write 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D2-4] linearizable·sequential·eventual

- 이해할 것: linearizable·sequential·eventual을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: leader·log·quorum·lag·read guarantee 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: replica delay와 failover 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: split brain·stale read·lost acknowledged write 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D2-5] CAP·PACELC를 실제 latency와 연결

- 이해할 것: CAP·PACELC를 실제 latency와 연결을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: leader·log·quorum·lag·read guarantee 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: replica delay와 failover 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: split brain·stale read·lost acknowledged write 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D2 단계 결과물

- 업무 요구에 맞는 consistency 선택.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## D3. Transaction·Concurrency

- 관찰 축: isolation·MVCC·lock·version·fencing token
- 통합 실습: lost update·write skew·deadlock 재현
- 핵심 실패: retry가 중복 효과 생성·stale lock holder

### [D3-1] ACID boundary·commit outcome

- 이해할 것: ACID boundary·commit outcome을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: isolation·MVCC·lock·version·fencing token 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: lost update·write skew·deadlock 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry가 중복 효과 생성·stale lock holder 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D3-2] isolation anomaly·MVCC

- 이해할 것: isolation anomaly·MVCC을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: isolation·MVCC·lock·version·fencing token 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: lost update·write skew·deadlock 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry가 중복 효과 생성·stale lock holder 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D3-3] optimistic concurrency·CAS

- 이해할 것: optimistic concurrency·CAS을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: isolation·MVCC·lock·version·fencing token 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: lost update·write skew·deadlock 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry가 중복 효과 생성·stale lock holder 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D3-4] pessimistic lock·deadlock

- 이해할 것: pessimistic lock·deadlock을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: isolation·MVCC·lock·version·fencing token 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: lost update·write skew·deadlock 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry가 중복 효과 생성·stale lock holder 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D3-5] distributed lock·lease·fencing

- 이해할 것: distributed lock·lease·fencing을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: isolation·MVCC·lock·version·fencing token 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: lost update·write skew·deadlock 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry가 중복 효과 생성·stale lock holder 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D3 단계 결과물

- DB와 application 불변식 결합.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## D4. Messaging·Streaming

- 관찰 축: queue/log·partition·offset·ack·consumer group
- 통합 실습: crash 전후 redelivery와 rebalance
- 핵심 실패: poison message·hot partition·out-of-order

### [D4-1] queue·pubsub·append log

- 이해할 것: queue·pubsub·append log을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: queue/log·partition·offset·ack·consumer group 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash 전후 redelivery와 rebalance에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: poison message·hot partition·out-of-order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D4-2] partition·ordering·consumer group

- 이해할 것: partition·ordering·consumer group을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: queue/log·partition·offset·ack·consumer group 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash 전후 redelivery와 rebalance에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: poison message·hot partition·out-of-order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D4-3] at-most/at-least/effectively-once

- 이해할 것: at-most/at-least/effectively-once을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: queue/log·partition·offset·ack·consumer group 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash 전후 redelivery와 rebalance에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: poison message·hot partition·out-of-order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D4-4] ack·retry·DLQ·poison message

- 이해할 것: ack·retry·DLQ·poison message을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: queue/log·partition·offset·ack·consumer group 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash 전후 redelivery와 rebalance에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: poison message·hot partition·out-of-order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D4-5] backpressure·flow control·load shedding

- 이해할 것: backpressure·flow control·load shedding을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: queue/log·partition·offset·ack·consumer group 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash 전후 redelivery와 rebalance에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: poison message·hot partition·out-of-order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D4 단계 결과물

- delivery보다 business effect 기준 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## D5. Workflow·Data consistency

- 관찰 축: outbox·CDC·saga·dedup·state machine
- 통합 실습: commit/publish·step/compensation 실패
- 핵심 실패: dual write·compensation failure·stuck workflow

### [D5-1] idempotency key·dedup store

- 이해할 것: idempotency key·dedup store을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: outbox·CDC·saga·dedup·state machine 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: commit/publish·step/compensation 실패에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dual write·compensation failure·stuck workflow 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D5-2] transactional outbox·CDC

- 이해할 것: transactional outbox·CDC을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: outbox·CDC·saga·dedup·state machine 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: commit/publish·step/compensation 실패에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dual write·compensation failure·stuck workflow 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D5-3] saga orchestration·choreography

- 이해할 것: saga orchestration·choreography을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: outbox·CDC·saga·dedup·state machine 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: commit/publish·step/compensation 실패에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dual write·compensation failure·stuck workflow 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D5-4] compensation·semantic rollback

- 이해할 것: compensation·semantic rollback을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: outbox·CDC·saga·dedup·state machine 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: commit/publish·step/compensation 실패에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dual write·compensation failure·stuck workflow 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D5-5] workflow checkpoint·recovery

- 이해할 것: workflow checkpoint·recovery을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: outbox·CDC·saga·dedup·state machine 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: commit/publish·step/compensation 실패에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dual write·compensation failure·stuck workflow 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D5 단계 결과물

- 중단 후 재개 가능한 long-running process.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## D6. Reliability·Operation

- 관찰 축: retry budget·circuit·bulkhead·trace·SLO
- 통합 실습: dependency degradation과 chaos experiment
- 핵심 실패: retry storm·cascading failure·coordinated omission

### [D6-1] retry·backoff·jitter·budget

- 이해할 것: retry·backoff·jitter·budget을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: retry budget·circuit·bulkhead·trace·SLO 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: dependency degradation과 chaos experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·cascading failure·coordinated omission 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D6-2] circuit breaker·bulkhead

- 이해할 것: circuit breaker·bulkhead을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: retry budget·circuit·bulkhead·trace·SLO 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: dependency degradation과 chaos experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·cascading failure·coordinated omission 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D6-3] distributed tracing·correlation

- 이해할 것: distributed tracing·correlation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: retry budget·circuit·bulkhead·trace·SLO 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: dependency degradation과 chaos experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·cascading failure·coordinated omission 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D6-4] SLI·SLO·error budget·capacity

- 이해할 것: SLI·SLO·error budget·capacity을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: retry budget·circuit·bulkhead·trace·SLO 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: dependency degradation과 chaos experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·cascading failure·coordinated omission 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [D6-5] fault injection·load test·incident review

- 이해할 것: fault injection·load test·incident review을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: retry budget·circuit·bulkhead·trace·SLO 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: dependency degradation과 chaos experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·cascading failure·coordinated omission 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### D6 단계 결과물

- 운영에서 가정을 검증하는 방법 확립.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
