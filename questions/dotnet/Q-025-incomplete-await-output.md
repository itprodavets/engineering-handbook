# Q-025 — Incomplete await gate

[Русский](./Q-025-incomplete-await-output.md) · [English](en/Q-025-incomplete-await-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-025) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-024-completed-await-output.md) · [Следующий →](Q-026-whenany-faulted-output.md)

## Вопрос

Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource.

## Фрагмент .NET / C# — попробуйте предсказать результат

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

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-025.cs
```

[Q-025.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-025.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ACB. Метод печатает A, приостанавливается на незавершённом await; вызывающий код печатает C, затем SetResult разрешает продолжение с B.

</details>

### Почему это работает

Async state machine; continuation; RunContinuationsAsynchronously; нет thread-per-wait.

### Риск или ошибка

Не путать приостановку метода с остановкой/созданием worker thread.

### Что гарантировано

Порядок A→C→B задан незавершённой gate и последовательностью вызовов.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Русский](./Q-025-incomplete-await-output.md) · [English](en/Q-025-incomplete-await-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-025) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-024-completed-await-output.md) · [Следующий →](Q-026-whenany-faulted-output.md)
