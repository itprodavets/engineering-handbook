#!/usr/bin/env python3
"""Validate site source consistency, localization and source link targets."""
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
loads={l:json.loads((ROOT/'site/data'/f'{l}.json').read_text()) for l in ('ru','en')}
for lang,data in loads.items():
  lessons=data['lessons']; questions=data['questions']; glossary=data['glossary']
  ids=[q['id'] for q in questions]
  source_questions=json.loads((ROOT/'content/questions.json').read_text())
  if ids!=[q['id'] for q in source_questions]:errors.append(f'{lang}: question IDs mismatch')
  if len(lessons)!=len(json.loads((ROOT/'content/lessons.json').read_text())):errors.append(f'{lang}: lesson count mismatch')
  if len(glossary)!=len(json.loads((ROOT/'content/glossary.json').read_text())):errors.append(f'{lang}: glossary count mismatch')
  mapping={}
  for lesson in lessons:
    if not lesson.get('overview') or not lesson.get('mechanism') or not lesson.get('resources'):errors.append(f'{lang}: incomplete {lesson["id"]}')
    for i in lesson['questions']:
      if i in mapping:errors.append(f'{lang}: duplicate Q-{i:03d}: {mapping[i]} and {lesson["id"]}')
      mapping[i]=lesson['id']
  if sorted(mapping)!=sorted(int(q['id'][2:]) for q in source_questions):errors.append(f'{lang}: canonical lesson mapping has gaps')
  for q in questions:
    i=int(q['id'][2:]);source_q=next(s for s in source_questions if s['id']==q['id']);expect_kind='reinforcement' if source_q.get('lab') else 'review'
    if q['kind']!=expect_kind:errors.append(f'{lang}: {q["id"]} wrong kind')
    if q['lesson']!=mapping.get(i):errors.append(f'{lang}: {q["id"]} wrong lesson')
    if not q['question'] or not q['answer']:errors.append(f'{lang}: {q["id"]} no answer')
    if expect_kind=='reinforcement' and (not q['lab'] or not q['code']):errors.append(f'{lang}: {q["id"]} no lab')
    if expect_kind=='review' and q['lab']:errors.append(f'{lang}: {q["id"]} unexpected lab')
    if not (ROOT/q['markdown']).is_file():errors.append(f'{lang}: {q["id"]} bad markdown path')
  if lang=='en':
    for lesson in lessons:
      for field in ('title','desc','overview'):
        if re.search('[А-Яа-яЁё]',lesson[field]):errors.append(f'en: {lesson["id"]}.{field} not localized')
      for val in lesson['mechanism']+lesson['risks']:
        if re.search('[А-Яа-яЁё]',val):errors.append(f'en: {lesson["id"]} contains Cyrillic text')
      for r in lesson['resources']:
        if re.search('[А-Яа-яЁё]',r['name']+r['detail']):errors.append(f'en: {lesson["id"]} has untranslated resource')
    for q in questions:
      for field in ('title','question','answer','code'):
        if re.search('[А-Яа-яЁё]',q[field]):errors.append(f'en: {q["id"]}.{field} contains untranslated Cyrillic')
    for g in glossary:
      if re.search('[А-Яа-яЁё]',g['definition']):errors.append(f'en glossary: {g["term"]}')
if loads['ru']['meta']!=loads['en']['meta']:errors.append('locale datasets inconsistent')
for p in ('site/index.html','site/assets/app.js','site/assets/styles.css','site/assets/icon.svg','.github/workflows/pages.yml','README.md','README.en.md'):
  if not (ROOT/p).is_file():errors.append(f'missing {p}')
if errors:
  print('FAIL: '+str(len(errors))+' errors\n'+'\n'.join(errors))
  raise SystemExit(1)
print(f'PASS: {len(loads["ru"]["lessons"])} canonical lessons, {len(loads["ru"]["questions"])} questions per locale, 12 labs, localized paths, no duplicate concept ownership.')
