# Q-025 — The async/await execution lifecycle

[Русский](../Q-025-incomplete-await-output.md) · [English](./Q-025-incomplete-await-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-025) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-024-completed-await-output.md) · [Next →](Q-026-whenany-faulted-output.md)

## Question

What is the output? The method awaits an incomplete TaskCompletionSource.

## .NET / C# challenge — predict the outcome first

```csharp
var gate = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

async Task PrintAsync()
{
    Console.Write("A");
    await gate.Task;
    Console.Write("B");
}
var task = PrintAsync();
Console.Write("C");
gate.SetResult();
await task;
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-025.cs
```

[Q-025.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-025.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

ACB. The method prints A and suspends; the caller prints C, then SetResult allows the continuation to print B.

</details>

### Internal mechanism

Async state machine; continuation; RunContinuationsAsynchronously; нет thread-per-wait.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Русский](../Q-025-incomplete-await-output.md) · [English](./Q-025-incomplete-await-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-025) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-024-completed-await-output.md) · [Next →](Q-026-whenany-faulted-output.md)
