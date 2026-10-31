# Structured learning and spaced repetition

[Русский](learning-method.md) · [English](learning-method.en.md)

[Home](../README.en.md) · [Learning units](../topics/dotnet/units/en/README.md) · [Flashcards](https://itprodavets.github.io/engineering-handbook/#/en/cards)

**Path:** engineering area → module → deep-dive unit → code lab/question → spaced-repetition card.

Each mechanism has one canonical explanation: definition, compiler, runtime, OS, resources, concurrency failure modes, code and references. Questions reinforce that content rather than duplicating the theory.

## Spaced repetition

- Don't know: repeat in **10 minutes** and reset the correct-answer streak.
- Know: next intervals **1, 3, 7, 14, 30, 60, 120, 240 days**.
- At most **10 new cards per day**; due reviews take priority.

This is a simple fixed scheduler, **not Anki FSRS**. Intervals are counted from grading time.

## Personal data

Completion flags and card schedules live in this browser's localStorage, not the public GitHub repository. There is no cross-device sync yet; clearing browser data can erase progress.

## Source of truth

- content/units.json — bilingual units.
- content/questions.json — one question/card bank.
- labs/<track>/ — runnable experiments.
- scripts/build_units.py — generated Markdown and Pages data.

[Add lessons from chat](chat-authoring.en.md)
