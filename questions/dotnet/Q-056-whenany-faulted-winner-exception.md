# Q-056 — WhenAny faults

[Русский](./Q-056-whenany-faulted-winner-exception.md) · [English](en/Q-056-whenany-faulted-winner-exception.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-056) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-055-whenany-winner-vs-continuation-time.md) · [Следующий →](Q-057-whenall-multiple-exceptions-await-one.md)

## Вопрос

Выбросит ли await Task.WhenAny исключение из Faulted Task-победителя? Что меняет await completed?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task completed=await Task.WhenAny(failed,Task.Delay(100));
await completed; // propagates winner's exception
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-056.cs
```

[Q-056.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-056.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Внешняя Task<Task> завершается успешно и выдаёт победителя. Для распространения Faulted исключения необходим `await completed` или явная обработка статуса/Exception.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](./Q-056-whenany-faulted-winner-exception.md) · [English](en/Q-056-whenany-faulted-winner-exception.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-056) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-055-whenany-winner-vs-continuation-time.md) · [Следующий →](Q-057-whenall-multiple-exceptions-await-one.md)
