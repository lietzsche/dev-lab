# Production LLM & Agent Systems

평가·추적·복구·승인 가능한 LLM/agent를 설계하기 위한 독립 학습 브랜치다.

이 브랜치는 `learn/llm-systems` 전용이며 다른 과목 브랜치나 `main`으로 병합하지 않는다. 전체 순서는 [STUDY_ROADMAP.md](STUDY_ROADMAP.md)를 따른다.

## 범위

- 대상: Java/Spring 5년 차, Python·데이터·AI workflow 실무 확장 중
- 선수지식: Python·Data·분산 기초
- 결과물: 조사 agent의 eval·trace·approval·비용 검증
- 구성: 6단계, 24소단원

## 환경

provider 중립 fixture, 유료 API 선택. 현재는 계획과 검증 계약만 준비하며 단원별 최소 의존성만 추가한다. 전역 설치, 실제 cloud·계정·유료 API 변경은 자동 수행하지 않는다.

## 학습 루프

```text
내부 모델 → 최소 실습 → 상태 관찰 → 실패 재현 → 진단·복구 → 완료 증거
```

문서: [CURRICULUM.md](CURRICULUM.md), [PROGRESS.md](PROGRESS.md), [AGENTS.md](AGENTS.md)

```bash
./scripts/check.sh
```
