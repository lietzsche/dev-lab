# Bash & Shell Internals 커리큘럼

## 과정 목표

명령어 암기가 아니라 parsing, expansion, process, file descriptor, exit status라는 실행 모델로 Bash를 이해하고 안전한 운영 자동화를 설계한다.

## 단계 지도

| 단계 | 주제 | 결과 |
| :--- | :--- | :--- |
| B1 | 명령 실행 모델 | 명령 한 줄이 executable·argv·exit status가 되는 과정 설명 |
| B2 | Parsing·quoting·expansion | 문자열과 token이 변환되는 순서 예측 |
| B3 | Stream·process·signal | FD와 process graph로 pipeline과 job 진단 |
| B4 | Script 구성 요소 | 조건·반복·함수·array로 작은 CLI 구현 |
| B5 | 안전성·이식성·품질 | 입력·임시 자원·실패를 안전하게 다루고 검사 |
| B6 | 운영 자동화 종합 | 테스트 가능한 운영 CLI를 설계하고 장애 복구 |

## 로드맵 체크포인트

| 범위 | 의미 | 다음 경로 |
| :--- | :--- | :--- |
| B1~B2 | Git 실습을 방해하지 않을 shell 실행·해석 기반 | Python 완료 후 Git G1로 이동 |
| B3~B5 | process·FD·signal과 안전한 자동화 기반 | Linux·container·CI/CD 전에 완료 |
| B6 | 운영 CLI 설계 심화 | 실제 반복 작업을 제품화할 때 선택 |

Bash 전체는 Git의 선수 과정이 아니다. B1~B2 이후 Git을 시작할 수 있으며, Git에서 만난
redirection·pipeline은 필요 범위만 사용한 뒤 B3에서 내부 모델로 다시 검증한다.

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| B1-1 | prompt·현재 디렉터리·경로 | prompt와 명령 입력을 구분하고 상대·절대 경로를 예측 | - |
| B1-2 | command·argument·option·`--` | token이 argv가 되는 구조와 option 경계를 설명 | B1-1 |
| B1-3 | exit status·stderr·control operator | 성공·실패와 `&&`, `||`, `;`의 실행 조건을 판별 | B1-2 |
| B1-4 | builtin·function·executable·PATH | command lookup 순서와 실행 대상을 진단 | B1-3 |
| B2-1 | parsing 순서와 quoting | unquoted·single·double quote의 차이를 예측 | B1-4 |
| B2-2 | parameter와 environment | shell variable·environment·export의 process 경계를 설명 | B2-1 |
| B2-3 | splitting·globbing·array | word splitting과 pathname expansion 사고를 방지 | B2-2 |
| B2-4 | command·arithmetic·process substitution | 각 substitution의 실행 process와 결과를 관찰 | B2-3 |
| B3-1 | FD 0·1·2와 redirection | open FD와 redirection 순서를 설명 | B2-4 |
| B3-2 | pipeline·PIPESTATUS·pipefail | pipeline process와 실패 전달 방식을 진단 | B3-1 |
| B3-3 | subshell·group·background·job | scope와 process 관계를 예측하고 job을 회수 | B3-2 |
| B3-4 | signal·trap·cleanup | signal 전달과 종료 정리를 안전하게 구현 | B3-3 |
| B4-1 | script·shebang·실행 권한 | source와 execute의 차이 및 interpreter 선택을 설명 | B3-4 |
| B4-2 | test·conditional·case | 문자열·숫자·파일 조건을 안전하게 분기 | B4-1 |
| B4-3 | loop·function·scope·return | 반복과 함수 상태 전달을 exit status와 연결 | B4-2 |
| B4-4 | indexed·associative array·read | record 입력을 보존하며 collection을 처리 | B4-3 |
| B5-1 | shell option과 오류 전파 | `errexit`, `nounset`, `pipefail`의 예외를 실험 | B4-4 |
| B5-2 | temporary resource·atomic update | `mktemp`, `trap`, rename으로 안전하게 갱신 | B5-1 |
| B5-3 | input·injection·secret boundary | `eval`과 문자열 조립 위험을 재현하고 제거 | B5-2 |
| B5-4 | POSIX·ShellCheck·format·test | dialect와 platform 경계를 정하고 자동 검사 | B5-3 |
| B6-1 | CLI contract·getopts·config | 안정적인 interface와 precedence를 설계 | B5-4 |
| B6-2 | logging·structured output·observability | stdout/stderr 계약과 진단 정보를 분리 | B6-1 |
| B6-3 | retry·timeout·parallel process | 중복·시간 제한·동시 작업의 실패를 통제 | B6-2 |
| B6-4 | 운영 CLI 종합과 언어 선택 | 안전·테스트·복구 가능한 도구를 완성하고 경계 판단 | B6-3 |

## B1. 명령 실행 모델

- 관찰 축: prompt, cwd, token, argv, PATH, exit status
- 통합 실습: 같은 문자열을 서로 다른 argv와 executable로 전달해 비교
- 핵심 실패: prompt 기호를 명령에 포함, 경로 혼동, option으로 오인된 filename
- 완료 기준: 실행 전 command lookup·argv·종료 상태를 예측하고 증거로 설명

## B2. Parsing·quoting·expansion

- 관찰 축: parsing, parameter expansion, command substitution, splitting, globbing
- 통합 실습: 공백·newline·wildcard가 포함된 값을 손실 없이 전달
- 핵심 실패: unquoted variable, 빈 값, glob match 부재, nested substitution
- 완료 기준: 원문에서 최종 argv까지 단계별 변환을 재구성

## B3. Stream·process·signal

- 관찰 축: `/proc`, PID/PPID, FD 0·1·2, process group, signal, wait status
- 통합 실습: 여러 process의 stdout·stderr를 분리하고 종료를 회수
- 핵심 실패: redirection 순서, pipeline 실패 은폐, orphan job, cleanup 누락
- 완료 기준: process/FD graph로 정상·실패 경로와 남은 상태를 설명

## B4. Script 구성 요소

- 관찰 축: interpreter, source/execute, conditional status, scope, array boundary
- 통합 실습: 입력을 검증하고 여러 파일을 처리하는 작은 CLI
- 핵심 실패: `[ ]` token 누락, subshell scope 손실, whitespace record 손상
- 완료 기준: 각 construct가 만든 argv·scope·status를 설명하며 구현

## B5. 안전성·이식성·품질

- 관찰 축: shell option context, temporary resource, permissions, dialect, lint/test
- 통합 실습: 실패 주입에도 원본과 임시 자원을 안전하게 보존
- 핵심 실패: `set -e` 오판, unsafe `rm`, injection, Bash/POSIX 혼용
- 완료 기준: 위협·실패 모델을 명시하고 자동 검사와 회귀 실험으로 검증

## B6. 운영 자동화 종합

- 관찰 축: CLI contract, config precedence, logs, timeout, retry, concurrency
- 통합 실습: 외부 command를 조율하는 진단·복구 가능한 운영 CLI
- 핵심 실패: partial failure, duplicate execution, timeout, corrupt output, secret leak
- 완료 기준: 테스트와 runbook을 포함해 완성하고 Bash를 선택한 이유와 한계를 설명

## 과정 완료 결과물

- 안전한 sandbox 운영 CLI와 자동 test
- quoting·expansion·FD·process·signal을 설명하는 실습 증거
- CI/CD 또는 운영 환경에 적용 가능한 script review checklist
- Bash 대신 Python·Java·전용 도구를 선택할 판단 기준
