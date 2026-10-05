# JDK Migration 실전 훈련 로드맵

## 과정 목표

이 과정의 목표는 새 JDK 문법을 배우는 것이 아니다. 운영 중인 Java/Spring 시스템을 인수해 현행을 파악하고, 실패를 재현하고, 변경 범위와 위험을 통제하면서 JDK와 framework를 전환하는 경험을 쌓는다.

완료 시 다음 업무를 독립적으로 수행할 수 있어야 한다.

- JDK, framework, library, build plugin과 WAS의 호환성을 조사한다.
- compile, test, packaging, startup, request 처리 중 어느 경계에서 실패했는지 구분한다.
- 직접 dependency와 transitive dependency를 함께 분석한다.
- 최소 변경과 선제 업그레이드 사이의 trade-off를 설명한다.
- 회귀 범위, rollout, rollback과 운영 위험을 포함한 전환 계획을 작성한다.

## 학습 운영 방식

각 Phase는 하나의 큰 과제가 아니라 여러 개의 짧은 작업으로 진행한다. 저장소에는 항상 현재 작업 하나만 공개한다.

```text
실행하여 현상 경험
→ 로그·build·dependency 관찰
→ 실패 경계 분류
→ 원인 후보 조사와 가설 수립
→ 최소 변경
→ 같은 조건으로 재실행
→ test·runtime·회귀 검증
→ 해결 후 migration 원칙 정리
```

Codex는 실행 환경과 실패 사례를 준비하지만 핵심 migration 변경은 먼저 구현하지 않는다. 학습자가 실행 결과를 공유하면 현재 작업을 검토하고, 통과한 경우에만 다음 작업을 연다.

힌트는 관찰 지점 → 문제 영역 → 관련 기술 → 동작 원리 → 구체적인 해결 방향 순으로 한 단계씩 제공한다.

## Phase 1. 현행 파악과 JDK 8 → 17

목표:

- 기존 JDK 8 기준선이 무엇을 보장하는지 확인한다.
- 같은 source를 JDK 17에서 실행해 최초 실패 경계를 식별한다.
- compile 성공, test 성공, packaging 성공, 실제 기동 성공을 서로 다른 검증으로 다룬다.
- 변경 전후의 dependency와 실행 환경을 증거로 남긴다.

완료 기준:

- 모든 module을 JDK 17에서 build하고 test한다.
- API와 batch를 JDK 17에서 실제 실행한다.
- 대표 REST 요청과 주요 batch 결과를 회귀 검증한다.
- 변경 이유와 남은 위험을 짧게 설명한다.

## Phase 2. JDK 변경에 따른 build·runtime 장애

- compiler와 runtime이 제공하는 API의 차이를 구분한다.
- build plugin, annotation processing, reflection과 JVM option 문제를 실패 시점별로 분석한다.
- 임시 우회와 유지보수 가능한 해결책을 비교한다.

## Phase 3. Spring Framework / Spring Boot 전환

- JDK 지원 범위와 Spring release line의 관계를 조사한다.
- BOM과 dependency management가 실제 선택 버전에 미치는 영향을 확인한다.
- framework upgrade에 따른 configuration과 기본 동작 변화를 회귀 테스트로 찾는다.

## Phase 4. Java EE `javax` → Jakarta 생태계 전환

- package rename을 단순 문자열 교체가 아닌 ecosystem 전환으로 다룬다.
- persistence, validation, servlet, serialization 경계를 함께 검증한다.
- 혼합된 API 세대가 compile과 runtime에 만드는 문제를 분석한다.

## Phase 5. WAS / Servlet / Framework 호환성

- embedded 실행과 외부 WAS 배포의 classloader 및 dependency 차이를 확인한다.
- Servlet spec, WAR packaging, provided dependency와 운영 설정을 함께 검토한다.
- 로컬 성공이 운영 배포 성공을 보장하지 않는 사례를 해결한다.

## Phase 6. JDK 17 → 21

- 이미 한 번 전환된 시스템을 다시 평가한다.
- JDK, framework, library 지원 정책을 근거로 목표 조합을 선택한다.
- 성능·관찰 가능성·운영 option을 기능 회귀와 분리해 검증한다.

## Phase 7. 복합 dependency와 runtime 장애

- dependency tree와 실제 runtime classpath의 차이를 조사한다.
- transitive dependency 충돌, logging binding, serialization 호환 문제를 해결한다.
- dependency override가 다른 module에 미치는 영향을 확인한다.

## Phase 8. 회귀 테스트와 migration 검증

- 기존 test가 잡지 못하는 migration 위험을 식별한다.
- API, database, batch, 외부 연계와 packaging 경계의 검증 전략을 보강한다.
- 재현 가능한 migration verification 명령을 만든다.

## Phase 9. Application Architect 전환 계획

- 실제로 겪은 장애를 dependency inventory, compatibility matrix와 risk register로 연결한다.
- migration 순서, 병행 개발, rollout, rollback과 지원 종료 위험을 판단한다.
- 개발팀이 사용할 수 있는 migration guide와 장애 대응 기준을 작성한다.

## Phase 10. 독립 종합 migration

이전 실습과 다른 레거시 시스템을 고객 요구사항만으로 분석한다. 목표 환경 선정, 영향도 분석, 실제 migration, 검증과 개발자 가이드 제출까지 독립적으로 수행하며 Codex는 리뷰어 역할만 한다.
