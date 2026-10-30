#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
question="${1:-}"
# Only validated IDs are allowed. Never interpolate arbitrary paths into commands.
if [[ ! "$question" =~ ^Q-[0-9]{3,}$ ]]; then
    echo "Usage: ./scripts/run-lab.sh Q-024 (or another registered .NET lab ID)" >&2
    exit 2
fi
lab="labs/dotnet/${question}.cs"
if [[ ! -f "$lab" ]]; then
    echo "No runnable .NET lab exists for ${question}." >&2
    exit 2
fi
dotnet run --file "$lab"
