# Kubernetes Architecture & Operations 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **K1-1** | API resource·GVK·metadata | API resource·GVK·metadata의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **K1-2** | spec·status·generation·condition | spec·status·generation·condition의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-1 | 대기 | - |
| **K1-3** | API server·etcd·watch | API server·etcd·watch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-2 | 대기 | - |
| **K1-4** | controller reconciliation·owner reference | controller reconciliation·owner reference의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-3 | 대기 | - |
| **K1-5** | scheduler·binding·event | scheduler·binding·event의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-4 | 대기 | - |
| **K2-1** | Pod lifecycle·init·sidecar | Pod lifecycle·init·sidecar의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K1-5 | 대기 | - |
| **K2-2** | probe·restart·graceful termination | probe·restart·graceful termination의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-1 | 대기 | - |
| **K2-3** | ReplicaSet·Deployment rollout | ReplicaSet·Deployment rollout의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-2 | 대기 | - |
| **K2-4** | StatefulSet identity·ordering | StatefulSet identity·ordering의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-3 | 대기 | - |
| **K2-5** | Job·CronJob·completion·retry | Job·CronJob·completion·retry의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-4 | 대기 | - |
| **K3-1** | Pod network·CNI·kube-proxy | Pod network·CNI·kube-proxy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K2-5 | 대기 | - |
| **K3-2** | Service·EndpointSlice·session affinity | Service·EndpointSlice·session affinity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-1 | 대기 | - |
| **K3-3** | CoreDNS·service discovery | CoreDNS·service discovery의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-2 | 대기 | - |
| **K3-4** | Ingress·Gateway·TLS | Ingress·Gateway·TLS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-3 | 대기 | - |
| **K3-5** | NetworkPolicy·egress control | NetworkPolicy·egress control의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-4 | 대기 | - |
| **K4-1** | PV·PVC·StorageClass·CSI | PV·PVC·StorageClass·CSI의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K3-5 | 대기 | - |
| **K4-2** | Stateful data·snapshot·restore | Stateful data·snapshot·restore의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-1 | 대기 | - |
| **K4-3** | ConfigMap·Secret·reload | ConfigMap·Secret·reload의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-2 | 대기 | - |
| **K4-4** | ServiceAccount·RBAC·impersonation | ServiceAccount·RBAC·impersonation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-3 | 대기 | - |
| **K4-5** | securityContext·Pod Security·admission | securityContext·Pod Security·admission의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-4 | 대기 | - |
| **K5-1** | request·limit·QoS | request·limit·QoS의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K4-5 | 대기 | - |
| **K5-2** | node pressure·eviction | node pressure·eviction의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-1 | 대기 | - |
| **K5-3** | affinity·taint·topology spread | affinity·taint·topology spread의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-2 | 대기 | - |
| **K5-4** | HPA·VPA·cluster autoscaling | HPA·VPA·cluster autoscaling의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-3 | 대기 | - |
| **K5-5** | PDB·drain·high availability | PDB·drain·high availability의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-4 | 대기 | - |
| **K6-1** | Kustomize·Helm·configuration boundary | Kustomize·Helm·configuration boundary의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K5-5 | 대기 | - |
| **K6-2** | CI/CD·GitOps·image digest | CI/CD·GitOps·image digest의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-1 | 대기 | - |
| **K6-3** | metrics·logs·traces·events | metrics·logs·traces·events의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-2 | 대기 | - |
| **K6-4** | audit·security·cost visibility | audit·security·cost visibility의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-3 | 대기 | - |
| **K6-5** | cluster/application 종합 triage·rollback | cluster/application 종합 triage·rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | K6-4 | 대기 | - |

## 세부 기록

### K1-1. API resource·GVK·metadata

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K1-2. spec·status·generation·condition

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K1-3. API server·etcd·watch

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K1-4. controller reconciliation·owner reference

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K1-5. scheduler·binding·event

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K2-1. Pod lifecycle·init·sidecar

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K2-2. probe·restart·graceful termination

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K2-3. ReplicaSet·Deployment rollout

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K2-4. StatefulSet identity·ordering

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K2-5. Job·CronJob·completion·retry

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K3-1. Pod network·CNI·kube-proxy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K3-2. Service·EndpointSlice·session affinity

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K3-3. CoreDNS·service discovery

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K3-4. Ingress·Gateway·TLS

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K3-5. NetworkPolicy·egress control

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K4-1. PV·PVC·StorageClass·CSI

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K4-2. Stateful data·snapshot·restore

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K4-3. ConfigMap·Secret·reload

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K4-4. ServiceAccount·RBAC·impersonation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K4-5. securityContext·Pod Security·admission

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K5-1. request·limit·QoS

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K5-2. node pressure·eviction

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K5-3. affinity·taint·topology spread

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K5-4. HPA·VPA·cluster autoscaling

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K5-5. PDB·drain·high availability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K6-1. Kustomize·Helm·configuration boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K6-2. CI/CD·GitOps·image digest

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K6-3. metrics·logs·traces·events

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K6-4. audit·security·cost visibility

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### K6-5. cluster/application 종합 triage·rollback

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
