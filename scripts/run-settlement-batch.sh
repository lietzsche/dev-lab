#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

if [[ "${1:-}" != "--docker" ]]; then
  echo "usage: $0 --docker <8|17>" >&2
  exit 2
fi

case "${2:-}" in
  8|17)
    exec docker compose run --rm "settlement-batch-jdk${2}"
    ;;
  *)
    echo "usage: $0 --docker <8|17>" >&2
    exit 2
    ;;
esac
