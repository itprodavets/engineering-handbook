# Q-055 — Task composition and exceptions

[Русский](../Q-055-whenany-winner-vs-continuation-time.md) · [English](./Q-055-whenany-winner-vs-continuation-time.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-055) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-054-task-delay-is-not-synchronization.md) · [Next →](Q-056-whenany-faulted-winner-exception.md)

## Question

If Task.Delay wins WhenAny, must producer still be incomplete when the continuation executes?

## .NET / C# challenge — predict the outcome first

```csharp
Task winner=await Task.WhenAny(producer,Task.Delay(100));
// winner == timeout does not prove producer still pending now
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-055.cs
```

[Q-055.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-055.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Winner denotes the first completed Task, but the loser can complete before the caller resumes. Inspect winner identity; the timer does not cancel producer.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](../Q-055-whenany-winner-vs-continuation-time.md) · [English](./Q-055-whenany-winner-vs-continuation-time.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-055) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-054-task-delay-is-not-synchronization.md) · [Next →](Q-056-whenany-faulted-winner-exception.md)
