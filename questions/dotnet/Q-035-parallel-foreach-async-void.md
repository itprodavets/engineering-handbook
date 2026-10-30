# Q-035 — Parallel.ForEach async void

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-034-semaphore-waitasync.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Parallel.ForEach async void

## Вопрос (RU)

Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован?

## Question (EN)

Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed?

## Code challenge / Фрагмент кода

```csharp
var gate = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Parallel.ForEach(new[] { 1, 2, 3 }, async _ =>
{
    await gate.Task;
    Console.Write("X");
});
Console.Write("A");
gate.SetResult();
// X могут появиться позже, а программа — завершиться.
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-035.cs](../../labs/dotnet/Q-035.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-035.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-035`. The workflow reports stdout in Job Summary.

**Expected / classification:** A печатается первой; X позже не гарантированы..

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Лямбда приводится к async void для Action<T>. Parallel.ForEach считает итерацию завершённой, когда делегат вернулся на await; оставшиеся continuations не дожидается. Используй Parallel.ForEachAsync или Task.WhenAll.

### EN — concise interview answer

The lambda becomes async void because Parallel.ForEach accepts Action<T>. The loop returns after delegates yield at await and does not await their continuations. Use Parallel.ForEachAsync or WhenAll.

</details>

## Why / Внутренний механизм

async void; Action<T>; compiler state machine; ThreadPool continuation.

**Risk / ошибка:** Утрата ожидания завершения, исключения вне обычной Task-цепочки, аварийное завершение процесса.

**Guarantee / недетерминированность:** A раньше X; дальнейший вывод недетерминирован без явного ожидания.

**Source:** https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-034-semaphore-waitasync.md)
