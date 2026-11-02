# Q-067 — Shared memory and synchronization

[Русский](../Q-067-semaphore-canceled-wait-overrelease.md) · [English](./Q-067-semaphore-canceled-wait-overrelease.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-067) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-066-semaphore-nested-async-deadlock.md) · [Next →](Q-068-static-semaphore-three-pods.md)

## Question

Why can finally Release after a canceled WaitAsync corrupt the count?

## .NET / C# challenge — predict the outcome first

```csharp
try { await sem.WaitAsync(ct); } finally { sem.Release(); }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-67.cs
```

[Q-67.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-67.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Canceled wait acquired no permit; unconditional finally Release corrupts the count. Acquire before try/finally.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](../Q-067-semaphore-canceled-wait-overrelease.md) · [English](./Q-067-semaphore-canceled-wait-overrelease.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-067) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-066-semaphore-nested-async-deadlock.md) · [Next →](Q-068-static-semaphore-three-pods.md)
