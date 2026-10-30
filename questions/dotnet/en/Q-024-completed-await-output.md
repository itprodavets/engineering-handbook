# Q-024 — The async/await execution lifecycle

[Русский](../Q-024-completed-await-output.md) · [English](./Q-024-completed-await-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-024) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-023-asynclocal-executioncontext.md) · [Next →](Q-025-incomplete-await-output.md)

## Question

What is the output and why? The awaited Task is already complete.

## .NET / C# challenge — predict the outcome first

```csharp
async Task PrintAsync()
{
    Console.Write("A");
    await Task.CompletedTask;
    Console.Write("B");
}
var task = PrintAsync();
Console.Write("C");
await task;
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

[Q-024.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-024.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

ABC. The awaited Task is already complete, so the method continues synchronously and prints B before the caller prints C.

</details>

### Internal mechanism

Roslyn state machine; IsCompleted = true; без обязательного ThreadPool worker.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs)

---

[Русский](../Q-024-completed-await-output.md) · [English](./Q-024-completed-await-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-024) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-023-asynclocal-executioncontext.md) · [Next →](Q-025-incomplete-await-output.md)
