# Q-064 — Monitor ownership

[Русский](./Q-064-monitor-exit-after-await.md) · [English](en/Q-064-monitor-exit-after-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-064) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-063-async-task-throws-after-completed-await.md) · [Следующий →](Q-065-semaphore-permits-vs-threads.md)

## Вопрос

Почему Monitor.Exit после await на другом потоке выбросит исключение?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Monitor.Enter(gate);
try { await Task.Delay(100); } finally { Monitor.Exit(gate); }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-64.cs
```

[Q-64.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-64.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Monitor имеет thread affinity; Exit с другого потока выбросит SynchronizationLockException. await не освобождает монитор.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit)

---

[Русский](./Q-064-monitor-exit-after-await.md) · [English](en/Q-064-monitor-exit-after-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-064) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-063-async-task-throws-after-completed-await.md) · [Следующий →](Q-065-semaphore-permits-vs-threads.md)
