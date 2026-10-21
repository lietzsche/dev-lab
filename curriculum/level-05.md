# Level 5. Bash 생산성 도구

## 목표
- 매일 수십 번 반복하는 긴 명령어를 `alias`와 Bash 함수로 단축한다.
- `fzf`, `zoxide`, `tmux` 등 현대적 CLI 생산성 도구를 활용해 탐색과 다중 작업 속도를 극대화한다.
- 기존 `.bashrc`를 오염시키지 않고 안전하게 셸 설정을 모듈화·관리하는 습관을 들인다.

---

## 세션 구성 (각 15~20분)

### Session 5.1: 반복 명령어 단축 (`alias`, `unalias`)
- **실습 목표**: 자주 사용하는 옵션 조합을 짧은 별칭(`alias`)으로 등록해 타이핑을 줄인다.
- **다루는 명령어**:
  - `alias`: 현재 등록된 별칭 목록 확인
  - `alias 이름='명령어'`: 현재 세션에 별칭 등록 (예: `alias ll='ls -lah'`, `alias ports='ss -tulnp'`)
  - `unalias 이름` 또는 `\명령어`: 별칭 해제 또는 별칭을 우회해 원본 명령어 실행
- **실습 과제**:
  1. 현재 셸에 기본 설정된 `alias` 목록 확인하기
  2. `playground/logs`의 에러만 빠르게 보는 임시 별칭 `alias errlog='grep -n "ERROR" playground/logs/app-2026-10-21.log'` 만들어 실행하기
  3. `unalias errlog`로 깔끔하게 해제하기

### Session 5.2: 인자를 받는 Bash 함수와 `.bashrc` 관리
- **실습 목표**: `alias`로 처리할 수 없는 동적 인자($1, $2) 처리를 위해 Bash 함수를 작성한다.
- **다루는 기술**:
  - `함수이름() { ... }`: 셸 함수 정의 및 `$1`(첫 번째 인자) 활용
  - `source <파일>`: 셸 스크립트에 정의한 함수/별칭을 현재 세션에 로드
- **실습 과제**:
  1. 폴더 생성과 이동을 한 번에 수행하는 `mkcd() { mkdir -p "$1" && cd "$1"; }` 함수를 정의해 `playground/files/temp` 안에서 테스트하기
  2. 특정 에러 코드를 로그에서 검색하는 함수를 `playground/scripts/my-shortcuts.sh`에 작성하고 `source`로 불러와 사용하기

### Session 5.3: 명령어 히스토리 검색 최적화와 `fzf`
- **실습 목표**: 퍼지 파인더(`fzf`) 또는 표준 파이프라인을 활용해 파일 탐색과 명령어 히스토리 검색을 가속한다.
- **다루는 도구**:
  - `history | grep "<키워드>"`: 과거 실행 명령 필터링
  - `fzf`: 대화형 퍼지 검색기 (설치 여부 확인 후, 파이프 `find playground | fzf` 또는 `history | fzf` 실습)
- **실습 과제**:
  1. `fzf` 설치 여부를 `which fzf`로 확인하고, 파일 목록이나 로그 줄을 실시간 필터링해 선택하기
  2. `rg --line-number "" playground/java-project | fzf`로 코드 라인을 대화형으로 검색하기

### Session 5.4: 스마트 디렉터리 이동 (`zoxide` / `CDPATH` / 디렉터리 스택)
- **실습 목표**: 깊은 패키지 경로(`src/main/java/com/example/order/...`)를 매번 입력하지 않고 즉시 점프한다.
- **다루는 기술**:
  - `pushd`, `popd`, `dirs -v`: Bash 내장 디렉터리 스택 활용
  - `zoxide` (`z`): 방문 빈도 기반 스마트 점프 도구 개념과 활용
- **실습 과제**:
  1. `pushd`로 깊은 Java 소스 디렉터리로 이동했다가 `popd`로 한 번에 원래 위치로 복귀하기
  2. `zoxide` 활용 패턴 익히기

### Session 5.5: 터미널 멀티플렉서 `tmux`로 다중 작업하기
- **실습 목표**: 하나의 터미널 창 안에서 화면을 분할해 한쪽에서는 서버를 띄우고, 다른 쪽에서는 로그 감시(`tail -f`)와 `curl` 테스트를 동시에 수행한다.
- **다루는 명령어**:
  - `tmux new -s dev`: 이름이 있는 새 세션 시작
  - `Ctrl+B` 후 `%` (좌우 분할), `"` (상하 분할), 방향키 (패인 이동), `d` (세션 분리 Detach)
  - `tmux ls`, `tmux attach -t dev`, `tmux kill-session -t dev`
- **실습 과제**:
  1. `tmux new -s lab`으로 세션을 열고 화면을 좌우로 분할하기
  2. 왼쪽 패인에서 로그를 띄우고 오른쪽 패인에서 명령어를 실행한 뒤 세션 분리(`detach`) 및 재접속(`attach`) 연습하기
