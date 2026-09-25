# Container Internals & Runtime 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Linux isolation primitives 단계에서 container가 Linux process인 이유 설명할 수 있는가?
- Resource와 runtime security 단계에서 최소 권한 runtime profile 작성할 수 있는가?
- Image와 content store 단계에서 source에서 실행 image까지 identity 추적할 수 있는가?
- Supply chain과 reproducibility 단계에서 검증 가능한 최소 image release할 수 있는가?
- Runtime data와 network 단계에서 state와 ephemeral compute 수명 분리할 수 있는가?
- Compose 운영과 debugging 단계에서 local production-like stack 운영 runbook할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 24소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **C1** | Linux isolation primitives | 4 | container가 Linux process인 이유 설명 |
| **C2** | Resource와 runtime security | 4 | 최소 권한 runtime profile 작성 |
| **C3** | Image와 content store | 4 | source에서 실행 image까지 identity 추적 |
| **C4** | Supply chain과 reproducibility | 4 | 검증 가능한 최소 image release |
| **C5** | Runtime data와 network | 4 | state와 ephemeral compute 수명 분리 |
| **C6** | Compose 운영과 debugging | 4 | local production-like stack 운영 runbook |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **C1-1** | PID·UTS·IPC namespace | PID·UTS·IPC namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **C1-2** | mount namespace·rootfs | mount namespace·rootfs의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-1 |
| **C1-3** | network·user namespace | network·user namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-2 |
| **C1-4** | PID 1·signal·process lifecycle | PID 1·signal·process lifecycle의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-3 |
| **C2-1** | cgroup CPU·memory·PID | cgroup CPU·memory·PID의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C1-4 |
| **C2-2** | capability와 non-root | capability와 non-root의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-1 |
| **C2-3** | seccomp·AppArmor/SELinux | seccomp·AppArmor/SELinux의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-2 |
| **C2-4** | rootless·user mapping·runtime boundary | rootless·user mapping·runtime boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-3 |
| **C3-1** | OCI image·layer·copy-on-write | OCI image·layer·copy-on-write의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C2-4 |
| **C3-2** | build context·Dockerfile graph | build context·Dockerfile graph의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-1 |
| **C3-3** | cache key·multi-stage build | cache key·multi-stage build의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-2 |
| **C3-4** | registry·manifest list·tag·digest | registry·manifest list·tag·digest의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-3 |
| **C4-1** | dependency pinning·reproducible build | dependency pinning·reproducible build의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C3-4 |
| **C4-2** | secret·cache mount·build isolation | secret·cache mount·build isolation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-1 |
| **C4-3** | SBOM·license·vulnerability | SBOM·license·vulnerability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-2 |
| **C4-4** | signature·attestation·provenance | signature·attestation·provenance의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-3 |
| **C5-1** | writable layer·volume·bind mount | writable layer·volume·bind mount의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C4-4 |
| **C5-2** | ownership·backup·restore | ownership·backup·restore의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-1 |
| **C5-3** | bridge·DNS·port publishing | bridge·DNS·port publishing의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-2 |
| **C5-4** | log driver·healthcheck·restart | log driver·healthcheck·restart의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-3 |
| **C6-1** | Compose model·environment·secret | Compose model·environment·secret의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C5-4 |
| **C6-2** | dependency·health·startup readiness | dependency·health·startup readiness의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-1 |
| **C6-3** | debug·exec·inspect·events | debug·exec·inspect·events의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-2 |
| **C6-4** | immutable deploy·rollback·cleanup | immutable deploy·rollback·cleanup의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | C6-3 |

## C1. Linux isolation primitives

- 관찰 축: namespace·rootfs·pivot_root·PID 1
- 통합 실습: namespace별 격리와 host view 비교
- 핵심 실패: PID 1 signal·zombie·escape boundary

### [C1-1] PID·UTS·IPC namespace

- 이해할 것: PID·UTS·IPC namespace을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: namespace·rootfs·pivot_root·PID 1 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace별 격리와 host view 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: PID 1 signal·zombie·escape boundary 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C1-2] mount namespace·rootfs

- 이해할 것: mount namespace·rootfs을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: namespace·rootfs·pivot_root·PID 1 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace별 격리와 host view 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: PID 1 signal·zombie·escape boundary 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C1-3] network·user namespace

- 이해할 것: network·user namespace을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: namespace·rootfs·pivot_root·PID 1 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace별 격리와 host view 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: PID 1 signal·zombie·escape boundary 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C1-4] PID 1·signal·process lifecycle

- 이해할 것: PID 1·signal·process lifecycle을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: namespace·rootfs·pivot_root·PID 1 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace별 격리와 host view 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: PID 1 signal·zombie·escape boundary 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C1 단계 결과물

- container가 Linux process인 이유 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## C2. Resource와 runtime security

- 관찰 축: cgroup v2·capability·seccomp·LSM·rootless
- 통합 실습: resource limit과 syscall/권한 차단
- 핵심 실패: OOM·CPU throttle·privileged 위험

### [C2-1] cgroup CPU·memory·PID

- 이해할 것: cgroup CPU·memory·PID을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: cgroup v2·capability·seccomp·LSM·rootless 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: resource limit과 syscall/권한 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM·CPU throttle·privileged 위험 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C2-2] capability와 non-root

- 이해할 것: capability와 non-root을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: cgroup v2·capability·seccomp·LSM·rootless 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: resource limit과 syscall/권한 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM·CPU throttle·privileged 위험 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C2-3] seccomp·AppArmor/SELinux

- 이해할 것: seccomp·AppArmor/SELinux을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: cgroup v2·capability·seccomp·LSM·rootless 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: resource limit과 syscall/권한 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM·CPU throttle·privileged 위험 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C2-4] rootless·user mapping·runtime boundary

- 이해할 것: rootless·user mapping·runtime boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: cgroup v2·capability·seccomp·LSM·rootless 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: resource limit과 syscall/권한 차단에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM·CPU throttle·privileged 위험 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C2 단계 결과물

- 최소 권한 runtime profile 작성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## C3. Image와 content store

- 관찰 축: layer·overlayfs·manifest·config·digest
- 통합 실습: Dockerfile 변경별 cache/digest 비교
- 핵심 실패: mutable tag·cache poisoning·large context

### [C3-1] OCI image·layer·copy-on-write

- 이해할 것: OCI image·layer·copy-on-write을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: layer·overlayfs·manifest·config·digest 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Dockerfile 변경별 cache/digest 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mutable tag·cache poisoning·large context 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C3-2] build context·Dockerfile graph

- 이해할 것: build context·Dockerfile graph을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: layer·overlayfs·manifest·config·digest 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Dockerfile 변경별 cache/digest 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mutable tag·cache poisoning·large context 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C3-3] cache key·multi-stage build

- 이해할 것: cache key·multi-stage build을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: layer·overlayfs·manifest·config·digest 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Dockerfile 변경별 cache/digest 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mutable tag·cache poisoning·large context 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C3-4] registry·manifest list·tag·digest

- 이해할 것: registry·manifest list·tag·digest을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: layer·overlayfs·manifest·config·digest 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Dockerfile 변경별 cache/digest 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mutable tag·cache poisoning·large context 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C3 단계 결과물

- source에서 실행 image까지 identity 추적.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## C4. Supply chain과 reproducibility

- 관찰 축: lock·SBOM·provenance·signature·scan
- 통합 실습: 동일 source 재build와 artifact 비교
- 핵심 실패: base drift·secret in layer·false-positive scan

### [C4-1] dependency pinning·reproducible build

- 이해할 것: dependency pinning·reproducible build을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: lock·SBOM·provenance·signature·scan 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 동일 source 재build와 artifact 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: base drift·secret in layer·false-positive scan 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C4-2] secret·cache mount·build isolation

- 이해할 것: secret·cache mount·build isolation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: lock·SBOM·provenance·signature·scan 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 동일 source 재build와 artifact 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: base drift·secret in layer·false-positive scan 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C4-3] SBOM·license·vulnerability

- 이해할 것: SBOM·license·vulnerability을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: lock·SBOM·provenance·signature·scan 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 동일 source 재build와 artifact 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: base drift·secret in layer·false-positive scan 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C4-4] signature·attestation·provenance

- 이해할 것: signature·attestation·provenance을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: lock·SBOM·provenance·signature·scan 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 동일 source 재build와 artifact 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: base drift·secret in layer·false-positive scan 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C4 단계 결과물

- 검증 가능한 최소 image release.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## C5. Runtime data와 network

- 관찰 축: volume·overlay write·bridge·DNS·port·log
- 통합 실습: API/worker/DB의 data/network path 구성
- 핵심 실패: ownership·stale DNS·port collision·log growth

### [C5-1] writable layer·volume·bind mount

- 이해할 것: writable layer·volume·bind mount을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: volume·overlay write·bridge·DNS·port·log 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: API/worker/DB의 data/network path 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: ownership·stale DNS·port collision·log growth 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C5-2] ownership·backup·restore

- 이해할 것: ownership·backup·restore을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: volume·overlay write·bridge·DNS·port·log 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: API/worker/DB의 data/network path 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: ownership·stale DNS·port collision·log growth 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C5-3] bridge·DNS·port publishing

- 이해할 것: bridge·DNS·port publishing을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: volume·overlay write·bridge·DNS·port·log 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: API/worker/DB의 data/network path 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: ownership·stale DNS·port collision·log growth 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C5-4] log driver·healthcheck·restart

- 이해할 것: log driver·healthcheck·restart을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: volume·overlay write·bridge·DNS·port·log 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: API/worker/DB의 data/network path 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: ownership·stale DNS·port collision·log growth 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C5 단계 결과물

- state와 ephemeral compute 수명 분리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## C6. Compose 운영과 debugging

- 관찰 축: compose model·dependency·signal·resource·artifact
- 통합 실습: 다중 service failure와 upgrade/rollback
- 핵심 실패: startup order 착각·health loop·partial upgrade

### [C6-1] Compose model·environment·secret

- 이해할 것: Compose model·environment·secret을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: compose model·dependency·signal·resource·artifact 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 다중 service failure와 upgrade/rollback에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: startup order 착각·health loop·partial upgrade 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C6-2] dependency·health·startup readiness

- 이해할 것: dependency·health·startup readiness을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: compose model·dependency·signal·resource·artifact 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 다중 service failure와 upgrade/rollback에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: startup order 착각·health loop·partial upgrade 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C6-3] debug·exec·inspect·events

- 이해할 것: debug·exec·inspect·events을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: compose model·dependency·signal·resource·artifact 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 다중 service failure와 upgrade/rollback에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: startup order 착각·health loop·partial upgrade 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [C6-4] immutable deploy·rollback·cleanup

- 이해할 것: immutable deploy·rollback·cleanup을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: compose model·dependency·signal·resource·artifact 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 다중 service failure와 upgrade/rollback에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: startup order 착각·health loop·partial upgrade 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### C6 단계 결과물

- local production-like stack 운영 runbook.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
