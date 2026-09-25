# Production LLM & Agent Systems 커리큘럼

## 과정 목표

도구 사용법을 늘리는 데서 끝나지 않고 내부 상태, 불변식, 실패 모델과 운영 판단을 설명하고 검증한다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Model boundary와 reproducibility 단계에서 application이 의존할 model contract 정의할 수 있는가?
- Prompt·Retrieval·Grounding 단계에서 검색 실패와 생성 실패 분리할 수 있는가?
- Evaluation engineering 단계에서 release 판단 가능한 eval gate 구축할 수 있는가?
- Tool·Agent architecture 단계에서 결정과 실행을 통제 가능한 workflow로 구성할 수 있는가?
- Security·Reliability 단계에서 권한과 failure가 제한된 agent 운영할 수 있는가?
- Observability·Cost·Governance 단계에서 품질·비용·위험을 함께 관리할 수 있는가?

## 설계 기준

- 단원 수보다 개념의 선행 관계와 완료 역량을 우선한다.
- 정상 경로마다 실패 실험과 복구를 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 24소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **A1** | Model boundary와 reproducibility | 4 | application이 의존할 model contract 정의 |
| **A2** | Prompt·Retrieval·Grounding | 4 | 검색 실패와 생성 실패 분리 |
| **A3** | Evaluation engineering | 4 | release 판단 가능한 eval gate 구축 |
| **A4** | Tool·Agent architecture | 4 | 결정과 실행을 통제 가능한 workflow로 구성 |
| **A5** | Security·Reliability | 4 | 권한과 failure가 제한된 agent 운영 |
| **A6** | Observability·Cost·Governance | 4 | 품질·비용·위험을 함께 관리 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **A1-1** | tokenization·context budget | tokenization·context budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - |
| **A1-2** | sampling·determinism 한계 | sampling·determinism 한계의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-1 |
| **A1-3** | structured output·runtime validation | structured output·runtime validation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-2 |
| **A1-4** | provider abstraction·version·fallback | provider abstraction·version·fallback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-3 |
| **A2-1** | prompt contract·template version | prompt contract·template version의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-4 |
| **A2-2** | chunking·metadata·embedding | chunking·metadata·embedding의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-1 |
| **A2-3** | retrieval·filter·rerank | retrieval·filter·rerank의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-2 |
| **A2-4** | grounding·citation·abstention | grounding·citation·abstention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-3 |
| **A3-1** | evaluation dataset·failure taxonomy | evaluation dataset·failure taxonomy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-4 |
| **A3-2** | deterministic metric·task success | deterministic metric·task success의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-1 |
| **A3-3** | model judge·calibration | model judge·calibration의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-2 |
| **A3-4** | experiment·regression·human review | experiment·regression·human review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-3 |
| **A4-1** | tool contract·validation·idempotency | tool contract·validation·idempotency의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-4 |
| **A4-2** | agent state·planning·termination | agent state·planning·termination의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-1 |
| **A4-3** | checkpoint·memory·resume | checkpoint·memory·resume의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-2 |
| **A4-4** | human-in-the-loop·permission·audit | human-in-the-loop·permission·audit의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-3 |
| **A5-1** | prompt injection·content trust | prompt injection·content trust의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-4 |
| **A5-2** | tool authorization·sandbox | tool authorization·sandbox의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-1 |
| **A5-3** | privacy·secret·retention | privacy·secret·retention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-2 |
| **A5-4** | timeout·retry·rate limit·degradation | timeout·retry·rate limit·degradation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-3 |
| **A6-1** | end-to-end trace·correlation | end-to-end trace·correlation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-4 |
| **A6-2** | cost·latency·capacity budget | cost·latency·capacity budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-1 |
| **A6-3** | deployment·canary·rollback | deployment·canary·rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-2 |
| **A6-4** | feedback loop·governance·incident review | feedback loop·governance·incident review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-3 |

## A1. Model boundary와 reproducibility

- 관찰 축: token·context·sampling·schema·provider metadata
- 통합 실습: 고정 fixture로 model/parameter 비교
- 핵심 실패: truncation·invalid structure·provider drift

### [A1-1] tokenization·context budget

- 이해할 것: tokenization·context budget을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: token·context·sampling·schema·provider metadata 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 고정 fixture로 model/parameter 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: truncation·invalid structure·provider drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A1-2] sampling·determinism 한계

- 이해할 것: sampling·determinism 한계을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: token·context·sampling·schema·provider metadata 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 고정 fixture로 model/parameter 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: truncation·invalid structure·provider drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A1-3] structured output·runtime validation

- 이해할 것: structured output·runtime validation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: token·context·sampling·schema·provider metadata 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 고정 fixture로 model/parameter 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: truncation·invalid structure·provider drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A1-4] provider abstraction·version·fallback

- 이해할 것: provider abstraction·version·fallback을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: token·context·sampling·schema·provider metadata 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: 고정 fixture로 model/parameter 비교에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: truncation·invalid structure·provider drift 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A1 단계 결과물

- application이 의존할 model contract 정의.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## A2. Prompt·Retrieval·Grounding

- 관찰 축: prompt version·chunk·embedding·rank·citation
- 통합 실습: retrieval candidate와 answer 근거 추적
- 핵심 실패: prompt drift·lost context·retrieval miss·fabrication

### [A2-1] prompt contract·template version

- 이해할 것: prompt contract·template version을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: prompt version·chunk·embedding·rank·citation 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: retrieval candidate와 answer 근거 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: prompt drift·lost context·retrieval miss·fabrication 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A2-2] chunking·metadata·embedding

- 이해할 것: chunking·metadata·embedding을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: prompt version·chunk·embedding·rank·citation 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: retrieval candidate와 answer 근거 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: prompt drift·lost context·retrieval miss·fabrication 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A2-3] retrieval·filter·rerank

- 이해할 것: retrieval·filter·rerank을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: prompt version·chunk·embedding·rank·citation 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: retrieval candidate와 answer 근거 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: prompt drift·lost context·retrieval miss·fabrication 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A2-4] grounding·citation·abstention

- 이해할 것: grounding·citation·abstention을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: prompt version·chunk·embedding·rank·citation 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: retrieval candidate와 answer 근거 추적에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: prompt drift·lost context·retrieval miss·fabrication 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A2 단계 결과물

- 검색 실패와 생성 실패 분리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## A3. Evaluation engineering

- 관찰 축: dataset slice·rubric·metric·judge·human label
- 통합 실습: baseline/candidate blind regression
- 핵심 실패: data leakage·judge bias·aggregate score 착시

### [A3-1] evaluation dataset·failure taxonomy

- 이해할 것: evaluation dataset·failure taxonomy을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: dataset slice·rubric·metric·judge·human label 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: baseline/candidate blind regression에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data leakage·judge bias·aggregate score 착시 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A3-2] deterministic metric·task success

- 이해할 것: deterministic metric·task success을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: dataset slice·rubric·metric·judge·human label 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: baseline/candidate blind regression에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data leakage·judge bias·aggregate score 착시 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A3-3] model judge·calibration

- 이해할 것: model judge·calibration을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: dataset slice·rubric·metric·judge·human label 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: baseline/candidate blind regression에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data leakage·judge bias·aggregate score 착시 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A3-4] experiment·regression·human review

- 이해할 것: experiment·regression·human review을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: dataset slice·rubric·metric·judge·human label 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: baseline/candidate blind regression에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data leakage·judge bias·aggregate score 착시 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A3 단계 결과물

- release 판단 가능한 eval gate 구축.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## A4. Tool·Agent architecture

- 관찰 축: tool schema·state machine·checkpoint·approval
- 통합 실습: invalid/duplicate tool call과 resume
- 핵심 실패: loop·side effect duplication·permission escalation

### [A4-1] tool contract·validation·idempotency

- 이해할 것: tool contract·validation·idempotency을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: tool schema·state machine·checkpoint·approval 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: invalid/duplicate tool call과 resume에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: loop·side effect duplication·permission escalation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A4-2] agent state·planning·termination

- 이해할 것: agent state·planning·termination을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: tool schema·state machine·checkpoint·approval 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: invalid/duplicate tool call과 resume에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: loop·side effect duplication·permission escalation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A4-3] checkpoint·memory·resume

- 이해할 것: checkpoint·memory·resume을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: tool schema·state machine·checkpoint·approval 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: invalid/duplicate tool call과 resume에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: loop·side effect duplication·permission escalation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A4-4] human-in-the-loop·permission·audit

- 이해할 것: human-in-the-loop·permission·audit을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: tool schema·state machine·checkpoint·approval 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: invalid/duplicate tool call과 resume에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: loop·side effect duplication·permission escalation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A4 단계 결과물

- 결정과 실행을 통제 가능한 workflow로 구성.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## A5. Security·Reliability

- 관찰 축: trust boundary·injection·secret·timeout·rate limit
- 통합 실습: malicious document와 provider outage 주입
- 핵심 실패: data exfiltration·retry cost storm·unsafe tool use

### [A5-1] prompt injection·content trust

- 이해할 것: prompt injection·content trust을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trust boundary·injection·secret·timeout·rate limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: malicious document와 provider outage 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data exfiltration·retry cost storm·unsafe tool use 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A5-2] tool authorization·sandbox

- 이해할 것: tool authorization·sandbox을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trust boundary·injection·secret·timeout·rate limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: malicious document와 provider outage 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data exfiltration·retry cost storm·unsafe tool use 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A5-3] privacy·secret·retention

- 이해할 것: privacy·secret·retention을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trust boundary·injection·secret·timeout·rate limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: malicious document와 provider outage 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data exfiltration·retry cost storm·unsafe tool use 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A5-4] timeout·retry·rate limit·degradation

- 이해할 것: timeout·retry·rate limit·degradation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trust boundary·injection·secret·timeout·rate limit 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: malicious document와 provider outage 주입에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: data exfiltration·retry cost storm·unsafe tool use 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A5 단계 결과물

- 권한과 failure가 제한된 agent 운영.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## A6. Observability·Cost·Governance

- 관찰 축: trace·token/cost·latency·feedback·release lineage
- 통합 실습: canary·rollback·feedback triage
- 핵심 실패: untraceable quality drop·cost runaway·model deprecation

### [A6-1] end-to-end trace·correlation

- 이해할 것: end-to-end trace·correlation을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trace·token/cost·latency·feedback·release lineage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: canary·rollback·feedback triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: untraceable quality drop·cost runaway·model deprecation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A6-2] cost·latency·capacity budget

- 이해할 것: cost·latency·capacity budget을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trace·token/cost·latency·feedback·release lineage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: canary·rollback·feedback triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: untraceable quality drop·cost runaway·model deprecation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A6-3] deployment·canary·rollback

- 이해할 것: deployment·canary·rollback을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trace·token/cost·latency·feedback·release lineage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: canary·rollback·feedback triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: untraceable quality drop·cost runaway·model deprecation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### [A6-4] feedback loop·governance·incident review

- 이해할 것: feedback loop·governance·incident review을 구성하는 상태, 경계, 불변식과 비용.
- 직접 관찰: trace·token/cost·latency·feedback·release lineage 중 이 단원과 관련된 상태를 명령·로그·metadata로 확인한다.
- 실습: canary·rollback·feedback triage에서 조건 하나를 바꾸고 전후 결과를 비교한다.
- 실패 실험: untraceable quality drop·cost runaway·model deprecation 중 관련 상황을 재현하고 남은 상태를 진단한다.
- 완료 기준: 결과를 먼저 예측하고, 관찰 증거로 설명하며, 안전하게 복구하거나 회귀 검증한다.

### A6 단계 결과물

- 품질·비용·위험을 함께 관리.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
