# Q-067 — Canceled WaitAsync

[Русский](./Q-067-semaphore-canceled-wait-overrelease.md) · [English](en/Q-067-semaphore-canceled-wait-overrelease.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-067) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-066-semaphore-nested-async-deadlock.md) · [Следующий →](Q-068-static-semaphore-three-pods.md)

## Вопрос

Почему finally Release после отменённого WaitAsync может повредить счётчик?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
try { await sem.WaitAsync(ct); } finally { sem.Release(); }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-067.cs
```

[Q-67.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-067.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Отменённое ожидание не получило permit; finally нельзя освобождать чужой permit. wait должен быть до try/finally.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](./Q-067-semaphore-canceled-wait-overrelease.md) · [English](en/Q-067-semaphore-canceled-wait-overrelease.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-067) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-066-semaphore-nested-async-deadlock.md) · [Следующий →](Q-068-static-semaphore-three-pods.md)
