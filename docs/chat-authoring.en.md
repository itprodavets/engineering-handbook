# Adding lessons to Engineering Handbook from ChatGPT

[Русский](chat-authoring.md) · [English](chat-authoring.en.md)

[Home](../README.en.md) · [Curriculum](../topics/dotnet/en/README.md) · [Accuracy rules](technical-accuracy.en.md)

You do **not** need to write Markdown, JSON, or source files manually. Just ask in our ChatGPT conversation:

> Add a new Engineering Handbook topic on **Go's G/M/P scheduler**. Deduplicate existing topics, explain the runtime/OS mechanics in RU and EN, and add two interview questions plus a runnable lab.

Or:

> Add this C# snippet as a reinforcement challenge for the existing ThreadPool lesson. Explain the runtime resources, include the verified output, and update the site.

Or:

> Review Q-009 against the .NET 10 source, correct the definition in both languages, regenerate pages, and verify CI.

## Source of truth and publishing flow

1. Read [`content/lessons.json`](../content/lessons.json) and reuse the canonical explanation of an existing concept.
2. Add or refine one bilingual lesson with a stable ID, a technology `track` and a `stage`; cite authoritative references.
3. Allocate the next global `Q-###` in [`content/questions.json`](../content/questions.json). Each question belongs to **exactly one** canonical lesson.
4. Include runnable examples in `labs/<track>/`, with an explicit run command and deterministic verification where possible.
5. Regenerate localized Markdown, links, and site data from canonical JSON. Do **not** hand-edit generated pages.
6. Validate links, localization, source, and executable examples; commit as one cohesive change and share the GitHub link.

## Standards

- One core mechanism has one authoritative lesson; similar questions reinforce it rather than repeat theory.
- Keep Russian and English explanations separate, with a language switch preserving the current page.
- Distinguish language/API guarantees from runtime implementation and measured behavior.
- Personal answers, scores, business context, tokens, or secrets must stay out of public GitHub and Pages.

```bash
python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 scripts/check_site.py
python3 scripts/check_links.py
node --check site/assets/app.js
python3 scripts/check_labs.py  # if .NET 10 SDK is available
```

[Agent rules](../AGENTS.md) · [Contributor guide](../CONTRIBUTING.en.md)
