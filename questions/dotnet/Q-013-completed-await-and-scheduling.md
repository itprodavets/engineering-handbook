# Q-013 — Await / completed task

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-012-async-starts-synchronously.md) · [Следующий →](Q-014-whenany-faulted-task.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Await completion

## Вопрос (RU)

Всегда ли await приостанавливает метод, выделяет worker или переключает поток?

## Question (EN)

Does await always suspend, allocate a worker, or switch threads?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Нет. Для уже завершённого awaitable GetAwaiter().IsCompleted позволяет продолжить выполнение синхронно. Незавершённый await регистрирует continuation; новый поток при этом не создаётся самим await.

### EN — concise interview answer

No. An already completed awaitable continues synchronously. An incomplete await registers a continuation and suspends the method; await itself does not create a thread.

</details>

**Terminology / Термины:** awaiter; IsCompleted; continuation; thread identity

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-012-async-starts-synchronously.md) · [Следующий →](Q-014-whenany-faulted-task.md)
