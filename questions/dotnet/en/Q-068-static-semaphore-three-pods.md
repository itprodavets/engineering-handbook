# Q-068 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-068-static-semaphore-three-pods.md) · [English](./Q-068-static-semaphore-three-pods.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-068) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-067-semaphore-canceled-wait-overrelease.md) · [Next →](Q-069-network-await-permit-lifetime.md)

## Question

Does static SemaphoreSlim(1,1) protect a last-item SKU across three Pods?

## .NET / C# challenge — predict the outcome first

```csharp
private static readonly SemaphoreSlim Gate=new(1,1);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-068.cs
```

[Q-068.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-068.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No: each Pod has its own permit; InventoryService/PostgreSQL must enforce stock.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](../Q-068-static-semaphore-three-pods.md) · [English](./Q-068-static-semaphore-three-pods.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-068) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-067-semaphore-canceled-wait-overrelease.md) · [Next →](Q-069-network-await-permit-lifetime.md)
