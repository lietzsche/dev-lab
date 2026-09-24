# Linux Internals & Operations AI 페어 프로그래밍 지침

- 시작 시 `CURRICULUM.md`와 `PROGRESS.md`를 읽고 한 번에 `L1-1` 같은 한 단원만 진행한다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.
- Java/Spring 입문을 반복하지 않고 JVM·transaction·불변 값·reference·thread·GC와 비교한다.
- Python·Databricks·LLM workflow 실무와 연결하고 상태·경계·불변식·실패·복구를 우선한다.
- 실행 결과를 확인한 뒤 다음 개념으로 간다. 첫 요청은 방향, 두 번째는 구체적 힌트, 요청 시 정답과 해설을 준다.
- 위험한 실습은 전용 sandbox/container/local cluster/fixture에서 수행한다.
- 실제 cloud·운영 cluster·유료 API·계정 권한은 명시적 요청 없이 변경하지 않는다.
- 특정 사용자 홈·drive·mount 경로를 하드코딩하지 않는다.
- 완료 시 관찰·실패·복구를 진도표에 기록하고 `./scripts/check.sh`를 통과한다.
