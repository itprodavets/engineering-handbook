# Q-062 — AsyncTaskMethodBuilder

[Русский](./Q-062-async-task-oce-builder-canceled.md) · [English](en/Q-062-async-task-oce-builder-canceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-062) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-061-fromexception-oce-vs-fromcanceled.md) · [Следующий →](Q-063-async-task-throws-after-completed-await.md)

## Вопрос

Почему async Task с throw OperationCanceledException получает Canceled, а Task.FromException(OCE) — Faulted?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
static async Task F(){await Task.Yield();throw new OperationCanceledException();}
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-062.cs
```

[Q-062.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-062.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

AsyncTaskMethodBuilder.SetException видит OperationCanceledException и применяет TrySetCanceled(token,oсe). Task.Yield только даёт continuation, не создаёт отмену. Task.FromException принудительно Faulted.

</details>

### Документация и исходники

[https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)

---

[Русский](./Q-062-async-task-oce-builder-canceled.md) · [English](en/Q-062-async-task-oce-builder-canceled.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-062) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-061-fromexception-oce-vs-fromcanceled.md) · [Следующий →](Q-063-async-task-throws-after-completed-await.md)
