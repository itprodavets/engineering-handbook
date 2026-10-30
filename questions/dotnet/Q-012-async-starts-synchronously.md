# Q-012 — Async / first await

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-011-threadpool-worker-creation.md) · [Следующий →](Q-013-completed-await-and-scheduling.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Async execution

## Вопрос (RU)

Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?

## Question (EN)

Does calling an async Task method start a new thread or run synchronously at first?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Вызов начинает исполнять тело на текущем потоке до первого await незавершённой операции. Компилятор генерирует state machine, но async не означает запуск в ThreadPool.

### EN — concise interview answer

It executes on the calling thread until the first await of an incomplete awaitable. The compiler generates a state machine; async alone does not queue work to the ThreadPool.

</details>

**Terminology / Термины:** async; state machine; await; initial synchronous path

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-011-threadpool-worker-creation.md) · [Следующий →](Q-013-completed-await-and-scheduling.md)
