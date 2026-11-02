# Q-066 — Shared memory and synchronization

[Русский](../Q-066-semaphore-nested-async-deadlock.md) · [English](./Q-066-semaphore-nested-async-deadlock.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-066) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-065-semaphore-permits-vs-threads.md) · [Next →](Q-067-semaphore-canceled-wait-overrelease.md)

## Question

What if Outer holds SemaphoreSlim(1,1) and awaits Inner, which also awaits it?

## .NET / C# challenge — predict the outcome first

```csharp
await gate.WaitAsync();
try { await InnerAsync(); } finally { gate.Release(); }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-066.cs
```

[Q-066.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-066.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Only Outer entered; Inner cannot acquire the permit and Outer cannot release it until Inner completes. Async deadlocks need not block workers.

</details>

### Documentation and source

[https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/](https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/)

---

[Русский](../Q-066-semaphore-nested-async-deadlock.md) · [English](./Q-066-semaphore-nested-async-deadlock.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-066) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-065-semaphore-permits-vs-threads.md) · [Next →](Q-067-semaphore-canceled-wait-overrelease.md)
