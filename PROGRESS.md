# Java Fundamentals & VS Code Development 진도표

## 진행 원칙

- 한 번에 한 소단원만 진행한다.
- 시작할 때 해당 단원만 `진행 중`으로 바꾼다.
- 예측·관찰·실패 재현·복구·회귀 검증 후 `완료`로 바꾼다.
- 사용자가 `넘어가자`고 하기 전에는 다음 단원을 시작하지 않는다.

## 현황

| ID | 소단원 | 목표 | 선행 | 상태 | 완료일 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **JF1-1** | JDK·CLI compile·execute | `javac`, `java`, classpath `-cp`의 동작 원리를 이해하고 CLI에서 컴파일 및 실행 검증 | - | 대기 | - |
| **JF1-2** | VS Code Java environment & LSP | Eclipse JDT Language Server, settings.json, workspaceStorage 캐시의 구조를 이해하고 환경 구축 | JF1-1 | 대기 | - |
| **JF1-3** | Package structure & naming boundary | 패키지 선언, 디렉터리 계층 매핑, 식별자 명명 규칙과 컴파일러 패키지 검증 | JF1-2 | 대기 | - |
| **JF1-4** | Build tool & dependency management | Gradle 빌드 생명주기, sourceSets, 의존성 resolution, JAR 패키징 검증 | JF1-3 | 대기 | - |
| **JF1-5** | VS Code test & debug workflow | JUnit 테스트 러너 연동, breakpoint 설정, 스택 프레임 및 변수 인스펙션 검증 | JF1-4 | 대기 | - |
| **JF2-1** | Primitive types vs Reference types | 원시 타입과 참조 타입의 메모리 배치(스택 vs 힙) 및 Pass-by-value 불변식 검증 | JF1-5 | 대기 | - |
| **JF2-2** | String pool & immutability | 문자열 리터럴 풀, 불변 객체 특성, `==` vs `.equals()`, StringBuilder 버퍼링 검증 | JF2-1 | 대기 | - |
| **JF2-3** | Arrays & boundary invariants | 연속 메모리 할당, 0-indexed 불변식, `ArrayIndexOutOfBoundsException`과 다차원 배열 참조 검증 | JF2-2 | 대기 | - |
| **JF2-4** | Wrapper classes & Autoboxing traps | 박싱/언박싱 비용, 캐싱 범위(-128~127), NullPointerException(NPE) 함정 검증 | JF2-3 | 대기 | - |
| **JF2-5** | Constants & Enums | `static final` 상수, 타입 세이프 enum의 내부 클래스 모델과 인스턴스 상태 검증 | JF2-4 | 대기 | - |
| **JF3-1** | Class anatomy & lifecycle | 필드, 생성자 오버로딩, `this()`, 인스턴스 초기화 블록의 실행 순서 검증 | JF2-5 | 대기 | - |
| **JF3-2** | Encapsulation & Access control | `private`, default(package-private), `protected`, `public`의 패키지/상속 접근 경계 검증 | JF3-1 | 대기 | - |
| **JF3-3** | Inheritance & Polymorphism | `extends`, 메서드 오버라이딩(`@Override`), `super`, 동적 바인딩과 다형적 참조 검증 | JF3-2 | 대기 | - |
| **JF3-4** | Abstract class vs Interface | 상태 템플릿(추상 클래스) vs 순수 계약(인터페이스), default method와 다중 구현 충돌 검증 | JF3-3 | 대기 | - |
| **JF3-5** | Record & Immutability | Java 16+ record의 불변 데이터 모델, 컴파일러 자동 생성 메서드, 컴팩트 생성자 검증 | JF3-4 | 대기 | - |
| **JF4-1** | Exception hierarchy | `Throwable`, `Error`, `Exception`, `RuntimeException`의 계층 구조와 발생 원인 분석 | JF3-5 | 대기 | - |
| **JF4-2** | Checked vs Unchecked exceptions | 컴파일 타임 계약(`throws`) vs 런타임 버그(`RuntimeException`), 예외 변환 패턴 검증 | JF4-1 | 대기 | - |
| **JF4-3** | Resource management & try-with-resources | `AutoCloseable`, 자원 해제 순서, suppressed exceptions 누락 방지 검증 | JF4-2 | 대기 | - |
| **JF4-4** | Custom exceptions & error propagation | 도메인 예외 정의, root cause stack trace 보존, 예외 래핑 기법 검증 | JF4-3 | 대기 | - |
| **JF4-5** | Defensive programming & assertions | `Objects.requireNonNull`, 사전 조건/사후 조건 불변식 검증 및 실패 모델 수립 | JF4-4 | 대기 | - |
| **JF5-1** | Generics syntax & Type erasure | 제네릭 타입 파라미터, 컴파일 타임 타입 검사와 런타임 타입 소거(Type Erasure) 검증 | JF4-5 | 대기 | - |
| **JF5-2** | Wildcards & Variance | 상한 와일드카드(`? extends T`), 하한 와일드카드(`? super T`), PECS 원칙 검증 | JF5-1 | 대기 | - |
| **JF5-3** | List interface & implementation trade-offs | `ArrayList`(연속 메모리/랜덤 액세스) vs `LinkedList`(노드 포인터/삽입삭제) 성능 트레이드오프 검증 | JF5-2 | 대기 | - |
| **JF5-4** | Set & Map contract | `hashCode()`와 `equals()` 불변식 계약, 해시 충돌과 버킷 체이닝 동작 검증 | JF5-3 | 대기 | - |
| **JF5-5** | Sorting & Comparators | `Comparable`(자연 순서) vs `Comparator`(외부 주입 전략), 정렬 안정성과 불변식 검증 | JF5-4 | 대기 | - |
| **JF6-1** | Lambda expressions & Functional interfaces | `@FunctionalInterface`, 익명 클래스와 람다의 인스턴스화 차이, 렉시컬 스코프 검증 | JF5-5 | 대기 | - |
| **JF6-2** | Stream pipeline fundamentals | 지연 연산(Lazy evaluation), 중간 연산(Intermediate) vs 최종 연산(Terminal) 실행 시점 검증 | JF6-1 | 대기 | - |
| **JF6-3** | Stream collectors & reductions | `Collectors.toList/toMap/groupingBy`, `reduce` 연산과 불변 컬렉션 변환 검증 | JF6-2 | 대기 | - |
| **JF6-4** | Optional & Null safety | `Optional` 래핑, `orElse` vs `orElseGet` 평가 시점 차이, 올바른 안티패턴 방지 검증 | JF6-3 | 대기 | - |
| **JF6-5** | Modern I/O & Path operations | `java.nio.file.Path`, `Files`, 스트림 기반 파일 읽기/쓰기 및 안전한 I/O 처리 검증 | JF6-4 | 대기 | - |

## 세부 기록

### JF1-1. JDK·CLI compile·execute

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF1-2. VS Code Java environment & LSP

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF1-3. Package structure & naming boundary

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF1-4. Build tool & dependency management

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF1-5. VS Code test & debug workflow

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF2-1. Primitive types vs Reference types

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF2-2. String pool & immutability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF2-3. Arrays & boundary invariants

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF2-4. Wrapper classes & Autoboxing traps

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF2-5. Constants & Enums

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF3-1. Class anatomy & lifecycle

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF3-2. Encapsulation & Access control

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF3-3. Inheritance & Polymorphism

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF3-4. Abstract class vs Interface

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF3-5. Record & Immutability

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF4-1. Exception hierarchy

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF4-2. Checked vs Unchecked exceptions

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF4-3. Resource management & try-with-resources

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF4-4. Custom exceptions & error propagation

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF4-5. Defensive programming & assertions

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF5-1. Generics syntax & Type erasure

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF5-2. Wildcards & Variance

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF5-3. List interface & implementation trade-offs

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF5-4. Set & Map contract

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF5-5. Sorting & Comparators

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF6-1. Lambda expressions & Functional interfaces

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF6-2. Stream pipeline fundamentals

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF6-3. Stream collectors & reductions

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF6-4. Optional & Null safety

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:

### JF6-5. Modern I/O & Path operations

- 계획:
- 예측:
- 관찰 증거:
- 실패와 복구:
- 배운 점:
