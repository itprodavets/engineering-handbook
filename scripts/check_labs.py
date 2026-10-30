#!/usr/bin/env python3
"""Run all registered .NET 10 file-based C# labs; assert deterministic cases."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import re
ROOT=Path(__file__).resolve().parents[1]
if not shutil.which('dotnet'):
    sys.exit('dotnet not found: .NET 10 SDK is required to compile/run labs')
questions=json.loads((ROOT/'content/questions.json').read_text(encoding='utf-8'))
lessons=json.loads((ROOT/'content/lessons.json').read_text(encoding='utf-8'))
track_of={f'Q-{int(n):03d}':l.get('track','dotnet') for l in lessons for n in l['questions']}
# Legacy baseline assertions for the first 12 labs; new labs should specify verify.
fixed={
 'Q-024':'ABC','Q-025':'ACB','Q-026':'True','Q-027':'2',
 'Q-030':'DONE','Q-031':'X','Q-032':'True',
 'Q-033':'Outer awaited\nInner awaited','Q-034':'False','Q-035':'AXXX'
}
labs=[q for q in questions if q.get('lab') and q['lab'].endswith('.cs') and track_of.get(q['id'])=='dotnet']
for q in labs:
    qid=q['id']; lab=q['lab']
    if not (ROOT/lab).is_file():
        sys.exit(f'{qid}: lab file does not exist: {lab}')
    result=subprocess.run(['dotnet','run','--file',lab],cwd=ROOT,text=True,capture_output=True,timeout=120)
    actual=result.stdout.strip()
    if result.returncode:
        sys.exit(f'{qid}: dotnet failed ({result.returncode})\nstdout: {actual}\nstderr: {result.stderr}')
    verify=q.get('verify')
    if verify:
        if verify['mode']=='exact' and actual!=verify['output']:
            sys.exit(f'{qid}: expected {verify["output"]!r}, got {actual!r}')
        elif verify['mode']=='integer-range':
            if not re.fullmatch(r'[-+]?[0-9]+',actual) or not (verify['min']<=int(actual)<=verify['max']):
                sys.exit(f'{qid}: expected integer within {verify["min"]}..{verify["max"]}, got {actual!r}')
        elif verify['mode'] not in ('exact','integer-range','run-only'):
            sys.exit(f'{qid}: unknown verify mode {verify["mode"]}')
    elif qid in fixed and actual!=fixed[qid]:
        sys.exit(f'{qid}: expected {fixed[qid]!r}, got {actual!r}')
    elif qid in ('Q-028','Q-029') and (not re.fullmatch(r'[0-9]+',actual) or not (1<=int(actual)<=10000)):
        sys.exit(f'{qid}: expected integer in 1..10000, got {actual!r}')
    print(f'PASS {qid}: {actual.replace(chr(10)," / ")}')
print(f'PASS: {len(labs)} registered .NET 10 labs compiled and executed.')
