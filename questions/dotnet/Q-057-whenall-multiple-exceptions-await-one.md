# Q-057 — WhenAll exceptions

[Русский](./Q-057-whenall-multiple-exceptions-await-one.md) · [English](en/Q-057-whenall-multiple-exceptions-await-one.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-057) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-056-whenany-faulted-winner-exception.md) · [Следующий →](Q-058-whenall-faulted-priority-over-canceled.md)

## Вопрос

Сколько исключений в combined.Exception.InnerExceptions при двух Task.FromException и что выбросит await combined?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task combined=Task.WhenAll(first,second);
try { await combined; } catch { var all=combined.Exception!.InnerExceptions; }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-057.cs
```

[Q-057.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-057.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Два InnerExceptions для двух одиночных ошибок. await combined распространяет одно из сохранённых исключений, не обязательно AggregateException; остальные доступны через combined.Exception.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](./Q-057-whenall-multiple-exceptions-await-one.md) · [English](en/Q-057-whenall-multiple-exceptions-await-one.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-057) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-056-whenany-faulted-winner-exception.md) · [Следующий →](Q-058-whenall-faulted-priority-over-canceled.md)
