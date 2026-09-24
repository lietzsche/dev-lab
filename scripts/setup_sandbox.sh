#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
MARKER_NAME=".git-lab-sandbox"

# 샌드박스에 복사된 sandbox.sh는 자신의 위치를 대상으로 삼습니다.
if [ -f "${SCRIPT_DIR}/${MARKER_NAME}" ]; then
    RAW_SANDBOX_DIR="${SCRIPT_DIR}"
else
    RAW_SANDBOX_DIR="${GIT_SANDBOX_DIR:-/tmp/git-lab-sandbox}"
fi
# 상대 경로 또는 환경별 경로를 표준 절대 경로로 정규화
SANDBOX_DIR="$(python3 -c "import os, sys; print(os.path.abspath(sys.argv[1]))" "${RAW_SANDBOX_DIR}")"

assert_safe_target() {
    if [ "${SANDBOX_DIR}" = "/" ] || [ "${SANDBOX_DIR}" = "${PROJECT_ROOT}" ]; then
        echo "오류: 안전하지 않은 샌드박스 경로입니다: ${SANDBOX_DIR}" >&2
        exit 1
    fi
}

assert_owned_sandbox() {
    assert_safe_target
    if [ ! -f "${SANDBOX_DIR}/${MARKER_NAME}" ]; then
        echo "오류: 이 도구가 만든 샌드박스가 아니므로 삭제하지 않습니다: ${SANDBOX_DIR}" >&2
        exit 1
    fi
}

install_helpers() {
    local inspect_source setup_source
    if [ -f "${SCRIPT_DIR}/inspect_object.py" ]; then
        inspect_source="${SCRIPT_DIR}/inspect_object.py"
    else
        inspect_source="${PROJECT_ROOT}/scripts/inspect_object.py"
    fi
    setup_source="${SCRIPT_DIR}/$(basename -- "${BASH_SOURCE[0]}")"

    if [ "${inspect_source}" != "${SANDBOX_DIR}/inspect_object.py" ]; then
        cp "${inspect_source}" "${SANDBOX_DIR}/inspect_object.py"
    fi
    if [ "${setup_source}" != "${SANDBOX_DIR}/sandbox.sh" ]; then
        cp "${setup_source}" "${SANDBOX_DIR}/sandbox.sh"
    fi
    chmod +x "${SANDBOX_DIR}/inspect_object.py" "${SANDBOX_DIR}/sandbox.sh"
}

init_sandbox() {
    echo "==> Git 학습용 격리 샌드박스를 생성합니다: ${SANDBOX_DIR}"

    assert_safe_target
    if [ -d "${SANDBOX_DIR}" ]; then
        if [ "${ALLOW_EXISTING_SANDBOX:-0}" != "1" ]; then
            echo "경고: 기존 샌드박스 디렉터리가 이미 존재합니다: ${SANDBOX_DIR}"
            echo "완전히 초기화하려면 '$0 reset'을 실행하세요."
            exit 1
        fi
        assert_owned_sandbox
    else
        mkdir -p "${SANDBOX_DIR}"
        : > "${SANDBOX_DIR}/${MARKER_NAME}"
    fi

    cd "${SANDBOX_DIR}"

    # 1. 중앙 원격 베어(Bare) 저장소 생성
    echo "1) 중앙 원격 베어 저장소 (remote.git) 생성 중..."
    git init --bare --initial-branch=main remote.git > /dev/null 2>&1

    # 2. 초기 커밋 생성을 위한 임시 작업 디렉터리
    echo "2) 기본 초기 커밋 생성 및 푸시 중..."
    git clone remote.git temp-init > /dev/null 2>&1
    (
        cd temp-init
        git config user.name "System"
        git config user.email "system@devlab.local"
        echo "# Git Learning Lab" > README.md
        echo "Git 내부 동작과 협업 실습을 위한 샌드박스입니다." >> README.md
        git add README.md
        git commit -m "docs: 초기 README 추가" > /dev/null 2>&1
        git push origin main > /dev/null 2>&1
    )
    rm -rf temp-init

    # 3. 협업자 Alice 저장소 생성
    echo "3) 협업자 Alice 저장소 생성 중..."
    git clone remote.git alice > /dev/null 2>&1
    (
        cd alice
        git config user.name "Alice"
        git config user.email "alice@devlab.local"
    )

    # 4. 협업자 Bob 저장소 생성
    echo "4) 협업자 Bob 저장소 생성 중..."
    git clone remote.git bob > /dev/null 2>&1
    (
        cd bob
        git config user.name "Bob"
        git config user.email "bob@devlab.local"
    )

    # 5. 학습자 전용 저장소 (learner) 생성
    echo "5) 학습자 작업 저장소 (learner) 생성 중..."
    git clone remote.git learner > /dev/null 2>&1
    (
        cd learner
        git config user.name "Learner"
        git config user.email "learner@devlab.local"
    )

    # 6. 샌드박스 내부용 헬퍼 유틸리티 복사 (샌드박스 내부에서 상대 경로로 바로 실행 가능)
    install_helpers

    echo ""
    echo "=========================================================="
    echo " [성공] Git 샌드박스 초기화가 완료되었습니다!"
    echo "=========================================================="
    echo "저장소 목록:"
    echo "  - 중앙 원격 저장소: ${SANDBOX_DIR}/remote.git"
    echo "  - 학습자 작업 공간: ${SANDBOX_DIR}/learner (메인 실습 공간)"
    echo "  - 동료 Alice 공간: ${SANDBOX_DIR}/alice   (동시성/충돌 시뮬레이션용)"
    echo "  - 동료 Bob 공간:   ${SANDBOX_DIR}/bob     (동시성/충돌 시뮬레이션용)"
    echo ""
    echo "학습자 작업 공간 내부 편의 도구:"
    echo "  - 객체 분석: python3 ../inspect_object.py <hash>"
    echo "  - 샌드박스 리셋: ../sandbox.sh reset"
    echo "  - 샌드박스 상태: ../sandbox.sh status"
    echo ""
    echo "실습 시작 명령:"
    echo "  cd ${SANDBOX_DIR}/learner"
    echo "=========================================================="
}

clean_sandbox() {
    if [ -d "${SANDBOX_DIR}" ]; then
        assert_owned_sandbox
        echo "==> 샌드박스 디렉터리를 삭제합니다: ${SANDBOX_DIR}"
        rm -rf "${SANDBOX_DIR}"
        echo "삭제 완료."
    else
        echo "알림: 삭제할 샌드박스 디렉터리가 존재하지 않습니다: ${SANDBOX_DIR}"
    fi
}

reset_sandbox() {
    assert_owned_sandbox
    echo "==> 샌드박스를 초기 상태로 되돌립니다: ${SANDBOX_DIR}"
    rm -rf \
        "${SANDBOX_DIR}/remote.git" \
        "${SANDBOX_DIR}/temp-init" \
        "${SANDBOX_DIR}/alice" \
        "${SANDBOX_DIR}/bob" \
        "${SANDBOX_DIR}/learner"
    ALLOW_EXISTING_SANDBOX=1 init_sandbox
}

status_sandbox() {
    if [ ! -d "${SANDBOX_DIR}" ]; then
        echo "오류: 샌드박스가 존재하지 않습니다. 먼저 '$0 init'을 실행하세요."
        exit 1
    fi

    echo "==> 샌드박스 상태 점검: ${SANDBOX_DIR}"
    for dir in learner alice bob; do
        if [ -d "${SANDBOX_DIR}/${dir}" ]; then
            echo "--- [${dir}] ---"
            (
                cd "${SANDBOX_DIR}/${dir}"
                git status -s -b
                git log --oneline -n 1 || true
            )
        fi
    done
}

case "${1:-init}" in
    init)
        init_sandbox
        ;;
    clean)
        clean_sandbox
        ;;
    reset)
        reset_sandbox
        ;;
    status)
        status_sandbox
        ;;
    *)
        echo "사용법: $0 {init|clean|reset|status}"
        exit 1
        ;;
esac
