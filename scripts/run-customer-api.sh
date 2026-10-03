#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

if [[ "${1:-}" == "--docker" ]]; then
  exec docker compose run --rm --service-ports customer-api-jdk8
fi

exec mvn -pl customer-api -am spring-boot:run
