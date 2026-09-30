# Engineering Study Roadmap

## 목적

이 문서는 과목별 장기 브랜치의 순서와 선택 기준을 관리하는 저장소 전체의 정본이다.
각 브랜치는 독립된 학습 과정이며 서로 병합하지 않는다. 순서는 모든 과목을 끝까지 직렬로
수강하라는 뜻이 아니라, 공통 기반을 확보한 뒤 실제 업무와 채용 방향에 따라 다음 투자를
결정하기 위한 체크포인트다.

## 학습자 기준

- Java/Spring 기반의 5년 차 백엔드 개발자
- Python, Databricks, 데이터 파이프라인, LLM workflow 실무로 역할 확장 중
- Git, Docker, Kubernetes, JavaScript/TypeScript를 사용해 본 경험이 있음
- 다음 역할은 AI 또는 Java 백엔드가 유력하지만 아직 확정되지 않음
- 문법 암기보다 내부 모델, 장애 분석, 운영과 설계 판단을 강화하는 것이 목표

## 이번 재설계의 결론

Bash 전체는 Git의 선수 과정이 아니다. Bash는 명령줄을 parsing하고 process를 실행하는
shell이고, Git은 객체 저장소와 commit graph를 관리하는 별도 프로그램이다. Git 명령을
입력할 때 Bash를 사용하지만 Git의 blob·tree·commit·ref·DAG는 Bash의 고급 문법에
의존하지 않는다.

Git 전에 필요한 Bash 범위는 `B1~B2`다. 여기서 command·argv·exit status·PATH와
quoting·variable·expansion을 익히면 Git 실습 명령이 왜 다르게 실행됐는지 구분할 수 있다.
`B3~B5`의 FD·process·signal·안전한 script는 Linux, container, CI/CD와 운영 자동화의
선수 기반이다. `B6`는 운영 CLI를 실제로 만들 필요가 생겼을 때 선택한다.

Git도 취업을 위한 명령어 과정으로 보지 않는다. 이미 pull·push·PR/MR을 사용할 수 있는
학습자에게 Git 과정의 가치는 immutable object, content identity, mutable reference,
DAG, replay, reachability와 recovery를 실제 저장소에서 검증하는 데 있다. 이 모델은 데이터
lineage, build cache, event history, 배포 artifact와 분산 시스템을 이해하는 데 재사용된다.

## 설계 원칙

1. 언어 수집보다 현재 업무에서 반복되는 문제를 설명하는 기반 개념을 우선한다.
2. 모든 과목을 완주한 뒤 진로를 선택하지 않고, 체크포인트마다 다음 과목의 기대효과를 다시 평가한다.
3. 소단원 수를 미리 고정하지 않고 예측·관찰·실패·복구할 수 있는 개념 경계로 나눈다.
4. 도구 사용법보다 process, state, boundary, invariant와 실패 복구를 먼저 이해한다.
5. 진행 중인 과목의 완료 기록은 보존하고, 범위가 달라지면 중단이 아니라 체크포인트 도달로 기록한다.
6. 과목 브랜치는 장기 브랜치이며 다른 과목 브랜치나 main으로 병합하지 않는다.

## 현재 권장 경로

| 구간 | 브랜치·범위 | 얻을 역량 | 다음 결정 |
| :--- | :--- | :--- | :--- |
| 1 | `learn/bash` B1~B2 | 명령 실행과 shell 해석 오류를 Git 오류와 구분 | B2 완료 후 Python으로 복귀 |
| 2 | `main` 남은 과정 | AI 업무에 쓸 Python 구현·테스트·서비스 역량 완성 | Python 결과물과 부족한 역량 점검 |
| 3 | `learn/git-internals` G1~G3 | 객체·ref·index·DAG·merge를 상태 모델로 설명 | G4~G6 즉시 심화 여부 결정 |
| 4 | 진로 공통 실전 | 작은 결과물 하나에 Python·Git 모델 적용 | AI 또는 Java 우선 트랙 선택 |

Git G1~G3은 내부 모델 체크포인트다. history rewrite, 원격 협업 정책, bisect·reflog·gc가
현재 문제 해결에 중요하거나 개념을 끝까지 연결하고 싶다면 G4~G6을 이어서 완료한다.
채용 준비의 병목이 포트폴리오나 특정 직무 역량이라면 해당 트랙을 먼저 진행하고 돌아온다.

## 진로별 우선 트랙

### AI·데이터 역할

```text
Python 완료
  → Data Pipelines
  → LLM Systems
  → 필요 범위의 Distributed Systems
  → 배포 요구가 생기면 Linux → Containers → Kubernetes
```

- `learn/data-pipelines`: 증분 처리, idempotency, backfill, lineage로 데이터 신뢰성을 다룬다.
- `learn/llm-systems`: evaluation, tracing, 비용, tool/agent reliability를 결과물로 만든다.
- Java/Spring은 API나 transaction 경계가 필요한 실습 구현체로 계속 활용한다.

### Java 백엔드 역할

```text
JVM/Spring Internals
  → Distributed Systems
  → Linux 운영 기반
  → Containers
  → 채용 공고나 업무가 요구하면 Kubernetes
```

- `learn/jvm-spring-internals`: JVM 장애 분석, Spring lifecycle, transaction·observability를 강화한다.
- `learn/distributed-systems`: timeout, retry, idempotency, consistency, messaging을 서비스 설계와 연결한다.
- 이미 가진 Java 경력은 입문 문법보다 장애 분석과 운영 증거로 확장한다.

## Bash와 Git의 재진입 지점

| 체크포인트 | 필수 여부 | 시작 또는 재개 조건 |
| :--- | :---: | :--- |
| Bash B1~B2 | 공통 기반 | Git·CLI 실습 전에 완료 |
| Git G1~G3 | 권장 기반 | Python 완료 후 객체·DAG 모델을 확보할 때 |
| Git G4~G6 | 선택 심화 | rewrite·협업 정책·복구를 체계화할 필요가 있을 때 |
| Bash B3~B5 | 운영 기반 | Linux, container, CI/CD 자동화 전에 완료 |
| Bash B6 | 결과물 선택 | 반복 운영 작업을 CLI로 제품화할 때 |

Bash와 Git은 서로를 전부 끝내야 시작할 수 있는 관계가 아니다. Git 실습 중 필요한 간단한
redirection이나 pipeline은 해당 시점에 최소 설명으로 사용하고, Bash B3에서 process와 FD
모델로 다시 깊게 검증한다.

## 나머지 선택 과목

| 브랜치 | 선택하는 조건 |
| :--- | :--- |
| `learn/linux-internals` | 운영 장애, process·I/O·network·filesystem을 진단해야 할 때 |
| `learn/containers` | image·namespace·cgroup·runtime을 설명하고 디버깅해야 할 때 |
| `learn/kubernetes` | 실제 지원 직무나 배포 환경에서 cluster 운영을 요구할 때 |
| `learn/typescript` | Agent UI, Playwright 플랫폼, Node 자동화 도구를 만들 때 |
| `learn/rust` | 고성능 CLI, sandbox, native extension이라는 명확한 결과물이 있을 때 |

## 공통 품질 기준

과목 브랜치의 초기 설정과 큰 수정은 다음을 만족해야 한다.

- README에 대상, 학습 목표, 선수지식, 실행 방법과 완료 기준이 있다.
- CURRICULUM은 역량 목표에서 역산하며 선후 관계, 관찰 대상, 실습, 실패와 검증이 있다.
- PROGRESS의 모든 소단원이 CURRICULUM과 일치하고 실제 완료 기록을 보존한다.
- AGENTS에 한 소단원 진행, 사용자 출력 확인, 힌트 단계, 안전·격리 규칙이 있다.
- `scripts/check.sh`가 문서 존재, 단원 ID, 진행 상태와 경로 이식성을 검사한다.
- 특정 머신 경로를 하드코딩하지 않고 위험한 실습의 격리와 복구 경계를 명시한다.

## 커리큘럼 품질 게이트

커리큘럼 신규 작성과 큰 수정은 아래 10점 기준에서 9점 이상이고 치명적 실패가 없어야 한다.

| 기준 | 점수 | 확인 질문 |
| :--- | ---: | :--- |
| 범위 완결성 | 2 | 목표 역량에 필요한 핵심 영역과 통합 결과물이 있는가? |
| 선수 관계 | 2 | 각 단원이 앞선 개념을 실제 전제로 사용하며 순서가 설명 가능한가? |
| 관찰 가능한 실습 | 2 | 내부 상태·로그·metadata를 직접 확인하는가? |
| 실패와 복구 | 2 | 대표 실패를 재현하고 남은 상태를 진단·복구하는가? |
| 자동 검증 | 1 | ID, 진도, 문서 구조와 이식성을 script가 검사하는가? |
| 학습자 적합성 | 1 | 이미 아는 입문은 압축하고 업무·채용 방향에 연결하는가? |

다음 중 하나라도 있으면 점수와 무관하게 수정한다.

- 뒤 단계의 추상화를 선수지식 없이 먼저 다룬다.
- 실습 성공만 확인하고 실패 상태나 복구 방법이 없다.
- 위험한 실습의 격리, 삭제, 비용, 권한 경계가 불명확하다.
- CURRICULUM, PROGRESS, README, 검사 기준이 서로 다르다.
- 단원 수를 맞추려고 개념을 억지로 합치거나 쪼갠다.
- 모든 과목을 직렬 완주하게 해 목표 직무의 결과물 제작을 불필요하게 늦춘다.

## 검토 루프

1. 구조·선수 관계와 현재 진도를 확인한다.
2. 학습자의 경력, 실제 업무, 목표 직무에 주는 한계효용을 검토한다.
3. 각 단원의 상태 관찰, 실패 진단, 복구와 결과물을 확인한다.
4. 안전·격리·이식성 및 자동 검사를 확인한다.
5. 수정 후 `./scripts/check.sh`와 `git diff --check`를 실행한다.
6. 9점 이상이고 치명적 실패가 없을 때만 커밋·푸시한다.

## 로드맵 변경 규칙

- 체크포인트에 도달하면 최근 채용 공고, 면접 피드백, 실제 업무를 근거로 다음 과목을 고른다.
- 이미 진행 중인 과목의 범위를 바꾸면 완료 기록을 유지하고 변경 이유를 PROGRESS에 남긴다.
- 새 과목은 `learn/<subject>` 브랜치로 만들고 이 문서에 등록한다.
- 학습 결과를 하나의 제품으로 합칠 때는 과목 브랜치를 병합하지 않고 별도 프로젝트를 만든다.
