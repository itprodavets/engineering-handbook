# Q-065 — Semaphore permits

[Русский](./Q-065-semaphore-permits-vs-threads.md) · [English](en/Q-065-semaphore-permits-vs-threads.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-065) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-064-monitor-exit-after-await.md) · [Следующий →](Q-066-semaphore-nested-async-deadlock.md)

## Вопрос

Что означает SemaphoreSlim(2,2) при двух Task.Delay и ожидании ещё двух задач?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
await sem.WaitAsync();
try { await Task.Delay(1000); } finally { sem.Release(); }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-65.cs
```

[Q-65.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-65.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Два permit заняты до Release, но dedicated workers не требуются; следующие WaitAsync ожидают асинхронно.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](./Q-065-semaphore-permits-vs-threads.md) · [English](en/Q-065-semaphore-permits-vs-threads.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-065) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-064-monitor-exit-after-await.md) · [Следующий →](Q-066-semaphore-nested-async-deadlock.md)
