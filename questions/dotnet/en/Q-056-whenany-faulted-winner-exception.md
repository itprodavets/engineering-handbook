# Q-056 — Task composition and exceptions

[Русский](../Q-056-whenany-faulted-winner-exception.md) · [English](./Q-056-whenany-faulted-winner-exception.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-056) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-055-whenany-winner-vs-continuation-time.md) · [Next →](Q-057-whenall-multiple-exceptions-await-one.md)

## Question

Does awaiting WhenAny throw the winner's exception? What does awaiting the returned Task do?

## .NET / C# challenge — predict the outcome first

```csharp
Task completed=await Task.WhenAny(failed,Task.Delay(100));
await completed; // propagates winner's exception
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-056.cs
```

[Q-056.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-056.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

The outer Task<Task> completes successfully and returns the winner. Await the winner to propagate its fault, or inspect its status/Exception explicitly.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)

---

[Русский](../Q-056-whenany-faulted-winner-exception.md) · [English](./Q-056-whenany-faulted-winner-exception.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-056) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-055-whenany-winner-vs-continuation-time.md) · [Next →](Q-057-whenall-multiple-exceptions-await-one.md)
