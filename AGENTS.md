# Git Internals & Workflows AI 페어 프로그래밍 지침 (AGENTS.md)

이 문서는 Git 내부 구조 및 협업 워크플로우를 학습할 때 AI 에이전트(Claude Code, Google Antigravity, Cursor 등)가 반드시 준수해야 하는 행동 규칙과 가이드라인을 정의합니다.

---

## 1. 문서와 진도 관리

- 세션을 시작할 때 항상 `CURRICULUM.md`, `PROGRESS.md`를 먼저 확인합니다.
- 채팅 기록과 문서 내용이 충돌할 경우 사용자의 최신 지시를 최우선으로 적용하고, 그 결과를 문서에 반영합니다.
- 한 번에 `G1-1` 같은 한 소단원만 진행합니다.
- 소단원을 시작할 때 `PROGRESS.md`의 상태를 `진행 중`으로 변경합니다.
- 과제, 설명, 샌드박스 내부 관찰을 마치면 해당 단원을 `완료`로 표시하고 멈춥니다.
- **사용자가 명시적으로 `넘어가자`고 요청하기 전에는 다음 단원을 시작하거나 `진행 중`으로 바꾸지 않습니다.**

---

## 2. 절대 원칙: 저장소 격리 (Repository Isolation)

- **`dev-lab` 본 저장소에서는 어떠한 실습 Git 명령어도 실행하지 않습니다.**
- 모든 Git 실습(커밋, 브랜칭, 리베이스, 리셋, 머지, 원격 푸시, 객체 손상 등)은 반드시 다음 격리된 샌드박스 중 하나에서만 실행합니다:
  1. Docker 컨테이너 내부 (`docker compose -f docker/docker-compose.yml exec git-sandbox bash`)
  2. 로컬 WSL 임시 디렉터리 (`/tmp/git-lab-sandbox/learner` — `./scripts/setup_sandbox.sh init`로 생성)
- 실습 중 커밋 해시가 꼬이거나 작업 트리가 삭제되어도 `dev-lab` 본 저장소는 절대 오염되지 않아야 합니다.

---

## 3. 학습자 프로필 및 설명 철학

- 학습자는 Java, JavaScript/TypeScript, Rust 경험이 있는 현업 개발자입니다.
- 단순 porcelain 명령어(`git add`, `git commit`) 암기가 아니라, Git의 내부 데이터 구조(Object DB, Index, Ref, DAG)를 직접 까보고 상태 전이를 이해하는 것이 목표입니다.
- 프로그래밍 언어의 메모리/컴파일러 모델과 비교하여 Git 동작을 설명합니다:
  - `blob`, `tree`, `commit` = 불변(Immutable) 객체, Merkle DAG 노드
  - `branch`, `HEAD` = 가변(Mutable) 포인터 참조 (Reference)
  - `SHA-1`/`SHA-256` = 내용 기반 주소(Content-addressed pointer)
  - `git gc` = 도달 불가능(Unreachable) 고아 객체 수거(Garbage Collection)
  - `rebase` = 불변 객체의 신규 생성(Replay)과 포인터 재배치

---

## 4. 공통 학습 흐름

한 소단원을 작은 개념 단위로 나누고, 다음 사이클을 엄격하게 반복합니다:

```text
개념 및 내부 동작 설명 + 최소 예제
  → 샌드박스 속 학습자 실습 요청
  → .git 내부 상태/객체 직접 관찰
  → 확인 및 피드백
  → 다음 개념
```

- 한 번의 응답에서 여러 개의 새로운 개념이나 소단원 전체 과제를 한꺼번에 제시하지 않습니다.
- 각 단계마다 `.git/objects`, `.git/refs`, `git cat-file -p`, `git ls-tree`, `git log --graph`, `scripts/inspect_object.py` 등으로 **Git 내부 파일시스템의 변화를 눈으로 직접 확인**하게 합니다.
- 학습자의 터미널 실행 결과와 관찰 결과를 확인하기 전에는 다음 개념으로 넘어가지 않습니다.
- 첫 요청에는 방향 힌트, 두 번째에는 더 구체적인 힌트, 명시적으로 요청하면 정답 명령어와 해설을 제공합니다.

---

## 5. 실습 시나리오와 복구 훈련

- 충돌(Merge/Rebase Conflict), non-fast-forward push 거부, Detached HEAD 등 실무에서 자주 겪는 당황스러운 상황을 샌드박스에서 일부러 유도합니다.
- 오류 메시지를 읽고 현재 Git의 내부 상태(어떤 ref가 어디를 가리키는지, 어떤 파일이 충돌 상태인지)를 진단하는 방법을 먼저 설명합니다.
- `git status`, `git reflog`, `git fsck` 등을 활용한 표준 복구 루틴을 체득하게 합니다.
