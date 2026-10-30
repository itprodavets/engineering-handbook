# Q-030 — Cancellation after start

[Русский](./Q-030-cancellation-after-start.md) · [English](en/Q-030-cancellation-after-start.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-030) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-029-lock-new-object.md) · [Следующий →](Q-031-asynclocal-flow.md)

## Вопрос

Выведет ли программа DONE, если отменить token после запуска делегата?

## Фрагмент C# — попробуйте предсказать результат

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

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-030.cs
```

[Q-030.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-030.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

DONE. Token у Task.Run может предотвратить запуск, но не останавливает уже выполняющийся делегат. Код не проверяет token, поэтому продолжает работу.

</details>

### Почему это работает

CancellationToken; Task.Run proxy; await continuation.

### Риск или ошибка

Ложная уверенность в принудительной отмене I/O/CPU работы.

### Что гарантировано

started завершён до Cancel; делегат уже начал выполнение.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.run](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.run)

---

[Русский](./Q-030-cancellation-after-start.md) · [English](en/Q-030-cancellation-after-start.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-030) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-029-lock-new-object.md) · [Следующий →](Q-031-asynclocal-flow.md)
