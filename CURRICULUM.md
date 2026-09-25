# JVM & Spring Internals 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- JVM execution과 type runtime 단계에서 source에서 runtime call까지 설명할 수 있는가?
- Memory·GC·Performance 단계에서 증거 기반 JVM 성능 진단할 수 있는가?
- Concurrency 단계에서 workload에 맞는 concurrency model 선택할 수 있는가?
- Spring container와 cross-cutting 단계에서 framework magic을 object graph로 환원할 수 있는가?
- Data·Web·Security boundary 단계에서 request에서 DB commit까지 경계 설계할 수 있는가?
- Test·Production operation 단계에서 Spring service 운영·복구 runbook 작성할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **J1** | JVM execution과 type runtime | 5 | source에서 runtime call까지 설명 |
| **J2** | Memory·GC·Performance | 5 | 증거 기반 JVM 성능 진단 |
| **J3** | Concurrency | 5 | workload에 맞는 concurrency model 선택 |
| **J4** | Spring container와 cross-cutting | 5 | framework magic을 object graph로 환원 |
| **J5** | Data·Web·Security boundary | 5 | request에서 DB commit까지 경계 설계 |
| **J6** | Test·Production operation | 5 | Spring service 운영·복구 runbook 작성 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **J1-1** | bytecode·operand stack·dispatch | bytecode·operand stack·dispatch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **J1-2** | class loading·linking·initialization | class loading·linking·initialization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-1 |
| **J1-3** | class loader identity·module | class loader identity·module의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-2 |
| **J1-4** | reflection·annotation·method handle | reflection·annotation·method handle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-3 |
| **J1-5** | JIT·warmup·deoptimization 입문 | JIT·warmup·deoptimization 입문의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-4 |
| **J2-1** | heap·stack·object layout | heap·stack·object layout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J1-5 |
| **J2-2** | allocation·TLAB·escape analysis | allocation·TLAB·escape analysis의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-1 |
| **J2-3** | GC root·reachability·reference type | GC root·reachability·reference type의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-2 |
| **J2-4** | collector·pause·throughput tradeoff | collector·pause·throughput tradeoff의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-3 |
| **J2-5** | JFR·heap dump·profiling·benchmark | JFR·heap dump·profiling·benchmark의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-4 |
| **J3-1** | Java Memory Model·visibility | Java Memory Model·visibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J2-5 |
| **J3-2** | synchronized·lock·condition | synchronized·lock·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-1 |
| **J3-3** | atomic·CAS·concurrent collection | atomic·CAS·concurrent collection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-2 |
| **J3-4** | executor·queue·backpressure | executor·queue·backpressure의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-3 |
| **J3-5** | virtual thread·structured concurrency·pinning | virtual thread·structured concurrency·pinning의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-4 |
| **J4-1** | bean definition·lifecycle·scope | bean definition·lifecycle·scope의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J3-5 |
| **J4-2** | dependency injection·cycle·lazy | dependency injection·cycle·lazy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-1 |
| **J4-3** | proxy·AOP·self invocation | proxy·AOP·self invocation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-2 |
| **J4-4** | configuration·auto-configuration·condition | configuration·auto-configuration·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-3 |
| **J4-5** | event·validation·cache boundary | event·validation·cache boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-4 |
| **J5-1** | transaction proxy·propagation | transaction proxy·propagation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J4-5 |
| **J5-2** | isolation·locking·retry | isolation·locking·retry의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-1 |
| **J5-3** | JPA identity·flush·batch·N+1 | JPA identity·flush·batch·N+1의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-2 |
| **J5-4** | MVC lifecycle·exception·serialization | MVC lifecycle·exception·serialization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-3 |
| **J5-5** | Security filter·authorization·async context | Security filter·authorization·async context의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-4 |
| **J6-1** | unit·slice·integration contract | unit·slice·integration contract의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J5-5 |
| **J6-2** | Testcontainers·migration·external dependency | Testcontainers·migration·external dependency의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-1 |
| **J6-3** | configuration·secret·profile boundary | configuration·secret·profile boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-2 |
| **J6-4** | Micrometer·OpenTelemetry·structured log | Micrometer·OpenTelemetry·structured log의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-3 |
| **J6-5** | container·Kubernetes·graceful shutdown·incident | container·Kubernetes·graceful shutdown·incident의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | J6-4 |

## J1. JVM execution과 type runtime

- 관찰 축: bytecode·class loader·linking·reflection·dispatch
- 통합 실습: compile/disassemble/load experiment
- 핵심 실패: class identity split·linkage error·reflection cache

### [J1-1] bytecode·operand stack·dispatch

- 이해할 것: bytecode·operand stack·dispatch을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bytecode·class loader·linking·reflection·dispatch 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compile/disassemble/load experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: class identity split·linkage error·reflection cache 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J1-2] class loading·linking·initialization

- 이해할 것: class loading·linking·initialization을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bytecode·class loader·linking·reflection·dispatch 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compile/disassemble/load experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: class identity split·linkage error·reflection cache 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J1-3] class loader identity·module

- 이해할 것: class loader identity·module을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bytecode·class loader·linking·reflection·dispatch 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compile/disassemble/load experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: class identity split·linkage error·reflection cache 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J1-4] reflection·annotation·method handle

- 이해할 것: reflection·annotation·method handle을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bytecode·class loader·linking·reflection·dispatch 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compile/disassemble/load experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: class identity split·linkage error·reflection cache 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J1-5] JIT·warmup·deoptimization 입문

- 이해할 것: JIT·warmup·deoptimization 입문을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bytecode·class loader·linking·reflection·dispatch 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compile/disassemble/load experiment에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: class identity split·linkage error·reflection cache 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J1 단계 결과물

- source에서 runtime call까지 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## J2. Memory·GC·Performance

- 관찰 축: object layout·allocation·escape·collector·JFR
- 통합 실습: allocation/GC/heap/thread dump 분석
- 핵심 실패: leak·promotion pressure·pause·benchmark 오류

### [J2-1] heap·stack·object layout

- 이해할 것: heap·stack·object layout을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object layout·allocation·escape·collector·JFR 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: allocation/GC/heap/thread dump 분석에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: leak·promotion pressure·pause·benchmark 오류 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J2-2] allocation·TLAB·escape analysis

- 이해할 것: allocation·TLAB·escape analysis을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object layout·allocation·escape·collector·JFR 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: allocation/GC/heap/thread dump 분석에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: leak·promotion pressure·pause·benchmark 오류 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J2-3] GC root·reachability·reference type

- 이해할 것: GC root·reachability·reference type을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object layout·allocation·escape·collector·JFR 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: allocation/GC/heap/thread dump 분석에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: leak·promotion pressure·pause·benchmark 오류 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J2-4] collector·pause·throughput tradeoff

- 이해할 것: collector·pause·throughput tradeoff을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object layout·allocation·escape·collector·JFR 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: allocation/GC/heap/thread dump 분석에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: leak·promotion pressure·pause·benchmark 오류 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J2-5] JFR·heap dump·profiling·benchmark

- 이해할 것: JFR·heap dump·profiling·benchmark을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object layout·allocation·escape·collector·JFR 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: allocation/GC/heap/thread dump 분석에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: leak·promotion pressure·pause·benchmark 오류 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J2 단계 결과물

- 증거 기반 JVM 성능 진단.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## J3. Concurrency

- 관찰 축: JMM·happens-before·lock·atomic·executor·virtual thread
- 통합 실습: race/deadlock/starvation/pinning 재현
- 핵심 실패: visibility bug·pool exhaustion·context loss

### [J3-1] Java Memory Model·visibility

- 이해할 것: Java Memory Model·visibility을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: JMM·happens-before·lock·atomic·executor·virtual thread 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race/deadlock/starvation/pinning 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: visibility bug·pool exhaustion·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J3-2] synchronized·lock·condition

- 이해할 것: synchronized·lock·condition을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: JMM·happens-before·lock·atomic·executor·virtual thread 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race/deadlock/starvation/pinning 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: visibility bug·pool exhaustion·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J3-3] atomic·CAS·concurrent collection

- 이해할 것: atomic·CAS·concurrent collection을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: JMM·happens-before·lock·atomic·executor·virtual thread 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race/deadlock/starvation/pinning 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: visibility bug·pool exhaustion·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J3-4] executor·queue·backpressure

- 이해할 것: executor·queue·backpressure을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: JMM·happens-before·lock·atomic·executor·virtual thread 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race/deadlock/starvation/pinning 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: visibility bug·pool exhaustion·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J3-5] virtual thread·structured concurrency·pinning

- 이해할 것: virtual thread·structured concurrency·pinning을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: JMM·happens-before·lock·atomic·executor·virtual thread 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race/deadlock/starvation/pinning 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: visibility bug·pool exhaustion·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J3 단계 결과물

- workload에 맞는 concurrency model 선택.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## J4. Spring container와 cross-cutting

- 관찰 축: bean graph·scope·lifecycle·proxy·condition
- 통합 실습: bean/proxy/transaction 실제 type 관찰
- 핵심 실패: cycle·self invocation·scope mismatch·condition surprise

### [J4-1] bean definition·lifecycle·scope

- 이해할 것: bean definition·lifecycle·scope을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bean graph·scope·lifecycle·proxy·condition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bean/proxy/transaction 실제 type 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: cycle·self invocation·scope mismatch·condition surprise 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J4-2] dependency injection·cycle·lazy

- 이해할 것: dependency injection·cycle·lazy을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bean graph·scope·lifecycle·proxy·condition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bean/proxy/transaction 실제 type 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: cycle·self invocation·scope mismatch·condition surprise 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J4-3] proxy·AOP·self invocation

- 이해할 것: proxy·AOP·self invocation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bean graph·scope·lifecycle·proxy·condition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bean/proxy/transaction 실제 type 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: cycle·self invocation·scope mismatch·condition surprise 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J4-4] configuration·auto-configuration·condition

- 이해할 것: configuration·auto-configuration·condition을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bean graph·scope·lifecycle·proxy·condition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bean/proxy/transaction 실제 type 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: cycle·self invocation·scope mismatch·condition surprise 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J4-5] event·validation·cache boundary

- 이해할 것: event·validation·cache boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bean graph·scope·lifecycle·proxy·condition 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bean/proxy/transaction 실제 type 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: cycle·self invocation·scope mismatch·condition surprise 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J4 단계 결과물

- framework magic을 object graph로 환원.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## J5. Data·Web·Security boundary

- 관찰 축: transaction·JPA context·MVC pipeline·filter·async context
- 통합 실습: isolation/auth/exception/async 반례
- 핵심 실패: lazy load·rollback mismatch·auth bypass·context loss

### [J5-1] transaction proxy·propagation

- 이해할 것: transaction proxy·propagation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: transaction·JPA context·MVC pipeline·filter·async context 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: isolation/auth/exception/async 반례에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: lazy load·rollback mismatch·auth bypass·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J5-2] isolation·locking·retry

- 이해할 것: isolation·locking·retry을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: transaction·JPA context·MVC pipeline·filter·async context 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: isolation/auth/exception/async 반례에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: lazy load·rollback mismatch·auth bypass·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J5-3] JPA identity·flush·batch·N+1

- 이해할 것: JPA identity·flush·batch·N+1을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: transaction·JPA context·MVC pipeline·filter·async context 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: isolation/auth/exception/async 반례에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: lazy load·rollback mismatch·auth bypass·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J5-4] MVC lifecycle·exception·serialization

- 이해할 것: MVC lifecycle·exception·serialization을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: transaction·JPA context·MVC pipeline·filter·async context 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: isolation/auth/exception/async 반례에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: lazy load·rollback mismatch·auth bypass·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J5-5] Security filter·authorization·async context

- 이해할 것: Security filter·authorization·async context을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: transaction·JPA context·MVC pipeline·filter·async context 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: isolation/auth/exception/async 반례에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: lazy load·rollback mismatch·auth bypass·context loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J5 단계 결과물

- request에서 DB commit까지 경계 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## J6. Test·Production operation

- 관찰 축: test slice·container·config·metric/trace·shutdown·K8s
- 통합 실습: 실 dependency·부하·배포 failure 검증
- 핵심 실패: context cache 착시·probe loop·graceful loss

### [J6-1] unit·slice·integration contract

- 이해할 것: unit·slice·integration contract을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test slice·container·config·metric/trace·shutdown·K8s 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실 dependency·부하·배포 failure 검증에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: context cache 착시·probe loop·graceful loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J6-2] Testcontainers·migration·external dependency

- 이해할 것: Testcontainers·migration·external dependency을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test slice·container·config·metric/trace·shutdown·K8s 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실 dependency·부하·배포 failure 검증에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: context cache 착시·probe loop·graceful loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J6-3] configuration·secret·profile boundary

- 이해할 것: configuration·secret·profile boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test slice·container·config·metric/trace·shutdown·K8s 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실 dependency·부하·배포 failure 검증에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: context cache 착시·probe loop·graceful loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J6-4] Micrometer·OpenTelemetry·structured log

- 이해할 것: Micrometer·OpenTelemetry·structured log을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test slice·container·config·metric/trace·shutdown·K8s 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실 dependency·부하·배포 failure 검증에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: context cache 착시·probe loop·graceful loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [J6-5] container·Kubernetes·graceful shutdown·incident

- 이해할 것: container·Kubernetes·graceful shutdown·incident을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: test slice·container·config·metric/trace·shutdown·K8s 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실 dependency·부하·배포 failure 검증에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: context cache 착시·probe loop·graceful loss 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### J6 단계 결과물

- Spring service 운영·복구 runbook 작성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
