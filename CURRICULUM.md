# JVM & Spring Internals 커리큘럼

## 목적

JVM·동시성·transaction·proxy 모델로 Spring 장애를 진단한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Java/Spring 실무
- 최종 실습: Spring API를 부하·trace·dump로 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **J1** | JVM 실행·메모리 | bytecode·class·heap·layout | compile·allocation 관찰 |
| **J2** | 동시성·성능 | thread dump·lock·JFR | race·deadlock |
| **J3** | Spring container | bean·lifecycle·proxy | scope·proxy 관찰 |
| **J4** | Transaction | SQL·connection·lock | isolation 반례 |
| **J5** | Web·Security·Async | filter·request thread·context | auth·async 실패 |
| **J6** | 운영·테스트 | test context·metric·dump | 실 dependency·부하 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **J1-1** | bytecode·class loading | bytecode·class loading의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **J1-2** | heap·stack·layout | heap·stack·layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-1 |
| **J1-3** | GC·memory leak | GC·memory leak의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-2 |
| **J2-1** | Java Memory Model | Java Memory Model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-3 |
| **J2-2** | lock·collection | lock·collection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-1 |
| **J2-3** | executor·virtual thread | executor·virtual thread의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-2 |
| **J3-1** | bean lifecycle | bean lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-3 |
| **J3-2** | AOP·self invocation | AOP·self invocation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-1 |
| **J3-3** | auto-configuration | auto-configuration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-2 |
| **J4-1** | transaction boundary | transaction boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-3 |
| **J4-2** | propagation·locking | propagation·locking의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-1 |
| **J4-3** | JPA flush·batch | JPA flush·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-2 |
| **J5-1** | MVC exception | MVC exception의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-3 |
| **J5-2** | Security chain | Security chain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-1 |
| **J5-3** | async·event·batch | async·event·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-2 |
| **J6-1** | test slice·containers | test slice·containers의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-3 |
| **J6-2** | profiling·trace | profiling·trace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J6-1 |
| **J6-3** | Kubernetes 운영 | Kubernetes 운영의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J6-2 |

## 상세 커리큘럼

### [J1-1] bytecode·class loading

- 목표: bytecode·class loading의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bytecode·class·heap·layout를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile·allocation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J1-2] heap·stack·layout

- 목표: heap·stack·layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bytecode·class·heap·layout를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile·allocation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J1-3] GC·memory leak

- 목표: GC·memory leak의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bytecode·class·heap·layout를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: compile·allocation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J2-1] Java Memory Model

- 목표: Java Memory Model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread dump·lock·JFR를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J2-2] lock·collection

- 목표: lock·collection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread dump·lock·JFR를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J2-3] executor·virtual thread

- 목표: executor·virtual thread의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: thread dump·lock·JFR를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: race·deadlock 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J3-1] bean lifecycle

- 목표: bean lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bean·lifecycle·proxy를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: scope·proxy 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J3-2] AOP·self invocation

- 목표: AOP·self invocation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bean·lifecycle·proxy를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: scope·proxy 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J3-3] auto-configuration

- 목표: auto-configuration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: bean·lifecycle·proxy를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: scope·proxy 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J4-1] transaction boundary

- 목표: transaction boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: SQL·connection·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: isolation 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J4-2] propagation·locking

- 목표: propagation·locking의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: SQL·connection·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: isolation 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J4-3] JPA flush·batch

- 목표: JPA flush·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: SQL·connection·lock를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: isolation 반례 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J5-1] MVC exception

- 목표: MVC exception의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: filter·request thread·context를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: auth·async 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J5-2] Security chain

- 목표: Security chain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: filter·request thread·context를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: auth·async 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J5-3] async·event·batch

- 목표: async·event·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: filter·request thread·context를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: auth·async 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J6-1] test slice·containers

- 목표: test slice·containers의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test context·metric·dump를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 실 dependency·부하 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J6-2] profiling·trace

- 목표: profiling·trace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test context·metric·dump를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 실 dependency·부하 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [J6-3] Kubernetes 운영

- 목표: Kubernetes 운영의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: test context·metric·dump를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 실 dependency·부하 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
