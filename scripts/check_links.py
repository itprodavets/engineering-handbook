#!/usr/bin/env python3
"""Validate local Markdown links and references to dynamically registered questions."""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
files=list(ROOT.rglob('*.md'))
rx=re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)]+)\)')
for page in files:
    content=page.read_text(encoding='utf-8')
    for dest in rx.findall(content):
        dest=dest.strip().split('#',1)[0]
        if not dest or re.match(r'^[a-z][a-z0-9+.-]*:',dest,re.I):
            continue
        dest=unquote(dest)
        target=(page.parent/dest).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            errors.append(f'{page.relative_to(ROOT)} -> {dest}: missing local target')
questions=json.loads((ROOT/'content/questions.json').read_text(encoding='utf-8'))
lessons=json.loads((ROOT/'content/lessons.json').read_text(encoding='utf-8'))
owner={f'Q-{int(n):03d}':l.get('track','dotnet') for l in lessons for n in l['questions']}
for q in questions:
    track=owner.get(q['id'])
    if not track:
        errors.append(f'{q["id"]}: missing canonical lesson')
        continue
    for locale in ('','en/'):
        path=ROOT/'questions'/track/locale/(q['slug']+'.md')
        if not path.is_file():
            errors.append(f'{q["id"]}: missing {path.relative_to(ROOT)}')
    if q.get('lab') and not (ROOT/q['lab']).is_file():
        errors.append(f'{q["id"]}: missing {q["lab"]}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(files)} Markdown pages; {len(questions)} questions, '
      f'{sum(bool(q.get("lab")) for q in questions)} lab references; local links valid.')
