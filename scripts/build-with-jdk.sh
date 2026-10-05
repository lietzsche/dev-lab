#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

case "${1:-}" in
  8)
    service="build-jdk8"
    ;;
  17)
    service="build-jdk17"
    ;;
  *)
    echo "usage: $0 <8|17>" >&2
    exit 2
    ;;
esac

exec docker compose run --rm "$service"
