#!/usr/bin/env python3
"""Run registered .NET 10 snippets and check deterministic outputs where defined."""
from pathlib import Path
import json, subprocess, shutil, re, sys
ROOT=Path(__file__).resolve().parents[1]
if not shutil.which("dotnet"): sys.exit("dotnet not found: .NET 10 SDK is required")
questions=json.loads((ROOT/"content/questions.json").read_text(encoding="utf-8"))
fixed={"Q-024":"ABC","Q-025":"ACB","Q-026":"True","Q-027":"2","Q-030":"DONE","Q-031":"X","Q-032":"True","Q-033":"Outer awaited\nInner awaited","Q-034":"False","Q-035":"AXXX"}
labs=[q for q in questions if q.get("lab") and q["lab"].startswith("labs/dotnet/") and q["lab"].endswith(".cs")]
for q in labs:
    path=ROOT/q["lab"]
    if not path.is_file(): sys.exit(f"{q['id']}: missing {q['lab']}")
    p=subprocess.run(["dotnet","run","--file",q["lab"]],cwd=ROOT,capture_output=True,text=True,timeout=120)
    got=p.stdout.strip()
    if p.returncode: sys.exit(f"{q['id']}: compile/run failed ({p.returncode})\nstdout: {got}\nstderr: {p.stderr}")
    verify=q.get("verify")
    if verify:
        if verify.get("mode")=="exact":
            if got!=verify["output"]: sys.exit(f"{q['id']}: expected {verify['output']!r}, got {got!r}")
        elif verify.get("mode")=="integer-range":
            if not re.fullmatch(r"[-+]?[0-9]+",got) or not verify["min"]<=int(got)<=verify["max"]: sys.exit(f"{q['id']}: output outside expected range: {got!r}")
        elif verify.get("mode")!="run-only": sys.exit(f"{q['id']}: unrecognized verification mode")
    elif q["id"] in fixed and got!=fixed[q["id"]]: sys.exit(f"{q['id']}: expected {fixed[q['id']]!r}, got {got!r}")
    elif q["id"] in ("Q-028","Q-029") and (not got.isdigit() or not 1<=int(got)<=10000): sys.exit(f"{q['id']}: unexpected counter value {got!r}")
    print(f"PASS {q['id']}: "+got.replace("\n"," / "))
print(f"PASS: {len(labs)} registered .NET labs compiled and executed")
