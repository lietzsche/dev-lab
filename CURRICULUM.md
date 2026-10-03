# JDK Migration 실전 훈련 로드맵

이 과정은 하나의 레거시 시스템을 실제로 변경하고 검증하는 방식으로 진행한다. 각 Phase의 구체적인 문제는 앞서 공개하지 않는다.

1. 현행 시스템 파악 및 JDK 8 → 17 전환
2. compile/build/runtime 장애 분석
3. Spring Framework / Spring Boot 전환
4. Java EE `javax` → Jakarta 생태계 전환
5. WAS / Servlet / Framework 호환성 검토
6. JDK 17 → 21 전환
7. dependency 및 runtime 복합 장애 분석
8. 회귀 테스트와 migration 검증
9. AA 관점의 영향도·위험·일정·전환 계획
10. 별도 레거시 시스템 종합 migration

진행 원칙은 `경험 → 실패 → 관찰 → 조사 → 가설 → 수정 → 실행 → 검증 → 개념화`다. 한 번에 고객 요청 하나만 수행하며, 해결 후에만 원인과 migration 원칙을 짧게 정리한다.
