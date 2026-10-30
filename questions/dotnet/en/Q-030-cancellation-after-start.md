# Q-030 — Cancellation of asynchronous work

[Русский](../Q-030-cancellation-after-start.md) · [English](./Q-030-cancellation-after-start.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-030) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-029-lock-new-object.md) · [Next →](Q-031-asynclocal-flow.md)

## Question

Will the program print DONE when the token is canceled after the delegate starts?

## C# challenge — predict the outcome first

```csharp
using var cts = new CancellationTokenSource();
var started = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
var release = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

var task = Task.Run(async () =>
{
    started.SetResult();
    await release.Task;
    Console.Write("DONE");
}, cts.Token);

await started.Task;
cts.Cancel();
release.SetResult();
await task;
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-030.cs
```

[Q-030.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-030.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

DONE. Task.Run's token can prevent the delegate from starting, but cannot forcibly stop it after execution has begun. The body never checks the token.

</details>

### Internal mechanism

CancellationToken; Task.Run proxy; await continuation.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.run](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.run)

---

[Русский](../Q-030-cancellation-after-start.md) · [English](./Q-030-cancellation-after-start.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-030) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-029-lock-new-object.md) · [Next →](Q-031-asynclocal-flow.md)
