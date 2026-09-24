# Git Internals Lab

Git의 내부 객체 모델(Content-Addressed Storage, Merkle DAG)과 분산 협업 워크플로우를 깊이 있게 체득하는 독립 학습 저장소입니다.

단순한 명령어 문법 암기(`add`, `commit`, `push`)를 넘어서, Git이 내부 파일시스템(`.git`)에서 객체를 어떻게 생성하고, 포인터를 어떻게 이동시키며, 충돌과 분기를 어떻게 계산하는지 직접 확인합니다.

---

## 💡 학습 철학

1. **내용 주소화 불변 저장소 (Content-Addressed Storage)**
   - Git의 `blob`, `tree`, `commit`, `tag`는 내용(Content)의 해시값으로 주소가 지정되는 불변(Immutable) 객체입니다.
   - 객체는 한 번 쓰여지면 절대 수정되지 않으며, 수정은 언제나 '새로운 객체 생성'으로 표현됩니다.
2. **방향성 비순환 그래프 (DAG, Directed Acyclic Graph)**
   - 히스토리는 커밋 객체들이 부모 커밋을 단방향으로 참조하는 그래프입니다.
   - 브랜치와 `HEAD`는 특정 커밋 노드를 가리키는 단순한 '가변 포인터(참조)'에 불과합니다.
3. **저장소 격리 절대 원칙 (Repository Isolation)**
   - 학습 중 파괴적인 실험(`reset --hard`, `rebase -i`, 브랜치 강제 삭제, 객체 손상 등)을 자유롭게 수행할 수 있도록, **모든 실습은 독립된 샌드박스(Docker 컨테이너 또는 로컬 임시 디렉터리)에서 진행**합니다.

---

## 🚀 빠른 시작 (Quick Start)

실습 환경은 **Docker 컨테이너** 또는 **로컬 OS/WSL 디렉터리** 중 원하는 방식으로 구성할 수 있습니다.

### 방법 A. Docker 환경 (권장: 완전 격리)

```bash
# 1. 샌드박스 컨테이너 빌드 및 백그라운드 실행
docker compose -f docker/docker-compose.yml up -d --build

# 2. 샌드박스 컨테이너 쉘 진입
docker compose -f docker/docker-compose.yml exec git-sandbox bash

# 3. 컨테이너 내부에서 실습 진행 (/workspace/learner)
cd /workspace/learner
git status
```

실습을 마치거나 초기화할 때:
```bash
docker compose -f docker/docker-compose.yml down -v
```

---

### 방법 B. 로컬 OS/WSL 환경 (경량: 즉시 실행)

Docker 데몬 없이 로컬 파일시스템의 격리 디렉터리(기본값: `/tmp/git-lab-sandbox`)를 사용합니다:

```bash
# 1. 샌드박스 초기화 (중앙 베어 저장소 + alice + bob + learner 자동 구성)
./scripts/setup_sandbox.sh init

# 2. 학습자 작업 디렉터리로 이동하여 실습 시작
cd /tmp/git-lab-sandbox/learner

# 3. 객체 분석 및 샌드박스 관리 (상대 경로로 언제든 실행 가능)
python3 ../inspect_object.py <hash>   # Git 객체 구조 분석
../sandbox.sh status                  # 각 작업 공간 상태 확인
../sandbox.sh reset                   # 샌드박스 초기 깨끗한 상태로 리셋
```

> 💡 **팁**: 샌드박스 경로를 변경하고 싶다면 `GIT_SANDBOX_DIR` 환경 변수를 지정할 수 있습니다:
> ```bash
> export GIT_SANDBOX_DIR=./sandbox
> ./scripts/setup_sandbox.sh init
> ```

---

## 🛠️ 제공 도구

- **`scripts/setup_sandbox.sh`**: 중앙 베어 저장소(`remote.git`)와 동료 작업자(`alice`, `bob`), 학습자(`learner`) 작업 공간을 자동으로 구성하고 리셋합니다.
- **`scripts/inspect_object.py`**: Git의 `.git/objects/xx/yy...` 바이너리 파일을 직접 읽어 zlib 압축을 풀고, 객체 타입(`blob`, `tree`, `commit`), 선언 크기, SHA-1 해시, 파싱된 내용을 덤프해 주는 분석 도구입니다.

```bash
# Git 객체 직접 까보기 예시
python3 scripts/inspect_object.py <40자리_해시_또는_파일경로>
```

---

## 📚 문서 안내

- **[`CURRICULUM.md`](./CURRICULUM.md)**: G1(객체 모델과 Plumbing)부터 G6(사고 복구와 GC)까지의 6단계 상세 로드맵
- **[`PROGRESS.md`](./PROGRESS.md)**: 소단원별 실습 현황 및 점검 기록
- **[`AGENTS.md`](./AGENTS.md)**: AI 페어 프로그래밍 시 지켜야 할 원칙과 학습 흐름 지침 (Claude Code, Google Antigravity 등 공통 표준)
