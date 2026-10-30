# Q-033 — StartNew nested Task

[Русский](./Q-033-startnew-nested-task.md) · [English](en/Q-033-startnew-nested-task.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-033) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-032-configureawait-thread-id.md) · [Следующий →](Q-034-semaphore-waitasync.md)

## Вопрос

Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task<Task> outer = Task.Factory.StartNew<Task>(
    async () => await Task.Delay(100));

Task inner = await outer;
// Завершён ли inner здесь — не гарантировано.
await inner;
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-033.cs
```

[Q-033.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-033.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

StartNew с Func<Task> возвращает Task<Task>. await outer даёт inner, но не гарантирует её завершение; нужен await inner или outer.Unwrap().

</details>

### Почему это работает

Generic Task<TResult>; nested await; compiler async lambda.

### Риск или ошибка

Преждевременное завершение операции и потеря исключений внутренней задачи.

### Что гарантировано

Тип Task<Task> гарантирован; завершённость inner после outer зависит от времени.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap)

---

[Русский](./Q-033-startnew-nested-task.md) · [English](en/Q-033-startnew-nested-task.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-033) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-032-configureawait-thread-id.md) · [Следующий →](Q-034-semaphore-waitasync.md)
