# Level 4. 네트워크와 서버 작업

## 목표
- 서버의 IP 주소, 라우팅, 열린 포트와 그 포트를 점유하고 있는 프로세스를 즉시 확인한다.
- 터미널에서 `curl`로 REST API 요청(GET/POST, 헤더, JSON 바디)을 보내고 응답 상태 코드와 헤더를 검증한다.
- 배포 아카이브(`tar`) 압축/해제와 원격 서버 작업(`ssh`, `scp`)의 실전 패턴을 익힌다.

---

## 세션 구성 (각 15~20분)

### Session 4.1: 네트워크 인터페이스와 연결 확인 (`ip`, `ping`)
- **실습 목표**: 현재 머신의 네트워크 인터페이스 IP를 확인하고 네트워크 도달 가능성을 점검한다.
- **다루는 명령어**:
  - `ip a` (`ip addr`), `ip -br a`: 네트워크 인터페이스와 할당된 IP 주소 확인
  - `ip route`: 기본 게이트웨이(Default Gateway)와 라우팅 테이블 확인
  - `ping -c 3 <호스트>`: 패킷 손실 여부와 왕복 지연시간(RTT) 확인 (`-c`로 횟수 제한)
- **실습 과제**:
  1. `ip -br a`로 WSL2 가상 이더넷(`eth0`)과 루프백(`lo`) 주소 확인하기
  2. `ip route`로 기본 게이트웨이 확인하기
  3. `ping -c 3 127.0.0.1`로 로컬 루프백 응답 확인하기

### Session 4.2: 열린 포트와 프로세스 추적 (`ss`)
- **실습 목표**: `"Address already in use"` 포트 충돌이 발생했을 때 어느 프로세스가 해당 포트를 점유 중인지 찾아낸다.
- **다루는 명령어**:
  - `ss -tuln`: 현재 리스닝(`-l`) 중인 TCP(`-t`)/UDP(`-u`) 포트를 숫자(`-n`)로 표시
  - `ss -tulnp`: 해당 포트를 열고 있는 프로세스 이름과 PID(`-p`)까지 함께 확인
- **실습 과제**:
  1. `playground/scripts/mock-server.py`를 백그라운드로 실행해 로컬 테스트 서버(기본 포트 `18080`) 띄우기
  2. `ss -tulnp | grep 18080`으로 포트 리스닝 상태와 프로세스 PID 직접 확인하기

### Session 4.3: HTTP 요청과 API 응답 검증 (`curl`)
- **실습 목표**: 브라우저나 Postman 없이 터미널에서 REST API 엔드포인트를 호출하고 응답 헤더·상태 코드·바디를 검증한다.
- **다루는 명령어**:
  - `curl http://localhost:18080/health`: 기본 GET 요청
  - `curl -i`: HTTP 응답 상태 줄(`HTTP/1.1 200 OK`)과 응답 헤더까지 함께 출력
  - `curl -v`: 요청 헤더와 응답 헤더 전체 통신 과정 상세 확인
  - `curl -X POST -H "Content-Type: application/json" -d '{"item":"book"}' <URL>`: JSON POST 요청 전송
- **실습 과제**:
  1. 실행 중인 로컬 테스트 서버의 `/health`와 `/api/orders`를 `curl -i`로 호출해 상태 코드와 JSON 응답 확인하기
  2. 존재하지 않는 경로를 호출해 `404` 응답 확인하기
  3. `curl -X POST`로 주문 생성 요청을 보내고 응답 확인하기

### Session 4.4: DNS 조회와 경로 진단 (`dig`, `traceroute`)
- **실습 목표**: 도메인 이름이 어떤 IP로 해석되는지 확인하고 네트워크 경로 진단 도구의 사용법을 익힌다.
- **다루는 명령어**:
  - `dig <도메인>`, `dig +short <도메인>` (또는 `nslookup`, `getent hosts`): DNS 레코드 및 IP 조회
  - `traceroute` / `tracepath`: 목적지까지의 네트워크 홉(Hop) 경로 확인
- **실습 과제**:
  1. `/etc/resolv.conf`를 조회해 WSL이 참조하는 DNS 서버 확인하기
  2. `getent hosts localhost` 또는 `dig`로 호스트 이름 해석 결과 확인하기

### Session 4.5: 아카이브 압축과 해제 (`tar`)
- **실습 목표**: 로그 파일 묶음이나 배포 산출물을 `.tar.gz`로 압축하고, 풀기 전에 내부 목록을 먼저 확인한다.
- **다루는 명령어**:
  - `tar -czf <아카이브.tar.gz> <대상>`: gzip 압축 아카이브 생성 (`c` 생성, `z` gzip, `f` 파일명)
  - `tar -tf <아카이브.tar.gz>`: 압축을 풀지 않고 내부 파일 목록만 안전하게 확인 (`t` 목록)
  - `tar -xzf <아카이브.tar.gz> -C <대상폴더>`: 지정한 폴더에 압축 해제 (`x` 해제)
- **실습 과제**:
  1. `playground/logs/` 폴더를 `playground/files/backup/logs-archive.tar.gz`로 압축하기
  2. `tar -tf`로 압축 파일 안의 내용물 목록 확인하기
  3. `playground/files/temp/` 아래에 새 폴더를 만들고 `-C` 옵션으로 압축 해제하기

### Session 4.6: 원격 서버 접속과 파일 전송 (`ssh`, `scp`)
- **실습 목표**: 실무 Linux 서버 접속(`ssh`)과 서버 간 안전한 파일 복사(`scp`) 구문 및 `~/.ssh/config` 관리법을 익힌다.
- **다루는 명령어**:
  - `ssh -i <키파일> user@host -p <포트>`
  - `scp <로컬파일> user@host:<원격경로>` / `scp user@host:<원격파일> <로컬경로>`
  - SSH 설정 파일(`config`) 작성 형식 실습 (`playground/files/config/` 내에서 안전하게 연습)
