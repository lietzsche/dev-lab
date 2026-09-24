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
    "docker/entrypoint.sh"
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
for script in scripts/*.sh docker/*.sh; do
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
echo "==> 4. 특정 머신 절대 경로 하드코딩 여부 검사..."
forbidden_pattern="(/mnt/[a-z]/|/home/[^/]+/|(^|[[:blank:]\"'\`])[A-Za-z]:[/\\\\])"
set +e
grep_matches=$(git grep -n -E "${forbidden_pattern}" -- ':!scripts/check.sh' 2>&1)
grep_exit=$?
set -e

if [ ${grep_exit} -eq 0 ]; then
    echo "오류: 파일에 특정 머신 종속 절대 경로가 포함되어 있습니다:" >&2
    echo "${grep_matches}" >&2
    exit 1
fi
echo "  [OK] 특정 머신 종속 절대 경로 없음 (완전한 이식성 유지)"

echo ""
echo "==> 5. setup_sandbox.sh init / status / reset / clean 전체 동작 검증..."
test_sandbox_dir="/tmp/git-test-sandbox-$$"
GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh init > /dev/null
GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh status > /dev/null

# README가 안내하는 것처럼 샌드박스에 복사된 관리 스크립트를 직접 실행합니다.
"${test_sandbox_dir}/sandbox.sh" reset > /dev/null
"${test_sandbox_dir}/sandbox.sh" status > /dev/null

# 샌드박스 내부 헬퍼 도구 동작 확인
if [ ! -f "${test_sandbox_dir}/inspect_object.py" ] || [ ! -f "${test_sandbox_dir}/sandbox.sh" ]; then
    echo "오류: 샌드박스 내부에 헬퍼 도구가 올바르게 복사되지 않았습니다." >&2
    GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh clean > /dev/null
    exit 1
fi

# marker가 없는 임의 디렉터리는 clean/reset 대상이 되어서는 안 됩니다.
unsafe_dir="/tmp/git-test-unsafe-$$"
mkdir -p "${unsafe_dir}"
touch "${unsafe_dir}/keep-me"
if GIT_SANDBOX_DIR="${unsafe_dir}" ./scripts/setup_sandbox.sh clean > /dev/null 2>&1; then
    echo "오류: marker가 없는 디렉터리의 clean이 허용되었습니다." >&2
    exit 1
fi
if [ ! -f "${unsafe_dir}/keep-me" ]; then
    echo "오류: marker가 없는 디렉터리의 파일이 삭제되었습니다." >&2
    exit 1
fi
rm -rf "${unsafe_dir}"

GIT_SANDBOX_DIR="${test_sandbox_dir}" ./scripts/setup_sandbox.sh clean > /dev/null
echo "  [OK] 샌드박스 라이프사이클 및 헬퍼 배포 검증 완료"

echo ""
echo "=========================================================="
echo " [성공] 모든 Git Lab 검사가 통과했습니다!"
echo "=========================================================="
