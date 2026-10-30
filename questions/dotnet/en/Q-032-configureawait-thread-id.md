# Q-032 — Continuations and execution contexts

[Русский](../Q-032-configureawait-thread-id.md) · [English](./Q-032-configureawait-thread-id.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-032) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-031-asynclocal-flow.md) · [Next →](Q-033-startnew-nested-task.md)

## Question

Does awaiting CompletedTask.ConfigureAwait(false) change the managed thread ID?

## C# challenge — predict the outcome first

```csharp
int before = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(
    before == Environment.CurrentManagedThreadId);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-032.cs
```

[Q-032.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-032.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

True. The Task is already completed, so the await continues synchronously. ConfigureAwait(false) does not force a thread switch.

</details>

### Internal mechanism

Task awaiter; IsCompleted; SynchronizationContext (захват не нужен).

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Русский](../Q-032-configureawait-thread-id.md) · [English](./Q-032-configureawait-thread-id.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-032) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-031-asynclocal-flow.md) · [Next →](Q-033-startnew-nested-task.md)
