# Kubernetes Architecture & Operations 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`, 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **K1-1** | API object | API object의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - | 대기 | - |
| **K1-2** | control plane·etcd | control plane·etcd의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-1 | 대기 | - |
| **K1-3** | owner·reconciliation | owner·reconciliation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-2 | 대기 | - |
| **K2-1** | Pod lifecycle | Pod lifecycle의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K1-3 | 대기 | - |
| **K2-2** | Deployment rollout | Deployment rollout의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-1 | 대기 | - |
| **K2-3** | Job·CronJob | Job·CronJob의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-2 | 대기 | - |
| **K3-1** | Service·EndpointSlice | Service·EndpointSlice의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K2-3 | 대기 | - |
| **K3-2** | Ingress·TLS | Ingress·TLS의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-1 | 대기 | - |
| **K3-3** | PV·PVC | PV·PVC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-2 | 대기 | - |
| **K4-1** | ConfigMap·Secret | ConfigMap·Secret의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K3-3 | 대기 | - |
| **K4-2** | ServiceAccount·RBAC | ServiceAccount·RBAC의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-1 | 대기 | - |
| **K4-3** | request·limit·scheduling | request·limit·scheduling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-2 | 대기 | - |
| **K5-1** | probe·shutdown | probe·shutdown의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K4-3 | 대기 | - |
| **K5-2** | metrics·logs·traces | metrics·logs·traces의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-1 | 대기 | - |
| **K5-3** | HPA·PDB | HPA·PDB의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-2 | 대기 | - |
| **K6-1** | Helm·Kustomize | Helm·Kustomize의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K5-3 | 대기 | - |
| **K6-2** | GitOps·rollback | GitOps·rollback의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K6-1 | 대기 | - |
| **K6-3** | 종합 triage | 종합 triage의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | K6-2 | 대기 | - |

## 세부 기록

### K1-1. API object

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K1-2. control plane·etcd

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K1-3. owner·reconciliation

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K2-1. Pod lifecycle

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K2-2. Deployment rollout

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K2-3. Job·CronJob

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K3-1. Service·EndpointSlice

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K3-2. Ingress·TLS

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K3-3. PV·PVC

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K4-1. ConfigMap·Secret

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K4-2. ServiceAccount·RBAC

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K4-3. request·limit·scheduling

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K5-1. probe·shutdown

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K5-2. metrics·logs·traces

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K5-3. HPA·PDB

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K6-1. Helm·Kustomize

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K6-2. GitOps·rollback

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:

### K6-3. 종합 triage

- 계획:
- 관찰:
- 실패와 복구:
- 배운 점:
