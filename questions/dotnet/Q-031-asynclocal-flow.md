# Q-031 — AsyncLocal flow

[Русский](./Q-031-asynclocal-flow.md) · [English](en/Q-031-asynclocal-flow.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-031) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-030-cancellation-after-start.md) · [Следующий →](Q-032-configureawait-thread-id.md)

## Вопрос

Что напечатает Task.Run — X или null?

## Фрагмент C# — попробуйте предсказать результат

```csharp
var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() =>
{
    Console.Write(trace.Value);
});
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-031.cs
```

[Q-031.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-031.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

X. ExecutionContext захватывается при планировании работы в ThreadPool, и AsyncLocal распространяется через него, независимо от конкретного worker.

</details>

### Почему это работает

ExecutionContext; AsyncLocal logical context flow.

### Риск или ошибка

Контекст может незаметно переносить данные; ThreadStatic ведёт себя иначе.

### Что гарантировано

При стандартном ExecutionContext flow без SuppressFlow — X.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[Русский](./Q-031-asynclocal-flow.md) · [English](en/Q-031-asynclocal-flow.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-031) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-030-cancellation-after-start.md) · [Следующий →](Q-032-configureawait-thread-id.md)
