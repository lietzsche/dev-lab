# JVM & Spring Internals 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **J1-1** | bytecode·operand stack·dispatch | bytecode·operand stack·dispatch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **J1-2** | class loading·linking·initialization | class loading·linking·initialization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-1 | 대기 | - |
| **J1-3** | class loader identity·module | class loader identity·module의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-2 | 대기 | - |
| **J1-4** | reflection·annotation·method handle | reflection·annotation·method handle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-3 | 대기 | - |
| **J1-5** | JIT·warmup·deoptimization 입문 | JIT·warmup·deoptimization 입문의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-4 | 대기 | - |
| **J2-1** | heap·stack·object layout | heap·stack·object layout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-5 | 대기 | - |
| **J2-2** | allocation·TLAB·escape analysis | allocation·TLAB·escape analysis의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-1 | 대기 | - |
| **J2-3** | GC root·reachability·reference type | GC root·reachability·reference type의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-2 | 대기 | - |
| **J2-4** | collector·pause·throughput tradeoff | collector·pause·throughput tradeoff의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-3 | 대기 | - |
| **J2-5** | JFR·heap dump·profiling·benchmark | JFR·heap dump·profiling·benchmark의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-4 | 대기 | - |
| **J3-1** | Java Memory Model·visibility | Java Memory Model·visibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-5 | 대기 | - |
| **J3-2** | synchronized·lock·condition | synchronized·lock·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-1 | 대기 | - |
| **J3-3** | atomic·CAS·concurrent collection | atomic·CAS·concurrent collection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-2 | 대기 | - |
| **J3-4** | executor·queue·backpressure | executor·queue·backpressure의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-3 | 대기 | - |
| **J3-5** | virtual thread·structured concurrency·pinning | virtual thread·structured concurrency·pinning의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-4 | 대기 | - |
| **J4-1** | bean definition·lifecycle·scope | bean definition·lifecycle·scope의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-5 | 대기 | - |
| **J4-2** | dependency injection·cycle·lazy | dependency injection·cycle·lazy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-1 | 대기 | - |
| **J4-3** | proxy·AOP·self invocation | proxy·AOP·self invocation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-2 | 대기 | - |
| **J4-4** | configuration·auto-configuration·condition | configuration·auto-configuration·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-3 | 대기 | - |
| **J4-5** | event·validation·cache boundary | event·validation·cache boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-4 | 대기 | - |
| **J5-1** | transaction proxy·propagation | transaction proxy·propagation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-5 | 대기 | - |
| **J5-2** | isolation·locking·retry | isolation·locking·retry의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-1 | 대기 | - |
| **J5-3** | JPA identity·flush·batch·N+1 | JPA identity·flush·batch·N+1의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-2 | 대기 | - |
| **J5-4** | MVC lifecycle·exception·serialization | MVC lifecycle·exception·serialization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-3 | 대기 | - |
| **J5-5** | Security filter·authorization·async context | Security filter·authorization·async context의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-4 | 대기 | - |
| **J6-1** | unit·slice·integration contract | unit·slice·integration contract의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-5 | 대기 | - |
| **J6-2** | Testcontainers·migration·external dependency | Testcontainers·migration·external dependency의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-1 | 대기 | - |
| **J6-3** | configuration·secret·profile boundary | configuration·secret·profile boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-2 | 대기 | - |
| **J6-4** | Micrometer·OpenTelemetry·structured log | Micrometer·OpenTelemetry·structured log의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-3 | 대기 | - |
| **J6-5** | container·Kubernetes·graceful shutdown·incident | container·Kubernetes·graceful shutdown·incident의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-4 | 대기 | - |

## 세부 기록

### J1-1. bytecode·operand stack·dispatch

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J1-2. class loading·linking·initialization

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J1-3. class loader identity·module

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J1-4. reflection·annotation·method handle

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J1-5. JIT·warmup·deoptimization 입문

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J2-1. heap·stack·object layout

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J2-2. allocation·TLAB·escape analysis

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J2-3. GC root·reachability·reference type

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J2-4. collector·pause·throughput tradeoff

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J2-5. JFR·heap dump·profiling·benchmark

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J3-1. Java Memory Model·visibility

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J3-2. synchronized·lock·condition

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J3-3. atomic·CAS·concurrent collection

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J3-4. executor·queue·backpressure

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J3-5. virtual thread·structured concurrency·pinning

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J4-1. bean definition·lifecycle·scope

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J4-2. dependency injection·cycle·lazy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J4-3. proxy·AOP·self invocation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J4-4. configuration·auto-configuration·condition

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J4-5. event·validation·cache boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J5-1. transaction proxy·propagation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J5-2. isolation·locking·retry

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J5-3. JPA identity·flush·batch·N+1

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J5-4. MVC lifecycle·exception·serialization

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J5-5. Security filter·authorization·async context

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J6-1. unit·slice·integration contract

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J6-2. Testcontainers·migration·external dependency

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J6-3. configuration·secret·profile boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J6-4. Micrometer·OpenTelemetry·structured log

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### J6-5. container·Kubernetes·graceful shutdown·incident

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
