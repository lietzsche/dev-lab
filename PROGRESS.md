# Container Internals & Runtime 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`, 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1-1** | PID namespace | PID namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - | 대기 | - |
| **C1-2** | mount·UTS·IPC | mount·UTS·IPC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-1 | 대기 | - |
| **C1-3** | network·user namespace | network·user namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-2 | 대기 | - |
| **C2-1** | cgroup CPU·memory | cgroup CPU·memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-3 | 대기 | - |
| **C2-2** | capability·seccomp | capability·seccomp의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-1 | 대기 | - |
| **C2-3** | rootless | rootless의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-2 | 대기 | - |
| **C3-1** | copy-on-write | copy-on-write의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-3 | 대기 | - |
| **C3-2** | build graph·cache | build graph·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-1 | 대기 | - |
| **C3-3** | registry·manifest | registry·manifest의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-2 | 대기 | - |
| **C4-1** | multi-stage·cache | multi-stage·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-3 | 대기 | - |
| **C4-2** | SBOM | SBOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-1 | 대기 | - |
| **C4-3** | provenance·scan | provenance·scan의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-2 | 대기 | - |
| **C5-1** | PID 1·signal | PID 1·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-3 | 대기 | - |
| **C5-2** | volume·ownership | volume·ownership의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-1 | 대기 | - |
| **C5-3** | bridge·DNS·port | bridge·DNS·port의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-2 | 대기 | - |
| **C6-1** | service dependency | service dependency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-3 | 대기 | - |
| **C6-2** | debug·exec | debug·exec의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C6-1 | 대기 | - |
| **C6-3** | 배포·복구 | 배포·복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C6-2 | 대기 | - |

## 세부 기록

### C1-1. PID namespace

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C1-2. mount·UTS·IPC

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C1-3. network·user namespace

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C2-1. cgroup CPU·memory

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C2-2. capability·seccomp

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C2-3. rootless

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C3-1. copy-on-write

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C3-2. build graph·cache

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C3-3. registry·manifest

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C4-1. multi-stage·cache

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C4-2. SBOM

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C4-3. provenance·scan

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C5-1. PID 1·signal

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C5-2. volume·ownership

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C5-3. bridge·DNS·port

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C6-1. service dependency

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C6-2. debug·exec

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### C6-3. 배포·복구

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:
