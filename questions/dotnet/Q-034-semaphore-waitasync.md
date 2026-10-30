# Q-034 — Semaphore nonreentrant

[Русский](./Q-034-semaphore-waitasync.md) · [English](en/Q-034-semaphore-waitasync.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-034) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-033-startnew-nested-task.md) · [Следующий →](Q-035-parallel-foreach-async-void.md)

## Вопрос

Что напечатает second.IsCompleted после повторного WaitAsync без Release?

## Фрагмент C# — попробуйте предсказать результат

```csharp
using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();

Task second = semaphore.WaitAsync();
Console.WriteLine(second.IsCompleted);

semaphore.Release();
await second;
semaphore.Release();
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-034.cs
```

[Q-034.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-034.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

False. Первый Wait уменьшил счётчик с 1 до 0; второй ждёт разрешения. SemaphoreSlim не рекурсивный mutex: await второго до Release привёл бы к зависанию.

</details>

### Почему это работает

SemaphoreSlim count, task waiter, asynchronous queue.

### Риск или ошибка

Self-deadlock; лишний Release → SemaphoreFullException при maxCount=1.

### Что гарантировано

False до Release при одиночном владении семафором.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](./Q-034-semaphore-waitasync.md) · [English](en/Q-034-semaphore-waitasync.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-034) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-033-startnew-nested-task.md) · [Следующий →](Q-035-parallel-foreach-async-void.md)
