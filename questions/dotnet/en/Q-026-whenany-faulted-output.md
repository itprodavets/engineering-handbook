# Q-026 — Task composition and exceptions

[Русский](../Q-026-whenany-faulted-output.md) · [English](./Q-026-whenany-faulted-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-026) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-025-incomplete-await-output.md) · [Next →](Q-027-whenall-exceptions-count.md)

## Question

What does it print, and does awaiting WhenAny throw the winning task's exception?

## .NET / C# challenge — predict the outcome first

```csharp
var failed = Task.FromException(
    new InvalidOperationException("boom"));
var winner = await Task.WhenAny(
    failed, Task.Delay(Timeout.Infinite));
Console.WriteLine(winner.IsFaulted);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-026.cs
```

[Q-026.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-026.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

True. WhenAny completes with the faulted winner but does not throw its exception; awaiting winner would rethrow it.

</details>

### Internal mechanism

Task<Task>; статус Faulted у winner, RanToCompletion у WhenAny.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany)

---

[Русский](../Q-026-whenany-faulted-output.md) · [English](./Q-026-whenany-faulted-output.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-026) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-025-incomplete-await-output.md) · [Next →](Q-027-whenall-exceptions-count.md)
