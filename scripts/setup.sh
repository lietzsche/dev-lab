#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
venv_dir="${project_root}/.venv"
python_bin="${PYTHON_BIN:-python3}"

"${python_bin}" -m venv "${venv_dir}"
"${venv_dir}/bin/python" -m pip install -e "${project_root}"

echo
echo "Development environment is ready."
echo "Activate it with: source .venv/bin/activate"
echo "For VS Code, select: ${venv_dir}/bin/python"
