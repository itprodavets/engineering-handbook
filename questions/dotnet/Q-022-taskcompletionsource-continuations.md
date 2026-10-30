# Q-022 — TaskCompletionSource / continuation

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-021-volatile-vs-interlocked.md) · [Следующий →](Q-023-asynclocal-executioncontext.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** TaskCompletionSource

## Вопрос (RU)

Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously?

## Question (EN)

Why can SetResult under a lock run unexpected code, and what does RunContinuationsAsynchronously change?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Продолжения Task могут выполняться синхронно при SetResult, включая код под удерживаемой вызывающим потоком блокировкой. TaskCreationOptions.RunContinuationsAsynchronously исключает синхронное встраивание продолжений, помогая уменьшить опасность lock inversion/reentrancy.

### EN — concise interview answer

Task continuations may run inline when SetResult completes the task, including while the caller holds a lock. RunContinuationsAsynchronously prevents inline execution of continuations and mitigates reentrancy or lock-inversion hazards.

</details>

**Terminology / Термины:** TaskCompletionSource; continuations; RunContinuationsAsynchronously

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-021-volatile-vs-interlocked.md) · [Следующий →](Q-023-asynclocal-executioncontext.md)
