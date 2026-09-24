# Linux Internals & Operations 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`, 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L1-1** | PID와 process tree | PID와 process tree의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - | 대기 | - |
| **L1-2** | signal과 종료 | signal과 종료의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-1 | 대기 | - |
| **L1-3** | thread와 scheduler | thread와 scheduler의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-2 | 대기 | - |
| **L2-1** | inode와 mount | inode와 mount의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-3 | 대기 | - |
| **L2-2** | fd와 redirection | fd와 redirection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-1 | 대기 | - |
| **L2-3** | buffer와 page cache | buffer와 page cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-2 | 대기 | - |
| **L3-1** | virtual memory | virtual memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-3 | 대기 | - |
| **L3-2** | RSS·swap·OOM | RSS·swap·OOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-1 | 대기 | - |
| **L3-3** | ulimit와 cgroup | ulimit와 cgroup의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-2 | 대기 | - |
| **L4-1** | interface·route·DNS | interface·route·DNS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-3 | 대기 | - |
| **L4-2** | socket·port·TCP | socket·port·TCP의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-1 | 대기 | - |
| **L4-3** | HTTP·TLS·timeout | HTTP·TLS·timeout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-2 | 대기 | - |
| **L5-1** | user·group·permission | user·group·permission의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-3 | 대기 | - |
| **L5-2** | systemd lifecycle | systemd lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-1 | 대기 | - |
| **L5-3** | namespace·capability | namespace·capability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-2 | 대기 | - |
| **L6-1** | CPU·memory 진단 | CPU·memory 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-3 | 대기 | - |
| **L6-2** | I/O·network 진단 | I/O·network 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L6-1 | 대기 | - |
| **L6-3** | 종합 복구 | 종합 복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L6-2 | 대기 | - |

## 세부 기록

### L1-1. PID와 process tree

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L1-2. signal과 종료

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L1-3. thread와 scheduler

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L2-1. inode와 mount

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L2-2. fd와 redirection

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L2-3. buffer와 page cache

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L3-1. virtual memory

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L3-2. RSS·swap·OOM

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L3-3. ulimit와 cgroup

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L4-1. interface·route·DNS

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L4-2. socket·port·TCP

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L4-3. HTTP·TLS·timeout

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L5-1. user·group·permission

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L5-2. systemd lifecycle

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L5-3. namespace·capability

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L6-1. CPU·memory 진단

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L6-2. I/O·network 진단

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### L6-3. 종합 복구

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:
