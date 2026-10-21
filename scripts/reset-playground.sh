#!/usr/bin/env bash
set -euo pipefail

root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${root}"

git checkout HEAD -- playground
git clean -fd playground

chmod +x playground/scripts/dummy-worker.sh playground/scripts/mock-server.py
chmod -x playground/scripts/healthcheck.sh

echo "[복구 완료] playground/ 디렉터리가 초기 실습 상태로 복원되었습니다."
