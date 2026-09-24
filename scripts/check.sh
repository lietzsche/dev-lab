#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${project_root}"

echo "==> 1. 필수 문서 및 설정 파일 존재 여부 검사..."
required_files=(
    "README.md"
    "CURRICULUM.md"
    "PROGRESS.md"
    "AGENTS.md"
    "docker/Dockerfile"
    "docker/docker-compose.yml"
    "scripts/setup_sandbox.sh"
    "scripts/inspect_object.py"
)

for file in "${required_files[@]}"; do
    if [ ! -f "${file}" ]; then
        echo "오류: 필수 파일이 없습니다: ${file}" >&2
        exit 1
    fi
    echo "  [OK] ${file}"
done

echo ""
echo "==> 2. Bash 스크립트 문법 검사 (bash -n)..."
for script in scripts/*.sh; do
    bash -n "${script}"
    echo "  [OK] ${script}"
done

echo ""
echo "==> 3. Python 스크립트 컴파일 및 문법 검사..."
python_bin="python3"
if [ -f ".venv/bin/python" ]; then
    python_bin=".venv/bin/python"
fi
"${python_bin}" -m py_compile scripts/*.py
echo "  [OK] scripts/inspect_object.py 컴파일 성공"

echo ""
echo "==> 4. setup_sandbox.sh init / clean 동작 검증..."
test_sandbox_dir="/tmp/git-test-sandbox-$$"
GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh init > /dev/null
GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh clean > /dev/null
echo "  [OK] 샌드박스 생성 및 정리 검증 완료"

echo ""
echo "=========================================================="
echo " [성공] 모든 Git Lab 검사가 통과했습니다!"
echo "=========================================================="
