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
    filename = pth(q)
    if lang == "ru":
        switch = f"[Русский](./{filename}) · [English](en/{filename})"
        primary = "[Все вопросы](README.md) · [Учебная платформа](" + BASE + f"/#/ru/question/{q['id']})"
        topic = f"[Основная тема](../../topics/dotnet/{lesson['id']}.md)"
        go_back = "← Предыдущий"
        go_next = "Следующий →"
        label = "Вопрос"
        answer_title = "Эталонный ответ — открыть после своего ответа"
        method_title = "Почему это работает"
        risk_title = "Риск или ошибка"
        garanti_title = "Что гарантировано"
        code_title = "Фрагмент C# — попробуйте предсказать результат"
        run_title = "Запустить настоящий код"
        source_title = "Документация и исходники"
    else:
        switch = f"[Русский](../{filename}) · [English](./{filename})"
        primary = "[All questions](../README.en.md) · [Interactive handbook](" + BASE + f"/#/en/question/{q['id']})"
        topic = f"[Canonical lesson](../../../topics/dotnet/en/{lesson['id']}.md)"
        go_back = "← Previous"
        go_next = "Next →"
        label = "Question"
        answer_title = "Model answer — reveal after your attempt"
        method_title = "Internal mechanism"
        risk_title = "Failure mode"
        garanti_title = "Guarantee / variability"
        code_title = "C# challenge — predict the outcome first"
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
        doc += [f"## {code_title}","", "```csharp", safe_code(q["code"],lang),"```", ""]
        lab_url = REPO + "/blob/main/" + q["lab"]
        command = f"dotnet run --file {q['lab']}"
        doc += [f"### {run_title}","", "```bash",command,"```", "",f"[{q['id']}.cs]({lab_url}) · [GitHub Actions]({REPO}/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)", ""]
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
    t=lesson; id=t["id"]
    if lang == "ru":
        toggle = f"[Русский]({id}.md) · [English](en/{id}.md)"
        nav = f"[Главная](../../README.md) · [Все темы](README.md) · [Платформа]({BASE}/#/ru/lesson/{id})"
        q_link = lambda q: f"../../questions/dotnet/{pth(q)}"
        headings = dict(why="Определение",inside="Механизм: от C# до ОС",resources="Ресурсы",pitfalls="Ограничения и риски",exercises="Вопросы для проверки",practice="Закрепление на коде",source="Первоисточники")
    else:
        toggle = f"[Русский](../{id}.md) · [English]({id}.md)"
        nav = f"[Home](../../../README.en.md) · [All topics](README.md) · [Learning app]({BASE}/#/en/lesson/{id})"
        q_link = lambda q: f"../../../questions/dotnet/en/{pth(q)}"
        headings = dict(why="Definition",inside="Mechanics: C# to OS",resources="Resources",pitfalls="Constraints and pitfalls",exercises="Review questions",practice="Reinforcement challenges",source="Primary references")
    doc=[f"# {t['title'][lang]}","",toggle,"",nav,"",t['desc'][lang],"",f"## {headings['why']}","",t['overview'][lang],"",f"## {headings['inside']}",""]
    doc += [f"{i}. {step[lang]}" for i,step in enumerate(t["mechanism"],1)]
    doc += ["",f"## {headings['resources']}",""]
    doc += [f"- **{r['name'][lang]}:** {r['detail'][lang]}" for r in t["resources"]]
    doc += ["",f"## {headings['pitfalls']}",""]
    doc += bullets([r[lang] for r in t["risks"]]).splitlines()
    core=[q for q in questions if int(q['id'][2:])<24 and int(q['id'][2:]) in t['questions']]
    pract=[q for q in questions if int(q['id'][2:])>=24 and int(q['id'][2:]) in t['questions']]
    doc += ["",f"## {headings['exercises']}",""]
    doc += [f"- [{q['id']}: {q['q'][lang]}]({q_link(q)})" for q in core]
    doc += ["",f"## {headings['practice']}",""]
    doc += ([f"- [{q['id']}: {q['q'][lang]}]({q_link(q)})" for q in pract] if pract else ["—"])
    doc += ["",f"## {headings['source']}",""]
    doc += [f"- [{url}]({url})" for url in t['refs']]
    doc += ["", "---", "",toggle,"",nav,"" ]
    return "\n".join(doc)


def index_file(lessons, questions, lang):
    ru=lang=="ru"
    switch="[Русский](README.md) · [English](README.en.md)"
    head="# Вопросы и упражнения — C# / .NET" if ru else "# C# / .NET questions and exercises"
    text="Каждый вопрос относится ровно к одной основной теме; похожие задачи выделены как упражнения для закрепления. Эталонные ответы скрыты до попытки." if ru else "Each question belongs to exactly one canonical lesson; related code challenges serve as reinforcement rather than repeated theory. Model answers are hidden until you attempt the question."
    prefix="" if ru else "en/"
    root="../../README.md" if ru else "../../README.en.md"
    site=BASE+"/#/"+lang+"/home"
    doc=[head,"",switch,"",f"[{'Главная' if ru else 'Home'}]({root}) · [{'Интерактивная платформа' if ru else 'Interactive learning'}]({site})","",text,""]
    m={int(i):t for t in lessons for i in t['questions']}
    for t in lessons:
        doc += [f"## {t['title'][lang]}","",f"[{'Основная тема' if ru else 'Canonical lesson'}]({'../../topics/dotnet/' if ru else '../../topics/dotnet/en/'}{t['id']}.md)",""]
        for q in questions:
            if int(q['id'][2:]) not in t['questions']:continue
            ispractice=int(q['id'][2:])>=24
            tag=" — закрепление" if ru else " — reinforcement"
            doc += [f"- [{q['id']}]({prefix}{pth(q)}): {q['q'][lang]}{tag if ispractice else ''}"]
        doc += [""]
    return "\n".join(doc)


def topics_index(lessons,lang):
    ru=lang=="ru"
    switch="[Русский](README.md) · [English](en/README.md)" if ru else "[Русский](../README.md) · [English](README.md)"
    doc=["# Основные темы C# / .NET" if ru else "# Canonical C# / .NET lessons","",switch,"",('Основные механизмы объясняются ровно один раз. Дополнительные вопросы — примеры для закрепления.' if ru else 'Core mechanisms have one home; related challenges reinforce them instead of repeating the theory.'),""]
    for t in lessons:doc.append(f"- [{t['title'][lang]}]({t['id']}.md) — {t['desc'][lang]}")
    doc.append("")
    return "\n".join(doc)


def root_readme(lessons,lang):
    ru=lang=="ru"
    title="# Engineering Handbook — инженерный справочник" if ru else "# Engineering Handbook — software engineering learning"
    toggle="[Русский](README.md) · [English](README.en.md)"
    site=f"{BASE}/#/{lang}/home"
    doc=[title,"",toggle,"",('**Интерактивный учебник:** [открыть платформу](%s).'%site if ru else '**Interactive course:** [Open the learning app](%s).'%site),"",('Учебник по устройству языков, runtime, многопоточности, инфраструктуре и распределённым системам. Теория хранится отдельно от упражнений; один механизм — одна основная тема.' if ru else 'A technical learning handbook covering languages, runtimes, concurrency, infrastructure, and distributed systems. One canonical lesson per concept, with separate reinforcement exercises.'),"",('## Изучаемые темы' if ru else '## Curriculum'),""]
    doc += [f"- [{t['title'][lang]}](topics/dotnet/{'en/' if not ru else ''}{t['id']}.md) — {len(t['questions'])} {'вопросов и упражнений' if ru else 'questions and exercises'}" for t in lessons]
    doc += ["",('## Практика и код' if ru else '## Practical challenges and code'),"",f"- [{'Вопросы и ответы' if ru else 'Questions and answers'}](questions/dotnet/{'README.md' if ru else 'README.en.md'})",f"- [{'Запускаемые лаборатории' if ru else 'Runnable C# labs'}](labs/{'README.md' if ru else 'README.en.md'})",f"- [{'Открыть Codespaces' if ru else 'Open Codespaces'}](https://codespaces.new/itprodavets/engineering-handbook)",f"- [{'Запустить выбранный пример через Actions' if ru else 'Run a selected lab through Actions'}]({REPO}/actions/workflows/run-lab.yml)","",('## Как запустить C#' if ru else '## Running C#'),"","```bash","dotnet run --file labs/dotnet/Q-024.cs","```","",('Сама страница GitHub Pages не компилирует C#. Для настоящего запуска используй Codespaces или GitHub Actions; интерактивная проверка ответов в браузере — это сравнение с эталоном, а не исполнение C#.' if ru else 'GitHub Pages does not compile C#. Use Codespaces or GitHub Actions for actual execution; in-browser answer checking compares your prediction against the reference, not executed C#.'),"",('## Следующие направления' if ru else '## Planned learning tracks'),"",('Go, Kafka, PostgreSQL, Kubernetes, Linux, system design. Разделы будут заполняться по мере прохождения — без дублирования теории.' if ru else 'Go, Kafka, PostgreSQL, Kubernetes, Linux, and system design. These tracks will be filled with actual lessons, without duplicating theory.'),"",('## Личный прогресс' if ru else '## Learning progress'),"",('Результаты личных ответов и оценки — в приватной Google Таблице, не в репозитории. Браузерная платформа сохраняет отметки только локально на устройстве. GitHub Pages может быть публичным даже при приватном репозитории.' if ru else 'Personal answers and scores remain in the private Google Sheet, not in this repository. The browser app saves progress only on your device. GitHub Pages may be publicly reachable even when the repository is private.'),"",f"[{'Как вносить изменения' if ru else 'Contributing'}]({'CONTRIBUTING.md' if ru else 'CONTRIBUTING.en.md'})",""]
    return "\n".join(doc)


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
    changed=[]
    questions=json.loads(QUESTIONS.read_text(encoding="utf-8"))
    lessons=json.loads(LESSONS.read_text(encoding="utf-8"))
    qmap={q["id"]:q for q in questions}
    lesson_map={n:t for t in lessons for n in t["questions"]}
    assert len(questions)==35 and len(lessons)==8
    assert sorted(lesson_map)==list(range(1,36))
    for i,q in enumerate(questions):
        lid=lesson_map[int(q['id'][2:])]
        prev_q=questions[i-1] if i else None
        next_q=questions[i+1] if i<len(questions)-1 else None
        write_output(QDIR/pth(q),qfile(q,"ru","en",lid,prev_q,next_q),check,changed)
        write_output(QDIR/"en"/pth(q),qfile(q,"en","ru",lid,prev_q,next_q),check,changed)
    for lesson in lessons:
        write_output(TDIR/f"{lesson['id']}.md",lesson_file(lesson,"ru",questions),check,changed)
        write_output(TDIR/"en"/f"{lesson['id']}.md",lesson_file(lesson,"en",questions),check,changed)
    write_output(QDIR/"README.md",index_file(lessons,questions,"ru"),check,changed)
    write_output(QDIR/"README.en.md",index_file(lessons,questions,"en"),check,changed)
    write_output(TDIR/"README.md",topics_index(lessons,"ru"),check,changed)
    write_output(TDIR/"en"/"README.md",topics_index(lessons,"en"),check,changed)
    write_output(ROOT/"docs"/"glossary.md",glossary_markdown("ru"),check,changed)
    write_output(ROOT/"docs"/"glossary.en.md",glossary_markdown("en"),check,changed)
    write_output(ROOT/"README.md",root_readme(lessons,"ru"),check,changed)
    write_output(ROOT/"README.en.md",root_readme(lessons,"en"),check,changed)
    for lang in ("ru","en"):
        site_lessons=[]
        for t in lessons:
            l={k:v for k,v in t.items() if k not in ('title','desc','overview','mechanism','resources','risks')}
            l.update({'title':t['title'][lang], 'desc':t['desc'][lang], 'overview':t['overview'][lang], 'mechanism':[x[lang] for x in t['mechanism']], 'risks':[x[lang] for x in t['risks']], 'resources':[{'name':x['name'][lang],'detail':x['detail'][lang]} for x in t['resources']]})
            site_lessons.append(l)
        site_questions=[]
        for q in questions:
            site_questions.append({'id':q['id'],'title':q['title'] if lang=='ru' else lesson_map[int(q['id'][2:])]['title']['en'], 'question':q['q'][lang], 'answer':q['a'][lang], 'code':safe_code(q['code'],lang), 'expected':q['expected'] if lang=='ru' else '', 'mechanism':q['mechanism'] if lang=='ru' else '', 'risk':q['risk'] if lang=='ru' else '', 'guarantee':q['guarantee'] if lang=='ru' else '', 'source':q['source'], 'terms':q['terms'], 'lab':q['lab'], 'lesson':lesson_map[int(q['id'][2:])]['id'], 'kind':'reinforcement' if int(q['id'][2:])>=24 else 'review', 'markdown': 'questions/dotnet/'+('en/' if lang=='en' else '')+pth(q)})
        payload={'language':lang,'lessons':site_lessons,'questions':site_questions,'glossary':glossary_entries(lang),'meta':{'questionCount':len(questions),'lessonCount':len(lessons),'version':1}}
        write_output(SITE/"data"/(lang+".json"),json.dumps(payload,ensure_ascii=False,indent=2),check,changed)
    if check:
        if changed:
            print('STALE OUTPUTS:\n'+'\n'.join(changed));return 1
        print('PASS: generated Markdown, i18n content and references are up to date.')
    else:
        print(f'Updated {len(changed)} generated files. {len(questions)} questions in two languages; {len(lessons)} canonical lessons.')
    return 0

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    sys.exit(build(args.check))
