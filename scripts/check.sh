#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${project_root}/.venv/bin/python"
ruff_bin="${project_root}/.venv/bin/ruff"

cd "${project_root}"

"${ruff_bin}" format --check src tests
"${ruff_bin}" check src tests
"${python_bin}" -m mypy
"${python_bin}" -m pytest -q
