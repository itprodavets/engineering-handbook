#!/usr/bin/env python3
"""Validate all local Markdown navigation links and question/lab consistency."""
from pathlib import Path
from urllib.parse import unquote
import re,sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]
files=list(ROOT.rglob('*.md'))
rx=re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)]+)\)')
for page in files:
    content=page.read_text(encoding='utf-8')
    for dest in rx.findall(content):
        dest=dest.strip().split('#',1)[0]
        if not dest or re.match(r'^[a-z][a-z0-9+.-]*:',dest,re.I):continue
        dest=unquote(dest)
        target=(page.parent/dest).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            errors.append(f'{page.relative_to(ROOT)} -> {dest}: missing local target')
for i in range(1,36):
    glob=list((ROOT/'questions'/'dotnet').glob(f'Q-{i:03d}-*.md'))
    if len(glob)!=1:errors.append(f'Q-{i:03d}: expected one question Markdown, got {len(glob)}')
for i in range(24,36):
    path=ROOT/'labs'/'dotnet'/f'Q-{i:03d}.cs'
    if not path.is_file():errors.append(f'{path}: missing code lab')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(files)} Markdown pages, 35 questions, 12 labs, and local links validated.')
