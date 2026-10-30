# Q-027 — WhenAll exceptions

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-026-whenany-faulted-output.md) · [Следующий →](Q-028-lost-update-race.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** WhenAll exceptions

## Вопрос (RU)

Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task?

## Question (EN)

How many exceptions are stored by WhenAll when two input Tasks fault?

## Code challenge / Фрагмент кода

```csharp
var all = Task.WhenAll(
    Task.FromException(
        new InvalidOperationException("A")),
    Task.FromException(
        new ArgumentException("B")));
try
{
    await all;
}
catch (Exception)
{
    Console.WriteLine(all.Exception!.InnerExceptions.Count);
}
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-027.cs](../../labs/dotnet/Q-027.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-027.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-027`. The workflow reports stdout in Job Summary.

**Expected / classification:** 2.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

2. WhenAll агрегирует обе ошибки в своей Exception; обычный await сам выбрасывает одно исключение, а не весь AggregateException.

### EN — concise interview answer

2. WhenAll stores both failures in its aggregate Exception. A regular await rethrows one exception; inspect the Task for all failures.

</details>

## Why / Внутренний механизм

Task Exception property; AggregateException; awaiter GetResult.

**Risk / ошибка:** Потеря диагностики нескольких одновременных ошибок.

**Guarantee / недетерминированность:** Гарантировано две ошибки, порядок конкретных типов не нужен.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-026-whenany-faulted-output.md) · [Следующий →](Q-028-lost-update-race.md)
