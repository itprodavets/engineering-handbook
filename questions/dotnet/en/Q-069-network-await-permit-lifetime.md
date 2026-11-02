# Q-069 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-069-network-await-permit-lifetime.md) · [English](./Q-069-network-await-permit-lifetime.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-069) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-068-static-semaphore-three-pods.md) · [Next →](Q-070-three-pods-provider-quota.md)

## Question

During a five-second await ChargeAsync, does CheckoutAsync hold a worker or a permit?

## .NET / C# challenge — predict the outcome first

```csharp
await gate.WaitAsync();
try { await ChargeAsync(); } finally { gate.Release(); }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-069.cs
```

[Q-069.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-069.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Proper pending async I/O does not pin a worker, but holds a Gate permit until finally Release.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](../Q-069-network-await-permit-lifetime.md) · [English](./Q-069-network-await-permit-lifetime.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-069) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-068-static-semaphore-three-pods.md) · [Next →](Q-070-three-pods-provider-quota.md)
