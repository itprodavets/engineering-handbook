# Q-032 — ConfigureAwait(false)

[Русский](./Q-032-configureawait-thread-id.md) · [English](en/Q-032-configureawait-thread-id.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-032) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-031-asynclocal-flow.md) · [Следующий →](Q-033-startnew-nested-task.md)

## Вопрос

Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int before = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(
    before == Environment.CurrentManagedThreadId);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-032.cs
```

[Q-032.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-032.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

True. Task уже завершена, поэтому метод не приостанавливается. ConfigureAwait(false) не запускает новый поток.

</details>

### Почему это работает

Task awaiter; IsCompleted; SynchronizationContext (захват не нужен).

### Риск или ошибка

Путаница между отключением возврата в контекст и переключением потока.

### Что гарантировано

Гарантировано для завершённой Task в приведённом коде.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Русский](./Q-032-configureawait-thread-id.md) · [English](en/Q-032-configureawait-thread-id.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-032) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-031-asynclocal-flow.md) · [Следующий →](Q-033-startnew-nested-task.md)
