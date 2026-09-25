# Kubernetes Architecture & Operations 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- API와 control plane 단계에서 declarative reconciliation을 설명할 수 있는가?
- Workload lifecycle 단계에서 workload 종류별 lifecycle과 복구 선택할 수 있는가?
- Network와 traffic 단계에서 north-south/east-west traffic 진단할 수 있는가?
- Storage·Configuration·Security 단계에서 data와 권한 lifecycle 분리할 수 있는가?
- Resource·Availability·Scaling 단계에서 capacity와 availability tradeoff 판단할 수 있는가?
- Delivery·Observability·Incident 단계에서 commit부터 runtime까지 운영 증거 연결할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **K1** | API와 control plane | 5 | declarative reconciliation을 설명 |
| **K2** | Workload lifecycle | 5 | workload 종류별 lifecycle과 복구 선택 |
| **K3** | Network와 traffic | 5 | north-south/east-west traffic 진단 |
| **K4** | Storage·Configuration·Security | 5 | data와 권한 lifecycle 분리 |
| **K5** | Resource·Availability·Scaling | 5 | capacity와 availability tradeoff 판단 |
| **K6** | Delivery·Observability·Incident | 5 | commit부터 runtime까지 운영 증거 연결 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **K1-1** | API resource·GVK·metadata | API resource·GVK·metadata의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **K1-2** | spec·status·generation·condition | spec·status·generation·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-1 |
| **K1-3** | API server·etcd·watch | API server·etcd·watch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-2 |
| **K1-4** | controller reconciliation·owner reference | controller reconciliation·owner reference의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-3 |
| **K1-5** | scheduler·binding·event | scheduler·binding·event의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-4 |
| **K2-1** | Pod lifecycle·init·sidecar | Pod lifecycle·init·sidecar의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-5 |
| **K2-2** | probe·restart·graceful termination | probe·restart·graceful termination의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-1 |
| **K2-3** | ReplicaSet·Deployment rollout | ReplicaSet·Deployment rollout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-2 |
| **K2-4** | StatefulSet identity·ordering | StatefulSet identity·ordering의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-3 |
| **K2-5** | Job·CronJob·completion·retry | Job·CronJob·completion·retry의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-4 |
| **K3-1** | Pod network·CNI·kube-proxy | Pod network·CNI·kube-proxy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-5 |
| **K3-2** | Service·EndpointSlice·session affinity | Service·EndpointSlice·session affinity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-1 |
| **K3-3** | CoreDNS·service discovery | CoreDNS·service discovery의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-2 |
| **K3-4** | Ingress·Gateway·TLS | Ingress·Gateway·TLS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-3 |
| **K3-5** | NetworkPolicy·egress control | NetworkPolicy·egress control의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-4 |
| **K4-1** | PV·PVC·StorageClass·CSI | PV·PVC·StorageClass·CSI의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-5 |
| **K4-2** | Stateful data·snapshot·restore | Stateful data·snapshot·restore의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-1 |
| **K4-3** | ConfigMap·Secret·reload | ConfigMap·Secret·reload의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-2 |
| **K4-4** | ServiceAccount·RBAC·impersonation | ServiceAccount·RBAC·impersonation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-3 |
| **K4-5** | securityContext·Pod Security·admission | securityContext·Pod Security·admission의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-4 |
| **K5-1** | request·limit·QoS | request·limit·QoS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-5 |
| **K5-2** | node pressure·eviction | node pressure·eviction의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-1 |
| **K5-3** | affinity·taint·topology spread | affinity·taint·topology spread의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-2 |
| **K5-4** | HPA·VPA·cluster autoscaling | HPA·VPA·cluster autoscaling의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-3 |
| **K5-5** | PDB·drain·high availability | PDB·drain·high availability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-4 |
| **K6-1** | Kustomize·Helm·configuration boundary | Kustomize·Helm·configuration boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-5 |
| **K6-2** | CI/CD·GitOps·image digest | CI/CD·GitOps·image digest의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-1 |
| **K6-3** | metrics·logs·traces·events | metrics·logs·traces·events의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-2 |
| **K6-4** | audit·security·cost visibility | audit·security·cost visibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-3 |
| **K6-5** | cluster/application 종합 triage·rollback | cluster/application 종합 triage·rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-4 |

## K1. API와 control plane

- 관찰 축: API machinery·etcd·watch·controller·scheduler
- 통합 실습: object 생성 후 spec/status/event/watch 추적
- 핵심 실패: stale cache·conflict·finalizer stuck

### [K1-1] API resource·GVK·metadata

- 이해할 것: API resource·GVK·metadata을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: API machinery·etcd·watch·controller·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: object 생성 후 spec/status/event/watch 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale cache·conflict·finalizer stuck 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K1-2] spec·status·generation·condition

- 이해할 것: spec·status·generation·condition을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: API machinery·etcd·watch·controller·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: object 생성 후 spec/status/event/watch 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale cache·conflict·finalizer stuck 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K1-3] API server·etcd·watch

- 이해할 것: API server·etcd·watch을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: API machinery·etcd·watch·controller·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: object 생성 후 spec/status/event/watch 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale cache·conflict·finalizer stuck 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K1-4] controller reconciliation·owner reference

- 이해할 것: controller reconciliation·owner reference을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: API machinery·etcd·watch·controller·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: object 생성 후 spec/status/event/watch 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale cache·conflict·finalizer stuck 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K1-5] scheduler·binding·event

- 이해할 것: scheduler·binding·event을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: API machinery·etcd·watch·controller·scheduler 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: object 생성 후 spec/status/event/watch 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale cache·conflict·finalizer stuck 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K1 단계 결과물

- declarative reconciliation을 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## K2. Workload lifecycle

- 관찰 축: Pod sandbox·container state·ReplicaSet·revision·Job
- 통합 실습: crash·rollout·batch retry 관찰
- 핵심 실패: CrashLoop·ImagePull·stuck termination·duplicate Job

### [K2-1] Pod lifecycle·init·sidecar

- 이해할 것: Pod lifecycle·init·sidecar을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Pod sandbox·container state·ReplicaSet·revision·Job 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash·rollout·batch retry 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: CrashLoop·ImagePull·stuck termination·duplicate Job 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K2-2] probe·restart·graceful termination

- 이해할 것: probe·restart·graceful termination을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Pod sandbox·container state·ReplicaSet·revision·Job 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash·rollout·batch retry 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: CrashLoop·ImagePull·stuck termination·duplicate Job 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K2-3] ReplicaSet·Deployment rollout

- 이해할 것: ReplicaSet·Deployment rollout을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Pod sandbox·container state·ReplicaSet·revision·Job 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash·rollout·batch retry 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: CrashLoop·ImagePull·stuck termination·duplicate Job 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K2-4] StatefulSet identity·ordering

- 이해할 것: StatefulSet identity·ordering을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Pod sandbox·container state·ReplicaSet·revision·Job 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash·rollout·batch retry 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: CrashLoop·ImagePull·stuck termination·duplicate Job 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K2-5] Job·CronJob·completion·retry

- 이해할 것: Job·CronJob·completion·retry을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: Pod sandbox·container state·ReplicaSet·revision·Job 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: crash·rollout·batch retry 관찰에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: CrashLoop·ImagePull·stuck termination·duplicate Job 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K2 단계 결과물

- workload 종류별 lifecycle과 복구 선택.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## K3. Network와 traffic

- 관찰 축: CNI·Service·EndpointSlice·DNS·Ingress/Gateway
- 통합 실습: request가 Pod까지 가는 hop 추적
- 핵심 실패: selector mismatch·DNS·policy·TLS 장애

### [K3-1] Pod network·CNI·kube-proxy

- 이해할 것: Pod network·CNI·kube-proxy을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CNI·Service·EndpointSlice·DNS·Ingress/Gateway 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: request가 Pod까지 가는 hop 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: selector mismatch·DNS·policy·TLS 장애 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K3-2] Service·EndpointSlice·session affinity

- 이해할 것: Service·EndpointSlice·session affinity을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CNI·Service·EndpointSlice·DNS·Ingress/Gateway 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: request가 Pod까지 가는 hop 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: selector mismatch·DNS·policy·TLS 장애 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K3-3] CoreDNS·service discovery

- 이해할 것: CoreDNS·service discovery을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CNI·Service·EndpointSlice·DNS·Ingress/Gateway 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: request가 Pod까지 가는 hop 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: selector mismatch·DNS·policy·TLS 장애 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K3-4] Ingress·Gateway·TLS

- 이해할 것: Ingress·Gateway·TLS을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CNI·Service·EndpointSlice·DNS·Ingress/Gateway 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: request가 Pod까지 가는 hop 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: selector mismatch·DNS·policy·TLS 장애 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K3-5] NetworkPolicy·egress control

- 이해할 것: NetworkPolicy·egress control을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CNI·Service·EndpointSlice·DNS·Ingress/Gateway 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: request가 Pod까지 가는 hop 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: selector mismatch·DNS·policy·TLS 장애 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K3 단계 결과물

- north-south/east-west traffic 진단.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## K4. Storage·Configuration·Security

- 관찰 축: CSI·PV/PVC·config projection·identity·admission
- 통합 실습: stateful app과 최소 권한 account 구성
- 핵심 실패: mount·permission·secret rotation·RBAC deny

### [K4-1] PV·PVC·StorageClass·CSI

- 이해할 것: PV·PVC·StorageClass·CSI을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CSI·PV/PVC·config projection·identity·admission 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: stateful app과 최소 권한 account 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mount·permission·secret rotation·RBAC deny 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K4-2] Stateful data·snapshot·restore

- 이해할 것: Stateful data·snapshot·restore을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CSI·PV/PVC·config projection·identity·admission 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: stateful app과 최소 권한 account 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mount·permission·secret rotation·RBAC deny 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K4-3] ConfigMap·Secret·reload

- 이해할 것: ConfigMap·Secret·reload을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CSI·PV/PVC·config projection·identity·admission 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: stateful app과 최소 권한 account 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mount·permission·secret rotation·RBAC deny 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K4-4] ServiceAccount·RBAC·impersonation

- 이해할 것: ServiceAccount·RBAC·impersonation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CSI·PV/PVC·config projection·identity·admission 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: stateful app과 최소 권한 account 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mount·permission·secret rotation·RBAC deny 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K4-5] securityContext·Pod Security·admission

- 이해할 것: securityContext·Pod Security·admission을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: CSI·PV/PVC·config projection·identity·admission 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: stateful app과 최소 권한 account 구성에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: mount·permission·secret rotation·RBAC deny 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K4 단계 결과물

- data와 권한 lifecycle 분리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## K5. Resource·Availability·Scaling

- 관찰 축: request/limit·QoS·affinity·autoscaler·disruption
- 통합 실습: pressure·reschedule·scale·drain 실험
- 핵심 실패: OOMKilled·throttle·Pending·eviction·PDB deadlock

### [K5-1] request·limit·QoS

- 이해할 것: request·limit·QoS을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: request/limit·QoS·affinity·autoscaler·disruption 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: pressure·reschedule·scale·drain 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOMKilled·throttle·Pending·eviction·PDB deadlock 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K5-2] node pressure·eviction

- 이해할 것: node pressure·eviction을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: request/limit·QoS·affinity·autoscaler·disruption 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: pressure·reschedule·scale·drain 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOMKilled·throttle·Pending·eviction·PDB deadlock 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K5-3] affinity·taint·topology spread

- 이해할 것: affinity·taint·topology spread을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: request/limit·QoS·affinity·autoscaler·disruption 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: pressure·reschedule·scale·drain 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOMKilled·throttle·Pending·eviction·PDB deadlock 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K5-4] HPA·VPA·cluster autoscaling

- 이해할 것: HPA·VPA·cluster autoscaling을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: request/limit·QoS·affinity·autoscaler·disruption 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: pressure·reschedule·scale·drain 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOMKilled·throttle·Pending·eviction·PDB deadlock 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K5-5] PDB·drain·high availability

- 이해할 것: PDB·drain·high availability을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: request/limit·QoS·affinity·autoscaler·disruption 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: pressure·reschedule·scale·drain 실험에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: OOMKilled·throttle·Pending·eviction·PDB deadlock 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K5 단계 결과물

- capacity와 availability tradeoff 판단.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## K6. Delivery·Observability·Incident

- 관찰 축: manifest render·revision·audit·metric/log/trace
- 통합 실습: bad release와 복합 장애를 time line으로 복구
- 핵심 실패: config drift·image mismatch·silent partial failure

### [K6-1] Kustomize·Helm·configuration boundary

- 이해할 것: Kustomize·Helm·configuration boundary을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: manifest render·revision·audit·metric/log/trace 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bad release와 복합 장애를 time line으로 복구에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: config drift·image mismatch·silent partial failure 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K6-2] CI/CD·GitOps·image digest

- 이해할 것: CI/CD·GitOps·image digest을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: manifest render·revision·audit·metric/log/trace 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bad release와 복합 장애를 time line으로 복구에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: config drift·image mismatch·silent partial failure 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K6-3] metrics·logs·traces·events

- 이해할 것: metrics·logs·traces·events을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: manifest render·revision·audit·metric/log/trace 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bad release와 복합 장애를 time line으로 복구에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: config drift·image mismatch·silent partial failure 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K6-4] audit·security·cost visibility

- 이해할 것: audit·security·cost visibility을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: manifest render·revision·audit·metric/log/trace 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bad release와 복합 장애를 time line으로 복구에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: config drift·image mismatch·silent partial failure 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [K6-5] cluster/application 종합 triage·rollback

- 이해할 것: cluster/application 종합 triage·rollback을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: manifest render·revision·audit·metric/log/trace 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: bad release와 복합 장애를 time line으로 복구에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: config drift·image mismatch·silent partial failure 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### K6 단계 결과물

- commit부터 runtime까지 운영 증거 연결.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
