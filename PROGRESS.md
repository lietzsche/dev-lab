# Container Internals & Runtime 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1-1** | PID·UTS·IPC namespace | PID·UTS·IPC namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **C1-2** | mount namespace·rootfs | mount namespace·rootfs의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-1 | 대기 | - |
| **C1-3** | network·user namespace | network·user namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-2 | 대기 | - |
| **C1-4** | PID 1·signal·process lifecycle | PID 1·signal·process lifecycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-3 | 대기 | - |
| **C2-1** | cgroup CPU·memory·PID | cgroup CPU·memory·PID의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-4 | 대기 | - |
| **C2-2** | capability와 non-root | capability와 non-root의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-1 | 대기 | - |
| **C2-3** | seccomp·AppArmor/SELinux | seccomp·AppArmor/SELinux의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-2 | 대기 | - |
| **C2-4** | rootless·user mapping·runtime boundary | rootless·user mapping·runtime boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-3 | 대기 | - |
| **C3-1** | OCI image·layer·copy-on-write | OCI image·layer·copy-on-write의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-4 | 대기 | - |
| **C3-2** | build context·Dockerfile graph | build context·Dockerfile graph의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-1 | 대기 | - |
| **C3-3** | cache key·multi-stage build | cache key·multi-stage build의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-2 | 대기 | - |
| **C3-4** | registry·manifest list·tag·digest | registry·manifest list·tag·digest의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-3 | 대기 | - |
| **C4-1** | dependency pinning·reproducible build | dependency pinning·reproducible build의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-4 | 대기 | - |
| **C4-2** | secret·cache mount·build isolation | secret·cache mount·build isolation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-1 | 대기 | - |
| **C4-3** | SBOM·license·vulnerability | SBOM·license·vulnerability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-2 | 대기 | - |
| **C4-4** | signature·attestation·provenance | signature·attestation·provenance의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-3 | 대기 | - |
| **C5-1** | writable layer·volume·bind mount | writable layer·volume·bind mount의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-4 | 대기 | - |
| **C5-2** | ownership·backup·restore | ownership·backup·restore의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-1 | 대기 | - |
| **C5-3** | bridge·DNS·port publishing | bridge·DNS·port publishing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-2 | 대기 | - |
| **C5-4** | log driver·healthcheck·restart | log driver·healthcheck·restart의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-3 | 대기 | - |
| **C6-1** | Compose model·environment·secret | Compose model·environment·secret의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-4 | 대기 | - |
| **C6-2** | dependency·health·startup readiness | dependency·health·startup readiness의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-1 | 대기 | - |
| **C6-3** | debug·exec·inspect·events | debug·exec·inspect·events의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-2 | 대기 | - |
| **C6-4** | immutable deploy·rollback·cleanup | immutable deploy·rollback·cleanup의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-3 | 대기 | - |

## 세부 기록

### C1-1. PID·UTS·IPC namespace

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C1-2. mount namespace·rootfs

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C1-3. network·user namespace

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C1-4. PID 1·signal·process lifecycle

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C2-1. cgroup CPU·memory·PID

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C2-2. capability와 non-root

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C2-3. seccomp·AppArmor/SELinux

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C2-4. rootless·user mapping·runtime boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C3-1. OCI image·layer·copy-on-write

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C3-2. build context·Dockerfile graph

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C3-3. cache key·multi-stage build

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C3-4. registry·manifest list·tag·digest

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C4-1. dependency pinning·reproducible build

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C4-2. secret·cache mount·build isolation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C4-3. SBOM·license·vulnerability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C4-4. signature·attestation·provenance

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C5-1. writable layer·volume·bind mount

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C5-2. ownership·backup·restore

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C5-3. bridge·DNS·port publishing

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C5-4. log driver·healthcheck·restart

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C6-1. Compose model·environment·secret

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C6-2. dependency·health·startup readiness

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C6-3. debug·exec·inspect·events

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### C6-4. immutable deploy·rollback·cleanup

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
