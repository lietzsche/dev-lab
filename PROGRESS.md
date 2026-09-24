# JVM & Spring Internals 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`, 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **J1-1** | bytecode·class loading | bytecode·class loading의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - | 대기 | - |
| **J1-2** | heap·stack·layout | heap·stack·layout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-1 | 대기 | - |
| **J1-3** | GC·memory leak | GC·memory leak의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-2 | 대기 | - |
| **J2-1** | Java Memory Model | Java Memory Model의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J1-3 | 대기 | - |
| **J2-2** | lock·collection | lock·collection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-1 | 대기 | - |
| **J2-3** | executor·virtual thread | executor·virtual thread의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-2 | 대기 | - |
| **J3-1** | bean lifecycle | bean lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J2-3 | 대기 | - |
| **J3-2** | AOP·self invocation | AOP·self invocation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-1 | 대기 | - |
| **J3-3** | auto-configuration | auto-configuration의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-2 | 대기 | - |
| **J4-1** | transaction boundary | transaction boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J3-3 | 대기 | - |
| **J4-2** | propagation·locking | propagation·locking의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-1 | 대기 | - |
| **J4-3** | JPA flush·batch | JPA flush·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-2 | 대기 | - |
| **J5-1** | MVC exception | MVC exception의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J4-3 | 대기 | - |
| **J5-2** | Security chain | Security chain의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-1 | 대기 | - |
| **J5-3** | async·event·batch | async·event·batch의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-2 | 대기 | - |
| **J6-1** | test slice·containers | test slice·containers의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J5-3 | 대기 | - |
| **J6-2** | profiling·trace | profiling·trace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J6-1 | 대기 | - |
| **J6-3** | Kubernetes 운영 | Kubernetes 운영의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | J6-2 | 대기 | - |

## 세부 기록

### J1-1. bytecode·class loading

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J1-2. heap·stack·layout

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J1-3. GC·memory leak

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J2-1. Java Memory Model

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J2-2. lock·collection

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J2-3. executor·virtual thread

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J3-1. bean lifecycle

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J3-2. AOP·self invocation

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J3-3. auto-configuration

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J4-1. transaction boundary

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J4-2. propagation·locking

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J4-3. JPA flush·batch

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J5-1. MVC exception

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J5-2. Security chain

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J5-3. async·event·batch

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J6-1. test slice·containers

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J6-2. profiling·trace

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### J6-3. Kubernetes 운영

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:
