#!/usr/bin/env bash
set -euo pipefail

root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${root}"

required_files=(
  "AGENTS.md"
  "README.md"
  "progress.md"
  "curriculum/level-01.md"
  "curriculum/level-02.md"
  "curriculum/level-03.md"
  "curriculum/level-04.md"
  "curriculum/level-05.md"
  "curriculum/level-06.md"
  "curriculum/level-07.md"
  "playground/files/notes.txt"
  "playground/files/server-inventory.csv"
  "playground/files/config/application.yml"
  "playground/java-project/pom.xml"
  "playground/java-project/src/main/java/com/example/order/service/OrderService.java"
  "playground/logs/app-2026-10-21.log"
  "playground/logs/access.log"
  "playground/scripts/healthcheck.sh"
  "playground/scripts/dummy-worker.sh"
  "playground/scripts/mock-server.py"
)

for f in "${required_files[@]}"; do
  if [[ ! -s "${f}" ]]; then
    echo "[오류] 필수 파일이 없거나 비어 있습니다: ${f}" >&2
    exit 1
  fi
done

for d in playground/files playground/java-project playground/logs playground/scripts; do
  if [[ ! -d "${d}" ]]; then
    echo "[오류] 필수 디렉터리가 없습니다: ${d}" >&2
    exit 1
  fi
done

bash -n scripts/check.sh
bash -n scripts/reset-playground.sh
bash -n playground/scripts/healthcheck.sh
bash -n playground/scripts/dummy-worker.sh

echo "[성공] WSL CLI Mastery 학습 환경 및 실습 데이터 검증 완료"
