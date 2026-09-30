#!/usr/bin/env bash

set -euo pipefail

mkdir -p /lab/workspace /lab/fixtures /lab/logs
if [ ! -f /lab/fixtures/records.txt ]; then
    printf '%s\n' alpha 'two words' '*.txt' '' omega > /lab/fixtures/records.txt
fi
cd /lab/workspace
exec "$@"
