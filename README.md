# WSL 기반 CLI 생산성 마스터리 (CLI Mastery)

Windows 11 + WSL2 Ubuntu 환경에서 작업하는 Java/Spring 개발자를 위한 **실습 중심 Linux CLI & 생산성 훈련 프로젝트**입니다.

마우스 사용을 최소화하고, 로컬 터미널과 실제 Linux 서버 환경에서 손이 먼저 움직이는 수준으로 명령어를 체득하는 것을 목표로 합니다.

---

## 1. 프로젝트 구조

```text
.
├── AGENTS.md                 # AI 튜터(Codex) 운영 및 코칭 규칙
├── README.md                 # 학습 시작 방법 및 전체 안내
├── curriculum/               # Level 1 ~ Level 7 단계별 실습 가이드
│   ├── level-01.md           # Level 1. Bash와 터미널 조작
│   ├── level-02.md           # Level 2. 파일 검색과 텍스트 처리
│   ├── level-03.md           # Level 3. 프로세스와 시스템 관리
│   ├── level-04.md           # Level 4. 네트워크와 서버 작업
│   ├── level-05.md           # Level 5. Bash 생산성 도구
│   ├── level-06.md           # Level 6. Windows + WSL 통합
│   └── level-07.md           # Level 7. 실전 개발 워크플로
├── playground/               # 안전하게 명령어를 실행할 실습 공간
│   ├── files/                # 문서, CSV, 설정 파일 및 임시 디렉터리
│   ├── java-project/         # 탐색·검색 실습용 가상 Spring Boot 프로젝트
│   ├── logs/                 # 분석 실습용 애플리케이션·접근·GC 로그
│   └── scripts/              # 프로세스·네트워크·권한 실습용 스크립트
├── progress.md               # 학습 진도 및 완료한 실습 기록
└── scripts/                  # 환경 검증 및 playground 초기화 도구
    ├── check.sh              # 프로젝트 구조 및 실습 데이터 무결성 검증
    └── reset-playground.sh   # playground 데이터를 초기 상태로 안전 복구
```

---

## 2. 커리큘럼 구성 (7 Levels)

| Level | 주제 | 핵심 명령어 및 기술 |
| :--- | :--- | :--- |
| **Level 1** | [Bash와 터미널 조작](curriculum/level-01.md) | `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`, `less`, `head`, `tail`, `Tab`, `Ctrl+A/E/W/U/K/R/L`, `history`, 와일드카드 |
| **Level 2** | [파일 검색과 텍스트 처리](curriculum/level-02.md) | `find`, `grep`, `rg`, `sort`, `uniq`, `wc`, `cut`, `sed`, `awk`, 파이프(`\|`), 리다이렉션(`>`, `>>`), Java 코드·로그 분석 |
| **Level 3** | [프로세스와 시스템 관리](curriculum/level-03.md) | `ps`, `top`, `htop`, `kill`, `pkill`, `jobs`, `bg`, `fg`, `free`, `df`, `du`, `chmod`, `chown`, 환경변수/`PATH`, `systemctl`/로그 |
| **Level 4** | [네트워크와 서버 작업](curriculum/level-04.md) | `ip`, `ss`, `ping`, `curl`, `dig`, `traceroute`, `ssh`, `scp`, `tar`, 로컬 테스트 서버 HTTP 점검 및 포트 추적 |
| **Level 5** | [Bash 생산성 도구](curriculum/level-05.md) | `fzf`, `zoxide`, `tmux`, `alias`, Bash 함수, `.bashrc` 관리, 히스토리 검색 최적화 |
| **Level 6** | [Windows + WSL 통합](curriculum/level-06.md) | Windows Terminal 탭/분할, `explorer.exe`, `code`, `/mnt/c` 접근, `wslpath`, `Win+E/R/V`, 가상 데스크톱, 키보드 워크플로 |
| **Level 7** | [실전 개발 워크플로](curriculum/level-07.md) | Java 코드 탐색 + 장애 로그 추출 + 포트/프로세스 제어 + HTTP API 테스트 + Git 조합 + `tmux` + 자동화 스크립트 |

---

## 3. 학습 시작 및 진행 방법

1. **AI 튜터와 대화 시작**
   - 루트 디렉터리에서 Codex CLI(또는 AI 에이전트)를 실행하고 `"이어서 진행하자"` 또는 `"시작하자"`라고 입력합니다.
   - 튜터는 [AGENTS.md](AGENTS.md)와 [progress.md](progress.md)를 읽고 현재 단계의 실습을 **한 번에 하나씩** 안내합니다.
2. **직접 입력 후 결과 공유**
   - 제시된 명령어를 터미널에 직접 입력해 실행합니다.
   - 실행 출력(또는 확인 여부)을 튜터에게 알려주면 다음 실습으로 넘어갑니다.
3. **실습 환경 검증 및 초기화**
   - 환경 상태 확인: `./scripts/check.sh`
   - 실습 중 `playground/` 내 파일을 삭제·변경해 초기 상태로 되돌리고 싶을 때: `./scripts/reset-playground.sh`
