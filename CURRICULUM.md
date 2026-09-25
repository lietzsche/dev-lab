# Git Internals & Workflows 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- 객체 저장소와 snapshot 단계에서 저수준 객체에서 commit history를 직접 재구성할 수 있는가?
- Working Tree·Index·Reference 단계에서 porcelain 명령 전후 상태를 내부 파일로 예측할 수 있는가?
- DAG·Diff·Merge 단계에서 merge commit의 두 parent와 결과 tree 설명할 수 있는가?
- Patch replay와 history rewrite 단계에서 공개 여부에 따라 안전한 rewrite 전략 선택할 수 있는가?
- 분산 협업과 review history 단계에서 원격 동기화와 팀 merge 정책을 설명할 수 있는가?
- 진단·복구·유지보수 단계에서 표준 triage로 원인 commit과 손실 history 복구할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 24소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **G1** | 객체 저장소와 snapshot | 4 | 저수준 객체에서 commit history를 직접 재구성 |
| **G2** | Working Tree·Index·Reference | 4 | porcelain 명령 전후 상태를 내부 파일로 예측 |
| **G3** | DAG·Diff·Merge | 4 | merge commit의 두 parent와 결과 tree 설명 |
| **G4** | Patch replay와 history rewrite | 4 | 공개 여부에 따라 안전한 rewrite 전략 선택 |
| **G5** | 분산 협업과 review history | 4 | 원격 동기화와 팀 merge 정책을 설명 |
| **G6** | 진단·복구·유지보수 | 4 | 표준 triage로 원인 commit과 손실 history 복구 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **G1-1** | 내용 주소화와 object header | 내용 주소화와 object header의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **G1-2** | blob·tree와 snapshot 구조 | blob·tree와 snapshot 구조의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-1 |
| **G1-3** | commit·annotated tag와 identity | commit·annotated tag와 identity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-2 |
| **G1-4** | loose object·packfile·delta와 plumbing 조립 | loose object·packfile·delta와 plumbing 조립의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-3 |
| **G2-1** | 세 영역과 status 비교 모델 | 세 영역과 status 비교 모델의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G1-4 |
| **G2-2** | index binary·stat cache·intent-to-add | index binary·stat cache·intent-to-add의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-1 |
| **G2-3** | conflict stage 1·2·3와 partial staging | conflict stage 1·2·3와 partial staging의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-2 |
| **G2-4** | ref·symbolic ref·packed-refs와 reset/restore/switch | ref·symbolic ref·packed-refs와 reset/restore/switch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-3 |
| **G3-1** | commit DAG와 revision selection | commit DAG와 revision selection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G2-4 |
| **G3-2** | snapshot diff·patch·rename detection | snapshot diff·patch·rename detection의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-1 |
| **G3-3** | merge-base와 fast-forward | merge-base와 fast-forward의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-2 |
| **G3-4** | three-way merge·conflict marker·index stage | three-way merge·conflict marker·index stage의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-3 |
| **G4-1** | cherry-pick과 patch identity | cherry-pick과 patch identity의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G3-4 |
| **G4-2** | revert와 inverse patch | revert와 inverse patch의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-1 |
| **G4-3** | rebase replay와 interactive rebase | rebase replay와 interactive rebase의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-2 |
| **G4-4** | rewrite conflict·abort·published history 정책 | rewrite conflict·abort·published history 정책의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-3 |
| **G5-1** | bare repository·transport·refspec | bare repository·transport·refspec의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G4-4 |
| **G5-2** | remote-tracking ref·fetch·pull | remote-tracking ref·fetch·pull의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-1 |
| **G5-3** | push fast-forward·CAS·force-with-lease | push fast-forward·CAS·force-with-lease의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-2 |
| **G5-4** | merge commit·squash·rebase merge와 commit hygiene | merge commit·squash·rebase merge와 commit hygiene의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-3 |
| **G6-1** | detached HEAD·reflog·lost commit | detached HEAD·reflog·lost commit의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G5-4 |
| **G6-2** | bisect와 자동 회귀 탐색 | bisect와 자동 회귀 탐색의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-1 |
| **G6-3** | worktree·rerere·반복 작업 격리 | worktree·rerere·반복 작업 격리의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-2 |
| **G6-4** | fsck·repack·gc·복구 종합 훈련 | fsck·repack·gc·복구 종합 훈련의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | G6-3 |

## G1. 객체 저장소와 snapshot

- 관찰 축: object header·OID·loose/pack·tree graph
- 통합 실습: plumbing으로 두 snapshot과 parent chain 조립
- 핵심 실패: 동일 내용·다른 metadata·packing 전후 identity를 비교

### [G1-1] 내용 주소화와 object header

- 이해할 것: 내용 주소화와 object header을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object header·OID·loose/pack·tree graph 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: plumbing으로 두 snapshot과 parent chain 조립에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 동일 내용·다른 metadata·packing 전후 identity를 비교 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G1-2] blob·tree와 snapshot 구조

- 이해할 것: blob·tree와 snapshot 구조을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object header·OID·loose/pack·tree graph 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: plumbing으로 두 snapshot과 parent chain 조립에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 동일 내용·다른 metadata·packing 전후 identity를 비교 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G1-3] commit·annotated tag와 identity

- 이해할 것: commit·annotated tag와 identity을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object header·OID·loose/pack·tree graph 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: plumbing으로 두 snapshot과 parent chain 조립에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 동일 내용·다른 metadata·packing 전후 identity를 비교 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G1-4] loose object·packfile·delta와 plumbing 조립

- 이해할 것: loose object·packfile·delta와 plumbing 조립을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: object header·OID·loose/pack·tree graph 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: plumbing으로 두 snapshot과 parent chain 조립에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 동일 내용·다른 metadata·packing 전후 identity를 비교 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G1 단계 결과물

- 저수준 객체에서 commit history를 직접 재구성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## G2. Working Tree·Index·Reference

- 관찰 축: index entry·stat cache·stage·HEAD·ref
- 통합 실습: 파일 하나를 세 영역에서 독립적으로 변화
- 핵심 실패: 잘못된 restore/reset과 unmerged index를 복구

### [G2-1] 세 영역과 status 비교 모델

- 이해할 것: 세 영역과 status 비교 모델을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: index entry·stat cache·stage·HEAD·ref 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 파일 하나를 세 영역에서 독립적으로 변화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 restore/reset과 unmerged index를 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G2-2] index binary·stat cache·intent-to-add

- 이해할 것: index binary·stat cache·intent-to-add을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: index entry·stat cache·stage·HEAD·ref 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 파일 하나를 세 영역에서 독립적으로 변화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 restore/reset과 unmerged index를 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G2-3] conflict stage 1·2·3와 partial staging

- 이해할 것: conflict stage 1·2·3와 partial staging을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: index entry·stat cache·stage·HEAD·ref 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 파일 하나를 세 영역에서 독립적으로 변화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 restore/reset과 unmerged index를 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G2-4] ref·symbolic ref·packed-refs와 reset/restore/switch

- 이해할 것: ref·symbolic ref·packed-refs와 reset/restore/switch을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: index entry·stat cache·stage·HEAD·ref 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 파일 하나를 세 영역에서 독립적으로 변화에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 잘못된 restore/reset과 unmerged index를 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G2 단계 결과물

- porcelain 명령 전후 상태를 내부 파일로 예측.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## G3. DAG·Diff·Merge

- 관찰 축: reachability·revision set·merge-base·index stage
- 통합 실습: 분기 graph에서 diff와 merge 결과 예측
- 핵심 실패: criss-cross·rename·content conflict를 진단

### [G3-1] commit DAG와 revision selection

- 이해할 것: commit DAG와 revision selection을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reachability·revision set·merge-base·index stage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 분기 graph에서 diff와 merge 결과 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: criss-cross·rename·content conflict를 진단 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G3-2] snapshot diff·patch·rename detection

- 이해할 것: snapshot diff·patch·rename detection을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reachability·revision set·merge-base·index stage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 분기 graph에서 diff와 merge 결과 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: criss-cross·rename·content conflict를 진단 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G3-3] merge-base와 fast-forward

- 이해할 것: merge-base와 fast-forward을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reachability·revision set·merge-base·index stage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 분기 graph에서 diff와 merge 결과 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: criss-cross·rename·content conflict를 진단 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G3-4] three-way merge·conflict marker·index stage

- 이해할 것: three-way merge·conflict marker·index stage을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reachability·revision set·merge-base·index stage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 분기 graph에서 diff와 merge 결과 예측에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: criss-cross·rename·content conflict를 진단 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G3 단계 결과물

- merge commit의 두 parent와 결과 tree 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## G4. Patch replay와 history rewrite

- 관찰 축: patch identity·new commit·ORIG_HEAD·rebase state
- 통합 실습: cherry-pick·revert·rebase를 동일 변경으로 비교
- 핵심 실패: 중간 conflict에서 continue·skip·abort와 복구

### [G4-1] cherry-pick과 patch identity

- 이해할 것: cherry-pick과 patch identity을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: patch identity·new commit·ORIG_HEAD·rebase state 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: cherry-pick·revert·rebase를 동일 변경으로 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 중간 conflict에서 continue·skip·abort와 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G4-2] revert와 inverse patch

- 이해할 것: revert와 inverse patch을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: patch identity·new commit·ORIG_HEAD·rebase state 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: cherry-pick·revert·rebase를 동일 변경으로 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 중간 conflict에서 continue·skip·abort와 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G4-3] rebase replay와 interactive rebase

- 이해할 것: rebase replay와 interactive rebase을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: patch identity·new commit·ORIG_HEAD·rebase state 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: cherry-pick·revert·rebase를 동일 변경으로 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 중간 conflict에서 continue·skip·abort와 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G4-4] rewrite conflict·abort·published history 정책

- 이해할 것: rewrite conflict·abort·published history 정책을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: patch identity·new commit·ORIG_HEAD·rebase state 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: cherry-pick·revert·rebase를 동일 변경으로 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: 중간 conflict에서 continue·skip·abort와 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G4 단계 결과물

- 공개 여부에 따라 안전한 rewrite 전략 선택.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## G5. 분산 협업과 review history

- 관찰 축: bare repo·refspec·tracking ref·receive policy
- 통합 실습: Alice/Bob/learner로 동시 push와 review merge 재현
- 핵심 실패: stale lease·non-fast-forward·잘못된 pull 복구

### [G5-1] bare repository·transport·refspec

- 이해할 것: bare repository·transport·refspec을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bare repo·refspec·tracking ref·receive policy 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Alice/Bob/learner로 동시 push와 review merge 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale lease·non-fast-forward·잘못된 pull 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G5-2] remote-tracking ref·fetch·pull

- 이해할 것: remote-tracking ref·fetch·pull을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bare repo·refspec·tracking ref·receive policy 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Alice/Bob/learner로 동시 push와 review merge 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale lease·non-fast-forward·잘못된 pull 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G5-3] push fast-forward·CAS·force-with-lease

- 이해할 것: push fast-forward·CAS·force-with-lease을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bare repo·refspec·tracking ref·receive policy 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Alice/Bob/learner로 동시 push와 review merge 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale lease·non-fast-forward·잘못된 pull 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G5-4] merge commit·squash·rebase merge와 commit hygiene

- 이해할 것: merge commit·squash·rebase merge와 commit hygiene을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: bare repo·refspec·tracking ref·receive policy 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: Alice/Bob/learner로 동시 push와 review merge 재현에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: stale lease·non-fast-forward·잘못된 pull 복구 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G5 단계 결과물

- 원격 동기화와 팀 merge 정책을 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## G6. 진단·복구·유지보수

- 관찰 축: reflog·bisect·worktree·rerere·fsck·reachability
- 통합 실습: 삭제·rewrite·regression·반복 conflict 사고 주입
- 핵심 실패: reflog 만료와 unreachable object 한계까지 확인

### [G6-1] detached HEAD·reflog·lost commit

- 이해할 것: detached HEAD·reflog·lost commit을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reflog·bisect·worktree·rerere·fsck·reachability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 삭제·rewrite·regression·반복 conflict 사고 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reflog 만료와 unreachable object 한계까지 확인 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G6-2] bisect와 자동 회귀 탐색

- 이해할 것: bisect와 자동 회귀 탐색을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reflog·bisect·worktree·rerere·fsck·reachability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 삭제·rewrite·regression·반복 conflict 사고 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reflog 만료와 unreachable object 한계까지 확인 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G6-3] worktree·rerere·반복 작업 격리

- 이해할 것: worktree·rerere·반복 작업 격리을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reflog·bisect·worktree·rerere·fsck·reachability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 삭제·rewrite·regression·반복 conflict 사고 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reflog 만료와 unreachable object 한계까지 확인 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [G6-4] fsck·repack·gc·복구 종합 훈련

- 이해할 것: fsck·repack·gc·복구 종합 훈련을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: reflog·bisect·worktree·rerere·fsck·reachability 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 삭제·rewrite·regression·반복 conflict 사고 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: reflog 만료와 unreachable object 한계까지 확인 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### G6 단계 결과물

- 표준 triage로 원인 commit과 손실 history 복구.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
