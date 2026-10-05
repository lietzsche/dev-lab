# Legacy Capital Migration Lab

오래 운영된 캐피탈 업무 시스템을 인수해 JDK와 Spring 생태계를 단계적으로 전환하는 실전 훈련 저장소다. Java/Spring 문법 학습이 아니라 현행 분석, 호환성 판단, 장애 조사, 회귀 검증과 전환 의사결정에 집중한다.

## 시스템 개요

`Legacy Capital`은 고객 심사, 계약 조회, 일 마감 배치와 외부 신용평가 연계를 제공하는 Maven multi-module 애플리케이션이다.

| 모듈 | 책임 | 실행 형태 |
|---|---|---|
| `capital-common` | 공통 도메인과 식별자/직렬화 규칙 | JAR |
| `credit-integration` | 외부 신용평가 시스템 연계 | JAR |
| `customer-api` | 고객·계약 REST API와 영속성 | 실행 JAR / WAR |
| `settlement-batch` | 일 마감 정산 작업 | 실행 JAR |

## 기준 환경

- JDK 8
- Maven 3.6.x
- Spring Boot 2.1.x
- 내장 H2 데이터베이스

학습에 필요한 JDK와 Maven은 Docker image로 고정되어 있다. 로컬에 JDK나 Maven을 별도로 설치할 필요가 없다.

기존 운영 기준선은 아래 명령으로 검증한다.

```bash
./scripts/verify-baseline.sh --docker
```

두 JDK에서 동일한 전체 build를 실행하는 공통 진입점도 제공한다.

```bash
./scripts/build-with-jdk.sh 8
./scripts/build-with-jdk.sh 17
```

두 번째 명령은 현재 작업에서 지시하기 전까지 먼저 실행하지 않는다. 각 작업은 [PROGRESS.md](PROGRESS.md)에 하나씩 공개된다.

API 실행:

```bash
./scripts/run-customer-api.sh --docker 8
curl http://localhost:8080/actuator/health
curl http://localhost:8080/api/customers/CUST-1001
```

batch 실행:

```bash
./scripts/run-settlement-batch.sh --docker 8
```

## 진행 방법

- [PROGRESS.md](PROGRESS.md)의 현재 작업 하나만 수행한다.
- 명령의 전체 출력에서 성공·실패가 발생한 경계를 먼저 관찰한다.
- 결과를 Codex에게 전달하면 저장소 상태와 함께 검토한다.
- 막히면 `힌트 1`부터 요청한다.
- 현재 작업이 확인되기 전에는 다음 migration 문제나 해결책을 공개하지 않는다.

전체 역량 순서는 [CURRICULUM.md](CURRICULUM.md), AI와의 운영 규칙은 [AGENTS.md](AGENTS.md)를 따른다.
