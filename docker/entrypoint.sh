#!/usr/bin/env bash

set -euo pipefail

WORKSPACE="/workspace"

if [ ! -d "${WORKSPACE}/remote.git" ]; then
    echo "==> Docker 컨테이너 내 Git 샌드박스를 초기화합니다..."
    cd "${WORKSPACE}"

    # 1. 중앙 원격 베어 저장소
    git init --bare --initial-branch=main remote.git > /dev/null 2>&1

    # 2. 초기 커밋
    git clone remote.git temp-init > /dev/null 2>&1
    (
        cd temp-init
        git config user.name "System"
        git config user.email "system@devlab.local"
        echo "# Git Learning Lab (Docker Sandbox)" > README.md
        echo "Git 내부 동작과 협업 실습을 위한 격리 샌드박스입니다." >> README.md
        git add README.md
        git commit -m "docs: 초기 README 추가" > /dev/null 2>&1
        git push origin main > /dev/null 2>&1
    )
    rm -rf temp-init

    # 3. 협업자 Alice
    git clone remote.git alice > /dev/null 2>&1
    (
        cd alice
        git config user.name "Alice"
        git config user.email "alice@devlab.local"
    )

    # 4. 협업자 Bob
    git clone remote.git bob > /dev/null 2>&1
    (
        cd bob
        git config user.name "Bob"
        git config user.email "bob@devlab.local"
    )

    # 5. 학습자 전용 저장소
    git clone remote.git learner > /dev/null 2>&1
    (
        cd learner
        git config user.name "Learner"
        git config user.email "learner@devlab.local"
    )

    echo "==> 초기화 완료!"
    echo "  - 메인 실습 저장소: ${WORKSPACE}/learner"
    echo "  - 객체 분석 유틸리티: inspect_object <hash>"
fi

exec "$@"
