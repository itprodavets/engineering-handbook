# Q-061 — Task status vs exception

[Русский](./Q-061-fromexception-oce-vs-fromcanceled.md) · [English](en/Q-061-fromexception-oce-vs-fromcanceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-061) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-060-whenall-waits-not-fail-fast.md) · [Следующий →](Q-062-async-task-oce-builder-canceled.md)

## Вопрос

Почему Task.FromException(new OperationCanceledException()) имеет Faulted, а Task.FromCanceled(token) имеет Canceled?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task a=Task.FromException(new OperationCanceledException());
Task b=Task.FromCanceled(new CancellationToken(true));
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-061.cs
```

[Q-061.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-061.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

FromException всегда создаёт Task со статусом Faulted независимо от типа exception. FromCanceled при уже отменённом token создаёт Canceled. Тип OCE не универсально определяет Task.Status.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0)

---

[Русский](./Q-061-fromexception-oce-vs-fromcanceled.md) · [English](en/Q-061-fromexception-oce-vs-fromcanceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-061) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-060-whenall-waits-not-fail-fast.md) · [Следующий →](Q-062-async-task-oce-builder-canceled.md)
