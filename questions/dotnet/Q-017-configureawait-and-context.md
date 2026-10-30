# Q-017 — ConfigureAwait / contexts

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-016-sync-over-async-deadlocks.md) · [Следующий →](Q-018-cancellationtoken-taskrun.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ConfigureAwait

## Вопрос (RU)

Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext?

## Question (EN)

What exactly does ConfigureAwait(false) change? Does it suppress ExecutionContext?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Для обычного Task-await он отключает возврат continuation в захваченный SynchronizationContext/нестандартный TaskScheduler. Он не создаёт поток и не отключает распространение ExecutionContext или AsyncLocal.

### EN — concise interview answer

For standard Task awaiting it avoids capturing SynchronizationContext or a non-default TaskScheduler for the continuation. It neither creates a thread nor suppresses ExecutionContext or AsyncLocal flow.

</details>

**Terminology / Термины:** ConfigureAwait; SynchronizationContext; ExecutionContext; AsyncLocal

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-016-sync-over-async-deadlocks.md) · [Следующий →](Q-018-cancellationtoken-taskrun.md)
