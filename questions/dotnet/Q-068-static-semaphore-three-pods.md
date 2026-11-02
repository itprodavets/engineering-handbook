# Q-068 — Kubernetes Pod

[Русский](./Q-068-static-semaphore-three-pods.md) · [English](en/Q-068-static-semaphore-three-pods.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-068) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-067-semaphore-canceled-wait-overrelease.md) · [Следующий →](Q-069-network-await-permit-lifetime.md)

## Вопрос

Защитит ли static SemaphoreSlim(1,1) последний SKU от трёх Pod?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
private static readonly SemaphoreSlim Gate=new(1,1);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-068.cs
```

[Q-068.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-068.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет: каждый Pod имеет собственное разрешение; защищать SKU нужно в InventoryService/PostgreSQL.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](./Q-068-static-semaphore-three-pods.md) · [English](en/Q-068-static-semaphore-three-pods.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-068) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-067-semaphore-canceled-wait-overrelease.md) · [Следующий →](Q-069-network-await-permit-lifetime.md)
