# Production LLM & Agent Systems 커리큘럼

## 목적

평가·추적·복구·승인 가능한 LLM/agent를 설계한다. 도구 암기보다 내부 상태와 실패 모델을 관찰한다.

- 선수지식: Python·Data·분산 기초
- 최종 실습: 조사 agent의 eval·trace·approval·비용 검증
- 전체: 6단계, 18소단원

## 단계 요약

| 단계 | 주제 | 관찰 대상 | 통합 실습 |
| :--- | :--- | :--- | :--- |
| **A1** | 모델 계약 | token·response·schema failure | model·parameter 비교 |
| **A2** | Prompt·지식 | prompt version·retrieval·citation | chunk·검색 비교 |
| **A3** | 평가 | dataset·metric·judge·label | baseline/candidate 비교 |
| **A4** | Tool·Agent | tool call·state·approval | 중복·중단 재개 |
| **A5** | 신뢰·보안 | retry·injection·secret log | provider 장애·abuse |
| **A6** | 운영 | trace·cost·latency·feedback | canary·rollback |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **A1-1** | context·sampling | context·sampling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | - |
| **A1-2** | structured output | structured output의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A1-1 |
| **A1-3** | provider fallback | provider fallback의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A1-2 |
| **A2-1** | prompt contract | prompt contract의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A1-3 |
| **A2-2** | retrieval·rerank | retrieval·rerank의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A2-1 |
| **A2-3** | grounding·citation | grounding·citation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A2-2 |
| **A3-1** | dataset·rubric | dataset·rubric의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A2-3 |
| **A3-2** | metric·judge | metric·judge의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A3-1 |
| **A3-3** | regression experiment | regression experiment의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A3-2 |
| **A4-1** | tool boundary | tool boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A3-3 |
| **A4-2** | agent state loop | agent state loop의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A4-1 |
| **A4-3** | human approval | human approval의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A4-2 |
| **A5-1** | timeout·rate limit | timeout·rate limit의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A4-3 |
| **A5-2** | prompt injection | prompt injection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A5-1 |
| **A5-3** | privacy·retention | privacy·retention의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A5-2 |
| **A6-1** | observability | observability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A5-3 |
| **A6-2** | cost·capacity | cost·capacity의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A6-1 |
| **A6-3** | deployment governance | deployment governance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다 | A6-2 |

## 상세 커리큘럼

### [A1-1] context·sampling

- 목표: context·sampling의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: token·response·schema failure를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: model·parameter 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A1-2] structured output

- 목표: structured output의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: token·response·schema failure를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: model·parameter 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A1-3] provider fallback

- 목표: provider fallback의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: token·response·schema failure를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: model·parameter 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A2-1] prompt contract

- 목표: prompt contract의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: prompt version·retrieval·citation를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: chunk·검색 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A2-2] retrieval·rerank

- 목표: retrieval·rerank의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: prompt version·retrieval·citation를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: chunk·검색 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A2-3] grounding·citation

- 목표: grounding·citation의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: prompt version·retrieval·citation를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: chunk·검색 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A3-1] dataset·rubric

- 목표: dataset·rubric의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: dataset·metric·judge·label를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: baseline/candidate 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A3-2] metric·judge

- 목표: metric·judge의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: dataset·metric·judge·label를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: baseline/candidate 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A3-3] regression experiment

- 목표: regression experiment의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: dataset·metric·judge·label를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: baseline/candidate 비교 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A4-1] tool boundary

- 목표: tool boundary의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: tool call·state·approval를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·중단 재개 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A4-2] agent state loop

- 목표: agent state loop의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: tool call·state·approval를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·중단 재개 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A4-3] human approval

- 목표: human approval의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: tool call·state·approval를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: 중복·중단 재개 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A5-1] timeout·rate limit

- 목표: timeout·rate limit의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: retry·injection·secret log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: provider 장애·abuse 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A5-2] prompt injection

- 목표: prompt injection의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: retry·injection·secret log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: provider 장애·abuse 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A5-3] privacy·retention

- 목표: privacy·retention의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: retry·injection·secret log를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: provider 장애·abuse 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A6-1] observability

- 목표: observability의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·cost·latency·feedback를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: canary·rollback 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A6-2] cost·capacity

- 목표: cost·capacity의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·cost·latency·feedback를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: canary·rollback 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.

### [A6-3] deployment governance

- 목표: deployment governance의 내부 구조, 상태 전이와 실패 조건을 설명하고 검증한다.
- 내부 관찰: trace·cost·latency·feedback를 확인해 실제 상태 표현을 설명한다.
- 최소 실습: canary·rollback 과정에서 조건을 바꾸고 결과를 비교한다.
- 실패·반례: 정상과 실패 경로를 만들고 관찰 증거로 진단한다.
- 완료 증거: 명령, 출력, 상태 전이와 복구 검증을 `PROGRESS.md`에 기록한다.
