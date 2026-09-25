# Reliable Data Pipelines 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Data contract와 modeling 단계에서 table 한 행과 consumer 계약 명시할 수 있는가?
- Ingestion과 incremental state 단계에서 변경 포착과 진행 상태를 복구 가능하게 저장할 수 있는가?
- Idempotency와 transaction 단계에서 임의 지점 재실행에도 결과 불변할 수 있는가?
- Quality·Lineage·Governance 단계에서 감사 가능한 data product 구성할 수 있는가?
- Orchestration·Observability·Cost 단계에서 SLA와 비용을 함께 운영할 수 있는가?
- Lakehouse와 serving 단계에서 현재 실무 pipeline을 원리로 설명·개선할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 24소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **P1** | Data contract와 modeling | 4 | table 한 행과 consumer 계약 명시 |
| **P2** | Ingestion과 incremental state | 4 | 변경 포착과 진행 상태를 복구 가능하게 저장 |
| **P3** | Idempotency와 transaction | 4 | 임의 지점 재실행에도 결과 불변 |
| **P4** | Quality·Lineage·Governance | 4 | 감사 가능한 data product 구성 |
| **P5** | Orchestration·Observability·Cost | 4 | SLA와 비용을 함께 운영 |
| **P6** | Lakehouse와 serving | 4 | 현재 실무 pipeline을 원리로 설명·개선 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **P1-1** | grain·business key·invariant | grain·business key·invariant의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **P1-2** | schema contract·compatibility | schema contract·compatibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-1 |
| **P1-3** | event time·processing time·timezone | event time·processing time·timezone의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-2 |
| **P1-4** | data type·null·semantic validation | data type·null·semantic validation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-3 |
| **P2-1** | snapshot·append·CDC 선택 | snapshot·append·CDC 선택의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P1-4 |
| **P2-2** | checkpoint·cursor·watermark | checkpoint·cursor·watermark의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-1 |
| **P2-3** | late·out-of-order data | late·out-of-order data의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-2 |
| **P2-4** | partition·file layout·compaction | partition·file layout·compaction의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-3 |
| **P3-1** | idempotent transform·determinism | idempotent transform·determinism의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P2-4 |
| **P3-2** | upsert·merge·dedup | upsert·merge·dedup의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-1 |
| **P3-3** | checkpoint·restart·backfill | checkpoint·restart·backfill의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-2 |
| **P3-4** | transactional publish·concurrent run | transactional publish·concurrent run의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-3 |
| **P4-1** | quality dimensions·test strategy | quality dimensions·test strategy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P3-4 |
| **P4-2** | quarantine·reconciliation | quarantine·reconciliation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-1 |
| **P4-3** | lineage·code/input/output version | lineage·code/input/output version의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-2 |
| **P4-4** | ownership·catalog·access·retention | ownership·catalog·access·retention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-3 |
| **P5-1** | task DAG·dependency·parameter | task DAG·dependency·parameter의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P4-4 |
| **P5-2** | retry·timeout·backfill orchestration | retry·timeout·backfill orchestration의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-1 |
| **P5-3** | freshness·volume·quality observability | freshness·volume·quality observability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-2 |
| **P5-4** | performance·skew·capacity·cost | performance·skew·capacity·cost의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-3 |
| **P6-1** | Delta transaction log·time travel | Delta transaction log·time travel의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P5-4 |
| **P6-2** | bronze·silver·gold boundary | bronze·silver·gold boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-1 |
| **P6-3** | batch·stream convergence | batch·stream convergence의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-2 |
| **P6-4** | serving freshness·RAG index lifecycle | serving freshness·RAG index lifecycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | P6-3 |

## P1. Data contract와 modeling

- 관찰 축: grain·key·schema·event time·quality invariant
- 통합 실습: source fixture의 중복·null·schema drift
- 핵심 실패: 잘못된 grain·silent coercion·timezone drift

### [P1-1] grain·business key·invariant

- 이해할 것: grain·business key·invariant을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: grain·key·schema·event time·quality invariant 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: source fixture의 중복·null·schema drift에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 grain·silent coercion·timezone drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P1-2] schema contract·compatibility

- 이해할 것: schema contract·compatibility을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: grain·key·schema·event time·quality invariant 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: source fixture의 중복·null·schema drift에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 grain·silent coercion·timezone drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P1-3] event time·processing time·timezone

- 이해할 것: event time·processing time·timezone을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: grain·key·schema·event time·quality invariant 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: source fixture의 중복·null·schema drift에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 grain·silent coercion·timezone drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P1-4] data type·null·semantic validation

- 이해할 것: data type·null·semantic validation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: grain·key·schema·event time·quality invariant 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: source fixture의 중복·null·schema drift에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 grain·silent coercion·timezone drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P1 단계 결과물

- table 한 행과 consumer 계약 명시.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## P2. Ingestion과 incremental state

- 관찰 축: snapshot·CDC·cursor·watermark·partition
- 통합 실습: full/incremental 결과 대조
- 핵심 실패: missed update·late event·small files

### [P2-1] snapshot·append·CDC 선택

- 이해할 것: snapshot·append·CDC 선택을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: snapshot·CDC·cursor·watermark·partition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: full/incremental 결과 대조에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: missed update·late event·small files 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P2-2] checkpoint·cursor·watermark

- 이해할 것: checkpoint·cursor·watermark을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: snapshot·CDC·cursor·watermark·partition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: full/incremental 결과 대조에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: missed update·late event·small files 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P2-3] late·out-of-order data

- 이해할 것: late·out-of-order data을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: snapshot·CDC·cursor·watermark·partition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: full/incremental 결과 대조에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: missed update·late event·small files 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P2-4] partition·file layout·compaction

- 이해할 것: partition·file layout·compaction을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: snapshot·CDC·cursor·watermark·partition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: full/incremental 결과 대조에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: missed update·late event·small files 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P2 단계 결과물

- 변경 포착과 진행 상태를 복구 가능하게 저장.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## P3. Idempotency와 transaction

- 관찰 축: run identity·merge·publish·concurrency
- 통합 실습: 중간 crash·duplicate input·parallel run
- 핵심 실패: partial publish·double effect·stale checkpoint

### [P3-1] idempotent transform·determinism

- 이해할 것: idempotent transform·determinism을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: run identity·merge·publish·concurrency 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 중간 crash·duplicate input·parallel run에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: partial publish·double effect·stale checkpoint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P3-2] upsert·merge·dedup

- 이해할 것: upsert·merge·dedup을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: run identity·merge·publish·concurrency 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 중간 crash·duplicate input·parallel run에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: partial publish·double effect·stale checkpoint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P3-3] checkpoint·restart·backfill

- 이해할 것: checkpoint·restart·backfill을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: run identity·merge·publish·concurrency 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 중간 crash·duplicate input·parallel run에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: partial publish·double effect·stale checkpoint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P3-4] transactional publish·concurrent run

- 이해할 것: transactional publish·concurrent run을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: run identity·merge·publish·concurrency 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 중간 crash·duplicate input·parallel run에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: partial publish·double effect·stale checkpoint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P3 단계 결과물

- 임의 지점 재실행에도 결과 불변.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## P4. Quality·Lineage·Governance

- 관찰 축: rule result·quarantine·provenance·catalog
- 통합 실습: 오염 차단과 downstream impact 추적
- 핵심 실패: quality rule blind spot·PII leak·retention violation

### [P4-1] quality dimensions·test strategy

- 이해할 것: quality dimensions·test strategy을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: rule result·quarantine·provenance·catalog 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 오염 차단과 downstream impact 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: quality rule blind spot·PII leak·retention violation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P4-2] quarantine·reconciliation

- 이해할 것: quarantine·reconciliation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: rule result·quarantine·provenance·catalog 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 오염 차단과 downstream impact 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: quality rule blind spot·PII leak·retention violation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P4-3] lineage·code/input/output version

- 이해할 것: lineage·code/input/output version을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: rule result·quarantine·provenance·catalog 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 오염 차단과 downstream impact 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: quality rule blind spot·PII leak·retention violation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P4-4] ownership·catalog·access·retention

- 이해할 것: ownership·catalog·access·retention을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: rule result·quarantine·provenance·catalog 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 오염 차단과 downstream impact 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: quality rule blind spot·PII leak·retention violation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P4 단계 결과물

- 감사 가능한 data product 구성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## P5. Orchestration·Observability·Cost

- 관찰 축: DAG·retry·freshness·volume·skew·cost
- 통합 실습: slow/stuck/expensive run 진단
- 핵심 실패: retry storm·silent stale data·cost runaway

### [P5-1] task DAG·dependency·parameter

- 이해할 것: task DAG·dependency·parameter을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: DAG·retry·freshness·volume·skew·cost 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: slow/stuck/expensive run 진단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·silent stale data·cost runaway 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P5-2] retry·timeout·backfill orchestration

- 이해할 것: retry·timeout·backfill orchestration을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: DAG·retry·freshness·volume·skew·cost 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: slow/stuck/expensive run 진단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·silent stale data·cost runaway 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P5-3] freshness·volume·quality observability

- 이해할 것: freshness·volume·quality observability을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: DAG·retry·freshness·volume·skew·cost 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: slow/stuck/expensive run 진단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·silent stale data·cost runaway 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P5-4] performance·skew·capacity·cost

- 이해할 것: performance·skew·capacity·cost을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: DAG·retry·freshness·volume·skew·cost 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: slow/stuck/expensive run 진단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: retry storm·silent stale data·cost runaway 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P5 단계 결과물

- SLA와 비용을 함께 운영.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## P6. Lakehouse와 serving

- 관찰 축: Delta log·medallion·batch/stream·serving contract
- 통합 실습: Databricks flow와 local model 비교
- 핵심 실패: concurrent write·vacuum·consumer break

### [P6-1] Delta transaction log·time travel

- 이해할 것: Delta transaction log·time travel을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Delta log·medallion·batch/stream·serving contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Databricks flow와 local model 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: concurrent write·vacuum·consumer break 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P6-2] bronze·silver·gold boundary

- 이해할 것: bronze·silver·gold boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Delta log·medallion·batch/stream·serving contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Databricks flow와 local model 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: concurrent write·vacuum·consumer break 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P6-3] batch·stream convergence

- 이해할 것: batch·stream convergence을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Delta log·medallion·batch/stream·serving contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Databricks flow와 local model 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: concurrent write·vacuum·consumer break 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [P6-4] serving freshness·RAG index lifecycle

- 이해할 것: serving freshness·RAG index lifecycle을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Delta log·medallion·batch/stream·serving contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Databricks flow와 local model 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: concurrent write·vacuum·consumer break 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### P6 단계 결과물

- 현재 실무 pipeline을 원리로 설명·개선.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
