# Q-039 — Race vs Data Race

[Русский](./Q-039-race-condition-vs-data-race.md) · [English](en/Q-039-race-condition-vs-data-race.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-039) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-038-inline-apm-callback-captured-result.md) · [Следующий →](Q-040-lost-update-two-task-run.md)

## Вопрос

Чем отличается Race Condition от Data Race и может ли логическая гонка возникнуть без data race?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Race Condition — нарушение инварианта из-за допустимого порядка конкурентных событий. Data Race — конфликтующие несинхронизированные обращения к общей области памяти (одно — запись). Две отдельно атомарные операции check и act могут создать логическую гонку без data race.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices](https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices)

---

[Русский](./Q-039-race-condition-vs-data-race.md) · [English](en/Q-039-race-condition-vs-data-race.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-039) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-038-inline-apm-callback-captured-result.md) · [Следующий →](Q-040-lost-update-two-task-run.md)
