# Java Fundamentals & VS Code Development 커리큘럼

## 과정 목표

VS Code 개발 환경 세팅부터 Java의 타입 시스템, 객체지향, 예외, 컬렉션, 함수형 프로그래밍까지 언어의 핵심 기본기를 상태와 불변식 관점에서 견고하게 다진다. 완료 시 다음 질문에 자신의 실습 증거로 답할 수 있어야 한다.

- Development Environment & Project Model 단계에서 VS Code LSP, 패키지 계층, Gradle 빌드 구조를 설명하고 문제를 진단할 수 있는가?
- Type System & Memory Primitives 단계에서 원시 타입과 참조 타입의 메모리 배치, 불변식, 캐싱 범위를 증명할 수 있는가?
- Object-Oriented Principles & Design 단계에서 캡슐화 경계, 상속/다형성, 인터페이스 다중 구현, Record 불변 모델을 설계할 수 있는가?
- Exception & Resource Lifecycle 단계에서 예외 계층, 자원 자동 해제(try-with-resources), 방어적 프로그래밍을 구현할 수 있는가?
- Generics & Collection Architecture 단계에서 Type Erasure, PECS 원칙, List/Set/Map의 내부 계약을 검증할 수 있는가?
- Modern Java & Functional I/O 단계에서 람다, 스트림 지연 연산, Optional null safety, NIO 파일 파이프라인을 작성할 수 있는가?

## 설계 기준

- 단순 문법 암기를 지양하고 컴파일러 검증, 메모리 상태(스택/힙), 불변식, 런타임 실패와 복구를 우선한다.
- 정상 경로마다 컴파일 에러 또는 런타임 예외 실패 실험을 짝지어 학습한다.
- 한 단계는 관찰 가능한 결과물로 끝나며 사용자가 `넘어가자`고 할 때만 다음 단계로 간다.
- 전체 범위: 30소단원.

## 단계 지도

| 단계 | 주제 | 단원 수 | 단계 결과 |
| :--- | :--- | ---: | :--- |
| **JF1** | Development Environment & Project Model | 5 | VS Code와 CLI, Gradle 빌드 환경을 구축하고 검증 |
| **JF2** | Type System & Memory Primitives | 5 | 기본 타입, 참조 타입, 문자열 풀과 메모리 불변식을 설명 |
| **JF3** | Object-Oriented Principles & Design | 5 | 클래스 생명주기, 접근 제어, 다형성, 인터페이스, Record를 설계 |
| **JF4** | Exception & Resource Lifecycle | 5 | 예외 계층, 자원 자동 해제, 방어적 프로그래밍과 복구 전략을 수립 |
| **JF5** | Generics & Collection Architecture | 5 | 타입 소거, PECS, List/Set/Map 내부 구조와 계약을 검증 |
| **JF6** | Modern Java & Functional I/O | 5 | 람다, 스트림 지연 연산, Optional, 최신 NIO 파일 처리를 구현 |

## 소단원 지도

| ID | 소단원 | 목표 | 선행 |
| :--- | :--- | :--- | :--- |
| **JF1-1** | JDK·CLI compile·execute | `javac`, `java`, classpath `-cp`의 동작 원리를 이해하고 CLI에서 컴파일 및 실행 검증 | - |
| **JF1-2** | VS Code Java environment & LSP | Eclipse JDT Language Server, settings.json, workspaceStorage 캐시의 구조를 이해하고 환경 구축 | JF1-1 |
| **JF1-3** | Package structure & naming boundary | 패키지 선언, 디렉터리 계층 매핑, 식별자 명명 규칙과 컴파일러 패키지 검증 | JF1-2 |
| **JF1-4** | Build tool & dependency management | Gradle 빌드 생명주기, sourceSets, 의존성 resolution, JAR 패키징 검증 | JF1-3 |
| **JF1-5** | VS Code test & debug workflow | JUnit 테스트 러너 연동, breakpoint 설정, 스택 프레임 및 변수 인스펙션 검증 | JF1-4 |
| **JF2-1** | Primitive types vs Reference types | 원시 타입과 참조 타입의 메모리 배치(스택 vs 힙) 및 Pass-by-value 불변식 검증 | JF1-5 |
| **JF2-2** | String pool & immutability | 문자열 리터럴 풀, 불변 객체 특성, `==` vs `.equals()`, StringBuilder 버퍼링 검증 | JF2-1 |
| **JF2-3** | Arrays & boundary invariants | 연속 메모리 할당, 0-indexed 불변식, `ArrayIndexOutOfBoundsException`과 다차원 배열 참조 검증 | JF2-2 |
| **JF2-4** | Wrapper classes & Autoboxing traps | 박싱/언박싱 비용, 캐싱 범위(-128~127), NullPointerException(NPE) 함정 검증 | JF2-3 |
| **JF2-5** | Constants & Enums | `static final` 상수, 타입 세이프 enum의 내부 클래스 모델과 인스턴스 상태 검증 | JF2-4 |
| **JF3-1** | Class anatomy & lifecycle | 필드, 생성자 오버로딩, `this()`, 인스턴스 초기화 블록의 실행 순서 검증 | JF2-5 |
| **JF3-2** | Encapsulation & Access control | `private`, default(package-private), `protected`, `public`의 패키지/상속 접근 경계 검증 | JF3-1 |
| **JF3-3** | Inheritance & Polymorphism | `extends`, 메서드 오버라이딩(`@Override`), `super`, 동적 바인딩과 다형적 참조 검증 | JF3-2 |
| **JF3-4** | Abstract class vs Interface | 상태 템플릿(추상 클래스) vs 순수 계약(인터페이스), default method와 다중 구현 충돌 검증 | JF3-3 |
| **JF3-5** | Record & Immutability | Java 16+ record의 불변 데이터 모델, 컴파일러 자동 생성 메서드, 컴팩트 생성자 검증 | JF3-4 |
| **JF4-1** | Exception hierarchy | `Throwable`, `Error`, `Exception`, `RuntimeException`의 계층 구조와 발생 원인 분석 | JF3-5 |
| **JF4-2** | Checked vs Unchecked exceptions | 컴파일 타임 계약(`throws`) vs 런타임 버그(`RuntimeException`), 예외 변환 패턴 검증 | JF4-1 |
| **JF4-3** | Resource management & try-with-resources | `AutoCloseable`, 자원 해제 순서, suppressed exceptions 누락 방지 검증 | JF4-2 |
| **JF4-4** | Custom exceptions & error propagation | 도메인 예외 정의, root cause stack trace 보존, 예외 래핑 기법 검증 | JF4-3 |
| **JF4-5** | Defensive programming & assertions | `Objects.requireNonNull`, 사전 조건/사후 조건 불변식 검증 및 실패 모델 수립 | JF4-4 |
| **JF5-1** | Generics syntax & Type erasure | 제네릭 타입 파라미터, 컴파일 타임 타입 검사와 런타임 타입 소거(Type Erasure) 검증 | JF4-5 |
| **JF5-2** | Wildcards & Variance | 상한 와일드카드(`? extends T`), 하한 와일드카드(`? super T`), PECS 원칙 검증 | JF5-1 |
| **JF5-3** | List interface & implementation trade-offs | `ArrayList`(연속 메모리/랜덤 액세스) vs `LinkedList`(노드 포인터/삽입삭제) 성능 트레이드오프 검증 | JF5-2 |
| **JF5-4** | Set & Map contract | `hashCode()`와 `equals()` 불변식 계약, 해시 충돌과 버킷 체이닝 동작 검증 | JF5-3 |
| **JF5-5** | Sorting & Comparators | `Comparable`(자연 순서) vs `Comparator`(외부 주입 전략), 정렬 안정성과 불변식 검증 | JF5-4 |
| **JF6-1** | Lambda expressions & Functional interfaces | `@FunctionalInterface`, 익명 클래스와 람다의 인스턴스화 차이, 렉시컬 스코프 검증 | JF5-5 |
| **JF6-2** | Stream pipeline fundamentals | 지연 연산(Lazy evaluation), 중간 연산(Intermediate) vs 최종 연산(Terminal) 실행 시점 검증 | JF6-1 |
| **JF6-3** | Stream collectors & reductions | `Collectors.toList/toMap/groupingBy`, `reduce` 연산과 불변 컬렉션 변환 검증 | JF6-2 |
| **JF6-4** | Optional & Null safety | `Optional` 래핑, `orElse` vs `orElseGet` 평가 시점 차이, 올바른 안티패턴 방지 검증 | JF6-3 |
| **JF6-5** | Modern I/O & Path operations | `java.nio.file.Path`, `Files`, 스트림 기반 파일 읽기/쓰기 및 안전한 I/O 처리 검증 | JF6-4 |

## JF1. Development Environment & Project Model

- 관찰 축: CLI compile·classpath·LSP·package hierarchy·Gradle
- 통합 실습: VS Code와 CLI 환경에서 컴파일·실행·디버깅 파이프라인 검증
- 핵심 실패: package mismatch·classpath unresolved·LSP cache corruption

### [JF1-1] JDK·CLI compile·execute

- 이해할 것: `javac` 컴파일러와 `java` 실행기의 역할, 클래스패스(`-cp`) 탐색 원리와 바이트코드(`.class`) 생성.
- 직접 관찰: `javac -d`, `java -cp` 실행 시 클래스 파일 생성 위치와 클래스로더의 탐색 경로를 확인한다.
- 실습: CLI 환경에서 단일 클래스를 컴파일하고 클래스패스를 지정하여 실행한다.
- 실패 실험: 클래스패스가 누락되었을 때 발생하는 `ClassNotFoundException` / `NoClassDefFoundError`를 재현하고 복구한다.
- 완료 기준: CLI 기반 컴파일 및 클래스패스 지정 실행 결과를 증거로 확인하고 설명한다.

### [JF1-2] VS Code Java environment & LSP

- 이해할 것: VS Code Java 확장(Language Support for Java by Red Hat)의 Eclipse JDT Language Server 구동 모델과 캐시 구조.
- 직접 관찰: `.vscode/settings.json`, `workspaceStorage` 캐시 디렉터리, JDT LS 로그(`.metadata/.log`) 상태를 확인한다.
- 실습: 불필요한 비자바 폴더(`.venv`, `.git`) 스캔을 차단하고 소스 폴더를 정확히 등록하여 언어 서버를 안정화한다.
- 실패 실험: 대용량 폴더 스캔으로 인한 `Initialize Workspace` 멈춤 현상을 재현하고 캐시 정리 및 필터링으로 복구한다.
- 완료 기준: VS Code에서 코드 편집 시 자동완성, 정의 이동, 에러 진단이 지연 없이 동작함을 확인한다.

### [JF1-3] Package structure & naming boundary

- 이해할 것: Java 패키지 명명 규칙(유효 식별자), 디렉터리 계층 구조와 FQCN(Fully Qualified Class Name) 매핑 불변식.
- 직접 관찰: 패키지 선언과 실제 파일 시스템 디렉터리 경로의 일치 여부를 컴파일러 및 IDE 진단 메시지로 확인한다.
- 실습: 다중 패키지 구조를 구성하고 서로 다른 패키지 간의 클래스를 `import`하여 컴파일 및 실행한다.
- 실패 실험: 디렉터리 이름에 하이픈(`-`)이 포함되거나 선언된 패키지와 경로가 다를 때의 컴파일 에러를 재현하고 복구한다.
- 완료 기준: 패키지 식별자 규칙을 준수하는 디렉터리 구조에서 정상적으로 상호 참조가 이루어짐을 검증한다.

### [JF1-4] Build tool & dependency management

- 이해할 것: 빌드 도구(Gradle)의 기본 프로젝트 모델, 표준 디렉터리 레이아웃(`src/main/java`), 태스크 실행 생명주기.
- 직접 관찰: `build.gradle` 설정과 `gradle build` 실행 시 생성되는 산출물(`build/classes`, `build/libs`)을 확인한다.
- 실습: 최소한의 Gradle 빌드 스크립트를 작성하고 CLI 및 VS Code에서 프로젝트로 인식시킨다.
- 실패 실험: 잘못된 의존성 좌표나 문법 오류로 인한 빌드 실패를 유도하고 로그를 통해 원인을 진단·복구한다.
- 완료 기준: Gradle을 통해 컴파일, 테스트, JAR 생성이 정상 완료됨을 확인한다.

### [JF1-5] VS Code test & debug workflow

- 이해할 것: Java Debug Server 프로토콜, 브레이크포인트 매커니즘, 스택 프레임 탐색 및 변수 검사.
- 직접 관찰: VS Code 디버거 창에서 Call Stack, Variables, Watch 패널의 실시간 상태 변화를 확인한다.
- 실습: JUnit 테스트 코드를 작성하고 VS Code Test Runner 및 디버거를 붙여 중단점에서 상태를 인스펙션한다.
- 실패 실험: 의도적인 논리 결함을 심고 디버거 변수 조작 및 단계별 실행(Step Over/Into)으로 결함을 찾아 수정한다.
- 완료 기준: 테스트 실행과 디버깅 중단점 검사가 정상 동작함을 확인한다.

### JF1 단계 결과물

- VS Code와 CLI, Gradle 빌드 환경을 구축하고 검증.
- 핵심 명령·출력·설정·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## JF2. Type System & Memory Primitives

- 관찰 축: primitive·reference·stack/heap·string pool·array·autoboxing
- 통합 실습: 값 전달 vs 참조 전달, 문자열 불변식, 박싱 비용 메모리 관찰
- 핵심 실패: NPE·out of bounds·caching mismatch·precision loss

### [JF2-1] Primitive types vs Reference types

- 이해할 것: 8가지 기본 타입(byte, short, int, long, float, double, boolean, char)과 참조 타입의 메모리 저장 방식(스택 vs 힙).
- 직접 관찰: 메서드 호출 시 인자 전달(Pass-by-value)에서 기본 타입의 값 복사와 참조 타입의 주소 복사 동작을 관찰한다.
- 실습: 메서드 내부에서 매개변수를 재할당하거나 상태를 변경했을 때 호출자의 변수 변화 유무를 비교 검증한다.
- 실패 실험: 참조 자체를 변경(재할당)했을 때 호출자에게 반영되지 않는 오해 시나리오를 재현하고 올바른 객체 상태 변경으로 복구한다.
- 완료 기준: Java가 순수 Pass-by-value로 동작함을 메모리 상태 다이어그램과 코드로 증명한다.

### [JF2-2] String pool & immutability

- 이해할 것: 문자열 불변성(Immutability), String Constant Pool, 리터럴 생성 vs `new String()` 생성 차이.
- 직접 관찰: `==`(주소 비교)와 `.equals()`(동등성 비교) 결과 차이 및 `intern()` 호출 결과를 확인한다.
- 실습: 반복문 내 `+` 연산과 `StringBuilder` 사용 시의 객체 생성 비용 및 실행 시간을 비교한다.
- 실패 실험: `==`로 문자열을 비교하여 발생하는 논리적 버그를 재현하고 `.equals()`로 안전하게 교체한다.
- 완료 기준: 문자열 풀의 주소 재사용과 불변 객체의 스레드 안전성 이점을 설명한다.

### [JF2-3] Arrays & boundary invariants

- 이해할 것: 고정 크기 연속 메모리 구조, 0-indexed 인덱싱, 다차원 배열의 배열-오브-배열 참조 모델.
- 직접 관찰: 배열 선언, 초기화, 메모리 할당 및 `length` 불변 필드 상태를 확인한다.
- 실습: 1차원 및 2차원 배열을 순회하고 조작하는 유틸리티 메서드를 구현한다.
- 실패 실험: 인덱스 경계를 벗어났을 때 발생하는 `ArrayIndexOutOfBoundsException`을 재현하고 방어 코드로 복구한다.
- 완료 기준: 배열의 크기 불변 제약과 경계 검사 불변식을 증명한다.

### [JF2-4] Wrapper classes & Autoboxing traps

- 이해할 것: 기본 타입의 래퍼 클래스(Integer, Long 등), 컴파일러의 자동 박싱/언박싱 메커니즘.
- 직접 관찰: Integer 캐시(-128 ~ 127) 범위 내외에서의 `==` 비교 결과와 언박싱 시 생성되는 바이트코드(`.intValue()`)를 확인한다.
- 실습: 대량 연산에서 `Long` vs `long`의 성능 차이 및 메모리 오버헤드를 측정한다.
- 실패 실험: null 참조인 래퍼 객체를 언박싱할 때 발생하는 `NullPointerException`을 재현하고 복구한다.
- 완료 기준: 래퍼 클래스 비교 시 `.equals()` 사용과 언박싱 NPE 방어 불변식을 확립한다.

### [JF2-5] Constants & Enums

- 이해할 것: `static final` 상수의 컴파일 타임 인라인 치환과 타입 세이프 `enum`의 클래스 기반 내부 구현.
- 직접 관찰: enum 상수들의 `ordinal()`, `name()`, 커스텀 필드 및 메서드 바인딩 상태를 확인한다.
- 실습: 상태와 행위를 캡슐화한 enum 타입을 정의하고 분기문(`switch`)에서 활용한다.
- 실패 실험: `ordinal()`에 의존하여 순서 변경 시 발생하는 비즈니스 오류를 재현하고 명시적 코드로 복구한다.
- 완료 기준: 단순 정수/문자열 상수 대신 enum을 활용한 타입 안정성 보장 설계를 검증한다.

### JF2 단계 결과물

- 기본 타입, 참조 타입, 문자열 풀과 메모리 불변식을 설명.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## JF3. Object-Oriented Principles & Design

- 관찰 축: encapsulation·inheritance·polymorphism·interface·record
- 통합 실습: 도메인 객체 모델링, 다형적 디스패치, 불변 DTO 검증
- 핵심 실패: tight coupling·LSP violation·immutable breach

### [JF3-1] Class anatomy & lifecycle

- 이해할 것: 인스턴스 변수, 클래스 변수(`static`), 생성자 체이닝(`this()`), 초기화 블록의 실행 순서.
- 직접 관찰: 객체 인스턴스화 시 static 블록, 인스턴스 블록, 생성자의 호출 순서와 기본값 초기화 과정을 로그로 확인한다.
- 실습: 필수 속성과 선택 속성을 안전하게 초기화하는 생성자 오버로딩 구조를 작성한다.
- 실패 실험: 생성자 내에서 오버라이딩 가능한 메서드를 호출하여 발생하는 미초기화 상태 읽기 버그를 재현하고 복구한다.
- 완료 기준: 객체 생성 시점의 필드 초기화 생명주기를 설명하고 검증한다.

### [JF3-2] Encapsulation & Access control

- 이해할 것: 4가지 접근 제어자(`private`, package-private, `protected`, `public`)와 정보 은닉(Information Hiding).
- 직접 관찰: 패키지 내부 및 외부, 상속 관계에서의 접근 가능 범위를 컴파일러 에러를 통해 확인한다.
- 실습: 내부 상태를 `private`으로 숨기고 유효성 검증을 거치는 접근자(getter/setter 또는 비즈니스 메서드)를 구현한다.
- 실패 실험: 가변 객체 필드를 외부로 그대로 노출하여 캡슐화가 깨지는 현상을 재현하고 방어적 복사(Defensive Copy)로 복구한다.
- 완료 기준: 클래스 외부에서 불변식을 임의로 훼손할 수 없도록 캡슐화 경계를 확립한다.

### [JF3-3] Inheritance & Polymorphism

- 이해할 것: `extends` 상속, 메서드 재정의(`@Override`), `super` 키워드, 부모 타입 참조를 통한 자식 인스턴스 다형성.
- 직접 관찰: 부모 타입 변수로 오버라이딩된 메서드를 호출할 때 실제 인스턴스의 메서드가 동적으로 실행됨을 확인한다.
- 실습: 공통 동작을 부모에 정의하고 서브클래스에서 구체적 행위를 재정의하는 상속 구조를 구현한다.
- 실패 실험: 잘못된 다운캐스팅으로 인한 `ClassCastException`을 재현하고 `instanceof` 패턴 매칭으로 안전하게 복구한다.
- 완료 기준: 리스코프 치환 원칙(LSP)을 준수하는 다형적 상속 구조를 검증한다.

### [JF3-4] Abstract class vs Interface

- 이해할 것: 추상 클래스(공통 상태/구현 재사용)와 인터페이스(역할과 계약의 분리, 다중 구현, default/static 메서드).
- 직접 관찰: 인터페이스 구현체의 메서드 시그니처 일치 여부 및 default 메서드 충돌 시 컴파일러 요구사항을 확인한다.
- 실습: 인터페이스 기반의 서비스 계약을 정의하고 다중 구현체를 주입받아 동작하는 구조를 구현한다.
- 실패 실험: 두 인터페이스에 동일한 시그니처의 default 메서드가 존재할 때 발생하는 충돌을 재현하고 명시적 재정의로 복구한다.
- 완료 기준: 추상 클래스와 인터페이스의 설계 목적 차이를 명확히 구분하고 적용한다.

### [JF3-5] Record & Immutability

- 이해할 것: Java 16+ `record`의 데이터 지향 모델, 자동 생성되는 컴포넌트 접근자, `equals()`, `hashCode()`, `toString()`.
- 직접 관찰: record 선언 시 컴파일러가 생성하는 불변 필드(`final`)와 바이트코드 구조를 확인한다.
- 실습: DTO(Data Transfer Object)와 값 객체(Value Object)를 record로 작성하고 컴팩트 생성자에서 유효성 검증을 수행한다.
- 실패 실험: record 내부에 가변 객체(예: List)가 포함되었을 때 불변성이 침해되는 사례를 재현하고 `List.copyOf`로 복구한다.
- 완료 기준: 보일러플레이트 없는 안전한 불변 데이터 모델을 설계하고 검증한다.

### JF3 단계 결과물

- 클래스 생명주기, 접근 제어, 다형성, 인터페이스, Record를 설계.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## JF4. Exception & Resource Lifecycle

- 관찰 축: throwable hierarchy·checked/unchecked·try-with-resources·defensive
- 통합 실습: 안전한 파일/스트림 처리, 예외 변환 및 전파, 도메인 예외 설계
- 핵심 실패: leak·swallowed exception·NPE·suppressed loss

### [JF4-1] Exception hierarchy

- 이해할 것: `Throwable` 하위의 `Error`(시스템 비정상)와 `Exception`(애플리케이션 처리 가능), `RuntimeException`의 분기점.
- 직접 관찰: 스택 트레이스 출력 구조(예외 메시지, 발생 라인, 호출 경로 체인)를 확인한다.
- 실습: 다양한 표준 예외(`IllegalArgumentException`, `IllegalStateException`)의 적절한 발생 상황을 구현한다.
- 실패 실험: `catch (Exception e) {}`로 예외를 무시(swallow)하여 문제 추적이 불가능해지는 버그를 재현하고 로깅/전파로 복구한다.
- 완료 기준: 예외 계층 구조와 스택 트레이스 해석 능력을 증명한다.

### [JF4-2] Checked vs Unchecked exceptions

- 이해할 것: Checked 예외(컴파일 타임 강제 처리)와 Unchecked 예외(런타임 프로그래밍 오류)의 철학과 선택 기준.
- 직접 관찰: `throws` 선언 누락 시 컴파일 에러 및 런타임 언체크드 예외 전파 양상을 확인한다.
- 실습: 저수준 Checked 예외(예: `IOException`)를 잡아서 의미 있는 도메인 Unchecked 예외로 전환(Wrapping)하는 패턴을 구현한다.
- 실패 실험: 예외를 감싸면서 원본 원인(cause)을 누락하여 root cause 정보가 유실되는 실수를 재현하고 `cause` 생성자로 복구한다.
- 완료 기준: 예외 전환 시 원본 스택 트레이스를 보존하는 표준 패턴을 확립한다.

### [JF4-3] Resource management & try-with-resources

- 이해할 것: `AutoCloseable` 인터페이스, try-with-resources 구문의 자동 해제 보장, Suppressed Exceptions 메커니즘.
- 직접 관찰: 정상 종료 및 예외 발생 시 자원의 `close()` 호출 순서(선언 역순)를 로그로 확인한다.
- 실습: 커스텀 `AutoCloseable` 리소스를 정의하고 try-with-resources 블록 내에서 안전하게 소비한다.
- 실패 실험: 기존 try-finally에서 finally 블록의 close 예외로 인해 본래의 비즈니스 예외가 덮어써지는 현상을 재현하고 복구한다.
- 완료 기준: 자원 누수(Leak) 없는 안전한 리소스 생명주기 관리 코드를 검증한다.

### [JF4-4] Custom exceptions & error propagation

- 이해할 것: 비즈니스 도메인 명확성을 위한 커스텀 예외 설계, 에러 코드 및 문맥 데이터 바인딩.
- 직접 관찰: 커스텀 예외 객체에 포함된 필드(에러 코드, 실패 파라미터)가 상위 호출자에게 전달되는 구조를 확인한다.
- 실습: 비즈니스 불변식 위반을 나타내는 커스텀 도메인 예외 클래스를 작성하고 검증 테스트를 구성한다.
- 실패 실험: 무분별한 커스텀 예외 남발로 인한 계층 오염을 진단하고 표준 예외와의 균형 잡힌 설계로 리팩터링한다.
- 완료 기준: 명확한 문맥 정보를 담는 도메인 예외 모델을 확립한다.

### [JF4-5] Defensive programming & assertions

- 이해할 것: 사전 조건(Pre-conditions) 검증, `Objects.requireNonNull`, 빠른 실패(Fail-fast) 원칙.
- 직접 관찰: 메서드 진입 시점에 유효하지 않은 인자를 차단했을 때와 지연 발생했을 때의 디버깅 난이도 차이를 확인한다.
- 실습: 모든 공개 메서드 진입부에 방어적 검증 로직을 작성하고 단위 테스트로 경계값을 검증한다.
- 실패 실험: null이 시스템 내부 깊숙한 곳까지 침투하여 엉뚱한 위치에서 NPE가 발생하는 현상을 재현하고 Fail-fast로 복구한다.
- 완료 기준: 객체 내부 불변식을 항상 유효한 상태로 유지하는 방어 코드를 검증한다.

### JF4 단계 결과물

- 예외 계층, 자원 자동 해제, 방어적 프로그래밍과 복구 전략을 수립.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## JF5. Generics & Collection Architecture

- 관찰 축: generics·type erasure·wildcard·List·Set·Map·equals/hashCode
- 통합 실습: 제네릭 자료구조 구현, 컬렉션 성능 비교, 해시 계약 검증
- 핵심 실패: ClassCastException·hash collision·PECS mismatch·raw type leak

### [JF5-1] Generics syntax & Type erasure

- 이해할 것: 컴파일 타임 타입 세이프티, 제네릭 클래스/메서드, 런타임에 타입 정보가 제거되는 타입 소거(Type Erasure).
- 직접 관찰: `javap -c`를 통해 제네릭 코드가 컴파일 후 `Object` 및 캐스팅 바이트코드(`checkcast`)로 변환됨을 확인한다.
- 실습: 임의의 타입을 안전하게 보관하고 반환하는 제네릭 컨테이너 클래스를 구현한다.
- 실패 실험: Raw type 사용으로 인해 컴파일러 경고를 무시하다 런타임에 `ClassCastException`이 터지는 상황을 재현하고 복구한다.
- 완료 기준: 런타임 오버헤드 없이 컴파일 타임 타입 검사를 제공하는 제네릭 원리를 설명한다.

### [JF5-2] Wildcards & Variance

- 이해할 것: 무공변(Invariant) 특성, 상한 와일드카드(`? extends T`), 하한 와일드카드(`? super T`), PECS(Producer Extends, Consumer Super).
- 직접 관찰: `List<Integer>`가 `List<Number>`의 하위 타입이 아님을 컴파일러 에러로 확인한다.
- 실습: 컬렉션에서 데이터를 읽기만 하는 메서드와 쓰기만 하는 메서드에 적절한 와일드카드를 적용한다.
- 실패 실험: `? extends T` 컬렉션에 원소를 `add()`하려다 발생하는 컴파일 에러를 관찰하고 PECS 원칙에 맞게 복구한다.
- 완료 기준: 유연하고 재사용성 높은 제네릭 API 메서드 시그니처를 설계하고 검증한다.

### [JF5-3] List interface & implementation trade-offs

- 이해할 것: `List` 계약, `ArrayList`(동적 배열, 랜덤 액세스 \(O(1)\)) vs `LinkedList`(이중 연결 리스트, 삽입/삭제 \(O(1)\)).
- 직접 관찰: 인덱스 기반 조회와 중간 원소 삽입 시 두 구현체의 실제 수행 시간과 메모리 캐시 지역성 차이를 측정한다.
- 실습: 워크로드 특성(조회 빈도 vs 삽입 빈도)에 따라 적절한 List 구현체를 선택하는 벤치마크 테스트를 작성한다.
- 실패 실험: `ArrayList` 크기 확장 시 발생하는 배열 복사 비용을 간과하여 발생하는 성능 저하를 초기 용량(`capacity`) 지정으로 복구한다.
- 완료 기준: 내부 데이터 구조에 기반한 자료구조 선택 기준을 수립한다.

### [JF5-4] Set & Map contract

- 이해할 것: `Set`(중복 불허)과 `Map`(키-값 매핑), `HashSet`/`HashMap`의 해싱 원리와 `hashCode()`, `equals()` 불변식.
- 직접 관찰: `hashCode()`가 동일할 때 발생하는 해시 충돌(Hash Collision)과 버킷 체이닝 동작을 확인한다.
- 실습: 커스텀 클래스를 Map의 키로 사용하기 위해 `equals()`와 `hashCode()`를 올바르게 오버라이딩한다.
- 실패 실험: `equals()`만 구현하고 `hashCode()`를 누락하여 동일한 키를 Map에서 찾지 못하는 버그를 재현하고 복구한다.
- 완료 기준: 해시 기반 컬렉션의 동작 계약 불변식을 증명한다.

### [JF5-5] Sorting & Comparators

- 이해할 것: 자연 순서(`Comparable<T>`), 외부 정렬 기준(`Comparator<T>`), 람다 기반의 `Comparator.comparing` 체이닝.
- 직접 관찰: 다중 정렬 조건(1차 정렬 후 동점자 2차 정렬)의 실행 순서와 안정 정렬(Stable Sort) 특성을 확인한다.
- 실습: 복합 비즈니스 도메인 객체 목록을 다양한 조건으로 정렬하는 테스트 코드를 구현한다.
- 실패 실험: `compareTo()` 구현 시 오버플로 가능성이 있는 뺄셈 연산(`a - b`) 버그를 재현하고 `Integer.compare()`로 안전하게 복구한다.
- 완료 기준: 정렬 계약(반사성, 반대칭성, 추이성)을 만족하는 안전한 정렬 로직을 검증한다.

### JF5 단계 결과물

- 타입 소거, PECS, List/Set/Map 내부 구조와 계약을 검증.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.

## JF6. Modern Java & Functional I/O

- 관찰 축: lambda·functional interface·stream pipeline·optional·NIO
- 통합 실습: 스트림 데이터 변환 파이프라인, 안전한 null 제어, 비차단 파일 I/O
- 핵심 실패: lazy evaluation misunderstanding·optional misuse·stream re-use error

### [JF6-1] Lambda expressions & Functional interfaces

- 이해할 것: `@FunctionalInterface`, 단 하나의 추상 메서드(SAM), 익명 클래스 vs 람다의 문법 및 바이트코드(`invokedynamic`) 차이.
- 직접 관찰: 표준 함수형 인터페이스(`Predicate`, `Function`, `Consumer`, `Supplier`)의 시그니처와 메서드 참조(`::`) 형태를 확인한다.
- 실습: 고차 함수(함수를 인자로 받거나 반환하는 메서드)를 설계하여 비즈니스 정책을 동적으로 주입한다.
- 실패 실험: 람다 본문에서 외부 지역 변수를 수정하려 할 때 발생하는 Effectively Final 제약 에러를 관찰하고 복구한다.
- 완료 기준: 함수형 프로그래밍 스타일을 활용한 간결하고 명확한 코드 분리를 구현한다.

### [JF6-2] Stream pipeline fundamentals

- 이해할 것: 스트림의 지연 연산(Lazy Evaluation), 데이터 소스 → 중간 연산(Intermediate) → 최종 연산(Terminal) 파이프라인 구조.
- 직접 관찰: 최종 연산이 호출되기 전까지는 중간 연산(`filter`, `map`)이 전혀 실행되지 않음을 로깅으로 확인한다.
- 실습: 컬렉션 데이터를 필터링하고 변환하는 파이프라인을 작성하고 루프 융합(Loop Fusion) 동작을 관찰한다.
- 실패 실험: 이미 닫힌 스트림을 재사용하려 할 때 발생하는 `IllegalStateException: stream has already been operated upon or closed`를 재현하고 복구한다.
- 완료 기준: 중간 연산과 최종 연산의 차이 및 단축 평가(Short-circuit) 원리를 검증한다.

### [JF6-3] Stream collectors & reductions

- 이해할 것: `reduce`를 통한 값 누적, `Collectors`를 통한 컬렉션 변환(`toList`, `toMap`, `groupingBy`, `partitioningBy`).
- 직접 관찰: 그룹핑 및 파티셔닝 결과로 생성되는 `Map<K, List<V>>` 또는 중첩 구조를 디버거로 확인한다.
- 실습: 복합 데이터셋을 특정 기준에 따라 집계하고 통계를 산출하는 집계 파이프라인을 구현한다.
- 실패 실험: `Collectors.toMap`에서 중복 키 충돌 시 발생하는 `IllegalStateException`을 재현하고 머지 함수(`(existing, replacement) -> ...`)로 복구한다.
- 완료 기준: 유연한 스트림 수집 및 축소 연산을 활용한 데이터 처리 파이프라인을 검증한다.

### [JF6-4] Optional & Null safety

- 이해할 것: `Optional<T>`의 설계 목적(값의 부재를 명시적으로 표현), `orElse` vs `orElseGet`의 평가 시점 차이.
- 직접 관찰: `orElse(callMethod())`와 `orElseGet(() -> callMethod())` 실행 시 부수 효과(Side effect) 발생 여부를 확인한다.
- 실습: null을 반환할 수 있는 메서드를 `Optional` 반환으로 리팩터링하고 안전하게 값을 추출한다.
- 실패 실험: `optional.get()`을 무조건 호출하여 발생하는 `NoSuchElementException` 안티패턴을 재현하고 `orElseThrow` 또는 `map`/`ifPresent`로 복구한다.
- 완료 기준: NullPointer 위험을 컴파일 타임 및 API 계약 차원에서 제거하는 코드를 작성한다.

### [JF6-5] Modern I/O & Path operations

- 이해할 것: `java.nio.file.Path`, `Files` 클래스, 스트림 기반 파일 읽기/쓰기(`Files.lines`), 안전한 디렉터리 탐색.
- 직접 관찰: 대용량 파일을 메모리에 한 번에 올리지 않고 라인 단위 스트림으로 지연 처리하는 메모리 점유율을 확인한다.
- 실습: 파일 경로 조작, 디렉터리 생성, 파일 읽기/쓰기 및 필터링 처리를 수행하는 유틸리티를 작성한다.
- 실패 실험: 파일 스트림 리소스를 닫지 않아 발생하는 파일 잠금(Lock) 또는 리소스 누수를 재현하고 try-with-resources로 복구한다.
- 완료 기준: Java의 최신 NIO API를 활용한 안전하고 효율적인 파일 처리 파이프라인을 구축한다.

### JF6 단계 결과물

- 람다, 스트림 지연 연산, Optional, 최신 NIO 파일 처리를 구현.
- 핵심 명령·출력·diagram·실패 복구 기록을 `PROGRESS.md`에 남긴다.
