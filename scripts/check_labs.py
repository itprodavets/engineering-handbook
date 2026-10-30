#!/usr/bin/env python3
"""Run safe .NET 10 file-based snippets and verify deterministic properties."""
from pathlib import Path
import shutil,subprocess,sys,re
ROOT=Path(__file__).resolve().parents[1]
if not shutil.which('dotnet'):
    sys.exit('dotnet not found: .NET 10 SDK is required to compile/run labs')
fixed={
 'Q-024':'ABC','Q-025':'ACB','Q-026':'True','Q-027':'2',
 'Q-030':'DONE','Q-031':'X','Q-032':'True',
 'Q-033':'Outer awaited\nInner awaited','Q-034':'False','Q-035':'AXXX'
}
for i in range(24,36):
    id=f'Q-{i:03d}'
    result=subprocess.run(['dotnet','run','--file',f'labs/dotnet/{id}.cs'],cwd=ROOT,text=True,capture_output=True,timeout=120)
    actual=result.stdout.strip()
    if result.returncode:
        sys.exit(f'{id}: dotnet failed ({result.returncode})\nstdout: {actual}\nstderr: {result.stderr}')
    if id in fixed:
        if actual!=fixed[id]:sys.exit(f'{id}: expected {fixed[id]!r}, got {actual!r}')
    else:
        if not re.fullmatch(r'[0-9]+',actual) or not (1<=int(actual)<=10000):
            sys.exit(f'{id}: expected integer in 1..10000, got {actual!r}')
    print(f'PASS {id}: {actual.replace(chr(10)," / ")}')
print('PASS: all 12 labs compiled and their output conditions passed')
