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

기준선은 아래 명령으로 검증한다.

```bash
./scripts/verify-baseline.sh
```

로컬에 기준 JDK와 Maven이 없다면 Docker를 사용할 수 있다.

```bash
./scripts/verify-baseline.sh --docker
```

API 실행:

```bash
./scripts/run-customer-api.sh --docker
curl http://localhost:8080/actuator/health
curl http://localhost:8080/api/customers/CUST-1001
```

현재 고객 요청과 진행 상태는 [PROGRESS.md](PROGRESS.md)를 따른다. 전체 단계의 상세 장애나 정답은 저장소 문서에 제공하지 않는다.
