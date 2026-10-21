# Level 6. Windows + WSL 통합

## 목표
- WSL2 Ubuntu와 Windows 11 사이의 경계를 자유자재로 넘나들며 두 OS의 장점을 결합한다.
- 마우스로 폴더나 에디터를 찾는 대신 WSL 터미널에서 Windows 프로그램을 즉시 호출하고 클립보드를 연동한다.
- Windows Terminal 단축키와 Windows 11 창 관리 단축키를 익혀 완전한 키보드 중심 워크플로를 완성한다.

---

## 세션 구성 (각 15~20분)

### Session 6.1: WSL에서 Windows 프로그램과 클립보드 다루기 (`explorer.exe`, `code`, `clip.exe`)
- **실습 목표**: WSL 셸에서 Windows 탐색기, VS Code, Windows 클립보드를 직접 제어한다.
- **다루는 명령어**:
  - `explorer.exe .`: 현재 WSL 디렉터리를 Windows 파일 탐색기로 열기
  - `code <파일/경로>`: 현재 폴더나 특정 설정 파일을 VS Code로 즉시 열기
  - `<명령어> | clip.exe`: Linux 명령어의 실행 결과를 Windows 클립보드에 즉시 복사 (`Ctrl+V`로 붙여넣기 가능)
- **실습 과제**:
  1. `grep "ERROR" playground/logs/app-2026-10-21.log | clip.exe` 실행 후 Windows 클립보드에 에러 로그가 복사되었는지 확인하기
  2. `code playground/java-project/src/main/java/com/example/order/service/OrderService.java`로 특정 소스 파일 바로 열기
  3. `explorer.exe playground/files`로 탐색기 열기 확인하기

### Session 6.2: Windows ↔ WSL 파일시스템과 경로 변환 (`/mnt/c`, `wslpath`)
- **실습 목표**: Windows 경로(`C:\...`)와 WSL 경로(`/mnt/c/...`)를 변환하고 파일시스템 I/O 특성을 이해한다.
- **다루는 명령어**:
  - `wslpath -w <리눅스경로>`: WSL 경로를 Windows 형식(`C:\...` 또는 `\\wsl.localhost\...`)으로 변환
  - `wslpath -u '<윈도우경로>'`: 복사한 Windows 경로 문자열을 즉시 WSL 경로(`/mnt/c/...`)로 변환
- **실습 과제**:
  1. `wslpath -w .`으로 현재 디렉터리의 Windows 경로 확인하기
  2. `wslpath -u 'C:\Windows\System32'`로 Windows 경로를 리눅스 경로로 변환하기
  3. `/home/<유저>`(Linux 네이티브 ext4)와 `/mnt/c/...`(Windows 마운트 9P) 간의 속도 및 권한 차이점 확인하기

### Session 6.3: Windows Terminal 핵심 키보드 단축키
- **실습 목표**: 마우스로 탭이나 창을 클릭하지 않고 단축키만으로 Windows Terminal을 제어한다.
- **다루는 단축키** (사용자가 직접 입력 후 확인):
  - `Ctrl+Shift+T` / `Ctrl+Shift+W`: 새 탭 열기 / 현재 탭(또는 패인) 닫기
  - `Ctrl+Tab` / `Ctrl+Shift+Tab`: 다음 탭 / 이전 탭 전환
  - `Alt+Shift+D` (또는 `Alt+Shift++` / `Alt+Shift+-`): 화면 분할(Pane Split)
  - `Alt+방향키`: 분할된 패인 간 포커스 이동
  - `Alt+Shift+방향키`: 분할된 패인 크기 조절
  - `Ctrl+Shift+F`: 터미널 출력 내용 내 텍스트 검색

### Session 6.4: Windows 11 창 배치 및 가상 데스크톱 단축키
- **실습 목표**: 에디터, 터미널, 브라우저 간 전환과 화면 배치를 키보드만으로 수행한다.
- **다루는 단축키** (사용자가 직접 수행 후 확인):
  - `Win+V`: 클립보드 히스토리 열기 (`clip.exe`로 복사한 여러 로그 조각을 골라 붙여넣을 때 유용)
  - `Win+E` / `Win+R`: 파일 탐색기 / 실행 창 열기
  - `Win+좌/우/상/하 방향키`: 현재 창을 화면 절반이나 사분면으로 즉시 스냅 배치
  - `Win+Ctrl+D` / `Win+Ctrl+좌/우 방향키`: 가상 데스크톱 생성 및 데스크톱 간 빠른 전환
  - `Alt+Tab`: 작업 중인 창 빠르게 전환
