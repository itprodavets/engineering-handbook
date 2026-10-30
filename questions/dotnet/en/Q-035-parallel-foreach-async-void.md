# Q-035 — Shared memory and synchronization

[Русский](../Q-035-parallel-foreach-async-void.md) · [English](./Q-035-parallel-foreach-async-void.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-035) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-034-semaphore-waitasync.md)

## Question

Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed?

## .NET / C# challenge — predict the outcome first

```csharp
var gate = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Parallel.ForEach(new[] { 1, 2, 3 }, async _ =>
{
    await gate.Task;
    Console.Write("X");
});
Console.Write("A");
gate.SetResult();
// X may print later, or the program may exit.
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-035.cs
```

[Q-035.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-035.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

The lambda becomes async void because Parallel.ForEach accepts Action<T>. The loop returns after delegates yield at await and does not await their continuations. Use Parallel.ForEachAsync or WhenAll.

</details>

### Internal mechanism

async void; Action<T>; compiler state machine; ThreadPool continuation.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs)

---

[Русский](../Q-035-parallel-foreach-async-void.md) · [English](./Q-035-parallel-foreach-async-void.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-035) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-034-semaphore-waitasync.md)
