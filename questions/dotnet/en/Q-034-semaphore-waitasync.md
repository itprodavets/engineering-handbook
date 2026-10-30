# Q-034 — Shared memory and synchronization

[Русский](../Q-034-semaphore-waitasync.md) · [English](./Q-034-semaphore-waitasync.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-034) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-033-startnew-nested-task.md) · [Next →](Q-035-parallel-foreach-async-void.md)

## Question

What does second.IsCompleted print after another WaitAsync without Release?

## C# challenge — predict the outcome first

```csharp
using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();

Task second = semaphore.WaitAsync();
Console.WriteLine(second.IsCompleted);

semaphore.Release();
await second;
semaphore.Release();
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-034.cs
```

[Q-034.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-034.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

False. The first Wait reduces the count to zero, so the second WaitAsync is pending. Awaiting the second before Release would deadlock this flow.

</details>

### Internal mechanism

SemaphoreSlim count, task waiter, asynchronous queue.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[Русский](../Q-034-semaphore-waitasync.md) · [English](./Q-034-semaphore-waitasync.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-034) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-033-startnew-nested-task.md) · [Next →](Q-035-parallel-foreach-async-void.md)
