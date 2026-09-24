# Reliable Data Pipelines 커리큘럼

## 목적

증분 처리·재실행·정합성·lineage를 설계한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Python·SQL·분산 기초
- 최종 실습: 문서→embedding→serving pipeline 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **P1** | 계약·모델 | schema·key·event time | 중복·late data |
| **P2** | 증분 처리 | checkpoint·watermark·partition | full/incremental 비교 |
| **P3** | 재실행 | run id·version·dedup | 부분 실패·중복 |
| **P4** | 품질·lineage | rule·graph·quarantine | 오염 차단·역추적 |
| **P5** | 운영·비용 | latency·throughput·cost | skew·비용 급증 |
| **P6** | Lakehouse·serving | Delta log·catalog·freshness | bronze/silver/gold |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **P1-1** | grain·key | grain·key의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **P1-2** | schema evolution | schema evolution의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-1 |
| **P1-3** | event vs processing time | event vs processing time의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-2 |
| **P2-1** | snapshot·CDC | snapshot·CDC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P1-3 |
| **P2-2** | watermark | watermark의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-1 |
| **P2-3** | partition·file layout | partition·file layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-2 |
| **P3-1** | idempotent merge | idempotent merge의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P2-3 |
| **P3-2** | restart·backfill | restart·backfill의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-1 |
| **P3-3** | concurrent run | concurrent run의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-2 |
| **P4-1** | data quality | data quality의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P3-3 |
| **P4-2** | lineage·provenance | lineage·provenance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-1 |
| **P4-3** | reconciliation | reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-2 |
| **P5-1** | orchestration | orchestration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P4-3 |
| **P5-2** | SLA·observability | SLA·observability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-1 |
| **P5-3** | performance·cost | performance·cost의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-2 |
| **P6-1** | Delta transaction | Delta transaction의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P5-3 |
| **P6-2** | governance·retention | governance·retention의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P6-1 |
| **P6-3** | batch·stream·serving | batch·stream·serving의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | P6-2 |

## 상세 커리큘럼

### [P1-1] grain·key

- 목표: grain·key의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: schema·key·event time를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·late data 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P1-2] schema evolution

- 목표: schema evolution의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: schema·key·event time를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·late data 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P1-3] event vs processing time

- 목표: event vs processing time의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: schema·key·event time를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·late data 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P2-1] snapshot·CDC

- 목표: snapshot·CDC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: checkpoint·watermark·partition를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: full/incremental 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P2-2] watermark

- 목표: watermark의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: checkpoint·watermark·partition를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: full/incremental 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P2-3] partition·file layout

- 목표: partition·file layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: checkpoint·watermark·partition를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: full/incremental 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P3-1] idempotent merge

- 목표: idempotent merge의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: run id·version·dedup를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부분 실패·중복 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P3-2] restart·backfill

- 목표: restart·backfill의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: run id·version·dedup를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부분 실패·중복 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P3-3] concurrent run

- 목표: concurrent run의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: run id·version·dedup를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부분 실패·중복 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P4-1] data quality

- 목표: data quality의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: rule·graph·quarantine를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 오염 차단·역추적 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P4-2] lineage·provenance

- 목표: lineage·provenance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: rule·graph·quarantine를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 오염 차단·역추적 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P4-3] reconciliation

- 목표: reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: rule·graph·quarantine를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 오염 차단·역추적 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P5-1] orchestration

- 목표: orchestration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: latency·throughput·cost를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: skew·비용 급증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P5-2] SLA·observability

- 목표: SLA·observability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: latency·throughput·cost를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: skew·비용 급증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P5-3] performance·cost

- 목표: performance·cost의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: latency·throughput·cost를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: skew·비용 급증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P6-1] Delta transaction

- 목표: Delta transaction의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Delta log·catalog·freshness를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: bronze/silver/gold 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P6-2] governance·retention

- 목표: governance·retention의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Delta log·catalog·freshness를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: bronze/silver/gold 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [P6-3] batch·stream·serving

- 목표: batch·stream·serving의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Delta log·catalog·freshness를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: bronze/silver/gold 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
