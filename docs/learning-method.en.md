# Structured learning, depth checks and spaced repetition

[Русский](learning-method.md) · [English](learning-method.en.md)

[Home](../README.en.md) · [Deep-dive units](../topics/dotnet/units/en/README.md) · [Flashcards](https://itprodavets.github.io/engineering-handbook/#/en/cards)

## Five layers of a technical mechanism

Follow **engineering area → module → detailed unit → reproducible experiment → knowledge check → focused spaced review**. Each idea has **one canonical explanation**, with related questions and labs linking to it.

The reference [Async/Await module](../topics/dotnet/en/async-lifecycle.md) contains **six ordered units**: I/O versus CPU → awaiter contract → compiler state machine → socket I/O → allocations → production diagnostics. Each unit includes separate RU/EN explanations, code, resource costs, pitfalls and assessment criteria.

## Evidence of competence

| Level | Demonstration |
|---|---|
| **Recall** | Exact definition and important limitations |
| **Explain** | C# → Roslyn → CLR/JIT → OS mechanism |
| **Predict** | Predict unseen code behavior before running it |
| **Diagnose** | Form hypotheses and verify them using metrics/traces |
| **Design** | Choose a production solution and justify trade-offs |

**Write your explanation first**, then reveal the rubric and self-grade: Not yet / Partially / Can justify. These ratings are **self-assessments**, not certifications. Predict, Diagnose and Design require actual code execution and measurement evidence. See the [interview methodology](engineering-interview.en.md).

## Weak skills become review cards

A rating of Not yet or Partially adds a review card **specific to the failed skill**. Regular question cards unlock **after studying the owning unit**; previously started cards remain accessible.

**Don't know:** repeat in 10 minutes. **Know:** progress through 1, 3, 7, 14, 30, 60, 120, 240 days, with at most 10 new cards daily. This is a fixed scheduler, **not Anki FSRS**.

## Storage and privacy

Public sources: `content/units.json`, `content/questions.json`, `labs/<track>/`, generated Markdown and Pages files. Private browser-only values: `eh:units:v1`, `eh:mastery:v1`, `eh:mastery-drafts:v1`, `eh:srs:v1` in localStorage. There is no cross-device sync yet; clearing browser data can erase your progress. Separate Google Sheet grades remain private.

## Authoring workflow

Edit canonical `content/units.json` and `content/questions.json`, then run:

```bash
python3 scripts/build_site.py
python3 scripts/build_units.py
python3 scripts/build_site.py --check
python3 scripts/build_units.py --check
python3 scripts/check_site.py
python3 scripts/check_links.py
node --test tests/spaced-repetition.test.mjs tests/mastery.test.mjs
python3 scripts/check_deep_labs.py   # Requires .NET 10 SDK
```

[Async/Await runnable labs](../labs/dotnet/async-internals/README.en.md) · [Adding content from ChatGPT](chat-authoring.en.md)
