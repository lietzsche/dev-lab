#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${root}"
for f in README.md CURRICULUM.md PROGRESS.md AGENTS.md STUDY_ROADMAP.md scripts/check.sh; do test -s "${f}" || exit 1; done
c="$(sed -n 's/^### \[\(R[0-9]-[0-9]\)\].*/\1/p' CURRICULUM.md | sort -u)"
r="$(sed -n 's/^| \*\*\(R[0-9]-[0-9]\)\*\*.*/\1/p' PROGRESS.md | sort -u)"
test "$(printf '%s\n' "${c}" | sed '/^$/d' | wc -l)" -eq 30
test "${c}" = "${r}"
test "$(grep -c '| 대기 | - |$' PROGRESS.md)" -eq 30
if git grep -n -E '(/mnt/[a-z]/|/home/[^/]+/|[A-Za-z]:[/\\])' -- ':!scripts/check.sh'; then exit 1; fi
bash -n scripts/check.sh
git diff --check
echo "[성공] Rust Systems Programming 초기 설정 검증 완료"
