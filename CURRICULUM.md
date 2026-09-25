# Rust Systems Programming 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Ownership와 data modeling 단계에서 memory ownership을 type으로 표현할 수 있는가?
- Trait와 abstraction 단계에서 zero-cost abstraction의 경계 이해할 수 있는가?
- Error와 shared memory 단계에서 복구 가능한 API와 공유 상태 설계할 수 있는가?
- Concurrency와 async 단계에서 type-safe concurrent task runner 구성할 수 있는가?
- System programming boundary 단계에서 OS 경계를 안전 abstraction으로 감쌈할 수 있는가?
- Quality·Performance·Delivery 단계에서 재현 가능한 cross-platform CLI release할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **R1** | Ownership와 data modeling | 5 | memory ownership을 type으로 표현 |
| **R2** | Trait와 abstraction | 5 | zero-cost abstraction의 경계 이해 |
| **R3** | Error와 shared memory | 5 | 복구 가능한 API와 공유 상태 설계 |
| **R4** | Concurrency와 async | 5 | type-safe concurrent task runner 구성 |
| **R5** | System programming boundary | 5 | OS 경계를 안전 abstraction으로 감쌈 |
| **R6** | Quality·Performance·Delivery | 5 | 재현 가능한 cross-platform CLI release |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **R1-1** | ownership·move·Copy | ownership·move·Copy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **R1-2** | borrow·mutable aliasing | borrow·mutable aliasing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-1 |
| **R1-3** | slice·lifetime elision | slice·lifetime elision의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-2 |
| **R1-4** | struct·enum·pattern·Option | struct·enum·pattern·Option의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-3 |
| **R1-5** | Drop·RAII·resource ownership | Drop·RAII·resource ownership의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-4 |
| **R2-1** | trait·generic·monomorphization | trait·generic·monomorphization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-5 |
| **R2-2** | associated type·generic parameter | associated type·generic parameter의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-1 |
| **R2-3** | static·dynamic dispatch·object safety | static·dynamic dispatch·object safety의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-2 |
| **R2-4** | closure·Fn traits·iterator | closure·Fn traits·iterator의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-3 |
| **R2-5** | coherence·newtype·API design | coherence·newtype·API design의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-4 |
| **R3-1** | Result·?·custom error | Result·?·custom error의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-5 |
| **R3-2** | error context·source·boundary | error context·source·boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-1 |
| **R3-3** | Box·smart pointer·DST | Box·smart pointer·DST의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-2 |
| **R3-4** | Rc·Arc·Weak·cycle | Rc·Arc·Weak·cycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-3 |
| **R3-5** | Cell·RefCell·Mutex interior mutability | Cell·RefCell·Mutex interior mutability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-4 |
| **R4-1** | thread·Send·Sync·scope | thread·Send·Sync·scope의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-5 |
| **R4-2** | channel·ownership transfer | channel·ownership transfer의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-1 |
| **R4-3** | Mutex·RwLock·atomic ordering | Mutex·RwLock·atomic ordering의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-2 |
| **R4-4** | Future·poll·wake·Pin | Future·poll·wake·Pin의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-3 |
| **R4-5** | async runtime·select·cancellation·backpressure | async runtime·select·cancellation·backpressure의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-4 |
| **R5-1** | file·buffer·partial I/O | file·buffer·partial I/O의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-5 |
| **R5-2** | TCP·protocol framing·timeout | TCP·protocol framing·timeout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-1 |
| **R5-3** | process·signal·exit status | process·signal·exit status의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-2 |
| **R5-4** | serialization·zero-copy boundary | serialization·zero-copy boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-3 |
| **R5-5** | unsafe·FFI·raw pointer·safety invariant | unsafe·FFI·raw pointer·safety invariant의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-4 |
| **R6-1** | unit·integration·doc test | unit·integration·doc test의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-5 |
| **R6-2** | property test·fuzzing | property test·fuzzing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-1 |
| **R6-3** | benchmark·profiling·allocation | benchmark·profiling·allocation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-2 |
| **R6-4** | workspace·feature·cross compilation | workspace·feature·cross compilation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-3 |
| **R6-5** | clippy·audit·release·observability | clippy·audit·release·observability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-4 |

## R1. Ownership와 data modeling

- 관찰 축: move·borrow·lifetime·drop·enum
- 통합 실습: compiler diagnostic를 예측하고 수정
- 핵심 실패: dangling·aliasing·partial move·drop order

### [R1-1] ownership·move·Copy

- 이해할 것: ownership·move·Copy을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: move·borrow·lifetime·drop·enum 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic를 예측하고 수정에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dangling·aliasing·partial move·drop order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R1-2] borrow·mutable aliasing

- 이해할 것: borrow·mutable aliasing을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: move·borrow·lifetime·drop·enum 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic를 예측하고 수정에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dangling·aliasing·partial move·drop order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R1-3] slice·lifetime elision

- 이해할 것: slice·lifetime elision을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: move·borrow·lifetime·drop·enum 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic를 예측하고 수정에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dangling·aliasing·partial move·drop order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R1-4] struct·enum·pattern·Option

- 이해할 것: struct·enum·pattern·Option을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: move·borrow·lifetime·drop·enum 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic를 예측하고 수정에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dangling·aliasing·partial move·drop order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R1-5] Drop·RAII·resource ownership

- 이해할 것: Drop·RAII·resource ownership을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: move·borrow·lifetime·drop·enum 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic를 예측하고 수정에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: dangling·aliasing·partial move·drop order 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R1 단계 결과물

- memory ownership을 type으로 표현.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## R2. Trait와 abstraction

- 관찰 축: generic·trait·associated type·dispatch·coherence
- 통합 실습: generic API와 trait object 비교
- 핵심 실패: orphan rule·object safety·overconstraint

### [R2-1] trait·generic·monomorphization

- 이해할 것: trait·generic·monomorphization을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: generic·trait·associated type·dispatch·coherence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: generic API와 trait object 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: orphan rule·object safety·overconstraint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R2-2] associated type·generic parameter

- 이해할 것: associated type·generic parameter을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: generic·trait·associated type·dispatch·coherence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: generic API와 trait object 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: orphan rule·object safety·overconstraint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R2-3] static·dynamic dispatch·object safety

- 이해할 것: static·dynamic dispatch·object safety을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: generic·trait·associated type·dispatch·coherence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: generic API와 trait object 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: orphan rule·object safety·overconstraint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R2-4] closure·Fn traits·iterator

- 이해할 것: closure·Fn traits·iterator을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: generic·trait·associated type·dispatch·coherence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: generic API와 trait object 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: orphan rule·object safety·overconstraint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R2-5] coherence·newtype·API design

- 이해할 것: coherence·newtype·API design을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: generic·trait·associated type·dispatch·coherence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: generic API와 trait object 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: orphan rule·object safety·overconstraint 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R2 단계 결과물

- zero-cost abstraction의 경계 이해.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## R3. Error와 shared memory

- 관찰 축: Result·error source·Box/Rc/Arc/Weak·interior mutability
- 통합 실습: ownership graph과 error chain 관찰
- 핵심 실패: reference cycle·RefCell panic·opaque error loss

### [R3-1] Result·?·custom error

- 이해할 것: Result·?·custom error을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Result·error source·Box/Rc/Arc/Weak·interior mutability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: ownership graph과 error chain 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reference cycle·RefCell panic·opaque error loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R3-2] error context·source·boundary

- 이해할 것: error context·source·boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Result·error source·Box/Rc/Arc/Weak·interior mutability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: ownership graph과 error chain 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reference cycle·RefCell panic·opaque error loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R3-3] Box·smart pointer·DST

- 이해할 것: Box·smart pointer·DST을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Result·error source·Box/Rc/Arc/Weak·interior mutability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: ownership graph과 error chain 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reference cycle·RefCell panic·opaque error loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R3-4] Rc·Arc·Weak·cycle

- 이해할 것: Rc·Arc·Weak·cycle을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Result·error source·Box/Rc/Arc/Weak·interior mutability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: ownership graph과 error chain 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reference cycle·RefCell panic·opaque error loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R3-5] Cell·RefCell·Mutex interior mutability

- 이해할 것: Cell·RefCell·Mutex interior mutability을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Result·error source·Box/Rc/Arc/Weak·interior mutability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: ownership graph과 error chain 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reference cycle·RefCell panic·opaque error loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R3 단계 결과물

- 복구 가능한 API와 공유 상태 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## R4. Concurrency와 async

- 관찰 축: Send/Sync·thread·channel·atomic·Future·runtime
- 통합 실습: worker pool·cancel·timeout 구현
- 핵심 실패: deadlock·blocking runtime·lost cancellation

### [R4-1] thread·Send·Sync·scope

- 이해할 것: thread·Send·Sync·scope을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Send/Sync·thread·channel·atomic·Future·runtime 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: worker pool·cancel·timeout 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: deadlock·blocking runtime·lost cancellation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R4-2] channel·ownership transfer

- 이해할 것: channel·ownership transfer을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Send/Sync·thread·channel·atomic·Future·runtime 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: worker pool·cancel·timeout 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: deadlock·blocking runtime·lost cancellation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R4-3] Mutex·RwLock·atomic ordering

- 이해할 것: Mutex·RwLock·atomic ordering을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Send/Sync·thread·channel·atomic·Future·runtime 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: worker pool·cancel·timeout 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: deadlock·blocking runtime·lost cancellation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R4-4] Future·poll·wake·Pin

- 이해할 것: Future·poll·wake·Pin을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Send/Sync·thread·channel·atomic·Future·runtime 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: worker pool·cancel·timeout 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: deadlock·blocking runtime·lost cancellation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R4-5] async runtime·select·cancellation·backpressure

- 이해할 것: async runtime·select·cancellation·backpressure을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Send/Sync·thread·channel·atomic·Future·runtime 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: worker pool·cancel·timeout 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: deadlock·blocking runtime·lost cancellation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R4 단계 결과물

- type-safe concurrent task runner 구성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## R5. System programming boundary

- 관찰 축: file/socket·fd·process·signal·serialization·unsafe/FFI
- 통합 실습: partial I/O와 child lifecycle 구현
- 핵심 실패: short write·zombie·signal race·UB contract

### [R5-1] file·buffer·partial I/O

- 이해할 것: file·buffer·partial I/O을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: file/socket·fd·process·signal·serialization·unsafe/FFI 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: partial I/O와 child lifecycle 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: short write·zombie·signal race·UB contract 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R5-2] TCP·protocol framing·timeout

- 이해할 것: TCP·protocol framing·timeout을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: file/socket·fd·process·signal·serialization·unsafe/FFI 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: partial I/O와 child lifecycle 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: short write·zombie·signal race·UB contract 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R5-3] process·signal·exit status

- 이해할 것: process·signal·exit status을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: file/socket·fd·process·signal·serialization·unsafe/FFI 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: partial I/O와 child lifecycle 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: short write·zombie·signal race·UB contract 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R5-4] serialization·zero-copy boundary

- 이해할 것: serialization·zero-copy boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: file/socket·fd·process·signal·serialization·unsafe/FFI 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: partial I/O와 child lifecycle 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: short write·zombie·signal race·UB contract 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R5-5] unsafe·FFI·raw pointer·safety invariant

- 이해할 것: unsafe·FFI·raw pointer·safety invariant을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: file/socket·fd·process·signal·serialization·unsafe/FFI 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: partial I/O와 child lifecycle 구현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: short write·zombie·signal race·UB contract 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R5 단계 결과물

- OS 경계를 안전 abstraction으로 감쌈.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## R6. Quality·Performance·Delivery

- 관찰 축: test·property·fuzz·benchmark·profile·workspace·supply chain
- 통합 실습: failure corpus와 profile 기반 최적화
- 핵심 실패: flaky concurrency·misleading benchmark·dependency risk

### [R6-1] unit·integration·doc test

- 이해할 것: unit·integration·doc test을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test·property·fuzz·benchmark·profile·workspace·supply chain 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: failure corpus와 profile 기반 최적화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: flaky concurrency·misleading benchmark·dependency risk 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R6-2] property test·fuzzing

- 이해할 것: property test·fuzzing을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test·property·fuzz·benchmark·profile·workspace·supply chain 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: failure corpus와 profile 기반 최적화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: flaky concurrency·misleading benchmark·dependency risk 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R6-3] benchmark·profiling·allocation

- 이해할 것: benchmark·profiling·allocation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test·property·fuzz·benchmark·profile·workspace·supply chain 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: failure corpus와 profile 기반 최적화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: flaky concurrency·misleading benchmark·dependency risk 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R6-4] workspace·feature·cross compilation

- 이해할 것: workspace·feature·cross compilation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test·property·fuzz·benchmark·profile·workspace·supply chain 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: failure corpus와 profile 기반 최적화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: flaky concurrency·misleading benchmark·dependency risk 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [R6-5] clippy·audit·release·observability

- 이해할 것: clippy·audit·release·observability을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test·property·fuzz·benchmark·profile·workspace·supply chain 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: failure corpus와 profile 기반 최적화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: flaky concurrency·misleading benchmark·dependency risk 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### R6 단계 결과물

- 재현 가능한 cross-platform CLI release.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
