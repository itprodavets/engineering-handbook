# Q-023 — AsyncLocal / ExecutionContext

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-022-taskcompletionsource-continuations.md) · [Следующий →](Q-024-completed-await-output.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ExecutionContext

## Вопрос (RU)

Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет?

## Question (EN)

Why does AsyncLocal<T> flow through Task.Run to another thread while ThreadStatic does not?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

AsyncLocal<T> хранится в логическом ExecutionContext, который по умолчанию распространяется через асинхронные переходы и Task.Run. ThreadStatic привязан к конкретному потоку ОС/CLR, поэтому при смене потока значение не переносится.

### EN — concise interview answer

AsyncLocal<T> belongs to the logical ExecutionContext, which normally flows through async work and Task.Run. ThreadStatic is tied to a specific physical thread and does not follow thread changes.

</details>

**Terminology / Термины:** AsyncLocal; ThreadStatic; ExecutionContext; context flow

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-022-taskcompletionsource-continuations.md) · [Следующий →](Q-024-completed-await-output.md)
