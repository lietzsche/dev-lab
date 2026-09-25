# Linux Internals & Operations 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L1-1** | process image와 exec | process image와 exec의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **L1-2** | PID·PPID·process tree | PID·PPID·process tree의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-1 | 대기 | - |
| **L1-3** | process state와 /proc | process state와 /proc의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-2 | 대기 | - |
| **L1-4** | signal delivery와 exit status | signal delivery와 exit status의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-3 | 대기 | - |
| **L1-5** | thread·scheduler·context switch | thread·scheduler·context switch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-4 | 대기 | - |
| **L2-1** | inode·dentry·hard/symbolic link | inode·dentry·hard/symbolic link의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-5 | 대기 | - |
| **L2-2** | mount·filesystem·namespace | mount·filesystem·namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-1 | 대기 | - |
| **L2-3** | file descriptor·open file description | file descriptor·open file description의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-2 | 대기 | - |
| **L2-4** | pipe·redirection·blocking I/O | pipe·redirection·blocking I/O의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-3 | 대기 | - |
| **L2-5** | buffering·page cache·fsync·atomic replace | buffering·page cache·fsync·atomic replace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-4 | 대기 | - |
| **L3-1** | virtual memory·page·mapping | virtual memory·page·mapping의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-5 | 대기 | - |
| **L3-2** | stack·heap·mmap·shared memory | stack·heap·mmap·shared memory의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-1 | 대기 | - |
| **L3-3** | RSS·PSS·cache·swap | RSS·PSS·cache·swap의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-2 | 대기 | - |
| **L3-4** | overcommit·OOM killer | overcommit·OOM killer의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-3 | 대기 | - |
| **L3-5** | rlimit·cgroup resource accounting | rlimit·cgroup resource accounting의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-4 | 대기 | - |
| **L4-1** | interface·address·route | interface·address·route의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-5 | 대기 | - |
| **L4-2** | neighbor·DNS resolution | neighbor·DNS resolution의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-1 | 대기 | - |
| **L4-3** | socket·bind·listen·connect | socket·bind·listen·connect의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-2 | 대기 | - |
| **L4-4** | TCP state·flow·timeout | TCP state·flow·timeout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-3 | 대기 | - |
| **L4-5** | HTTP·TLS·proxy와 packet inspection | HTTP·TLS·proxy와 packet inspection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-4 | 대기 | - |
| **L5-1** | user·group·process credential | user·group·process credential의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-5 | 대기 | - |
| **L5-2** | permission·umask·ACL | permission·umask·ACL의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-1 | 대기 | - |
| **L5-3** | sudo·capability·seccomp | sudo·capability·seccomp의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-2 | 대기 | - |
| **L5-4** | systemd unit·dependency·journal | systemd unit·dependency·journal의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-3 | 대기 | - |
| **L5-5** | service user·secret·graceful shutdown | service user·secret·graceful shutdown의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-4 | 대기 | - |
| **L6-1** | CPU saturation·load average | CPU saturation·load average의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-5 | 대기 | - |
| **L6-2** | memory pressure·leak | memory pressure·leak의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-1 | 대기 | - |
| **L6-3** | disk latency·filesystem exhaustion | disk latency·filesystem exhaustion의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-2 | 대기 | - |
| **L6-4** | fd·socket·network exhaustion | fd·socket·network exhaustion의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-3 | 대기 | - |
| **L6-5** | strace·lsof·perf 관점의 종합 장애 대응 | strace·lsof·perf 관점의 종합 장애 대응의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-4 | 대기 | - |

## 세부 기록

### L1-1. process image와 exec

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L1-2. PID·PPID·process tree

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L1-3. process state와 /proc

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L1-4. signal delivery와 exit status

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L1-5. thread·scheduler·context switch

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L2-1. inode·dentry·hard/symbolic link

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L2-2. mount·filesystem·namespace

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L2-3. file descriptor·open file description

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L2-4. pipe·redirection·blocking I/O

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L2-5. buffering·page cache·fsync·atomic replace

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L3-1. virtual memory·page·mapping

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L3-2. stack·heap·mmap·shared memory

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L3-3. RSS·PSS·cache·swap

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L3-4. overcommit·OOM killer

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L3-5. rlimit·cgroup resource accounting

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L4-1. interface·address·route

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L4-2. neighbor·DNS resolution

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L4-3. socket·bind·listen·connect

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L4-4. TCP state·flow·timeout

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L4-5. HTTP·TLS·proxy와 packet inspection

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L5-1. user·group·process credential

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L5-2. permission·umask·ACL

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L5-3. sudo·capability·seccomp

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L5-4. systemd unit·dependency·journal

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L5-5. service user·secret·graceful shutdown

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L6-1. CPU saturation·load average

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L6-2. memory pressure·leak

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L6-3. disk latency·filesystem exhaustion

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L6-4. fd·socket·network exhaustion

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### L6-5. strace·lsof·perf 관점의 종합 장애 대응

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
