# Q-065 — Shared memory and synchronization

[Русский](../Q-065-semaphore-permits-vs-threads.md) · [English](./Q-065-semaphore-permits-vs-threads.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-065) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-064-monitor-exit-after-await.md) · [Next →](Q-066-semaphore-nested-async-deadlock.md)

## Question

What does SemaphoreSlim(2,2) mean with two pending delays and two additional tasks?

## .NET / C# challenge — predict the outcome first

```csharp
await sem.WaitAsync();
try { await Task.Delay(1000); } finally { sem.Release(); }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-065.cs
```

[Q-065.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-065.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Two permits remain held until Release, with no dedicated blocked workers; further WaitAsync calls wait asynchronously.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](../Q-065-semaphore-permits-vs-threads.md) · [English](./Q-065-semaphore-permits-vs-threads.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-065) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-064-monitor-exit-after-await.md) · [Next →](Q-066-semaphore-nested-async-deadlock.md)
