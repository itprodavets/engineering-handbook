# Q-002 — Async / потоки

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-001-async-io-scalability.md) · [Следующий →](Q-003-what-is-io.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Async / threads

## Вопрос (RU)

Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await новый поток?

## Question (EN)

Must Environment.CurrentManagedThreadId be the same before and after await ToListAsync()? If not, did await create a new thread?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Нет. В ASP.NET Core продолжение после await может выполняться на другом ThreadPool-потоке. await сам по себе не создаёт поток и не гарантирует переключение; завершённая операция может продолжиться синхронно.

### EN — concise interview answer

No. In ASP.NET Core, the continuation may execute on a different ThreadPool thread. await neither creates a thread nor guarantees a thread switch; an already completed task may continue synchronously.

</details>

**Terminology / Термины:** Continuation; ThreadPool; SynchronizationContext

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-001-async-io-scalability.md) · [Следующий →](Q-003-what-is-io.md)
