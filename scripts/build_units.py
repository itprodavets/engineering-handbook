#!/usr/bin/env python3
"""Generate RU/EN deep-dive Markdown from content/units.json and sync Pages data."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tr(obj, lang):
    value = obj.get(lang)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing {lang} translation")
    return value


def page(u, lang, qmap, group):
    ru = lang == "ru"
    root = "../../../" if ru else "../../../../"
    module = "../" + u["lesson"] + ".md" if ru else "../../en/" + u["lesson"] + ".md"
    qdir = root + "questions/" + u.get("track", "dotnet") + "/" + ("" if ru else "en/")
    slug = u["id"]
    switch = (f"[Русский]({slug}.md) · [English](en/{slug}.md)" if ru
              else f"[Русский](../{slug}.md) · [English]({slug}.md)")
    lines = [
        "# " + tr(u["title"], lang), "", switch, "",
        f"[{'Главная' if ru else 'Home'}]({root}{'README.md' if ru else 'README.en.md'}) · "
        f"[{'Модуль' if ru else 'Module'}]({module}) · "
        f"[{'Все разделы' if ru else 'All units'}](README.md) · "
        f"[{'Платформа' if ru else 'Learning app'}]"
        f"(https://itprodavets.github.io/engineering-handbook/#/{lang}/unit/{slug})",
        "", "> " + tr(u["goal"], lang), "",
        "## " + ("Определение" if ru else "Definition"), "",
        tr(u["definition"], lang), "",
        "## " + ("Внутренний механизм" if ru else "Internal mechanics"), "",
    ]
    lines += [f"{i}. {tr(step, lang)}" for i, step in enumerate(u["steps"], 1)]
    lines += ["", "## " + ("Потребляемые ресурсы" if ru else "Resources"),
              "", tr(u["resources"], lang), "",
              "## " + ("Ошибки и ограничения" if ru else "Pitfalls and constraints"),
              "", tr(u["pitfalls"], lang), ""]
    if u.get("code"):
        lines += ["## " + ("Пример" if ru else "Example"), "",
                  chr(96)*3 + u.get("codeLanguage", "csharp"),
                  u["code"].rstrip(), chr(96)*3, ""]
    lines += ["## " + ("Вопросы для закрепления" if ru else "Review questions"), ""]
    for n in u["questions"]:
        q = qmap[f"Q-{n:03d}"]
        lines.append(f"- [{q['id']}: {tr(q['q'], lang)}]({qdir}{q['slug']}.md)")
    lines += ["", "## " + ("Источники" if ru else "References"), ""]
    lines += [f"- [{ref}]({ref})" for ref in u.get("refs", [])]
    pos = group.index(u)
    nav = []
    if pos > 0:
        nav.append(f"[{'← Назад' if ru else '← Previous'}]({group[pos-1]['id']}.md)")
    if pos + 1 < len(group):
        nav.append(f"[{'Далее →' if ru else 'Next →'}]({group[pos+1]['id']}.md)")
    lines += ["", "---", "", " · ".join(nav + [switch]), ""]
    return "\n".join(lines).rstrip() + "\n"


def index(units, lessons, lang):
    ru = lang == "ru"
    lines = ["# " + ("Разделы углублённого обучения" if ru else "Deep-dive learning units"),
             "", ("[Русский](README.md) · [English](en/README.md)" if ru
                  else "[Русский](../README.md) · [English](README.md)"),
             "", ("Один механизм — одно объяснение. Вопросы закрепляют материал." if ru
                  else "One mechanism, one canonical explanation; questions reinforce it."), ""]
    for lid in dict.fromkeys(u["lesson"] for u in units):
        module = "../" + lid + ".md" if ru else "../../en/" + lid + ".md"
        lines += ["## [" + tr(lessons[lid]["title"], lang) + "](" + module + ")", ""]
        lines += ["- [" + tr(u["title"], lang) + "](" + u["id"] + ".md) — " +
                  tr(u["goal"], lang) for u in units if u["lesson"] == lid]
        lines += [""]
    return "\n".join(lines).rstrip() + "\n"


def main(check):
    source = ROOT / "content/units.json"
    units = json.loads(source.read_text(encoding="utf-8"))
    questions = {q["id"]:q for q in json.loads((ROOT/"content/questions.json").read_text())}
    lessons = {l["id"]:l for l in json.loads((ROOT/"content/lessons.json").read_text())}
    owned = {}
    seen = set()
    for u in units:
        if u["id"] in seen or not re.fullmatch(r"[a-z][a-z0-9-]*",u["id"]):
            raise ValueError("Duplicate/invalid unit ID")
        seen.add(u["id"])
        if u["lesson"] not in lessons:
            raise ValueError("Missing parent module")
        if u.get("track","dotnet") != lessons[u["lesson"]].get("track","dotnet"):
            raise ValueError("Unit track differs from its module")
        for field in ("title","goal","definition","resources","pitfalls"):
            for lang in ("ru","en"):
                tr(u[field],lang)
        if len(u["steps"]) < 3:
            raise ValueError("Unit must explain actual mechanics")
        for step in u["steps"]:
            tr(step,"ru");tr(step,"en")
        for n in u["questions"]:
            qid = f"Q-{n:03d}"
            if qid not in questions:
                raise ValueError(f"Missing question {qid}")
            if qid in owned:
                raise ValueError(f"Duplicated question in two units: {qid}")
            owned[qid] = u["lesson"]
    if set(owned) != set(questions):
        raise ValueError(f"Questions without canonical units: {set(questions)-set(owned)}")
    for lid,lesson in lessons.items():
        for n in lesson["questions"]:
            if owned.get(f"Q-{n:03d}") != lid:
                raise ValueError(f"Question ownership wrong: {n}")
    targets = {ROOT/"site/data/units.json":source.read_text(encoding="utf-8")}
    for lang in ("ru","en"):
        for track in dict.fromkeys(u.get("track","dotnet") for u in units):
            track_units=[u for u in units if u.get("track","dotnet")==track]
            directory = ROOT/"topics"/track/"units"/("" if lang=="ru" else "en")
            targets[directory/"README.md"]=index(track_units,lessons,lang)
            for u in track_units:
                group=[v for v in track_units if v["lesson"]==u["lesson"]]
                targets[directory/(u["id"]+".md")]=page(u,lang,questions,group)
    stale=[]
    for path,content in targets.items():
        if not path.exists() or path.read_text(encoding="utf-8")!=content:
            stale.append(str(path.relative_to(ROOT)))
            if not check:
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(content,encoding="utf-8")
    if check and stale:
        raise SystemExit("Outdated files:\n"+"\n".join(stale))
    print(f"PASS: {len(units)} detailed units, {len(owned)} questions, {len(targets)} outputs.")
    return 0

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    raise SystemExit(main(args.check))
