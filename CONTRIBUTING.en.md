# Contributing to the handbook

[Русский](CONTRIBUTING.md) · [English](CONTRIBUTING.en.md)

[Home](README.en.md) · [Interactive platform](https://itprodavets.github.io/engineering-handbook/#/en/home)

## One core explanation per concept

If a concept already exists in `content/lessons.json`, extend that **canonical lesson**. Add related questions as reinforcement challenges. Do not create a second lesson with duplicated theory.

## Single source of truth

- `content/lessons.json` — localized lessons and question ownership.
- `content/questions.json` — bilingual questions, model answers, and original snippets.
- `content/glossary.json` — technical definitions for both locales.
- `labs/dotnet/*.cs` — runnable C# labs.
- `site/assets/` — the static learning UI (contains no personal data).

Do not edit generated Markdown pages directly. Rebuild them using:

```bash
python3 scripts/build_site.py
python3 scripts/check_links.py
python3 scripts/check_site.py
node --check site/assets/app.js
```

New languages and platforms should introduce their own curricula with one canonical mechanism per lesson. Keep stable question IDs and link reinforcement challenges back to the core lesson.

**Never commit personal answers, scores, or credentials.**
## Add from ChatGPT

[How to add new topics from chat](docs/chat-authoring.en.md). After updating canonical JSON and running the generator, new topics and questions appear in localized navigation and Pages automatically. Do not edit `site/data` directly.

New technologies use the lesson's `track` (for example `go` or `kafka`). Question IDs remain global; `kind: "review"` is a knowledge question and `kind: "reinforcement"` is a code or applied exercise. Keep executable examples and their run commands separate from theory.

## Categories

Register new technology tracks in [`content/catalog.json`](content/catalog.json). The generator updates README, RU/EN category pages and Pages datasets. [Repository layout](docs/repository-layout.en.md).
