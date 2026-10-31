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
print("PASS: all five deep-dive .NET 10 labs verified")
