#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER="itprodavets"
REPO="engineering-handbook"
if ! command -v gh >/dev/null; then
  echo "Install GitHub CLI first (macOS: brew install gh), then run: gh auth login" >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "Authenticate with GitHub: gh auth login" >&2
  exit 1
fi
if gh repo view "${OWNER}/${REPO}" >/dev/null 2>&1; then
  echo "Repository ${OWNER}/${REPO} already exists; refusing to overwrite anything." >&2
  exit 1
fi
if [ ! -d .git ]; then git init -b main; fi
git add .
if ! git diff --cached --quiet; then git commit -m "docs: bootstrap multilingual engineering handbook and runnable .NET 10 labs"; fi
gh repo create "${OWNER}/${REPO}" --private --source=. --remote=origin --push
echo "Published privately: https://github.com/${OWNER}/${REPO}"
