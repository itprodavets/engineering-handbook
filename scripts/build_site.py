#!/usr/bin/env python3
"""Build localized Markdown plus static Pages data from canonical bilingual JSON.

One question ID belongs to exactly one conceptual lesson. Repeated questions are
classified as reinforcement, not copied lessons. Use --check in CI.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "content" / "questions.json"
LESSONS = ROOT / "content" / "lessons.json"
QDIR = ROOT / "questions" / "dotnet"
TDIR = ROOT / "topics" / "dotnet"
SITE = ROOT / "site"
BASE = "https://itprodavets.github.io/engineering-handbook"
REPO = "https://github.com/itprodavets/engineering-handbook"

TRACK_NAMES = {"dotnet": ".NET / C#", "go": "Go", "kafka": "Kafka", "postgresql": "PostgreSQL", "kubernetes": "Kubernetes", "linux": "Linux", "system-design": "System Design"}


def track_of(lesson):
    return lesson.get("track", "dotnet")


def title_of_track(track):
    return TRACK_NAMES.get(track, track.replace("-", " ").title())


def question_kind(q):
    return q.get("kind") or ("reinforcement" if q.get("lab") else "review")


def question_language(q, track):
    return q.get("codeLanguage") or {"dotnet": "csharp", "go": "go", "kafka": "bash"}.get(track, "text")


def run_command(q, track):
    if not q.get("lab"):
        return ""
    lab = q["lab"]
    if track == "dotnet" and lab.endswith(".cs"):
        return f"dotnet run --file {lab}"
    if track == "go" and lab.endswith(".go"):
        return f"go run {lab}"
    if track == "python" and lab.endswith(".py"):
        return f"python3 {lab}"
    return ""  # Non-executable snippets must not masquerade as runnable labs.



def pth(q):
    return q["slug"] + ".md"


def safe_code(code, lang):
    if lang == "en":
        code = code.replace("// Завершён ли inner здесь — не гарантировано.", "// The inner task may still be incomplete here.")
        code = code.replace("// X могут появиться позже, а программа — завершиться.", "// X may print later, or the program may exit.")
        lines = []
        for line in code.splitlines():
            if re.search(r"[А-Яа-яЁё]", line) and "//" in line:
                line = line.split("//", 1)[0].rstrip()
            lines.append(line)
        return "\n".join(lines).rstrip()
    return code


def write_output(path: Path, content: str, check: bool, changed: list[str]):
    content = content.rstrip() + "\n"
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            if path.name in ("README.md", "README.en.md") and path.parent == ROOT:
                import difflib
                current = path.read_text(encoding="utf-8") if path.exists() else ""
                print("\\n".join(list(difflib.unified_diff(current.splitlines(), content.splitlines(), fromfile="committed", tofile="generated", lineterm=""))[:90]))
            changed.append(str(path.relative_to(ROOT)))
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))


def bullets(items):
    return "\n".join("- " + line for line in items)


def qfile(q, lang, other_lang, lesson, prev_q, next_q):
    title = lesson["title"]["en"] if lang == "en" else q["title"]
    track = track_of(lesson)
    filename = pth(q)
    if lang == "ru":
        switch = f"[Русский](./{filename}) · [English](en/{filename})"
        primary = "[Все вопросы](README.md) · [Учебная платформа](" + BASE + f"/#/ru/question/{q['id']})"
        topic = f"[Основная тема](../../topics/{track}/{lesson['id']}.md)"
        go_back = "← Предыдущий"
        go_next = "Следующий →"
        label = "Вопрос"
        answer_title = "Эталонный ответ — открыть после своего ответа"
        method_title = "Почему это работает"
        risk_title = "Риск или ошибка"
        garanti_title = "Что гарантировано"
        code_title = f"Фрагмент {title_of_track(track)} — попробуйте предсказать результат"
        run_title = "Запустить настоящий код"
        source_title = "Документация и исходники"
    else:
        switch = f"[Русский](../{filename}) · [English](./{filename})"
        primary = "[All questions](../README.en.md) · [Interactive handbook](" + BASE + f"/#/en/question/{q['id']})"
        topic = f"[Canonical lesson](../../../topics/{track}/en/{lesson['id']}.md)"
        go_back = "← Previous"
        go_next = "Next →"
        label = "Question"
        answer_title = "Model answer — reveal after your attempt"
        method_title = "Internal mechanism"
        risk_title = "Failure mode"
        garanti_title = "Guarantee / variability"
        code_title = f"{title_of_track(track)} challenge — predict the outcome first"
        run_title = "Run the actual code"
        source_title = "Documentation and source"
    baseprefix = "" if lang == "ru" else "../"
    near = []
    if prev_q:
        near.append(f"[{go_back}]({pth(prev_q) if lang == 'ru' else pth(prev_q)})")
    if next_q:
        near.append(f"[{go_next}]({pth(next_q) if lang == 'ru' else pth(next_q)})")
    nav = " · ".join([switch,primary,topic]+near)
    doc = [f"# {q['id']} — {title}", "", nav, "", f"## {label}", "", q["q"][lang], ""]
    if q["code"]:
        doc += [f"## {code_title}", "", "```"+question_language(q,track), safe_code(q["code"],lang), "```", ""]
        command = run_command(q,track)
        if command:
            lab_url = REPO + "/blob/main/" + q["lab"]
            actions = f" · [GitHub Actions]({REPO}/actions/workflows/run-lab.yml)" if track == "dotnet" else ""
            doc += [f"### {run_title}", "", "```bash", command, "```", "", f"[{q['lab'].split('/')[-1]}]({lab_url}){actions} · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)", ""]
    doc += ["<details>",f"<summary>{answer_title}</summary>","",q["a"][lang],"","</details>",""]
    if q["mechanism"]:
        doc += [f"### {method_title}", "",q["mechanism"],""]
    if q["risk"]:
        doc += [f"### {risk_title}", "", q["risk"],""] if lang=="ru" else []
    if q["guarantee"]:
        doc += [f"### {garanti_title}", "", q["guarantee"],""] if lang=="ru" else []
    if q["source"]:
        doc += [f"### {source_title}","",f"[{q['source']}]({q['source']})",""]
    doc += ["---","",nav,""]
    return "\n".join(doc)


def lesson_file(lesson,lang,questions):
    t=lesson; id=t["id"]; track=track_of(t)
    if lang == "ru":
        toggle = f"[Русский]({id}.md) · [English](en/{id}.md)"
        nav = f"[Главная](../../README.md) · [Все темы](README.md) · [Платформа]({BASE}/#/ru/lesson/{id})"
        q_link = lambda q: f"../../questions/{track}/{pth(q)}"
        headings = dict(why="Определение",inside="Механизм: от языка и runtime до ОС",resources="Ресурсы",pitfalls="Ограничения и риски",exercises="Вопросы для проверки",practice="Закрепление на коде",source="Первоисточники")
    else:
        toggle = f"[Русский](../{id}.md) · [English]({id}.md)"
        nav = f"[Home](../../../README.en.md) · [All topics](README.md) · [Learning app]({BASE}/#/en/lesson/{id})"
        q_link = lambda q: f"../../../questions/{track}/en/{pth(q)}"
        headings = dict(why="Definition",inside="Mechanics: language/runtime to OS",resources="Resources",pitfalls="Constraints and pitfalls",exercises="Review questions",practice="Reinforcement challenges",source="Primary references")
    doc=[f"# {t['title'][lang]}","",toggle,"",nav,"",t['desc'][lang],"",f"## {headings['why']}","",t['overview'][lang],"",f"## {headings['inside']}",""]
    doc += [f"{i}. {step[lang]}" for i,step in enumerate(t["mechanism"],1)]
    doc += ["",f"## {headings['resources']}",""]
    doc += [f"- **{r['name'][lang]}:** {r['detail'][lang]}" for r in t["resources"]]
    doc += ["",f"## {headings['pitfalls']}",""]
    doc += bullets([r[lang] for r in t["risks"]]).splitlines()
    core=[q for q in questions if question_kind(q)=="review" and int(q['id'][2:]) in t['questions']]
    pract=[q for q in questions if question_kind(q)=="reinforcement" and int(q['id'][2:]) in t['questions']]
    doc += ["",f"## {headings['exercises']}",""]
    doc += [f"- [{q['id']}: {q['q'][lang]}]({q_link(q)})" for q in core]
    doc += ["",f"## {headings['practice']}",""]
    doc += ([f"- [{q['id']}: {q['q'][lang]}]({q_link(q)})" for q in pract] if pract else ["—"])
    doc += ["",f"## {headings['source']}",""]
    doc += [f"- [{url}]({url})" for url in t['refs']]
    doc += ["", "---", "",toggle,"",nav,"" ]
    return "\n".join(doc)


def index_file(lessons, questions, lang, track):
    ru=lang=="ru"
    switch="[Русский](README.md) · [English](README.en.md)"
    head=f"# Вопросы и упражнения — {title_of_track(track)}" if ru else f"# {title_of_track(track)} questions and exercises"
    text="Каждый вопрос относится ровно к одной основной теме; похожие задачи выделены как упражнения для закрепления. Эталонные ответы скрыты до попытки." if ru else "Each question belongs to exactly one canonical lesson; related code challenges serve as reinforcement rather than repeated theory. Model answers are hidden until you attempt the question."
    prefix="" if ru else "en/"
    root="../../README.md" if ru else "../../README.en.md"
    site=BASE+"/#/"+lang+"/home"
    doc=[head,"",switch,"",f"[{'Главная' if ru else 'Home'}]({root}) · [{'Интерактивная платформа' if ru else 'Interactive learning'}]({site})","",text,""]
    m={int(i):t for t in lessons for i in t['questions']}
    for t in lessons:
        doc += [f"## {t['title'][lang]}","",f"[{'Основная тема' if ru else 'Canonical lesson'}]({'../../topics/'+track+'/' if ru else '../../topics/'+track+'/en/'}{t['id']}.md)",""]
        for q in questions:
            if int(q['id'][2:]) not in t['questions']:continue
            ispractice=question_kind(q)=="reinforcement"
            tag=" — закрепление" if ru else " — reinforcement"
            doc += [f"- [{q['id']}]({prefix}{pth(q)}): {q['q'][lang]}{tag if ispractice else ''}"]
        doc += [""]
    return "\n".join(doc)


def topics_index(lessons,lang,track):
    ru=lang=="ru"
    switch="[Русский](README.md) · [English](en/README.md)" if ru else "[Русский](../README.md) · [English](README.md)"
    doc=[f"# Основные темы {title_of_track(track)}" if ru else f"# Canonical {title_of_track(track)} lessons","",switch,"",('Основные механизмы объясняются ровно один раз. Дополнительные вопросы — примеры для закрепления.' if ru else 'Core mechanisms have one home; related challenges reinforce them instead of repeating the theory.'),""]
    for t in lessons:doc.append(f"- [{t['title'][lang]}]({t['id']}.md) — {t['desc'][lang]}")
    doc.append("")
    return "\n".join(doc)


def root_readme(lessons,lang):
    ru=lang=="ru"
    title="# Engineering Handbook — инженерный справочник" if ru else "# Engineering Handbook — software engineering learning"
    toggle="[Русский](README.md) · [English](README.en.md)"
    site=f"{BASE}/#/{lang}/home"
    doc=[title,"",toggle,"",('**Интерактивный учебник:** [открыть платформу](%s).'%site if ru else '**Interactive course:** [Open the learning app](%s).'%site),"",('Учебник по устройству языков, runtime, многопоточности, инфраструктуре и распределённым системам. Теория хранится отдельно от упражнений; один механизм — одна основная тема.' if ru else 'A technical learning handbook covering languages, runtimes, concurrency, infrastructure, and distributed systems. One canonical lesson per concept, with separate reinforcement exercises.'),"",('## Изучаемые темы' if ru else '## Curriculum'),""]
    catalog=json.loads((ROOT/"content/catalog.json").read_text(encoding="utf-8"))
    doc += ["| Направление | Темы |" if ru else "| Area | Topics |","|---|---|"]
    for group in catalog:
        path="catalog/"+("en/" if not ru else "")+group["id"]+".md"
        names=", ".join(track["title"][lang] for track in group["tracks"])
        doc.append("| ["+group["title"][lang]+"]("+path+") | "+names+" |")
    doc += ["","[Полный каталог](catalog/README.md)" if ru else "[Full catalog](catalog/README.en.md)",""]
    tracks = list(dict.fromkeys(track_of(t) for t in lessons))
    for track in tracks:
        doc += [f"### {title_of_track(track)}", ""]
        doc += [f"- [{t['title'][lang]}](topics/{track}/{'en/' if not ru else ''}{t['id']}.md) — {len(t['questions'])} {'вопросов и упражнений' if ru else 'questions and exercises'}" for t in lessons if track_of(t)==track]
        doc.append("")
    future = [title_of_track(t) for t in ('go','kafka','postgresql','kubernetes','linux','system-design') if t not in tracks]
    future_text = ", ".join(future) if future else ("Все запланированные направления открыты" if ru else "All planned tracks are available")
    doc += ["", ("## Пошаговое обучение и карточки" if ru else "## Deep-dive learning and flashcards"), "",
            ("- [Углублённые разделы C# / .NET](topics/dotnet/units/README.md)" if ru else "- [C# / .NET deep-dive units](topics/dotnet/units/en/README.md)"),
            (f"- [Карточки «Знаю / Не знаю»]({BASE}/#/ru/cards)" if ru else f"- [Know / Don\'t know flashcards]({BASE}/#/en/cards)"),
            ("- [Методика повторения](docs/learning-method.md)" if ru else "- [Spaced-repetition method](docs/learning-method.en.md)")]
    doc += ["",('## Практика и код' if ru else '## Practical challenges and code'),""]
    doc += [f"- [{title_of_track(track)} — {'Вопросы' if ru else 'Questions'}](questions/{track}/{'README.md' if ru else 'README.en.md'})" for track in tracks]
    doc += [f"- [{'Запускаемые лаборатории' if ru else 'Runnable C# labs'}](labs/{'README.md' if ru else 'README.en.md'})",f"- [{'Открыть Codespaces' if ru else 'Open Codespaces'}](https://codespaces.new/itprodavets/engineering-handbook)",f"- [{'Запустить выбранный пример через Actions' if ru else 'Run a selected lab through Actions'}]({REPO}/actions/workflows/run-lab.yml)","",('## Как запустить C#' if ru else '## Running C#'),"","```bash","dotnet run --file labs/dotnet/Q-024.cs","```","",('Сама страница GitHub Pages не компилирует C#. Для настоящего запуска используй Codespaces или GitHub Actions; интерактивная проверка ответов в браузере — это сравнение с эталоном, а не исполнение C#.' if ru else 'GitHub Pages does not compile C#. Use Codespaces or GitHub Actions for actual execution; in-browser answer checking compares your prediction against the reference, not executed C#.'),"",('## Следующие направления' if ru else '## Planned learning tracks'),"",(future_text+'. Разделы будут заполняться по мере прохождения — без дублирования теории.' if ru else future_text+'. New tracks are added when their first verified canonical lesson is ready.'),"",('## Личный прогресс' if ru else '## Learning progress'),"",('Результаты личных ответов и оценки — в приватной Google Таблице, не в репозитории. Браузерная платформа сохраняет отметки только локально на устройстве. GitHub Pages может быть публичным даже при приватном репозитории.' if ru else 'Personal answers and scores remain in the private Google Sheet, not in this repository. The browser app saves progress only on your device. GitHub Pages may be publicly reachable even when the repository is private.'),"",f"[{'Добавлять темы прямо из чата' if ru else 'Add topics from ChatGPT'}](docs/{'chat-authoring.md' if ru else 'chat-authoring.en.md'}) · [{'Как вносить изменения' if ru else 'Contributing'}]({'CONTRIBUTING.md' if ru else 'CONTRIBUTING.en.md'})",""]
    doc += [("[Структура репозитория](docs/repository-layout.md) · [Почему без SQLite](docs/storage.md) · [Бенчмарки](benchmarks/README.md)" if ru else "[Repository layout](docs/repository-layout.en.md) · [Why no SQLite](docs/storage.en.md) · [Benchmarks](benchmarks/README.en.md)"),""]
    return "\n".join(doc)



def catalog_index_file(catalog,lang):
    ru=lang=="ru"
    lines=["# Каталог знаний" if ru else "# Knowledge catalog","",
           "[Русский](README.md) · [English](README.en.md)","",
           "[Главная](../README.md)" if ru else "[Home](../README.en.md)","",""]
    for group in catalog:
        path=("en/" if not ru else "")+group["id"]+".md"
        lines += ["## ["+group["title"][lang]+"]("+path+")","",group["description"][lang],""]
    return "\n".join(lines)

def catalog_area_file(group,lessons,lang):
    ru=lang=="ru"
    fname=group["id"]+".md"
    toggle="[Русский]("+fname+") · [English](en/"+fname+")" if ru else "[Русский](../"+fname+") · [English]("+fname+")"
    nav="[Главная](../README.md) · [Каталог](README.md)" if ru else "[Home](../../README.en.md) · [Catalog](../README.en.md)"
    lines=["# "+group["title"][lang],"",toggle,"",nav,"",group["description"][lang],"",
           "## Технологии" if ru else "## Technologies",""]
    for track in group["tracks"]:
        lines += ["### "+track["title"][lang],""]
        found=[x for x in lessons if x.get("track","dotnet")==track["id"]]
        if found:
            for lesson in found:
                dest=("../" if ru else "../../")+"topics/"+track["id"]+"/"+("" if ru else "en/")+lesson["id"]+".md"
                lines += ["- ["+lesson["title"][lang]+"]("+dest+")"]
        else:
            lines += ["Запланировано — уроков пока нет." if ru else "Planned — no published lessons yet."]
        lines.append("")
    lines += ["---","",toggle]
    return "\n".join(lines)

def glossary_entries(lang):
    entries=json.loads((ROOT/'content/glossary.json').read_text(encoding='utf-8'))
    return [{'term':x['term'], 'definition':x['definition'][lang], 'translation':x['translation'] if lang=='ru' else '', 'example':x['example']} for x in entries]


def glossary_markdown(lang):
    entries=glossary_entries(lang)
    ru=lang=='ru'
    toggle=('[Русский](glossary.md) · [English](glossary.en.md)')
    lead='Термины C#/.NET, ОС и многопоточности. Полное объяснение механизма ищи в одной основной теме, а не в повторяющихся ответах.' if ru else 'C#/.NET, OS, and concurrency terminology. Full mechanisms live in one canonical lesson rather than being duplicated across answers.'
    nav=f"[{'Главная' if ru else 'Home'}](../{'README.md' if ru else 'README.en.md'}) · [{'Интерактивный глоссарий' if ru else 'Interactive glossary'}]({BASE}/#/{lang}/glossary)"
    md=[('# Глоссарий' if ru else '# Glossary'),'',toggle,'',nav,'',lead,'']
    for entry in entries:
        md += [f"## {entry['term']}",'',entry['definition'],'',f"{'Пример' if ru else 'Example'}: `{entry['example']}`",'']
    return '\n'.join(md)



def build(check=False):
    changed = []
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    lessons = json.loads(LESSONS.read_text(encoding="utf-8"))
    if not questions or not lessons:
        raise ValueError("At least one lesson and question is required")
    question_ids = [q["id"] for q in questions]
    if len(question_ids) != len(set(question_ids)) or any(not re.fullmatch(r"Q-[0-9]{3,}", i) for i in question_ids):
        raise ValueError("Question IDs must be unique in Q-### format")
    if len({t["id"] for t in lessons}) != len(lessons):
        raise ValueError("Lesson IDs must be unique across all tracks")

    lesson_map = {}
    for t in lessons:
        track = track_of(t)
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", track) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", t["id"]):
            raise ValueError(f"Unsafe track/lesson id: {track}/{t['id']}")
        for number in t["questions"]:
            if number in lesson_map:
                raise ValueError(f"Q-{number:03d} belongs to two lessons")
            lesson_map[number] = t
    numbered = {int(i[2:]) for i in question_ids}
    if set(lesson_map) != numbered:
        raise ValueError(f"Every question must have exactly one lesson; unmapped={sorted(numbered-set(lesson_map))}, absent={sorted(set(lesson_map)-numbered)}")

    tracks = list(dict.fromkeys(track_of(t) for t in lessons))
    for track in tracks:
        track_lessons = [t for t in lessons if track_of(t) == track]
        track_questions = [q for q in questions if track_of(lesson_map[int(q['id'][2:])]) == track]
        qdir = ROOT / "questions" / track
        tdir = ROOT / "topics" / track
        for i, q in enumerate(track_questions):
            lesson = lesson_map[int(q["id"][2:])]
            prev_q = track_questions[i-1] if i else None
            next_q = track_questions[i+1] if i < len(track_questions)-1 else None
            write_output(qdir / pth(q), qfile(q,"ru","en",lesson,prev_q,next_q),check,changed)
            write_output(qdir / "en" / pth(q), qfile(q,"en","ru",lesson,prev_q,next_q),check,changed)
        for lesson in track_lessons:
            write_output(tdir / f"{lesson['id']}.md", lesson_file(lesson,"ru",track_questions),check,changed)
            write_output(tdir / "en" / f"{lesson['id']}.md", lesson_file(lesson,"en",track_questions),check,changed)
        write_output(qdir / "README.md",index_file(track_lessons,track_questions,"ru",track),check,changed)
        write_output(qdir / "README.en.md",index_file(track_lessons,track_questions,"en",track),check,changed)
        write_output(tdir / "README.md",topics_index(track_lessons,"ru",track),check,changed)
        write_output(tdir / "en" / "README.md",topics_index(track_lessons,"en",track),check,changed)

    write_output(ROOT / "docs" / "glossary.md",glossary_markdown("ru"),check,changed)
    write_output(ROOT / "docs" / "glossary.en.md",glossary_markdown("en"),check,changed)
    write_output(ROOT / "README.md",root_readme(lessons,"ru"),check,changed)
    write_output(ROOT / "README.en.md",root_readme(lessons,"en"),check,changed)

    catalog=json.loads((ROOT/"content/catalog.json").read_text(encoding="utf-8"))
    write_output(ROOT/"catalog"/"README.md",catalog_index_file(catalog,"ru"),check,changed)
    write_output(ROOT/"catalog"/"README.en.md",catalog_index_file(catalog,"en"),check,changed)
    for group in catalog:
        write_output(ROOT/"catalog"/(group["id"]+".md"),catalog_area_file(group,lessons,"ru"),check,changed)
        write_output(ROOT/"catalog"/"en"/(group["id"]+".md"),catalog_area_file(group,lessons,"en"),check,changed)


    for lang in ("ru","en"):
        site_lessons = []
        for t in lessons:
            l = {k:v for k,v in t.items() if k not in ('title','desc','overview','mechanism','resources','risks')}
            l.update({
                'track':track_of(t),
                'title':t['title'][lang], 'desc':t['desc'][lang],
                'overview':t['overview'][lang],
                'mechanism':[x[lang] for x in t['mechanism']],
                'risks':[x[lang] for x in t['risks']],
                'resources':[{'name':x['name'][lang],'detail':x['detail'][lang]} for x in t['resources']]
            })
            site_lessons.append(l)
        site_questions=[]
        for q in questions:
            lesson=lesson_map[int(q["id"][2:])]
            track=track_of(lesson)
            site_questions.append({
                'id':q['id'],
                'title':q['title'] if lang=='ru' else lesson['title']['en'],
                'question':q['q'][lang], 'answer':q['a'][lang],
                'code':safe_code(q.get('code',''),lang),
                'expected':q.get('expected','') if lang=='ru' else '',
                'mechanism':q.get('mechanism','') if lang=='ru' else '',
                'risk':q.get('risk','') if lang=='ru' else '',
                'guarantee':q.get('guarantee','') if lang=='ru' else '',
                'source':q.get('source',''), 'terms':q.get('terms',''),
                'lab':q.get('lab'), 'track':track, 'codeLanguage':question_language(q,track),
                'runCommand':run_command(q,track),
                'checkOutput':q.get('checkOutput'),
                'lesson':lesson['id'], 'kind':question_kind(q),
                'markdown':f"questions/{track}/"+('en/' if lang=='en' else '')+pth(q)
            })
        payload={'language':lang,'lessons':site_lessons,'questions':site_questions,'glossary':glossary_entries(lang),'meta':{'questionCount':len(questions),'lessonCount':len(lessons),'version':2}}
        payload['catalog']=[{'id':g['id'],'title':g['title'][lang],'description':g['description'][lang],'tracks':[{'id':t['id'],'title':t['title'][lang]} for t in g['tracks']]} for g in catalog]
        payload['meta']['categoryCount']=len(catalog)
        write_output(SITE / 'data' / (lang+'.json'),json.dumps(payload,ensure_ascii=False,indent=2),check,changed)
    if check:
        if changed:
            print('STALE OUTPUTS:\n'+'\n'.join(changed))
            return 1
        print('PASS: generated Markdown, localized data and references are up to date.')
    else:
        print(f'Updated {len(changed)} generated files. {len(questions)} questions in two languages; {len(lessons)} canonical lessons across {len(tracks)} tracks.')
    return 0

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    sys.exit(build(args.check))
