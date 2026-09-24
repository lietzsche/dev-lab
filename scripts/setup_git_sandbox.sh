#!/usr/bin/env bash

set -euo pipefail

SANDBOX_DIR="${GIT_SANDBOX_DIR:-/tmp/git-lab-sandbox}"

init_sandbox() {
    echo "==> Git 학습용 샌드박스를 생성합니다: ${SANDBOX_DIR}"
    
    if [ -d "${SANDBOX_DIR}" ]; then
        echo "경고: 기존 샌드박스 디렉터리가 이미 존재합니다."
        echo "초기화하려면 먼저 reset 또는 clean 명령을 실행하세요."
        exit 1
    fi

    mkdir -p "${SANDBOX_DIR}"
    cd "${SANDBOX_DIR}"

    # 1. 중앙 원격 베어(Bare) 저장소 생성
    echo "1) 중앙 원격 베어 저장소 (remote.git) 생성 중..."
    git init --bare --initial-branch=main remote.git

    # 2. 초기 커밋을 위한 임시 작업 디렉터리
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

    # 3. 협업자 및 학습자 클론 생성
    echo "3) 협업자 Alice 저장소 생성 중..."
    git clone remote.git alice > /dev/null 2>&1
    (
        cd alice
        git config user.name "Alice"
        git config user.email "alice@devlab.local"
    )

    echo "4) 협업자 Bob 저장소 생성 중..."
    git clone remote.git bob > /dev/null 2>&1
    (
        cd bob
        git config user.name "Bob"
        git config user.email "bob@devlab.local"
    )

    echo "5) 학습자 작업 저장소 (learner) 생성 중..."
    git clone remote.git learner > /dev/null 2>&1
    (
        cd learner
        git config user.name "Learner"
        git config user.email "learner@devlab.local"
    )

    echo "==> 샌드박스 준비 완료!"
    echo "디렉터리 구조:"
    echo "  ${SANDBOX_DIR}/remote.git  (중앙 베어 저장소)"
    echo "  ${SANDBOX_DIR}/learner     (학습자 전용 작업 공간)"
    echo "  ${SANDBOX_DIR}/alice       (동료 Alice 작업 공간)"
    echo "  ${SANDBOX_DIR}/bob         (동료 Bob 작업 공간)"
    echo ""
    echo "학습 시작 명령:"
    echo "  cd ${SANDBOX_DIR}/learner"
}

clean_sandbox() {
    if [ -d "${SANDBOX_DIR}" ]; then
        echo "==> 샌드박스 디렉터리를 삭제합니다: ${SANDBOX_DIR}"
        rm -rf "${SANDBOX_DIR}"
        echo "삭제 완료."
    else
        echo "샌드박스 디렉터리가 존재하지 않습니다."
    fi
}

reset_sandbox() {
    clean_sandbox
    init_sandbox
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
    *)
        echo "사용법: $0 {init|clean|reset}"
        exit 1
        ;;
esac
