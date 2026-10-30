# Структура Engineering Handbook

[Русский](repository-layout.md) · [English](repository-layout.en.md)

[Главная](../README.md) · [Каталог](../catalog/README.md)

**Категория → технология → основная тема → вопросы и лаборатории.**

- `content/catalog.json` — направления и названия технологий RU/EN.
- `content/lessons.json` — единая теория на двух языках.
- `content/questions.json` — вопросы и эталонные ответы, постоянные ID.
- `topics/<technology>/` — генерируемые Markdown-уроки RU/EN.
- `questions/<technology>/` — генерируемые вопросы RU/EN.
- `labs/<technology>/` — настоящий запускаемый код.
- `benchmarks/<technology>/` — воспроизводимые измерения.
- `docs/` — правила и структура учебника.
- `site/` — статический Pages-интерфейс.

Генератор создаёт README, страницы категорий и локализацию из JSON. Не редактируй генерируемые документы вручную. Один механизм — одно основное объяснение; повторные вопросы — закрепление.
