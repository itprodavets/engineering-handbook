# Q-035 — Parallel.ForEach async void

[Русский](./Q-035-parallel-foreach-async-void.md) · [English](en/Q-035-parallel-foreach-async-void.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-035) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-034-semaphore-waitasync.md)

## Вопрос

Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован?

## Фрагмент .NET / C# — попробуйте предсказать результат

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

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-035.cs
```

[Q-035.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-035.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Лямбда приводится к async void для Action<T>. Parallel.ForEach считает итерацию завершённой, когда делегат вернулся на await; оставшиеся continuations не дожидается. Используй Parallel.ForEachAsync или Task.WhenAll.

</details>

### Почему это работает

async void; Action<T>; compiler state machine; ThreadPool continuation.

### Риск или ошибка

Утрата ожидания завершения, исключения вне обычной Task-цепочки, аварийное завершение процесса.

### Что гарантировано

A раньше X; дальнейший вывод недетерминирован без явного ожидания.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs)

---

[Русский](./Q-035-parallel-foreach-async-void.md) · [English](en/Q-035-parallel-foreach-async-void.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-035) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-034-semaphore-waitasync.md)
