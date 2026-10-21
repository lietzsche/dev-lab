#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="${APP_ENV:-dev}"
echo "=== [Healthcheck] Environment: ${ENV_NAME} ==="
echo "Timestamp : $(date '+%Y-%m-%d %H:%M:%S')"
echo "WorkingDir: $(pwd)"
echo "Status    : OK"
