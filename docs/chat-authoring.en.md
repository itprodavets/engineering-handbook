# Extending Engineering Handbook from ChatGPT

[Русский](chat-authoring.md) · [English](chat-authoring.en.md)

[Home](../README.en.md) · [Technical accuracy](technical-accuracy.en.md)

You do not need to write Markdown or JSON manually. Simply say:

> Add a new topic on Go's scheduler. First check for duplicate concepts, then explain the runtime and OS behavior in RU/EN, add two interview questions, and provide a runnable lab.

> Add this tricky C# snippet as reinforcement for the existing ThreadPool lesson. Include a precise answer, resource accounting, failure conditions, and primary references.

## Workflow

1. Reuse canonical explanations in [content/lessons.json](../content/lessons.json); never duplicate the same underlying mechanism.
2. Add a stable Q-### to [content/questions.json](../content/questions.json), associated with exactly one lesson.
3. Put runnable examples under [labs](../labs/README.en.md).
4. Regenerate localized Markdown and Pages content, validate links and code, commit one scoped change, and provide direct links.

Personal answers and grades remain in the private Google Sheet, never in the public repository.

[Agent instructions](../AGENTS.md) · [Contribution guide](../CONTRIBUTING.en.md)
