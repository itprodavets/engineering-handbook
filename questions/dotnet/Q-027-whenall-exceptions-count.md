# Q-027 — WhenAll exceptions

[Русский](./Q-027-whenall-exceptions-count.md) · [English](en/Q-027-whenall-exceptions-count.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-027) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-026-whenany-faulted-output.md) · [Следующий →](Q-028-lost-update-race.md)

## Вопрос

Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task?

## Фрагмент C# — попробуйте предсказать результат

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

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-027.cs
```

[Q-027.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-027.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

2. WhenAll агрегирует обе ошибки в своей Exception; обычный await сам выбрасывает одно исключение, а не весь AggregateException.

</details>

### Почему это работает

Task Exception property; AggregateException; awaiter GetResult.

### Риск или ошибка

Потеря диагностики нескольких одновременных ошибок.

### Что гарантировано

Гарантировано две ошибки, порядок конкретных типов не нужен.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)

---

[Русский](./Q-027-whenall-exceptions-count.md) · [English](en/Q-027-whenall-exceptions-count.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-027) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-026-whenany-faulted-output.md) · [Следующий →](Q-028-lost-update-race.md)
