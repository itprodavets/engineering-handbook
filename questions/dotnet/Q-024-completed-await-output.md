# Q-024 — Completed await

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-023-asynclocal-executioncontext.md) · [Следующий →](Q-025-incomplete-await-output.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Completed await

## Вопрос (RU)

Какой вывод и почему? async-метод содержит await уже завершённой Task.

## Question (EN)

What is the output and why? The awaited Task is already complete.

## Code challenge / Фрагмент кода

```csharp
async Task PrintAsync()
{
    Console.Write("A");
    await Task.CompletedTask;
    Console.Write("B");
}
var task = PrintAsync();
Console.Write("C");
await task;
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-024.cs](../../labs/dotnet/Q-024.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-024`. The workflow reports stdout in Job Summary.

**Expected / classification:** ABC.

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ABC. CompletedTask уже завершена, поэтому await не приостанавливает метод и B печатается до возврата в вызывающий код.

### EN — concise interview answer

ABC. The awaited Task is already complete, so the method continues synchronously and prints B before the caller prints C.

</details>

## Why / Внутренний механизм

Roslyn state machine; IsCompleted = true; без обязательного ThreadPool worker.

**Risk / ошибка:** Нельзя считать, что каждый async-вызов запускается в фоне или переключает поток.

**Guarantee / недетерминированность:** Гарантировано для уже завершённой Task.

**Source:** https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-023-asynclocal-executioncontext.md) · [Следующий →](Q-025-incomplete-await-output.md)
