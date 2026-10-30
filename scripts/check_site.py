#!/usr/bin/env python3
"""Validate localized site data, unique ownership, paths, and future extensions."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_LESSONS = json.loads((ROOT/'content/lessons.json').read_text(encoding='utf-8'))
SOURCE_QUESTIONS = json.loads((ROOT/'content/questions.json').read_text(encoding='utf-8'))
SOURCE_GLOSSARY = json.loads((ROOT/'content/glossary.json').read_text(encoding='utf-8'))
LOCALES = {lang: json.loads((ROOT/'site/data'/f'{lang}.json').read_text(encoding='utf-8')) for lang in ('ru','en')}
errors = []
source_ids = [q['id'] for q in SOURCE_QUESTIONS]
lesson_ids = [l['id'] for l in SOURCE_LESSONS]
if len(source_ids) != len(set(source_ids)):
    errors.append('Duplicate question IDs')
if len(lesson_ids) != len(set(lesson_ids)):
    errors.append('Duplicate lesson IDs')

owner = {}
for lesson in SOURCE_LESSONS:
    track = lesson.get('track','dotnet')
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*',track):
        errors.append(f'Unsafe track: {track}')
    if not lesson.get('overview') or not lesson.get('mechanism') or not lesson.get('resources'):
        errors.append(f'Incomplete lesson: {lesson["id"]}')
    for number in lesson['questions']:
        qid = f'Q-{int(number):03d}'
        if qid in owner:
            errors.append(f'Duplicate question ownership: {qid} in {owner[qid]["id"]} and {lesson["id"]}')
        owner[qid] = lesson
if set(owner) != set(source_ids):
    errors.append(f'Lesson coverage mismatch: no owner={sorted(set(source_ids)-set(owner))}, no question={sorted(set(owner)-set(source_ids))}')

for lang, data in LOCALES.items():
    questions = data['questions']; lessons = data['lessons']; glossary = data['glossary']
    if [q['id'] for q in questions] != source_ids:
        errors.append(f'{lang}: source question ID/order mismatch')
    if [l['id'] for l in lessons] != lesson_ids:
        errors.append(f'{lang}: source lesson ID/order mismatch')
    if len(glossary) != len(SOURCE_GLOSSARY):
        errors.append(f'{lang}: glossary count mismatch')
    if data['meta'].get('questionCount') != len(SOURCE_QUESTIONS):
        errors.append(f'{lang}: stale question count')
    if data['meta'].get('lessonCount') != len(SOURCE_LESSONS):
        errors.append(f'{lang}: stale lesson count')
    for lesson in lessons:
        original = next((x for x in SOURCE_LESSONS if x['id'] == lesson['id']),None)
        if original is None or lesson['track'] != original.get('track','dotnet'):
            errors.append(f'{lang}: inconsistent track on {lesson["id"]}')
        if lang == 'en':
            for field in ('title','desc','overview'):
                if re.search('[А-Яа-яЁё]', lesson[field]):
                    errors.append(f'en: {lesson["id"]}.{field} is not translated')
            if any(re.search('[А-Яа-яЁё]', val) for val in lesson['mechanism']+lesson['risks']):
                errors.append(f'en: {lesson["id"]} contains Cyrillic')
            if any(re.search('[А-Яа-яЁё]', x['name']+x['detail']) for x in lesson['resources']):
                errors.append(f'en: {lesson["id"]} has untranslated resources')
        mdpath = ROOT/'topics'/lesson['track']/('en' if lang=='en' else '')/(lesson['id']+'.md')
        if not mdpath.is_file():
            errors.append(f'{lang}: missing {mdpath.relative_to(ROOT)}')
    for q in questions:
        source = next(x for x in SOURCE_QUESTIONS if x['id']==q['id'])
        track = owner[q['id']].get('track','dotnet')
        kind = source.get('kind') or ('reinforcement' if source.get('lab') else 'review')
        if q['kind'] != kind or q['track'] != track or q['lesson'] != owner[q['id']]['id']:
            errors.append(f'{lang}: incorrect kind/track/lesson for {q["id"]}')
        if not q.get('question') or not q.get('answer'):
            errors.append(f'{lang}: missing question or answer for {q["id"]}')
        if q.get('code') and not q.get('codeLanguage'):
            errors.append(f'{lang}: missing codeLanguage for {q["id"]}')
        if q.get('lab') and not (ROOT/q['lab']).is_file():
            errors.append(f'{lang}: missing lab for {q["id"]}: {q["lab"]}')
        if not (ROOT/q['markdown']).is_file():
            errors.append(f'{lang}: missing {q["markdown"]}')
        if lang == 'en' and any(re.search('[А-Яа-яЁё]',q[field]) for field in ('question','answer','code')):
            errors.append(f'en: {q["id"]} has untranslated text')
    if lang == 'en' and any(re.search('[А-Яа-яЁё]',g['definition']) for g in glossary):
        errors.append('en glossary contains Cyrillic definitions')

if LOCALES['ru']['meta'] != LOCALES['en']['meta']:
    errors.append('Localized datasets have inconsistent metadata')
for name in ('site/index.html','site/assets/app.js','site/assets/styles.css','site/assets/icon.svg',
             '.github/workflows/pages.yml','README.md','README.en.md','AGENTS.md'):
    if not (ROOT/name).is_file():
        errors.append(f'Missing {name}')
if errors:
    print('FAIL: '+str(len(errors))+' errors\n'+'\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(SOURCE_LESSONS)} lessons, {len(SOURCE_QUESTIONS)} questions, '
      f'{len(SOURCE_GLOSSARY)} glossary entries, localized paths and unique ownership.')
