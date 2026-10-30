# Engineering Handbook layout

[Русский](repository-layout.md) · [English](repository-layout.en.md)

[Home](../README.en.md) · [Catalog](../catalog/README.en.md)

**Category → technology → canonical lesson → questions and labs.**

- `content/catalog.json` — localized taxonomy.
- `content/lessons.json` — canonical bilingual lessons.
- `content/questions.json` — questions, model answers, stable IDs.
- `topics/<technology>/` — generated Markdown lessons (RU/EN).
- `questions/<technology>/` — generated questions (RU/EN).
- `labs/<technology>/` — executable examples.
- `benchmarks/<technology>/` — reproducible measurements.
- `docs/` — handbook architecture and contribution rules.
- `site/` — static Pages frontend.

The generator builds README, category pages, and locales from JSON. Do not manually edit generated Markdown. Explain one mechanism once and use questions for reinforcement.
