# 훈련 진행 상황

## 현재 위치

- 과정: JDK Migration 실전 훈련
- Phase: 1 — 현행 파악과 JDK 8 → 17
- 작업: P1-1 — JDK 8 기준선 확인
- 상태: 진행 중
- 시작 기준점: `learn/jdk-migration`

## 현재 작업

인수한 시스템이 기존 운영 환경에서 정상인지 먼저 확인한다.

저장소 루트에서 다음 명령을 실행하라.

```bash
./scripts/verify-baseline.sh --docker
```

아직 source나 build 설정은 변경하지 않는다. 실행이 끝나면 다음 세 가지만 확인해 알려준다.

1. 실제 Java와 Maven 버전
2. reactor에 포함된 module과 각 결과
3. 전체 build의 최종 결과

## 완료 판정

Codex가 실제 실행 결과와 저장소 변경 여부를 확인한다. 기준선이 확인되면 P1-1을 완료 처리하고 다음 작업 하나만 공개한다.
