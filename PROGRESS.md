# Git Internals & Workflows 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G1-1** | 내용 주소화와 object header | 내용 주소화와 object header의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **G1-2** | blob·tree와 snapshot 구조 | blob·tree와 snapshot 구조의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-1 | 대기 | - |
| **G1-3** | commit·annotated tag와 identity | commit·annotated tag와 identity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-2 | 대기 | - |
| **G1-4** | loose object·packfile·delta와 plumbing 조립 | loose object·packfile·delta와 plumbing 조립의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-3 | 대기 | - |
| **G2-1** | 세 영역과 status 비교 모델 | 세 영역과 status 비교 모델의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-4 | 대기 | - |
| **G2-2** | index binary·stat cache·intent-to-add | index binary·stat cache·intent-to-add의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-1 | 대기 | - |
| **G2-3** | conflict stage 1·2·3와 partial staging | conflict stage 1·2·3와 partial staging의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-2 | 대기 | - |
| **G2-4** | ref·symbolic ref·packed-refs와 reset/restore/switch | ref·symbolic ref·packed-refs와 reset/restore/switch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-3 | 대기 | - |
| **G3-1** | commit DAG와 revision selection | commit DAG와 revision selection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-4 | 대기 | - |
| **G3-2** | snapshot diff·patch·rename detection | snapshot diff·patch·rename detection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-1 | 대기 | - |
| **G3-3** | merge-base와 fast-forward | merge-base와 fast-forward의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-2 | 대기 | - |
| **G3-4** | three-way merge·conflict marker·index stage | three-way merge·conflict marker·index stage의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-3 | 대기 | - |
| **G4-1** | cherry-pick과 patch identity | cherry-pick과 patch identity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-4 | 대기 | - |
| **G4-2** | revert와 inverse patch | revert와 inverse patch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-1 | 대기 | - |
| **G4-3** | rebase replay와 interactive rebase | rebase replay와 interactive rebase의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-2 | 대기 | - |
| **G4-4** | rewrite conflict·abort·published history 정책 | rewrite conflict·abort·published history 정책의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-3 | 대기 | - |
| **G5-1** | bare repository·transport·refspec | bare repository·transport·refspec의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-4 | 대기 | - |
| **G5-2** | remote-tracking ref·fetch·pull | remote-tracking ref·fetch·pull의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-1 | 대기 | - |
| **G5-3** | push fast-forward·CAS·force-with-lease | push fast-forward·CAS·force-with-lease의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-2 | 대기 | - |
| **G5-4** | merge commit·squash·rebase merge와 commit hygiene | merge commit·squash·rebase merge와 commit hygiene의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-3 | 대기 | - |
| **G6-1** | detached HEAD·reflog·lost commit | detached HEAD·reflog·lost commit의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-4 | 대기 | - |
| **G6-2** | bisect와 자동 회귀 탐색 | bisect와 자동 회귀 탐색의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-1 | 대기 | - |
| **G6-3** | worktree·rerere·반복 작업 격리 | worktree·rerere·반복 작업 격리의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-2 | 대기 | - |
| **G6-4** | fsck·repack·gc·복구 종합 훈련 | fsck·repack·gc·복구 종합 훈련의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-3 | 대기 | - |

## 세부 기록

### G1-1. 내용 주소화와 object header

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G1-2. blob·tree와 snapshot 구조

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G1-3. commit·annotated tag와 identity

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G1-4. loose object·packfile·delta와 plumbing 조립

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G2-1. 세 영역과 status 비교 모델

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G2-2. index binary·stat cache·intent-to-add

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G2-3. conflict stage 1·2·3와 partial staging

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G2-4. ref·symbolic ref·packed-refs와 reset/restore/switch

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G3-1. commit DAG와 revision selection

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G3-2. snapshot diff·patch·rename detection

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G3-3. merge-base와 fast-forward

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G3-4. three-way merge·conflict marker·index stage

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G4-1. cherry-pick과 patch identity

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G4-2. revert와 inverse patch

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G4-3. rebase replay와 interactive rebase

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G4-4. rewrite conflict·abort·published history 정책

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G5-1. bare repository·transport·refspec

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G5-2. remote-tracking ref·fetch·pull

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G5-3. push fast-forward·CAS·force-with-lease

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G5-4. merge commit·squash·rebase merge와 commit hygiene

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G6-1. detached HEAD·reflog·lost commit

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G6-2. bisect와 자동 회귀 탐색

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G6-3. worktree·rerere·반복 작업 격리

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### G6-4. fsck·repack·gc·복구 종합 훈련

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
