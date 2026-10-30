# Q-025 — Incomplete await gate

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-024-completed-await-output.md) · [Следующий →](Q-026-whenany-faulted-output.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Incomplete await gate

## Вопрос (RU)

Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource.

## Question (EN)

What is the output? The method awaits an incomplete TaskCompletionSource.

## Code challenge / Фрагмент кода

```csharp
var gate = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

async Task PrintAsync()
{
    Console.Write("A");
    await gate.Task;
    Console.Write("B");
}
var task = PrintAsync();
Console.Write("C");
gate.SetResult();
await task;
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-025.cs](../../labs/dotnet/Q-025.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-025.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-025`. The workflow reports stdout in Job Summary.

**Expected / classification:** ACB.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ACB. Метод печатает A, приостанавливается на незавершённом await; вызывающий код печатает C, затем SetResult разрешает продолжение с B.

### EN — concise interview answer

ACB. The method prints A and suspends; the caller prints C, then SetResult allows the continuation to print B.

</details>

## Why / Внутренний механизм

Async state machine; continuation; RunContinuationsAsynchronously; нет thread-per-wait.

**Risk / ошибка:** Не путать приостановку метода с остановкой/созданием worker thread.

**Guarantee / недетерминированность:** Порядок A→C→B задан незавершённой gate и последовательностью вызовов.

**Source:** https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-024-completed-await-output.md) · [Следующий →](Q-026-whenany-faulted-output.md)
