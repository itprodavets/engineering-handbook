# Q-030 — Cancellation after start

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-029-lock-new-object.md) · [Следующий →](Q-031-asynclocal-flow.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Cancellation after start

## Вопрос (RU)

Выведет ли программа DONE, если отменить token после запуска делегата?

## Question (EN)

Will the program print DONE when the token is canceled after the delegate starts?

## Code challenge / Фрагмент кода

```csharp
using var cts = new CancellationTokenSource();
var started = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
var release = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

var task = Task.Run(async () =>
{
    started.SetResult();
    await release.Task;
    Console.Write("DONE");
}, cts.Token);

await started.Task;
cts.Cancel();
release.SetResult();
await task;
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-030.cs](../../labs/dotnet/Q-030.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-030.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-030`. The workflow reports stdout in Job Summary.

**Expected / classification:** DONE.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

DONE. Token у Task.Run может предотвратить запуск, но не останавливает уже выполняющийся делегат. Код не проверяет token, поэтому продолжает работу.

### EN — concise interview answer

DONE. Task.Run's token can prevent the delegate from starting, but cannot forcibly stop it after execution has begun. The body never checks the token.

</details>

## Why / Внутренний механизм

CancellationToken; Task.Run proxy; await continuation.

**Risk / ошибка:** Ложная уверенность в принудительной отмене I/O/CPU работы.

**Guarantee / недетерминированность:** started завершён до Cancel; делегат уже начал выполнение.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.run

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-029-lock-new-object.md) · [Следующий →](Q-031-asynclocal-flow.md)
