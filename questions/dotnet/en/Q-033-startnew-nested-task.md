# Q-033 — Task composition and exceptions

[Русский](../Q-033-startnew-nested-task.md) · [English](./Q-033-startnew-nested-task.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-033) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-032-configureawait-thread-id.md) · [Next →](Q-034-semaphore-waitasync.md)

## Question

What is the task type, and does awaiting outer once wait for the inner async operation?

## .NET / C# challenge — predict the outcome first

```csharp
Task<Task> outer = Task.Factory.StartNew<Task>(
    async () => await Task.Delay(100));

Task inner = await outer;
// The inner task may still be incomplete here.
await inner;
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-033.cs
```

[Q-033.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-033.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

StartNew(Func<Task>) yields Task<Task>. Awaiting the outer task returns the inner task and does not guarantee its completion. Await inner or use Unwrap().

</details>

### Internal mechanism

Generic Task<TResult>; nested await; compiler async lambda.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap)

---

[Русский](../Q-033-startnew-nested-task.md) · [English](./Q-033-startnew-nested-task.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-033) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-032-configureawait-thread-id.md) · [Next →](Q-034-semaphore-waitasync.md)
