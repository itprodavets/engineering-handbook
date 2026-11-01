# Q-057 — Task composition and exceptions

[Русский](../Q-057-whenall-multiple-exceptions-await-one.md) · [English](./Q-057-whenall-multiple-exceptions-await-one.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-057) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-056-whenany-faulted-winner-exception.md) · [Next →](Q-058-whenall-faulted-priority-over-canceled.md)

## Question

How many InnerExceptions are stored for two faulted tasks, and what does await combined propagate?

## .NET / C# challenge — predict the outcome first

```csharp
Task combined=Task.WhenAll(first,second);
try { await combined; } catch { var all=combined.Exception!.InnerExceptions; }
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-057.cs
```

[Q-057.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-057.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Two stored inner exceptions for two single-fault input tasks. Awaiting combined propagates one of them rather than necessarily throwing AggregateException; all failures remain on combined.Exception.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](../Q-057-whenall-multiple-exceptions-await-one.md) · [English](./Q-057-whenall-multiple-exceptions-await-one.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-057) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-056-whenany-faulted-winner-exception.md) · [Next →](Q-058-whenall-faulted-priority-over-canceled.md)
