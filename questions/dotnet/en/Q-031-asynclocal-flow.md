# Q-031 — Continuations and execution contexts

[Русский](../Q-031-asynclocal-flow.md) · [English](./Q-031-asynclocal-flow.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-031) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-030-cancellation-after-start.md) · [Next →](Q-032-configureawait-thread-id.md)

## Question

Does Task.Run print X or null?

## C# challenge — predict the outcome first

```csharp
var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() =>
{
    Console.Write(trace.Value);
});
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-031.cs
```

[Q-031.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-031.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

X. ExecutionContext normally flows into Task.Run, carrying AsyncLocal values across worker threads.

</details>

### Internal mechanism

ExecutionContext; AsyncLocal logical context flow.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[Русский](../Q-031-asynclocal-flow.md) · [English](./Q-031-asynclocal-flow.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-031) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-030-cancellation-after-start.md) · [Next →](Q-032-configureawait-thread-id.md)
