#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${root}"
for f in README.md CURRICULUM.md PROGRESS.md AGENTS.md STUDY_ROADMAP.md scripts/check.sh; do test -s "${f}" || exit 1; done
c="$(sed -n 's/^### \[\(JF[0-9]-[0-9]\)\].*/\1/p' CURRICULUM.md | sort -u)"
r="$(sed -n 's/^| \*\*\(JF[0-9]-[0-9]\)\*\*.*/\1/p' PROGRESS.md | sort -u)"
test "$(printf '%s\n' "${c}" | sed '/^$/d' | wc -l)" -eq 30
test "${c}" = "${r}"
awk -F '|' '
/^\| \*\*JF[0-9]-[0-9]\*\*/ {
  state = $6; date = $7
  gsub(/^[[:space:]]+|[[:space:]]+$/, "", state)
  gsub(/^[[:space:]]+|[[:space:]]+$/, "", date)
  if (state == "진행 중") active++
  if (state == "대기" || state == "진행 중") {
    if (date != "-") invalid = 1
  } else if (state == "완료") {
    if (date !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/) invalid = 1
  } else invalid = 1
}
END { exit (invalid || active > 1) }
' PROGRESS.md
if git grep -n -E '(/mnt/[a-z]/|/home/[^/]+/|[A-Za-z]:[/\\])' -- ':!scripts/check.sh'; then exit 1; fi
bash -n scripts/check.sh
git diff --check
echo "[성공] Java Fundamentals 문서·진도 검증 완료"
