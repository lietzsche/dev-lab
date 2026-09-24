# Kubernetes Architecture & Operations 커리큘럼

## 목적

controller가 desired state를 조정하는 구조와 운영을 이해한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Containers 완료 권장
- 최종 실습: API·worker rollout·관측·RBAC 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **K1** | API와 제어 루프 | spec·status·event·etcd | reconciliation 관찰 |
| **K2** | Workload | Pod·ReplicaSet·revision | failure·rollout 유도 |
| **K3** | Network·Storage | Service·DNS·PV/PVC | 연결·volume 장애 |
| **K4** | 설정·보안·배치 | ConfigMap·RBAC·scheduler | 최소 권한과 pending |
| **K5** | 신뢰성·관측 | probe·metric·log·trace | pressure·drain 재현 |
| **K6** | 배포·대응 | diff·history·audit | release 장애 복구 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **K1-1** | API object | API object의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **K1-2** | control plane·etcd | control plane·etcd의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-1 |
| **K1-3** | owner·reconciliation | owner·reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-2 |
| **K2-1** | Pod lifecycle | Pod lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-3 |
| **K2-2** | Deployment rollout | Deployment rollout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-1 |
| **K2-3** | Job·CronJob | Job·CronJob의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-2 |
| **K3-1** | Service·EndpointSlice | Service·EndpointSlice의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-3 |
| **K3-2** | Ingress·TLS | Ingress·TLS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-1 |
| **K3-3** | PV·PVC | PV·PVC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-2 |
| **K4-1** | ConfigMap·Secret | ConfigMap·Secret의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-3 |
| **K4-2** | ServiceAccount·RBAC | ServiceAccount·RBAC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-1 |
| **K4-3** | request·limit·scheduling | request·limit·scheduling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-2 |
| **K5-1** | probe·shutdown | probe·shutdown의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-3 |
| **K5-2** | metrics·logs·traces | metrics·logs·traces의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-1 |
| **K5-3** | HPA·PDB | HPA·PDB의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-2 |
| **K6-1** | Helm·Kustomize | Helm·Kustomize의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-3 |
| **K6-2** | GitOps·rollback | GitOps·rollback의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K6-1 |
| **K6-3** | 종합 triage | 종합 triage의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K6-2 |

## 상세 커리큘럼

### [K1-1] API object

- 목표: API object의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: spec·status·event·etcd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: reconciliation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K1-2] control plane·etcd

- 목표: control plane·etcd의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: spec·status·event·etcd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: reconciliation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K1-3] owner·reconciliation

- 목표: owner·reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: spec·status·event·etcd를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: reconciliation 관찰 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K2-1] Pod lifecycle

- 목표: Pod lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Pod·ReplicaSet·revision를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: failure·rollout 유도 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K2-2] Deployment rollout

- 목표: Deployment rollout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Pod·ReplicaSet·revision를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: failure·rollout 유도 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K2-3] Job·CronJob

- 목표: Job·CronJob의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Pod·ReplicaSet·revision를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: failure·rollout 유도 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K3-1] Service·EndpointSlice

- 목표: Service·EndpointSlice의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Service·DNS·PV/PVC를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 연결·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K3-2] Ingress·TLS

- 목표: Ingress·TLS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Service·DNS·PV/PVC를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 연결·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K3-3] PV·PVC

- 목표: PV·PVC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: Service·DNS·PV/PVC를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 연결·volume 장애 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K4-1] ConfigMap·Secret

- 목표: ConfigMap·Secret의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ConfigMap·RBAC·scheduler를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한과 pending 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K4-2] ServiceAccount·RBAC

- 목표: ServiceAccount·RBAC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ConfigMap·RBAC·scheduler를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한과 pending 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K4-3] request·limit·scheduling

- 목표: request·limit·scheduling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: ConfigMap·RBAC·scheduler를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 최소 권한과 pending 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K5-1] probe·shutdown

- 목표: probe·shutdown의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: probe·metric·log·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: pressure·drain 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K5-2] metrics·logs·traces

- 목표: metrics·logs·traces의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: probe·metric·log·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: pressure·drain 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K5-3] HPA·PDB

- 목표: HPA·PDB의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: probe·metric·log·trace를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: pressure·drain 재현 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K6-1] Helm·Kustomize

- 목표: Helm·Kustomize의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: diff·history·audit를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: release 장애 복구 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K6-2] GitOps·rollback

- 목표: GitOps·rollback의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: diff·history·audit를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: release 장애 복구 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [K6-3] 종합 triage

- 목표: 종합 triage의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: diff·history·audit를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: release 장애 복구 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
