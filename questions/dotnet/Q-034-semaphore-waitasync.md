# Q-034 — Semaphore nonreentrant

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-033-startnew-nested-task.md) · [Следующий →](Q-035-parallel-foreach-async-void.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Semaphore nonreentrant

## Вопрос (RU)

Что напечатает second.IsCompleted после повторного WaitAsync без Release?

## Question (EN)

What does second.IsCompleted print after another WaitAsync without Release?

## Code challenge / Фрагмент кода

```csharp
using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();

Task second = semaphore.WaitAsync();
Console.WriteLine(second.IsCompleted);

semaphore.Release();
await second;
semaphore.Release();
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-034.cs](../../labs/dotnet/Q-034.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-034.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-034`. The workflow reports stdout in Job Summary.

**Expected / classification:** False.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

False. Первый Wait уменьшил счётчик с 1 до 0; второй ждёт разрешения. SemaphoreSlim не рекурсивный mutex: await второго до Release привёл бы к зависанию.

### EN — concise interview answer

False. The first Wait reduces the count to zero, so the second WaitAsync is pending. Awaiting the second before Release would deadlock this flow.

</details>

## Why / Внутренний механизм

SemaphoreSlim count, task waiter, asynchronous queue.

**Risk / ошибка:** Self-deadlock; лишний Release → SemaphoreFullException при maxCount=1.

**Guarantee / недетерминированность:** False до Release при одиночном владении семафором.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-033-startnew-nested-task.md) · [Следующий →](Q-035-parallel-foreach-async-void.md)
