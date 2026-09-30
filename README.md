# Bash & Shell Internals Lab

Bash 문법을 외우는 데서 끝나지 않고, 명령 한 줄이 parsing·expansion·process·file
descriptor·exit status로 이어지는 과정을 직접 관찰하는 독립 학습 브랜치입니다.

이 과정은 [STUDY_ROADMAP.md](STUDY_ROADMAP.md)의 공통 기반 과정입니다. `B1~B2`는
Git 실습 전에 필요한 command·argv·quoting·expansion 체크포인트이고, `B3~B5`는
Linux·container·CI/CD 전에 필요한 운영 기반입니다. `B6`는 운영 CLI가 실제 결과물로
필요할 때 진행합니다. 과목 브랜치는 서로 병합하지 않습니다.

## 과정 목표

- 명령, 인자, quoting, expansion이 `argv`로 변환되는 과정을 설명한다.
- stdin·stdout·stderr와 redirection·pipeline을 file descriptor 관점에서 설명한다.
- process·subshell·job·signal·trap의 상태와 실패를 진단한다.
- 안전하고 테스트 가능한 운영 자동화 CLI를 Bash로 작성한다.
- Bash, POSIX `sh`, Python 등 다른 도구를 선택해야 하는 경계를 판단한다.

## 로드맵 체크포인트

- **B1~B2 — Git 진입 기반:** Git 자체를 배우는 과정이 아니라 shell 해석과 Git 오류를 구분할 최소 기반입니다.
- **B3~B5 — 운영 기반:** Git과 병행하거나 이후에 진행하며 Linux·container·CI/CD로 이어집니다.
- **B6 — 선택 결과물:** 반복 운영 작업을 Bash CLI로 만들 이유가 있을 때 진행합니다.

Bash 전체 완료는 Git 시작 조건이 아닙니다. 현재 완료한 단원은 그대로 보존하며 B2 완료 뒤
Python 학습으로 복귀하는 것이 기본 경로입니다.

## 학습 방식

```text
개념 하나와 최소 예제
  → 결과 예측
  → 격리 샌드박스에서 실행
  → process·FD·환경·종료 상태 관찰
  → 실패 재현과 복구
  → PROGRESS.md에 증거 기록
```

한 번에 `B1-1` 같은 한 소단원만 진행하며, 사용자가 명시적으로 `넘어가자`고 하기
전에는 다음 소단원을 시작하지 않습니다.

## 빠른 시작

프로젝트 루트에서 로컬 샌드박스를 만듭니다.

```bash
./scripts/setup_sandbox.sh init
cd "${BASH_SANDBOX_DIR:-/tmp/bash-lab-sandbox}/workspace"
../sandbox.sh status
```

샌드박스를 초기 상태로 되돌리려면 다음을 실행합니다.

```bash
../sandbox.sh reset
```

완전히 삭제하려면 프로젝트 루트에서 실행합니다.

```bash
./scripts/setup_sandbox.sh clean
```

Docker를 선호하면 다음을 사용합니다.

```bash
docker compose -f docker/docker-compose.yml up -d --build
docker compose -f docker/docker-compose.yml exec bash-sandbox bash
```

## 안전 경계

- 모든 파괴적 실습은 `/tmp/bash-lab-sandbox` 또는 Docker 내부에서만 수행합니다.
- 본 저장소 루트에서는 `rm`, 권한 변경, process 종료, redirection 덮어쓰기 실습을 하지 않습니다.
- sandbox 도구는 marker 파일이 있는 자신이 만든 디렉터리만 reset·clean합니다.
- `sudo`, 실제 secret, 운영 서버, 개인 설정 파일은 실습에 사용하지 않습니다.

## 도구

- `scripts/setup_sandbox.sh`: 안전 marker를 사용하는 샌드박스 lifecycle 도구
- `scripts/inspect_context.sh`: argv, PID/PPID, 환경, FD, 종료 상태 관찰 도구
- `scripts/check.sh`: 문서 구조, Bash 문법, 이식성, sandbox lifecycle 검사
- Docker: Bash 5 기반의 선택적 완전 격리 환경

## 문서

- `CURRICULUM.md`: 6단계 24소단원의 선후 관계와 완료 기준
- `PROGRESS.md`: 현재 학습 위치와 관찰 증거
- `AGENTS.md`: AI 페어 학습 규칙과 안전 원칙

## 검증

```bash
./scripts/check.sh
```

필수 검사에는 문서·단원 ID 일치, `bash -n`, 절대 경로 하드코딩 탐지, sandbox의
init/status/reset/clean 안전성 검증이 포함됩니다. `shellcheck`가 설치돼 있으면 정적 분석도
함께 수행합니다.
