#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

if [[ "${1:-}" == "--docker" ]]; then
  exec docker compose run --rm build-jdk8
fi

java -version
mvn -version
exec mvn -B verify
