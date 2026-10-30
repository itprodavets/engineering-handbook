# Q-031 — AsyncLocal flow

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-030-cancellation-after-start.md) · [Следующий →](Q-032-configureawait-thread-id.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** AsyncLocal flow

## Вопрос (RU)

Что напечатает Task.Run — X или null?

## Question (EN)

Does Task.Run print X or null?

## Code challenge / Фрагмент кода

```csharp
var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() =>
{
    Console.Write(trace.Value);
});
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-031.cs](../../labs/dotnet/Q-031.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-031.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-031`. The workflow reports stdout in Job Summary.

**Expected / classification:** X.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

X. ExecutionContext захватывается при планировании работы в ThreadPool, и AsyncLocal распространяется через него, независимо от конкретного worker.

### EN — concise interview answer

X. ExecutionContext normally flows into Task.Run, carrying AsyncLocal values across worker threads.

</details>

## Why / Внутренний механизм

ExecutionContext; AsyncLocal logical context flow.

**Risk / ошибка:** Контекст может незаметно переносить данные; ThreadStatic ведёт себя иначе.

**Guarantee / недетерминированность:** При стандартном ExecutionContext flow без SuppressFlow — X.

**Source:** https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-030-cancellation-after-start.md) · [Следующий →](Q-032-configureawait-thread-id.md)
