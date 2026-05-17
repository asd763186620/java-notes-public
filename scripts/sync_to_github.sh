#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git fetch origin main || true
python3 scripts/update_readme.py

git add -A

if git diff --cached --quiet; then
  echo "No local changes to commit."
else
  git commit -m "Update notes and README index"
fi

git push --force-with-lease -u origin main
