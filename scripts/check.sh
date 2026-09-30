#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${project_root}"

required_files=(
    README.md CURRICULUM.md PROGRESS.md AGENTS.md
    scripts/setup_sandbox.sh scripts/inspect_context.sh scripts/check.sh
    docker/Dockerfile docker/docker-compose.yml docker/entrypoint.sh
)

printf '%s\n' '==> required files'
for file in "${required_files[@]}"; do
    test -f "${file}"
    printf '  [OK] %s\n' "${file}"
done

printf '%s\n' '==> bash syntax'
for script in scripts/*.sh docker/*.sh; do
    bash -n "${script}"
    printf '  [OK] %s\n' "${script}"
done

if command -v shellcheck >/dev/null 2>&1; then
    printf '%s\n' '==> ShellCheck'
    shellcheck scripts/*.sh docker/*.sh
else
    printf '%s\n' '==> ShellCheck skipped (not installed)'
fi

printf '%s\n' '==> curriculum/progress IDs'
curriculum_ids="$(sed -n 's/^| \(B[0-9]-[0-9]\) |.*/\1/p' CURRICULUM.md | sort -u)"
progress_ids="$(sed -n 's/^| \*\*\(B[0-9]-[0-9]\)\*\* |.*/\1/p' PROGRESS.md | sort -u)"
if [ "$(printf '%s\n' "${curriculum_ids}" | sed '/^$/d' | wc -l)" -ne 24 ]; then
    printf '%s\n' '오류: 커리큘럼은 24개 소단원이어야 합니다.' >&2
    exit 1
fi
if [ "${curriculum_ids}" != "${progress_ids}" ]; then
    printf '%s\n' '오류: CURRICULUM과 PROGRESS의 ID가 다릅니다.' >&2
    exit 1
fi
valid_state_count="$(grep -cE '^\| \*\*B[0-9]-[0-9]\*\* \|.*\| (대기|진행 중|완료) \|.*\|$' PROGRESS.md)"
in_progress_count="$(grep -c '| 진행 중 |' PROGRESS.md || true)"
if [ "${valid_state_count}" -ne 24 ] || [ "${in_progress_count}" -gt 1 ]; then
    printf '%s\n' '오류: 진도 상태가 유효하지 않거나 진행 중인 단원이 둘 이상입니다.' >&2
    exit 1
fi
printf '%s\n' '  [OK] 24 IDs and valid progress states'

printf '%s\n' '==> machine-specific path check'
forbidden_pattern='(/mnt/[a-z]/|/home/[^/]+/|(^|[[:space:]])[A-Za-z]:/)'
if git grep -n -E "${forbidden_pattern}" -- ':!scripts/check.sh'; then
    printf '%s\n' '오류: 특정 머신의 절대 경로가 포함돼 있습니다.' >&2
    exit 1
fi
printf '%s\n' '  [OK] no machine-specific paths'

printf '%s\n' '==> sandbox lifecycle'
test_root="$(mktemp -d)"
test_sandbox="${test_root}/lab"
unsafe_dir="${test_root}/unsafe"
cleanup() { rm -rf "${test_root}"; }
trap cleanup EXIT

BASH_SANDBOX_DIR="${test_sandbox}" ./scripts/setup_sandbox.sh init >/dev/null
BASH_SANDBOX_DIR="${test_sandbox}" ./scripts/setup_sandbox.sh status >/dev/null
"${test_sandbox}/inspect_context.sh" one 'two words' >/dev/null
"${test_sandbox}/sandbox.sh" reset >/dev/null

mkdir -p "${unsafe_dir}"
printf '%s\n' keep > "${unsafe_dir}/keep-me"
if BASH_SANDBOX_DIR="${unsafe_dir}" ./scripts/setup_sandbox.sh clean >/dev/null 2>&1; then
    printf '%s\n' '오류: marker 없는 디렉터리 clean이 허용됐습니다.' >&2
    exit 1
fi
test -f "${unsafe_dir}/keep-me"
BASH_SANDBOX_DIR="${test_sandbox}" ./scripts/setup_sandbox.sh clean >/dev/null
printf '%s\n' '  [OK] init/status/reset/clean and marker guard'

printf '%s\n' '[SUCCESS] all Bash lab checks passed'
