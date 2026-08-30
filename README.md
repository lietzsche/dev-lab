# PortKeeper (Python)

PortKeeper (Rust/egui로 만든 SSH 로컬 포트 포워딩 GUI)를 Python으로 다시 구현한
버전입니다. 목적과 동작은 원본과 동일합니다: SSH 서버를 경유해 로컬 포트를 원격
목적지로 포워딩하고, 연결이 끊기면 자동으로 재연결합니다.

> 이 브랜치(`portkeeper-python`)는 `python_s` 커리큘럼과는 별개로, "이 프로젝트를
> 파이썬으로 다시 짤 수 있는가"라는 질문에 대한 실제 참고 구현으로 만들어졌습니다.
> `main` 브랜치의 학습 커리큘럼 내용과는 무관합니다.

## 스택

- **SSH + 포트 포워딩**: [`paramiko`](https://www.paramiko.org/) — `direct-tcpip`
  채널을 열어 로컬 소켓과 양방향으로 데이터를 중계합니다.
- **GUI**: [`dearpygui`](https://github.com/hoffstadt/DearPyGui) — 즉시 모드(immediate
  mode) GUI로, 원본 Rust판이 쓰는 `egui`와 개념이 비슷합니다.
- **설정 저장**: 표준 라이브러리 `json` (평문 텍스트, 비밀번호/암호문 없음).
- **동시성**: `threading` — 터널마다 감독 스레드 하나, 포워딩된 연결마다 중계
  스레드 두 개(양방향 각각). asyncio 대신 스레드를 쓴 이유는 Rust판의 "터널당
  태스크 하나" 구조와 가장 직접적으로 대응되기 때문입니다.

## 실행하기

```bash
python -m venv .venv
source .venv/bin/activate        # Windows는 .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 사용법

Rust판과 동일합니다.

1. **"+ 새 터널 추가"** 로 프로필 생성 (이름/SSH 호스트·포트/사용자 이름/인증 방식/
   로컬·원격 주소).
2. 목록에서 **시작** 클릭 → 비밀번호(또는 키 암호문) 입력 팝업 → **연결**.
   "이번 세션 동안 기억하기"를 켜두면 재연결 시 다시 묻지 않습니다.
3. 비밀번호/암호문은 메모리에만 있고 설정 파일에는 절대 저장되지 않습니다.
4. 호스트 키는 TOFU 방식으로 검증됩니다 — 처음 보는 호스트는 자동 등록, 이미
   등록된 호스트의 키가 바뀌면 (중간자 공격 가능성) paramiko가 자동으로
   `BadHostKeyException`을 발생시켜 연결을 차단합니다.

## 설정 파일 위치

Rust판과 충돌하지 않도록 별도 디렉터리를 씁니다.

| OS | 경로 |
|---|---|
| Linux | `~/.config/portkeeper-py/config.json` |
| macOS | `~/Library/Application Support/PortKeeperPy/config.json` |
| Windows | `%APPDATA%\PortKeeperPy\config.json` |

## 단일 실행 파일로 묶기 (PyInstaller)

```bash
pip install pyinstaller
# Linux/macOS (경로 구분자 ':')
pyinstaller --noconfirm --onefile --windowed --name portkeeper \
    --add-data "assets:assets" main.py
# Windows (경로 구분자 ';')
pyinstaller --noconfirm --onefile --windowed --name portkeeper ^
    --add-data "assets;assets" main.py
```

`--windowed`는 Rust판의 `windows_subsystem = "windows"`와 같은 역할로, Windows에서
콘솔 창 없이 GUI만 뜨게 합니다. 결과물은 `dist/portkeeper`(Windows는
`dist/portkeeper.exe`)에 생성됩니다.

주의: `--onefile`로 묶은 exe는 실행할 때마다 임시 폴더에 파일을 풀기 때문에
Rust판보다 시작이 느리고, Windows Defender/백신이 오탐하는 경우가 종종 있습니다
(파이썬을 실행 파일로 묶는 도구들의 공통적인 특성입니다). 배포 전에 실제 사용할
백신으로 한 번 검사해 보는 것을 권장합니다.

## Rust판과의 차이

| | Rust (`egui`) | Python (이 버전) |
|---|---|---|
| 실행 파일 크기 | ~30MB | 인터프리터를 통째로 묶어서 보통 더 큼 |
| 시작 속도 | 빠름 | 상대적으로 느림 (특히 `--onefile`) |
| 재연결/전달 로직 | `tokio` 태스크 | OS 스레드 |
| 라이트/다크 테마 전환 | 있음 (상단 툴바) | 없음 (DearPyGui 기본 테마만) |
| 코드 수정 난이도 | 컴파일 필요, 타입 체크가 오류를 미리 잡아줌 | 바로 실행하며 수정 가능, 대신 런타임에야 오류 발견 |

기능적으로는 동일합니다: 여러 프로필 관리, 자동 재연결(지수 백오프), SSH
keepalive, 비밀번호/키 인증, TOFU 호스트 키 검증, 로그 패널, 한글 폰트 내장.

## 테스트

```bash
pip install -r requirements-dev.txt
pytest
```

`tests/test_config.py`는 프로필 직렬화가 원본 그대로 왕복되는지, 그리고
비밀번호가 저장되는 JSON 구조 어디에도 절대 나타나지 않는지를 검증합니다.

## 라이선스

앱에는 한글이 깨지지 않도록 [나눔고딕](https://github.com/google/fonts/tree/main/ofl/nanumgothic)
폰트(`assets/fonts/NanumGothic-Regular.ttf`, SIL Open Font License 1.1,
전문은 `assets/fonts/OFL.txt`)가 포함되어 있습니다.
