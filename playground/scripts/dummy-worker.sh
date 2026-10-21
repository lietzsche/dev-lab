#!/usr/bin/env bash
set -euo pipefail

trap 'echo "[dummy-worker] SIGTERM 수신: 안전하게 종료합니다 (PID=$$)"; exit 0' TERM INT

echo "[dummy-worker] 워커 시작됨 (PID=$$)"
while true; do
    sleep 2
done
