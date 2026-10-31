#!/usr/bin/env python3
"""Verify .NET 10 deep-dive labs without assuming nondeterministic metrics."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "labs" / "dotnet" / "async-internals"
EXPECT = {
    "01-await-control-flow.cs": lambda text: text == "ABC|DEF",
    "02-state-machine-reflection.cs": lambda text: text == "True\n42",
    "03-socket-simulation.cs": lambda text: text == "READY",
    "04-allocations.cs": lambda text: bool(re.fullmatch(
        r"Sum=70000\nCallerThreadAllocatedBytes=\d+", text)),
    "05-queue-diagnostics.cs": lambda text: bool(re.fullmatch(
        r"ThreadPoolThreadCount=\d+\nPendingWorkItemCount=\d+\nFinished=True", text)),
}
for name, valid in EXPECT.items():
    result = subprocess.run(
        ["dotnet", "run", "--file", str(DIR / name)],
        cwd=ROOT, capture_output=True, text=True, timeout=120)
    output = result.stdout.strip()
    if result.returncode or not valid(output):
        raise SystemExit(f"FAIL {name}: exit={result.returncode}\n"
                         f"stdout={output!r}\nstderr={result.stderr}")
    print(f"PASS {name}: {output.replace(chr(10),' | ')}")
EXTRA_EXPECT = {
    "Q-036.cs": "Read=1; Byte=42",
    "Q-038.cs": "CapturedIsNull=True; CallbackHasResult=True",
    "Q-040.cs": "Value=1",
    "Q-042.cs": "Counter=2",
    "Q-043.cs": "Purchased=2; Stock=-1",
    "Q-044.cs": "Previous=1; Stock=0\\nCurrent=10; Previous=10; Stock=7",
    "Q-045.cs": "Purchased=1; Stock=0",
    "Q-046.cs": "Previous=2,3; Stock=2",
    "Q-047.cs": "Stock3: Purchased=2; Stock=1\\nStock1: Purchased=1; Rejected=4; Stock=0",
}
for name, expected in EXTRA_EXPECT.items():
    result = subprocess.run(
        ["dotnet", "run", "--file", str(ROOT / "labs" / "dotnet" / name)],
        cwd=ROOT, capture_output=True, text=True, timeout=120)
    actual = result.stdout.strip()
    if result.returncode or actual != expected:
        raise SystemExit(f"FAIL {name}: exit={result.returncode}\\n"
                         f"stdout={actual!r}, expected={expected!r}\\nstderr={result.stderr}")
    print(f"PASS {name}: {actual.replace(chr(10), ' | ')}")
print(f"PASS: {len(EXPECT) + len(EXTRA_EXPECT)} deep-dive .NET 10 labs verified")
