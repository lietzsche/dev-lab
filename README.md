# Java Fundamentals & VS Code Development

VS Code 개발 환경 세팅부터 Java의 타입 시스템, 객체지향, 예외, 컬렉션, 함수형 프로그래밍까지 언어의 핵심 기본기를 상태와 불변식 관점에서 견고하게 다지는 독립 학습 브랜치다.

이 브랜치는 `learn/java-fundamentals` 전용이며 다른 과목 브랜치나 `main`으로 병합하지 않는다. 전체 순서는 [STUDY_ROADMAP.md](STUDY_ROADMAP.md)를 따른다.

## 범위

- 대상: VS Code 개발 환경 구성 및 Java 핵심 기본기를 체계적으로 재정립하려는 엔지니어
- 선수지식: 프로그래밍 기본 개념 (변수, 조건문, 반복문, 함수)
- 결과물: VS Code 환경에서 Gradle 기반의 컴파일·테스트·디버깅 및 핵심 불변식 검증 완료
- 구성: 6단계, 30소단원

## 환경

JDK 17/21 LTS, Gradle, VS Code (Extension Pack for Java).
단원별 최소 의존성과 프로젝트 설정을 유지하며 전역 설치나 실제 cloud/계정 변경은 자동 수행하지 않는다.

## 학습 루프

```text
환경/원리 이해 → 최소 실습 → 상태 관찰 → 실패 재현 → 진단·복구 → 완료 증거
```

문서: [CURRICULUM.md](CURRICULUM.md), [PROGRESS.md](PROGRESS.md), [AGENTS.md](AGENTS.md)

```bash
./scripts/check.sh
```
