# Rust Systems Programming 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1-1** | ownership·move·Copy | ownership·move·Copy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **R1-2** | borrow·mutable aliasing | borrow·mutable aliasing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-1 | 대기 | - |
| **R1-3** | slice·lifetime elision | slice·lifetime elision의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-2 | 대기 | - |
| **R1-4** | struct·enum·pattern·Option | struct·enum·pattern·Option의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-3 | 대기 | - |
| **R1-5** | Drop·RAII·resource ownership | Drop·RAII·resource ownership의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-4 | 대기 | - |
| **R2-1** | trait·generic·monomorphization | trait·generic·monomorphization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R1-5 | 대기 | - |
| **R2-2** | associated type·generic parameter | associated type·generic parameter의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-1 | 대기 | - |
| **R2-3** | static·dynamic dispatch·object safety | static·dynamic dispatch·object safety의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-2 | 대기 | - |
| **R2-4** | closure·Fn traits·iterator | closure·Fn traits·iterator의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-3 | 대기 | - |
| **R2-5** | coherence·newtype·API design | coherence·newtype·API design의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-4 | 대기 | - |
| **R3-1** | Result·?·custom error | Result·?·custom error의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R2-5 | 대기 | - |
| **R3-2** | error context·source·boundary | error context·source·boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-1 | 대기 | - |
| **R3-3** | Box·smart pointer·DST | Box·smart pointer·DST의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-2 | 대기 | - |
| **R3-4** | Rc·Arc·Weak·cycle | Rc·Arc·Weak·cycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-3 | 대기 | - |
| **R3-5** | Cell·RefCell·Mutex interior mutability | Cell·RefCell·Mutex interior mutability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-4 | 대기 | - |
| **R4-1** | thread·Send·Sync·scope | thread·Send·Sync·scope의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R3-5 | 대기 | - |
| **R4-2** | channel·ownership transfer | channel·ownership transfer의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-1 | 대기 | - |
| **R4-3** | Mutex·RwLock·atomic ordering | Mutex·RwLock·atomic ordering의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-2 | 대기 | - |
| **R4-4** | Future·poll·wake·Pin | Future·poll·wake·Pin의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-3 | 대기 | - |
| **R4-5** | async runtime·select·cancellation·backpressure | async runtime·select·cancellation·backpressure의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-4 | 대기 | - |
| **R5-1** | file·buffer·partial I/O | file·buffer·partial I/O의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R4-5 | 대기 | - |
| **R5-2** | TCP·protocol framing·timeout | TCP·protocol framing·timeout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-1 | 대기 | - |
| **R5-3** | process·signal·exit status | process·signal·exit status의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-2 | 대기 | - |
| **R5-4** | serialization·zero-copy boundary | serialization·zero-copy boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-3 | 대기 | - |
| **R5-5** | unsafe·FFI·raw pointer·safety invariant | unsafe·FFI·raw pointer·safety invariant의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-4 | 대기 | - |
| **R6-1** | unit·integration·doc test | unit·integration·doc test의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R5-5 | 대기 | - |
| **R6-2** | property test·fuzzing | property test·fuzzing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-1 | 대기 | - |
| **R6-3** | benchmark·profiling·allocation | benchmark·profiling·allocation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-2 | 대기 | - |
| **R6-4** | workspace·feature·cross compilation | workspace·feature·cross compilation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-3 | 대기 | - |
| **R6-5** | clippy·audit·release·observability | clippy·audit·release·observability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | R6-4 | 대기 | - |

## 세부 기록

### R1-1. ownership·move·Copy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R1-2. borrow·mutable aliasing

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R1-3. slice·lifetime elision

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R1-4. struct·enum·pattern·Option

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R1-5. Drop·RAII·resource ownership

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R2-1. trait·generic·monomorphization

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R2-2. associated type·generic parameter

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R2-3. static·dynamic dispatch·object safety

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R2-4. closure·Fn traits·iterator

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R2-5. coherence·newtype·API design

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R3-1. Result·?·custom error

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R3-2. error context·source·boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R3-3. Box·smart pointer·DST

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R3-4. Rc·Arc·Weak·cycle

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R3-5. Cell·RefCell·Mutex interior mutability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R4-1. thread·Send·Sync·scope

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R4-2. channel·ownership transfer

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R4-3. Mutex·RwLock·atomic ordering

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R4-4. Future·poll·wake·Pin

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R4-5. async runtime·select·cancellation·backpressure

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R5-1. file·buffer·partial I/O

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R5-2. TCP·protocol framing·timeout

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R5-3. process·signal·exit status

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R5-4. serialization·zero-copy boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R5-5. unsafe·FFI·raw pointer·safety invariant

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R6-1. unit·integration·doc test

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R6-2. property test·fuzzing

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R6-3. benchmark·profiling·allocation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R6-4. workspace·feature·cross compilation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### R6-5. clippy·audit·release·observability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
