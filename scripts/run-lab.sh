#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
question="${1:-}"
case "$question" in
  Q-024|Q-025|Q-026|Q-027|Q-028|Q-029|Q-030|Q-031|Q-032|Q-033|Q-034|Q-035)
    dotnet run --file "labs/dotnet/${question}.cs"
    ;;
  *)
    echo "Usage: ./scripts/run-lab.sh Q-024..Q-035" >&2
    exit 2
    ;;
esac
