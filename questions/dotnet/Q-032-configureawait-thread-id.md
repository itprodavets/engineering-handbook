# Q-032 — ConfigureAwait(false)

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-031-asynclocal-flow.md) · [Следующий →](Q-033-startnew-nested-task.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ConfigureAwait(false)

## Вопрос (RU)

Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)?

## Question (EN)

Does awaiting CompletedTask.ConfigureAwait(false) change the managed thread ID?

## Code challenge / Фрагмент кода

```csharp
int before = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(
    before == Environment.CurrentManagedThreadId);
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-032.cs](../../labs/dotnet/Q-032.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-032.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-032`. The workflow reports stdout in Job Summary.

**Expected / classification:** True.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

True. Task уже завершена, поэтому метод не приостанавливается. ConfigureAwait(false) не запускает новый поток.

### EN — concise interview answer

True. The Task is already completed, so the await continues synchronously. ConfigureAwait(false) does not force a thread switch.

</details>

## Why / Внутренний механизм

Task awaiter; IsCompleted; SynchronizationContext (захват не нужен).

**Risk / ошибка:** Путаница между отключением возврата в контекст и переключением потока.

**Guarantee / недетерминированность:** Гарантировано для завершённой Task в приведённом коде.

**Source:** https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-031-asynclocal-flow.md) · [Следующий →](Q-033-startnew-nested-task.md)
