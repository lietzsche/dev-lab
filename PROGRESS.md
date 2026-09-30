# Bash & Shell Internals 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`으로 변경한다.
- 예측·관찰·실패·복구·검증 후 `완료`로 변경하고 멈춘다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- |
| **B1-1** | prompt·현재 디렉터리·경로 | 완료 | 2026-09-30 |
| **B1-2** | command·argument·option·`--` | 완료 | 2026-09-30 |
| **B1-3** | exit status·stderr·control operator | 완료 | 2026-09-30 |
| **B1-4** | builtin·function·executable·PATH | 완료 | 2026-09-30 |
| **B2-1** | parsing 순서와 quoting | 대기 | - |
| **B2-2** | parameter와 environment | 대기 | - |
| **B2-3** | splitting·globbing·array | 대기 | - |
| **B2-4** | command·arithmetic·process substitution | 대기 | - |
| **B3-1** | FD 0·1·2와 redirection | 대기 | - |
| **B3-2** | pipeline·PIPESTATUS·pipefail | 대기 | - |
| **B3-3** | subshell·group·background·job | 대기 | - |
| **B3-4** | signal·trap·cleanup | 대기 | - |
| **B4-1** | script·shebang·실행 권한 | 대기 | - |
| **B4-2** | test·conditional·case | 대기 | - |
| **B4-3** | loop·function·scope·return | 대기 | - |
| **B4-4** | indexed·associative array·read | 대기 | - |
| **B5-1** | shell option과 오류 전파 | 대기 | - |
| **B5-2** | temporary resource·atomic update | 대기 | - |
| **B5-3** | input·injection·secret boundary | 대기 | - |
| **B5-4** | POSIX·ShellCheck·format·test | 대기 | - |
| **B6-1** | CLI contract·getopts·config | 대기 | - |
| **B6-2** | logging·structured output·observability | 대기 | - |
| **B6-3** | retry·timeout·parallel process | 대기 | - |
| **B6-4** | 운영 CLI 종합과 언어 선택 | 대기 | - |

## 세부 기록

각 소단원은 시작할 때 아래 다섯 항목을 확장한다. 미래 단원의 답을 미리 기록하지 않는다.

### B1-1. prompt·현재 디렉터리·경로
- 계획: prompt와 입력 명령을 구분하고 현재 디렉터리 기준의 상대·절대 경로 해석을 관찰한다.
- 예측: `../fixtures/records.txt`와 절대 경로는 같은 파일을 가리키며 cwd가 바뀌면 같은 상대 경로의 대상도 바뀐다.
- 관찰 증거: 두 경로의 inode가 `319813`으로 같았고 `pwd`와 prompt가 `/tmp/bash-lab-sandbox/workspace`로 일치했다.
- 실패와 복구: 부모로 이동한 뒤 `../fixtures/records.txt`가 `/tmp/fixtures/records.txt`로 해석되어 실패했고 `cd workspace`로 복구했다.
- 배운 점: prompt는 입력이 아니며 상대 경로는 process의 현재 디렉터리를 기준으로 해석된다.

### B1-2. command·argument·option·`--`
- 계획: 명령 이름과 위치 인자의 경계를 관찰하고 option과 `--`를 누가 해석하는지 확인한다.
- 예측: 공백으로 나뉜 `two words`는 두 인자, quote로 묶은 값은 한 인자가 되며 `--`도 Bash에서는 인자로 전달된다.
- 관찰 증거: helper에서 command name, positional count와 각 인자를 확인했고 `--`, `--version`이 각각 전달됐다.
- 실패와 복구: `cat --version`이 파일 대신 option으로 해석됐고 `cat -- --version`으로 option parsing을 끝내 파일을 읽었다.
- 배운 점: Bash는 인자를 전달하며 `-` option과 `--` 경계의 의미는 대상 프로그램이 해석한다.
### B1-3. exit status·stderr·control operator
- 계획: stdout·stderr·exit status를 분리해 관찰하고 control operator의 실행 조건을 확인한다.
- 예측: `true`는 0, `false`는 1을 반환하고 `&&`는 성공 시, `||`는 실패 시 오른쪽을 실행하며 `;`는 항상 실행한다.
- 관찰 증거: stdout과 stderr를 별도 파일로 분리해도 status 7이 유지됐고 각 operator의 출력과 최종 status를 확인했다.
- 실패와 복구: `$?`가 다음 `printf` 성공으로 0에 덮였고 `false || printf ...`도 원래 실패를 최종 성공으로 바꾸는 것을 관찰했다.
- 배운 점: 출력 통로와 종료 상태는 독립적이며 compound list의 status는 실제로 마지막에 실행된 명령을 따른다.
### B1-4. builtin·function·executable·PATH
- 계획: builtin·function·external executable을 구분하고 PATH 검색과 우선순위를 관찰한다.
- 예측: 이름에 slash가 없으면 PATH를 왼쪽부터 검색하고 같은 이름의 function은 PATH executable보다 먼저 선택된다.
- 관찰 증거: `cd`와 `printf`는 builtin, `cat`은 `/usr/bin/cat`, 경로 지정 helper는 external executable로 확인했다.
- 실패와 복구: PATH에 없는 `show-argv`는 status 127로 실패했고 임시 PATH로 찾았으며 function shadowing은 `unset -f`로 제거했다.
- 배운 점: PATH는 colon으로 구분된 검색 우선순위이며 `type`과 `command -v`로 실제 실행 대상을 진단할 수 있다.
### B2-1. parsing 순서와 quoting
### B2-2. parameter와 environment
### B2-3. splitting·globbing·array
### B2-4. command·arithmetic·process substitution
### B3-1. FD 0·1·2와 redirection
### B3-2. pipeline·PIPESTATUS·pipefail
### B3-3. subshell·group·background·job
### B3-4. signal·trap·cleanup
### B4-1. script·shebang·실행 권한
### B4-2. test·conditional·case
### B4-3. loop·function·scope·return
### B4-4. indexed·associative array·read
### B5-1. shell option과 오류 전파
### B5-2. temporary resource·atomic update
### B5-3. input·injection·secret boundary
### B5-4. POSIX·ShellCheck·format·test
### B6-1. CLI contract·getopts·config
### B6-2. logging·structured output·observability
### B6-3. retry·timeout·parallel process
### B6-4. 운영 CLI 종합과 언어 선택
