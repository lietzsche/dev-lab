# Level 3. 프로세스와 시스템 관리

## 목표
- 실행 중인 프로세스의 PID와 자원 점유율을 확인하고 백그라운드 작업을 제어한다.
- 응답 없는 프로세스를 안전하게 종료하고, 디스크·메모리 부족 상황을 즉시 진단한다.
- 스크립트 실행 권한(`chmod`), 환경변수(`PATH`), Linux 서비스(`systemctl`)와 시스템 로그 확인 방법을 익힌다.

---

## 세션 구성 (각 15~20분)

### Session 3.1: 프로세스 상태 관찰 (`ps`, `top`, `htop`)
- **실습 목표**: 현재 떠 있는 프로세스 목록과 CPU/메모리 사용량을 확인한다.
- **다루는 명령어**:
  - `ps`, `ps aux`, `ps -ef`: 전체 실행 프로세스와 PID, 실행 명령어 확인 (`grep`과 조합)
  - `top`, `htop`: 실시간 프로세스 모니터링 및 리소스 사용량 확인 (`q`로 종료)
- **실습 과제**:
  1. `ps aux`로 현재 실행 중인 프로세스 확인하기
  2. `ps aux | grep bash`로 특정 프로세스만 필터링해 PID 확인하기
  3. `top` (또는 `htop`)을 실행해 시스템 상태를 관찰하고 `q`로 종료하기

### Session 3.2: 파일 권한과 실행 가능 스크립트 (`chmod`, `chown`)
- **실습 목표**: 리눅스의 읽기(`r`), 쓰기(`w`), 실행(`x`) 권한 체계를 이해하고 셸 스크립트에 실행 권한을 부여한다.
- **다루는 명령어**:
  - `ls -l`: 권한 문자열(`-rw-r--r--`, `-rwxr-xr-x`) 해석
  - `chmod +x <파일>`, `chmod 755 <파일>`, `chmod 644 <파일>`: 권한 변경
  - `chown`: 파일 소유자/그룹 변경 개념 이해
- **실습 과제**:
  1. `ls -l playground/scripts/`로 스크립트들의 현재 권한 확인하기
  2. 실행 권한이 없는 `playground/scripts/healthcheck.sh`를 그냥 실행해 `Permission denied` 확인하기
  3. `chmod +x playground/scripts/healthcheck.sh` 부여 후 다시 실행해 결과 확인하기

### Session 3.3: 백그라운드 실행과 작업 제어 (`jobs`, `&`, `bg`, `fg`)
- **실습 목표**: 터미널 하나로 워커 프로세스를 백그라운드에 띄우고 포그라운드로 전환하며 제어한다.
- **다루는 기술**:
  - `<명령어> &`: 프로세스를 백그라운드로 즉시 실행
  - `jobs -l`: 현재 셸 세션의 백그라운드 작업 목록과 PID 확인
  - `fg %1`, `Ctrl+Z`, `bg %1`: 작업 포그라운드 전환, 일시 중지, 백그라운드 재개
- **실습 과제**:
  1. `playground/scripts/dummy-worker.sh &`로 연습용 워커를 백그라운드 실행하기
  2. `jobs -l`과 `ps aux | grep dummy-worker`로 작업 번호와 PID 확인하기
  3. `fg`로 가져온 뒤 `Ctrl+Z`로 멈추고 `bg`로 다시 백그라운드에서 돌리기

### Session 3.4: 시그널과 프로세스 종료 (`kill`, `pkill`)
- **실습 목표**: 연습용 백그라운드 프로세스에 정상 종료 시그널(`SIGTERM`)과 강제 종료 시그널(`SIGKILL`)을 보내 정리한다.
- **다루는 명령어**:
  - `kill <PID>` (`kill -15`): 정상 종료 요청 (리소스 정리 기회 부여 — 기본값)
  - `kill -9 <PID>`: 강제 즉시 종료 (응답 불능 상태일 때만 최후 수단으로 사용)
  - `pkill -f "<패턴>"`: 프로세스 이름/명령어 패턴으로 종료
- **실습 과제**:
  1. 실행 중인 `dummy-worker.sh`의 PID를 확인해 `kill <PID>`로 안전하게 종료하기
  2. 다시 백그라운드로 띄운 뒤 `pkill -f dummy-worker.sh`로 종료하고 `jobs`로 확인하기

### Session 3.5: 메모리와 디스크 용량 진단 (`free`, `df`, `du`)
- **실습 목표**: 서버 장애의 단골 원인인 메모리 고갈과 디스크 풀(Disk Full) 상태를 빠르게 파악한다.
- **다루는 명령어**:
  - `free -h`: 전체/사용 중/가용(available) 메모리 용량을 읽기 쉬운 단위로 확인
  - `df -h`: 마운트된 파일시스템별 디스크 전체/남은 용량 확인
  - `du -sh <경로>`, `du -h --max-depth=1 <경로>`: 어느 폴더가 용량을 많이 차지하는지 추적
- **실습 과제**:
  1. `free -h`로 현재 WSL에 할당된 메모리와 `available` 수치 확인하기
  2. `df -h`로 리눅스 루트(`/`)와 Windows 마운트 드라이브(`/mnt/c`) 용량 확인하기
  3. `du -sh playground/*`로 `playground` 하위 폴더별 용량 비교하기

### Session 3.6: 환경변수와 `PATH` (`env`, `export`, `echo $PATH`)
- **실습 목표**: 애플리케이션 설정 주입에 쓰이는 환경변수와 명령어 탐색 경로(`PATH`)의 동작 원리를 익힌다.
- **다루는 명령어**:
  - `env`, `echo $변수명`: 환경변수 조회
  - `export KEY=VALUE`: 현재 셸과 자식 프로세스에 전달할 환경변수 설정
  - `which <명령어>`: `PATH`에서 실제 실행되는 바이너리 위치 확인
- **실습 과제**:
  1. `echo $PATH`와 `which java` (또는 `which bash`, `which python3`)로 명령어 탐색 경로 확인하기
  2. `APP_ENV=staging ./playground/scripts/healthcheck.sh`처럼 일회성 환경변수를 주입해 실행 결과 변화 관찰하기

### Session 3.7: 시스템 로그와 서비스 관리 (`systemctl`, WSL과 서버의 차이)
- **실습 목표**: 실제 Linux 운영 서버에서 데몬 서비스를 관리하는 표준 명령과 시스템 로그 확인법을 이해한다.
- **다루는 명령어**:
  - `systemctl status <서비스>`, `systemctl start/stop/restart`: systemd 기반 서비스 제어
  - `journalctl -u <서비스>`, `dmesg`: 시스템/서비스 로그 확인
- **주의 사항**:
  - WSL2 환경의 systemd 활성화 여부와 실제 Ubuntu 서버 환경의 차이를 확인하고, 시스템 설정을 변경하지 않는 안전한 조회 명령(`systemctl status` 등)만 실습한다.
