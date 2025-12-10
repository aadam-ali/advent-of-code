#!/usr/bin/env bash

cd "$(dirname "$0")" || exit 1

VENV="$PWD/.venv"
if [[ ! -d "$VENV" ]]; then
  python -m venv .venv
  "$VENV"/bin/pip install -r requirements.txt
fi

"$VENV"/bin/ruff format .
rg -l --type python '' | xargs "$VENV"/bin/reorder-python-imports
