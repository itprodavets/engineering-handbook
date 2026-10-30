# Q-020 — lock / async mutex

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-019-valuetask-consumption.md) · [Следующий →](Q-021-volatile-vs-interlocked.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Lock versus async semaphore

## Вопрос (RU)

Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?

## Question (EN)

Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Компилятор выдаёт CS1996: нельзя приостановить async-метод внутри lock. SemaphoreSlim.WaitAsync даёт ожидаемое без блокировки потока получение разрешения; Release обязателен, обычно в finally. SemaphoreSlim не обеспечивает автоматической рекурсивности.

### EN — concise interview answer

The compiler reports CS1996 for await inside lock. SemaphoreSlim.WaitAsync awaits a permit without blocking a worker; release it in finally. SemaphoreSlim is not automatically reentrant.

</details>

**Terminology / Термины:** lock; CS1996; SemaphoreSlim; WaitAsync; Release

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-019-valuetask-consumption.md) · [Следующий →](Q-021-volatile-vs-interlocked.md)
