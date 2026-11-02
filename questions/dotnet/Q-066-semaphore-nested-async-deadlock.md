# Q-066 — Async deadlock

[Русский](./Q-066-semaphore-nested-async-deadlock.md) · [English](en/Q-066-semaphore-nested-async-deadlock.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-066) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-065-semaphore-permits-vs-threads.md) · [Следующий →](Q-067-semaphore-canceled-wait-overrelease.md)

## Вопрос

Что будет, если Outer держит SemaphoreSlim(1,1) и await Inner, который тоже ждёт его?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
await gate.WaitAsync();
try { await InnerAsync(); } finally { gate.Release(); }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-066.cs
```

[Q-066.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-066.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Только Outer entered; Inner не может получить permit, Outer не отпускает его до Inner. Async deadlock не требует блокировки ThreadPool.

</details>

### Документация и исходники

[https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/](https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/)

---

[Русский](./Q-066-semaphore-nested-async-deadlock.md) · [English](en/Q-066-semaphore-nested-async-deadlock.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-066) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-065-semaphore-permits-vs-threads.md) · [Следующий →](Q-067-semaphore-canceled-wait-overrelease.md)
