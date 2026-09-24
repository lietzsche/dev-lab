# Reliable Data Pipelines 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`, 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P1-1** | grain·key | grain·key의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - | 대기 | - |
| **P1-2** | schema evolution | schema evolution의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-1 | 대기 | - |
| **P1-3** | event vs processing time | event vs processing time의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-2 | 대기 | - |
| **P2-1** | snapshot·CDC | snapshot·CDC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-3 | 대기 | - |
| **P2-2** | watermark | watermark의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-1 | 대기 | - |
| **P2-3** | partition·file layout | partition·file layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-2 | 대기 | - |
| **P3-1** | idempotent merge | idempotent merge의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-3 | 대기 | - |
| **P3-2** | restart·backfill | restart·backfill의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-1 | 대기 | - |
| **P3-3** | concurrent run | concurrent run의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-2 | 대기 | - |
| **P4-1** | data quality | data quality의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-3 | 대기 | - |
| **P4-2** | lineage·provenance | lineage·provenance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-1 | 대기 | - |
| **P4-3** | reconciliation | reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-2 | 대기 | - |
| **P5-1** | orchestration | orchestration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-3 | 대기 | - |
| **P5-2** | SLA·observability | SLA·observability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-1 | 대기 | - |
| **P5-3** | performance·cost | performance·cost의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-2 | 대기 | - |
| **P6-1** | Delta transaction | Delta transaction의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-3 | 대기 | - |
| **P6-2** | governance·retention | governance·retention의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P6-1 | 대기 | - |
| **P6-3** | batch·stream·serving | batch·stream·serving의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P6-2 | 대기 | - |

## 세부 기록

### P1-1. grain·key

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P1-2. schema evolution

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P1-3. event vs processing time

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P2-1. snapshot·CDC

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P2-2. watermark

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P2-3. partition·file layout

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P3-1. idempotent merge

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P3-2. restart·backfill

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P3-3. concurrent run

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P4-1. data quality

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P4-2. lineage·provenance

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P4-3. reconciliation

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P5-1. orchestration

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P5-2. SLA·observability

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P5-3. performance·cost

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P6-1. Delta transaction

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P6-2. governance·retention

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### P6-3. batch·stream·serving

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:
