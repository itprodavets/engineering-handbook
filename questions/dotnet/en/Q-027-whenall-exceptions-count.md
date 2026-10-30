# Q-027 — Task composition and exceptions

[Русский](../Q-027-whenall-exceptions-count.md) · [English](./Q-027-whenall-exceptions-count.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-027) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-026-whenany-faulted-output.md) · [Next →](Q-028-lost-update-race.md)

## Question

How many exceptions are stored by WhenAll when two input Tasks fault?

## .NET / C# challenge — predict the outcome first

```csharp
var all = Task.WhenAll(
    Task.FromException(
        new InvalidOperationException("A")),
    Task.FromException(
        new ArgumentException("B")));
try
{
    await all;
}
catch (Exception)
{
    Console.WriteLine(all.Exception!.InnerExceptions.Count);
}
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-027.cs
```

[Q-027.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-027.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

2. WhenAll stores both failures in its aggregate Exception. A regular await rethrows one exception; inspect the Task for all failures.

</details>

### Internal mechanism

Task Exception property; AggregateException; awaiter GetResult.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)

---

[Русский](../Q-027-whenall-exceptions-count.md) · [English](./Q-027-whenall-exceptions-count.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-027) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-026-whenany-faulted-output.md) · [Next →](Q-028-lost-update-race.md)
