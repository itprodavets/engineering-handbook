# Q-069 — Async I/O

[Русский](./Q-069-network-await-permit-lifetime.md) · [English](en/Q-069-network-await-permit-lifetime.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-069) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-068-static-semaphore-three-pods.md) · [Следующий →](Q-070-three-pods-provider-quota.md)

## Вопрос

Что удерживает CheckoutAsync во время 5-секундного await ChargeAsync: worker или permit?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
await gate.WaitAsync();
try { await ChargeAsync(); } finally { gate.Release(); }
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-069.cs
```

[Q-069.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-069.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

При корректном pending async I/O worker не закреплён, а permit Gate остаётся занятым до finally Release.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](./Q-069-network-await-permit-lifetime.md) · [English](en/Q-069-network-await-permit-lifetime.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-069) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-068-static-semaphore-three-pods.md) · [Следующий →](Q-070-three-pods-provider-quota.md)
