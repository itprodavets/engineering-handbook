# Q-059 — WhenAny losers

[Русский](./Q-059-whenany-does-not-cancel-loser.md) · [English](en/Q-059-whenany-does-not-cancel-loser.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-059) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-058-whenall-faulted-priority-over-canceled.md) · [Следующий →](Q-060-whenall-waits-not-fail-fast.md)

## Вопрос

Отменяет ли Task.WhenAny проигравшие Task и как они завершаются?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task winner=await Task.WhenAny(producer,Task.Delay(100));
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-059.cs
```

[Q-059.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-059.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет, проигравшие продолжают выполнять работу. Timeout является решением вызывающего, не автоматической отменой. Нужны кооперативный токен/cleanup и наблюдение ошибок проигравшего.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](./Q-059-whenany-does-not-cancel-loser.md) · [English](en/Q-059-whenany-does-not-cancel-loser.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-059) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-058-whenall-faulted-priority-over-canceled.md) · [Следующий →](Q-060-whenall-waits-not-fail-fast.md)
