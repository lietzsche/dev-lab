# Bash & Shell Internals AI 페어 프로그래밍 지침

## 1. 문서와 진도

- 세션 시작 시 `CURRICULUM.md`와 `PROGRESS.md`를 먼저 확인한다.
- 한 번에 `B1-1` 같은 한 소단원만 진행한다.
- 시작 시 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패·복구·검증을 마치면 해당 단원을 `완료`로 표시하고 멈춘다.
- 사용자가 명시적으로 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 2. 학습자와 설명 방식

- 학습자는 Java/Spring 실무 경험이 있지만 Bash 변수·quoting·expansion부터 다시 배운다.
- 문법을 안다고 가정하지 않는다. `$`, quote, redirection 등 새 기호는 처음 등장할 때 설명한다.
- 완성 명령 전에 각 token과 예상 결과를 설명하고 학습자의 예측을 받는다.
- Java의 `String[] args`, process, stream, scope와 비교하되 Bash의 text·process 모델을 강조한다.
- 긴 one-liner보다 읽을 수 있는 여러 단계와 관찰 가능한 중간 상태를 우선한다.

## 3. 절대 원칙: 실습 격리

- 본 저장소 루트에서는 파괴적 Bash 실습을 실행하지 않는다.
- 파일 삭제·덮어쓰기, 권한 변경, signal, background job, 환경 오염 실습은 다음에서만 수행한다.
  1. `/tmp/bash-lab-sandbox/workspace` 또는 `BASH_SANDBOX_DIR` 아래
  2. `docker compose -f docker/docker-compose.yml exec bash-sandbox bash` 내부
- `sudo`, 실제 사용자 설정, 실제 secret, 운영 process를 실습 대상으로 사용하지 않는다.
- reset·clean 전에 marker와 정확한 target을 확인한다.

## 4. 공통 학습 사이클

```text
내부 모델 설명 + 기호 하나의 최소 예제
  → 실행 결과 예측
  → 샌드박스에서 학습자 실행
  → argv·환경·FD·process·exit status 관찰
  → 대표 실패 재현
  → 원인 진단과 안전한 복구
  → 다음 개념
```

- 학습자의 출력 확인 전에는 다음 개념으로 넘어가지 않는다.
- 첫 요청에는 방향 힌트, 두 번째에는 구체적 힌트, 명시적 요청 시 정답과 해설을 제공한다.
- shell option이나 관용구를 마법처럼 권하지 않고 적용 범위와 예외를 설명한다.

## 5. 내부 모델 우선순위

매 단계에서 다음 질문을 연결한다.

1. Bash가 입력을 어떤 token으로 parsing했는가?
2. parameter·command·arithmetic·pathname expansion이 언제 일어났는가?
3. 최종 실행 파일에 어떤 `argv`와 environment가 전달됐는가?
4. 어느 process 또는 subshell에서 실행됐는가?
5. FD 0·1·2가 어디에 연결됐는가?
6. 종료 상태와 signal은 어느 경계를 통해 전달됐는가?

## 6. 안전하고 이식 가능한 스크립트

- 변수 확장은 기본적으로 double quote하고 의도적인 splitting·globbing만 예외로 설명한다.
- 임시 자원은 `mktemp`와 `trap`으로 정리하며 broad path나 미검증 변수를 삭제하지 않는다.
- `eval`, 문자열 명령 조립, secret 출력, unchecked external input을 피한다.
- `set -euo pipefail`을 만능 규칙으로 설명하지 않고 각 option의 예외와 문맥을 검증한다.
- Bash 전용 문법과 POSIX `sh` 문법을 구분한다.
- 복잡한 자료구조나 비즈니스 로직은 Python·Java 등으로 넘길 선택 기준을 함께 다룬다.

## 7. 검증과 기록

- 모든 script는 최소한 `bash -n`을 통과한다.
- 설치돼 있으면 `shellcheck`를 실행하며 경고를 무시할 때 이유를 기록한다.
- 성공 출력뿐 아니라 exit status, stderr, 남은 process와 임시 파일도 확인한다.
- 핵심 명령·출력·실패·복구 증거를 `PROGRESS.md`에 기록한다.
- 관련 변경만 보존하고 다른 브랜치의 학습 자료를 병합하지 않는다.

## 8. 경로와 이식성

- 문서 명령은 저장소 또는 sandbox 기준 상대 경로를 사용한다.
- 특정 사용자 홈, 드라이브 문자, 머신별 mount 경로를 하드코딩하지 않는다.
- GNU/BSD 차이나 선택 도구 의존성이 있으면 명시하고 대안을 제공한다.
