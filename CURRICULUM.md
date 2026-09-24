# Git Internals & Workflows 커리큘럼

## 학습 철학

- Git은 단순한 '버전 관리 CLI 툴'이 아니라, **불변 객체(Immutable Object) 기반의 내용 주소화 저장소(Content-Addressed Storage)**이자 **방향성 비순환 그래프(DAG, Directed Acyclic Graph)**입니다.
- 단순 문법 암기(`add`, `commit`, `push`)를 넘어서, 명령어 실행 시 `.git` 디렉터리 내부에서 객체와 참조가 어떻게 생성되고 포인터가 어떻게 전이되는지 직접 관찰합니다.
- 본 프로젝트(`dev-lab`)의 작업 트리를 보호하기 위해, 모든 파괴적·실험적 실습은 **독립된 샌드박스(Docker 컨테이너 또는 `/tmp/git-lab-sandbox`)**에서 격리 수행합니다.

---

## 단계 요약

| 단계 | 소단원 | 핵심 내용 | 비고 |
| :--- | :--- | :--- | :--- |
| **G1** | Git의 객체 모델과 Plumbing | `blob`, `tree`, `commit`, `tag`, SHA-1/256, zlib 압축, `hash-object`, `cat-file`, `write-tree`, `commit-tree` | 저수준 명령어로 첫 커밋 조립 |
| **G2** | 참조와 3대 영역 상태 전이 | Working Directory, Index(Staging), HEAD, `refs/heads`, `refs/tags`, `update-ref`, `symbolic-ref`, `switch`/`restore` | 상태 전이와 stat 캐시 |
| **G3** | DAG 순회와 브랜치 병합 | Commit DAG, 부모 포인터, Fast-Forward vs 3-way Merge, 충돌 마커 원리, `cherry-pick`, `revert` | 분기점 탐색과 머지 메커니즘 |
| **G4** | Rebase와 히스토리 재작성 | Rebase의 본질(커밋 재생과 새 SHA 생성), `rebase -i`, squash, fixup, reword, 충돌 해결 흐름, Golden Rule | 선형 히스토리 구축 |
| **G5** | 원격 저장소와 분산 협업 모델 | Bare repository, Remote tracking branch(`origin/*`), `fetch` vs `pull`, upstream 설정, non-fast-forward push와 `--force-with-lease` | 멀티 유저 동시 작업 시뮬레이션 |
| **G6** | 사고 복구와 내부 유지보수 | Detached HEAD 원리와 구출, `reflog` 시간 여행, Dangling commit 구출, `fsck`, `gc`와 packfile 최적화 | 망가진 Git 살려내기 |

---

## 상세 커리큘럼

### G1. Git의 객체 모델과 저수준(Plumbing) 명령어
- **G1-1. Content-Addressed Storage와 4대 불변 객체**
  - Git 객체 4형제: `blob` (내용), `tree` (디렉터리 구조 및 파일명 메타데이터), `commit` (스냅샷 메타데이터), `tag` (annotated tag)
  - 객체 헤더 포맷: `"{type} {length}\0{content}"`와 SHA-1 해시 계산
  - zlib 압축과 `.git/objects/xx/yyyy...` 샤딩 디렉터리 구조
  - `git hash-object -w`, `git cat-file -t`, `git cat-file -p`, `git cat-file -s`로 객체 직접 덤프
- **G1-2. Plumbing 명령어로 커밋 수작업 조립하기**
  - 고수준 `git add`, `git commit`을 전혀 쓰지 않고 커밋 생성하기
  - 파일 해싱 -> `blob` 생성 -> 인덱스 조작(`git update-index`) -> `git write-tree`로 `tree` 객체 생성
  - `git commit-tree`로 트리를 가리키는 `commit` 객체 생성 (Author, Committer, Commit message, Timestamp)
  - 부모 커밋(`-p parent_hash`)을 지정해 2번째 커밋 수동 연결하고 `git log`로 DAG 검증하기

### G2. 참조(References)와 3대 영역 상태 전이
- **G2-1. Git의 3대 영역 (Working Tree, Index, HEAD)**
  - Working Tree(작업 폴더), Staging Area(인덱스 바이너리 파일 `.git/index`), Repository(객체 DB + 커밋)
  - `git status`가 파일의 `mtime`, `size` stat 캐시와 SHA-1을 비교하여 변경을 감지하는 메커니즘
  - 변경 취소와 복구: 레거시 `git checkout`에서 `git switch`(브랜치 이동)와 `git restore`(작업/인덱스 복원)로의 분리 이유
- **G2-2. References와 심볼릭 참조 (Refs & HEAD)**
  - 브랜치(Branch)의 본질: `.git/refs/heads/<name>` 파일에 적힌 40자리 커밋 해시 포인터에 불과함
  - 태그(Lightweight tag vs Annotated tag): 단순 참조 파일 vs 서명/메시지를 가진 태그 객체
  - `HEAD`의 본질: 현재 작업 브랜치를 가리키는 심볼릭 참조 (`.git/HEAD` -> `ref: refs/heads/main`)
  - 저수준 명령어: `git update-ref`, `git symbolic-ref`로 브랜치 생성 및 이동 관찰

### G3. DAG 순회와 브랜치 병합
- **G3-1. Commit DAG(방향성 비순환 그래프)와 Revision 표기법**
  - 커밋 노드의 단방향 부모 링크: 자식이 부모를 참조하며, 부모는 자식을 모른다.
  - `git log --graph --oneline --all`의 토폴로지 해석
  - Revision 문법: `HEAD~` (부모), `HEAD^2` (머지 커밋의 두 번째 부모), `HEAD@{2}` (reflog 기준)
  - 커밋 범위 비교: `main..feature` (도달 가능 집합 차이) vs `main...feature` (대칭 차집합)
- **G3-2. Fast-Forward Merge vs 3-way Merge**
  - Fast-forward: 공통 조상(Base)에서 한쪽만 진전되었을 때 단순히 브랜치 포인터만 전진
  - 3-way Merge: 세 지점(Our HEAD, Their Branch, Common Ancestor/Merge Base)을 비교하여 새 머지 커밋 노드 생성
  - `git merge-base` 명령어로 공통 조상 찾기
  - 충돌(Conflict) 발생 원리와 Git 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 구조 분석
- **G3-3. Cherry-Pick과 Revert의 원리**
  - `git cherry-pick`: 특정 커밋의 diff(패치)를 현재 HEAD 위에 적용하고 새로운 SHA-1 커밋 생성
  - `git revert`: 이전 커밋의 변경 사항을 정확히 반대로 뒤집는(inverse diff) 새로운 커밋 생성 (히스토리 보존)

### G4. Rebase와 히스토리 재작성
- **G4-1. Rebase의 내부 메커니즘**
  - Rebase = 분기점(Base)을 최신 upstream으로 옮겨 커밋들을 순차적으로 임시 영역에 보관 후 Replay
  - 원본 커밋이 수정되는 것이 아니라, 새로운 내용/부모를 가진 **새로운 커밋 객체(신규 SHA-1)**가 생성됨
  - Merge 히스토리(비선형, 보존형) vs Rebase 히스토리(선형, 가독성형)의 장단점 비교
- **G4-2. Interactive Rebase (`git rebase -i`)**
  - todo 리스트의 동작: `pick`, `reword`, `edit`, `squash`, `fixup`, `drop`
  - 커밋 메시지 수정, 여러 커밋 하나로 합치기, 특정 커밋 쪼개기 실습
  - Rebase 중 충돌 발생 시 내부 상태 (`.git/rebase-merge/`)와 해결 흐름 (`--continue`, `--abort`, `--skip`)
- **G4-3. Git의 황금률 (Golden Rule of Rebasing)**
  - "이미 공개된(원격에 푸시된) 브랜치는 절대 Rebase하지 않는다"의 컴퓨터 과학적 이유
  - 협업자의 로컬 DAG와 원격 DAG가 어긋났을 때 발생하는 중복 커밋과 병합 지옥 체험

### G5. 원격 저장소와 분산 협업 모델
- **G5-1. Bare Repository와 Remote Tracking References**
  - 작업 트리 없는 순수 객체 저장소: `git init --bare`의 구조와 원격 중앙 서버의 동작
  - Remote Tracking Branch: `.git/refs/remotes/origin/*` (원격 서버의 스냅샷 로컬 캐시)
  - `git remote -v`, `git remote add`
- **G5-2. 동기화 프로토콜: Fetch, Merge, Pull**
  - `git fetch`: 원격의 누락된 객체들을 로컬로 전송받고 `origin/*` 참조만 갱신 (로컬 작업 트리 변경 없음)
  - `git merge origin/main`: 로컬 `main`에 `origin/main` 병합
  - `git pull` = `fetch` + `merge` (또는 `git pull --rebase` = `fetch` + `rebase`)
  - Tracking branch 연결: `git push -u origin <branch>` (`--set-upstream`)의 설정 파일(`config`) 영향
- **G5-3. 동시성 충돌과 Push 정책**
  - 두 개발자(Alice, Bob)가 동일 브랜치에 동시에 push할 때의 non-fast-forward 거부
  - 거부당했을 때의 표준 해결 패턴: `pull --rebase` 후 재push
  - `git push --force`의 위험성과 대안 `git push --force-with-lease`의 원자적(CAS) 검증 원리

### G6. 사고 복구와 내부 유지보수
- **G6-1. Detached HEAD 상태의 진실과 탈출**
  - HEAD가 브랜치 이름이 아닌 특정 커밋 SHA-1을 직접 가리키는 상태
  - Detached 상태에서 커밋 후 다른 브랜치로 전환하면 커밋이 유실되는 원리 (참조 부재)
  - 유실되기 전 새 브랜치를 생성하여 영구 보존하는 방법
- **G6-2. Reflog: Git의 최후 안전망**
  - `.git/logs/`에 기록되는 HEAD 및 브랜치 포인터의 모든 변경 이력
  - `git reset --hard`나 브랜치 강제 삭제(`git branch -D`)로 증발한 커밋을 `git reflog`로 찾아 복구하기
  - `git checkout HEAD@{1}`, `git branch rescue-branch <lost-hash>`
- **G6-3. Dangling Objects와 가비지 컬렉션 (GC)**
  - 어떤 참조(브랜치, 태그, reflog)에서도 도달할 수 없는 고아 객체(Dangling commit/blob)
  - `git fsck --lost-found`: 참조가 끊긴 고아 객체 검사
  - `git gc` (Garbage Collection): 느슨한 객체(loose objects)들을 묶어 압축 팩파일(`pack-*.pack`, `pack-*.idx`)로 변환하고 고아 객체 영구 정리
