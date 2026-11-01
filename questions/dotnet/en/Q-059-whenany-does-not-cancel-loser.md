# Q-059 — Task composition and exceptions

[Русский](../Q-059-whenany-does-not-cancel-loser.md) · [English](./Q-059-whenany-does-not-cancel-loser.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-059) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-058-whenall-faulted-priority-over-canceled.md) · [Next →](Q-060-whenall-waits-not-fail-fast.md)

## Question

Does WhenAny cancel losing tasks and what happens to them?

## .NET / C# challenge — predict the outcome first

```csharp
Task winner=await Task.WhenAny(producer,Task.Delay(100));
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-059.cs
```

[Q-059.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-059.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No, losers continue running. Timeout is a caller-side decision, not automatic cancellation. Cooperatively cancel and observe faults/cleanup as appropriate.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](../Q-059-whenany-does-not-cancel-loser.md) · [English](./Q-059-whenany-does-not-cancel-loser.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-059) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-058-whenall-faulted-priority-over-canceled.md) · [Next →](Q-060-whenall-waits-not-fail-fast.md)
