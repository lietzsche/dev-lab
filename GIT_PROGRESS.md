# Git Internals & Workflows 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행합니다.
- 소단원을 시작할 때 상태를 `진행 중`으로 변경합니다.
- 모든 실습은 본 저장소(`dev-lab`)가 아닌 **Docker 샌드박스** 또는 **격리 디렉터리(`/tmp/git-lab-sandbox`)**에서 수행합니다.
- 과제, 내부 객체 관찰, 복구 검증을 마치면 상태를 `완료`로 변경합니다.
- 사용자가 명시적으로 `넘어가자`고 요청하기 전에는 다음 단원으로 넘어가지 않습니다.

---

## 소단원별 현황

| 단계 | 소단원 | 목표 | 선행 조건 | 상태 | 완료일 | 비고 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G1-1** | 객체 모델과 4대 불변 객체 | `blob`, `tree`, `commit`, `tag`, zlib, SHA-1 해시 포맷 관찰 | - | 대기 | - | 저수준 객체 구조 |
| **G1-2** | Plumbing 커밋 조립 | `hash-object`, `write-tree`, `commit-tree`로 첫 커밋 수작업 생성 | G1-1 | 대기 | - | 고수준 명령 없이 커밋 생성 |
| **G2-1** | Git의 3대 영역 상태 전이 | Working Tree, Index, HEAD 상호작용 및 `switch`/`restore` | G1-2 | 대기 | - | 인덱스와 상태 머신 |
| **G2-2** | References와 심볼릭 참조 | `.git/refs/heads/*`, `HEAD`, `update-ref`, `symbolic-ref` | G2-1 | 대기 | - | 브랜치는 포인터다 |
| **G3-1** | Commit DAG와 Revision 표기법 | 부모 포인터, `log --graph`, `HEAD~`, `HEAD^`, `main..feature` | G2-2 | 대기 | - | 그래프 토폴로지 해석 |
| **G3-2** | Fast-Forward vs 3-way Merge | 공통 조상 탐색(`merge-base`), 3자 병합, 충돌 마커 원리 | G3-1 | 대기 | - | 충돌 해결 메커니즘 |
| **G3-3** | Cherry-Pick과 Revert | 특정 패치 적용과 역패치(Inverse diff) 커밋 생성 | G3-2 | 대기 | - | 선택적 커밋 적용 |
| **G4-1** | Rebase의 내부 메커니즘 | Base 재배치와 신규 커밋 객체 생성(Replay) 관찰 | G3-3 | 대기 | - | 선형 히스토리의 본질 |
| **G4-2** | Interactive Rebase | `rebase -i`, squash, fixup, reword, 충돌 중단/계속 | G4-1 | 대기 | - | 커밋 정리와 다듬기 |
| **G4-3** | Git의 황금률 (Golden Rule) | 공유 브랜치 Rebase 금지 이유, 원격 DAG 어긋남 체험 | G4-2 | 대기 | - | 협업 안전 규칙 |
| **G5-1** | Bare 저장소와 원격 추적 참조 | `git init --bare`, `refs/remotes/origin/*`, 원격 저장소 구조 | G4-3 | 대기 | - | 중앙 서버 모델 |
| **G5-2** | Fetch, Merge, Pull 프로토콜 | 원격 객체 전송, `pull` vs `pull --rebase`, upstream 연결 | G5-1 | 대기 | - | 분산 저장소 동기화 |
| **G5-3** | 동시성 충돌과 Push 정책 | Non-fast-forward 거부, 협업자 충돌 해결, `--force-with-lease` | G5-2 | 대기 | - | 안전한 강제 푸시 |
| **G6-1** | Detached HEAD와 복구 | HEAD 분리 상태의 실체, 고아 커밋 방지 및 브랜치 구출 | G5-3 | 대기 | - | 포인터 이탈 복구 |
| **G6-2** | Reflog: 시간 여행 | `.git/logs/`, `reset --hard` 및 삭제 브랜치 완전 복구 | G6-1 | 대기 | - | 최후의 안전망 |
| **G6-3** | Dangling Objects와 가비지 컬렉션 | 고아 객체 검사(`fsck`), `gc`와 packfile 압축 최적화 | G6-2 | 대기 | - | 내부 청소와 최적화 |

---

## 단계별 세부 기록

### G1. Git의 객체 모델과 저수준(Plumbing) 명령어
- **G1-1. 객체 모델과 4대 불변 객체**
  - 계획:
  - 배운 점:
- **G1-2. Plumbing 커밋 조립**
  - 계획:
  - 배운 점:

### G2. 참조(References)와 3대 영역 상태 전이
- **G2-1. Git의 3대 영역 (Working Tree, Index, HEAD)**
  - 계획:
  - 배운 점:
- **G2-2. References와 심볼릭 참조 (Refs & HEAD)**
  - 계획:
  - 배운 점:

### G3. DAG 순회와 브랜치 병합
- **G3-1. Commit DAG와 Revision 표기법**
  - 계획:
  - 배운 점:
- **G3-2. Fast-Forward vs 3-way Merge**
  - 계획:
  - 배운 점:
- **G3-3. Cherry-Pick과 Revert**
  - 계획:
  - 배운 점:

### G4. Rebase와 히스토리 재작성
- **G4-1. Rebase의 내부 메커니즘**
  - 계획:
  - 배운 점:
- **G4-2. Interactive Rebase**
  - 계획:
  - 배운 점:
- **G4-3. Git의 황금률 (Golden Rule)**
  - 계획:
  - 배운 점:

### G5. 원격 저장소와 분산 협업 모델
- **G5-1. Bare 저장소와 원격 추적 참조**
  - 계획:
  - 배운 점:
- **G5-2. Fetch, Merge, Pull 프로토콜**
  - 계획:
  - 배운 점:
- **G5-3. 동시성 충돌과 Push 정책**
  - 계획:
  - 배운 점:

### G6. 사고 복구와 내부 유지보수
- **G6-1. Detached HEAD와 복구**
  - 계획:
  - 배운 점:
- **G6-2. Reflog: 시간 여행**
  - 계획:
  - 배운 점:
- **G6-3. Dangling Objects와 가비지 컬렉션**
  - 계획:
  - 배운 점:
