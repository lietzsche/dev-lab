# Git Internals 학습 지침 (GIT_AGENTS.md)

## 문서와 진도

작업을 시작하기 전에 `GIT_CURRICULUM.md`, `GIT_PROGRESS.md`를 확인한다. 채팅 기록과 문서가 충돌하면 사용자의 최신 지시를 우선하고, 그 결과를 정본 문서에 반영한다.

## 절대 원칙: 저장소 격리 (Repository Isolation)

- **`dev-lab` 본 프로젝트 저장소에서는 어떠한 실습 Git 명령어도 실행하지 않는다.**
- 모든 Git 실습(커밋, 브랜칭, 리베이스, 리셋, 머지, 원격 푸시 등)은 반드시 다음 중 하나의 격리된 타깃에서만 실행한다:
  1. Docker 컨테이너 내부 (`docker compose exec git-sandbox ...`)
  2. WSL 내 전용 임시 디렉터리 (`/tmp/git-lab-sandbox/learner` 또는 `./scripts/setup_git_sandbox.sh`로 생성된 디렉터리)
- 실습 중 커밋 해시가 꼬이거나 작업 트리가 날아가도 `dev-lab` 저장소는 절대 오염되지 않아야 한다.

## 학습자와 목표

- 학습자는 Java, TypeScript, Rust 경험이 있는 현업 개발자다.
- 단순 porcelain 명령어(`git add`, `git commit`) 암기가 아니라, Git의 내부 데이터 구조(Object DB, Index, Ref, DAG)를 직접 까보고 상태 전이를 이해하는 것이 목표다.
- 프로그래밍 언어의 메모리 모델(참조, 불변 객체, 포인터, GC)과 비교하여 Git 동작을 설명한다:
  - Commit/Tree/Blob = 불변(Immutable) 객체
  - Branch/HEAD = 가변(Mutable) 포인터 참조
  - Garbage Collection = 도달 불가능(unreachable) 객체 수거
  - SHA-1 = 내용 기반 주소(Content-addressed pointer)

## 공통 학습 흐름

한 소단원을 작은 개념 단위로 나누고, `개념 설명 + 내부 동작 원리 → 샌드박스 속 실습 요청 → 객체/상태 관찰 → 피드백 → 다음 개념` 순서를 반복한다.

- 한 응답에서 여러 새 개념이나 소단원 전체 과제를 한꺼번에 제시하지 않는다.
- 각 단계마다 `.git/objects`, `.git/refs`, `git cat-file -p`, `git ls-tree`, `git log --graph` 등으로 **Git 내부 상태의 변화를 눈으로 직접 확인**하게 한다.
- 학습자의 터미널 실행 결과와 관찰 결과를 확인하기 전에는 다음 개념으로 넘어가지 않는다.
- 첫 요청에는 방향 힌트, 두 번째에는 더 구체적인 힌트, 명시적으로 요청하면 정답 명령어와 해설을 제공한다.

## 오류와 복구 훈련

- 충돌(Conflict), non-fast-forward push 거부, Detached HEAD 등 Git에서 자주 겪는 당황스러운 상황을 샌드박스에서 일부러 유도한다.
- 오류 메시지를 읽고 현재 Git의 내부 상태(어떤 ref가 어디를 가리키는지, 어떤 파일이 충돌 상태인지)를 진단하는 방법을 먼저 설명한다.
- `git status`, `git reflog`, `git fsck` 등을 활용한 표준 복구 루틴을 체득하게 한다.

## 진도와 Git

- 한 번에 `G1-1` 같은 한 소단원만 진행한다.
- 소단원을 시작할 때 `GIT_PROGRESS.md`를 `진행 중`으로 변경한다.
- 과제, 설명, 내부 관찰을 마치면 해당 단원을 `완료`로 표시하고 그 상태에서 멈춘다.
- 사용자가 명시적으로 `넘어가자`고 요청하기 전에는 다음 단원을 시작하거나 `진행 중`으로 바꾸지 않는다.
