# Q-055 — WhenAny timing

[Русский](./Q-055-whenany-winner-vs-continuation-time.md) · [English](en/Q-055-whenany-winner-vs-continuation-time.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-055) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-054-task-delay-is-not-synchronization.md) · [Следующий →](Q-056-whenany-faulted-winner-exception.md)

## Вопрос

Если Task.Delay выиграла WhenAny, обязательно ли Producer остаётся незавершённым к моменту продолжения?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task winner=await Task.WhenAny(producer,Task.Delay(100));
// winner == timeout does not prove producer still pending now
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-055.cs
```

[Q-055.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-055.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Победитель — первая завершившаяся Task, но проигравший может успеть завершиться до исполнения кода после await. Проверяй идентичность победителя; таймер не отменяет Producer.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](./Q-055-whenany-winner-vs-continuation-time.md) · [English](en/Q-055-whenany-winner-vs-continuation-time.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-055) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-054-task-delay-is-not-synchronization.md) · [Следующий →](Q-056-whenany-faulted-winner-exception.md)
