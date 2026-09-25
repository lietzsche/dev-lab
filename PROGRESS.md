# Reliable Data Pipelines 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P1-1** | grain·business key·invariant | grain·business key·invariant의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **P1-2** | schema contract·compatibility | schema contract·compatibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-1 | 대기 | - |
| **P1-3** | event time·processing time·timezone | event time·processing time·timezone의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-2 | 대기 | - |
| **P1-4** | data type·null·semantic validation | data type·null·semantic validation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-3 | 대기 | - |
| **P2-1** | snapshot·append·CDC 선택 | snapshot·append·CDC 선택의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-4 | 대기 | - |
| **P2-2** | checkpoint·cursor·watermark | checkpoint·cursor·watermark의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-1 | 대기 | - |
| **P2-3** | late·out-of-order data | late·out-of-order data의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-2 | 대기 | - |
| **P2-4** | partition·file layout·compaction | partition·file layout·compaction의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-3 | 대기 | - |
| **P3-1** | idempotent transform·determinism | idempotent transform·determinism의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-4 | 대기 | - |
| **P3-2** | upsert·merge·dedup | upsert·merge·dedup의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-1 | 대기 | - |
| **P3-3** | checkpoint·restart·backfill | checkpoint·restart·backfill의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-2 | 대기 | - |
| **P3-4** | transactional publish·concurrent run | transactional publish·concurrent run의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-3 | 대기 | - |
| **P4-1** | quality dimensions·test strategy | quality dimensions·test strategy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-4 | 대기 | - |
| **P4-2** | quarantine·reconciliation | quarantine·reconciliation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-1 | 대기 | - |
| **P4-3** | lineage·code/input/output version | lineage·code/input/output version의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-2 | 대기 | - |
| **P4-4** | ownership·catalog·access·retention | ownership·catalog·access·retention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-3 | 대기 | - |
| **P5-1** | task DAG·dependency·parameter | task DAG·dependency·parameter의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-4 | 대기 | - |
| **P5-2** | retry·timeout·backfill orchestration | retry·timeout·backfill orchestration의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-1 | 대기 | - |
| **P5-3** | freshness·volume·quality observability | freshness·volume·quality observability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-2 | 대기 | - |
| **P5-4** | performance·skew·capacity·cost | performance·skew·capacity·cost의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-3 | 대기 | - |
| **P6-1** | Delta transaction log·time travel | Delta transaction log·time travel의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-4 | 대기 | - |
| **P6-2** | bronze·silver·gold boundary | bronze·silver·gold boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-1 | 대기 | - |
| **P6-3** | batch·stream convergence | batch·stream convergence의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-2 | 대기 | - |
| **P6-4** | serving freshness·RAG index lifecycle | serving freshness·RAG index lifecycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-3 | 대기 | - |

## 세부 기록

### P1-1. grain·business key·invariant

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P1-2. schema contract·compatibility

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P1-3. event time·processing time·timezone

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P1-4. data type·null·semantic validation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P2-1. snapshot·append·CDC 선택

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P2-2. checkpoint·cursor·watermark

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P2-3. late·out-of-order data

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P2-4. partition·file layout·compaction

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P3-1. idempotent transform·determinism

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P3-2. upsert·merge·dedup

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P3-3. checkpoint·restart·backfill

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P3-4. transactional publish·concurrent run

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P4-1. quality dimensions·test strategy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P4-2. quarantine·reconciliation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P4-3. lineage·code/input/output version

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P4-4. ownership·catalog·access·retention

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P5-1. task DAG·dependency·parameter

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P5-2. retry·timeout·backfill orchestration

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P5-3. freshness·volume·quality observability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P5-4. performance·skew·capacity·cost

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P6-1. Delta transaction log·time travel

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P6-2. bronze·silver·gold boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P6-3. batch·stream convergence

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### P6-4. serving freshness·RAG index lifecycle

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
