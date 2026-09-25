# Linux Internals & Operations 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Process 실행 모델 단계에서 service 장애를 process 관점에서 진단할 수 있는가?
- Filesystem과 I/O 단계에서 파일 이름부터 storage flush까지 경로 설명할 수 있는가?
- Memory와 resource 단계에서 memory 지표로 application과 kernel 원인 분리할 수 있는가?
- Network stack 단계에서 HTTP 오류를 name/network/transport/application 층으로 분리할 수 있는가?
- Identity·Security·Service 단계에서 권한과 service lifecycle을 운영 가능하게 설계할 수 있는가?
- 성능·운영 진단 단계에서 재현 가능한 incident report와 복구 runbook 작성할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **L1** | Process 실행 모델 | 5 | service 장애를 process 관점에서 진단 |
| **L2** | Filesystem과 I/O | 5 | 파일 이름부터 storage flush까지 경로 설명 |
| **L3** | Memory와 resource | 5 | memory 지표로 application과 kernel 원인 분리 |
| **L4** | Network stack | 5 | HTTP 오류를 name/network/transport/application 층으로 분리 |
| **L5** | Identity·Security·Service | 5 | 권한과 service lifecycle을 운영 가능하게 설계 |
| **L6** | 성능·운영 진단 | 5 | 재현 가능한 incident report와 복구 runbook 작성 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **L1-1** | process image와 exec | process image와 exec의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **L1-2** | PID·PPID·process tree | PID·PPID·process tree의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-1 |
| **L1-3** | process state와 /proc | process state와 /proc의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-2 |
| **L1-4** | signal delivery와 exit status | signal delivery와 exit status의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-3 |
| **L1-5** | thread·scheduler·context switch | thread·scheduler·context switch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-4 |
| **L2-1** | inode·dentry·hard/symbolic link | inode·dentry·hard/symbolic link의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L1-5 |
| **L2-2** | mount·filesystem·namespace | mount·filesystem·namespace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-1 |
| **L2-3** | file descriptor·open file description | file descriptor·open file description의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-2 |
| **L2-4** | pipe·redirection·blocking I/O | pipe·redirection·blocking I/O의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-3 |
| **L2-5** | buffering·page cache·fsync·atomic replace | buffering·page cache·fsync·atomic replace의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-4 |
| **L3-1** | virtual memory·page·mapping | virtual memory·page·mapping의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L2-5 |
| **L3-2** | stack·heap·mmap·shared memory | stack·heap·mmap·shared memory의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-1 |
| **L3-3** | RSS·PSS·cache·swap | RSS·PSS·cache·swap의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-2 |
| **L3-4** | overcommit·OOM killer | overcommit·OOM killer의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-3 |
| **L3-5** | rlimit·cgroup resource accounting | rlimit·cgroup resource accounting의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-4 |
| **L4-1** | interface·address·route | interface·address·route의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L3-5 |
| **L4-2** | neighbor·DNS resolution | neighbor·DNS resolution의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-1 |
| **L4-3** | socket·bind·listen·connect | socket·bind·listen·connect의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-2 |
| **L4-4** | TCP state·flow·timeout | TCP state·flow·timeout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-3 |
| **L4-5** | HTTP·TLS·proxy와 packet inspection | HTTP·TLS·proxy와 packet inspection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-4 |
| **L5-1** | user·group·process credential | user·group·process credential의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L4-5 |
| **L5-2** | permission·umask·ACL | permission·umask·ACL의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-1 |
| **L5-3** | sudo·capability·seccomp | sudo·capability·seccomp의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-2 |
| **L5-4** | systemd unit·dependency·journal | systemd unit·dependency·journal의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-3 |
| **L5-5** | service user·secret·graceful shutdown | service user·secret·graceful shutdown의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-4 |
| **L6-1** | CPU saturation·load average | CPU saturation·load average의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L5-5 |
| **L6-2** | memory pressure·leak | memory pressure·leak의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-1 |
| **L6-3** | disk latency·filesystem exhaustion | disk latency·filesystem exhaustion의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-2 |
| **L6-4** | fd·socket·network exhaustion | fd·socket·network exhaustion의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-3 |
| **L6-5** | strace·lsof·perf 관점의 종합 장애 대응 | strace·lsof·perf 관점의 종합 장애 대응의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | L6-4 |

## L1. Process 실행 모델

- 관찰 축: PID·task·procfs·signal·scheduler
- 통합 실습: parent/child/thread를 만들고 상태 전이 추적
- 핵심 실패: zombie·orphan·uninterruptible sleep·signal race

### [L1-1] process image와 exec

- 이해할 것: process image와 exec을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: PID·task·procfs·signal·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: parent/child/thread를 만들고 상태 전이 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: zombie·orphan·uninterruptible sleep·signal race 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L1-2] PID·PPID·process tree

- 이해할 것: PID·PPID·process tree을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: PID·task·procfs·signal·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: parent/child/thread를 만들고 상태 전이 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: zombie·orphan·uninterruptible sleep·signal race 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L1-3] process state와 /proc

- 이해할 것: process state와 /proc을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: PID·task·procfs·signal·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: parent/child/thread를 만들고 상태 전이 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: zombie·orphan·uninterruptible sleep·signal race 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L1-4] signal delivery와 exit status

- 이해할 것: signal delivery와 exit status을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: PID·task·procfs·signal·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: parent/child/thread를 만들고 상태 전이 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: zombie·orphan·uninterruptible sleep·signal race 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L1-5] thread·scheduler·context switch

- 이해할 것: thread·scheduler·context switch을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: PID·task·procfs·signal·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: parent/child/thread를 만들고 상태 전이 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: zombie·orphan·uninterruptible sleep·signal race 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L1 단계 결과물

- service 장애를 process 관점에서 진단.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## L2. Filesystem과 I/O

- 관찰 축: inode·dentry·mount·fd·VFS·page cache
- 통합 실습: link·rename·unlink·pipe·open file 실험
- 핵심 실패: disk full·inode full·deleted-open-file·partial I/O

### [L2-1] inode·dentry·hard/symbolic link

- 이해할 것: inode·dentry·hard/symbolic link을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: inode·dentry·mount·fd·VFS·page cache 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: link·rename·unlink·pipe·open file 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: disk full·inode full·deleted-open-file·partial I/O 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L2-2] mount·filesystem·namespace

- 이해할 것: mount·filesystem·namespace을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: inode·dentry·mount·fd·VFS·page cache 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: link·rename·unlink·pipe·open file 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: disk full·inode full·deleted-open-file·partial I/O 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L2-3] file descriptor·open file description

- 이해할 것: file descriptor·open file description을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: inode·dentry·mount·fd·VFS·page cache 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: link·rename·unlink·pipe·open file 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: disk full·inode full·deleted-open-file·partial I/O 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L2-4] pipe·redirection·blocking I/O

- 이해할 것: pipe·redirection·blocking I/O을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: inode·dentry·mount·fd·VFS·page cache 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: link·rename·unlink·pipe·open file 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: disk full·inode full·deleted-open-file·partial I/O 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L2-5] buffering·page cache·fsync·atomic replace

- 이해할 것: buffering·page cache·fsync·atomic replace을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: inode·dentry·mount·fd·VFS·page cache 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: link·rename·unlink·pipe·open file 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: disk full·inode full·deleted-open-file·partial I/O 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L2 단계 결과물

- 파일 이름부터 storage flush까지 경로 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## L3. Memory와 resource

- 관찰 축: virtual address·page table·RSS·swap·OOM·limit
- 통합 실습: mmap·allocation·leak·pressure 실험
- 핵심 실패: OOM kill·thrashing·overcommit·limit mismatch

### [L3-1] virtual memory·page·mapping

- 이해할 것: virtual memory·page·mapping을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: virtual address·page table·RSS·swap·OOM·limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: mmap·allocation·leak·pressure 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM kill·thrashing·overcommit·limit mismatch 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L3-2] stack·heap·mmap·shared memory

- 이해할 것: stack·heap·mmap·shared memory을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: virtual address·page table·RSS·swap·OOM·limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: mmap·allocation·leak·pressure 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM kill·thrashing·overcommit·limit mismatch 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L3-3] RSS·PSS·cache·swap

- 이해할 것: RSS·PSS·cache·swap을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: virtual address·page table·RSS·swap·OOM·limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: mmap·allocation·leak·pressure 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM kill·thrashing·overcommit·limit mismatch 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L3-4] overcommit·OOM killer

- 이해할 것: overcommit·OOM killer을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: virtual address·page table·RSS·swap·OOM·limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: mmap·allocation·leak·pressure 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM kill·thrashing·overcommit·limit mismatch 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L3-5] rlimit·cgroup resource accounting

- 이해할 것: rlimit·cgroup resource accounting을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: virtual address·page table·RSS·swap·OOM·limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: mmap·allocation·leak·pressure 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOM kill·thrashing·overcommit·limit mismatch 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L3 단계 결과물

- memory 지표로 application과 kernel 원인 분리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## L4. Network stack

- 관찰 축: interface·route·ARP/NDP·DNS·socket·TCP
- 통합 실습: namespace 안 server/client packet path 추적
- 핵심 실패: DNS delay·SYN timeout·reset·port exhaustion

### [L4-1] interface·address·route

- 이해할 것: interface·address·route을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: interface·route·ARP/NDP·DNS·socket·TCP 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace 안 server/client packet path 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: DNS delay·SYN timeout·reset·port exhaustion 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L4-2] neighbor·DNS resolution

- 이해할 것: neighbor·DNS resolution을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: interface·route·ARP/NDP·DNS·socket·TCP 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace 안 server/client packet path 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: DNS delay·SYN timeout·reset·port exhaustion 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L4-3] socket·bind·listen·connect

- 이해할 것: socket·bind·listen·connect을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: interface·route·ARP/NDP·DNS·socket·TCP 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace 안 server/client packet path 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: DNS delay·SYN timeout·reset·port exhaustion 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L4-4] TCP state·flow·timeout

- 이해할 것: TCP state·flow·timeout을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: interface·route·ARP/NDP·DNS·socket·TCP 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace 안 server/client packet path 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: DNS delay·SYN timeout·reset·port exhaustion 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L4-5] HTTP·TLS·proxy와 packet inspection

- 이해할 것: HTTP·TLS·proxy와 packet inspection을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: interface·route·ARP/NDP·DNS·socket·TCP 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: namespace 안 server/client packet path 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: DNS delay·SYN timeout·reset·port exhaustion 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L4 단계 결과물

- HTTP 오류를 name/network/transport/application 층으로 분리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## L5. Identity·Security·Service

- 관찰 축: credential·permission·ACL·capability·systemd
- 통합 실습: 최소 권한 daemon과 lifecycle 구성
- 핵심 실패: permission denied·secret leak·restart loop

### [L5-1] user·group·process credential

- 이해할 것: user·group·process credential을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: credential·permission·ACL·capability·systemd 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 최소 권한 daemon과 lifecycle 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: permission denied·secret leak·restart loop 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L5-2] permission·umask·ACL

- 이해할 것: permission·umask·ACL을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: credential·permission·ACL·capability·systemd 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 최소 권한 daemon과 lifecycle 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: permission denied·secret leak·restart loop 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L5-3] sudo·capability·seccomp

- 이해할 것: sudo·capability·seccomp을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: credential·permission·ACL·capability·systemd 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 최소 권한 daemon과 lifecycle 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: permission denied·secret leak·restart loop 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L5-4] systemd unit·dependency·journal

- 이해할 것: systemd unit·dependency·journal을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: credential·permission·ACL·capability·systemd 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 최소 권한 daemon과 lifecycle 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: permission denied·secret leak·restart loop 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L5-5] service user·secret·graceful shutdown

- 이해할 것: service user·secret·graceful shutdown을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: credential·permission·ACL·capability·systemd 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 최소 권한 daemon과 lifecycle 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: permission denied·secret leak·restart loop 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L5 단계 결과물

- 권한과 service lifecycle을 운영 가능하게 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## L6. 성능·운영 진단

- 관찰 축: load·CPU·memory·I/O·network·syscall evidence
- 통합 실습: 복합 장애를 주입하고 가설 순서로 triage
- 핵심 실패: 관측 도구 자체 부하와 잘못된 지표 해석

### [L6-1] CPU saturation·load average

- 이해할 것: CPU saturation·load average을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: load·CPU·memory·I/O·network·syscall evidence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 복합 장애를 주입하고 가설 순서로 triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 관측 도구 자체 부하와 잘못된 지표 해석 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L6-2] memory pressure·leak

- 이해할 것: memory pressure·leak을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: load·CPU·memory·I/O·network·syscall evidence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 복합 장애를 주입하고 가설 순서로 triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 관측 도구 자체 부하와 잘못된 지표 해석 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L6-3] disk latency·filesystem exhaustion

- 이해할 것: disk latency·filesystem exhaustion을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: load·CPU·memory·I/O·network·syscall evidence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 복합 장애를 주입하고 가설 순서로 triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 관측 도구 자체 부하와 잘못된 지표 해석 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L6-4] fd·socket·network exhaustion

- 이해할 것: fd·socket·network exhaustion을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: load·CPU·memory·I/O·network·syscall evidence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 복합 장애를 주입하고 가설 순서로 triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 관측 도구 자체 부하와 잘못된 지표 해석 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [L6-5] strace·lsof·perf 관점의 종합 장애 대응

- 이해할 것: strace·lsof·perf 관점의 종합 장애 대응을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: load·CPU·memory·I/O·network·syscall evidence 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 복합 장애를 주입하고 가설 순서로 triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 관측 도구 자체 부하와 잘못된 지표 해석 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### L6 단계 결과물

- 재현 가능한 incident report와 복구 runbook 작성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
