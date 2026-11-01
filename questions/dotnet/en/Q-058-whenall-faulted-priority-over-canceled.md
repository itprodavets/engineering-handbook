# Q-058 — Task composition and exceptions

[Русский](../Q-058-whenall-faulted-priority-over-canceled.md) · [English](./Q-058-whenall-faulted-priority-over-canceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-058) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-057-whenall-multiple-exceptions-await-one.md) · [Next →](Q-059-whenany-does-not-cancel-loser.md)

## Question

What status does WhenAll(Faulted,Canceled) have, and what does await propagate?

## .NET / C# challenge — predict the outcome first

```csharp
Task combined=Task.WhenAll(Task.FromException(new InvalidOperationException()),Task.FromCanceled(new CancellationToken(true)));
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-058.cs
```

[Q-058.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-058.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Faulted takes precedence over Canceled. Await propagates a fault exception; the canceled input remains Canceled and is not added as a fault to the aggregate.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](../Q-058-whenall-faulted-priority-over-canceled.md) · [English](./Q-058-whenall-faulted-priority-over-canceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-058) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-057-whenall-multiple-exceptions-await-one.md) · [Next →](Q-059-whenany-does-not-cancel-loser.md)
