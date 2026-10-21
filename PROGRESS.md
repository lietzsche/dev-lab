# CLI Mastery 학습 진도 기록 (progress.md)

## 현재 진행 상태
- **현재 단계**: Level 2. 파일 검색과 텍스트 처리
- **현재 세션**: Session 2.5 — 줄 수 집계와 중복 제거·정렬 (`wc`, `sort`, `uniq`)
- **최근 업데이트**: 2026-10-21 (Session 2.4 완료, 다음 시간 Session 2.5 시작 예정)

---

## 전체 진도 체크리스트

### Level 1. Bash와 터미널 조작
- [x] **Session 1.1**: 현재 위치 확인과 디렉터리 탐색 (`pwd`, `ls`, `cd`)
- [x] **Session 1.2**: 디렉터리와 파일 생성 (`mkdir`, `touch`, `Tab` 자동완성)
- [x] **Session 1.3**: 파일 복사, 이동/이름 변경, 안전 삭제 (`cp`, `mv`, `rm`)
- [x] **Session 1.4**: 파일과 로그 내용 읽기 (`cat`, `head`, `tail`, `less`)
- [x] **Session 1.5**: 터미널 커서 이동과 줄 편집 단축키 (`Ctrl+A/E/W/U/K/L`)
- [x] **Session 1.6**: 명령어 히스토리와 와일드카드 (`history`, `Ctrl+R`, `*`, `?`)

### Level 2. 파일 검색과 텍스트 처리
- [x] **Session 2.1**: 파일 이름과 조건으로 탐색 (`find`)
- [x] **Session 2.2**: 텍스트 패턴 검색의 표준 (`grep`)
- [x] **Session 2.3**: 초고속 코드 검색 도구 (`git grep` 활용)
- [x] **Session 2.4**: 파이프와 리다이렉션 (`|`, `>`, `>>`, `2>`)
- [ ] **Session 2.5**: 줄 수 집계와 중복 제거·정렬 (`wc`, `sort`, `uniq`) *(다음 진행 예정)*
- [ ] **Session 2.6**: 필드 추출과 텍스트 가공 (`cut`, `sed`, `awk` 기초)
- [ ] **Session 2.7**: 실전 조합 — Java 코드 및 장애 로그 분석 파이프라인

### Level 3. 프로세스와 시스템 관리
- [ ] **Session 3.1**: 프로세스 상태 관찰 (`ps`, `top`, `htop`)
- [ ] **Session 3.2**: 파일 권한과 실행 가능 스크립트 (`chmod`, `chown`)
- [ ] **Session 3.3**: 백그라운드 실행과 작업 제어 (`jobs`, `&`, `bg`, `fg`)
- [ ] **Session 3.4**: 시그널과 프로세스 종료 (`kill`, `pkill`)
- [ ] **Session 3.5**: 메모리와 디스크 용량 진단 (`free`, `df`, `du`)
- [ ] **Session 3.6**: 환경변수와 `PATH` (`env`, `export`, `echo $PATH`)
- [ ] **Session 3.7**: 시스템 로그와 서비스 관리 (`systemctl`, WSL과 서버의 차이)

### Level 4. 네트워크와 서버 작업
- [ ] **Session 4.1**: 네트워크 인터페이스와 연결 확인 (`ip`, `ping`)
- [ ] **Session 4.2**: 열린 포트와 프로세스 추적 (`ss`)
- [ ] **Session 4.3**: HTTP 요청과 API 응답 검증 (`curl`)
- [ ] **Session 4.4**: DNS 조회와 경로 진단 (`dig`, `traceroute`)
- [ ] **Session 4.5**: 아카이브 압축과 해제 (`tar`)
- [ ] **Session 4.6**: 원격 서버 접속과 파일 전송 (`ssh`, `scp`)

### Level 5. Bash 생산성 도구
- [ ] **Session 5.1**: 반복 명령어 단축 (`alias`, `unalias`)
- [ ] **Session 5.2**: 인자를 받는 Bash 함수와 `.bashrc` 관리
- [ ] **Session 5.3**: 명령어 히스토리 검색 최적화와 `fzf`
- [ ] **Session 5.4**: 스마트 디렉터리 이동 (`pushd`/`popd`, `zoxide`)
- [ ] **Session 5.5**: 터미널 멀티플렉서 `tmux`로 다중 작업하기

### Level 6. Windows + WSL 통합
- [ ] **Session 6.1**: WSL에서 Windows 프로그램과 클립보드 다루기 (`explorer.exe`, `code`, `clip.exe`)
- [ ] **Session 6.2**: Windows ↔ WSL 파일시스템과 경로 변환 (`/mnt/c`, `wslpath`)
- [ ] **Session 6.3**: Windows Terminal 핵심 키보드 단축키
- [ ] **Session 6.4**: Windows 11 창 배치 및 가상 데스크톱 단축키

### Level 7. 실전 개발 워크플로
- [ ] **Session 7.1**: 레거시/신규 Java 프로젝트 아키텍처 초고속 파악
- [ ] **Session 7.2**: 운영 장애 로그 분석 및 원인 코드 역추적
- [ ] **Session 7.3**: 좀비/충돌 프로세스 정리 및 API 서버 기동·검증
- [ ] **Session 7.4**: Git CLI와 파이프라인 조합 워크플로
- [ ] **Session 7.5**: `tmux` 관제 환경 구축 및 반복 점검 스크립트 자동화

---

## 수행 작업 로그

| 날짜 | 세션 | 수행한 작업 및 체득 명령어 | 비고 |
| :--- | :--- | :--- | :--- |
| 2026-10-21 | 환경 구축 | WSL2 Ubuntu 24.04 환경 확인 및 `playground/` 데이터셋 생성 완료 | Level 1.1 시작 대기 |
| 2026-10-21 | 환경 문제 해결 | Windows Codex 경로 혼용 확인 후 WSL nvm 환경에 Codex 설치. `type -a`, `npm config get prefix`, `npm install -g @openai/codex@latest`, `hash -r`, `codex --version` 직접 실행 | codex-cli 0.163.0 정상 출력 확인 |
| 2026-10-21 | Session 1.1 ~ 1.6 | `pwd`, `history 15`, `Ctrl+R`/`Ctrl+S`(`stty -ixon`), 와일드카드(`*.log`, `application-*.yml`, `app-2026-10-2?.log`) 및 Windows Terminal 분할 창 조작 실습 | Level 1 완료 |
| 2026-10-21 | Session 2.1 | `find <경로> -name "*.java"`, `find <경로> -type f -name "*Controller*.java"`, `.yml` 설정 파일 탐색 완료 | Session 2.1 완료 |
| 2026-10-21 | Session 2.2 | `grep -n`, `grep -C 2 -n`, `grep -rn "@Transactional"`, `grep -nE "ERROR\|WARN"`, `git grep` 비교 실습 완료 | Session 2.2 완료 |
| 2026-10-21 | Session 2.3 | 외부 도구 설치 없이 내장 `git grep -n`, `git grep -l "OrderRepository" -- "*.java"`, `git grep -nE "TODO\|FIXME"`로 고속 코드 탐색 완료 | Session 2.3 완료 |
| 2026-10-21 | Session 2.4 | 리다이렉션(`>`, `>>`), 파이프(`\| tail -n 5`), 표준 에러 리다이렉션(`2>`, `2>/dev/null`) 실습 완료 | Session 2.4 완료 |
