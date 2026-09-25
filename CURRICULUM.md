# JavaScript Runtime & TypeScript Systems 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- JavaScript object와 execution 단계에서 JS runtime behavior를 언어 모델로 설명할 수 있는가?
- TypeScript type system 단계에서 domain state를 type으로 제한할 수 있는가?
- Runtime boundary와 API 단계에서 외부 입력을 검증된 domain 값으로 변환할 수 있는가?
- Node runtime와 automation 단계에서 신뢰 가능한 CLI와 automation worker 구축할 수 있는가?
- Browser·React application 단계에서 agent 승인 UI의 state boundary 설계할 수 있는가?
- Test·Build·Operation 단계에서 배포 후 회귀와 장애를 추적할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 24소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **T1** | JavaScript object와 execution | 4 | JS runtime behavior를 언어 모델로 설명 |
| **T2** | TypeScript type system | 4 | domain state를 type으로 제한 |
| **T3** | Runtime boundary와 API | 4 | 외부 입력을 검증된 domain 값으로 변환 |
| **T4** | Node runtime와 automation | 4 | 신뢰 가능한 CLI와 automation worker 구축 |
| **T5** | Browser·React application | 4 | agent 승인 UI의 state boundary 설계 |
| **T6** | Test·Build·Operation | 4 | 배포 후 회귀와 장애를 추적 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **T1-1** | value·identity·prototype chain | value·identity·prototype chain의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **T1-2** | scope·closure·this | scope·closure·this의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T1-1 |
| **T1-3** | ESM·CommonJS·module cache | ESM·CommonJS·module cache의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T1-2 |
| **T1-4** | event loop·task·microtask·Promise | event loop·task·microtask·Promise의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T1-3 |
| **T2-1** | structural typing·inference | structural typing·inference의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T1-4 |
| **T2-2** | union·narrowing·never | union·narrowing·never의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T2-1 |
| **T2-3** | generic·constraint·variance | generic·constraint·variance의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T2-2 |
| **T2-4** | type erasure·declaration·compiler options | type erasure·declaration·compiler options의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T2-3 |
| **T3-1** | unknown·runtime validation | unknown·runtime validation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T2-4 |
| **T3-2** | JSON·date·number·serialization | JSON·date·number·serialization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T3-1 |
| **T3-3** | typed error·Result·async failure | typed error·Result·async failure의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T3-2 |
| **T3-4** | API contract·OpenAPI·versioning | API contract·OpenAPI·versioning의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T3-3 |
| **T4-1** | Node I/O·Buffer·stream | Node I/O·Buffer·stream의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T3-4 |
| **T4-2** | backpressure·pipeline·error | backpressure·pipeline·error의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T4-1 |
| **T4-3** | process·signal·child process | process·signal·child process의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T4-2 |
| **T4-4** | worker thread·concurrency·cancellation | worker thread·concurrency·cancellation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T4-3 |
| **T5-1** | browser lifecycle·DOM·network | browser lifecycle·DOM·network의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T4-4 |
| **T5-2** | React render·state·reducer | React render·state·reducer의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T5-1 |
| **T5-3** | effect·external synchronization | effect·external synchronization의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T5-2 |
| **T5-4** | server state·forms·accessibility | server state·forms·accessibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T5-3 |
| **T6-1** | test boundary·fake·clock | test boundary·fake·clock의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T5-4 |
| **T6-2** | Playwright·polling·flaky control | Playwright·polling·flaky control의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T6-1 |
| **T6-3** | package·lockfile·build·bundle | package·lockfile·build·bundle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T6-2 |
| **T6-4** | logging·metric·trace·release | logging·metric·trace·release의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | T6-3 |

## T1. JavaScript object와 execution

- 관찰 축: value/reference·prototype·scope·module·event loop
- 통합 실습: 실행 순서와 object lookup 예측
- 핵심 실패: this/closure·module cycle·microtask starvation

### [T1-1] value·identity·prototype chain

- 이해할 것: value·identity·prototype chain을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: value/reference·prototype·scope·module·event loop 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실행 순서와 object lookup 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: this/closure·module cycle·microtask starvation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T1-2] scope·closure·this

- 이해할 것: scope·closure·this을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: value/reference·prototype·scope·module·event loop 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실행 순서와 object lookup 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: this/closure·module cycle·microtask starvation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T1-3] ESM·CommonJS·module cache

- 이해할 것: ESM·CommonJS·module cache을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: value/reference·prototype·scope·module·event loop 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실행 순서와 object lookup 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: this/closure·module cycle·microtask starvation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T1-4] event loop·task·microtask·Promise

- 이해할 것: event loop·task·microtask·Promise을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: value/reference·prototype·scope·module·event loop 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 실행 순서와 object lookup 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: this/closure·module cycle·microtask starvation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T1 단계 결과물

- JS runtime behavior를 언어 모델로 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## T2. TypeScript type system

- 관찰 축: structural type·narrowing·generic·variance·emit
- 통합 실습: compiler diagnostic와 emitted JS 비교
- 핵심 실패: unsound assertion·any leak·exhaustiveness 누락

### [T2-1] structural typing·inference

- 이해할 것: structural typing·inference을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: structural type·narrowing·generic·variance·emit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic와 emitted JS 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: unsound assertion·any leak·exhaustiveness 누락 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T2-2] union·narrowing·never

- 이해할 것: union·narrowing·never을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: structural type·narrowing·generic·variance·emit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic와 emitted JS 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: unsound assertion·any leak·exhaustiveness 누락 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T2-3] generic·constraint·variance

- 이해할 것: generic·constraint·variance을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: structural type·narrowing·generic·variance·emit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic와 emitted JS 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: unsound assertion·any leak·exhaustiveness 누락 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T2-4] type erasure·declaration·compiler options

- 이해할 것: type erasure·declaration·compiler options을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: structural type·narrowing·generic·variance·emit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: compiler diagnostic와 emitted JS 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: unsound assertion·any leak·exhaustiveness 누락 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T2 단계 결과물

- domain state를 type으로 제한.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## T3. Runtime boundary와 API

- 관찰 축: unknown·schema·serialization·error·contract
- 통합 실습: 깨진 env/JSON/HTTP payload 차단
- 핵심 실패: static type 신뢰로 runtime crash·partial response

### [T3-1] unknown·runtime validation

- 이해할 것: unknown·runtime validation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unknown·schema·serialization·error·contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 깨진 env/JSON/HTTP payload 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: static type 신뢰로 runtime crash·partial response 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T3-2] JSON·date·number·serialization

- 이해할 것: JSON·date·number·serialization을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unknown·schema·serialization·error·contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 깨진 env/JSON/HTTP payload 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: static type 신뢰로 runtime crash·partial response 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T3-3] typed error·Result·async failure

- 이해할 것: typed error·Result·async failure을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unknown·schema·serialization·error·contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 깨진 env/JSON/HTTP payload 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: static type 신뢰로 runtime crash·partial response 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T3-4] API contract·OpenAPI·versioning

- 이해할 것: API contract·OpenAPI·versioning을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unknown·schema·serialization·error·contract 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 깨진 env/JSON/HTTP payload 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: static type 신뢰로 runtime crash·partial response 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T3 단계 결과물

- 외부 입력을 검증된 domain 값으로 변환.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## T4. Node runtime와 automation

- 관찰 축: process·stream·buffer·child·worker·signal
- 통합 실습: large stream과 child cancellation
- 핵심 실패: memory growth·backpressure·orphan child

### [T4-1] Node I/O·Buffer·stream

- 이해할 것: Node I/O·Buffer·stream을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: process·stream·buffer·child·worker·signal 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: large stream과 child cancellation에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: memory growth·backpressure·orphan child 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T4-2] backpressure·pipeline·error

- 이해할 것: backpressure·pipeline·error을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: process·stream·buffer·child·worker·signal 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: large stream과 child cancellation에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: memory growth·backpressure·orphan child 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T4-3] process·signal·child process

- 이해할 것: process·signal·child process을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: process·stream·buffer·child·worker·signal 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: large stream과 child cancellation에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: memory growth·backpressure·orphan child 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T4-4] worker thread·concurrency·cancellation

- 이해할 것: worker thread·concurrency·cancellation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: process·stream·buffer·child·worker·signal 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: large stream과 child cancellation에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: memory growth·backpressure·orphan child 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T4 단계 결과물

- 신뢰 가능한 CLI와 automation worker 구축.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## T5. Browser·React application

- 관찰 축: browser event·render·state·effect·cache·accessibility
- 통합 실습: race와 stale state를 UI test로 재현
- 핵심 실패: effect loop·stale closure·cache inconsistency

### [T5-1] browser lifecycle·DOM·network

- 이해할 것: browser lifecycle·DOM·network을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: browser event·render·state·effect·cache·accessibility 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race와 stale state를 UI test로 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: effect loop·stale closure·cache inconsistency 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T5-2] React render·state·reducer

- 이해할 것: React render·state·reducer을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: browser event·render·state·effect·cache·accessibility 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race와 stale state를 UI test로 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: effect loop·stale closure·cache inconsistency 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T5-3] effect·external synchronization

- 이해할 것: effect·external synchronization을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: browser event·render·state·effect·cache·accessibility 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race와 stale state를 UI test로 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: effect loop·stale closure·cache inconsistency 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T5-4] server state·forms·accessibility

- 이해할 것: server state·forms·accessibility을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: browser event·render·state·effect·cache·accessibility 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: race와 stale state를 UI test로 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: effect loop·stale closure·cache inconsistency 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T5 단계 결과물

- agent 승인 UI의 state boundary 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## T6. Test·Build·Operation

- 관찰 축: unit/integration/e2e·bundle·source map·telemetry
- 통합 실습: contract 변경과 flaky UI를 CI에서 검출
- 핵심 실패: fake timer misuse·bundle drift·unmapped error

### [T6-1] test boundary·fake·clock

- 이해할 것: test boundary·fake·clock을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unit/integration/e2e·bundle·source map·telemetry 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: contract 변경과 flaky UI를 CI에서 검출에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: fake timer misuse·bundle drift·unmapped error 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T6-2] Playwright·polling·flaky control

- 이해할 것: Playwright·polling·flaky control을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unit/integration/e2e·bundle·source map·telemetry 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: contract 변경과 flaky UI를 CI에서 검출에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: fake timer misuse·bundle drift·unmapped error 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T6-3] package·lockfile·build·bundle

- 이해할 것: package·lockfile·build·bundle을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unit/integration/e2e·bundle·source map·telemetry 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: contract 변경과 flaky UI를 CI에서 검출에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: fake timer misuse·bundle drift·unmapped error 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [T6-4] logging·metric·trace·release

- 이해할 것: logging·metric·trace·release을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: unit/integration/e2e·bundle·source map·telemetry 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: contract 변경과 flaky UI를 CI에서 검출에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: fake timer misuse·bundle drift·unmapped error 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### T6 단계 결과물

- 배포 후 회귀와 장애를 추적.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
