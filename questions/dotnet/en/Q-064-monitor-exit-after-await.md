# Q-064 — Shared memory and synchronization

[Русский](../Q-064-monitor-exit-after-await.md) · [English](./Q-064-monitor-exit-after-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-064) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-063-async-task-throws-after-completed-await.md) · [Next →](Q-065-semaphore-permits-vs-threads.md)

## Question

Why does Monitor.Exit after await on another thread throw?

## .NET / C# challenge — predict the outcome first

```csharp
Monitor.Enter(gate);
try { await Task.Delay(100); } finally { Monitor.Exit(gate); }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-064.cs
```

[Q-064.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-064.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Monitor has thread affinity; Exit on another thread throws SynchronizationLockException. await does not release it.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit)

---

[Русский](../Q-064-monitor-exit-after-await.md) · [English](./Q-064-monitor-exit-after-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-064) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-063-async-task-throws-after-completed-await.md) · [Next →](Q-065-semaphore-permits-vs-threads.md)
