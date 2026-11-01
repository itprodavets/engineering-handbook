# Q-058 — WhenAll precedence

[Русский](./Q-058-whenall-faulted-priority-over-canceled.md) · [English](en/Q-058-whenall-faulted-priority-over-canceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-058) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-057-whenall-multiple-exceptions-await-one.md) · [Следующий →](Q-059-whenany-does-not-cancel-loser.md)

## Вопрос

Какой статус имеет WhenAll(Faulted,Canceled) и какое исключение распространяет await?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task combined=Task.WhenAll(Task.FromException(new InvalidOperationException()),Task.FromCanceled(new CancellationToken(true)));
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-058.cs
```

[Q-058.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-058.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Faulted имеет приоритет над Canceled. await передаёт fault-исключение, отменённая входящая Task сохраняет статус Canceled и не становится отдельной ошибкой в агрегате.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](./Q-058-whenall-faulted-priority-over-canceled.md) · [English](en/Q-058-whenall-faulted-priority-over-canceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-058) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-057-whenall-multiple-exceptions-await-one.md) · [Следующий →](Q-059-whenany-does-not-cancel-loser.md)
