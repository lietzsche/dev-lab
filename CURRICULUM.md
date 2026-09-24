# Container Internals & Runtime 커리큘럼

## 목적

컨테이너를 격리·제한된 Linux process와 불변 image로 이해한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Linux 완료 권장
- 최종 실습: API·worker image의 권한·resource·health 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **C1** | 격리 | PID·mount·user namespace | host/container 비교 |
| **C2** | 자원과 보안 | cgroup·capability·seccomp | limit과 권한 실패 |
| **C3** | Image | layer·overlayfs·digest | layer와 digest 비교 |
| **C4** | 공급망 | BuildKit·SBOM·signature | multi-stage non-root build |
| **C5** | Runtime | state·signal·volume·network | shutdown·volume 장애 |
| **C6** | Compose | desired state·health·log | API·worker·DB 장애 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **C1-1** | PID namespace | PID namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **C1-2** | mount·UTS·IPC | mount·UTS·IPC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-1 |
| **C1-3** | network·user namespace | network·user namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-2 |
| **C2-1** | cgroup CPU·memory | cgroup CPU·memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C1-3 |
| **C2-2** | capability·seccomp | capability·seccomp의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-1 |
| **C2-3** | rootless | rootless의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-2 |
| **C3-1** | copy-on-write | copy-on-write의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C2-3 |
| **C3-2** | build graph·cache | build graph·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-1 |
| **C3-3** | registry·manifest | registry·manifest의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-2 |
| **C4-1** | multi-stage·cache | multi-stage·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C3-3 |
| **C4-2** | SBOM | SBOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-1 |
| **C4-3** | provenance·scan | provenance·scan의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-2 |
| **C5-1** | PID 1·signal | PID 1·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C4-3 |
| **C5-2** | volume·ownership | volume·ownership의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-1 |
| **C5-3** | bridge·DNS·port | bridge·DNS·port의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-2 |
| **C6-1** | service dependency | service dependency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C5-3 |
| **C6-2** | debug·exec | debug·exec의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C6-1 |
| **C6-3** | 배포·복구 | 배포·복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | C6-2 |

## 상세 커리큘럼

### [C1-1] PID namespace

- 목표: PID namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: PID·mount·user namespace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: host/container 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C1-2] mount·UTS·IPC

- 목표: mount·UTS·IPC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: PID·mount·user namespace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: host/container 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C1-3] network·user namespace

- 목표: network·user namespace의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: PID·mount·user namespace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: host/container 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C2-1] cgroup CPU·memory

- 목표: cgroup CPU·memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: cgroup·capability·seccomp를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: limit과 권한 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C2-2] capability·seccomp

- 목표: capability·seccomp의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: cgroup·capability·seccomp를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: limit과 권한 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C2-3] rootless

- 목표: rootless의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: cgroup·capability·seccomp를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: limit과 권한 실패 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C3-1] copy-on-write

- 목표: copy-on-write의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layer·overlayfs·digest를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: layer와 digest 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C3-2] build graph·cache

- 목표: build graph·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layer·overlayfs·digest를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: layer와 digest 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C3-3] registry·manifest

- 목표: registry·manifest의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: layer·overlayfs·digest를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: layer와 digest 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C4-1] multi-stage·cache

- 목표: multi-stage·cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: BuildKit·SBOM·signature를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: multi-stage non-root build 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C4-2] SBOM

- 목표: SBOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: BuildKit·SBOM·signature를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: multi-stage non-root build 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C4-3] provenance·scan

- 목표: provenance·scan의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: BuildKit·SBOM·signature를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: multi-stage non-root build 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C5-1] PID 1·signal

- 목표: PID 1·signal의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: state·signal·volume·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: shutdown·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C5-2] volume·ownership

- 목표: volume·ownership의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: state·signal·volume·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: shutdown·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C5-3] bridge·DNS·port

- 목표: bridge·DNS·port의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: state·signal·volume·network를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: shutdown·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C6-1] service dependency

- 목표: service dependency의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: desired state·health·log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: API·worker·DB 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C6-2] debug·exec

- 목표: debug·exec의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: desired state·health·log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: API·worker·DB 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [C6-3] 배포·복구

- 목표: 배포·복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: desired state·health·log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: API·worker·DB 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
