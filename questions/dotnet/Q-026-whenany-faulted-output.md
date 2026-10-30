# Q-026 — WhenAny faulted

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-025-incomplete-await-output.md) · [Следующий →](Q-027-whenall-exceptions-count.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** WhenAny faulted

## Вопрос (RU)

Что напечатает код и выбросит ли await Task.WhenAny исключение?

## Question (EN)

What does it print, and does awaiting WhenAny throw the winning task's exception?

## Code challenge / Фрагмент кода

```csharp
var failed = Task.FromException(
    new InvalidOperationException("boom"));
var winner = await Task.WhenAny(
    failed, Task.Delay(Timeout.Infinite));
Console.WriteLine(winner.IsFaulted);
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-026.cs](../../labs/dotnet/Q-026.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-026.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-026`. The workflow reports stdout in Job Summary.

**Expected / classification:** True; исключение не выбрасывается на этом await..

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

True. WhenAny возвращает завершившуюся Task независимо от Faulted; ошибка станет видна при await winner.

### EN — concise interview answer

True. WhenAny completes with the faulted winner but does not throw its exception; awaiting winner would rethrow it.

</details>

## Why / Внутренний механизм

Task<Task>; статус Faulted у winner, RanToCompletion у WhenAny.

**Risk / ошибка:** Исключение ошибочно считают обработанным; оставшиеся операции не отменяются автоматически.

**Guarantee / недетерминированность:** Гарантировано: вторая Task никогда не завершается.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-025-incomplete-await-output.md) · [Следующий →](Q-027-whenall-exceptions-count.md)
