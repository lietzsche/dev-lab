# Production LLM & Agent Systems 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A1-1** | tokenization·context budget | tokenization·context budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | - | 대기 | - |
| **A1-2** | sampling·determinism 한계 | sampling·determinism 한계의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-1 | 대기 | - |
| **A1-3** | structured output·runtime validation | structured output·runtime validation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-2 | 대기 | - |
| **A1-4** | provider abstraction·version·fallback | provider abstraction·version·fallback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-3 | 대기 | - |
| **A2-1** | prompt contract·template version | prompt contract·template version의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A1-4 | 대기 | - |
| **A2-2** | chunking·metadata·embedding | chunking·metadata·embedding의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-1 | 대기 | - |
| **A2-3** | retrieval·filter·rerank | retrieval·filter·rerank의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-2 | 대기 | - |
| **A2-4** | grounding·citation·abstention | grounding·citation·abstention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-3 | 대기 | - |
| **A3-1** | evaluation dataset·failure taxonomy | evaluation dataset·failure taxonomy의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A2-4 | 대기 | - |
| **A3-2** | deterministic metric·task success | deterministic metric·task success의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-1 | 대기 | - |
| **A3-3** | model judge·calibration | model judge·calibration의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-2 | 대기 | - |
| **A3-4** | experiment·regression·human review | experiment·regression·human review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-3 | 대기 | - |
| **A4-1** | tool contract·validation·idempotency | tool contract·validation·idempotency의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A3-4 | 대기 | - |
| **A4-2** | agent state·planning·termination | agent state·planning·termination의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-1 | 대기 | - |
| **A4-3** | checkpoint·memory·resume | checkpoint·memory·resume의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-2 | 대기 | - |
| **A4-4** | human-in-the-loop·permission·audit | human-in-the-loop·permission·audit의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-3 | 대기 | - |
| **A5-1** | prompt injection·content trust | prompt injection·content trust의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A4-4 | 대기 | - |
| **A5-2** | tool authorization·sandbox | tool authorization·sandbox의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-1 | 대기 | - |
| **A5-3** | privacy·secret·retention | privacy·secret·retention의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-2 | 대기 | - |
| **A5-4** | timeout·retry·rate limit·degradation | timeout·retry·rate limit·degradation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-3 | 대기 | - |
| **A6-1** | end-to-end trace·correlation | end-to-end trace·correlation의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A5-4 | 대기 | - |
| **A6-2** | cost·latency·capacity budget | cost·latency·capacity budget의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-1 | 대기 | - |
| **A6-3** | deployment·canary·rollback | deployment·canary·rollback의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-2 | 대기 | - |
| **A6-4** | feedback loop·governance·incident review | feedback loop·governance·incident review의 내부 모델과 선택 기준을 설명하고 실제 상태로 검증 | A6-3 | 대기 | - |

## 세부 기록

### A1-1. tokenization·context budget

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A1-2. sampling·determinism 한계

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A1-3. structured output·runtime validation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A1-4. provider abstraction·version·fallback

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A2-1. prompt contract·template version

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A2-2. chunking·metadata·embedding

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A2-3. retrieval·filter·rerank

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A2-4. grounding·citation·abstention

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A3-1. evaluation dataset·failure taxonomy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A3-2. deterministic metric·task success

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A3-3. model judge·calibration

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A3-4. experiment·regression·human review

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A4-1. tool contract·validation·idempotency

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A4-2. agent state·planning·termination

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A4-3. checkpoint·memory·resume

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A4-4. human-in-the-loop·permission·audit

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A5-1. prompt injection·content trust

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A5-2. tool authorization·sandbox

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A5-3. privacy·secret·retention

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A5-4. timeout·retry·rate limit·degradation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A6-1. end-to-end trace·correlation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A6-2. cost·latency·capacity budget

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A6-3. deployment·canary·rollback

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### A6-4. feedback loop·governance·incident review

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
