# Q-033 — StartNew nested Task

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-032-configureawait-thread-id.md) · [Следующий →](Q-034-semaphore-waitasync.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** StartNew nested Task

## Вопрос (RU)

Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции?

## Question (EN)

What is the task type, and does awaiting outer once wait for the inner async operation?

## Code challenge / Фрагмент кода

```csharp
Task<Task> outer = Task.Factory.StartNew<Task>(
    async () => await Task.Delay(100));

Task inner = await outer;
// Завершён ли inner здесь — не гарантировано.
await inner;
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-033.cs](../../labs/dotnet/Q-033.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-033.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-033`. The workflow reports stdout in Job Summary.

**Expected / classification:** Task<Task>; первый await ждёт только outer..

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

StartNew с Func<Task> возвращает Task<Task>. await outer даёт inner, но не гарантирует её завершение; нужен await inner или outer.Unwrap().

### EN — concise interview answer

StartNew(Func<Task>) yields Task<Task>. Awaiting the outer task returns the inner task and does not guarantee its completion. Await inner or use Unwrap().

</details>

## Why / Внутренний механизм

Generic Task<TResult>; nested await; compiler async lambda.

**Risk / ошибка:** Преждевременное завершение операции и потеря исключений внутренней задачи.

**Guarantee / недетерминированность:** Тип Task<Task> гарантирован; завершённость inner после outer зависит от времени.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-032-configureawait-thread-id.md) · [Следующий →](Q-034-semaphore-waitasync.md)
