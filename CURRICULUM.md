# Linux Internals & Operations 커리큘럼

## 목적

프로세스·파일·메모리·네트워크를 관찰하고 운영 장애를 진단한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Git 완료 권장
- 최종 실습: Spring API와 Python worker 장애 진단
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **L1** | 프로세스와 실행 | /proc·PID·signal | 부모·자식·zombie 재현 |
| **L2** | 파일과 I/O | inode·fd·page cache | link·pipe·열린 파일 재현 |
| **L3** | 메모리와 자원 | maps·smaps·vmstat | mmap·OOM·limit 재현 |
| **L4** | 네트워크 | ip·ss·DNS·TCP state | timeout·reset 재현 |
| **L5** | 서비스와 보안 | systemd·journal·credential | 최소 권한 서비스 구성 |
| **L6** | 장애 분석 | top·lsof·strace·ss | resource 장애 주입 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **L1-1** | PID와 process tree | PID와 process tree의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **L1-2** | signal과 종료 | signal과 종료의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-1 |
| **L1-3** | thread와 scheduler | thread와 scheduler의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-2 |
| **L2-1** | inode와 mount | inode와 mount의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L1-3 |
| **L2-2** | fd와 redirection | fd와 redirection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-1 |
| **L2-3** | buffer와 page cache | buffer와 page cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-2 |
| **L3-1** | virtual memory | virtual memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L2-3 |
| **L3-2** | RSS·swap·OOM | RSS·swap·OOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-1 |
| **L3-3** | ulimit와 cgroup | ulimit와 cgroup의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-2 |
| **L4-1** | interface·route·DNS | interface·route·DNS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L3-3 |
| **L4-2** | socket·port·TCP | socket·port·TCP의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-1 |
| **L4-3** | HTTP·TLS·timeout | HTTP·TLS·timeout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-2 |
| **L5-1** | user·group·permission | user·group·permission의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L4-3 |
| **L5-2** | systemd lifecycle | systemd lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-1 |
| **L5-3** | namespace·capability | namespace·capability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-2 |
| **L6-1** | CPU·memory 진단 | CPU·memory 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L5-3 |
| **L6-2** | I/O·network 진단 | I/O·network 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L6-1 |
| **L6-3** | 종합 복구 | 종합 복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | L6-2 |

## 상세 커리큘럼

### [L1-1] PID와 process tree

- 목표: PID와 process tree의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: /proc·PID·signal를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부모·자식·zombie 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L1-2] signal과 종료

- 목표: signal과 종료의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: /proc·PID·signal를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부모·자식·zombie 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L1-3] thread와 scheduler

- 목표: thread와 scheduler의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: /proc·PID·signal를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 부모·자식·zombie 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L2-1] inode와 mount

- 목표: inode와 mount의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inode·fd·page cache를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: link·pipe·열린 파일 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L2-2] fd와 redirection

- 목표: fd와 redirection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inode·fd·page cache를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: link·pipe·열린 파일 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L2-3] buffer와 page cache

- 목표: buffer와 page cache의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: inode·fd·page cache를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: link·pipe·열린 파일 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L3-1] virtual memory

- 목표: virtual memory의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: maps·smaps·vmstat를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: mmap·OOM·limit 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L3-2] RSS·swap·OOM

- 목표: RSS·swap·OOM의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: maps·smaps·vmstat를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: mmap·OOM·limit 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L3-3] ulimit와 cgroup

- 목표: ulimit와 cgroup의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: maps·smaps·vmstat를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: mmap·OOM·limit 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L4-1] interface·route·DNS

- 목표: interface·route·DNS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ip·ss·DNS·TCP state를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: timeout·reset 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L4-2] socket·port·TCP

- 목표: socket·port·TCP의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ip·ss·DNS·TCP state를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: timeout·reset 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L4-3] HTTP·TLS·timeout

- 목표: HTTP·TLS·timeout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ip·ss·DNS·TCP state를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: timeout·reset 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L5-1] user·group·permission

- 목표: user·group·permission의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: systemd·journal·credential를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한 서비스 구성 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L5-2] systemd lifecycle

- 목표: systemd lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: systemd·journal·credential를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한 서비스 구성 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L5-3] namespace·capability

- 목표: namespace·capability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: systemd·journal·credential를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한 서비스 구성 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L6-1] CPU·memory 진단

- 목표: CPU·memory 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: top·lsof·strace·ss를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: resource 장애 주입 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L6-2] I/O·network 진단

- 목표: I/O·network 진단의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: top·lsof·strace·ss를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: resource 장애 주입 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [L6-3] 종합 복구

- 목표: 종합 복구의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: top·lsof·strace·ss를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: resource 장애 주입 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
