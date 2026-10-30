# Engineering Handbook — instructions for AI collaborators

## When the user asks to add content from ChatGPT

1. Read content/lessons.json and content/questions.json first. One mechanism has one canonical lesson: improve it instead of duplicating theory.
2. Create separate Russian and English explanations. Distinguish language/API guarantees, runtime and OS implementation, resource use, concurrency risks and measurements.
3. Assign the next global Q-### identifier, link it to exactly one lesson, and use code challenges only as reinforcement.
4. Put runnable examples in labs/ and verify their behavior; do not claim that GitHub Markdown or Pages executes source code.
5. Update canonical JSON, regenerate RU/EN Markdown and Pages data with python3 scripts/build_site.py, then run the build, link and code checks.
6. For a first Go, Kafka or other new track, extend generator routes and technology-specific examples in the same scoped change. Never put Go/Kafka content inside .NET topic folders.
7. Commit a coherent change, verify CI, and link the exact lesson and commit in chat.
8. Do not publish personal answers, grades, secret tokens or private business context. They belong outside public GitHub.

[Инструкция RU](docs/chat-authoring.md) · [Guide EN](docs/chat-authoring.en.md) · [Technical accuracy](docs/technical-accuracy.md)
