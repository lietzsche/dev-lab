# Rust Systems Programming 커리큘럼

## 목적

소유권·메모리·동시성으로 안전한 시스템 도구를 개발한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: 핵심 로드맵 후
- 최종 실습: agent task runner CLI
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **R1** | 소유권 | move·borrow·lifetime | compiler 오류 예측 |
| **R2** | 추상화·오류 | generic·dispatch·error | typed API 구현 |
| **R3** | 메모리 | layout·allocation·refcount | 공유 소유 반례 |
| **R4** | 동시성·async | thread·channel·task | worker·cancel |
| **R5** | System I/O | syscall·fd·process | file·network·child |
| **R6** | 품질·배포 | test·benchmark·binary | 성능·build 검증 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **R1-1** | ownership·move | ownership·move의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **R1-2** | borrow·slice | borrow·slice의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R1-1 |
| **R1-3** | enum·pattern | enum·pattern의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R1-2 |
| **R2-1** | trait·dispatch | trait·dispatch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R1-3 |
| **R2-2** | Option·Result | Option·Result의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R2-1 |
| **R2-3** | iterator·closure | iterator·closure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R2-2 |
| **R3-1** | stack·heap | stack·heap의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R2-3 |
| **R3-2** | Box·Rc·Arc | Box·Rc·Arc의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R3-1 |
| **R3-3** | Cell·RefCell | Cell·RefCell의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R3-2 |
| **R4-1** | Send·Sync | Send·Sync의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R3-3 |
| **R4-2** | mutex·channel | mutex·channel의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R4-1 |
| **R4-3** | Future runtime | Future runtime의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R4-2 |
| **R5-1** | buffered I/O | buffered I/O의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R4-3 |
| **R5-2** | process·signal | process·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R5-1 |
| **R5-3** | FFI·unsafe | FFI·unsafe의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R5-2 |
| **R6-1** | property·fuzz | property·fuzz의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R5-3 |
| **R6-2** | profiling | profiling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R6-1 |
| **R6-3** | release·supply chain | release·supply chain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | R6-2 |

## 상세 커리큘럼

### [R1-1] ownership·move

- 목표: ownership·move의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: move·borrow·lifetime를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compiler 오류 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R1-2] borrow·slice

- 목표: borrow·slice의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: move·borrow·lifetime를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compiler 오류 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R1-3] enum·pattern

- 목표: enum·pattern의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: move·borrow·lifetime를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compiler 오류 예측 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R2-1] trait·dispatch

- 목표: trait·dispatch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: generic·dispatch·error를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: typed API 구현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R2-2] Option·Result

- 목표: Option·Result의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: generic·dispatch·error를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: typed API 구현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R2-3] iterator·closure

- 목표: iterator·closure의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: generic·dispatch·error를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: typed API 구현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R3-1] stack·heap

- 목표: stack·heap의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layout·allocation·refcount를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 공유 소유 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R3-2] Box·Rc·Arc

- 목표: Box·Rc·Arc의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layout·allocation·refcount를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 공유 소유 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R3-3] Cell·RefCell

- 목표: Cell·RefCell의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layout·allocation·refcount를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 공유 소유 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R4-1] Send·Sync

- 목표: Send·Sync의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread·channel·task를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: worker·cancel 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R4-2] mutex·channel

- 목표: mutex·channel의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread·channel·task를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: worker·cancel 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R4-3] Future runtime

- 목표: Future runtime의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread·channel·task를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: worker·cancel 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R5-1] buffered I/O

- 목표: buffered I/O의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: syscall·fd·process를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: file·network·child 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R5-2] process·signal

- 목표: process·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: syscall·fd·process를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: file·network·child 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R5-3] FFI·unsafe

- 목표: FFI·unsafe의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: syscall·fd·process를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: file·network·child 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R6-1] property·fuzz

- 목표: property·fuzz의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test·benchmark·binary를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 성능·build 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R6-2] profiling

- 목표: profiling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test·benchmark·binary를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 성능·build 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [R6-3] release·supply chain

- 목표: release·supply chain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test·benchmark·binary를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 성능·build 검증 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
