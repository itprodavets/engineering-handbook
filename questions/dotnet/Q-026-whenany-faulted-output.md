# Q-026 — WhenAny faulted

[Русский](./Q-026-whenany-faulted-output.md) · [English](en/Q-026-whenany-faulted-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-026) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-025-incomplete-await-output.md) · [Следующий →](Q-027-whenall-exceptions-count.md)

## Вопрос

Что напечатает код и выбросит ли await Task.WhenAny исключение?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
var failed = Task.FromException(
    new InvalidOperationException("boom"));
var winner = await Task.WhenAny(
    failed, Task.Delay(Timeout.Infinite));
Console.WriteLine(winner.IsFaulted);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-026.cs
```

[Q-026.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-026.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

True. WhenAny возвращает завершившуюся Task независимо от Faulted; ошибка станет видна при await winner.

</details>

### Почему это работает

Task<Task>; статус Faulted у winner, RanToCompletion у WhenAny.

### Риск или ошибка

Исключение ошибочно считают обработанным; оставшиеся операции не отменяются автоматически.

### Что гарантировано

Гарантировано: вторая Task никогда не завершается.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany)

---

[Русский](./Q-026-whenany-faulted-output.md) · [English](en/Q-026-whenany-faulted-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-026) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-025-incomplete-await-output.md) · [Следующий →](Q-027-whenall-exceptions-count.md)
