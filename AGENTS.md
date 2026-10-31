# Agent instructions — Engineering Handbook

This is a **public-safe**, bilingual, source-controlled learning handbook. Keep the source of truth in `content/*.json`, not in generated Markdown or `site/data/*.json`.

## When a user asks in ChatGPT to add or revise a lesson

1. Read `content/lessons.json`, `content/questions.json`, existing topic pages, and `docs/technical-accuracy.md`. Check for conceptual overlap **before** writing anything.
2. **One mechanism → one canonical lesson.** Improve an existing lesson rather than duplicating it. Related interview questions and puzzles are reinforcement linked to that one lesson.
3. Add Russian and English fields together; do not mix explanatory prose across languages. Use precise definitions at the compiler, runtime, OS, CPU, memory and concurrency levels when relevant. Distinguish guarantees, implementation-specific behavior and measured behavior. Do not invent quantitative resource estimates.
4. Each new question gets the next global stable `Q-###` identifier. Each Q belongs to exactly one lesson in `content/lessons.json`. Questions with runnable code should use `kind: "reinforcement"`, a matching lab file and verification where deterministic. Questions without labs may be review questions.
5. New lessons use a stable unique slug `id`, `track` such as `dotnet`, `go`, `kafka`, `postgresql`, and `stage` (`execution`, `concurrency`, `reliability`, or a new meaningful stage). Do not create empty placeholder lessons.
6. Add actual examples in `labs/<track>/`, e.g. `.cs` for .NET or `.go` for Go; never claim browser JS has executed a snippet. Include real run commands when supported. Never put secrets or personal answers/grades in this repo.
7. Regenerate with `python3 scripts/build_site.py`, then run `python3 scripts/build_site.py --check`, `python3 scripts/check_site.py`, `python3 scripts/check_links.py`, and `node --check site/assets/app.js`. Run relevant language labs or verify CI; report anything not executed.
8. Make a coherent Git commit (or one PR for the complete scope), verify the updated files on GitHub, and link the relevant lesson/question/commit to the user. Avoid repeated micro-PRs.
9. Personal scores and user answers belong only in the separately connected private Google Sheet. Do not sync them into public GitHub or Pages.

References: [Chat-based authoring (RU)](docs/chat-authoring.md) · [English](docs/chat-authoring.en.md) · [Technical accuracy](docs/technical-accuracy.md).

New categories are registered in `content/catalog.json`; keep the knowledge map and Pages data synchronized. See [repository layout](docs/repository-layout.md) and [storage design](docs/storage.md). Do not add private user scores to public content.

## Deep-dive units and cards

Canonical deep technical explanations belong in content/units.json: one unit per distinct mechanism, with Russian and English definitions, compiler/runtime/OS steps, resources, failure modes and the relevant question IDs. Each question has exactly one unit owner; do not duplicate explanations in practice cards. Generate with scripts/build_units.py and scripts/build_site.py, then run both --check validations. Browser-local SRS progress must never be committed to public GitHub. [Learning method](docs/learning-method.en.md).

## Interview-depth course authoring

For a complete technical module, do not stop at the four-point summary. In content/units.json supply focused `chapters` (one mechanism per chapter), reference links, runnable `labFiles`, and five `checks` in strict order Recall → Explain → Predict → Diagnose → Design. Each check has a question and *hidden rubric* in both RU and EN. Keep each existing Q ID owned by a single unit, and include expected behavior only when deterministic. Preserve the private self-ratings under browser localStorage keys (not Git). Review docs/engineering-interview.md before adding more content.
