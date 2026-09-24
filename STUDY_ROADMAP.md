# Engineering Study Roadmap

## 목적

이 문서는 과목별 장기 브랜치의 순서와 선택 기준을 관리하는 저장소 전체의 정본이다.
각 브랜치는 독립된 학습 과정이며 서로 병합하지 않는다. 학습 중 우선순위나 범위를
바꾸고 싶을 때는 이 문서를 먼저 수정하고 해당 과목 브랜치의 커리큘럼에 반영한다.

## 학습자 기준

- Java/Spring 기반의 5년 차 백엔드 개발자
- Python, Databricks, 데이터 파이프라인, LLM workflow 실무로 역할 확장 중
- Git, Docker, Kubernetes, JavaScript/TypeScript를 사용해 본 경험이 있음
- 문법 암기보다 내부 모델, 장애 분석, 운영과 설계 판단을 강화하는 것이 목표

## 설계 원칙

1. 언어 수집보다 현재 업무에서 반복되는 문제를 설명하는 기반 개념을 우선한다.
2. 한 과목은 18개 안팎의 소단원으로 제한하고 한 번에 한 소단원만 진행한다.
3. 각 소단원은 설명, 최소 실습, 내부 상태 관찰, 장애 또는 반례, 완료 검증을 포함한다.
4. 도구 사용법보다 프로세스, 상태, 경계, 불변식과 실패 복구를 먼저 이해한다.
5. 새 과목을 시작하기 전 직전 과목을 완료하고 회고한 뒤 이 문서의 우선순위를 재검토한다.
6. 과목 브랜치는 장기 브랜치이며 다른 과목 브랜치나 main으로 병합하지 않는다.

## 권장 순서

| 순서 | 브랜치 | 역할 | 시작 조건 | 완료 후 판단 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `main` | Python을 실무 주언어로 정착 | 현재 진행 과정 | 비동기·테스트·패키징·운영 경계를 설명하고 구현 |
| 2 | `learn/git-internals` | 버전·참조·DAG·복구 모델 | Python 과정 완료 | Linux로 이동 |
| 3 | `learn/linux-internals` | 프로세스·I/O·네트워크·격리 | Git 과정 완료 | 컨테이너 원리를 배울 준비 확인 |
| 4 | `learn/containers` | image·namespace·cgroup·runtime | Linux 과정 완료 | Kubernetes 필요성 재평가 |
| 5 | `learn/kubernetes` | 선언적 상태·스케줄링·운영 | 컨테이너 과정 완료 | 플랫폼 또는 데이터/AI 심화 선택 |
| 6 | `learn/distributed-systems` | 동시성·일관성·재시도·메시징 | 네트워크와 컨테이너 이해 | 데이터 파이프라인과 서비스 설계에 적용 |
| 7 | `learn/data-pipelines` | 증분 처리·멱등성·backfill·lineage | 분산 시스템 기초 완료 | LLM workflow의 데이터 신뢰성 확보 |
| 8 | `learn/llm-systems` | 평가·추적·비용·agent reliability | Python과 데이터 파이프라인 완료 | 현재 AI 업무에 직접 적용 |

## 선택 트랙

| 브랜치 | 선택하는 조건 | 우선순위 |
| :--- | :--- | :--- |
| `learn/typescript` | Agent UI, Playwright 플랫폼, Node 자동화 도구를 만들 때 | 필요 시 5~8 사이에 삽입 |
| `learn/jvm-spring-internals` | JVM 장애 분석과 Spring 운영 설계를 강화할 때 | 상시 병행하지 않고 집중 과정으로 수행 |
| `learn/rust` | 고성능 CLI, 실행 sandbox, native extension 등 명확한 결과물이 있을 때 | 핵심 로드맵 이후 |

## 단계별 연결

```text
Python
  └─ 실행 모델, 타입, 비동기, 테스트, 서비스 경계
       ↓
Git
  └─ 불변 객체, 가변 참조, DAG, 복구
       ↓
Linux
  └─ 프로세스, 파일, 메모리, 네트워크
       ↓
Containers
  └─ namespace, cgroup, image, runtime
       ↓
Kubernetes
  └─ desired state, controller, scheduling, operations
       ↓
Distributed Systems
  └─ concurrency, consistency, messaging, failure
       ↓
Data Pipelines
  └─ incremental processing, idempotency, lineage
       ↓
LLM Systems
  └─ evaluation, tracing, tool/agent reliability
```

Java/Spring은 분산 시스템의 API·transaction 실습 구현체로, Python은 데이터·LLM
worker 구현체로 계속 사용한다. TypeScript는 운영·승인 UI와 자동화 도구가 필요할 때
추가한다. Rust는 시스템 수준 성능이나 격리 문제가 실제 요구로 나타날 때 시작한다.

## 공통 품질 기준

과목 브랜치의 초기 설정은 아래 조건을 모두 만족해야 한다.

- README에 대상, 학습 목표, 선수지식, 실행 방법과 완료 기준이 있다.
- CURRICULUM에 선후 관계가 있는 소단원과 각 단원의 관찰 대상·실습·검증이 있다.
- PROGRESS의 모든 소단원이 CURRICULUM과 일치하며 처음에는 `대기` 상태다.
- AGENTS에 한 소단원 진행 규칙, 사용자 출력 확인, 힌트 단계, 안전·격리 규칙이 있다.
- `scripts/check.sh`가 문서 존재, 단원 ID 일치, 진행 상태와 경로 이식성을 검사한다.
- 특정 머신의 사용자 홈이나 드라이브 경로를 문서와 스크립트에 하드코딩하지 않는다.
- 실습이 호스트나 다른 과목 브랜치의 데이터를 변경할 수 있으면 격리 방법을 명시한다.
- 현재 학습 전에는 의존성을 강제로 설치하지 않으며 필요한 도구와 버전만 README에 적는다.

## 검토 루프

각 브랜치를 만들거나 크게 수정할 때 다음 루프를 적용한다.

1. 구조 검토: 공통 파일, 단원 수, ID와 선행 조건을 검사한다.
2. 내용 검토: 학습자 경력과 중복되는 입문 내용을 줄이고 내부 원리와 운영 문제를 강화한다.
3. 실습 검토: 각 단원이 명령 실행으로 끝나지 않고 상태 관찰과 실패 진단을 포함하는지 본다.
4. 안전 검토: 삭제, 권한, 네트워크, 클러스터 실습의 대상과 복구 방법을 확인한다.
5. 자동 검사: 해당 브랜치의 `./scripts/check.sh`와 `git diff --check`를 통과시킨다.
6. 수정 후 1~5를 다시 수행하고 모든 기준을 만족할 때만 커밋·푸시한다.

## 로드맵 변경 규칙

- 업무가 바뀌거나 실제 문제가 생기면 선택 트랙을 핵심 순서 사이에 삽입할 수 있다.
- 과목 시작 전에는 목표와 결과물을 다시 검토하고 불필요한 단원은 제거한다.
- 이미 진행 중인 과목의 범위를 바꾸면 PROGRESS에 변경 이유를 기록한다.
- 새 과목을 추가할 때는 `learn/<subject>` 이름을 사용하고 이 문서에 먼저 등록한다.
- 학습 결과를 하나의 제품으로 합치고 싶다면 과목 브랜치를 병합하지 않고 별도 프로젝트
  저장소를 만든다.
