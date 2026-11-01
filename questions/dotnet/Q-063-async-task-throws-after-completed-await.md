# Q-063 — Async exception capture

[Русский](./Q-063-async-task-throws-after-completed-await.md) · [English](en/Q-063-async-task-throws-after-completed-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-063) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-062-async-task-oce-builder-canceled.md)

## Вопрос

Выбрасывает ли TestAsync() синхронно InvalidOperationException, если внутри await Task.CompletedTask затем throw?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
static async Task F(){await Task.CompletedTask;throw new InvalidOperationException();}
Task task=F(); // Faulted Task, no direct throw
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-063.cs
```

[Q-063.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-063.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. async Task state machine перехватывает исключение и возвращает Faulted Task. CompletedTask уже готова, но это не меняет способ передачи ошибки; `await task` выбрасывает InvalidOperationException.

</details>

### Документация и исходники

[https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)

---

[Русский](./Q-063-async-task-throws-after-completed-await.md) · [English](en/Q-063-async-task-throws-after-completed-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-063) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-062-async-task-oce-builder-canceled.md)
