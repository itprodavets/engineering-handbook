# Q-001 — Async / I/O

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [Следующий →](Q-002-thread-id-after-await.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Async / I/O

## Вопрос (RU)

Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?

## Question (EN)

Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ToListAsync() использует асинхронный I/O: при незавершённом чтении await сохраняет продолжение и освобождает рабочий поток. Task.Run() отправляет синхронный ToList() в ThreadPool, где поток блокируется при ожидании БД; возможен ThreadPool starvation.

### EN — concise interview answer

ToListAsync() uses asynchronous I/O: when data is not ready, await suspends the method and releases the worker. Task.Run() queues synchronous I/O onto the ThreadPool, keeping a worker blocked and increasing the risk of thread pool starvation.

</details>

**Terminology / Термины:** await; Task.Run; ThreadPool; I/O; starvation

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [Следующий →](Q-002-thread-id-after-await.md)
